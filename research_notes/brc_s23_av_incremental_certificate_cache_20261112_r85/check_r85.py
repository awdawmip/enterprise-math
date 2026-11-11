#!/usr/bin/env python3
"""R85 exact incremental cache: auxiliary rational circular-source model only.
Exact rational complete single-time oracle plus separate critical-stratum oracle.
Source/time support is emulated with immutable version snapshots; not the full R82 AVL.
"""
from fractions import Fraction as F
from math import floor,ceil
from random import Random
from pathlib import Path
import json

def frac(z): return z-floor(z)

def member(t,theta,j,x,a,b):
    A,B=frac(a*theta),frac(b*theta)
    z=frac(x+(t-j)*theta)
    if A==B:return False
    return (A<=z<B) if A<B else (z>=A or z<B)

def stable(I,a,b):
    L,U=I
    ka,kb=floor(a*L),floor(b*L)
    assert L<=U and ka==floor(a*U) and kb==floor(b*U)
    assert 0<=a*L-ka<b*L-kb<1 and 0<=a*U-ka<b*U-kb<1
    return ka,kb

def exact_witness(t,I,j,x,a,b):
    L,U=I;ka,kb=stable(I,a,b)
    da=lambda z:x+(t-j-a)*z+ka
    db=lambda z:x+(t-j-b)*z+kb
    for k in range(floor(min(db(L),db(U)))+1,floor(max(da(L),da(U)))+1):
        lo,hi=L,U;closed_lo=closed_hi=True;ok=True
        for slope,offset,strict in ((t-j-a,x+ka-k,False),(t-j-b,x+kb-k,True)):
            if not slope:
                if (offset>=0 and not strict) or (offset<0 and strict):continue
                ok=False;break
            cut=-F(offset,slope)
            lower=(slope>0 and not strict) or (slope<0 and strict)
            if lower:
                if cut>lo:lo,closed_lo=cut,not strict
                elif cut==lo:closed_lo=closed_lo and not strict
            else:
                if cut<hi:hi,closed_hi=cut,not strict
                elif cut==hi:closed_hi=closed_hi and not strict
        if ok and (lo<hi or lo==hi and closed_lo and closed_hi):
            z=lo if lo==hi else (lo+hi)/2
            assert member(t,z,j,x,a,b)
            return z
    return None

def critical_witness(t,I,j,x,a,b):
    L,U=I;ka,kb=stable(I,a,b);points={L,U}
    for slope,off in ((t-j,x),(t-j-a,x+ka),(t-j-b,x+kb)):
        if slope==0:continue
        v,w=sorted((off+slope*L,off+slope*U))
        for k in range(ceil(v),floor(w)+1):
            z=(F(k)-off)/slope
            if L<=z<=U:points.add(z)
    pts=sorted(points)
    return next((z for z in pts+[(l+r)/2 for l,r in zip(pts,pts[1:])]
                 if member(t,z,j,x,a,b)),None)

def group_out(times,anchor,I,j,x,a,b):
    p,q=anchor.numerator,anchor.denominator
    assert times and all(t*p%q==times[0]*p%q for t in times)
    L,U=I;assert L<=anchor<=U
    ka,kb=stable(I,a,b)
    beta=frac(F(times[0]*p%q,q)+x-j*anchor)
    corners=[(t-j)*(z-anchor) for t in (min(times),max(times)) for z in I]
    sm,sp=beta+min(corners),beta+max(corners)
    qlo=min(a*L-ka,a*U-ka);qhi=max(b*L-kb,b*U-kb)
    return ceil(sm-qhi)>floor(sp-qlo)

