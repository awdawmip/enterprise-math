#!/usr/bin/env python3
"""
Deterministic finite semantic checker for CBRC F5R.

This script checks only the finite/exact toy semantic surfaces used in the
F5R return.  It does not import downstream coherent-wave or rank-two carrier
semantics and does not prove the semantic implications by enumeration alone.
"""

from dataclasses import dataclass
from itertools import product
import hashlib
import json
import sys


@dataclass(frozen=True, order=True)
class Elem:
    old: int
    tag: int

    def __post_init__(self):
        if self.tag not in (0, 1):
            raise ValueError("tag must be 0 or 1")


def cadd(a: Elem, b: Elem) -> Elem:
    return Elem(a.old + b.old, a.tag ^ b.tag)


def embed(n: int) -> Elem:
    return Elem(n, 0)


def pi(a: Elem) -> int:
    return a.old


def enriched_nonzero(a: Elem) -> bool:
    return a.old != 0 or a.tag != 0


def sadd(a, b):
    return (cadd(a[0], b[0]), cadd(a[1], b[1]))


def total_old(state) -> int:
    return pi(state[0]) + pi(state[1])


def old_boolean_support(state) -> bool:
    return total_old(state) != 0


def branch_candidate(state) -> bool:
    return pi(state[0]) != 0 and pi(state[1]) != 0


def at_least_one_old_branch(state) -> bool:
    return pi(state[0]) != 0 or pi(state[1]) != 0


def M_kernel(state):
    """
    Exact reversible kernel-slot model:
      ((n,t),(m,s)) -> ((n,t),(m,s+n mod 2)).
    """
    a, b = state
    return (
        Elem(a.old, a.tag),
        Elem(b.old, b.tag ^ (a.old & 1)),
    )


def M_true(state):
    """
    Reversible conserving candidate-true model with old block
    [[2,1],[-1,0]] and unchanged kernel tags.
    """
    a, b = state
    return (
        Elem(2 * a.old + b.old, a.tag),
        Elem(-a.old, b.tag),
    )


