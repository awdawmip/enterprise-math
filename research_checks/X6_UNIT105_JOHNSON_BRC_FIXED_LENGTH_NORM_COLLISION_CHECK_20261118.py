#!/usr/bin/env python3
"""Unit105: exact finite audit of Johnson-residue/metric N-BRC sufficiency.
Frozen sources: P000 V5 59538f585d037d09ef687b28715c4bc1a3f9fe03;
Johnson historical fd2bcff10ca6e147348b6c1236027fc0d2877df3.
All checks are explicit so Python -O / -OO run the identical certificate.
"""
import json
from collections import Counter
from itertools import product
from math import factorial

PAIRS=((0,5),(1,4),(2,3))
FACT=tuple(factorial(j) for j in range(25))

def check(ok, message):
    if not ok:
        raise AssertionError(message)

def packet(x):
    t=tuple(x[i]*x[j] for i,j in PAIRS)
    s=sum(t)
    rho=tuple((x[i]-x[j])%2 for i,j in PAIRS)+(sum(x)%3,)
    q=tuple(sorted(s-2*tj for tj in t))
    l1=sum(abs(z) for z in x)
    l2=sum(z*z for z in x)
    return (rho,q,l1,l2)

def brc_shortest(x):
    n=sum(abs(z) for z in x)
    out=FACT[n]
    for z in x:
        out//=FACT[abs(z)]
    return out

WITNESS_A=(-3,0,3,0,0,0)
WITNESS_B=(-1,-4,-1,0,0,0)
check(packet(WITNESS_A)==packet(WITNESS_B),'witness observation mismatch')
check(brc_shortest(WITNESS_A)==20 and brc_shortest(WITNESS_B)==30,'witness BRC mismatch')
check(packet(WITNESS_A)==((1,0,1,0),(0,0,0),6,18),'witness packet mismatch')

census=[]
for bound in range(1,5):
    first={}
    conflict_entries=0
    conflict_keys=set()
    first_counterexample=None
    min_conflict_l1=None
    for x in product(range(-bound,bound+1),repeat=6):
        k=packet(x)
        n=brc_shortest(x)
        prev=first.get(k)
        if prev is None:
            first[k]=(x,n)
        elif prev[1]!=n:
            conflict_entries+=1
            conflict_keys.add(k)
            if first_counterexample is None:
                first_counterexample={'a':list(prev[0]),'a_count':prev[1],'b':list(x),'b_count':n}
            l1=k[2]
            if min_conflict_l1 is None or l1<min_conflict_l1:
                min_conflict_l1=l1
    row={
        'bound':bound,
        'states':(2*bound+1)**6,
        'distinct_observation_packets':len(first),
        'conflict_entries_against_first_representative':conflict_entries,
        'conflicting_packets':len(conflict_keys),
        'minimal_conflict_l1':min_conflict_l1,
    }
    census.append(row)
    check((conflict_entries==0)==(bound<=3),'first failure bound mismatch')
    if bound==4:
        check(min_conflict_l1==6,'minimum L1 mismatch')

print(json.dumps({
    'schema':'X6_UNIT105_JOHNSON_BRC_COLLISION_V1',
    'input_source_pin':'P000-V5@59538f585d037d09ef687b28715c4bc1a3f9fe03',
    'historical_source_pin':'fd2bcff10ca6e147348b6c1236027fc0d2877df3',
    'native_shortest_paths':'(sum(abs(x)))! / prod(abs(x_i)!)',
    'observation':'rho_J, sorted Johnson product q_orbit, L1, L2',
    'witness':{'a':list(WITNESS_A),'b':list(WITNESS_B),
                'same_observation':{'rho_J':[1,0,1,0], 'q_orbit':[0,0,0], 'l1':6, 'l2':18},
                'brc_shortest_a':20,'brc_shortest_b':30},
    'bounded_census':census,
    'strength':'exact finite exhaustive search per listed bounded integer cubes; globally valid explicit counterexample',
    'original_R063_Helly_executed':False,
    'status':'AUTHOR_EXACT_FINITE_EXECUTED_NOT_REVIEWED_NOT_ADMITTED',
},sort_keys=True,separators=(',',':')))
