"""Exact finite witnesses for OWNER-FREE-20260907-3MARGINAL-7V8.

This verifies witnesses, not the general support lower-bound proof.
All 64 binary signed-X6 chart states are retained as the declared population.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from enterprise_math.brc_weighted import cwm_from_positive_weights

population = tuple(product((0, 1), repeat=6))
triples = tuple(combinations(range(6), 3))
seen = set()
pair_count = marginal_count = fiber_count = 0

for active in combinations(range(6), 4):
    fixed = tuple(i for i in range(6) if i not in active)
    for background in product((0, 1), repeat=2):
        rectangle = [x for x in population if tuple(x[i] for i in fixed) == background]
        legs = [[x for x in rectangle if sum(x[i] for i in active) % 2 == parity]
                for parity in (0, 1)]
        assert len(rectangle) == 16 and list(map(len, legs)) == [8, 8]
        assert set(legs[0]).isdisjoint(legs[1])
        seen.update(rectangle)
        assert cwm_from_positive_weights([1] * 8).count == 8
        for selected in triples:
            tables = []
            for leg in legs:
                fibers = defaultdict(list)
                for x in leg:
                    fibers[tuple(x[i] for i in selected)].append(Fraction(1))
                tables.append({y: cwm_from_positive_weights(weights)
                               for y, weights in fibers.items()})
            assert tables[0] == tables[1]
            r = len(set(selected) & set(active))
            expected = cwm_from_positive_weights([1] * (2 ** (3-r)))
            assert all(summary == expected for summary in tables[0].values())
            marginal_count += 1
            fiber_count += len(tables[0])
        pair_count += 1

assert seen == set(population)
base = [x for x in population if x[4:] == (0, 0)]
even = [x for x in base if sum(x[:4]) % 2 == 0]
odd = [x for x in base if sum(x[:4]) % 2 == 1]
norm_histograms = [dict(sorted(Counter(sum(a*a for a in x) for x in leg).items()))
                   for leg in (even, odd)]
joint_moments = [sum(x[0]*x[1]*x[2]*x[3] for x in leg) for leg in (even, odd)]
assert norm_histograms == [{0: 1, 2: 6, 4: 1}, {1: 4, 3: 4}]
assert joint_moments == [1, 0]

origin = (0,) * 6
diagonal = (1,) * 6
def can3(x, selected):
    values = tuple(x[i] for i in selected)
    return tuple(a - min(values) for a in values)

assert all(can3(origin, selected) == can3(diagonal, selected) for selected in triples)
assert sum(a*a for a in diagonal) == 6

result = {
    "status": "PASS",
    "candidate_id": "OWNER-FREE-20260907-3MARGINAL-7V8",
    "evidence_type": "EXACT_FINITE_WITNESS_CHECK_NOT_GENERAL_PROOF",
    "full_declared_population_size": len(population),
    "states_observed_without_filtering": len(seen),
    "four_axis_rectangle_pairs": pair_count,
    "complete_marginal_table_comparisons": marginal_count,
    "CWM_fiber_comparisons": fiber_count,
    "norm_squared_histograms_even_odd": norm_histograms,
    "four_coordinate_product_moments_even_odd": joint_moments,
    "can3_singleton_diagonal_collision": True,
    "existing_executable_reused": "enterprise_math.brc_weighted.cwm_from_positive_weights",
    "general_seven_support_uniqueness": "PROVED_IN_NOTE_NOT_BY_ENUMERATION",
}
output = Path(__file__).with_name("owner_free_20260907_check.json")
output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps(result, ensure_ascii=False, indent=2))
