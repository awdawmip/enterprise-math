#!/usr/bin/env python3
"""R750: exact finite verification of the declared V1R C12 internal transition.
No inference that SHELL is TRIADIC_CLOSURE_E=false.
"""
from itertools import permutations, product
import json

frames = [(axes, signs) for axes in permutations(range(6), 3)
          for signs in product((-1, 1), repeat=3)]
assert len(frames) == 960

def rotate(frame):
    axes, signs = frame
    return (axes[1:] + axes[:1], tuple(-s for s in signs))

def step(state):
    frame, mode = state
    if mode == "SHELL":
        return (frame, "CLOSURE")
    return (rotate(frame), "SHELL")

states = [(f, mode) for f in frames for mode in ("SHELL", "CLOSURE")]
assert len(states) == 1920
periods = {}
for state in states:
    seen = {state: 0}
    current = state
    for n in range(1, 13):
        current = step(current)
        if current in seen:
            assert current == state, (state, n)
            periods[n] = periods.get(n, 0) + 1
            break
        seen[current] = n
    else:
        raise AssertionError("period > 12")
assert periods == {12: 1920}, periods
assert all(rotate(rotate(rotate(rotate(rotate(rotate(f)))))) == f for f in frames)
assert all(step((f,"SHELL")) == (f,"CLOSURE") for f in frames)
assert all(step((f,"CLOSURE")) == (rotate(f),"SHELL") for f in frames)

# A count-only observer cannot determine the declared mode:
# attach the same V29 ledger L=0 to two distinct legal V1R states.
same_ledger_distinct_mode = sum(
    (f,"SHELL") != (f,"CLOSURE") for f in frames
)
assert same_ledger_distinct_mode == 960
print(json.dumps({
    "result": "PASS",
    "framed_states": 960,
    "declared_internal_states": 1920,
    "period_histogram": periods,
    "same_V29_ledger_distinct_V1R_mode_pairs": same_ledger_distinct_mode,
    "closure_truth_counterexample_proved": False,
    "coupled_V29_C1_event_authorized": False
}, sort_keys=True))
