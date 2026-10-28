"""Bounded post-freeze pressure test; not a general mechanism or theorem proof."""
from collections import Counter
from itertools import combinations, permutations, product
import hashlib
import json
from pathlib import Path

from enterprise_math.finite_symmetry import orbit_partition

ROOT = Path('/workspace/enterprise-math')
OUT = Path(__file__).resolve().parent
AXES = range(6)
ANCHOR = (-3, 2, -1, 0, 4, -2)

def degree(point, population):
    return sum(tuple(point[j] + (sign if j == i else 0) for j in AXES) in population
               for i in AXES for sign in (-1, 1))

def equality_box(population, k):
    fields = [sorted({p[i] for p in population}) for i in AXES]
    return (sum(len(v) == 2 for v in fields) == k
            and all(len(v) == 1 or (len(v) == 2 and v[1] == v[0] + 1) for v in fields)
            and population == set(product(*fields)))

# Execute the existing T7 tool on the complete finite S6 action on all 64
# axis-index subsets. This classifies axis choices of the equality family only.
# It is not an infinite-X6 automorphism computation or a bound proof.
elements = tuple(range(64))
actions = {
    permutation: {
        mask: sum(1 << permutation[i] for i in AXES if mask & (1 << i))
        for mask in elements
    }
    for permutation in permutations(AXES)
}
orbits = orbit_partition(elements, actions)
orbit_summary = sorted((next(iter(o)).bit_count(), len(o)) for o in orbits)
assert orbit_summary == [(0, 1), (1, 6), (2, 15), (3, 20), (4, 15), (5, 6), (6, 1)]

cases = []
for name, universe in [
    ('nine Cells at (u,v,0,0,0,0), u,v in {0,1,2}',
     [tuple(v) + (0, 0, 0, 0) for v in product(range(3), repeat=2)]),
    ('eight Cells at (u,v,w,0,0,0), u,v,w in {0,1}',
     [tuple(v) + (0, 0, 0) for v in product(range(2), repeat=3)]),
]:
    by_min_degree = Counter()
    for mask in range(1, 1 << len(universe)):
        population = {p for index, p in enumerate(universe) if mask & (1 << index)}
        minimum = min(degree(p, population) for p in population)
        by_min_degree[minimum] += 1
        assert minimum <= 6
        assert len(population) >= 2**minimum
        for k in range(minimum + 1):
            if len(population) == 2**k:
                assert equality_box(population, k)
    cases.append({'universe': name, 'nonempty_subsets': 2**len(universe)-1,
                  'full_population_preserved': True, 'by_min_degree': dict(by_min_degree)})

construction_count = 0
for k in range(7):
    for axes in combinations(AXES, k):
        population = {
            tuple(ANCHOR[i] + bit_by_axis.get(i, 0) for i in AXES)
            for bits in product((0, 1), repeat=k)
            for bit_by_axis in [dict(zip(axes, bits))]
        }
        assert len(population) == 2**k
        assert {degree(p, population) for p in population} == {k}
        construction_count += 1

output = {
    'status': 'PASS',
    'phase': 'B_POST_IMMUTABLE_RAW_FREEZE',
    'proof_status': 'BOUNDED_CHECK_ONLY_NOT_UNBOUNDED_PROOF',
    'T7_reuse': {
        'resolution': 'REUSE_EXECUTED',
        'callable': 'enterprise_math.finite_symmetry.orbit_partition',
        'complete_action_count': len(actions),
        'elements': len(elements),
        'orbit_sizes_by_active_axis_count': orbit_summary,
        'source_sha256': hashlib.sha256((ROOT/'src/enterprise_math/finite_symmetry.py').read_bytes()).hexdigest(),
        'scope': 'finite axis-choice action of equality boxes; no bound or infinite-graph claim',
    },
    'exhaustive_restricted_native_populations': cases,
    'all_axis_choices_constructions_checked': construction_count,
    'native_state': 'six signed coordinates retained; four or three fixed fields are actual restrictions',
    'time': 'static; no time variable required',
}
(OUT/'phase_b_check_result.json').write_text(json.dumps(output, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(output, ensure_ascii=False, indent=2))