class Cache:
    def __init__(self,anchor,I,j,x,a,b):
        self.anchor,self.I,self.j,self.x,self.a,self.b=anchor,I,j,x,a,b
        self.certs=[];self.verdict={};self.oracles=0;self.hits=0;self.memo=0
    def seed(self,groups):
        p,q=self.anchor.numerator,self.anchor.denominator
        for r,times in groups.items():
            assert group_out(times,self.anchor,self.I,self.j,self.x,self.a,self.b)
            self.certs.append((r,min(times),max(times)))
    def covered(self,t):
        r=t*self.anchor.numerator%self.anchor.denominator
        return any(rr==r and lo<=t<=hi for rr,lo,hi in self.certs)
    def decide(self,E):
        for t in sorted({t for t,_ in E},reverse=True):
            if self.covered(t):self.hits+=1;continue
            if t in self.verdict:self.memo+=1
            else:
                self.oracles+=1
                self.verdict[t]=exact_witness(t,self.I,self.j,self.x,self.a,self.b)
            if self.verdict[t] is not None:return ('EXISTS_MEMBER',t,self.verdict[t])
        return ('ALL_OUT',None,None)

def run():
    anchor=F(1,16);I=(anchor-F(1,100000),anchor+F(1,100000))
    j,x,a,b=0,F(0),4,8
    groups={0:list(range(16,161,16)),12:list(range(12,157,16))}
    E={(t,0) for g in groups.values() for t in g}
    cache=Cache(anchor,I,j,x,a,b)
    cache.seed(groups)
    initial=sorted({t for g in groups.values() for t in g})
    checks=0;out=0;inside=0;direct=0
    def check():
        nonlocal checks,out,inside,direct
        got=cache.decide(E)
        positive=[]
        for t in sorted({t for t,_ in E}):
            direct+=1
            z=exact_witness(t,I,j,x,a,b)
            if z is not None:positive.append(t)
        assert (got[0]=='EXISTS_MEMBER')==bool(positive)
        if positive:assert got[1] in positive;inside+=1
        else:out+=1
        checks+=1
    check()
    for i in range(80):
        t=initial[i%len(initial)]
        if (t,1) in E:E.remove((t,1))
        else:E.add((t,1))
        check()
    for i in range(40):
        t=initial[i%len(initial)]
        removed={(z,k) for z,k in E if z==t}
        E.difference_update(removed);check()
        E.update(removed);check()
    for i in range(40):
        r=0 if i%2==0 else 12
        t=160+16*(i//2+1) if r==0 else 156+16*(i//2+1)
        assert t%16==r
        E.add((t,0));check()
        E.add((t,1));check()
    assert member(4,anchor,j,x,a,b)
    E.add((4,0));check()
    E.remove((4,0));check()
    E.add((4,99));check()

    old=(F(1,4),F(31,120))
    narrow=(F(1,4),F(1,4)+F(1,1200))
    assert exact_witness(40,old,0,F(0),1,2) is not None
    assert exact_witness(40,narrow,0,F(0),1,2) is None
    assert group_out([0],F(1,4),old,0,F(0),1,2)
    assert not group_out([0,40],F(1,4),old,0,F(0),1,2)
    assert member(40,F(31,120),0,F(0),1,2)

    rng=Random(8520261112)
    for k in range(600):
        t=rng.randrange(-120,121)
        J=(anchor,anchor) if k%5==0 else (
            anchor-F(rng.randrange(1,200),1000000),
            anchor+F(rng.randrange(1,200),1000000))
        u=exact_witness(t,J,j,x,a,b)
        v=critical_witness(t,J,j,x,a,b)
        assert (u is None)==(v is None),(t,J,u,v)
    assert (checks,out,inside,direct,cache.oracles)==(244,242,2,6602,41)
    result={'schema':'EM_R85_EXACT_INCREMENTAL_CACHE_V1',
            'frozen_science':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
            'seed':8520261112,'versions':checks,'all_out':out,
            'exists_member':inside,'full_direct_oracle_calls':direct,
            'cached_exact_oracle_calls':cache.oracles,
            'seed_group_certificates':len(cache.certs),
            'covered_time_hits':cache.hits,'memo_hits':cache.memo,
            'independent_critical_stratum_checks':600,
            'positive_interval_shrink_counterexample':True,
            'envelope_expansion_counterexample':True,
            'result':'ALL_ASSERTIONS_PASS',
            'limits':['auxiliary circular model only','exact oracle calls not runtime/bit complexity',
                      'Python set/dict prototype, not full R82 AVL','fixed query signature']}
    Path(__file__).with_name('verification.json').write_text(
        json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print('R85_MIN_PASS',checks,out,inside,direct,cache.oracles)
if __name__=='__main__':run()
