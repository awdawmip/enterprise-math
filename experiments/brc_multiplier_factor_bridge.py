"""Finite benchmark for the BRC multiplier -> difference-of-squares bridge.

This experiment is deliberately prior-art-safe.  A square ceiling-completion
gap is exactly the classical multiplier-Fermat/difference-of-squares condition.
The experiment asks only whether BRC basin observables add a useful safe filter,
and benchmarks a classical quadratic-residue bitset before exact square-root
testing.

Reference sample:
- distinct odd semiprimes p*q with 101 <= p < q <= 997;
- multipliers 1..100;
- exact integer arithmetic only.

No factorization complexity or novelty claim follows from this bounded sample.
"""

from __future__ import annotations

import csv
from collections import defaultdict
from math import gcd, isqrt
from pathlib import Path
from statistics import median

from enterprise_math.brc_multiplier_basin import endpoint_resonance_defect
from enterprise_math.brc_square_gap_prefilter import (
    ceiling_completion_cost,
    passes_square_residue_filter,
    square_residue_count,
)
from enterprise_math.legendre import primes_up_to

MODULI = (1008, 1440, 1680, 2016, 2880, 3600, 4032, 20160)


def _exact_square_root(value: int) -> int | None:
    root = isqrt(value)
    return root if root * root == value else None


def _proper_factor_from_gap(n: int, x: int, b: int) -> int | None:
    if b <= 0:
        return None
    for candidate in (x - b, x + b):
        factor = gcd(candidate, n)
        if 1 < factor < n:
            return factor
    return None


def semiprime_sample() -> list[tuple[int, int, int]]:
    primes = [p for p in primes_up_to(997) if p >= 101]
    return [
        (p * q, p, q)
        for i, p in enumerate(primes)
        for q in primes[i + 1 :]
    ]


def benchmark() -> dict[str, object]:
    semiprimes = semiprime_sample()
    candidate_count = len(semiprimes) * 100
    residue_survivors = {modulus: 0 for modulus in MODULI}
    false_negatives = {modulus: 0 for modulus in MODULI}
    square_gap_count = 0
    successful_pairs = 0
    successful_semiprimes = 0
    first_multiplier: dict[int, int] = {}

    # Per-multiplier controlled comparison of the two main nonsquare H classes.
    per_m_class: dict[int, dict[int, list[int]]] = defaultdict(
        lambda: defaultdict(lambda: [0, 0])
    )
    resonance_totals = {False: [0, 0], True: [0, 0]}

    for n, _, _ in semiprimes:
        found = False
        k = isqrt(n)
        for multiplier in range(1, 101):
            x, gap = ceiling_completion_cost(n, multiplier)
            b = _exact_square_root(gap)
            square_gap = b is not None
            if square_gap:
                square_gap_count += 1

            for modulus in MODULI:
                passes = passes_square_residue_filter(gap, modulus)
                residue_survivors[modulus] += int(passes)
                if square_gap and not passes:
                    false_negatives[modulus] += 1

            factor = None if b is None else _proper_factor_from_gap(n, x, b)
            success = factor is not None
            if success:
                successful_pairs += 1
                if not found:
                    first_multiplier[n] = multiplier
                    found = True

            floor_root_m = isqrt(multiplier)
            if floor_root_m * floor_root_m != multiplier:
                # For this sample m<=100 and k>=101, so the Round-2 no-skip
                # condition m<=4*k^2 holds automatically. Endpoints therefore
                # give the exact consecutive support size without materializing
                # the full Weighted-BRC profile for every benchmark candidate.
                source_min = k * k
                source_max = (k + 1) * (k + 1) - 1
                support_size = (
                    isqrt(multiplier * source_max)
                    - isqrt(multiplier * source_min)
                    + 1
                )
                relative_h = support_size - floor_root_m
                per_m_class[multiplier][relative_h][0] += int(success)
                per_m_class[multiplier][relative_h][1] += 1

                defect, resonance = endpoint_resonance_defect(k + 1, multiplier)
                del defect
                resonance_totals[resonance][0] += int(success)
                resonance_totals[resonance][1] += 1

        successful_semiprimes += int(found)

    controlled_ratios: list[float] = []
    for class_map in per_m_class.values():
        if 1 not in class_map or 2 not in class_map:
            continue
        low_success, low_total = class_map[1]
        high_success, high_total = class_map[2]
        if low_total == 0 or high_total == 0 or low_success == 0:
            continue
        controlled_ratios.append(
            (high_success / high_total) / (low_success / low_total)
        )

    return {
        "semiprimes": len(semiprimes),
        "candidate_pairs": candidate_count,
        "successful_semiprimes": successful_semiprimes,
        "successful_pairs": successful_pairs,
        "square_gap_count": square_gap_count,
        "residue_survivors": residue_survivors,
        "false_negatives": false_negatives,
        "residue_counts": {m: square_residue_count(m) for m in MODULI},
        "controlled_h_ratio_count": len(controlled_ratios),
        "controlled_h_ratio_median": median(controlled_ratios),
        "controlled_h_ratio_gt_one": sum(ratio > 1 for ratio in controlled_ratios),
        "resonance_totals": resonance_totals,
    }


def write_prefilter_csv(path: str | Path) -> None:
    data = benchmark()
    candidate_count = int(data["candidate_pairs"])
    rows = []
    for modulus in MODULI:
        residue_count = data["residue_counts"][modulus]
        survivors = data["residue_survivors"][modulus]
        rows.append(
            {
                "modulus": modulus,
                "quadratic_residue_classes": residue_count,
                "uniform_pass_fraction": f"{residue_count}/{modulus}",
                "uniform_pass_rate": residue_count / modulus,
                "raw_bitset_bytes": (modulus + 7) // 8,
                "sample_candidates": candidate_count,
                "sample_survivors": survivors,
                "sample_rejected": candidate_count - survivors,
                "sample_reject_rate": (candidate_count - survivors) / candidate_count,
                "actual_square_gaps": data["square_gap_count"],
                "false_negatives": data["false_negatives"][modulus],
            }
        )
    output = Path(path)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    result = benchmark()
    print(result)
    write_prefilter_csv(
        Path(__file__).resolve().parents[1]
        / "research_artifacts"
        / "brc_multiplier_square_gap_prefilter_20260906.csv"
    )
