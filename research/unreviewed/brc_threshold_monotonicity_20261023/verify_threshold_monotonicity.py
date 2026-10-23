#!/usr/bin/env python3
"""Exact rational author-side checks for a four-label auxiliary BRC theorem."""
from fractions import Fraction as F
import json

G = {3, 6, 10, 12}

def Z(n, z):
    m = n - 2
    return (4 - 2**m - 2*(1-z)*(2+z)**m
            - (1+z)*(2-z)**m + (2-z)*(1+z)**m)

def gap(n, z):
    m = n - 2
    return (2**m + (1-z*z)*(2*(2+z)**m+(2-z)**m)
            - z*(2-z)*(1+z)**m)

def occupancy(word, z):
    dist = {0: F(1)}
    values = [F(0)]
    for action in word:
        if action == 0:
            q = [0, 1+z, 1-z, 1]
        elif action == 2:
            q = [1, 1, 0, 1]
        else:
            raise ValueError("single-pulse actions only")
        next_dist = {}
        for mask, weight in dist.items():
            for i, p in enumerate(q):
                if p:
                    dest = mask | (1<<i)
                    next_dist[dest] = next_dist.get(dest,F(0))+weight*p/3
        dist = next_dist
        assert sum(dist.values(),F(0)) == 1
        values.append(sum((dist.get(mask,F(0)) for mask in G),F(0)))
    return values

def check():
    zs = [F(0),F(1,7),F(1,3),F(1,2),F(7,10),
          F(9,10),F(99,100),F(999,1000),F(1)]
    counts = dict(difference_identity=0,difference_strict_positive=0,
                  occupancy_postpulse_increment=0,residual_increment=0,
                  peak_freeze=0,root_interval=0,root_order=0)
    for n in range(4,111):
        for z in zs:
            assert Z(n,z)-Z(n+1,z) == gap(n,z)
            counts["difference_identity"] += 1
            if z<1:
                assert gap(n,z)>0
                counts["difference_strict_positive"] += 1
            else:
                assert gap(n,z)==0 and Z(n,z)==Z(n+1,z)==2
    for k in range(4,13):
        for n in range(k+1,28):
            for z in zs:
                delta = occupancy([0]*(k-1)+[2]+[0]*(n-k),z)
                maxima = [max(delta[:i+1]) for i in range(n+1)]
                residual = [F(0)]*(n+1)
                pos = F(0)
                for t in range(2,n+1):
                    pos += max(delta[t]-delta[t-1], F(0))
                    residual[t] = pos-maxima[t]
                for t in range(k,n+1):
                    assert maxima[t]==maxima[k-1]
                    counts["peak_freeze"] += 1
                assert delta[n]-delta[n-1]==Z(n,z)/3**n
                counts["occupancy_postpulse_increment"] += 1
                assert residual[n]-residual[n-1]==max(Z(n,z),F(0))/3**n
                counts["residual_increment"] += 1
    old_hi = F(0)
    for n in range(4,45):
        lo,hi = F(0),F(1)
        assert Z(n,lo)<0<Z(n,hi)
        for _ in range(128):
            mid=(lo+hi)/2
            if Z(n,mid)<0: lo=mid
            elif Z(n,mid)>0: hi=mid
            else: lo=hi=mid; break
        assert Z(n,lo)<=0<=Z(n,hi)
        counts["root_interval"]+=1
        if n>4:
            assert old_hi<lo
            counts["root_order"]+=1
        old_hi=hi
    for k in range(4,13):
        for n in range(k+1,28):
            d=occupancy([0]*(k-1)+[2]+[0]*(n-k),F(1))
            s=sum((max(d[t]-d[t-1],F(0)) for t in range(2,n+1)),F(0))
            assert s-max(d)==F(1,3**k)-F(1,3**n)
    return {"status":"ALL_EXACT_TESTS_PASSED","method":"stdlib fractions; independent 16-state occupancy DP","counts":counts,"claim_scope":"finite author-side tests; the all-n claims use written algebraic proofs"}

if __name__=="__main__":
    print(json.dumps(check(),indent=2))
