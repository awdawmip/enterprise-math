"""Exact short exclusion of <=1 large embedded class through cost 10006.

This verifies all mother and cost-1244 proper twelve-point marginal shapes,
and all cheap ten-point shapes. The complete size plan distinguishes all
embedded classes from only embedded classes of size >=11.
"""
from collections import Counter
from hashlib import sha256
from itertools import permutations, product
from pathlib import Path
import argparse
import importlib.util
import json
import struct
from plan import catalogue, make_rows, minimum_by_number

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
P = list(product(range(5), repeat=3))


def points(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length()-1
        mask -= bit


def orbit(ids):
    oriented = {tuple(sorted(25*(P[i][perm[0]]*sg[0]*k % 5)+5*(P[i][perm[1]]*sg[1]*k % 5)
                             +P[i][perm[2]]*sg[2]*k % 5 for i in ids))
                for perm in permutations(range(3)) for sg in product((1, -1), repeat=3) for k in (1, 2)}
    return {sum(1 << (25*((P[i][0]+a) % 5)+5*((P[i][1]+b) % 5)+(P[i][2]+c) % 5) for i in row)
            for row in oriented for a, b, c in P}


def hist(mask):
    ids = list(points(mask))
    return tuple(tuple(sum(P[p][j] == a for p in ids) for a in range(5)) for j in range(3))


def defect(mask):
    return sum(max(value-2, 0) for row in hist(mask) for value in row)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--previous', type=Path, default=ROOT/'delivery')
    parser.add_argument('--bank', type=Path, default=ROOT/'r10/lower/work/bank')
    parser.add_argument('--parents', type=Path, default=ROOT/'r10/bias/work/parent')
    parser.add_argument('--proper12-bank', type=Path, default=ROOT/'r10/bias/work/B12')
    parser.add_argument('--output', type=Path, default=HERE/'single_embedded_verification.json')
    args = parser.parse_args()
    inputs = json.loads((HERE/'inputs.json').read_text())
    expected = {Path(row['path']).name: row['sha256'] for row in inputs['files']}
    for path in (args.bank, args.parents, args.proper12_bank):
        key = 'parent' if path == args.parents else 'bank' if path == args.bank else 'B12'
        assert sha256(path.read_bytes()).hexdigest() == expected[key]
    data = catalogue(); minima = {key: min(costs) for key, costs in data.items()}
    assert minimum_by_number(minima)[0] == minimum_by_number(minima, True)[0] == 10192
    rows = make_rows(10006, minima)
    profiles = [r for r in rows if r['large_embedded_count'] == 1]
    assert len(profiles) == 2
    assert all(sorted(r['embedded_sizes']+r['proper_sizes']) == [10]*10+[12, 13] for r in profiles)
    assert all(13 in r['embedded_sizes'] and 12 in r['proper_sizes'] for r in profiles)
    assert sorted({c for e in (0, 1) for c in data[10, e] if c <= 770}) == [744, 747, 752, 768]
    assert [c for c in data[12, 0] if c <= 1270] == [1244]
    source = json.loads((HERE/'proper12_representative.json').read_text())
    proper12 = orbit(source['points'])
    assert len(proper12) == source['complete_affine_orbit_size'] == 3000
    anchored = {lo+(hi << 64) for lo, hi, cost in struct.iter_unpack('<QQQ', args.proper12_bank.read_bytes()) if cost == 1244}
    assert len(anchored) == 288 and anchored == {m for m in proper12 if m & 1}
    mothers = {int(line.split()[0])+(int(line.split()[1]) << 64)
               for line in args.parents.read_text().splitlines()[:250]}
    assert len(mothers) == 250
    assert orbit(list(points(min(mothers)))) == mothers
    spec = importlib.util.spec_from_file_location('single_embedded_native', args.previous/'fractional/proof/verify.py')
    native = importlib.util.module_from_spec(spec); spec.loader.exec_module(native)
    bad, pair = native.observation_tables()
    for mother in mothers:
        assert native.native_class(mother, bad, pair) == (13, 1296)
        assert all(sorted(row) == [2, 2, 2, 2, 5] for row in hist(mother))
    for row in proper12:
        assert native.native_class(row, bad, pair) == (12, 1244)
        assert not any(row & ~m == 0 for m in mothers)
        assert all(sorted(axis) == [2, 2, 2, 2, 4] for axis in hist(row))
    # Pointwise defects of each possible cheap ten-point type. These banks
    # have been natively validated in the fixed predecessor/C appendices;
    # here their new coordinate-shape assertions are checked exhaustively.
    target_counts = {744: 12000, 747: 24000, 752: 12000, 768: 1500}
    target_defects = {744: 0, 747: 1, 752: 1, 768: 4}
    counts = Counter(); shapes = {c: Counter() for c in target_counts}
    for lo, hi, cost, tag in struct.iter_unpack('<QQII', args.bank.read_bytes()):
        if tag % 256 != 10 or cost not in counts and cost not in target_counts:
            continue
        if cost not in target_counts:
            continue
        mask = lo+(hi << 64); d = defect(mask)
        assert d == target_defects[cost] and cost-744 >= 3*d
        shape = tuple(sorted(tuple(sorted(axis)) for axis in hist(mask)))
        shapes[cost][shape] += 1; counts[cost] += 1
    assert dict(counts) == target_counts
    assert set(shapes[744]) == {((2, 2, 2, 2, 2),)*3}
    assert set(shapes[747]) == set(shapes[752]) == {((1, 2, 2, 2, 3), (2, 2, 2, 2, 2), (2, 2, 2, 2, 2))}
    assert set(shapes[768]) == {((1, 1, 2, 2, 4), (1, 1, 2, 2, 4), (2, 2, 2, 2, 2))}
    # Every axis has a mother-heavy level and a proper12-heavy level. Equal
    # levels produce residual [16,21,21,21,21], different levels produce
    # [18,19,21,21,21]. Their positive defects relative to 20 are 4 and 3.
    axis_cases = []
    for same in (True, False):
        mother = [5, 2, 2, 2, 2]
        proper = [4, 2, 2, 2, 2] if same else [2, 4, 2, 2, 2]
        residual = [25-a-b for a, b in zip(mother, proper)]
        demand = sum(max(v-20, 0) for v in residual)
        assert demand == (4 if same else 3)
        axis_cases.append({'heavy_levels_equal': same, 'residual_fiber_counts': residual, 'positive_defect': demand})
    lower = 1296+1244+10*744+3*9
    assert lower == 10007 > 10006
    result = {'schema': 'TWELVE_LABEL_SINGLE_EMBEDDED_SHORT_EXCLUSION_V1',
              'budget': 10006, 'classes': 12, 'points': 125,
              'definition_all_embedded': 'contained in at least one of all 250 legal thirteen-point mother classes',
              'definition_large_embedded': 'embedded and size at least eleven',
              'zero_large_embedded_size_cost_lower_bound': 10192,
              'single_large_embedded_size_profiles': profiles,
              'native_mothers_checked': 250, 'native_proper_twelve_checked': 3000,
              'proper_twelve_complete_orbit_equals_full_anchored_bank': True,
              'cheap_ten_classes_shape_checked': sum(counts.values()),
              'ten_type_shapes': [{'cost': c, 'classes': counts[c], 'positive_defect': target_defects[c],
                                   'shape': next(iter(shapes[c]))} for c in sorted(counts)],
              'axis_cases': axis_cases, 'minimum_residual_total_defect': 9,
              'single_large_embedded_lower_bound': lower,
              'conclusion': 'Every twelve-class partition of total cost <=10006 has at least two embedded classes of size >=11, hence at least two embedded classes in total.',
              'review_status': 'NOT_REVIEWED',
              'scope': 'Exact full sublayer exclusion and structural requirement only; not a new whole-domain cost lower bound. Native class census and mother completeness are inherited inputs.'}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
