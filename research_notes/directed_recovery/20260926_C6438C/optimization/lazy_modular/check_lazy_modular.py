"""Actual small-domain comparison and large-domain demand-only validation."""
from pathlib import Path
from copy import deepcopy
import gzip
import hashlib
import json
import lazy_modular as lazy
from stage45.brc_loop_recheck import CALLS

ROOT = Path(__file__).resolve().parent


def rejected(name, action):
    try:
        action()
    except (ValueError, TypeError, OverflowError) as exc:
        return {'case': name, 'rejected': True, 'reason': str(exc)}
    raise AssertionError(name+' was not rejected')


def main():
    start = len(CALLS)
    small, large, negatives, power_cases = [], [], [], []
    for N, b in [(2,1),(3,2),(5,2),(9,2),(15,2),(15,14),
                 (21,2),(21,5),(35,2),(35,6),(55,2)]:
        table = lazy.LazyModularColumns(N, b)
        verify = lazy.verify_lazy_permutation(table)
        assert table.stats['computed_columns'] == 0
        old, old_certificate = lazy.sparse.compile_modular_permutation(N, b)
        inverse = table.inverse()
        rows = []
        for y in range(table.carrier_size):
            actual = table[y]
            assert actual == old[y]
            assert inverse[actual] == y
            rows.append({'source':y, 'target':actual, 'old_actual_target':old[y],
                         'inverse_target':y})
        cached = table.report_metrics()
        again = table[1]
        assert again == b and table.stats['computed_columns'] == cached['computed_columns']
        assert table.stats['cache_hits'] == cached['cache_hits'] + 1
        vectors = {0:(1,-2,3,0), 1:(-5,7,0,11)}
        transported = table.transport_sparse(vectors)
        assert inverse.transport_sparse(transported) == vectors
        dense = old.native_dense_check() if N == 5 else None
        small.append({'N':N,'b':b,'verified':verify,'all_columns':rows,
                      'old_certificate_sha256':lazy.digest(old_certificate),
                      'old_resource_counts':old_certificate['resource_counts'],
                      'bounded_actual_dense_check':dense,
                      'all_signed_rows_retained':True,
                      'forward':table.export_certificate(),'inverse':inverse.export_certificate()})
        print(json.dumps({'small_N':N,'b':b,'columns':len(rows),'passed':True}),flush=True)

    # Each domain is astronomically larger than the seven explicit requests.
    # These inputs need no primality claim: odd N makes multiplier 2 a unit.
    for N in [(1<<127)-1, (1<<255)+19]:
        table = lazy.LazyModularColumns(N,2)
        proof = lazy.verify_lazy_permutation(table)
        inverse = table.inverse()
        sources = list(dict.fromkeys([0,1,3,N>>1,N-1,N,table.carrier_size-1]))
        rows = []
        for y in sources:
            target = table[y]
            recovered = inverse[target]
            assert recovered == y
            if y >= N:
                assert target == y
            rows.append({'source':y,'target':target,'inverse_target':recovered})
        assert table.stats['computed_columns'] == len(sources)
        assert inverse.stats['computed_columns'] == len(sources)
        columns_before = table.stats['computed_columns']
        digits_before = table.stats['column_adder_digit_replays']
        table[sources[-1]]
        assert table.stats['computed_columns'] == columns_before
        assert table.stats['column_adder_digit_replays'] == digits_before
        large.append({'width':table.width,'N':N,'b':2,'carrier_size':table.carrier_size,
                      'explicitly_requested_columns':len(sources),'verification':proof,
                      'rows':rows,'forward':table.export_certificate(),
                      'inverse':inverse.export_certificate()})
        print(json.dumps({'large_width':table.width,'requested_columns':len(sources),
                          'digit_replays':table.stats['column_adder_digit_replays'],
                          'passed':True}),flush=True)

    for N,a,e in [(15,2,0),(15,2,9),(21,2,6),(35,2,12),(55,2,20)]:
        trace = lazy.lazy_modular_power_trace(N,a,e)
        old = lazy.sparse.sparse_modular_power_trace(N,a,e)
        assert trace['value'] == old['value']
        power_cases.append({'case':[N,a,e], 'old_actual_trace':old,'lazy_trace':trace,
                            'equal':True})
    chain = lazy.lazy_modular_power_chain(21,2,6)
    old_chain = lazy.sparse.sparse_modular_power_chain(21,2,6)
    assert chain[0] == old_chain[0]
    assert tuple(r['square_target'] for r in chain[2]) == tuple(r['square_target'] for r in old_chain[2])

    table = lazy.LazyModularColumns(15,2)
    negatives.append(rejected('implicit_full_iteration', lambda: iter(table)))
    negatives.append(rejected('nonunit_multiplier', lambda: lazy.LazyModularColumns(15,5)))
    negatives.append(rejected('out_of_carrier', lambda: table[table.carrier_size]))
    huge = lazy.LazyModularColumns((1<<127)-1,2)
    negatives.append(rejected('python_len_cannot_encode_large_domain', lambda: len(huge)))
    bad = table.column_certificate(1)
    bad['target'] = 3
    negatives.append(rejected('changed_column_target', lambda: lazy.verify_column_certificate(bad,table)))
    original = deepcopy(table.permutation_certificate)
    table.permutation_certificate['inverse_certificate']['inverse_multiplier'] = 7
    negatives.append(rejected('changed_inverse_proof', lambda: lazy.verify_lazy_permutation(table)))
    table.permutation_certificate = original
    verified_column = lazy.verify_column_certificate(table.column_certificate(3),table)

    result = {'schema':'BRC_LAZY_MODULAR_CHECKS_V1',
              'activity':'RA-CAAAC604CB513AEA8BBC1DFC',
              'status':'AUTHOR_ACTUAL_BOUNDED_SHARED_CONTEXT_NOT_ADMITTED',
              'source':lazy.source_binding(),'small_cases':small,'large_cases':large,
              'power_cases':power_cases,'chain_case':{'N':21,'a':2,'t':6,
                  'powers':chain[0],'origins':chain[2],'equal_old_actual':True},
              'negative_controls':negatives,'one_column_replay':verified_column,
              'native_core_call_count':len(CALLS)-start,'native_core_calls':CALLS[start:],
              'ordinary_modular_reference_used':False,
              'scope':'actual full-adder arithmetic and permutation transport; no Shor measurement execution'}
    raw = json.dumps(result,sort_keys=True,separators=(',',':')).encode()
    (ROOT/'LAZY_MODULAR_RESULTS.json.gz').write_bytes(gzip.compress(raw,mtime=0))
    summary = {'status':result['status'],'small_cases':len(small),
        'small_complete_columns':sum(len(case['all_columns']) for case in small),
        'large_cases':[{k:v for k,v in case.items() if k in (
            'width','N','carrier_size','explicitly_requested_columns')} |
            {'forward_metrics':case['forward']['stats'],'inverse_metrics':case['inverse']['stats']}
            for case in large],
        'power_cases':len(power_cases),'chain_equal':True,
        'negative_controls':negatives,'native_core_call_count':len(CALLS)-start,
        'ordinary_modular_reference_used':False,
        'payload_sha256':hashlib.sha256(raw).hexdigest(),'uncompressed_bytes':len(raw),
        'source':result['source']}
    (ROOT/'LAZY_MODULAR_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASSED','small_cases':len(small),'large_cases':len(large),
        'payload_sha256':summary['payload_sha256'],'bytes':len(raw),'core_calls':len(CALLS)-start}),flush=True)


if __name__ == '__main__':
    main()
