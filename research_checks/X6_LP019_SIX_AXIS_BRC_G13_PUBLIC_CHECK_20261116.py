#!/usr/bin/env python3
"""Signed X6 exact N-BRC sharpness G=13; author-side, not R063 native bench."""
from itertools import product, combinations_with_replacement
from collections import defaultdict, Counter
from math import comb
from hashlib import sha256
import json

def check(ok, why):
    if not ok: raise AssertionError(why)

def brc(z):
    n=sum(map(abs,z)); result=1
    for x in z:
        result*=comb(n,abs(x)); n-=abs(x)
    return result

def obs(z):
    return (tuple(x-min(z) for x in z),sum(x*x for x in z),sum(map(abs,z)))

full=defaultdict(list)
for z in product(range(-3,4),repeat=6):
    if sum(x*x for x in z)<=13:full[obs(z)].append((z,brc(z)))
amb={k:v for k,v in full.items() if len({b for _,b in v})>1}
check(sum(map(len,full.values()))==12277,'complete signed six-axis domain')
check(len(full)==11396,'observer fiber population')
check(sum(len(v)>1 for v in full.values())==881,'two-point fibers')
check(len(amb)==360 and {k[1:] for k in amb}=={(13,7)},'sharp G13 only')
check({tuple(sorted(b for _,b in v)) for v in amb.values()}=={(630,840)},'exact positive BRC')
orbits=Counter(tuple(sorted(k[0])) for k in amb)
check(orbits=={(0,2,2,3,4,4):180,(0,0,1,2,2,4):180},'two signed S6 orbits')
small=defaultdict(set)
for z in combinations_with_replacement(range(-3,4),6):
    if sum(x*x for x in z)<=13:small[obs(z)].add(brc(z))
check({k for k,v in small.items() if len(v)>1}=={((0,2,2,3,4,4),13,7),((0,0,1,2,2,4),13,7)},'independent sorted orbit check')
pairs=[]
for t in (1,2):
    for z in product(range(-3,4),repeat=6):
        if sum(z)!=-3*t or sum(x*x for x in z)>13:continue
        q=tuple(x+t for x in z)
        if max(map(abs,q))>3 or sum(map(abs,z))!=sum(map(abs,q)):continue
        check(obs(z)==obs(q),'independent common depth equation')
        pairs.append((t,obs(z),brc(z),brc(q)))
check(len(pairs)==881,'independent depth-pair count')
check({k for t,k,b,c in pairs if b!=c}==set(amb),'independent depth-pair mismatch identity')
rows=[{'rho':k[0],'G':k[1],'L':k[2],'paths':tuple(b for _,b in v)} for k,v in sorted(amb.items())]
serial=json.dumps(rows,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
print('PASS_X6_LP019_SIGNED_NATIVE_G13',json.dumps({'vectors':12277,'fibers':11396,'two_point_fibers':881,'first_G':13,'ambiguous_fibers':len(amb),'orbits':[(list(k),v) for k,v in sorted(orbits.items())],'B_values':[630,840],'rows_sha256':sha256(serial).hexdigest(),'original_R063_native_benchmark':'NOT_EXECUTED'},sort_keys=True))
