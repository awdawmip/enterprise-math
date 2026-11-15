#!/usr/bin/env python3
"""Exact native X6 N=2500 integer certificate for equivariant path-order tie routing.
This is supplementary author-side research, not the original R063 17-gate replay.
"""
from collections import Counter
from math import factorial, isqrt, prod
from itertools import permutations
import sys
import json

N=2500
D=6
EXPECTED_ENDPOINTS=102539052
EXPECTED_MASS=int('46263931428930653590904265855801056735441499817749479001025131238806458196360489958119492948372')
EXPECTED_COUNTS={1:99200892,2:3275520,3:61440,4:1200}
counts=Counter(); masses=Counter(); orbits=0; checks=0


def visit(prefix, remaining, upper):
    global orbits, checks
    if len(prefix)==D-1:
        r=isqrt(remaining)
        if r<=upper and r*r==remaining:
            a=prefix+(r,)
            cc=Counter(a)
            n=sum(x>0 for x in a)
            endpoint_orbit=factorial(D)//prod(factorial(v) for v in cc.values())*2**n
            m=cc[a[0]]
            steps=sum(a)
            B=factorial(steps)//prod(factorial(x) for x in a)
            assert B % factorial(m)==0, (a,m,B)
            counts[m]+=endpoint_orbit
            masses[m]+=endpoint_orbit*B
            orbits+=1; checks+=1
        return
    slots=D-len(prefix)-1
    for a in range(min(upper,isqrt(remaining)),-1,-1):
        rest=remaining-a*a
        if rest<=slots*a*a:
            visit(prefix+(a,),rest,a)


def multiset_words(items):
    counts=Counter(items)
    size=len(items)
    def recur(prefix):
        if len(prefix)==size:
            yield tuple(prefix)
            return
        for k in sorted(counts):
            if counts[k]:
                counts[k]-=1
                yield from recur(prefix+[k])
                counts[k]+=1
    yield from recur([])


def brute_tie_orders(signed_vec):
    seq=[]
    for axis,n in enumerate(signed_vec):
        seq.extend([(axis,1 if n>0 else -1)]*abs(n))
    magnitude=max(map(abs,signed_vec))
    ties={(i,1 if n>0 else -1) for i,n in enumerate(signed_vec) if abs(n)==magnitude}
    histogram=Counter()
    for word in multiset_words(seq):
        seen=set(); ordering=[]
        for symbol in word:
            if symbol in ties and symbol not in seen:
                ordering.append(symbol);seen.add(symbol)
        histogram[tuple(ordering)]+=1
    expected=factorial(len(seq))//prod(factorial(abs(n)) for n in signed_vec)
    assert set(histogram)==set(permutations(ties))
    assert sum(histogram.values())==expected
    assert set(histogram.values())=={expected//factorial(len(ties))}
    return {'vector': list(signed_vec),'tie_count':len(ties),'paths':expected,'orders':len(histogram),'per_order':expected//factorial(len(ties))}

visit((),N,isqrt(N))
assert orbits==3356 and counts==EXPECTED_COUNTS
assert sum(masses.values())==EXPECTED_MASS
assert sum(counts.values())==EXPECTED_ENDPOINTS
assert EXPECTED_MASS%12==0
assert sum(masses[m]//factorial(m)*factorial(m) for m in masses)==EXPECTED_MASS
brute=[brute_tie_orders(z) for z in [(1,1,0,0,0,0),(-2,2,1,0,0,0),(1,1,1,0,0,0),(2,-2,2,1,0,0),(1,-1,1,-1,0,0)]]
result={'schema':'X6_LP011_SIGNED_TIE_ORDER_INTEGRAL_BRC_V1','N':N,'signed_dimensions':D,'sorted_absolute_orbits':orbits,'endpoint_count':sum(counts.values()),'mass_total':str(sum(masses.values())),'ties':{str(m):{'endpoints':counts[m],'paths':str(masses[m]),'integral_mfactorial_quotient_sum':str(masses[m]//factorial(m))} for m in sorted(counts)},'per_signed_axis_integral_allocated_paths':str(EXPECTED_MASS//12),'exhaustive_mfactorial_divisibility_cases':checks,'exact_small_word_tests':brute,'status':'AUTHOR_EXECUTED_EXACT_FINITE_UNREVIEWED_NOT_ADMITTED'}
print('PASS_X6_LP011_SIGNED_TIE_ORDER_INTEGRAL_BRC')
print(json.dumps(result,ensure_ascii=False,indent=2))
if len(sys.argv)>1:
    with open(sys.argv[1], 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
