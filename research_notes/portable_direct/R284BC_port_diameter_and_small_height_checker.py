#!/usr/bin/env python3
"""Exact standard-library reproducer for R284BC (2026-11-20).

No network, packages, floats or randomness. The complete finite alphabet
C in {1,2}^{2x2} and all bounded integer controls are enumerated.
"""
import json
import math
from itertools import product

MATRICES = list(product((1, 2), repeat=4))

def response2(c, d0, d1, z):
    a, b, c10, d = c
    return (d0-a)*(d1-d) - (b+z)*c10

def scan(K, signed):
    diagonals = range(-K, K+1) if signed else range(K+1)
    zvalues = range(-K, K+1) if signed else range(K+1)
    tried = 0
    successes = 0
    best = 0
    first = None
    for d0, d1, z in product(diagonals, diagonals, zvalues):
        v = sorted(response2(c,d0,d1,z) for c in MATRICES)
        distinct = len(set(v))
        tried += 1
        best = max(best,distinct)
        if distinct == len(MATRICES):
            successes += 1
            if first is None:
                first = {'d0':d0,'d1':d1,'z':z,'outputs':v,
                         'min_gap':min(b-a for a,b in zip(v,v[1:]))}
    return {'K':K,'settings_examined':tried,
            'max_distinct':best,'injective_settings':successes,
            'first_injective_witness':first}

def smallest_integer_power_at_least(num, den, power):
    lo, hi = 0, 1
    while den*hi**power < num:
        hi *= 2
    while lo < hi:
        mid = (lo+hi)//2
        if den*mid**power >= num:
            hi=mid
        else:
            lo=mid+1
    return lo

def old_K(n,H):
    return max(0, smallest_integer_power_at_least(H**(n*n)-1,2*math.factorial(n),n)-H)

def diameter_K(n,H,delta_twice_floor=0):
    # Exact integer packing gap Delta = floor(2*delta)+1.
    num = (H**(n*n)-1)*(delta_twice_floor+1)
    den = n*math.factorial(n)*(H-1)
    k = max(0,smallest_integer_power_at_least(num,den,n-1)-H)
    assert den*(H+k)**(n-1)>=num
    if k>0:
        assert den*(H+k-1)**(n-1)<num
    return k

def main():
    signed = [scan(k,True) for k in range(10)]
    nonnegative = [scan(k,False) for k in range(11)]
    assert all(row['injective_settings']==0 for row in signed[:9])
    assert all(row['injective_settings']==0 for row in nonnegative[:10])
    assert signed[9]['injective_settings']==8
    assert nonnegative[10]['injective_settings']==2
    assert signed[9]['first_injective_witness']['min_gap']==1
    assert nonnegative[10]['first_injective_witness']['min_gap']==1
    assert len(MATRICES)==16
    bounds = []
    for n,H in [(2,2),(3,2),(4,2),(8,2),(16,2),(32,2),(8,3),(16,3),(3,3),(4,3)]:
        bounds.append({'n':n,'H':H,'prior_AY_integer_K_lower_bound':old_K(n,H),
                       'BC_diameter_integer_K_lower_bound':diameter_K(n,H),
                       'BC_delta_half_integer_K_lower_bound':diameter_K(n,H,1)})
    diameter_checks=0
    for row in signed:
        k=row['K']
        if k in (0,4,8,9):
            for x,y,z in product(range(-k,k+1),repeat=3):
                outs=[response2(c,x,y,z) for c in MATRICES]
                assert max(outs)-min(outs) <= 2*math.factorial(2)*(2-1)*(2+k)**1
                diameter_checks+=1
    result={'schema':'R284BC_EXACT_VERIFICATION_V1',
            'date':'2026-11-20',
            'scope':'auxiliary 2x2 signed/nonnegative one-row star determinant; exact bounded-height scan',
            'candidate_count':len(MATRICES),
            'signed':signed,'nonnegative':nonnegative,
            'bound_examples':bounds,'direct_diameter_checks':diameter_checks,
            'status':'PASS','independent_review':'NOT_REVIEWED'}
    print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
if __name__ == '__main__':
    main()
