"""Recorded resource accounting only; no scientific imports or execution."""
from pathlib import Path
from copy import deepcopy
import gzip, hashlib, json

ROOT = Path(__file__).resolve().parent

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def semantic(cert):
    out = deepcopy(cert)
    out['actual_integer_evidence']['arithmetic_stats']['native_kernel_calls_delta'] = 0
    return out

def costs(evidences):
    rows = list(evidences)
    keys = ('typed_operations', 'adder_digit_replays', 'host_bit_wiring_operations',
            'host_bit_length_calls_in_arithmetic', 'native_kernel_calls_delta')
    for row in rows:
        assert len(row['arithmetic_operations']) == row['arithmetic_stats']['typed_operations']
        indices = [i for op in row['signed_operations'] for i in op['typed_operation_indices']]
        assert len(indices) == len(set(indices))
        assert set(indices) == set(range(len(row['arithmetic_operations'])))
        assert not row['window_weight_queries']
    return {'evidence_count': len(rows),
        'arithmetic_totals': {k: sum(row['arithmetic_stats'][k] for row in rows) for k in keys},
        'signed_operations': sum(len(row['signed_operations']) for row in rows),
        'moment_nodes': sum(len(row['moment_nodes']) for row in rows),
        'moment_requests': sum(row['stats']['moment_requests'] for row in rows),
        'cache_hits': sum(row['stats']['cache_hits'] for row in rows),
        'max_recursion_depth': max((row['stats']['max_recursion_depth'] for row in rows), default=0),
        'max_observed_integer_bits': max((row['stats']['max_observed_integer_bits'] for row in rows), default=0)}

def main():
    compressed = (ROOT/'DIRECT_RESULTS.json.gz').read_bytes()
    raw = gzip.decompress(compressed)
    assert sha(compressed) == '3ac0ebc17112afb9f068e39c1ebb91afd8f6e3f6aeb3d6cd46044d0733b26354'
    assert sha(raw) == '48780f175bc4bcf673345ee8c0b9e0240cc1c2a0e166037720c5fc06b8483157'
    data = json.loads(raw)
    summary = json.loads((ROOT/'DIRECT_SUMMARY.json').read_bytes())
    assert data['status'] == summary['status'] == 'PASS'
    for name, expected in summary['source_sha256'].items():
        assert sha((ROOT/name).read_bytes()) == expected == data['source_sha256'][name]
    assert sha((ROOT.parent/'DIFFERENCE_AUTOCORRELATION.md').read_bytes()) == data['direct_proof_sha256']
    assert sha((ROOT.parent/'STARTUP_GUARD.json').read_bytes()) == data['startup_guard']['sha256']
    cases = data['cases']
    for case in cases:
        assert semantic(case['certificate']) == semantic(case['verification']['replay_certificate'])
        assert case['values'] == case['history_reference']['values']
        assert case['values'] == [x['value'] for x in case['certificate']['requests']]
    fields = {
        'production': costs(c['certificate']['actual_integer_evidence'] for c in cases),
        'positive_replay': costs(c['verification']['replay_certificate']['actual_integer_evidence'] for c in cases),
        'negative_replay': costs(c['actual_integer_evidence'] for row in data['negative_checks']
                                 for c in row['actual_replay_certificates'])}
    for key, name in [('production','fresh_production_adder_digit_replays'),
                      ('positive_replay','positive_replay_adder_digit_replays'),
                      ('negative_replay','negative_replay_adder_digit_replays')]:
        assert fields[key]['arithmetic_totals']['adder_digit_replays'] == summary[name]
    assert len(data['actual_core_calls']) == summary['actual_core_call_count'] == 1
    assert sum(v['arithmetic_totals']['native_kernel_calls_delta'] for v in fields.values()) == 1
    out = {'status':'FULL_SAVED_COST_READBACK_PASS', 'scientific_execution_performed':False,
        'reader_sha256':sha(Path(__file__).read_bytes()), 'source_sha256':summary['source_sha256'],
        'payload_sha256':sha(raw), 'artifact_sha256':sha(compressed),
        'raw_bytes':len(raw), 'gzip_bytes':len(compressed), **fields,
        'per_case':summary['per_case'], 'top_level_table_calls':summary['top_level_table_calls'],
        'empty_progressions':summary['empty_progressions'],
        'negative_replay_counts':[{'name':r['name'], 'count':len(r['actual_replay_certificates'])}
                                  for r in data['negative_checks']],
        'actual_core_calls':data['actual_core_calls'],
        'all_signed_to_typed_operation_indices_covered_once':True,
        'positive_complete_semantic_equality_checked':True,
        'log_sha256':sha((ROOT/'DIRECT_EXECUTION_LOG.txt').read_bytes()),
        'failure_artifact_present':(ROOT/'DIRECT_FAILED_EXECUTION.json.gz').exists(),
        'scope':'Resource accounting on saved evidence; no historical or new science rerun.'}
    with (ROOT/'DIRECT_COST_READBACK.json').open('x',encoding='utf-8') as stream:
        stream.write(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('actual_core_calls','per_case')}))

if __name__ == '__main__':
    main()
