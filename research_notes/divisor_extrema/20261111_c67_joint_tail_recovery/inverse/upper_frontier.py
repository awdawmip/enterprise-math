"""Exact native maximum over all schedules via hereditary endpoint dominance."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from math import gcd,comb
from pathlib import Path
from dataclasses import dataclass
import json
import sys

@dataclass
class Candidate:
    columns:tuple
    path:tuple
    left:Q
    right:Q
    h:Q
    ways:int


def norm(x,y):
    g=gcd(x,y)
    return (x//g,y//g)


def make(p,q,path,ways=1):
    p0,p1=p;q0,q1=q
    d=p1*q0-q1*p0
    if d<0:
        d=-d;p,q=q,p;p0,p1=p;q0,q1=q
    assert d>0
    return Candidate((p,q),path,Q(d,p0*q0),Q(d,p1*q1),Q(p1*q0,p0*q1),ways)


def lift(e,child,m):
    a,b,h=e
    p,q=(norm(a*y+h*x,a*y+b*x) for x,y in child.columns)
    return make(p,q,(m,)+child.path,child.ways)


def maxima(candidates):
    # Descending left then right handles a shared endpoint; true equality of both
    # identifies the same normalized increasing odds, so co-winners are counted.
    candidates.sort(key=lambda p:(p.left,p.right),reverse=True)
    survivors=[]
    for one in candidates:
        if survivors and one.left==survivors[-1].left and one.right==survivors[-1].right:
            assert one.columns==survivors[-1].columns
            survivors[-1].ways+=one.ways
        elif not survivors or one.right>survivors[-1].right:
            survivors.append(one)
    return survivors


def terminal_forms(c,tail_forms):
    forms=sorted(tail_forms(c),key=lambda x:x[0]/x[1])
    def col(form):
        a,b=form
        frac=(a+b)/b
        return frac.denominator,frac.numerator
    return make(col(forms[-1]),col(forms[0]),(c-2,))


def decimal_bounds(v, digits=12):
    # Integer bounds times 10^exponent, with the requested mantissa length.
    e=len(str(v.numerator))-len(str(v.denominator))
    if (v<Q(10)**e): e-=1
    exponent=e-digits+1
    scaled=v/(Q(10)**exponent)
    return [scaled.numerator//scaled.denominator, -(-scaled.numerator//scaled.denominator),exponent]


def run(limit,maps,tail_forms):
    prev={c:[terminal_forms(c,tail_forms)] for c in range(2,limit+2)}
    rows=[]
    comparisons=0
    max_retained=1
    max_generated=1
    for r in range(1,limit):
        cur={}
        for c in prev:
            candidates=[lift(e,child,m) for m,e in enumerate(maps(r,c)) for child in prev[c-m]]
            comparisons+=len(candidates);max_generated=max(max_generated,len(candidates))
            cur[c]=maxima(candidates);max_retained=max(max_retained,len(cur[c]))
        k=r+1
        finalists=[(cand.h,(k+1-c,)+cand.path,cand.ways) for c in range(2,k+2) for cand in cur[c]]
        mx=max(z[0] for z in finalists)
        winners=[p for val,p,ways in finalists if val==mx]
        assert len(winners)==1 and sum(ways for val,p,ways in finalists if val==mx)==1
        rows.append(dict(k=k,gaps=winners[0],H_minus_one_enclosed=decimal_bounds(mx-1),total_at_scale=comb(2*k-1,k),
                         surviving_at_start=len(finalists),max_frontier_to_date=max_retained))
        if k in (2,3,4,5,16,17,32,limit): rows[-1]['H_minus_one_exact']=str(mx-1)
        prev=cur
        if k%10==0:print(k, len(finalists), max_retained,file=sys.stderr,flush=True)
    return dict(up_to=limit,largest_cell=max_retained,most_before_filter=max_generated,
                candidates_constructed=comparisons,records=rows)


if __name__=='__main__':
    p=ArgumentParser(description=__doc__)
    p.add_argument('--checks',type=Path,required=True)
    p.add_argument('--inherited',type=Path,required=True)
    p.add_argument('--limit',type=int,default=64)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    sys.path[:0]=[str(args.checks.resolve()),str(args.inherited.resolve())]
    from observed_four import tail_forms
    from certify_schedules import block_maps
    args.output.write_text(json.dumps(run(args.limit,block_maps,tail_forms),indent=2)+'\n')
