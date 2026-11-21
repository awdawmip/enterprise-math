"""Rebuild the exact restricted optimum for two complete parallel five-class orbits."""
import argparse
from itertools import combinations_with_replacement, permutations, product
from pathlib import Path
from tempfile import TemporaryDirectory
import subprocess
import sys

HERE = Path(__file__).resolve().parent
P = list(product(range(5), repeat=3))
MINIMA = (0, 0, 12, 36, 72, 120, 201, 292, 419, 557, 744, 936, 1104, 1296)

def idx(p):
    return 25 * p[0] + 5 * p[1] + p[2]

def translate(p, d, step=1):
    return tuple((x + step*y) % 5 for x, y in zip(p, d))

def bits(points):
    return sum(1 << i for i in set(points))

def linear_maps():
    for axes, signs, q in product(permutations(range(3)), product((-1, 1), repeat=3), (1, 2)):
        yield lambda p: tuple(q * signs[i] * p[axes[i]] % 5 for i in range(3))

def linear_and_affine():
    linear = [tuple(idx(f(p)) for p in P) for f in linear_maps()]
    translates = [tuple(idx(translate(p, d)) for p in P) for d in P]
    affine = [bytes(t[x] for x in g) for t in translates for g in linear]
    assert len(set(affine)) == 12000
    return linear, affine

def candidate_sizes():
    viable = set()
    for i, j in combinations_with_replacement(range(1, 14), 2):
        nleft = 125 - 5*(i+j)
        for residual in combinations_with_replacement(range(1, 14), 3):
            if sum(residual) == nleft and 5*(MINIMA[i]+MINIMA[j]) + sum(MINIMA[x] for x in residual) < 8881:
                viable.add((i, j))
    assert viable == {(9,9), (9,10), (9,11), (10,10)}
    return sorted(viable)

def orbits(rows, group):
    covered = set()
    for row in sorted(rows):
        if row not in covered:
            covered.update(tuple(sorted(g[x] for x in row)) for g in group)
    return sorted(covered)

def support_representatives(masks, transformations):
    seen = set()
    for m in masks:
        if m in seen:
            continue
        points = [j for j in range(25) if m >> j & 1]
        seen.update(sum(1 << g[j] for j in points) for g in transformations)
        yield m

def make_patches(bank, pairs, linear):
    dirs = [(0,0,1), (0,1,1), (0,1,2), (1,1,1), (1,1,2)]
    all_dirs = {frozenset(idx(translate((0,0,0),d,t)) for t in range(5)) for d in P[1:]}
    covered = set()
    for d in dirs:
        line = frozenset(idx(translate((0,0,0),d,t)) for t in range(5))
        images = {frozenset(g[i] for i in line) for g in linear}
        assert covered.isdisjoint(images)
        covered |= images
    assert all_dirs == covered
    for d in dirs:
        lines = sorted({tuple(sorted(idx(translate(p,d,t)) for t in range(5))) for p in P})
        ix = {point: i for i, line in enumerate(lines) for point in line}
        genline = {idx(translate((0,0,0),d,t)) for t in range(5)}
        representatives = [line[0] for line in lines]
        quotient_group = set()
        for g in linear:
            if g[idx(d)] in genline:
                for t in representatives:
                    quotient_group.add(tuple(ix[idx(translate(P[g[i]],P[t]))] for i in representatives))
        support = {k: {bits(ix[x] for x in r) for r in rows if len({ix[x] for x in r}) == k} for k, rows in bank.items()}
        for i, j in pairs:
            choices = ( ((1 << 25) - 1) ^ (u | v) for u in support_representatives(sorted(support[i]), quotient_group) for v in sorted(support[j]) if not u & v )
            for free in support_representatives(choices, quotient_group):
                points = [x for x in range(125) if free >> ix[x] & 1]
                yield (i, j, len(points), *points)

def run(curve):
    sys.path.insert(0,str(curve.parent/'bounds'))
    from prior_bounds import observation_file
    linear, affine = linear_and_affine()
    pairs = candidate_sizes()
    with TemporaryDirectory() as name:
        folder = Path(name)
        obs = folder/'observations.bin'
        observation_file(obs)
        enum = folder/'enum'
        subprocess.run(['c++','-O3','-std=c++17','-mpopcnt',str(curve/'class_minima.cpp'),'-o',str(enum)],check=True)
        text = subprocess.check_output([str(enum),str(obs),str(folder/'seeds')],text=True)
        assert {int(s):int(c) for s,_,c,*_ in (line.split() for line in text.splitlines())} == {s:MINIMA[s] for s in range(2,14)}
        seeds = {s:[] for s in (9,10,11)}
        for line in (folder/'seeds').read_text().splitlines():
            s,c,*r = map(int,line.split())
            if s in seeds and c == MINIMA[s]:
                seeds[s].append(tuple(r))
        bank = {s:orbits(rows,affine) for s,rows in seeds.items()}
        patches = list(make_patches(bank,pairs,linear))
        print('Shapes', len(patches), 'class counts', {s:len(rows) for s, rows in bank.items()},flush=True)
        assert len(patches)==502
        (folder/'patches').write_text(''.join(' '.join(map(str,patch))+'\n' for patch in patches))
        exe = folder/'search'
        subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',str(HERE/'parallel_orbits.cpp'),'-o',str(exe)],check=True)
        text=subprocess.check_output([str(exe),str(obs),str(folder/'patches')],text=True)
        best=int(text.splitlines()[-1].split()[2]);assert best==8881
        print('PASS: two complete parallel translation orbits of individually minimum classes have optimum',best)

if __name__ == '__main__':
    arg=argparse.ArgumentParser(description=__doc__)
    arg.add_argument('--curve',type=Path,default=HERE.parent/'curve')
    run(arg.parse_args().curve)
