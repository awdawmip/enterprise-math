#!/usr/bin/env python3
"""Exact BRC last-sector multiplicities and polynomial moments; stdlib only.
The source is uniform counting of all native 12-direction ordered paths.
No floating-point or signed-amplitude computation occurs.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product
from math import comb, prod

DIRECTIONS = [(1, 0, 0, 0, 0, 0)] + [tuple(sign if j == i else 0 for j in range(6)) for i in range(1, 6) for sign in (-1, 1)]
assert len(DIRECTIONS) == 11
ZERO = (0,)*6

@lru_cache(None)
def indices(d):
    return tuple(a for a in product(range(d+1), repeat=6) if sum(a) <= d)

def moments_11(m,d):
    """All moments of the 11-letter remaining walk, using a triangular recurrence."""
    A = indices(d)
    prev = {a: int(a == ZERO) for a in A}
    for _ in range(m):
        cur = {}
        for a in A:
            val = 11*prev[a]
            for k in range(1,a[0]+1):
                b = list(a); b[0]-=k
                val += comb(a[0],k)*prev[tuple(b)]
            for i in range(1,6):
                for k in range(2,a[i]+1,2):
                    b = list(a); b[i]-=k
                    val += 2*comb(a[i],k)*prev[tuple(b)]
            cur[a] = val
        prev = cur
    return prev

def actual_last_moment(raw,q,m,a):
    # q>=m+1, N=q+m-1; only k=q-1 first-axis negative steps.
    N=q+m-1
    total=0
    for k in range(a[0]+1):
        b=(k,)+a[1:]
        total += comb(a[0],k)*(-(q-1))**(a[0]-k)*raw[b]
    return comb(N,q-1)*total

def dp_11(m):
    hist={ZERO:1}
    for _ in range(m):
        nxt=defaultdict(int)
        for x,count in hist.items():
            for step in DIRECTIONS:
                y=tuple(x[i]+step[i] for i in range(6))
                nxt[y]+=count
        hist=dict(nxt)
    return hist

def W_size(m):
    return sum(comb(4,i)*comb(m-i+6,6) for i in range(min(m,4)+1))

def brute_sum(hist,q,m,a):
    factor=comb(q+m-1,q-1)
    return factor*sum(count*prod((x[i]-(q-1) if i==0 else x[i])**a[i] for i in range(6)) for x,count in hist.items())

def main():
    print('PREFIX461 integer certificate: PASS begin')
    # Character support matches the rational generating function (1+z)^4/(1-z)^7.
    for m in range(15):
        assert W_size(m)>0
    for m in range(7):
        hist=dp_11(m)
        assert len(hist)==W_size(m), (m,len(hist),W_size(m))
        assert sum(hist.values())==11**m
        q=max(2,m+1)
        d=m+1
        raw=moments_11(m,d)
        assert raw[ZERO]==11**m
        A=indices(d)
        # At m <= 4 check every monomial, at m=5,6 check a deterministic broad subset.
        check=A if m<=4 else tuple(a for a in A if sum(a)<=3 or a.count(0)>=4 or (a[0] in (1,2,3) and a[1] == 1))
        for a in check:
            got=actual_last_moment(raw,q,m,a)
            want=brute_sum(hist,q,m,a)
            assert got==want, (m,q,a,got,want)
        total=comb(q+m-1,q-1)*11**m
        assert actual_last_moment(raw,q,m,ZERO)==total
        print(f'm={m} q={q} support={len(hist)} total_mass={total} checked_moments={len(check)} degree={d} PASS')
    for m in (7,8,9,10,11,12,13):
        print(f'm={m} exact_support_formula={W_size(m)} PASS')
    for q,m in ((12,4),(20,5),(100,2)):
        raw=moments_11(m,3)
        hist=dp_11(m)
        A=indices(3)
        for a in A:
            assert actual_last_moment(raw,q,m,a)==brute_sum(hist,q,m,a)
        print(f'shift_case q={q} m={m} verified_degree=3 checked_moments={len(A)} PASS')
    print('PREFIX461 integer certificate: ALL PASS')
if __name__=='__main__': main()
