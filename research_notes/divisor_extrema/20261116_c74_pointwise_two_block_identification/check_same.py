"""Exact finite first landing, infinite outer-stock comparison certificates."""
from fractions import Fraction as Q
from itertools import combinations
from math import prod
from functools import cache
import argparse
import json


def rising(x, k):
    return prod(range(x, x + k))


def inner_intervals(v):
    rho = Q(4*v+3, v+3)
    y = prod((Q(4*j+1,4*(j+1)) for j in range(3,v+1)),start=Q(1))
    for w in range(v,1,-1):
        tau = rho*Q(28*(4*w+2)*rising(w+3,9),(w+2)*rising(v+4,9))
        u = Q(840,(w+2)*(w+3)*(w+4))
        t = [y*(u*a+b)/(1+u*y*a) for a,b in
             [(Q(3,32),Q(15,32)),(Q(3,2),Q(15,8)),(Q(6),Q(3))]]
        z = [(rho+tau*x)/(1+tau*x) for x in t]
        yield w,(min(z),max(z))
        j=w-1
        rho *= Q(4*j+3,4*(j+3))
        y /= Q(4*w+1,4*(w+1))


@cache
def outer(c,v):
    rho = Q(4*v+5,v+5)*prod((Q(4*j+5,4*(j+5)) for j in range(v+1,c+1)),start=Q(1))
    P = Q((v+4)*rising(c+6,15),28*(4*v+4)*rising(v+5,15))
    return P, P/rho


def rank_invariant(P,Q_,I):
    l,h=I
    return (h-l)/((P+l)*(Q_+h))


def search(limit, start=2, baseline=0):
    report=dict(start=start,end=limit, finite_verified_through=baseline, pairs=0,nested=0,
                left_width_ge_right=0,ordered_at_cutoff=0,
                integer_crossings_bracketed=0,max_bracket=0,collisions=[])
    for v in range(start,limit+1):
        entries=list(inner_intervals(v))
        assert len(set(I for _,I in entries))==len(entries)
        first=max(v,baseline+1)
        p,q=outer(first,v)
        rank0={w:rank_invariant(p,q,I) for w,I in entries}
        widths={w:I[1]-I[0] for w,I in entries}
        @cache
        def cached_rank(c,w):
            return rank_invariant(*outer(c,v), intervals[w])
        intervals=dict(entries)
        for s,t in combinations(entries,2):
            w,I=s
            z,J=t
            if I[0]>J[0]: w,I,z,J=z,J,w,I
            report['pairs']+=1
            if I[0]==J[0] or I[1]>=J[1]:
                report['nested']+=1
                continue
            if widths[z] <= widths[w]:
                report['left_width_ge_right']+=1
                continue
            if rank0[z] >= rank0[w]:
                report['ordered_at_cutoff']+=1
                if rank0[z]==rank0[w]:
                    report['collisions'].append([first,v,w,z])
                continue
            lo,hi=first,2*first
            def compare(c):
                x,y=cached_rank(c,z),cached_rank(c,w)
                return (x>y)-(x<y)
            while compare(hi)<0:lo,hi=hi,hi*2
            while hi-lo>1:
                mid=(hi+lo)//2
                if compare(mid)<0:lo=mid
                else:hi=mid
            report['integer_crossings_bracketed']+=1
            report['max_bracket']=max(hi,report['max_bracket'])
            if compare(hi)==0:report['collisions'].append([hi,v,w,z])
        outer.cache_clear()
    return report


if __name__=='__main__':
    arg=argparse.ArgumentParser()
    arg.add_argument('limit',type=int)
    arg.add_argument('--start',type=int,default=2)
    arg.add_argument('--baseline',type=int,default=0)
    a=arg.parse_args()
    print(json.dumps(search(a.limit,a.start,a.baseline),indent=2))
