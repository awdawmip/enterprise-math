"""Check the affine orbits of all extremal size-eight and size-nine classes."""
import argparse
import json
from itertools import product, permutations
from pathlib import Path
from collections import defaultdict
from functools import lru_cache
from tempfile import TemporaryDirectory
import subprocess
import sys

HERE = Path(__file__).resolve().parent
SEEDS = {
    8: [(0, 7, 35, 42, 51, 58, 86, 124), (0, 7, 35, 42, 51, 58, 91, 124), (0, 7, 35, 42, 54, 71, 86, 118)],
    9: [(0, 7, 35, 42, 51, 58, 89, 91, 124), (0, 7, 35, 42, 51, 58, 91, 99, 114)],
}
MIN = {8: 419, 9: 557}
POINTS = list(product(range(5), repeat=3))

def index(x, y, z):
    return 25 * (x % 5) + 5 * (y % 5) + z % 5

def group():
    translations = [[index(x + a, y + b, z + c) for x, y, z in POINTS] for a, b, c in POINTS]
    linear = []
    for p, signs, scale in product(permutations(range(3)), product((1, -1), repeat=3), (1, 2)):
        linear.append([index(*(scale * sign * x[j] for j, sign in zip(p, signs))) for x in POINTS])
    maps = [bytes(t[x] for x in a) for t in translations for a in linear]
    assert len(set(maps)) == len(maps) == 12000
    return maps

def verify_profile():
    minima = (0, 0, 12, 36, 72, 120, 201, 292, 419, 557, 744, 936, 1104, 1296)

    @lru_cache(None)
    def optimum(points, labels, minimum):
        if labels == 0:
            return (0, ((),)) if points == 0 else (10**9, ())
        choices = []
        for size in range(minimum, min(13, points // labels) + 1):
            value, tails = optimum(points - size, labels - 1, size)
            choices.extend((minima[size] + value, (size,) + t) for t in tails)
        if not choices:
            return 10**9, ()
        best = min(c for c, t in choices)
        return best, tuple(t for c, t in choices if c == best)

    value, profiles = optimum(125, 14, 1)
    assert value == 7660 and profiles == ((8,) + (9,) * 13,)
    print('Unique minimum profile: one size 8, thirteen size 9; lower bound 7660')

def verify(seed_file):
    verify_profile()
    maps = group()
    seeds = defaultdict(set)
    for line in Path(seed_file).read_text().splitlines():
        s, cost, *row = map(int, line.split())
        if s in MIN and cost == MIN[s]:
            seeds[s].add(tuple(sorted(row)))
    for n, reps in SEEDS.items():
        all_rows = set()
        sizes = []
        for row in reps:
            assert row in seeds[n]
            orbit = {tuple(sorted(f[x] for x in row)) for f in maps}
            assert all_rows.isdisjoint(orbit)
            all_rows.update(orbit)
            sizes.append(len(orbit))
        assert seeds[n] <= all_rows
        assert sizes == ([4000, 12000, 12000] if n == 8 else [12000, 12000])
        print(n, len(seeds[n]), 'enumerated seeds, orbit sizes', sizes, 'stabilizer orders', [12000 // s for s in sizes])
    witness = json.loads((HERE / 'witnesses.json').read_text())['explicit']['14']
    partition = {tuple(sorted(row)) for row in witness}
    stabilizer = [f for f in maps if {tuple(sorted(f[i] for i in row)) for row in witness} == partition]
    assert len(stabilizer) == 1
    neg = [index(-x, -y, -z) for x,y,z in POINTS]
    head = set(witness[0] + witness[1])
    assert len(head) == 17 and {neg[i] for i in head} == head
    tail = {tuple(sorted(row)) for row in witness[2:]}
    assert {tuple(sorted(neg[i] for i in row)) for row in tail} == tail
    print('PASS: every cost-7660 partition has trivial affine stabilizer; checked the explicit certificate and its partial inversion symmetry')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('seed_file', nargs='?', type=Path, help='Exhaustive class_minima.cpp output (optional)')
    parser.add_argument('--curve', type=Path, default=HERE, help='Directory containing class_minima.cpp, with sibling bounds/')
    args = parser.parse_args()
    if args.seed_file:
        verify(args.seed_file)
    else:
        sys.path.insert(0, str(args.curve.parent/'bounds'))
        from prior_bounds import observation_file
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            observation_file(root/'observations.bin')
            exe = root/'class_minima'
            subprocess.run(['c++', '-std=c++17', '-O3', '-mpopcnt', str(args.curve/'class_minima.cpp'), '-o', str(exe)], check=True)
            subprocess.run([str(exe), str(root/'observations.bin'), str(root/'seeds')], check=True, stdout=subprocess.DEVNULL)
            verify(root/'seeds')
