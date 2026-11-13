"""Generate and verify the exact fixed-stock single-column identification certificate."""
import argparse
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from fractions import Fraction as F
from math import comb, prod
from pathlib import Path
from tempfile import TemporaryDirectory


def terminal(stock):
    x = F(840, (stock + 2)*(stock + 3)*(stock + 4))
    y = prod((F(4*n+1, 4*n+4) for n in range(3, stock+1)), start=F(1))
    a = (F(3, 32), F(3, 2), F(6))
    b = (F(15, 32), F(15, 8), F(3))
    return [y*(x*i+j)/(1+x*y*i) for i, j in zip(a, b)]


def header(max_depth, cap, model):
    sys.path.insert(0, str(model.resolve()))
    from stock_decoder import edge
    lines = [f'{max_depth} {cap}']
    for r in range(max_depth+1):
        for c in range(2, cap+1):
            if not r:
                lines.append(' '.join(map(str, terminal(c))))
            else:
                lines.extend(' '.join(map(str, edge(r, c, m))) for m in range(c-1))
    return '\n'.join(lines)+'\n'


def run(args):
    rmax = min(args.depth, args.last-2)
    cases = [(r, c) for c in range(args.first, args.last+1)
             for r in range(1, min(args.depth, c-2)+1) if c > r+1 + r//51]
    assert cases
    with TemporaryDirectory() as tmp:
        exe = Path(tmp)/'first_gap'
        src = Path(__file__).with_name('first_gap.cpp')
        subprocess.run(['g++', '-O3', '-std=c++17', str(src), '-lgmpxx', '-lgmp', '-o', str(exe)], check=True)
        data = header(rmax, args.last, args.model)
        def verify(chunk):
            request = data + ''.join(f'{r} {c}\n' for r,c in chunk)
            child = subprocess.run([str(exe)], text=True, input=request, capture_output=True)
            if child.returncode:
                raise ValueError(child.stderr)
            rows = [list(map(int, line.split())) for line in child.stdout.splitlines()]
            assert [tuple(row[:2]) for row in rows] == chunk
            return rows
        with ThreadPoolExecutor(max_workers=args.jobs) as pool:
            groups = pool.map(verify, [cases[k::args.jobs] for k in range(args.jobs)])
            rows = sorted((row for group in groups for row in group), key=lambda z:(z[1], z[0]))
    return dict(stock_interval=[args.first,args.last], depth=rmax, stocks=len(cases),
                prime=2**61-1,grid_bits=192,subtree_column_limit=120000,scan_limit=180,
                rows_columns=['r','c','splits','modular_comparisons','field_points_tested','exact_checks'],
                totals=[sum(row[i] for row in rows) for i in range(2,6)], rows=rows)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--model', type=Path, required=True, help='C68/decoder containing stock_decoder.py')
    p.add_argument('--first', type=int, required=True)
    p.add_argument('--last', type=int, required=True)
    p.add_argument('--depth', type=int, default=100000)
    p.add_argument('--jobs', type=int, default=3)
    options=p.parse_args()
    assert 2<=options.first<=options.last and options.depth>=1 and options.jobs>=1
    print(json.dumps(run(options), indent=2))
