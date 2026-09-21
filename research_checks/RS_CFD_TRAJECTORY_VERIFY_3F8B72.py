#!/usr/bin/env python3
"""Independent verifier for the R15 CFD three-arm sign-test design.

This checks only finite combinatorics/statistics declared by R15. It does not
run spectralDNS, establish solver correctness, prove a PDE statement, or
establish a native-host speedup.
"""
from __future__ import annotations

from fractions import Fraction
from math import comb
from itertools import permutations
import json


ALPHA_FAMILY = Fraction(1, 20)   # 0.05
ALPHA_BONF = Fraction(1, 40)     # 0.025
TARGETS = (6, 12, 18, 24, 30)


def binomial_half_tail(n: int, k: int) -> Fraction:
    return sum(Fraction(comb(n, j), 2**n) for j in range(k, n + 1))


def least_k(n: int, alpha: Fraction) -> int:
    for k in range(n + 1):
        if binomial_half_tail(n, k) <= alpha:
            return k
    raise AssertionError("no threshold")


def binomial_power(n: int, k: int, p: Fraction) -> Fraction:
    q = 1 - p
    return sum(Fraction(comb(n, j)) * p**j * q**(n-j)
               for j in range(k, n + 1))


def order_balance():
    orders = ("ABC", "BCA", "CAB", "ACB", "CBA", "BAC")
    assert set(orders) == {"".join(p) for p in permutations("ABC")}
    positions = {arm: [0, 0, 0] for arm in "ABC"}
    precedence = {a+b: 0 for a in "ABC" for b in "ABC" if a != b}
    for order in orders:
        for i, arm in enumerate(order):
            positions[arm][i] += 1
        for a in "ABC":
            for b in "ABC":
                if a != b and order.index(a) < order.index(b):
                    precedence[a+b] += 1
    assert all(v == [2, 2, 2] for v in positions.values())
    assert all(v == 3 for v in precedence.values())
    return orders, positions, precedence


