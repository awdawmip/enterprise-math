#!/usr/bin/env python3
"""Exact-rational check of full-to-seedless likelihood-ratio compression TV bound.

The analytical theorem in PROOF.md is universal; this program checks the
strictly-positive parametrized family and a finite grid of strategy variants.
All probability arithmetic uses fractions.Fraction.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product

Y = (F(1, 2), F(1), F(3, 2))

def kernels(s):
    return {"a": (F(1, 8) + s, F(3, 4) - 2*s, F(1, 8) + s),
            "b": (F(1, 8), F(3, 4), F(1, 8))}

def tv(x, y):
    return sum((abs(x.get(z, F(0)) - y.get(z, F(0))) for z in set(x)|set(y)), F(0))/2

def actual_policy(e, s, early, mid, final=None):
    """Evaluate full behavioral policy under the reference Q and induced P.

    early: dict a/b continuation probabilities at t=1
    mid: dict a/b continuation probabilities at t=2 (same for u,v)
    final: terminal LR classification, default decide Q exactly at Y=3/2.
    Returns Q-law of (stop time, stopped LR, decision) and Q-mass of
    (time, LR, continue), where the latter is used in the theorem bound.
    """
    q_first = {"a": e, "b": 1-e}
    kern = kernels(s)
    decisions = final or {v: ("Q" if v == F(3,2) else "P") for v in Y}
    joint = defaultdict(F)
    continuing = defaultdict(F)
    for first in ("a", "b"):
        qa = q_first[first]
        pc1 = early[first]
        joint[(1,F(1),"P")] += qa*(1-pc1)
        continuing[(1,F(1))] += qa*pc1
        for middle in ("u","v"):
            qt = qa*pc1/F(2)
            pc2 = mid.get((first,middle),mid.get(first,F(0)))
            joint[(2,F(1),"P")] += qt*(1-pc2)
            continuing[(2,F(1))] += qt*pc2
            for z, k in zip(Y,kern[first]):
                joint[(3,z,decisions[z])] += qt*pc2*k
    return dict(joint),dict(continuing)

def aggregate_lr_policy(e,s,early,mid):
    """Q-conditional action averages for this N=3 family.

    The time-1 LR is always 1, as is the time-2 LR; t=3 actions already
    depend only on LR in this example. This is the seedless construction.
    """
    weights={"a":e,"b":1-e}
    c1=sum((weights[i]*early[i] for i in weights),F(0))
    denom=sum((weights[i]*early[i] for i in weights),F(0))
    c2=(sum((weights[i]*early[i]*mid[i] for i in weights),F(0))/denom
        if denom else F(0))
    return {i:c1 for i in weights},{i:c2 for i in weights}

def observer(q):
    # Q-stopped likelihood ratio is dP/dQ: P-observables are weighted by R_tau.
    return (
        sum((mass*r for (t,r,d),mass in q.items() if d=="Q"),F(0)),
        sum((mass for (t,r,d),mass in q.items() if d=="P"),F(0)),
        sum((mass*r*t for (t,r,d),mass in q.items()),F(0)),
        sum((mass*t for (t,r,d),mass in q.items()),F(0)),
    )
def distribution_checks(q):
    assert sum(q.values(),F(0))==1
    assert sum((r*mass for (_,r,_),mass in q.items()),F(0))==1
    assert all(m>=0 for m in q.values())

def check(e,s,early,mid):
    k=kernels(s)
    assert 0<e<1 and 0<s<F(3,8)
    assert all(p>0 for mass in k.values() for p in mass)
    assert all(sum(ker,F(0))==1 for ker in k.values())
    assert all(sum((z*p for z,p in zip(Y,ker)),F(0))==1 for ker in k.values())
    δ=tv(dict(zip(Y,k['a'])),dict(zip(Y,k['b'])))
    assert δ==2*s
    full,ct=actual_policy(e,s,early,mid)
    ebar,mbar=aggregate_lr_policy(e,s,early,mid)
    compressed,_=actual_policy(e,s,ebar,mbar)
    distribution_checks(full);distribution_checks(compressed)
    assert ct.get((1,F(1)),F(0))<=1
    # All t1 kernels are delta at r2=1 => δ1=0. t2 fiber δ2=2s.
    B=ct.get((2,F(1)),F(0))*δ
    d=tv(full,compressed)
    assert d<=B,(e,s,early,mid,d,B)
    o1,o2=observer(full),observer(compressed)
    # Exact observable errors bounded by oscillations of [r 1_Q, 1_P, tr, t]
    r_min,r_max=Y[0],Y[-1]
    widths=(r_max, F(1), 3*r_max-r_min,F(2))
    assert all(abs(v-u)<=w*B for u,v,w in zip(o1,o2,widths))
    return d,B,o1,o2

def main():
    s=F(1,8)
    early={'a':F(1),'b':F(1)}
    mid={'a':F(1),'b':F(0)}
    for e in (F(1,2),F(1,4),F(1,16),F(1,64)):
        d,B,o1,o2=check(e,s,early,mid)
        assert d == e*(1-e)*2*s
        assert B == e*2*s
        assert o2[0]-o1[0] == -F(3,2)*e*(1-e)*s
        assert o2[1]-o1[1] == e*(1-e)*s
        assert o2[2:] == o1[2:] == (2+e,2+e)
        print('family eta=',e,'s=',s,'delta=',2*s,'B=',B,'TV=',d,'ratio=',d/B)
        print('  O_full=',o1, 'O_seedless=',o2)
    checked=0
    vals=(F(0),F(1,2),F(1))
    # Exhaustive finite grid in the specified 2+2 independent continuation
    # probabilities. The theorem covers general history-dependent decisions.
    for e,s in ((F(1,2),F(1,8)),(F(1,4),F(1,16))):
        for v in product(vals,repeat=4):
            check(e,s,{'a':v[0],'b':v[1]},{'a':v[2],'b':v[3]})
            checked+=1
    # A second N=3 candidate: exact all-signed-support rejection certificate.
    # The single rational signed direction (1,1,0,1/12) is sufficient to
    # reject equality of convex hulls; all deterministic histories are covered.
    e,s,c=F(9,10),F(1,4),F(1,12)
    bayes={F(1,2):"Q",F(1):"P",F(3,2):"P"}
    full_best=None;full_arg=None
    for bits in product((F(0),F(1)),repeat=6):
        early={"a":bits[0],"b":bits[1]}
        mid={("a","u"):bits[2],("a","v"):bits[3],
             ("b","u"):bits[4],("b","v"):bits[5]}
        law,_=actual_policy(e,s,early,mid,bayes)
        val=sum((o*t for o,t in zip(observer(law),(F(1),F(1),F(0),c))),F(0))
        if full_best is None or val<full_best:
            full_best,full_arg=val,bits
    lr_best=None;lr_arg=None
    for first,second in product((F(0),F(1)),repeat=2):
        law,_=actual_policy(e,s,{"a":first,"b":first},{"a":second,"b":second},bayes)
        val=sum((o*t for o,t in zip(observer(law),(F(1),F(1),F(0),c))),F(0))
        if lr_best is None or val<lr_best:
            lr_best,lr_arg=val,(first,second)
    assert full_best==F(511,480),(full_best,full_arg)
    assert lr_best==F(43,40),(lr_best,lr_arg)
    assert lr_best-full_best==F(1,96)
    print('all_signed_direction_certificate=lambda=(1,1,0,1/12)')
    print('candidate_eta=9/10, s=1/4; full_pure_cases=64, seedless_pure_cases=4')
    print('full_min=',full_best,'argmin=',full_arg,'seedless_min=',lr_best,'argmin=',lr_arg,'gap=',lr_best-full_best)
    print('grid_cases=',checked,'; fully exact Fraction arithmetic')
    print('ALL EXACT CHECKS PASSED')
if __name__=='__main__':
    main()
