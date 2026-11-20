"""Rebuild the selected complete affine families and replay the moment checks.

The source lower directory supplies the previously published exact-cover code
and its two coordinate-margin headers. No binary candidate cache is needed.
"""
import argparse
import json
import shutil
import struct
import subprocess
from concurrent.futures import ThreadPoolExecutor
from itertools import permutations, product
from pathlib import Path
from tempfile import TemporaryDirectory

from verify_mixed_moments import verify

HERE = Path(__file__).resolve().parent
POINTS = tuple(product(range(5), repeat=3))


def actions():
    return [[25*((p[perm[0]]*signs[0]*scale)%5)
             + 5*((p[perm[1]]*signs[1]*scale)%5)
             + (p[perm[2]]*signs[2]*scale)%5 for p in POINTS]
            for perm in permutations(range(3))
            for signs in product((1, -1), repeat=3) for scale in (1, 2)]


def build_bank(work):
    linear = actions()
    source = json.loads((HERE / 'class_representatives.json').read_text())
    types = []
    with (work / 'bank').open('wb') as out:
        for family in source['families']:
            types.append((family['size'], family['cost']))
            all_rows = set()
            representative_masks = set()
            for points in family['representatives']:
                oriented = {tuple(sorted(g[i] for i in points)) for g in linear}
                orbit = set()
                for row in oriented:
                    for a, b, c in POINTS:
                        orbit.add(sum(1 << (25*((POINTS[i][0]+a)%5)
                                            +5*((POINTS[i][1]+b)%5)
                                            +(POINTS[i][2]+c)%5) for i in row))
                assert not (all_rows & orbit)
                all_rows |= orbit
                representative_masks.add(min(orbit))
            assert len(all_rows) == family['count']
            for mask in sorted(all_rows):
                flag = family['size'] + 256 * (mask in representative_masks)
                out.write(struct.pack('<QQII', mask % (1 << 64), mask >> 64,
                                      family['cost'], flag))
    (work / 'linear').write_text(''.join(' '.join(map(str, row))+'\n' for row in linear))
    shutil.copy2(HERE / 'two_core_orbits.txt', work / 'cores2.txt')
    return types


def run(lower_source, work, output):
    work.mkdir(parents=True, exist_ok=True)
    types = build_bank(work)
    for name, source in [('baseline', lower_source / 'front_orbits.cpp'),
                         ('enhanced', HERE / 'front_moments.cpp'),
                         ('tail', HERE / 'moment_tail.cpp')]:
        subprocess.run(['c++', '-std=c++20', '-O3', '-mpopcnt', '-I', str(lower_source),
                        str(source), '-o', str(work / name)], check=True)
    case = {(9, 557): 2, (10, 744): 5, (11, 936): 2, (11, 944): 1, (12, 1104): 2}
    data = ' '.join(map(str, [9858] + [case.get(t, 0) for t in types]))+'\n'
    (work / 'moment_case.txt').write_text(data)

    def evaluate(name):
        result = subprocess.run([str(work / name), str(work / 'bank'), str(work), str(work)],
                                input=data, capture_output=True, text=True, check=True)
        stem = 'moment_baseline' if name == 'baseline' else 'moment_enhanced'
        (work / (stem+'.log')).write_text(result.stdout)
        (work / (stem+'.stderr')).write_text(result.stderr)

    with ThreadPoolExecutor(max_workers=2) as pool:
        list(pool.map(evaluate, ('baseline', 'enhanced')))
    tail = json.loads((HERE / 'moment_tail.json').read_text())
    free = sum(1 << i for i in tail['free_history_ids'])
    tail_input = f'{free % (1 << 64)} {free >> 64} 3\n'
    for enabled, stem in [(0, 'tail_baseline'), (1, 'tail_enhanced')]:
        result = subprocess.run([str(work / 'tail'), str(work / 'bank'), str(enabled)],
                                input=tail_input, capture_output=True, text=True, check=True)
        (work / (stem+'.log')).write_text(result.stdout)
        (work / (stem+'.stderr')).write_text(result.stderr)
    verify(work / 'bank', work, HERE / 'moment_tail.json', output)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--lower-source', type=Path, required=True)
    p.add_argument('--work', type=Path)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    if a.work is None:
        with TemporaryDirectory() as directory:
            run(a.lower_source.resolve(), Path(directory), a.output.resolve())
    else:
        run(a.lower_source.resolve(), a.work.resolve(), a.output.resolve())
