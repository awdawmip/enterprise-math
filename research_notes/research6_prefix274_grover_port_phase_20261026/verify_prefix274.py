#!/usr/bin/env python3
"""PREFIX274: labelled signed ordered-pair BRC for Stage46 scoped Grover coin.

Author-side exact semantic execution, not original Stage46 source import or
physical Heartbeat. Pure rational path-pair contributions keep branch labels.
"""
from __future__ import annotations
from fractions import Fraction
from itertools import product
from math import comb
import json


def coin_entry(d: int, output: int, incoming: int) -> Fraction:
    return Fraction(2, d) - (1 if output == incoming else 0)


def brc_pair_intensity(d: int, state: tuple[int, ...], output: int) -> Fraction:
    """Normalized Z2 ordered (source_i, source_j) path-pair BRC intensity."""
    signed_branches = []
    for incoming, phase in enumerate(state):
        coeff = coin_entry(d, output, incoming)
        if coeff:
            signed_branches.append((incoming, abs(coeff), phase * (1 if coeff > 0 else -1)))
    return sum(
        (wi * wj * (1 if si == sj else -1) / d
         for _i, wi, si in signed_branches
         for _j, wj, sj in signed_branches),
        Fraction(0),
    )


def direct_intensity(d: int, s: tuple[int, ...], output: int) -> Fraction:
    total = sum(s)
    return Fraction((2 * total - d * s[output]) ** 2, d ** 3)


def signatures(d: int, s: tuple[int, ...]) -> tuple[Fraction, ...]:
    result = tuple(brc_pair_intensity(d, s, j) for j in range(d))
    assert result == tuple(direct_intensity(d, s, j) for j in range(d))
    assert sum(result) == 1
    return result


def orbit_representatives(d: int):
    return ((1,) + tail for tail in product((-1, 1), repeat=d - 1))


def flip_first(s: tuple[int, ...]) -> tuple[int, ...]:
    return (-s[0],) + s[1:]


def validate_degree(d: int) -> dict:
    groups: dict[tuple[Fraction, ...], int] = {}
    doubled: set[tuple[tuple[Fraction, ...], tuple[Fraction, ...]]] = set()
    unit = tuple(Fraction(1, d) for _ in range(d))
    for s in orbit_representatives(d):
        o = signatures(d, s)
        groups[o] = groups.get(o, 0) + 1
        flipped = signatures(d, flip_first(s))
        doubled.add((o, flipped))
    count = 1 << (d - 1)
    predicted = count - (comb(d, d // 2) // 2 if d % 2 == 0 else 0)
    assert len(groups) == predicted, (d, len(groups), predicted)
    anomaly = groups[unit]
    anomaly_expected = 1 + (comb(d, d // 2) // 2 if d % 2 == 0 else 0)
    assert anomaly == anomaly_expected, (d, anomaly, anomaly_expected)
    assert len(doubled) == (count if d != 2 else 1), (d, len(doubled), count)
    if d % 2 == 0 and d >= 4:
        assert len(groups) < count
        assert len(doubled) == count
    return {"degree": d, "sign_orbits": count,
            "one_setting_classes": len(groups), "uniform_fiber_orbits": anomaly,
            "two_setting_classes": len(doubled), "one_setting_predicted": predicted}


def main():
    rows = [validate_degree(d) for d in range(1, 9)]
    all_pos = (1, 1, 1, 1)
    balanced = (1, 1, -1, -1)
    assert signatures(4, all_pos) == signatures(4, balanced) == (Fraction(1, 4),) * 4
    assert signatures(4, flip_first(all_pos)) == (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
    assert signatures(4, flip_first(balanced)) == (Fraction(0), Fraction(1), Fraction(0), Fraction(0))
    for s in orbit_representatives(2):
        for mask in product((-1, 1), repeat=2):
            transformed = tuple(a * b for a, b in zip(s, mask))
            assert signatures(2, transformed) == (Fraction(1, 2), Fraction(1, 2))
    result = {"schema": "PREFIX274_LABELLED_PHASE_BRC_CHECK_V1", "source_kernel":
              "STAGE46_SCOPED_GROVER_COIN_ORDERED_Z2_PATH_PAIR_SEMANTICS",
              "degrees_full_rational_pairs": [1, 2, 3, 4, 5, 6, 7, 8],
              "rows": rows,
              "four_port_witness": {"base": ["1/4"] * 4,
                                    "flip_all_plus": ["1", "0", "0", "0"],
                                    "flip_balanced": ["0", "1", "0", "0"]},
              "two_port_no_go_all_masks": "PASS", "checks": "PASS",
              "native_original_stage46_source_import": "NOT_EXECUTED",
              "physical_heartbeat": "NOT_CLAIMED"}
    print(json.dumps(result, sort_keys=True, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
