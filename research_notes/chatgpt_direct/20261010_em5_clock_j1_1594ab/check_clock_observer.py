"""Observer-law audit only; does not rerun or emulate the underlying BRC worlds."""
import json
import sys
from fractions import Fraction
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / 'reuse'))
from enterprise_math.relation_future_powerset import relation_support_image

assertions = 0
def check(ok):
    global assertions
    assertions += 1
    assert ok

rows = []
for L in range(2, 25):
    for budget in range(21):
        deadline = (L - 1) * (budget + 1)
        clock = [n + min(n // (L - 1), budget) for n in range(deadline + 1)]
        check(clock[0] == 0)
        check(all(1 <= clock[n + 1] - clock[n] <= 2 for n in range(deadline)))
        check(all(0 <= clock[n] - n <= budget for n in range(deadline + 1)))
        check(all(k % L != L - 1 for k in clock[:-1]))
        check(clock[-1] % L == L - 1)
        # Exact finite support DP, through inherited T8 relation kernel.
        # State = (sample n, accumulated skipped rounds).  Kill a branch only
        # for this clock-avoidance query when its sampled residue is the target.
        states = frozenset(range(budget + 1))
        support = frozenset({0})
        last_nonempty = 0
        for n in range(1, deadline + 1):
            edges = frozenset((b, c) for b in states for c in range(b, budget + 1)
                              if (n + c) % L != L - 1)
            support = relation_support_image(states, edges, support)
            check(all((n + c) % L != L - 1 for c in support))
            if support:
                last_nonempty = n
        check(not support)
        check(last_nonempty == deadline - 1)
        if L == 12:
            rows.append({'skip_budget': budget, 'first_guaranteed_sample_index': deadline,
                         'readings_including_n0': deadline + 1})

L = 12
hold_clock = [n + int(n % L == L - 1) for n in range(1201)]
check(hold_clock[0] == 0)
check(all(0 <= hold_clock[n + 1] - hold_clock[n] <= 2 for n in range(1200)))
check(all(0 <= hold_clock[n] - n <= 1 for n in range(1201)))
check(all(k % L != L - 1 for k in hold_clock))
inherited_pulse_readout = lambda k: Fraction(1, 4) if k % L == L - 1 else Fraction(0)
check(all(inherited_pulse_readout(k) == 0 for k in hold_clock))
check(inherited_pulse_readout(11) == Fraction(1, 4))

result = {'status': 'PASS_OBSERVER_LAW_CHECKS_ONLY', 'assertions': assertions,
          'grid': {'periods': [2, 24], 'skip_budgets': [0, 20]},
          'clock_support_kernel': 'unchanged relation_future_powerset.relation_support_image',
          'underlying_brc_world_rerun': False, 'independent_replication': False,
          'L12_bounds': rows, 'hold_counterexample_samples': len(hold_clock),
          'unexecuted': ['384-atom BRC controller suite', 'physical clock', 'measurement backreaction'],
          'new_proof': 'counting bound plus explicit all-n sharp clock and periodic hold witness'}
Path('CLOCK_OBSERVER_VALIDATION.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))
