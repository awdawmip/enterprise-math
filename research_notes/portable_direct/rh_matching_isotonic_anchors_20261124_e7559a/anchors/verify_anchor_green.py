#!/usr/bin/env python3
"""Exact finite checks for the anchor Green identity.

The general and infinite statements are proved in ANCHOR_GREEN_BRIDGE.md.
This checks rational finite geometry, affine boundary modes, signed sources,
and the precise interlaced packet family. No external dependencies.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import argparse
import json


def green(x, z, left, right):
    return (min(x, z) - left) * (right - max(x, z)) / (right - left)


def interpolate(x, grid, values):
    for i in range(len(grid) - 1):
        if grid[i] <= x <= grid[i + 1]:
            w = (x - grid[i]) / (grid[i + 1] - grid[i])
            return (1 - w) * values[i] + w * values[i + 1]
    raise ValueError('point outside interpolation range')


def moments(grid, values):
    return [(values[k] - values[k - 1]) / (grid[k] - grid[k - 1])
            - (values[k + 1] - values[k]) / (grid[k + 1] - grid[k])
            for k in range(1, len(grid) - 1)]


def verify():
    grids = basis_roads = point_checks = directed_checks = 0
    for size in range(2, 7):
        for raw_grid in combinations(range(1, 10), size):
            grid = list(map(F, raw_grid))
            points = sorted(set(grid + [(u + v) / 2 for u, v in zip(grid, grid[1:])]))
            grids += 1
            # All coordinate bases verify this linear identity on every real
            # node-value vector on each of these finite grids.
            for i in range(size):
                values = [F(int(k == i)) for k in range(size)]
                ts = moments(grid, values)
                basis_roads += 1
                for x in points:
                    j = ((grid[-1] - x) * values[0]
                         + (x - grid[0]) * values[-1]) / (grid[-1] - grid[0])
                    v = j + sum((green(x, grid[k], grid[0], grid[-1]) * ts[k - 1]
                                 for k in range(1, size - 1)), F(0))
                    assert v == interpolate(x, grid, values)
                    point_checks += 1
            # Signed cancellation and arbitrary affine endpoints.
            for mode in range(4):
                values = [F((-1) ** (k + mode) * (k + 1), k + 2)
                          + (mode - 2) * grid[k] + F(mode - 1, 3)
                          for k in range(size)]
                ts = moments(grid, values)
                for x in points:
                    j = ((grid[-1] - x) * values[0]
                         + (x - grid[0]) * values[-1]) / (grid[-1] - grid[0])
                    upper = j + sum((green(x, grid[k], grid[0], grid[-1])
                                     * max(ts[k - 1], 0)
                                     for k in range(1, size - 1)), F(0))
                    actual = interpolate(x, grid, values)
                    assert actual <= upper
                    assert max(actual, 0) <= max(upper, 0)
                    directed_checks += 1
            affine = [F(7, 3) - F(11, 5) * x for x in grid]
            assert all(t == 0 for t in moments(grid, affine))

    interlaced = [value for j in range(41) for value in (2 ** (j + 1), 3 * 2 ** j)]
    for k in range(1, len(interlaced) - 1):
        left, middle, right = interlaced[k - 1:k + 2]
        assert right == 2 * left
        assert F(4, 3) <= F(middle, left) <= F(3, 2)
        assert F(4, 3) <= F(right, middle) <= F(3, 2)
    return {
        'schema': 'RH_ANCHOR_GREEN_EXACT_CHECK_V1',
        'arithmetic': 'fractions.Fraction, exact',
        'finite_domain': 'all integer node subsets of {1,...,9} of size 2 through 6; all coordinate node-value bases',
        'grids': grids,
        'basis_roads': basis_roads,
        'basis_point_identities': point_checks,
        'signed_directed_point_checks': directed_checks,
        'affine_boundary_checks': grids,
        'interlaced_integer_nodes': len(interlaced),
        'interlaced_ratio_two_packets': len(interlaced) - 2,
        'all_passed': True,
        'scope': 'Finite implementation checks; the infinite normalization, series limits and analytic estimates use the written proof.'
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('anchor_green_certificate.json'))
    args = parser.parse_args()
    result = verify()
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
