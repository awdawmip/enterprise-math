"""Validate additional first-divergence stocks with GMP integer interval propagation."""
from argparse import ArgumentParser
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import subprocess
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from stock_decoder import span,widths,ends,edge


def header(cap,first):
    maxr=cap-2
    lines=[f'{cap} {first} {maxr}']
    for r in range(maxr+1):
        for c in range(2,cap+1):
            lines.append(' '.join(map(str,(*span(r,c),*widths(r,c)))))
            if not r:lines.append(' '.join(map(str,ends(c))))
            else:
                for m in range(c-1):lines.append(' '.join(map(str,edge(r,c,m))))
    return '\n'.join(lines)+'\n'


def main(args):
    batch=header(args.last,args.first)
    points=[(r,c) for c in range(args.first,args.last+1) for r in range(2,c-1) if c>r+1+r//51]
    with TemporaryDirectory() as temp:
        exe=Path(temp)/'proof'
        subprocess.run(['g++','-O3','-std=c++17',str(Path(__file__).with_name('region_search.cpp')),'-lgmpxx','-lgmp','-o',str(exe)],check=True)
        def compute(points):
            inp=batch+''.join(f'{r} {c}\n' for r,c in points)
            out=subprocess.run([str(exe)],input=inp,text=True,check=True,capture_output=True).stdout
            rows=[list(map(int,line.split())) for line in out.splitlines()]
            assert [tuple(x[:2]) for x in rows]==points
            return rows
        with ThreadPoolExecutor(max_workers=args.jobs) as pool:
            parts=list(pool.map(compute,[points[k::args.jobs] for k in range(args.jobs)]))
    rows=sorted((z for row in parts for z in row),key=lambda x:(x[1],x[0]))
    return dict(stocks=[args.first,args.last],tested=len(points),split_pairs=sum(z[2] for z in rows),
                rational_leaf_comparisons=sum(z[3] for z in rows),deepest_split=max(z[4] for z in rows),rows=rows)

if __name__=='__main__':
    p=ArgumentParser(description=__doc__)
    p.add_argument('--first',type=int,default=29)
    p.add_argument('--last',type=int,default=32)
    p.add_argument('--jobs',type=int,default=4)
    args=p.parse_args()
    assert 3<=args.first<=args.last
    print(json.dumps(main(args),indent=2))
