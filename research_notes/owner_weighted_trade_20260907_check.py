"""Small exact checks of the eight-positive weighted-trade classification.

This is not a solver or a weighted-support search. The general classification
is proved in OWNER_WEIGHTED_TRADE_FRONTIER_20260907.md.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "experiments" / "owner_joint_observer_20260907"))
from observer_certificate import Branch, all_three_axis_tables, raw_marginal_table


def bit_parity(value):
    return value.bit_count() % 2


def pair_count(first, second):
    return Counter(zip(first, second))


def run():
    cube3 = tuple(product((0, 1), repeat=3))
    first = tuple(row[0] for row in cube3)
    second = tuple(row[1] for row in cube3)
    expected_pair = Counter({bits: 2 for bits in product((0, 1), repeat=2)})
    compatible_columns = 0
    triple_types = Counter()
    affine_planes = 0
    for selected in combinations(range(8), 4):
        column = tuple(int(i in selected) for i in range(8))
        if pair_count(first, column) == expected_pair and pair_count(second, column) == expected_pair:
            counts = Counter(zip(first, second, column))
            alpha = counts[(0, 0, 0)] - 1
            assert alpha in (-1, 0, 1)
            assert all(counts[bits] == 1 + alpha * (-1) ** sum(bits) for bits in cube3)
            compatible_columns += 1
            triple_types[alpha] += 1
        points = tuple(cube3[i] for i in selected)
        if all(sum(point[axis] for point in points) == 2 for axis in range(3)):
            assert tuple(sum(point[axis] for point in points) % 2 for axis in range(3)) == (0, 0, 0)
            equations = [
                (normal, constant)
                for normal in cube3 if any(normal)
                for constant in (0, 1)
                if set(points) == {u for u in cube3
                                   if sum(a * b for a, b in zip(normal, u)) % 2 == constant}
            ]
            assert len(equations) == 1
            affine_planes += 1
    assert compatible_columns == 18
    assert triple_types == {-1: 1, 0: 16, 1: 1}
    assert affine_planes == 8

    # Three actual basis-axis representatives have character labels 1,2,4.
    # At most three additional distinct representatives fit in six axes.
    joins = []
    for size in range(4):
        for extras in combinations((3, 5, 6, 7), size):
            labels = (1, 2, 4) + extras
            positive = {tuple(bit_parity(label & u) for label in labels) for u in range(8)}
            projections = [
                (axes, {tuple(point[j] for j in axes) for point in positive})
                for order in (1, 2, 3)
                for axes in combinations(range(len(labels)), order)
            ]
            join = {point for point in product((0, 1), repeat=len(labels))
                    if all(tuple(point[j] for j in axes) in allowed for axes, allowed in projections)}
            if extras == (7,):
                assert len(join) == 16 and len(join - positive) == 8
            else:
                assert join == positive
            joins.append({"extra_characters": list(extras), "join_count": len(join),
                          "available_negative_cells": len(join - positive)})
    assert len(joins) == 15

    lam = Fraction(2, 7)
    embeddings = (
        lambda u: u + (0, 0),
        lambda u: u + (u[0], 1 - u[1]),
        lambda u: (-3 + 2 * u[0], 5 - 7 * u[1], 2 + 5 * u[2],
                   -1 + 11 * u[3], 4 - 13 * u[0], 6),
    )
    witness_count = 0
    for embed in embeddings:
        positive = tuple(Branch(f"p:{u}", embed(u), lam)
                         for u in product((0, 1), repeat=4) if sum(u) % 2 == 0)
        negative = tuple(Branch(f"n:{u}", embed(u), lam)
                         for u in product((0, 1), repeat=4) if sum(u) % 2 == 1)
        assert len({branch.coordinate for branch in positive + negative}) == 16
        pos_tables = all_three_axis_tables(positive)
        neg_tables = all_three_axis_tables(negative)
        assert pos_tables == neg_tables
        deleted_tables = all_three_axis_tables(positive[1:])
        defect = sum(abs(deleted_tables[axes].get(address, Fraction(0))
                         - neg_tables[axes].get(address, Fraction(0)))
                     for axes in deleted_tables
                     for address in deleted_tables[axes].keys() | neg_tables[axes].keys())
        assert defect == 20 * lam
        assert 15 * lam / defect == Fraction(3, 4)
        assert lam / (8 * lam) == Fraction(1, 8) > Fraction(2, 21)
        witness_count += 1

    # The theorem is not generalized to order one: positive weights 5 and 1.
    order_one_positive = (Branch("heavy", (0,) * 6, Fraction(5)),
                          Branch("light", (1,) * 6, Fraction(1)))
    order_one_negative = tuple(Branch(f"e:{i}", tuple(int(j == i) for j in range(6)))
                               for i in range(6))
    for axis in range(6):
        assert raw_marginal_table(order_one_positive, (axis,)) == raw_marginal_table(order_one_negative, (axis,))
    return {
        "status": "PASS",
        "arithmetic": "integer counts and Fraction; no solver",
        "compatible_third_columns": compatible_columns,
        "triple_types_by_alpha": dict(sorted(triple_types.items())),
        "coordinate_balanced_affine_planes": affine_planes,
        "character_join_cases": joins,
        "raw_brc_weighted_parity_embeddings": witness_count,
        "unequal_order_one_guard": "PASS",
        "deleted_point_ratio": "3/4",
        "light_weight_fraction": "1/8 > 2/21",
        "scope": "finite lemma/witness regressions; full proof is in the accompanying note",
    }


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, separators=(",", ":")))