def main():
    expected = {
        6: (6, Fraction(1, 64)),
        12: (10, Fraction(79, 4096)),
        18: (14, Fraction(253, 16384)),
        24: (18, Fraction(190051, 16777216)),
        30: (21, Fraction(22964087, 1073741824)),
    }
    threshold_rows = []
    for n in TARGETS:
        k = least_k(n, ALPHA_BONF)
        tail = binomial_half_tail(n, k)
        assert (k, tail) == expected[n]
        if k > 0:
            assert binomial_half_tail(n, k - 1) > ALPHA_BONF
        power = binomial_power(n, k, Fraction(4, 5))
        threshold_rows.append({
            "n": n,
            "k": k,
            "tail_fraction": f"{tail.numerator}/{tail.denominator}",
            "tail": float(tail),
            "per_gate_power_if_positive_probability_0_8": float(power),
        })

    marginal_power_24 = binomial_power(24, 18, Fraction(4, 5))
    frechet_lower = max(Fraction(0), 2*marginal_power_24 - 1)
    frechet_upper = marginal_power_24
    orders, positions, precedence = order_balance()

    # If the only intended acceptance claim is conjunctive (both effects
    # positive), an intersection-union test can use alpha=.05 per component.
    # R15's .025 Bonferroni gates are still valid and stronger.
    iut_k_24 = least_k(24, ALPHA_FAMILY)
    assert iut_k_24 == 17
    assert least_k(12, ALPHA_FAMILY) == 10

    result = {
        "schema": "CFD_R15_INDEPENDENT_DESIGN_VERIFIER_V1",
        "verdict": "PASS_WITH_REQUIRED_PROTOCOL_CLARIFICATIONS",
        "arithmetic": {
            "bonferroni_familywise_alpha": float(ALPHA_FAMILY),
            "per_gate_alpha": float(ALPHA_BONF),
            "threshold_rows": threshold_rows,
            "n24_per_gate_power_at_positive_probability_0_8": float(marginal_power_24),
            "n24_joint_power_not_identified_from_marginals": True,
            "frechet_bounds_if_both_gate_pass_marginals_equal_the_quoted_power": [
                float(frechet_lower), float(frechet_upper)
            ],
        },
        "multiplicity": {
            "bonferroni_valid_with_shared_B_arm": True,
            "gate_dependence_requires_independence": False,
            "note": (
                "Bonferroni alpha=.025 per gate is valid without assuming independence. "
                "If the only claim is the conjunction 'B beats A AND B beats C', an "
                "intersection-union rule at alpha=.05 per component is already level .05; "
                "R15's Bonferroni choice is conservative but valid."
            ),
            "n24_least_k_at_alpha_0_05_for_conjunctive_IUT_component": iut_k_24,
        },
        "order_balance": {
            "orders": list(orders),
            "position_counts": positions,
            "pairwise_precedence_counts": precedence,
            "combinatorial_balance_pass": True,
            "inference_caveat": (
                "Complete permutation cycles remove deterministic ordinal-position imbalance "
                "but do not by themselves prove independence/stationarity of repeat signs. "
                "Randomize or otherwise predeclare cycle/order execution and preserve raw order/time metadata."
            ),
        },
        "ties": {
            "r15_rule_audited": "exclude ties from usable n",
            "issue": (
                "Excluding gate-specific ties can destroy the analyzed six-order balance and can "
                "give A-B and C-B different effective n/order strata. '24 usable non-tied repeats' "
                "is therefore not automatically equivalent to four complete analyzed order cycles."
            ),
            "primary_fix": (
                "Freeze 24 scheduled physical triplets (four complete six-order cycles) and define "
                "success as delta>0; count delta==0 as non-success for each superiority gate. "
                "Then n remains 24 and the 18/24 threshold remains a conservative exact gate for "
                "P(delta>0)>1/2 under the sign-test sampling assumptions."
            ),
            "alternative": (
                "If classical tie deletion is retained, predeclare a bounded replacement/stratification "
                "rule that restores order balance separately for each gate and state clearly that the "
                "null is conditional on a non-tied contrast."
            ),
        },
        "effect_size": {
            "sign_gate_certifies_magnitude": False,
            "information_loss_witness": (
                "Any fixed sign vector is compatible with arbitrarily small positive timing deltas "
                "or much larger positive deltas. Therefore the sign gate certifies directional "
                "repeat probability, not a minimum practical speedup."
            ),
            "requirement_for_material_speedup_claim": (
                "Predeclare a nonzero engineering margin epsilon and test signs of (delta-epsilon), "
                "or keep the claim explicitly at epsilon=0 and report raw paired magnitudes separately. "
                "No numerical epsilon is inferred here."
            ),
        },
        "contrast_interpretation": {
            "A_minus_B": "valid end-to-end timing contrast if correctness and identical-input gates pass",
            "C_minus_B": (
                "supports the effect of allowing sparse routing within the guarded wrapper if B and C "
                "differ only by route permission; it does not by itself isolate pure sparse-convolution "
                "arithmetic from route-induced cache/allocation/control-state changes"
            ),
            "A_minus_C": (
                "diagnostic/veto only. A significantly positive A-C means the forced-fallback guarded "
                "control is unexpectedly faster than the unmodified dense baseline and blocks clean "
                "sparse-route attribution until diagnosed. Non-significance is not equivalence."
            ),
        },
        "hard_gates": [
            "all A/B/C correctness and frozen invariants pass before any performance acceptance",
            "B must execute >=1 sparse nonlinear call; C must execute 0 sparse calls",
            "preserve raw per-repeat deltas, ties, order, timestamps and route/cost decomposition",
            "keep shadow dense counterfactual work outside confirmatory production timing",
            "native-host execution and independent task-level acceptance remain outstanding",
        ],
        "boundary": (
            "Finite experimental-design verification only; no spectralDNS native rerun, generic CFD "
            "acceleration, continuous-PDE theorem, or Working Truth/canonical promotion."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
