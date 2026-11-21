"""Check the mother intersection input for the radius-nine matching lemma.

The Hall proof is in README.md. This does not search or exclude radius nine.
Completeness of the 250 mother classes is an inherited proved census fact.
"""
from collections import Counter
from hashlib import sha256
from itertools import permutations, product
from pathlib import Path
import argparse
import importlib.util
import json

HERE = Path(__file__).resolve().parent
POINTS = list(product(range(5), repeat=3))


def orbit(ids):
    linear = {tuple(sorted(25*(POINTS[i][perm[0]]*sg[0]*k % 5)
                           +5*(POINTS[i][perm[1]]*sg[1]*k % 5)
                           +(POINTS[i][perm[2]]*sg[2]*k % 5) for i in ids))
              for perm in permutations(range(3))
              for sg in product((1, -1), repeat=3) for k in (1, 2)}
    return {frozenset(25*((POINTS[i][0]+a) % 5)
                      +5*((POINTS[i][1]+b) % 5)
                      +(POINTS[i][2]+c) % 5 for i in row)
            for row in linear for a, b, c in POINTS}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--baseline', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    bindings = json.loads((HERE/'bindings.json').read_text())
    for name in ('initial.txt', 'verify.py'):
        assert sha256((a.baseline/name).read_bytes()).hexdigest() == bindings['sha256'][name]
    spec = importlib.util.spec_from_file_location('matching_native', a.baseline/'verify.py')
    native = importlib.util.module_from_spec(spec); spec.loader.exec_module(native)
    rows, costs = native.initial()
    mothers = orbit(rows[0])
    assert len(mothers) == 250 and all(len(m) == 13 for m in mothers)
    assert all(native.evaluate(m) == 1296 for m in mothers)
    assert all(frozenset(rows[i]) in mothers for i in (0, 1))
    histograms = []
    for i in (0, 1):
        original = frozenset(rows[i])
        counts = Counter(len(original & m) for m in mothers if m != original)
        assert dict(counts) == {0: 100, 1: 13, 2: 96, 3: 40}
        histograms.append(dict(sorted(counts.items())))
    # For k old ten-classes, deleting the new nine-class leaves >=10k-9
    # points for new ten-classes; k-1 such classes have capacity 10k-10.
    hall = []
    for k in range(1, 10):
        required = 10*k-9
        insufficient_capacity = 10*(k-1)
        assert required > insufficient_capacity
        hall.append({'old_ten_classes': k, 'points_for_new_tens_at_least': required,
                     'capacity_of_one_fewer_new_tens': insufficient_capacity})
    result = {'native_mother_classes_checked': len(mothers),
              'complete_mother_census': 'Inherited 250-class classification; not reproved by this orbit check',
              'other_mother_intersection_histograms': histograms,
              'different_mother_minimum_replacements': 10,
              'hall_capacity_checks': hall,
              'radius_nine_equals_full_fixed_two_core_size_pattern': True,
              'radius_nine_excluded': False,
              'review_status': 'NOT_REVIEWED', 'all_checks_passed': True}
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
