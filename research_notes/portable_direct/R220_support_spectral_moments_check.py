#!/usr/bin/env python3
"""R220: exact rational support-process and principal-ideal moment checker.

Only finite observer combinatorics; no physical BRC simulation.
Python standard library, exact int/Fraction. No external packages.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial
import json
from pathlib import Path


def stirling2(n: int, r: int) -> int:
    if n == 0:
        return int(r == 0)
    if r == 0 or r > n:
        return 0
    row = [1] + [0] * r
    for i in range(1, n + 1):
        new = [0] * (r + 1)
        for j in range(1, min(i, r) + 1):
            new[j] = j * row[j] + row[j - 1]
        row = new
    return row[r]


def full_fibre_weights(m: int, k: int, L: int) -> list[int]:
    assert m >= 1 and k >= 0 and L >= 1
    return [factorial(r) * m ** L * sum(stirling2(L+1, j+1)
            for j in range(min(r, L) + 1)) for r in range(k+1)]


def principal_counts(W: list[int]) -> list[int]:
    k = len(W) - 1
    return [sum(comb(k-r, j-r) * W[j] for j in range(r, k+1))
            for r in range(k+1)]


def support_distribution(p: list[Fraction], n: int) -> dict[int, Fraction]:
    """Exact law of the bitmask of selected tags after n iid events."""
    k = len(p) - 1
    assert n >= 0 and all(x >= 0 for x in p) and sum(p) == 1
    out = {}
    for mask in range(1 << k):
        members = [i+1 for i in range(k) if mask & (1 << i)]
        value = Fraction(0)
        for subset in range(1 << len(members)):
            excluded = len(members) - subset.bit_count()
            q = p[0] + sum((p[members[i]] for i in range(len(members))
                                  if subset & (1 << i)), Fraction(0))
            value += (-1 if excluded % 2 else 1) * q**n
        out[mask] = value
    assert all(v >= 0 for v in out.values()) and sum(out.values()) == 1
    return out


def moment_by_support(p: list[Fraction], W: list[int], n: int, order: int) -> Fraction:
    """Independent subset-zeta calculation of first or second moment."""
    k = len(W) - 1
    assert len(p) == k+1 and order in (1,2)
    q = [p[0] + sum((p[i+1] for i in range(k) if mask & (1 << i)), Fraction(0))
         for mask in range(1 << k)]
    if order == 1:
        return sum((W[mask.bit_count()] * q[mask]**n for mask in range(1 << k)), Fraction(0))
    return sum((W[u.bit_count()] * W[v.bit_count()] * q[u & v]**n
                for u in range(1 << k) for v in range(1 << k)), Fraction(0))


def moment_by_full_distribution(p: list[Fraction], W: list[int], n: int, order: int) -> Fraction:
    Ts = principal_counts(W)
    d = support_distribution(p,n)
    return sum((prob * Ts[mask.bit_count()]**order for mask,prob in d.items()),Fraction(0))


def brute_tag_support(p: list[Fraction], n: int) -> dict[int, Fraction]:
    k = len(p)-1
    ans=Counter()
    for seq in product(range(k+1),repeat=n):
        weight=Fraction(1)
        mask=0
        for t in seq:
            weight*=p[t]
            if t: mask|=1 << (t-1)
        ans[mask]+=weight
    return {s:ans[s] for s in range(1<<k)}


def run():
    tests=0
    enumerated=0
    for m in (1,2,3):
      for k in (0,1,2,3):
       for L in (1,2,3,4):
        W=full_fibre_weights(m,k,L)
        T=principal_counts(W)
        assert T == sorted(T,reverse=True)
        ps=[Fraction(i+1,(k+1)*(k+2)//2) for i in range(k+1)]
        for n in range(L, 7):
            d=support_distribution(ps,n)
            if k<=2 and n<=5:
                brute=brute_tag_support(ps,n)
                assert d==brute,(m,k,L,n,d,brute)
                enumerated+=(k+1)**n
            assert moment_by_support(ps,W,n,1)==moment_by_full_distribution(ps,W,n,1)
            assert moment_by_support(ps,W,n,2)==moment_by_full_distribution(ps,W,n,2)
            tests+=1

    m,k,L=12,6,2
    W=full_fibre_weights(m,k,L)
    T=principal_counts(W)
    p=[Fraction(1,k+1)]*(k+1)
    X={}
    for n in (2,3,4,6,12,24):
        E=moment_by_support(p,W,n,1)
        E2=moment_by_support(p,W,n,2)
        X[str(n)]={"mean_num":E.numerator,"mean_den":E.denominator,
                   "variance_num":(E2-E*E).numerator,"variance_den":(E2-E*E).denominator,
                   "p_all_seen_num":support_distribution(p,n)[(1<<k)-1].numerator,
                   "p_all_seen_den":support_distribution(p,n)[(1<<k)-1].denominator}
    # Uniform-tag source-support spectral recurrence, and complete monotonicity.
    spectral_recurrences=0
    monotone_differences=0
    for kx in range(0,7):
        Wk=full_fibre_weights(2,kx,2)
        poly=[1]  # increasing degree coefficients for product_(j=1)^(k+1) (X-j)
        for root in range(1,kx+2):
            nxt=[0]*(len(poly)+1)
            for j,c in enumerate(poly):
                nxt[j]-=root*c
                nxt[j+1]+=c
            poly=nxt
        def bn(n):
            return sum(comb(kx,r)*Wk[r]*(r+1)**n for r in range(kx+1))
        def en(n):
            return Fraction(bn(n),(kx+1)**n)
        for start in range(2,10):
            assert sum(poly[j]*bn(start+j) for j in range(len(poly)))==0
            spectral_recurrences+=1
            for order in range(1,5):
                signed_delta=sum((-1)**t*comb(order,t)*en(start+t)
                                 for t in range(order+1))
                assert signed_delta>=0
                monotone_differences+=1
    # nonuniform rational case, exact finite deterministic witness
    nonuniform=[Fraction(1,2),Fraction(1,3),Fraction(1,6)]
    assert support_distribution(nonuniform,5)==brute_tag_support(nonuniform,5)
    k2W=full_fibre_weights(2,2,2)
    assert moment_by_support(nonuniform,k2W,5,1)==moment_by_full_distribution(nonuniform,k2W,5,1)
    evidence={"status":"PASS","models":48,"moment_agreements":tests,
              "enumerated_tag_histories":enumerated,"spectral_recurrences":spectral_recurrences,"complete_monotonicity_inequalities":monotone_differences,"arithmetic":"exact Python int/Fraction",
              "scope":"iid tagged finite observer; not native physical BRC execution",
              "frozen_source":"awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34",
              "x6":{"m":m,"k":k,"L":L,"W":W,"T":T,"n_horizon":X},
              "nonuniform_tag_probabilities":[str(x) for x in nonuniform],
              "review":"NOT_REVIEWED"}
    here=Path(__file__).resolve().parent
    (here/"R220_verification.json").write_text(json.dumps(evidence,indent=2,ensure_ascii=False,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"status":"PASS","models":48,"moment_agreements":tests,
                      "enumerated_tag_histories":enumerated,"spectral_recurrences":spectral_recurrences,"complete_monotonicity_inequalities":monotone_differences,"X6_2":X['2'],"X6_12":X['12']},ensure_ascii=False))

if __name__=="__main__":
    run()
