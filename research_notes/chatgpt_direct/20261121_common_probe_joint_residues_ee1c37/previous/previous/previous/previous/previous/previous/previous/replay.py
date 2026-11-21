"""Rebuild the mathematical certificates and optionally replay archived native runs."""
import argparse
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
CHECKS = {
    'curve': [('curve/recompute_minima.py', None), ('curve/symmetry14.py', None), ('curve/verify.py', 'values.json'), ('curve/open_verify.py', 'open_ranges.json')],
    'bounds': [('bounds/extended.py', 'extended.json'), ('bounds/eight_class_cost.py', 'eight_class_cost.json'), ('bounds/two_deletions.py', 'two_deletions.json')],
    'strata': [('strata/region.py', None)],
    'thirteen': [('thirteen/parallel_orbits.py', None), ('thirteen/spectrum.py', 'spectrum.json')],
    'four': [('four/replay.py', None)],
    'native': [('native/replay.py', None)],
}

def run(group, original):
    for name, expected in CHECKS[group]:
        path = ROOT / name
        cmd = [sys.executable, '-B', str(path)]
        if group == 'native':
            cmd.extend(['--original', str(original)])
        out = subprocess.check_output(cmd, cwd=path.parent, text=True)
        if expected is not None:
            assert json.loads(out) == json.loads((path.parent / expected).read_text()), name
        else:
            print(out, end='', flush=True)
        print('PASS', name, flush=True)

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('groups', nargs='*', help='curve, bounds, strata, thirteen, four, native (default: all)')
    p.add_argument('--original', type=Path, default=ROOT / 'original')
    p.add_argument('--jobs', type=int, default=2)
    a = p.parse_args()
    requested = a.groups or list(CHECKS)
    assert all(g in CHECKS for g in requested) and a.jobs >= 1
    with ThreadPoolExecutor(max_workers=a.jobs) as pool:
        list(pool.map(lambda g: run(g, a.original.resolve()), requested))
