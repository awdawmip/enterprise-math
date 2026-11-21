"""Independent exact audit of the finite C86 Farey-to-Mellin reduction.

No generating module is imported. Every assertion uses integers/Fractions;
the affine spline identities are verified on whole rational cells, not samples.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product, combinations
from math import gcd
from pathlib import Path
import json

ROOT = Path(__file__).parent
CUTS = [F(0), F(1, 3), F(1, 2), F(2, 3), F(1)]


def det(a, b):
    return a[0] * b[1] - a[1] * b[0]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def extended_gcd(a, b):
    if not b:
        return abs(a), (1 if a > 0 else -1), 0
    g, x, y = extended_gcd(b, a % b)
    return g, y, x - (a // b) * y


def canonical_sign(triple):
    for x in triple:
        if x:
            return tuple(-v for v in triple) if x < 0 else tuple(triple)
    return tuple(triple)


def all_differences(poly):
    return sorted(set(sub(a, b) for a in poly for b in poly if a != b))


def width_partition(poly):
    cuts = sorted(set(-F(x, y) for x, y in all_differences(poly) if y))
    pieces = []
    for left, right in zip([None] + cuts, cuts + [None]):
        t = right - 1 if left is None else left + 1 if right is None else (left + right) / 2
        A, B = max(all_differences(poly), key=lambda p: p[0] + p[1] * t)
        if pieces and pieces[-1][2:] == (A, B):
            pieces[-1] = pieces[-1][0], right, A, B
        else:
            pieces.append((left, right, A, B))
    return pieces


def verify():
    kernels = json.loads((ROOT / 'width_kernels.json').read_text())
    chambers = json.loads((ROOT / 'mellin_chambers.json').read_text())
    groups = defaultdict(list)
    aggregate = defaultdict(F)
    transformations = 0
    for row in kernels['raw']:
        kind = row['kind']
        choices = tuple(row['choices'])
        groups[kind, choices].append(row)
        generators = [(1, 0), (0, 1)] + ([(1, 1)] if kind == 'face' else [])
        source = {(0, 0)}
        sign = 1
        for choice, gen in zip(choices, generators):
            if choice:
                source.add((choice * gen[0], choice * gen[1]))
            else:
                source.update([gen, (-gen[0], -gen[1])])
                sign = -sign
        poly = [tuple(p) for p in row['poly']]
        assert len(poly) >= 3 and set(poly) <= source
        for i, p in enumerate(poly):
            q = poly[(i + 1) % len(poly)]
            assert det(sub(q, p), sub(poly[(i + 2) % len(poly)], q)) > 0
            assert all(det(sub(q, p), sub(x, p)) >= 0 for x in source)
        i = row['edge']
        p, q = poly[i], poly[(i + 1) % len(poly)]
        dx, dy = sub(q, p)
        g = gcd(abs(dx), abs(dy))
        assert g == row['gcd']
        a, b = dx // g, dy // g
        unit, u, v = extended_gcd(a, b)
        assert unit == 1 and a * u + b * v == 1
        # Columns (a,b),(-v,u) have determinant +1.
        transformed = [(u * (x - p[0]) + v * (y - p[1]),
                        -b * (x - p[0]) + a * (y - p[1])) for x, y in poly]
        target = tuple(tuple(x) for x in row['canonical'])
        witness = False
        for reflection in [False, True]:
            base = [(g - x if reflection else x, y) for x, y in transformed]
            for shear in range(-100, 101):
                if tuple(sorted((x + shear * y, y) for x, y in base)) == target:
                    witness = True
                    break
            if witness:
                break
        assert witness, (kind, choices, i)
        expected = F(sign * g, 8) if kind == 'edge' else -F(sign * g, 12)
        assert F(row['coefficient']) == expected
        aggregate[target] += expected
        transformations += 1
    for kind, n in [('edge', 2), ('face', 3)]:
        expected_choices = set(product([1, -1, 0], repeat=n))
        assert {ch for k, ch in groups if k == kind} == expected_choices
        for choices in expected_choices:
            rows = groups[kind, choices]
            assert {row['edge'] for row in rows} == set(range(len(rows[0]['poly'])))
            assert len(rows) == len(rows[0]['poly'])
    stored = {tuple(tuple(p) for p in row['polygon']): F(row['coefficient'])
              for row in kernels['kernel_terms']}
    assert stored == {p: c for p, c in aggregate.items() if c}
    assert len(stored) == 15 and transformations == 142

    # Entire pushforward measure: complete affine width partitions.
    atoms, intervals, levels = defaultdict(F), [], {F(0)}
    for poly, coefficient in stored.items():
        for left, right, A, B in width_partition(poly):
            if B == 0:
                assert left is not None and right is not None
                atoms[F(A)] += coefficient * (right - left)
            else:
                finite_values = [F(A) + B * t for t in [left, right] if t is not None]
                low = min(finite_values)
                high = max(finite_values) if left is not None and right is not None else None
                intervals.append((low, high, coefficient / abs(B)))
                levels.add(low)
                if high is not None:
                    levels.add(high)
    assert {z: w for z, w in atoms.items() if w} == {F(1): F(1), F(2): F(-1)}
    levels = sorted(levels)
    for left, right in zip(levels, levels[1:] + [None]):
        t = left + 1 if right is None else (left + right) / 2
        assert sum(w for lo, hi, w in intervals if lo < t and (hi is None or t < hi)) == 0
    assert levels == [F(0), F(1), F(3, 2), F(2), F(3)]

    # Certify each whole affine spline cell by linear inequalities on its vertices.
    assert len(chambers['scaled_splines']) == len(stored)
    assert {tuple(tuple(p) for p in row['polygon']) for row in chambers['scaled_splines']} == set(stored)
    spline_count = band_count = 0
    for row in chambers['scaled_splines']:
        poly = tuple(tuple(p) for p in row['polygon'])
        assert stored[poly] == F(row['coefficient'])
        differences = all_differences(poly)
        for index, arr in enumerate(row['pieces']):
            left, right = CUTS[index:index + 2]
            knots = [(F(k['intercept']), F(k['slope']), F(k['jump'])) for k in arr]
            spline_count += 1
            if not knots:
                widths = [F(A) + B * t for lo, hi, A, B in width_partition(poly)
                          for t in [lo, hi] if t is not None]
                assert left * min(widths) >= 1
                continue
            assert sum(j for a, b, j in knots) == 0
            assert sum(a * j for a, b, j in knots) == 0
            assert sum(b * j for a, b, j in knots) == 0
            assert all(j.denominator == 1 for a, b, j in knots)
            for (a, b, j), (c, d, k) in zip(knots, knots[1:]):
                assert a + b * left <= c + d * left
                assert a + b * right <= c + d * right
            # A supporting inequality forces zero outside the first/last knot.
            for endpoint, direction in [(knots[0], -1), (knots[-1], 1)]:
                a, b, jump = endpoint
                assert any(B * direction > 0 and
                           all(A * r + B * (a + b * r) >= 1 for r in [left, right])
                           for A, B in differences)
            C = D = E = F(0)
            for i, ((a, b, j), (c, d, k)) in enumerate(zip(knots, knots[1:])):
                C -= j * a
                D -= j * b
                E += j
                # The spline equals one of the exact overlap constraints.
                assert (C, D, E) in [(F(1), -F(A), -F(B)) for A, B in differences]
                for r in [left, right]:
                    for z in [a + b * r, c + d * r]:
                        value = C + D * r + E * z
                        assert value >= 0
                        assert all(value <= 1 - A * r - B * z for A, B in differences)
                band_count += 1

    # Independent coefficient collection in every r>=s chamber.
    assert chambers['cuts'] == list(map(str, CUTS))
    assert len(chambers['chambers']) == 10
    assert {(row['r_index'], row['s_index']) for row in chambers['chambers']} == {
        (ri, si) for ri in range(4) for si in range(ri + 1)}
    for chamber in chambers['chambers']:
        ri, si = chamber['r_index'], chamber['s_index']
        assert 0 <= si <= ri <= 3
        expected, raw_count = defaultdict(F), 0
        for spline in chambers['scaled_splines']:
            coefficient = F(spline['coefficient'])
            for u in spline['pieces'][ri]:
                for v in spline['pieces'][si]:
                    key = canonical_sign((-F(v['intercept']), F(u['intercept']),
                                          F(u['slope']) - F(v['slope'])))
                    expected[key] += coefficient * F(u['jump']) * F(v['jump'])
                    raw_count += 1
        actual = {tuple(F(row[name]) for name in ['a_r', 'b_s', 'c_rs']): F(row['weight'])
                  for row in chamber['terms']}
        assert actual == {key: value for key, value in expected.items() if value and any(key)}
        assert chamber['raw_terms'] == raw_count
        assert chamber['combined_terms'] == len(actual)
    result = {'status': 'PASS', 'arithmetic': 'integers and Fraction only',
              'edge_configurations': 9, 'triangle_configurations': 27,
              'checked_affine_edge_transformations': transformations,
              'combined_kernels': len(stored),
              'pushforward_atoms': {'1': '1', '2': '-1'},
              'continuous_pushforward_density': 'identically zero',
              'whole_parameter_spline_cells': spline_count,
              'whole_affine_spline_bands': band_count,
              'exact_collected_chambers': len(chambers['chambers']),
              'sampling_used_for_certification': False}
    (ROOT / 'finite_reduction_certificate.json').write_text(json.dumps(result, indent=2) + '\n')
    return result


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2))
