#!/usr/bin/env python3
"""PREFIX-271: finite Z2 phase BRC ordered-pair observer, exact rational certificates.

SCOPED AUTHOR-SIDE MIRROR of the Stage46 source law:
 I_c = sum_{p,q} w_p*w_q*chi(g_p - g_q), chi(0)=+1, chi(1)=-1.
This script does not import/call the native Enterprise Math package and does
not model a full inter-heartbeat Phi or calibrated physical time.
"""
from __future__ import annotations

import itertools
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


@dataclass(frozen=True)
class PhaseBranch:
    label: int                  # preserves individual ordered branch label
    weight: Fraction            # strictly positive branch mass/amplitude magnitude
    phase: int                  # Z2 phase: 0 for plus, 1 for minus


def phase_brc_branches(a: tuple[Fraction, ...], c: tuple[Fraction, ...]) -> tuple[PhaseBranch, ...]:
    """Formal selection/recombination with rational control coefficients c."""
    assert len(a) == len(c)
    out: list[PhaseBranch] = []
    for i, (x, control) in enumerate(zip(a, c)):
        z = x * control
        if z:
            out.append(PhaseBranch(i, abs(z), int(z < 0)))
    return tuple(out)


def ordered_pair_brc_intensity(a: tuple[Fraction, ...], c: tuple[Fraction, ...]) -> Fraction:
    """Exact typed Stage46 Z2 ordered-pair BRC observer, not a positive-total shortcut."""
    bs = phase_brc_branches(a, c)
    result = Fraction(0)
    for p in bs:
        for q in bs:
            character = 1 if (p.phase - q.phase) % 2 == 0 else -1
            result += p.weight * q.weight * character
    assert result >= 0  # exact full ordered-pair recoalescence
    return result


def basis(n: int, i: int, j: int | None = None) -> tuple[Fraction, ...]:
    return tuple(Fraction(int(k == i or (j is not None and k == j))) for k in range(n))


def gram_from_pair_probes(a: tuple[Fraction, ...]) -> tuple[tuple[Fraction, ...], ...]:
    n = len(a)
    diag = [ordered_pair_brc_intensity(a, basis(n, i)) for i in range(n)]
    return tuple(
        tuple(
            diag[i] if i == j else
            (ordered_pair_brc_intensity(a, basis(n, i, j)) - diag[i] - diag[j]) / 2
            for j in range(n)
        ) for i in range(n)
    )


def actual_gram(a: tuple[Fraction, ...]) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(tuple(a[i] * a[j] for j in range(len(a))) for i in range(len(a)))


def subset_signature(a: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    n = len(a)
    return tuple(
        ordered_pair_brc_intensity(a, tuple(Fraction((mask >> i) & 1) for i in range(n)))
        for mask in range(1 << n)
    )


def gram_signature(a: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    return tuple(e for row in actual_gram(a) for e in row)


def verify_family(n: int, values: tuple[Fraction, ...]) -> dict:
    by_gram: dict[tuple[Fraction, ...], list[tuple[Fraction, ...]]] = {}
    by_future: dict[tuple[Fraction, ...], list[tuple[Fraction, ...]]] = {}
    tested = 0
    for aa in itertools.product(values, repeat=n):
        a = tuple(aa)
        assert gram_from_pair_probes(a) == actual_gram(a)
        future = subset_signature(a)
        key = gram_signature(a)
        by_gram.setdefault(key, []).append(a)
        by_future.setdefault(future, []).append(a)
        tested += 1
    assert len(by_gram) == len(by_future)
    for gram, group in by_gram.items():
        a = group[0]
        equal = set(group)
        assert equal == {a, tuple(-x for x in a)}  # zero vector gives one member
        assert set(by_future[subset_signature(a)]) == equal
    return {"n": n, "value_alphabet": [str(x) for x in values],
            "labeled_inputs_tested": tested, "gram_classes": len(by_gram),
            "all_subset_future_signatures": len(by_future), "status": "PASS"}


def verify_sign_family(n: int) -> dict:
    arr = [tuple(Fraction(z) for z in a) for a in itertools.product((-1, 1), repeat=n)]
    grams = {gram_signature(a) for a in arr}
    future = {subset_signature(a) for a in arr}
    assert len(grams) == len(future) == (1 << (n - 1))
    return {"k": n, "phase_vectors": len(arr),
            "future_safe_classes": len(grams), "missing_phase_bits_exact": n - 1,
            "status": "PASS"}


def main() -> None:
    sample_a = (Fraction(1), Fraction(1))
    sample_b = (Fraction(1), Fraction(-1))
    e0, e1, both = basis(2, 0), basis(2, 1), basis(2, 0, 1)
    witness = {
        "singletons_A": [str(ordered_pair_brc_intensity(sample_a, c)) for c in (e0, e1)],
        "singletons_B": [str(ordered_pair_brc_intensity(sample_b, c)) for c in (e0, e1)],
        "joint_A": str(ordered_pair_brc_intensity(sample_a, both)),
        "joint_B": str(ordered_pair_brc_intensity(sample_b, both)),
        "gram_A": [[str(z) for z in row] for row in gram_from_pair_probes(sample_a)],
        "gram_B": [[str(z) for z in row] for row in gram_from_pair_probes(sample_b)],
    }
    assert witness["singletons_A"] == witness["singletons_B"] == ["1", "1"]
    assert witness["joint_A"] == "4" and witness["joint_B"] == "0"
    sign_families = [verify_sign_family(n) for n in range(1, 9)]
    finite_families = [verify_family(n, (Fraction(-1), Fraction(0), Fraction(1))) for n in range(1, 6)]
    rational_family = verify_family(3, (Fraction(-1), Fraction(-1, 2), Fraction(0), Fraction(1, 2), Fraction(1)))
    out = {
        "schema": "EM_PREFIX271_AUTHOR_SIDE_EXACT_BRC_PHASE_PAIR_VERIFICATION_V1",
        "status": "PASS",
        "scientific_arithmetic": "FINITE_Z2_PHASE_BRC_ORDERED_PAIR_OBSERVER_EXACT_RATIONAL",
        "source_runtime_import_executed": False,
        "full_native_heartbeat_executed": False,
        "witness": witness,
        "sign_families": sign_families,
        "zero_including_families": finite_families,
        "rational_family": rational_family,
        "claim_scope": "Finite exact verification of the algebraic branch-pair formulas only; universal proof is in the paper.",
    }
    path = Path(__file__).with_name("RESULTS_PREFIX271.json")
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": out["status"], "witness": witness,
                      "sign_classes_k8": sign_families[-1]["future_safe_classes"],
                      "three_value_cases": sum(x["labeled_inputs_tested"] for x in finite_families),
                      "five_value_rational_cases": rational_family["labeled_inputs_tested"]}, ensure_ascii=False))

if __name__ == "__main__":
    main()
