#!/usr/bin/env python3
"""EC49FWR: exact finite crosscheck, frozen BRC16943 P10 population.
Auxiliary static indexed CRT model; no native Farey/X6 transition.
"""
import itertools
import collections
import math
import json

SLOPES = {(0,0):{3}, (0,1):{0,3,4,5}, (1,0):{2,3,4,5}, (1,1):{2,3}}

def predicate(h,k):
    h,k = h%10,k%10
    if h%5==0 and k%5==0: return False
    slope = 5 if h%5==0 else (k*pow(h,-1,5))%5
    return slope in SLOPES[(h%2,k%2)]

def supports():
    result=set(); directions=0
    for a,b in itertools.product(range(10),repeat=2):
        if math.gcd(math.gcd(a,b),10)!=1: continue
        directions+=1
        h,k=next((h,k) for h,k in itertools.product(range(10),repeat=2)
                 if ((b-a)*h-a*k+1)%10==0)
        result.add(sum(1<<t for t in range(10) if predicate(h+a*t,k+(b-a)*t)))
    assert directions==72 and len(result)==50
    return sorted(result)

def convolution(mask,n):
    return tuple(sum(((mask>>i)&1)*((mask>>((c-i)%n))&1)
                     for i in range(n)) for c in range(n))

def spectrum(ku,kv,nu,nv):
    return bytes(2*(nu*nv-x*y) for x in ku for y in kv)

def read_distance(first,second,sites):
    (u,v),(w,z)=first,second
    assert v==z
    return sum(bool(((u^w)>>j)&1) and bool((v>>b)&1) for j,b in sites)

def main():
    population=supports()
    ku={u:convolution(u,10) for u in population}
    groups=collections.defaultdict(list)
    for u in population:
        groups[tuple(2*(u.bit_count()-x) for x in ku[u])].append(u)
    pairs=[value for value in groups.values() if len(value)==2]
    assert len(groups)==38 and len(pairs)==12 and all(len(x)<=2 for x in groups.values())
    differences={tuple(j for j in range(10) if ((u^w)>>j)&1) for u,w in pairs}
    A,B,C = {1,4,6,9},{2,7},{3,8}
    assert len(differences)==7 and all(any(g.issubset(set(d)) for g in (A,B,C)) for d in differences)
    assert all(any(set(d)==g for d in differences) for g in (A,B,C))
    answer=[]
    for q in (3,7,11):
        fibers=collections.defaultdict(list)
        for v in range(1,1<<q):
            kv=convolution(v,q)
            for u in population:
                fibers[spectrum(ku[u],kv,u.bit_count(),v.bit_count())].append((u,v))
        assert max(map(len,fibers.values()))==2
        collisions=[f for f in fibers.values() if len(f)==2]
        assert all(a[1]==b[1] for a,b in collisions)
        original=[(j,b) for b in range(q) for j in (1,2,3)]
        erasure=[(j,b) for b in range(q) for j in (1,2,3,4,7,8)]
        assert min(read_distance(a,b,original) for a,b in collisions)==1
        assert min(read_distance(a,b,erasure) for a,b in collisions)==2
        # Singleton CRT factor and two-site B-pair certify distance<=2 for any distinct physical probes.
        assert (327,1) in next(f for f in collisions if (327,1) in f)
        assert next(z for z in collisions if (327,1) in z) == [(327,1),(789,1)]
        answer.append(dict(q=q,states=len(population)*((1<<q)-1),
                           indexed_spectra=len(fibers),doubleton_fibers=len(collisions),
                           fixed_no_erasure=3*q,fixed_one_erasure=6*q,
                           optimal_one_erasure_layouts=str(6**q),
                           min_distance_3q=1,min_distance_6q=2,
                           fixed_one_unknown_bit_error='IMPOSSIBLE'))
    return {'status':'ALL PASS','pin':'BRC16943','primitive_directions':72,
            'frozen_supports':50,'ten_defect_signatures':38,
            'ten_equal_spectrum_doubletons':12,
            'distinct_support_differences':[list(x) for x in sorted(differences)],
            'model':'full indexed reflection spectrum known; unknown nonempty odd CRT factor; distinct physical membership site probes',
            'analytic_extension':'fixed 3q for zero erasures; fixed 6q for one erasure; >=2 erasures or one arbitrary error impossible; adaptive 1 or 2',
            'finite_checks':answer,
            'review':'AUTHOR_PROVED/EXACT_FINITE_CROSSCHECK/PARENT_DEPENDENT/NOT_REVIEWED'}

if __name__ == '__main__':
    print(json.dumps(main(),indent=2,ensure_ascii=False))
