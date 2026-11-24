#!/usr/bin/env python3
"""Exact finite checks for the road-convex representation and shape bounds."""
from fractions import Fraction as F
from itertools import product
from math import isqrt
from pathlib import Path
import argparse
import json


def pav_cumulative_residual(edge_values, left):
    # Same weighted regression definition as the predecessor; no floating decisions.
    pools = []
    for n, value in enumerate(edge_values, left):
        weight = F(1, n * (n + 1))
        pools.append([n, n + 1, weight, weight * value])
        while len(pools) >= 2:
            a, b = pools[-2:]
            if a[3] * b[2] <= b[3] * a[2]:
                break
            pools[-2:] = [[a[0], b[1], a[2] + b[2], a[3] + b[3]]]
    fitted = []
    for lo, hi, weight, total in pools:
        fitted.extend([total / weight] * (hi - lo))
    residual = [F(0)]
    for n, value, fit in zip(range(left, left + len(edge_values)), edge_values, fitted):
        residual.append(residual[-1] + (value - fit) / (n * (n + 1)))
    return residual


def physical_convex_envelope(values):
    hull = []
    for j, value in enumerate(values):
        while len(hull) >= 2:
            i, k = hull[-2:]
            if (values[k] - values[i]) * (j - k) < (value - values[k]) * (k - i):
                break
            hull.pop()
        hull.append(j)
    result = [F(0)] * len(values)
    for i, j in zip(hull, hull[1:]):
        for k in range(i, j + 1):
            result[k] = F(j - k, j - i) * values[i] + F(k - i, j - i) * values[j]
    return result


def edge_field(values, left):
    return [n * values[j + 1] - (n + 1) * values[j]
            for j, n in enumerate(range(left, left + len(values) - 1))]


def exact_sqrt_interval(value, digits=65):
    scale = 10 ** digits
    k = isqrt(value.numerator * scale * scale // value.denominator)
    lo, hi = F(k, scale), F(k + 1, scale)
    assert lo * lo <= value <= hi * hi
    return lo, hi


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('road_convex_strength_certificate.json'))
    args = parser.parse_args()
    counts = {'roads': 0, 'split_checks': 0, 'subhat_denominator_cancellations': 0,
              'affine_invariance_checks': 0, 'curvature_roads': 0,
              'curvature_split_checks': 0, 'strict_sqrt_multiplier_gaps': 0}
    for left in (2, 7, 19):
        for h in range(2, 6):
            right = left + h
            for raw in product((-3, -1, 2), repeat=h + 1):
                q = list(map(F, raw))
                cumulative = pav_cumulative_residual(edge_field(q, left), left)
                convex = physical_convex_envelope(q)
                translated = [z + 2 * n + F(5, 3) for n, z in enumerate(q, left)]
                translated_convex = physical_convex_envelope(translated)
                for j in range(1, h):
                    x = left + j
                    factor = F(h, j * (h - j))
                    from_pav = factor * x * cumulative[j]
                    from_convex = factor * (q[j] - convex[j])
                    all_chords = [q[j]]
                    for i in range(j):
                        for k in range(j + 1, h + 1):
                            u, v = left + i, left + k
                            chord = F(k - j, k - i) * q[i] + F(j - i, k - i) * q[k]
                            all_chords.append(chord)
                            contrast = (q[j] - q[i]) / (j - i) - (q[k] - q[j]) / (k - j)
                            coefficient = F(h * (j - i) * (k - j), j * (h - j) * (k - i))
                            assert coefficient * contrast == factor * (q[j] - chord)
                            counts['subhat_denominator_cancellations'] += 1
                    brute = factor * (q[j] - min(all_chords))
                    assert from_pav == from_convex == brute >= 0
                    assert from_convex <= factor * (max(q) - min(q))
                    assert translated[j] - translated_convex[j] == q[j] - convex[j]
                    counts['affine_invariance_checks'] += 1
                    counts['split_checks'] += 1
                counts['roads'] += 1

    # Every model here has distributional second derivative >= -1/L.
    for left in range(2, 21):
        for h in range(2, min(left, 8) + 1):
            right = left + h
            source_patterns = [
                [F(0)] * (h - 1),
                [F(1)] * (h - 1),
                [F(j % 2) for j in range(1, h)],
                [F(3 if j == h // 2 else 0) for j in range(1, h)],
            ]
            for sources in source_patterns:
                q = [-F(j * j, 2 * left)
                     + sum((source * max(j - k, 0)
                            for k, source in enumerate(sources, 1)), F(0))
                     for j in range(h + 1)]
                convex = physical_convex_envelope(q)
                for j in range(1, h):
                    residual = F(h, j * (h - j)) * (q[j] - convex[j])
                    assert residual <= F(h, 2 * left)
                    counts['curvature_split_checks'] += 1
                counts['curvature_roads'] += 1

    # A certified square-root strict-concavity gap bounds every imaginary phase
    # on Re(s)=1/2. The full open-strip statement is proved analytically.
    smallest_gap = None
    for left in range(2, 25):
        for right in range(left + 2, 2 * left + 1):
            r = F(right, left)
            _, r_upper = exact_sqrt_interval(r)
            for pivot in range(left + 1, right):
                xi = F(pivot, left)
                alpha, beta = F(right - pivot, right - left), F(pivot - left, right - left)
                xi_lower, _ = exact_sqrt_interval(xi)
                gap = xi_lower - alpha - beta * r_upper
                assert gap > 0
                assert alpha + beta == 1 and alpha + beta * r == xi
                smallest_gap = gap if smallest_gap is None else min(smallest_gap, gap)
                counts['strict_sqrt_multiplier_gaps'] += 1

    q = [F(-2), F(-15, 8), F(-2)]
    convex = physical_convex_envelope(q)
    residual = 2 * (q[1] - convex[1])
    assert residual == F(1, 4) and all(z < 0 for z in q)
    assert q[2] - 2 * q[1] + q[0] == F(-1, 4)
    result = {
        'schema': 'EM_ROAD_CONVEX_RESIDUAL_STRENGTH_V1', 'status': 'PASS',
        'arithmetic': 'Exact fractions and integer square roots; no float admission.',
        'road_inputs': {'L': [2, 7, 19], 'h': [2, 3, 4, 5],
                        'q_nodes': 'all vectors in {-3,-1,2}^{h+1}'},
        'representations': ['weighted PAV of E_n=n q_(n+1)-(n+1)q_n',
                            'physical-node monotone-chain lower convex hull',
                            'independent enumeration of all crossing chords'],
        'counts': counts,
        'sqrt_multiplier_check': {
            'domain': '2<=L<=24; L+2<=R<=2L; L<x<R; xi=x/L and r=R/L',
            'root_decimal_digits': 65,
            'minimum_certified_gap_lower_rational': str(smallest_gap),
            'meaning': 'Strict lower bound for sqrt(xi)-alpha-beta sqrt(r), valid for every imaginary phase at Re(s)=1/2.'},
        'local_positive_energy_counterexample': {
            'nodes': [2, 3, 4], 'q': [str(z) for z in q],
            'positive_energy': '0', 'residual': str(residual),
            'second_difference': '-1/4',
            'scope': 'General local roads, not a modification of the fixed reference road.'},
        'scope': 'Finite author verification of representation, geometry, strict gaps and boundaries. Unbounded growth indices are proved analytically in ROAD_CONVEX_ENVELOPE_AND_STRENGTH.md; not an independent Review.'}
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'counts': counts}))


if __name__ == '__main__':
    main()
