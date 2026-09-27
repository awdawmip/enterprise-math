"""Bounded actual typed order discovery and strict serialization replay."""
from pathlib import Path
from copy import deepcopy
import gzip
import hashlib
import json
from time import perf_counter

from typed_odd_part import (discover_odd_part, verify_odd_part_certificate,
    OddPartDiscoveryError, source_hashes)
from lazy_modular import LazyModularFactory, verify_lazy_permutation
from stage45.brc_loop_recheck import CALLS, verify_vendor

ROOT = Path(__file__).resolve().parent


def packed(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()


def consecutive_reference(N, b, limit):
    """Paid actual typed first return, with no supplied true-order constant."""
    start = len(CALLS)
    factory = LazyModularFactory()
    table = factory(N, b)
    replay = verify_lazy_permutation(table)
    states, R = [1], None
    for exponent in range(1, limit+1):
        states.append(table[states[-1]])
        if states[-1] == 1:
            R = exponent
            break
    instances = factory.export_certificate()
    stats = table.stats
    return {'N': N, 'b': b, 'limit': limit,
        'status': 'CERTIFIED' if R is not None else 'PARTIAL', 'R': R,
        'states': states, 'table_instances': instances, 'permutation_replay': replay,
        'metrics': {'column_requests': stats['column_requests'],
            'total_adder_digit_replays': stats['setup_adder_digit_replays']+
                stats['column_adder_digit_replays']+replay['replayed_adder_digits'],
            'actual_native_core_calls_delta': len(CALLS)-start}}


def main():
    first, started = len(CALLS), perf_counter()
    startup = json.loads((ROOT.parent/'STARTUP_GUARD.json').read_bytes())
    assert startup['activity_allowed'] and startup['persistence_allowed'] and not startup['sync_debt_events']
    policy = json.loads((ROOT/'POLICY_READBACK.json').read_bytes())
    assert policy['canonical'] == '06788df022dbd11720132b4ed0882ce8e41b3b8a'
    assert 'ACTUAL_TYPED_BRC_ONLY' in policy['machine']['content']
    before = {**source_hashes(), 'check_odd_part.py': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    vendor = verify_vendor()
    cases, replays, negatives = [], [], []
    # Declared input fixtures; no expected order is passed to the discovery.
    for N, b, Q in ((2,1,1), (17,3,1), (97,5,3), (21,2,3), (21,4,3), (65,3,3)):
        actual = discover_odd_part(N, b, Q)
        reference = consecutive_reference(N, b, N-1)
        assert actual['status'] == reference['status'] == 'CERTIFIED'
        assert actual['R'] == reference['R']
        serialized = json.loads(packed(actual))
        replay = verify_odd_part_certificate(serialized)
        assert replay['verified'] and replay['replay']['R'] == actual['R']
        cases.append({'N': N, 'b': b, 'Q': Q, 'actual': actual,
                      'reference': reference, 'exact_order_equal': True})
        replays.append(replay)
        print(json.dumps({'N':N, 'b':b, 'status':actual['status'],
                          'q':actual['q'], 's':actual['s'], 'R':actual['R']}), flush=True)
    assert cases[1]['actual']['q'] == 1 and cases[1]['actual']['s'] >= 4
    assert cases[2]['actual']['s'] >= 4 and cases[2]['actual']['q'] > 1
    assert cases[0]['actual']['s'] == 0 and cases[4]['actual']['s'] == 0
    partials = []
    for N,b,Q in ((97,5,2), (17,3,0)):
        actual = discover_odd_part(N,b,Q)
        assert actual['status'] == 'PARTIAL'
        assert actual['q'] is actual['s'] is actual['R'] is None
        assert len(actual['evidence']['odd_first_return_chain']) == Q
        replay = verify_odd_part_certificate(json.loads(packed(actual)))
        assert replay['verified'] and replay['replay']['status'] == 'PARTIAL'
        partials.append({'actual': actual, 'replay': replay})
    for name, N, b, Q in (
        ('small_modulus',1,1,1), ('boolean_modulus',True,1,1),
        ('zero_base',21,0,3), ('noncanonical_base',21,21,3),
        ('boolean_base',21,True,3), ('nonunit_full_failed_gcd',21,3,3),
        ('negative_budget',21,2,-1), ('boolean_budget',21,2,True),
        ('string_budget',21,2,'3')):
        try:
            discover_odd_part(N,b,Q)
        except OddPartDiscoveryError as error:
            negatives.append({'name':name, 'rejected':True, 'message':str(error),
                              'evidence':error.evidence, 'metrics':error.metrics})
        else:
            raise AssertionError('invalid input accepted: '+name)
    original = cases[2]['actual']
    for name in ('wrong_q', 'wrong_s', 'wrong_R', 'boolean_R',
                 'changed_squaring', 'changed_first_return', 'missing_table',
                 'wrong_source', 'underreported_cost', 'partial_promoted'):
        changed = deepcopy(original)
        if name == 'wrong_q': changed['q'] = 1
        elif name == 'wrong_s': changed['s'] = 0
        elif name == 'wrong_R': changed['R'] = 1
        elif name == 'boolean_R': changed['R'] = True
        elif name == 'changed_squaring': changed['evidence']['c_squaring_chain'][0]['target'] = 1
        elif name == 'changed_first_return': changed['evidence']['odd_first_return_chain'][-1]['target'] = 2
        elif name == 'missing_table': changed['evidence']['table_instances'].pop()
        elif name == 'wrong_source': changed['evidence']['source_sha256']['typed_odd_part.py'] = '0'*64
        elif name == 'underreported_cost': changed['metrics']['total_adder_digit_replays'] = 0
        elif name == 'partial_promoted':
            changed = deepcopy(partials[0]['actual'])
            changed.update(status='CERTIFIED', q=original['q'], s=original['s'], R=original['R'])
        try:
            verify_odd_part_certificate(changed)
        except ValueError as error:
            negatives.append({'name':name, 'rejected':True, 'message':str(error),
                              'evidence':getattr(error,'evidence', {'attempt':changed})})
        else:
            raise AssertionError('forged certificate accepted: '+name)
    malformed = deepcopy(original)
    malformed[1] = 'ambiguous key'
    try:
        verify_odd_part_certificate(malformed)
    except ValueError as error:
        negatives.append({'name':'non_json_dictionary_key', 'rejected':True, 'message':str(error),
            'attempt_description':{'original_case':2, 'additional_key_type':'int', 'additional_key':1,
                                   'additional_value':'ambiguous key'},
            'no_scientific_replay_due_to_schema_rejection':True})
    else:
        raise AssertionError('non-JSON dictionary key accepted')
    after = {**source_hashes(), 'check_odd_part.py': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    assert before == after
    payload = {'schema':'BRC_SMALL_ODD_PART_DISCOVERY_CHECKS_V1',
        'status':'AUTHOR_ACTUAL_TYPED_BOUNDED_SHARED_CONTEXT_NOT_ADMITTED',
        'source_sha256':before, 'source_unchanged_during_execution':True,
        'startup_guard':startup, 'policy_canonical':policy['canonical'], 'vendor':vendor,
        'cases':cases, 'positive_serialized_replays':replays,
        'partial_cases':partials, 'negative_controls':negatives,
        'native_core_call_receipts':CALLS[first:], 'actual_native_core_calls':len(CALLS)-first,
        'elapsed_seconds':perf_counter()-started,
        'reference_scope':'bounded actual typed first-return enumeration; no ordinary modular pow/mod/gcd or ideal phase reference',
        'complexity_claim':'O(n+Q+log(q)) modular column requests plus n recovery squares, paid setup/replay and bit/receipt costs; no polylog(Q) claim'}
    raw = packed(payload)
    target = ROOT/'ODD_PART_RESULTS.json.gz'
    target.write_bytes(gzip.compress(raw, compresslevel=9,mtime=0))
    assert gzip.decompress(target.read_bytes()) == raw
    summary = {k:payload[k] for k in ('status','source_sha256','actual_native_core_calls','elapsed_seconds')}
    summary.update(certified_cases=len(cases),partial_cases=len(partials),negative_controls_rejected=len(negatives),
        payload_bytes=len(raw),payload_sha256=hashlib.sha256(raw).hexdigest(),
        gzip_bytes=target.stat().st_size,gzip_sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
        case_summary=[{'N':c['N'],'b':c['b'],'Q':c['Q'],'q':c['actual']['q'],
            's':c['actual']['s'],'R':c['actual']['R'],'metrics':c['actual']['metrics'],
            'consecutive_reference_metrics':c['reference']['metrics']} for c in cases],
        partial_summary=[{'inputs':p['actual']['inputs'],'metrics':p['actual']['metrics']} for p in partials])
    (ROOT/'ODD_PART_SUMMARY.json').write_bytes(packed(summary)+b'\n')
    print(json.dumps(summary),flush=True)


if __name__ == '__main__':
    main()
