"""Bounded end-to-end software examples, using the frozen actual BRC bank."""
import gzip, json, random, sys
from fractions import Fraction
from pathlib import Path
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / 'algorithm_intake'))
from terminal_instrument import StreamingProgram, load_frozen_bank, SOURCE
from stage45.brc_loop_recheck import verify_vendor, CALLS
from shor_driver import sample_once, factor_attempts


class BitPolicyTape:
    """Replay specified possible outcomes; not advertised as a uniform RNG."""
    def __init__(self, bits):
        self.bits = iter(bits)
    def randrange(self, n):
        return 0 if next(self.bits) == 0 else n - 1


def main():
    sys.set_int_max_str_digits(0)
    kernel = verify_vendor()
    bank, intervals, dim = load_frozen_bank(10)
    factory = lambda N, a, t: StreamingProgram(N, a, t, bank, dim)
    checks, examples = [], {}
    first = sample_once(factory(15, 2, 4), BitPolicyTape([1, 0]))
    assert first['k'] == 4 and first['postprocessing']['factors'] == [3, 5]
    examples['forced_possible_factor_history'] = first
    checks.append('possible nonzero history produces verified factors')
    nonpower = sample_once(factory(21, 2, 6), BitPolicyTape([1, 1, 0, 1, 0, 0]))
    assert nonpower['k'] == 11 and nonpower['postprocessing']['factors'] == [3, 7]
    examples['forced_possible_N21_history'] = nonpower
    checks.append('non-power-of-two order case produces verified factors with all residuals retained')
    # A single trajectory at the original standard width, checked against an
    # already published frozen native result; no new reference circuit run.
    standard_program = factory(21, 2, 10)
    standard = sample_once(standard_program, BitPolicyTape([(171 >> i) & 1 for i in range(10)]))
    archived = json.loads(gzip.decompress((SOURCE/'stage80'/'CASE_21_2_10.json.gz').read_bytes()))
    expected = Fraction(int(archived['probability_numerators'][171]), int(archived['probability_denominator']))
    assert Fraction(standard['history_probability']) == expected
    assert standard['postprocessing']['factors'] == [3, 7]
    standard['program_metrics'] = standard_program.report_metrics()
    standard['archived_probability_exact_equal'] = True
    examples['standard_N21_t10_frozen_terminal_bin'] = standard
    checks.append('standard t10 single trajectory matches archived complete-law bin exactly')
    retry = factor_attempts(15, 4, 2, BitPolicyTape([0,0,1,0]), factory, bases=[2, 2])
    assert len(retry['attempts']) == 2 and retry['status'] == 'FACTORS'
    assert retry['attempts'][0]['postprocessing']['status'] == 'ZERO_PHASE_RETRY'
    examples['zero_then_success'] = retry
    checks.append('zero phase retries with fresh preparation and then succeeds')
    limit = factor_attempts(15, 4, 2, BitPolicyTape([0]*4), factory, bases=[2, 2])
    assert limit['status'] == 'RETRY_LIMIT' and len(limit['attempts']) == 2
    checks.append('retry limit terminates without inventing a factor')
    examples['retry_limit'] = limit
    pre = factor_attempts(21, 6, 2, BitPolicyTape([]), factory, bases=[3])
    assert pre['status'] == 'FACTOR_GCD_PRECHECK' and pre['factors'] == [3]
    examples['gcd_precheck'] = pre
    checks.append('noncoprime base returns actual BRC-verified gcd without phase sample')
    even = factor_attempts(22, 6, 2, BitPolicyTape([]), factory)
    assert even['factors'] == [2]
    checks.append('even-input precheck produces verified proper factor')
    exhausted = factor_attempts(15, 4, 2, BitPolicyTape([0]*2), factory, bases=[2])
    assert exhausted['status'] == 'BASE_POLICY_EXHAUSTED'
    checks.append('finite external base policy exhaustion is explicit')
    incomplete = factor_attempts(15, 4, 2, BitPolicyTape([0]), factory, bases=[2])
    assert incomplete['status'] == 'INCOMPLETE_RANDOM_SOURCE'
    assert incomplete['attempts'][0]['history'] == (0,0,0)
    assert incomplete['attempts'][0]['resume_state']
    examples['incomplete_control_random_source'] = incomplete
    checks.append('random source exhaustion preserves raw prefix and differs from base exhaustion')
    class EmptyBaseRandom:
        def randrange(self, *args):
            raise StopIteration
    incomplete_base = factor_attempts(15, 4, 2, EmptyBaseRandom(), factory)
    assert incomplete_base['status'] == 'INCOMPLETE_RANDOM_SOURCE'
    assert incomplete_base['phase'] == 'BASE_SELECTION'
    checks.append('random base source exhaustion is not misclassified as finite base-list exhaustion')
    # This seed demonstrates an executable path; frequency claims come from the
    # complete distribution proof, not these few pseudorandom draws.
    program = factory(21, 2, 6)
    examples['seeded_21_2_6'] = sample_once(program, random.Random(20260926))
    examples['seeded_21_2_6']['program_metrics'] = program.report_metrics()
    checks.append('one streamed N21 sample runs without full histogram input')
    for N, t in [(1, 4), (15, 3)]:
        try:
            factor_attempts(N, t, 1, BitPolicyTape([]), factory)
        except ValueError:
            pass
        else:
            raise AssertionError('invalid input accepted')
    checks.append('invalid input and odd frozen width reject explicitly')
    result = {'schema': 'SHOR_STREAMING_DRIVER_CHECKS_V1',
              'activity_id': 'RA-40F334CAC4876C16B82B0215',
              'status': 'AUTHOR_DIRECTED_UNREVIEWED_NOT_ADMITTED',
              'kernel': kernel, 'checks': checks, 'examples': examples,
              'randomness_scope': 'external ideal randrange in theorem; specified tapes and seeded PRNG in examples',
              'born_scope': 'inherited quadratic terminal observer, not derived physical Born rule',
              'actual_BRC_core_calls': len(CALLS), 'core_call_receipts': CALLS}
    (ROOT / 'DRIVER_RESULTS.json').write_text(json.dumps(result, default=str, ensure_ascii=False, indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'checks': len(checks), 'calls': len(CALLS),
                      'seeded_result': examples['seeded_21_2_6']['postprocessing']},ensure_ascii=False))

if __name__ == '__main__':
    main()