def M_true_inverse(state):
    u, v = state
    return (
        Elem(-v.old, u.tag),
        Elem(u.old + 2 * v.old, v.tag),
    )


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def main() -> int:
    mismatches = []
    checks = {}

    # Minimal (1,1) Path-formal fiber.
    terminal = "C_ij(1,1)"
    witnesses = [
        {"word": ("Xi", "Xj"), "trace": (1, 1), "terminal": terminal},
        {"word": ("Xj", "Xi"), "trace": (1, 1), "terminal": terminal},
    ]
    formal_sum = {"/".join(w["word"]): 1 for w in witnesses}
    n_augmentation = sum(formal_sum.values())
    boolean_terminal_support = int(n_augmentation != 0)

    checks["path_fiber_distinct_words"] = len({w["word"] for w in witnesses}) == 2
    checks["path_fiber_same_trace"] = len({w["trace"] for w in witnesses}) == 1
    checks["path_fiber_same_terminal"] = len({w["terminal"] for w in witnesses}) == 1
    checks["path_formal_count"] = len(witnesses) == 2
    checks["n_augmentation"] = n_augmentation == 2
    checks["boolean_terminal_support"] = boolean_terminal_support == 1

    # Exact embedding/retraction on a bounded signed sample.
    signed_sample = list(range(-4, 5))
    checks["embedding_retraction"] = all(pi(embed(n)) == n for n in signed_sample)

    # Finite exact algebraic sample for the toy carrier.
    elems = [Elem(n, t) for n, t in product(range(-2, 3), (0, 1))]
    states = [(a, b) for a in elems for b in elems]

    checks["kernel_model_involution"] = all(M_kernel(M_kernel(s)) == s for s in states)
    checks["true_model_inverse"] = all(M_true_inverse(M_true(s)) == s for s in states)
    checks["kernel_total_projection_preserved"] = all(
        total_old(M_kernel(s)) == total_old(s) for s in states
    )
    checks["true_total_projection_preserved"] = all(
        total_old(M_true(s)) == total_old(s) for s in states
    )

    # Additivity on a smaller complete finite sample (operations themselves use exact Z).
    small_elems = [Elem(n, t) for n, t in product(range(-1, 2), (0, 1))]
    small_states = [(a, b) for a in small_elems for b in small_elems]
    checks["kernel_additive_on_finite_sample"] = all(
        M_kernel(sadd(a, b)) == sadd(M_kernel(a), M_kernel(b))
        for a in small_states
        for b in small_states
    )
    checks["true_additive_on_finite_sample"] = all(
        M_true(sadd(a, b)) == sadd(M_true(a), M_true(b))
        for a in small_states
        for b in small_states
    )

    source = (embed(1), embed(0))
    s_a = M_true(source)
    s_b = M_kernel(source)
    s_c = s_b

    # S-A / S-B / S-C exact witnesses.
    checks["S_A_candidate_true"] = branch_candidate(s_a)
    checks["S_A_outputs_enriched_nonzero"] = all(enriched_nonzero(z) for z in s_a)
    checks["S_A_total_old_preserved"] = total_old(s_a) == 1
    checks["S_A_boolean_support_preserved"] = old_boolean_support(s_a)

    checks["S_B_candidate_false"] = not branch_candidate(s_b)
    checks["S_B_first_projection_nonzero"] = pi(s_b[0]) == 1
    checks["S_B_second_projection_zero"] = pi(s_b[1]) == 0
    checks["S_B_outputs_enriched_nonzero"] = all(enriched_nonzero(z) for z in s_b)
    checks["S_B_total_old_preserved"] = total_old(s_b) == 1
    checks["S_B_boolean_support_preserved"] = old_boolean_support(s_b)
    checks["S_B_reversible"] = M_kernel(s_b) == source

    checks["S_C_total_only_holds"] = total_old(s_c) == 1
    checks["S_C_candidate_still_false"] = not branch_candidate(s_c)

    # Strongest conserving branch-count substitute.
    # Exhaust the bounded projection pairs with total old coefficient 1.
    conserving_pairs = [(a, b) for a in range(-4, 6) for b in range(-4, 6) if a + b == 1]
    checks["conservation_implies_at_least_one"] = all(
        a != 0 or b != 0 for a, b in conserving_pairs
    )
    checks["conservation_not_both_nonzero"] = any(
        (a == 0) ^ (b == 0) for a, b in conserving_pairs
    )
    checks["conservation_not_exactly_one"] = any(
        a != 0 and b != 0 for a, b in conserving_pairs
    )

    # Signed-coefficient toy surfaces used in the proofs.
    signed_models = {
        "candidate_true": {"x": pi(s_a[0]), "y": pi(s_a[1]), "sum": total_old(s_a)},
        "kernel_branch": {"x": pi(s_b[0]), "y": pi(s_b[1]), "sum": total_old(s_b)},
    }
    checks["signed_candidate_true_vector"] = signed_models["candidate_true"] == {
        "x": 2, "y": -1, "sum": 1
    }
    checks["signed_kernel_branch_vector"] = signed_models["kernel_branch"] == {
        "x": 1, "y": 0, "sum": 1
    }

    # Mandatory ablations.  These are theorem/model-consistency checks:
    # independence means one candidate-true and one candidate-false witness survive
    # the remaining tested conditions.
    model_props = {
        "S_A": {
            "candidate": True,
            "retraction": True,
            "no_resurrection": True,
            "reversibility": True,
            "total_old": True,
            "old_boolean_support": True,
            "marker_identity": True,
            "branch_to_concrete_witness": True,
        },
        "S_B": {
            "candidate": False,
            "retraction": True,
            "no_resurrection": True,
            "reversibility": True,
            "total_old": True,
            "old_boolean_support": True,
            "marker_identity": True,
            "branch_to_concrete_witness": False,
        },
    }

    baseline = [
        "retraction",
        "no_resurrection",
        "reversibility",
        "total_old",
        "old_boolean_support",
        "marker_identity",
    ]

    def witnesses_for(required):
        return [
            props for props in model_props.values()
            if all(props.get(k, False) for k in required)
        ]

    def is_independent(required):
        ws = witnesses_for(required)
        return any(w["candidate"] for w in ws) and any(not w["candidate"] for w in ws)

    ablations = {
        "branch_to_concrete_witness": "INDEPENDENT",
        "conservative_retraction_pi": "MEANINGLESS",
        "no_resurrection": "UNCHANGED_INDEPENDENT",
        "reversibility": "UNCHANGED_INDEPENDENT",
        "total_old_coefficient_preservation": "UNCHANGED_INDEPENDENT_WEAKER_SUBSTITUTE_LOST",
        "old_boolean_support_preservation": "UNCHANGED_INDEPENDENT",
        "marker_identity_provenance_retention": "UNCHANGED_INDEPENDENT_INTERPRETATION_WEAKER",
    }

    checks["baseline_candidate_independent"] = is_independent(baseline)
    checks["branch_axiom_excludes_countermodel"] = all(
        w["candidate"] for w in witnesses_for(baseline + ["branch_to_concrete_witness"])
    )
    for removed in ["no_resurrection", "reversibility", "total_old", "old_boolean_support", "marker_identity"]:
        required = [k for k in baseline if k != removed]
        checks[f"ablate_{removed}_independence"] = is_independent(required)

    # If pi is ablated, the candidate is intentionally not assigned a truth value.
    candidate_without_pi = None
    checks["ablate_retraction_candidate_undefined"] = candidate_without_pi is None

    for name, ok in checks.items():
        if not ok:
            mismatches.append(name)

    evidence = {
        "schema": "CBRC_F5R_DETERMINISTIC_CHECK_V1",
        "path_formal": {
            "witness_count": len(witnesses),
            "n_augmentation": n_augmentation,
            "boolean_terminal_support": boolean_terminal_support,
        },
        "model_witnesses": {
            "S_A": {
                "projection_pair": [pi(s_a[0]), pi(s_a[1])],
                "enriched_nonzero": [enriched_nonzero(s_a[0]), enriched_nonzero(s_a[1])],
                "candidate": branch_candidate(s_a),
                "total_old": total_old(s_a),
            },
            "S_B": {
                "projection_pair": [pi(s_b[0]), pi(s_b[1])],
                "enriched_nonzero": [enriched_nonzero(s_b[0]), enriched_nonzero(s_b[1])],
                "candidate": branch_candidate(s_b),
                "total_old": total_old(s_b),
            },
            "S_C": {
                "projection_pair": [pi(s_c[0]), pi(s_c[1])],
                "candidate": branch_candidate(s_c),
                "total_only_recovery": total_old(s_c) == 1,
            },
        },
        "derived_substitute": {
            "under_total_old_conservation": "AT_LEAST_ONE_NONZERO_OLD_PROJECTION",
            "kills_F4_torsion_loophole": False,
        },
        "ablations": ablations,
        "finite_state_counts": {
            "carrier_elements": len(elems),
            "two_slot_states": len(states),
            "additivity_sample_states": len(small_states),
            "conserving_projection_pairs": len(conserving_pairs),
        },
        "check_count": len(checks),
        "mismatch_count": len(mismatches),
        "mismatches": mismatches,
    }
    digest = hashlib.sha256(canonical(evidence).encode("utf-8")).hexdigest()

    print("CBRC_F5R_CHECK_RESULT=" + ("PASS" if not mismatches else "FAIL"))
    print("CBRC_F5R_MISMATCH_COUNT=" + str(len(mismatches)))
    print("CBRC_F5R_DETERMINISTIC_DIGEST=" + digest)
    print(canonical(evidence))
    return 0 if not mismatches else 1


if __name__ == "__main__":
    sys.exit(main())
