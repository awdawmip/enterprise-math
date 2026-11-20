#!/usr/bin/env python3
"""Exact dependency-free verifier for the R5 fifth-root leading term.
Integer cyclotomic residue vectors and rational traces; no floating point.
The universal Laurent proof is in RESEARCH.md.
"""
from fractions import Fraction as F
from math import prod
import json

P = set(range(214, 315))
S = [
    set(range(214, 219)),
    {214, *range(216, 222)},
    set(range(215, 222)),
    set(range(223, 291)),
    set(range(296, 313)),
]

def eq5(a, b):
    # Phi_5(q) = 1+q+q^2+q^3+q^4
    return len(set(x-y for x,y in zip(a,b))) == 1

def local_values(prices, limit):
    dp = [[0]*5 for _ in range(limit)]
    dp[0][0] = 1
    for p in sorted(prices):
        shift = p % 5
        for n in range(1,limit):
            for r in range(5):
                dp[n][r] += dp[n-1][(r-shift)%5]
    out = {}
    acc = [0]*5
    for m in range(1,limit+1):
        acc = [acc[r]+dp[m-1][r] for r in range(5)]
        out[m] = acc[:]
    return out

def ringmul(a,b):
    c = [F(0)]*5
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[(i+j)%5] += x*y
    return c

def trace5(coeffs, n):
    return sum(a*(4 if (j-n)%5==0 else -1)
               for j,a in enumerate(coeffs))

def main():
    poles = {}
    for mask in range(1,32):
        union = set().union(*(S[j] for j in range(5) if mask & (1<<j)))
        poles[mask] = sum(p%5==0 for p in P-union)
    assert sorted(mask for mask,rank in poles.items() if rank==19) == [1,2]
    assert max(rank for mask,rank in poles.items() if mask not in (1,2)) == 18
    for d in range(6,315):
        assert sum(p%d==0 for p in P) <= 17
    limit = 120
    h0 = local_values(S[0],limit)
    h1 = local_values(S[1],limit)
    for m in range(1,limit+1):
        k,r = divmod(m-1,5)
        expected0 = [k+1,0,0,0,0]
        expected1 = ([k+1,0,0,0,0] if r in (0,2)
                     else [k+1,k+1,0,0,k+1] if r==1
                     else [0]*5)
        assert eq5(h0[m],expected0), ("S0",m)
        assert eq5(h1[m],expected1), ("S1",m)
    inv = [F(1,5),F(-3,5),F(-2,5),F(-1,5),F(0)]
    assert eq5(ringmul([F(1),F(0),F(0),F(0),F(-1)],inv),
               [F(1),F(0),F(0),F(0),F(0)])
    b13 = [inv[j]+(F(44,43) if j==0 else -F(44,43) if j==1 else 0)
           for j in range(5)]
    b2 = [inv[j]+(-F(44,43) if j==2 else F(44,43) if j==4 else 0)
          for j in range(5)]
    v = {
        "m_mod5_1_or_3": [str(trace5(b13,n)) for n in range(5)],
        "m_mod5_2": [str(trace5(b2,n)) for n in range(5)],
        "m_mod5_4_or_0": [str(trace5(inv,n)) for n in range(5)],
    }
    assert v == {
        "m_mod5_1_or_3":["306/43","-306/43","-1","0","1"],
        "m_mod5_2":["2","-2","-263/43","0","263/43"],
        "m_mod5_4_or_0":["2","-2","-1","0","1"],
    }
    assert all(sum(F(x) for x in row)==0 for row in v.values())
    print(json.dumps({
        "status":"PASS",
        "arithmetic":"EXACT_INTEGER_AND_RATIONAL_CYCLOTOMIC",
        "fixed_prices":[214,314],
        "short_separator_sizes":[len(x) for x in S],
        "fifth_root_pole_19_event_masks":[1,2],
        "other_event_max_pole":18,
        "higher_order_d_ge_6_max_free_multiples":17,
        "local_m_checked":[1,limit],
        "P5_product":str(prod(range(220,315,5))),
        "leading_vectors_by_N_mod5":v,
        "review":"NOT_REVIEWED",
    }, ensure_ascii=False,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
