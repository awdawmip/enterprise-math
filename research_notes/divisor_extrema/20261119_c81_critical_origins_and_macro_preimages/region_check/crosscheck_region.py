"""Certified lower bound on globally single-preimage templates. Python 3.10+."""
from dataclasses import dataclass
from fractions import Fraction as F
from functools import cache
import argparse
import json
from itertools import groupby
import math
from pathlib import Path

@dataclass(frozen=True)
class Image:
    ulo: F
    uhi: F
    hlo: object
    hhi: object
    def meets(self, other):
        return not (self.uhi < other.ulo or other.uhi < self.ulo or
                    self.hhi < other.hlo or other.hhi < self.hlo)

@cache
def positive_powers(z, power):
    return z**power

def h(a, d, right_side):
    if a == 1:
        return math.inf if right_side else -math.inf
    m = 7*a**4*d/16
    return 1/(a-1)+5-4*m/(1+m)-5*m*a/(1+m*a)

def image(a0,a1,d0,d1):
    # Images are bounded after raising U/C to the 15th power.
    # Both inputs range on one side of each of the two zero lines.
    right = a0 >= 1
    ea0, ea1 = sorted((abs(1-a0), abs(1-a1)))
    ed0, ed1 = sorted((abs(1-d0), abs(1-d1)))
    def numerator(a, d, ea, ed):
        return (positive_powers(a,57)*positive_powers(d,70)*
                positive_powers(ea,15)*positive_powers(ed,15))
    def denominator(a,d):
        m = 7*a**4*d/16
        return ((1+m)*(1+m*a))**15
    return Image(numerator(a0,d0,ea0,ed0)/denominator(a1,d1),
                 numerator(a1,d1,ea1,ed1)/denominator(a0,d0),
                 h(a1,d1,right), h(a0,d0,right))

class SearchTree:
    def __init__(self, i0,i1,j0,j1, mesh):
        if i1-i0==1 and j1-j0==1:
            self.box = mesh[i0,j0]
            self.children = ()
            return
        if i1-i0>=j1-j0:
            mid=(i0+i1)//2
            ranges=((i0,mid,j0,j1),(mid,i1,j0,j1))
        else:
            mid=(j0+j1)//2
            ranges=((i0,i1,j0,mid),(i0,i1,mid,j1))
        self.children = [SearchTree(*edges,mesh) for edges in ranges]
        left,right=[s.box for s in self.children]
        self.box=Image(min(left.ulo,right.ulo),max(left.uhi,right.uhi),
                       min(left.hlo,right.hlo),max(left.hhi,right.hhi))

    def intersects(self, query):
        if not self.box.meets(query):
            return False
        return not self.children or any(c.intersects(query) for c in self.children)

def power_bracket(num, den, exponent_n, exponent_d, bits=76):
    # Bound (num/den)**(exponent_n/exponent_d) by dyadics with adjacent numerators.
    unit=1<<bits
    a=unit**exponent_d*num**exponent_n
    b=den**exponent_n
    lo,hi=0,unit+1
    while hi-lo>1:
        mid=(lo+hi)//2
        if mid**exponent_d*b <= a:
            lo=mid
        else:
            hi=mid
    return lo, lo+(lo**exponent_d*b!=a)

def cell_masses(n, numerator,denominator):
    nodal=[power_bracket(i,n,numerator,denominator) for i in range(n+1)]
    return [(max(0,v[0]-u[1]),v[1]-u[0]) for u,v in zip(nodal,nodal[1:])]

def runs_by_row(good):
    encoded=[]
    for i, row in groupby(good, key=lambda point: point[0]):
        columns=[point[1] for point in row]
        for _, consecutive in groupby(enumerate(columns), key=lambda item:item[1]-item[0]):
            block=[col for _, col in consecutive]
            encoded.append([i, block[0], block[-1]+1])
    return encoded

def covered(n, brute=False, strong=False):
    assert n%4==0
    s=n//4
    coords=[F(i,s) for i in range(n+1)]
    mesh={(i,j): image(coords[i],coords[i+1],coords[j],coords[j+1])
          for i in range(n) for j in range(n)}
    trees={(k,l):SearchTree(a,b,c,d,mesh) for k,(a,b) in enumerate(((0,s),(s,n)))
           for l,(c,d) in enumerate(((0,s),(s,n)))}
    first=cell_masses(n,8,15)
    second=cell_masses(n,4,9)
    weighted=[0,0]
    good=[]
    for (i,j), shape in mesh.items():
        if j<s: continue
        k=int(i>=s)
        def allowed_competitor(side):
            if strong and coords[j]>=F(9,8):
                return side[0]!=k
            return side!=(k,1)
        competitors=[tree for side,tree in trees.items() if allowed_competitor(side)]
        safe=not any(tree.intersects(shape) for tree in competitors)
        if brute:
            ref=not any(box.meets(shape) for (a,b),box in mesh.items()
                        if allowed_competitor((int(a>=s),int(b>=s))))
            assert safe==ref
        if safe:
            good.append((i,j))
            for end in (0,1):
                weighted[end]+=first[i][end]*second[j][end]
    return dict(n=n,strong=strong,side_counts=[sum(i<s for i,j in good),sum(i>=s for i,j in good)],
                certified_cells=len(good),normalized_mass_1e12=[weighted[0]*10**12//2**152,
                        -((-weighted[1]*10**12)//2**152)],
                row_runs=runs_by_row(good))

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('n',nargs='+',type=int)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--strong',action='store_true')
    parser.add_argument('--compare',type=Path,help='independently generated strong certificate')
    args=parser.parse_args()
    reports=[]
    for n in args.n:
        row=covered(n,brute=n<=32,strong=args.strong)
        print({k:v for k,v in row.items() if k!='row_runs'},flush=True)
        if args.compare:
            assert args.strong
            ref=next(r for r in json.loads(args.compare.read_text()) if r['n']==n)
            assert ref['row_runs']==row['row_runs']
            lo,hi=ref['mass_bounds_1e12']
            l,h=row['normalized_mass_1e12']
            assert max(l,lo)<=min(h,hi)
        reports.append(row)
        if args.output: args.output.write_text(json.dumps(reports,indent=2)+'\n')
