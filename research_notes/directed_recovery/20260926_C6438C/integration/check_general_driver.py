"""End-to-end sparse preparation AND postprocessing checks."""
import gzip, hashlib, json, sys
from fractions import Fraction as F
from pathlib import Path
from general_streaming import GeneralStreamingProgram, PREVIOUS
from general_driver import sample_once, factor_attempts
from terminal_instrument import load_frozen_bank, SOURCE
from sparse_modular import sparse_modular_columns
from stage45.brc_loop_recheck import CALLS, verify_vendor
ROOT = Path(__file__).resolve().parent


class RequestedHistory:
    """A replay policy, never represented as uniform random sampling."""
    def __init__(self, k): self.k = k; self.next_bit = 0
    def randrange(self, n): return n - 1 if self.next_bit else 0


class ReplayProgram(GeneralStreamingProgram):
    def __init__(self, *args, tape, **kwargs):
        super().__init__(*args, **kwargs); self.tape = tape
    def branches(self, state, den, history):
        self.tape.next_bit = (self.tape.k >> len(history)) & 1
        return super().branches(state, den, history)


def main():
    dense_entries = []
    def profile(frame, event, arg):
        if (event == 'call' and frame.f_code.co_name == 'modular_columns'
                and frame.f_globals.get('__name__') == 'stage78.shor_benchmark'):
            dense_entries.append({'N': frame.f_locals.get('N'), 'b': frame.f_locals.get('b')})
    sys.setprofile(profile)
    kernel = verify_vendor(); bank, intervals, dim = load_frozen_bank(10)
    examples = []; checks = []
    for N, a, t, k, wanted in [(15, 2, 4, 4, [3, 5]), (21, 2, 6, 11, [3, 7]), (21, 2, 10, 171, [3, 7])]:
        tape = RequestedHistory(k)
        program = ReplayProgram(N, a, t, bank, dim, column_factory=sparse_modular_columns, tape=tape)
        start = len(CALLS); row = sample_once(program, tape)
        assert row['k'] == k and row['postprocessing']['factors'] == wanted
        newcalls = CALLS[start:]
        row['program_metrics'] = program.report_metrics()
        row['new_core_calls_during_sample'] = newcalls
        if t == 10:
            old = json.loads(gzip.decompress((SOURCE / 'stage80' / 'CASE_21_2_10.json.gz').read_bytes()))
            assert F(row['history_probability']) == F(int(old['probability_numerators'][k]), int(old['probability_denominator']))
            row['frozen_complete_law_bin_exact_match'] = True
        examples.append(row)
        checks.append(f'N{N}/a{a}/t{t}/k{k}: sparse preparation and sparse CF verification')
    factory = lambda N, a, t: GeneralStreamingProgram(N, a, t, bank, dim, column_factory=sparse_modular_columns)
    tape = RequestedHistory(0)
    failure = factor_attempts(15, 4, 2, tape, factory, bases=[2, 2])
    assert failure['status'] == 'RETRY_LIMIT' and len(failure['attempts']) == 2
    checks.append('zero readout retains both failed attempts and bounded stop')
    class Empty:
        def randrange(self, *args): raise EOFError
    incomplete = factor_attempts(21, 6, 1, Empty(), factory, bases=[2])
    assert incomplete['status'] == 'INCOMPLETE_RANDOM_SOURCE'
    assert incomplete['attempts'][0]['resume_state']
    checks.append('exhausted random source retains entire unnormalized resume state')
    pre = factor_attempts(21, 6, 1, Empty(), factory, bases=[3])
    assert pre['status'] == 'FACTOR_GCD_PRECHECK' and pre['factors'] == [3]
    checks.append('noncoprime base handled before permutation compilation')
    # Native controlled-H4 also has 32 states: state count alone is not origin.
    # Observe the actual dense modular entrypoint, without replacing any tool.
    all_states = [r['states'] for r in CALLS]
    sys.setprofile(None)
    assert not dense_entries
    checks.append('profile observed zero entries into frozen dense modular_columns')
    result = {'schema': 'SHOR_GENERAL_SPARSE_DRIVER_V1',
        'activity': 'RA-CAAAC604CB513AEA8BBC1DFC',
        'status': 'AUTHOR_EXECUTED_SHARED_CONTEXT_UNREVIEWED_NOT_ADMITTED',
        'kernel': kernel, 'checks': checks, 'examples': examples,
        'retry_limit': failure, 'incomplete': incomplete,
        'actual_BRC_calls': len(CALLS), 'core_call_receipts': CALLS,
        'dense_modular_entrypoint_observations': dense_entries,
        'no_uniform_random_frequency_claim_from_replays': True,
        'factor_finding_only': True}
    (ROOT / 'GENERAL_DRIVER_RESULTS.json').write_text(json.dumps(result, default=str, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'checks': len(checks), 'actual_BRC_calls': len(CALLS), 'states': all_states}))


if __name__ == '__main__': main()
