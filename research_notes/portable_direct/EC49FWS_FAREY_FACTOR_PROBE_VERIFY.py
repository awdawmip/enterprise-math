#!/usr/bin/env python3
"""Exact static CRT + determinant-one Farey trace verification for BRC16943.
Uses integer arithmetic, standard library only; no native six-dimensional dynamics.
"""
import collections
import itertools
import math
import json

# Frozen P10 predicate and affine-word construction, reproduced independently.
SLOPES = {(0,0):{3}, (0,1):{0,3,4,5}, (1,0):{2,3,4,5}, (1,1):{2,3}}

def predicate(h,k):
    h,k=h%10,k%10
    if h%5==0 and k%5==0: return False
    slope=5 if h%5==0 else (k*pow(h,-1,5))%5
    return slope in SLOPES[(h%2,k%2)]

def supports():
    out=set(); dirs=0
    for a,b in itertools.product(range(10),repeat=2):
        if math.gcd(math.gcd(a,b),10)!=1: continue
        dirs+=1
        h,k=next((h,k) for h,k in itertools.product(range(10),repeat=2)
                 if ((b-a)*h-a*k+1)%10==0)
        out.add(sum(1<<t for t in range(10) if predicate(h+a*t,k+(b-a)*t)))
    assert dirs==72 and len(out)==50
    return sorted(out)

def convolution(mask,n):
    return tuple(sum(((mask>>i)&1)*((mask>>((c-i)%n))&1)
                     for i in range(n)) for c in range(n))

def spectrum(ku,kv,nu,nv):
    return bytes(2*(nu*nv-x*y) for x in ku for y in kv)

Q = 11
ALL = (1 << Q) - 1
GROUPS = ((1,4,6,9),(2,7),(3,8))
FAREY_FACTORS = [ALL] + [ALL ^ (1 << r) for r in range(Q)]

def distance(pair, sites):
    (u,v),(w,v2) = pair
    assert v == v2
    return sum(bool(((u^w)>>j)&1) and bool((v>>b)&1) for j,b in sites)

def to_canonical_minus(a,b, words):
    assert 0<a<b and math.gcd(a,b)==1
    h0,n0 = next((h,n) for h in range(-b,b+1) for n in range(-b,b+1)
                 if (b-a)*h-a*n==-1)
    x,y=next((x,y) for x,y in itertools.product(range(10),repeat=2)
             if ((b-a)*x-a*y+1)%10==0)
    offsets=[t for t in range(10) if (h0+a*t-x)%10==0 and (n0+(b-a)*t-y)%10==0]
    assert len(offsets)==1
    t0=offsets[0];h1=h0+a*t0;n1=n0+(b-a)*t0
    U=sum(1<<t for t in range(10) if predicate(h1+a*t,n1+(b-a)*t))
    assert U in words
    L0=(9*h1+10*n1)%11; D=(9*a+10*(b-a))%11
    assert L0 or D
    hole = (-L0*pow(D,-1,11))%11 if D else None
    V= ALL ^ (1<<hole) if hole is not None else ALL
    for t in range(110):
        hh,nn=h1+a*t,n1+(b-a)*t
        direct=predicate(hh,nn) and (9*hh+10*nn)%11 != 0
        product=bool((U>>(t%10))&1) and bool((V>>(t%11))&1)
        assert direct==product
    return {"a":a,"b":b,"rephase_t0":t0,"h1":h1,"n1":n1,
            "U_mask":U,"V_mask":V,"mod11_excluded":hole,
            "determinant_direction":"b*h-a*d=-1","period_tested":110}

def main():
    words=supports()
    ku={u:convolution(u,10) for u in words}
    f=collections.defaultdict(list)
    for v in FAREY_FACTORS:
        kv=convolution(v,11)
        for u in words:
            f[spectrum(ku[u],kv,u.bit_count(),v.bit_count())].append((u,v))
    pairs=[p for p in f.values() if len(p)==2]
    assert len(f)==478 and len(pairs)==122
    assert all(len(p)<=2 for p in f.values())
    assert all(a[1]==b[1] for a,b in pairs)
    # Needed minimal hitting groups and r-fold Hamming separation;
    # sampling first k columns suffices by permutation symmetry of the missing column.
    distances=[]
    for k in (1,2,3,4):
        sites={(j,v) for v in range(k) for j in (1,2,3)}
        mn=min(distance(p,sites) for p in pairs)
        assert mn == k-1
        distances.append({"columns":k,"physical_probes":3*k,"minimum_hamming_distance":mn,
                          "optimal_layouts":str(math.comb(11,k)**3 * 16**k)})
    # Each difference group occurs for an equal-mass pair for every V;
    # check the concrete worst-case missing-column construction.
    for group in GROUPS:
        pair_U=next((a,b) for a,b in itertools.combinations(words,2)
                    if tuple(j for j in range(10) if ((a^b)>>j)&1)==group
                    and a.bit_count()==b.bit_count()
                    and tuple(2*(a.bit_count()-x) for x in ku[a])
                     ==tuple(2*(b.bit_count()-x) for x in ku[b]))
        for exc in range(11):
            v=ALL^(1<<exc)
            assert spectrum(ku[pair_U[0]],convolution(v,11),pair_U[0].bit_count(),v.bit_count())==\
                spectrum(ku[pair_U[1]],convolution(v,11),pair_U[1].bit_count(),v.bit_count())
    anchors=[(1,2),(1,3),(2,3),(3,7),(5,11),(8,13),(11,37)]
    bridges=[to_canonical_minus(a,b,words) for a,b in anchors]
    # The theorem's one-hole/full restriction is exact for the determinant-one branch.
    assert all(x['V_mask'] in FAREY_FACTORS for x in bridges)
    return {'status':'ALL PASS','frozen_pin':'BRC16943','model':'complete indexed reflection spectrum, frozen P10 U, V full or exactly one exclusion modulo 11',
            'ten_supports':len(words),'possible_mod11_factors':len(FAREY_FACTORS),
            'static_product_states':len(words)*len(FAREY_FACTORS),
            'distinct_spectrum_fibers':len(f),'two_state_spectrum_fibers':len(pairs),
            'finite_optimum_witnesses':distances,
            'one_error_correcting_fixed_probes':12,'all_one_error_layouts':str(math.comb(11,4)**3 * 16**4),
            'anchors_rephase_110_tests':bridges,
            'scope':'determinant-one minus-side Farey trace affine bridge; no native X6 dynamics, no claim of lower-bound sharpness on restricted actual anchor subset',
            'review':'AUTHOR_PROVED/EXACT_FINITE_CROSSCHECK/PARENT_DEPENDENT/NOT_REVIEWED'}

if __name__=='__main__':
    print(json.dumps(main(),indent=2,ensure_ascii=False))
