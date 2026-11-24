"""Finite inputs of the R1/R2 sharp-nine observer proof (stdlib only)."""
from itertools import combinations
from math import gcd, isqrt, prod
import json

A = frozenset([1,2,10,11,12,16,17,22,25,26,30,31,32])
ps = (5,7)
def masks(D):
    return {frozenset(t for t in D if t % p == j) for p in ps for j in range(p)} - {frozenset()}
def digit_cost(e):
    v=0
    for p in range(2,isqrt(e)+1):
        while e % p == 0:
            v += p-1
            e //=p
    return v + e-1
def min_cover(D, todo, avoid):
    pool=sorted((m for m in masks(D) if avoid not in m), key=lambda m:tuple(sorted(m)))
    for k in range(len(pool)+1):
        for xs in combinations(pool,k):
            if todo <= frozenset().union(*xs):
                return k
    raise AssertionError("No line cover")
base_by_row = {str(r):min_cover(A,A-{r},r) for r in sorted(A)}
assert min(base_by_row.values())==4
assert max(map(len,masks(A))) == 5
# Verify the three phase copies r=0,1,2 in n=8+12(r+3w).
for r in range(3):
    D=frozenset((v-r)*pow(3,-1,35)%35 for v in A)
    assert max(map(len,masks(D)))==5
    assert min(min_cover(D,D-{t},t) for t in D)==4
    for g in (5,7):
        assert all(len(D-{v for v in D if v%g==t%g})>=8 for t in D)
# Each factor p in e costs p-1; if cost<=4 all p<=5 and exponent
# is at most 4/(p-1). This product bound exhausts, not a search cutoff.
E={2**a*3**b*5**c for a in range(5) for b in range(3) for c in range(2) if a+2*b+4*c<=4}
assert E=={1,2,3,4,5,6,8,9,12,16}
assert all(digit_cost(e)<=4 for e in E)
H=set()
for g in (1,5,7,35):
    for e in E-{5}:
        h=g*e
        if gcd(h,35)==g and digit_cost(e)+{1:0,5:2,7:2,35:4}[g]<=4:
            H.add(h)
D={d for h in H for d in range(1,36*h+1) if d//gcd(d,36)==h}
assert max(H)==35 and max(D)==1260
def prime_factors(n):
    r=[]
    for p in range(2,isqrt(n)+1):
        if n%p==0:
            r.append(p)
            while n%p==0:
                n//=p
    if n>1: r.append(n)
    return r

def phi_eval(d):
    fs=prime_factors(d)
    top=bot=1
    for k in range(len(fs)+1):
        for ps in combinations(fs,k):
            v=(1 << (d//prod(ps)))-1
            if k%2: bot*=v
            else: top*=v
    return divmod(top,bot)

high_orders={}
for d in D:
    if d//gcd(d,36)!=35: continue
    value,remainder=phi_eval(d)
    assert not remainder and ((1<<d)-1)%value==0
    assert all(gcd(value,(1<<(d//p))-1)==1 for p in prime_factors(d))
    high_orders[d]=value
assert set(high_orders)=={35,70,105,140,210,315,420,630,1260}
S2=11356718000553566643685496313583434507970452519839503606327232707476034989690
assert gcd(S2,prod(high_orders.values()))==71*281*29191
for q,d in [(2521,1260),(983431,315),(1711081,1260),(430839361,1260)]:
    assert all(q%i for i in range(2,isqrt(q)+1))
    assert high_orders[d]%q==0
    assert pow(2,d,q)==1
    assert all(pow(2,d//p,q)!=1 for p in prime_factors(d))
assert max(12*f for f in (7,10,14,28,35,70))==840
print(json.dumps({"row_line_cover_minima":base_by_row,"nonempty_line_max_size":5,
 "possible_local_normalized_periods_before_incidence":sorted(E),
 "phase_branch_permitted_h":sorted(H),"phase_branch_permitted_d":sorted(D),
 "coprime_phase_bound":840,"observed_sharp_order":1260,"witness_prime":2521,
 "complete_h35_cyclotomic_values":high_orders,
 "new_explicit_necessary_primes":[983431,1711081,430839361],
 "arithmetic":"standard-library scalar only"},indent=2))
