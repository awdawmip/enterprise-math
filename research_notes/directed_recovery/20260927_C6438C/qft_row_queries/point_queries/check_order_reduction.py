from pathlib import Path
import gzip
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
PREVIOUS = ROOT.parents[1]/'sep26-shor-general'
sys.path.insert(0, str(ROOT.parent/'gram_research'))
sys.path.insert(0, str(PREVIOUS/'phases'))
from order_from_zero_prefix import order_from_row_oracle
from checkpoint_row_oracle import CheckpointRowOracle
from check_single_walker import LazyStreamingProgram, serializable, packed, CALLS, verify_vendor
from closed_phase_bank import load_certified_bank


def main():
    sources = [Path(__file__), ROOT/'order_from_zero_prefix.py', ROOT/'checkpoint_row_oracle.py',
               ROOT.parent/'gram_research/single_walker.py']
    hashes = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    first = len(CALLS)
    kernel = verify_vendor()
    bank, _, dim, binding = load_certified_bank(16, cutoff=33,
        expected_payload_sha256='feecbc02808991f6d7b1e2c3179c8da2018b76901ef34c26ef0d28b65729dd5c')
    cases = []
    for N, a in ((15, 2), (21, 2), (21, 4), (35, 2), (143, 2)):
        t = 2*(N-1).bit_length()
        program = LazyStreamingProgram(N, a, t, bank, dim)
        oracle = CheckpointRowOracle(program, (0,)*(t-1))
        result = order_from_row_oracle(oracle)
        # Only after the one-query reduction, enumerate a separate actual typed
        # modular orbit as bounded checker evidence. It is never oracle input.
        verifier = LazyStreamingProgram(N, a, t, bank, dim)
        label, expected, labels = 1, 0, []
        while True:
            label = verifier.tables[-1][label]
            expected += 1
            labels.append(label)
            if label == 1:
                break
            assert expected < N
        assert result['base_order'] == expected
        assert oracle.report()['root_query_calls'] == 1
        cases.append({'reduction': result, 'oracle': oracle.evidence(),
            'validation_only_typed_orbit': labels, 'expected_order': expected,
            'validation_table': verifier.tables[-1].export_certificate(),
            'orbit_not_passed_to_algorithm': True})
    program = LazyStreamingProgram(21, 2, 10, bank, dim)
    rejected = []
    for label, history in (('wrong_depth', (0,)*8), ('nonzero_bit', (1,)+(0,)*8)):
        try:
            order_from_row_oracle(CheckpointRowOracle(program, history))
        except ValueError:
            rejected.append(label)
        else:
            raise AssertionError(label)
    assert hashes == {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    result = {'status': 'AUTHOR_ACTUAL_BOUNDED_EXACT_ROW_TO_ORDER_REDUCTION_NOT_ADMITTED',
        'activity': 'RA-CAAAC604CB513AEA8BBC1DFC', 'kernel': kernel, 'bank': binding,
        'source_sha256': hashes, 'cases': cases, 'negative_controls': rejected,
        'actual_BRC_core_calls': len(CALLS)-first, 'actual_BRC_core_receipts': CALLS[first:],
        'generic_polynomial_row_oracle_constructed': False,
        'efficient_order_finding_claimed': False,
        'average_sampled_history_lower_bound_claimed': False}
    raw = packed(serializable(result))
    target = ROOT/'ORDER_REDUCTION_RESULTS.json.gz'
    target.write_bytes(gzip.compress(raw, mtime=0))
    summary = {k: result[k] for k in ('status', 'activity', 'source_sha256',
        'negative_controls', 'actual_BRC_core_calls', 'generic_polynomial_row_oracle_constructed',
        'efficient_order_finding_claimed', 'average_sampled_history_lower_bound_claimed')}
    summary['cases'] = [{'N': c['reduction']['N'], 'a': c['reduction']['a'],
        't': c['reduction']['t'], 'squared_base_order': c['reduction']['squared_base_order'],
        'base_order': c['reduction']['base_order'], 'row': c['reduction']['row'],
        'oracle_report': c['oracle']['report'],
        'reduction_arithmetic_cost': c['reduction']['arithmetic_cost']} for c in cases]
    summary['payload_sha256'] = hashlib.sha256(raw).hexdigest()
    summary['gzip_sha256'] = hashlib.sha256(target.read_bytes()).hexdigest()
    (ROOT/'ORDER_REDUCTION_SUMMARY.json').write_text(json.dumps(json.loads(packed(serializable(summary))),indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'actual_BRC_core_calls': result['actual_BRC_core_calls'],
        'cases': [{'N': c['reduction']['N'], 'a': c['reduction']['a'],
                   'r': c['reduction']['base_order']} for c in cases],
        'one_top_level_query_per_case': True}), flush=True)


if __name__ == '__main__':
    main()
