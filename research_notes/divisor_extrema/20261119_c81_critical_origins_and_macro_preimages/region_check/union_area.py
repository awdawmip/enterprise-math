"""Exact overlap-aware mass bounds for the union of the h-only and grid certificates."""
import argparse
from fractions import Fraction as F
from functools import cache
import json
from pathlib import Path
from endpoint_certificate import BITS, Q, START, zero_bracket
from crosscheck_region import power_bracket

@cache
def powered_a(i):
    return power_bracket(i,4*Q,8,15,BITS)

def union_mass(intervals,lower):
    merged=[]
    for l,r in sorted(intervals):
        if l>=r:
            continue
        if merged and l<=merged[-1][1]:
            merged[-1][1]=max(merged[-1][1],r)
        else:
            merged.append([l,r])
    if lower:
        return sum(powered_a(r)[0]-powered_a(l)[1] for l,r in merged)
    return sum(powered_a(r)[1]-powered_a(l)[0] for l,r in merged)

def area(row,strips,start=START):
    n=row['n']
    assert Q % n == 0 and strips % n == 0
    bands=[[] for _ in range(n)]
    for i,l,r in row['row_runs']:
        for j in range(l,r):
            bands[j].append((4*Q*i//n,4*Q*(i+1)//n))
    cuts=sorted({F(4*i,strips) for i in range(strips+1)}|{start})
    powers=[power_bracket(d.numerator,4*d.denominator,4,9,BITS) for d in cuts]
    roots={d:(zero_bracket(d,True),zero_bracket(d,False)) for d in cuts if d>=start}
    lo=hi=0
    for k,(u,v) in enumerate(zip(cuts,cuts[1:])):
        fixed=bands[int(u*n/4)]
        inner=outer=[]
        if u>=start:
            inner=[(roots[u][0][1],roots[v][1][0])]
            outer=[(roots[v][0][0],roots[u][1][1])]
        lo+=union_mass(fixed+inner,True)*(powers[k+1][0]-powers[k][1])
        hi+=union_mass(fixed+outer,False)*(powers[k+1][1]-powers[k][0])
    return [lo*10**12//(1<<(2*BITS)),-((-hi*10**12)//(1<<(2*BITS)))]

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--certificates',required=True,type=Path)
    parser.add_argument('n',type=int,nargs='+')
    parser.add_argument('--strips',type=int,default=1024)
    parser.add_argument('--weak',action='store_true')
    args=parser.parse_args()
    records=json.loads(args.certificates.read_text())
    for n in args.n:
        row=next(r for r in records if r['n']==n and r.get('strong',True))
        print(n,args.strips,area(row,args.strips,F(1119,1000) if args.weak else START),flush=True)
