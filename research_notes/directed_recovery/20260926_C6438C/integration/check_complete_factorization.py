"""Finite real executions of the complete/partial certificate-bearing driver."""
from copy import deepcopy
from pathlib import Path
import gzip, hashlib, json, random, sys
from complete_factorization import factor_integer, verify_factorization, certified_phase_provider
from stage45.brc_loop_recheck import CALLS, verify_vendor
ROOT = Path(__file__).resolve().parent


def main():
    kernel = verify_vendor(); examples = []; checks = []
    for number, expected in [(2, [(2, 1)]), (9, [(3, 2)]), (27, [(3, 3)]),
            (22, [(2, 1), (11, 1)]), (35, [(5, 1), (7, 1)]),
            (45, [(3, 2), (5, 1)]), (225, [(3, 2), (5, 2)])]:
        result = factor_integer(number, random.Random(20260926 + number), certified_phase_provider,
            failure_bits=2, max_attempts=12)
        assert result['status'] == 'COMPLETE', (number, result['unresolved'])
        assert [(r['prime'], r['exponent']) for r in result['prime_factors']] == expected
        check = verify_factorization(result); examples.append(result); checks.append(check)
        print(json.dumps({'N': number, 'status': result['status'], 'prime_factors': expected}), flush=True)
    class Zero:
        def randrange(self, n): return 0
    partial = factor_integer(15, Zero(), certified_phase_provider,
        failure_bits=2, max_attempts=1, base_provider=lambda N: [2])
    assert partial['status'] == 'PARTIAL' and not partial['prime_factors']
    assert partial['unresolved'][0]['cofactor'] == 15
    checks.append(verify_factorization(partial)); examples.append(partial)
    # A perfect-power reduction keeps the actual unresolved multiplicity.
    partial_power = factor_integer(225, Zero(), certified_phase_provider,
        failure_bits=2, max_attempts=1, base_provider=lambda N: [2])
    assert partial_power['status'] == 'PARTIAL'
    assert [(r['cofactor'], r['multiplicity']) for r in partial_power['unresolved']] == [(15, 2)]
    checks.append(verify_factorization(partial_power)); examples.append(partial_power)
    negatives = []
    corrupt = deepcopy(partial); corrupt['status'] = 'COMPLETE'
    for label, specimen in [('hide_unresolved', corrupt)]:
        try: verify_factorization(specimen)
        except ValueError: negatives.append(label)
        else: raise AssertionError('unresolved cofactor was hidden')
    corrupt = deepcopy(examples[1]); corrupt['prime_factors'][0]['exponent'] += 1
    try: verify_factorization(corrupt)
    except ValueError: negatives.append('wrong_prime_exponent')
    else: raise AssertionError('wrong factor product accepted')
    output = {'schema': 'BRC_COMPLETE_FACTORIZATION_CHECKS_V1',
        'activity': 'RA-CAAAC604CB513AEA8BBC1DFC', 'status': 'AUTHOR_EXECUTED_SHARED_CONTEXT_UNREVIEWED_NOT_ADMITTED',
        'kernel': kernel, 'examples': examples, 'verified': checks, 'negative_controls': negatives,
        'actual_BRC_calls': len(CALLS), 'core_call_receipts': CALLS,
        'randomness_evidence': 'seeded PRNG examples and declared fixed tapes; no ideal randomness or measured success-rate claim'}
    payload = json.dumps(output, default=str, sort_keys=True, separators=(',', ':')).encode()
    (ROOT / 'COMPLETE_RESULTS.json.gz').write_bytes(gzip.compress(payload, mtime=0))
    brief = {k: v for k, v in output.items() if k not in ('examples', 'core_call_receipts')}
    brief['example_summaries'] = [{k: r[k] for k in ('N', 'status', 'prime_factors', 'unresolved', 'probability_contract')} for r in examples]
    brief['full_payload_sha256'] = hashlib.sha256(payload).hexdigest()
    (ROOT / 'COMPLETE_SUMMARY.json').write_text(json.dumps(brief, default=str, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'complete': 7, 'partial': 2, 'negative_controls': len(negatives), 'calls': len(CALLS)}), flush=True)


if __name__ == '__main__': main()
