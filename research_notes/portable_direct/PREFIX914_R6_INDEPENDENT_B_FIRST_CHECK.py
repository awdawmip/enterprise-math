#!/usr/bin/env python3
"""PREFIX914 independent b-first reconstruction, Python 3 standard library."""
import math
LOW,HIGH,N=262145,524287,1<<32
T=33*N
Q=range(LOW,HIGH+1,2)

def inherited():
    base={1<<h for h in range(1,18)}
    base.update(v for i in range(2,18) for j in range(1,i) for v in ((1<<i)+(1<<j),(1<<i)-(1<<j)))
    mid=set()
    for i in range(2,18):
        for j in range(1,i):
            for v in ((1<<i)+(1<<j),(1<<i)-(1<<j)):
                for m in range(3,8192,2):
                    if v%m==0:
                        d=v//m
                        if 0<d<=HIGH-LOW and d%2==0 and d not in base:mid.add(d)
    hi=set()
    for i in range(18,31):
        for j in range(1,18):
            for v in ((1<<i)+(1<<j),(1<<i)-(1<<j)):
                for m in range(1,8192,2):
                    if v%m==0:
                        d=v//m
                        if 0<d<=HIGH-LOW and d%2==0 and d not in base and d not in mid:hi.add(d)
    special={262147,280001,300001,320003,340007,360007,380003,400009,420001,440003,460001,480007,500383,510007,520001,524285}
    special.update(range(400011,400522,2));special.update(range(480011,480522,2))
    target={v for h in range(1,32) for v in ((1<<h)-1,(1<<h)+1)}
    special.update(q for q in Q if any(v%q==0 for v in target))
    panels={510000+z+194*j for z in (1,3,5) for j in range(64)}
    d907={(1<<i)+s*(1<<j) for i in range(18,23) for j in range(1,18) for s in (-1,1)}
    d908={(1<<i)+s for i in range(1,20) for s in (-1,1)}
    assert [len(x) for x in (base,mid,hi,special,panels,d907,d908)] == [258,276,857,552,192,169,37]
    return base|mid|hi,special,panels,d907,d908

gaps,special,panels,d907,d908=inherited()
bits={(1<<i)+s for i in range(1,23) for s in (-1,1)}
D={eps*(1<<i)-eta*(1<<j) for i in range(2,23) for j in range(1,i) for eps in (-1,1) for eta in (-1,1)}
assert len(D)==884

def covered(a,b):
    g=math.gcd(a,b)
    return (a*b<T or a in special or b in special or (a//g)*b<N or
        33*((N+a-1)//a)>b or 33*((N+b-1)//b)>a or
        a in panels or b in panels or abs(a-b) in gaps or
        3*a-b in d907 or 3*b-a in d907 or 2*a-b in d908 or 2*b-a in d908)

def prior_multipliers(a,b):
    for k in range(1,13):
        for ell in range(1,13):
            if (k-ell)%2 and (k*a-ell*b in bits or k*b-ell*a in bits):return True
    return False

raw=overlap=diag=baseline=multiplier=novel=novel_overlap=novel_diag=0
first=None;per_d={}
for d in sorted(D):
    lo=max(LOW,3*LOW-d);hi=min(HIGH,3*HIGH-d)
    for b in range(lo+(1-lo%2),hi+1,2):
        a=(b+d)//3
        if (b+d)%3 or a<LOW or a>HIGH or a%2==0:continue
        raw+=1;per_d[d]=per_d.get(d,0)+1
        symmetric=(3*b-a in D);overlap+=symmetric;diag+=(a==b)
        if covered(a,b):baseline+=1;continue
        if prior_multipliers(a,b):multiplier+=1;continue
        novel+=1;novel_overlap+=symmetric;novel_diag+=(a==b)
        if first is None:first=(a,b,d)
assert (raw,overlap,diag,baseline,multiplier,novel,novel_overlap,novel_diag)==(3036491,362,2,2963137,95,73259,0,0)
assert len(per_d)==86
print("INDEPENDENT_B_FIRST",raw,overlap,diag,baseline,multiplier,novel,novel_overlap,novel_diag,"D",len(per_d),"example",first)
print("DELTA",2*novel-novel_overlap,"TOTAL",7795529828+2*novel-novel_overlap)
