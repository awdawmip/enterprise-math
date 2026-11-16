#!/usr/bin/env python3
"""Constructive finite test for unit60 all-radius X6 signed G-shell support obstruction.
General proof uses Lagrange's four-square theorem; the computation checks an
exact finite horizon, not the unbounded theorem. No new native adjacency.
"""
from math import factorial, isqrt
from collections import Counter
import json

N=10000
pairs={}
for a in range(isqrt(N)+1):
    for b in range(a,isqrt(N-a*a)+1):
        pairs.setdefault(a*a+b*b,(a,b))

# Construct 0..N four-square witnesses from two independent square pairs.
four={}
values=sorted(pairs)
for u in values:
    for v in values:
        s=u+v
        if s>N:break
        if s not in four: four[s]=pairs[u]+pairs[v]

missing=[n for n in range(N+1) if n not in four]
if missing:raise AssertionError(('four-square construction failed',missing[:8]))

# Apply (1,1,a,b,c,d) with four squares of n-2 to witness >=3 axes.
for n in range(3,N+1):
    v=(1,1)+four[n-2]
    if len(v)!=6 or sum(x*x for x in v)!=n or sum(x!=0 for x in v)<3:
        raise AssertionError(('six-axis support witness failed',n,v))

def two_square_prime_criterion(n):
    tmp=n; p=2
    while p*p<=tmp:
        expo=0
        while tmp%p==0:
            tmp//=p;expo+=1
        if expo%2 and p%4==3:return False
        p+=1
    return tmp%4!=3

criterion_failed=[n for n in range(1,N+1) if ((n in pairs)!=two_square_prime_criterion(n))]
if criterion_failed:raise AssertionError(('two-square criterion mismatch',criterion_failed[:8]))

# Sieve primes in the 3 mod 4 class to validate the infinite family witness.
prime=[True]*(N+1)
prime[0]=prime[1]=False
for p in range(2,isqrt(N)+1):
    if prime[p]:
        for q in range(p*p,N+1,p):prime[q]=False
p3=[p for p in range(3,N+1,4) if prime[p]]
if any(p in pairs for p in p3):raise AssertionError('3-mod-4 prime has pair-only representation')

def lower_bound(n):
    # Signed-permutation orbit of one explicit nonzero support>=3 witness.
    z=(1,1)+four[n-2]
    mag=sorted(x for x in z if x)
    support=len(mag)
    multiplicity=1
    for v in Counter(mag).values():multiplicity*=factorial(v)
    orbit=factorial(6)//factorial(6-support)//multiplicity*2**support
    brc=factorial(sum(mag))
    for x in mag:brc//=factorial(x) # exact sequential division? not guaranteed at intermediate; factorial divisible by every factorial x, eventual product, yes each partial divisor divides.
    return dict(g=n,native_witness=list(z),support=support,signed_permutation_orbit_endpoints=orbit,
                brc_per_endpoint=brc,certified_missing_brc_mass_lower_bound=orbit*brc)

result={
    'schema':'X6_G_SHELL_INFINITE_SUPPORT_OBSTRUCTION_UNIT60_V1',
    'status':'AUTHOR_EXECUTED_FINITE_VERIFICATION_UNREVIEWED_NOT_ADMITTED',
    'frozen_p000':'59538f585d037d09ef687b28715c4bc1a3f9fe03',
    'finite_checked_g_range':[1,N],
    'all_n_ge3_constructive_four_square_lifts_verified':N-2,
    'pair_representable_positive_count':sum(n in pairs for n in range(1,N+1)),
    'pair_absent_positive_count':sum(n not in pairs for n in range(1,N+1)),
    'pair_absent_count_g1_to_512':sum(n not in pairs for n in range(1,513)),
    'three_mod_four_primes_up_to_N':len(p3),
    'g1_to_512_agrees_unit59':sum(n not in pairs for n in range(1,513))==332,
    'example_orbit_lower_bounds':[lower_bound(n) for n in (3,25,512,10000)],
    'unbounded_proof_uses':'Lagrange four-square theorem + Fermat two-square criterion; infinite 3mod4 primes also has elementary Euclid argument',
}
if not result['g1_to_512_agrees_unit59']:raise AssertionError('unit59 comparison failed')
print(json.dumps(result,indent=2,sort_keys=True))
print('UNIT60_PASS',result['all_n_ge3_constructive_four_square_lifts_verified'],result['pair_absent_positive_count'],result['three_mod_four_primes_up_to_N'])
