#!/usr/bin/env python3
"""R736 exact two-reflection BRC source-order census.

Scope: R735's free three-generator rooted CNB/V17 submonoid, with I/P/Q
representing source-preserving length-three returns. No native-force or
heartbeat arithmetic is asserted.
"""
from collections import defaultdict
from functools import lru_cache
from math import comb, factorial
import json

E = (0, 1, 2)
P = (1, 0, 2)
Q = (2, 1, 0)
THIRD = (0, 2, 1)

def mul(a, b):
    """Composition a after b on 0,1,2."""
    return tuple(a[b[i]] for i in range(3))

PQ = mul(P, Q)
QP = mul(Q, P)
assert len({E, P, Q, THIRD, PQ, QP}) == 6

def parity(g):
    return sum(g[i] > g[j] for i in range(3) for j in range(i+1,3)) % 2

@lru_cache(None)
def S(a, b):
    """Coefficient of (1-x^2-y^2+xy)^(-1), exact recurrence."""
    if a < 0 or b < 0:
        return 0
    if a == 0 and b == 0:
        return 1
    return S(a-2,b) + S(a,b-2) - S(a-1,b-1)

@lru_cache(None)
def census(a, b):
    """Independent permutation-word dynamic program."""
    if a == 0 and b == 0:
        return {E:1}
    ans = defaultdict(int)
    if a:
        for g, n in census(a-1,b).items():
            ans[mul(g,P)] += n
    if b:
        for g, n in census(a,b-1).items():
            ans[mul(g,Q)] += n
    return dict(ans)

def predicted(a, b):
    N = comb(a+b,a)
    if (a+b)%2 == 0:
        z = S(a,b)
        assert (N+2*z)%3 == 0 and (N-z)%3 == 0
        return {E:(N+2*z)//3, PQ:(N-z)//3, QP:(N-z)//3}
    u,v = S(a-1,b),S(a,b-1)
    assert (N+2*u-v)%3 == 0 and (N-u+2*v)%3 == 0 and (N-u-v)%3 == 0
    return {P:(N+2*u-v)//3, Q:(N-u+2*v)//3, THIRD:(N-u-v)//3}

def clean(d):
    return {"".join(map(str,k)):v for k,v in sorted(d.items()) if v}

cases = 0
for n in range(41):
    for a in range(n+1):
        b = n-a
        direct = census(a,b)
        pred = predicted(a,b)
        assert {k:v for k,v in direct.items() if v} == {k:v for k,v in pred.items() if v},(a,b,direct,pred)
        assert sum(direct.values()) == comb(a+b,a)
        assert all(parity(g)==((a+b)%2) for g in direct)
        cases += 1

def enumerate_words(a,b):
    def loop(a,b,g):
        if a+b == 0:
            yield g
        if a:
            yield from loop(a-1,b,mul(g,P))
        if b:
            yield from loop(a,b-1,mul(g,Q))
    counts=defaultdict(int)
    for g in loop(a,b,E):
        counts[g] +=1
    return dict(counts)

for a in range(8):
    for b in range(8):
        if a+b <= 11:
            assert enumerate_words(a,b) == census(a,b)

def central_trinomial(n):
    return sum(factorial(n)//(factorial(j)*factorial(j)*factorial(n-2*j)) for j in range(n//2+1))

balanced=[]
for n in range(1,17):
    tr=central_trinomial(n)
    assert S(n,n) == (-1)**n*tr
    direct=census(n,n)
    num=comb(2*n,n)
    expect=((num+2*(-1)**n*tr)//3,(num-(-1)**n*tr)//3)
    assert direct.get(E,0)==expect[0] and direct.get(PQ,0)==expect[1] and direct.get(QP,0)==expect[1]
    assert 0<tr<=3**n
    balanced.append({"n_each_transposition":n,"loop_count":2*n,"total_orders":num,
                     "central_trinomial":tr,"identity_count":expect[0],
                     "each_three_cycle_count":expect[1],
                     "signed_identity_minus_each_cycle":(-1)**n*tr,
                     "conditional_total_variation_from_uniform": {"numerator":2*tr,"denominator":3*num}})

check_r=[]
for r in range(1,5):
    x=census(2*r,2*r)
    assert (x[E],x[PQ],x[QP]) == [(4,1,1),(36,17,17),(402,261,261),(5028,3921,3921)][r-1]
    check_r.append({"r":r,"history_length":12*r,"counts":clean(x)})

for c in range(5):
    for a in range(8):
        for b in range(8):
            k=c+a+b
            multiplier=comb(k,c)
            assert sum(predicted(a,b).values())*multiplier == factorial(k)//(factorial(a)*factorial(b)*factorial(c))

result={"schema":"EM_R736_FIXED_LEDGER_DIHEDRAL_CENSUS_V1", "status":"PASS",
        "scope":"R735 rooted 3-step I/P/Q free monoid; no native P000 force realization",
        "p":"102","q":"210","third":"021", "rotations":["201","120"],
        "formula":"S_ab=[x^a y^b](1-x^2-y^2+xy)^(-1); N=C(a+b,a). Even a+b: (id,r,r2)=((N+2S)/3,(N-S)/3,(N-S)/3). Odd: (p,q,t)=((N+2u-v)/3,(N-u+2v)/3,(N-u-v)/3), u=S_(a-1,b),v=S_(a,b-1). Add c identity letters: multiply counts by C(a+b+c,c).",
        "certificates":{"exact_dp_cases_a_plus_b_at_most_40":cases,
                         "brute_word_enumeration":"all 0<=a,b<=7 with a+b<=11",
                         "balanced_identity":"S_(n,n)=(-1)^n central_trinomial(n), verified n=1..16",
                         "R735_prior_fixed_fibers":check_r},
        "balanced":balanced}
print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
