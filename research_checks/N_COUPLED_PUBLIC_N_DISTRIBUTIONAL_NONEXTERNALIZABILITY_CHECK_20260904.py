#!/usr/bin/env python3
from fractions import Fraction
from collections import defaultdict
import json, random


def law_dp(transitions, outputs):
    mass = {0: Fraction(1)}
    law = defaultdict(Fraction)
    for s in range(max(set(transitions) | set(outputs)) + 1):
        w = mass.get(s, Fraction(0))
        if not w:
            continue
        if s in outputs:
            law[outputs[s]] += w
            continue
        row = transitions[s]
        assert sum((p for p, _ in row), Fraction(0)) == 1
        for p, t in row:
            mass[t] = mass.get(t, Fraction(0)) + w * p
    return dict(law)


def law_paths(transitions, outputs):
    law = defaultdict(Fraction)
    stack = [(0, Fraction(1))]
    while stack:
        s, w = stack.pop()
        if s in outputs:
            law[outputs[s]] += w
        else:
            for p, t in transitions[s]:
                stack.append((t, w * p))
    return dict(law)


def make_effect(seed):
    rng = random.Random(seed)
    depth = 4 + seed % 4
    first_leaf = 2**depth - 1
    last_leaf = 2**(depth + 1) - 2
    transitions, outputs = {}, {}
    for s in range(last_leaf + 1):
        if s < first_leaf:
            a, b = 1 + rng.randrange(1, 8), 1 + rng.randrange(1, 8)
            p = Fraction(a, a + b)
            transitions[s] = [(p, 2*s + 1), (1-p, 2*s + 2)]
        else:
            outputs[s] = ((17*s + 31*seed) % 11, (s + seed) % 5)
    return transitions, outputs


finite_specs = 128
terminal_paths = 0
law_mismatches = 0
support_mismatches = 0
for seed in range(finite_specs):
    transitions, outputs = make_effect(seed)
    a = law_dp(transitions, outputs)
    b = law_paths(transitions, outputs)
    terminal_paths += len(outputs)
    law_mismatches += int(a != b)
    support_mismatches += int(set(a) != set(b))

# Unbounded almost-surely halting fair-bit example.
# K = number of 1s before first 0.
geometric_even = Fraction(1, 2) / (1 - Fraction(1, 4))
geometric_odd = Fraction(1, 4) / (1 - Fraction(1, 4))
assert geometric_even == Fraction(2, 3)
assert geometric_odd == Fraction(1, 3)
assert geometric_even + geometric_odd == 1

# Same public operation label, distinct hidden branches/outputs.
branch_opacity_nontrivial = len(set(make_effect(0)[1].values())) > 1

summary = {
    "calculus": "G_effect-dist^eff",
    "finite_rational_specs": finite_specs,
    "finite_terminal_paths": terminal_paths,
    "law_mismatches": law_mismatches,
    "support_mismatches": support_mismatches,
    "unbounded_as_halt_example": {"even": "2/3", "odd": "1/3"},
    "branch_opacity_nontrivial": branch_opacity_nontrivial,
    "status": "PASS" if law_mismatches == support_mismatches == 0 and branch_opacity_nontrivial else "FAIL",
}
assert summary["status"] == "PASS"
print("PASS G_EFFECT_DIST_PUBLIC_EMULATOR " + json.dumps(summary, sort_keys=True))
