"""Exact scout witnesses; derived consumers, not Foundation promotion.

Run from the checkout: python -X utf8 experiments/owner_branch_scout_20260907.py
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from enterprise_math.brc_histogram import WeightHistogram, histogram_serial
from enterprise_math.operation_quotient import (
    apply_word,
    class_count,
    family_future_partition_sequence,
)


AXES = tuple(combinations(range(6), 3))
CUBE = tuple(product((0, 1), repeat=6))


def raw_mass_tables(population):
    return {
        axes: {
            address: sum(
                (mass for point, mass in population if tuple(point[i] for i in axes) == address),
                Fraction(0),
            )
            for address in product((0, 1), repeat=3)
        }
        for axes in AXES
    }


def binary_x6_strength3_generators():
    """Return exact index-2/index-3 binary OA generators, with integer checks.

    Classical affine F2 and Paley constructions, shared by the scout and the
    typed histogram consumer. Rows index branches, never native space axes.
    """
    columns = [(1,) + bits for bits in list(product((0, 1), repeat=3))[:6]]
    rows = [
        tuple(sum(a * b for a, b in zip(u, column)) % 2 for column in columns)
        for u in product((0, 1), repeat=4)
    ]
    scaled = tuple((point, Fraction(1)) for point in rows)
    assert len(set(rows)) == 16
    assert all(value == 2 for table in raw_mass_tables(scaled).values() for value in table.values())

    # Parent-owner proposed completion: Paley q=11, then antipodal pairing.
    # Both row and column Gram identities are independently checked in integers.
    order = 11
    quadratic = [
        [0 if i == j else (1 if pow((j - i) % order, 5, order) == 1 else -1) for j in range(order)]
        for i in range(order)
    ]
    hadamard = [[1] * 12] + [
        [1] + [quadratic[i][j] - int(i == j) for j in range(order)]
        for i in range(order)
    ]
    assert all(entry in (-1, 1) for row in hadamard for entry in row)
    assert all(
        sum(hadamard[i][k] * hadamard[j][k] for k in range(12)) == 12 * int(i == j)
        for i in range(12) for j in range(12)
    )
    assert all(
        sum(hadamard[k][i] * hadamard[k][j] for k in range(12)) == 12 * int(i == j)
        for i in range(12) for j in range(12)
    )
    triple_rows = [
        tuple((1 - sign * value) // 2 for value in row[:6])
        for row in hadamard for sign in (1, -1)
    ]
    triple_population = tuple((point, Fraction(1)) for point in triple_rows)
    assert len(triple_rows) == len(set(triple_rows)) == 24
    assert all(value == 3 for table in raw_mass_tables(triple_population).values() for value in table.values())

    # Integer addition of populations is the BRC alternative/recoalescence
    # operation. All lambda>=2 equal 2a+3b, b in {0,1}.
    for multiplicity in range(2, 21):
        b = multiplicity % 2
        a = (multiplicity - 3 * b) // 2
        assert a >= 0 and 2 * a + 3 * b == multiplicity
        combined = scaled * a + triple_population * b
        assert all(value == multiplicity for table in raw_mass_tables(combined).values() for value in table.values())
    return tuple(rows), tuple(triple_rows)


def integer_histogram_gap():
    # Exact rational relaxation. Each weight-1 stratum coefficient would be 1/8,
    # so this is a mass realization, never the requested integral histogram.
    relaxed = tuple((point, Fraction(1, 8)) for point in CUBE)
    assert all(value == 1 for table in raw_mass_tables(relaxed).values() for value in table.values())
    requested = WeightHistogram.from_weights([1])
    actual_relaxed_fiber = WeightHistogram.from_weights([Fraction(1, 8)] * 8)
    assert requested.total_mass == actual_relaxed_fiber.total_mass
    assert requested != actual_relaxed_fiber
    # Twelve selected characters, not all degree-2 characters.
    characters = [frozenset()] + [frozenset([i]) for i in range(6)]
    characters += [frozenset([0, i]) for i in range(1, 6)]
    differences = [len(a ^ b) for a, b in combinations(characters, 2)]
    assert len(characters) == 12 and len(set(characters)) == 12
    assert all(1 <= size <= 3 for size in differences)
    rows, triple_rows = binary_x6_strength3_generators()
    return {
        "rational_mass_cells": len(relaxed),
        "rational_mass_per_cell": "1/8",
        "requested_histogram_per_triple_address": [["1", 1]],
        "relaxed_histogram_per_triple_address": [["1/8", 8]],
        "rao_character_count": len(characters),
        "pairwise_character_product_support_sizes": dict(sorted(Counter(differences).items())),
        "hypothetical_rows": 8,
        "required_gram_rank": 12,
        "minimal_uniform_positive_integer_multiplicity": 2,
        "multiplicity_two_rows": rows,
        "paley_order": 12,
        "paley_row_and_column_gram": "12I",
        "multiplicity_three_rows": triple_rows,
        "uniform_integer_realizability_spectrum": "{0} union {lambda in Z: lambda>=2}",
        "composition_spot_checks": list(range(2, 21)),
    }


def path_monitor():
    alphabet = tuple(range(1, 7)) + tuple(range(-1, -7, -1))
    start, hit = 0, "hit"
    states = (start,) + alphabet + (hit,)
    operations = {
        letter: {
            state: hit if state == hit or state == -letter else letter
            for state in states
        }
        for letter in alphabet
    }
    stages = family_future_partition_sequence(states, operations, {state: state == hit for state in states})
    assert [class_count(stage) for stage in stages] == [2, 14]
    left, right = (1, -1, 2, -2), (1, 2, -1, -2)
    assert Counter(left) == Counter(right)
    assert apply_word(start, operations, left) == hit
    assert apply_word(start, operations, right) != hit
    weights = {1: Fraction(2, 3), -1: Fraction(3, 5), 2: Fraction(5, 7), -2: Fraction(7, 11)}

    def hist(word):
        result = WeightHistogram.from_weights([1])
        for letter in word:
            result = histogram_serial(result, WeightHistogram.from_weights([weights[letter]]))
        return result

    assert hist(left) == hist(right) == WeightHistogram.from_weights([Fraction(2, 11)])
    return {
        "left_word": left,
        "right_word": right,
        "common_endpoint": [0] * 6,
        "common_weight": "2/11",
        "left_has_adjacent_reverse": True,
        "right_has_adjacent_reverse": False,
        "monitor_partition_sizes": [class_count(stage) for stage in stages],
    }


def local_global_gap():
    # Four varying native axes; last two raw coordinates fixed to zero.
    tables = {}
    for axes in AXES:
        variable = tuple(axis for axis in axes if axis < 4)
        table = {}
        for bits in product((0, 1), repeat=len(variable)):
            if len(variable) == 3 and sum(bits) % 2:
                continue
            address_map = dict(zip(variable, bits))
            address = tuple(address_map.get(axis, 0) for axis in axes)
            table[address] = 1 if len(variable) >= 2 else 2 ** (2 - len(variable))
        tables[axes] = table
    for left, right in combinations(AXES, 2):
        overlap = tuple(sorted(set(left) & set(right)))
        def project(axes):
            answer = Counter()
            for address, count in tables[axes].items():
                answer[tuple(address[axes.index(axis)] for axis in overlap)] += count
            return answer
        assert project(left) == project(right)
    admissible = []
    for bits in product((0, 1), repeat=4):
        point = bits + (0, 0)
        if all(tuple(point[i] for i in axes) in table for axes, table in tables.items()):
            admissible.append(point)
    assert admissible == [(0,) * 6]
    assert tables[(0, 1, 2)][(0, 1, 1)] == 1
    return {
        "pairwise_overlap_checks": 190,
        "all_overlap_histograms_compatible": True,
        "global_support_join": admissible,
        "unrealizable_required_triple_entry": {"axes": [0, 1, 2], "address": [0, 1, 1], "count": 1},
    }


if __name__ == "__main__":
    print(json.dumps({
        "histogram_integrality_gap": integer_histogram_gap(),
        "path_monitor": path_monitor(),
        "local_global_gap": local_global_gap(),
    }, ensure_ascii=False, indent=2))
