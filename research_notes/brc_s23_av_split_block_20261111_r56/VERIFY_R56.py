#!/usr/bin/env python3
"""R56 exact split-block circular classification and newest-only future-state update.
Pure integer arithmetic; source scientific pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
"""
from bisect import bisect_right
from hashlib import sha256
from random import Random
import json

D=10**24
LO=262204504569236716045286
HI=LO+1
PIN='43ec6098b1330ae86d0a7863be336c5d97f6ef34'

def farey(p,q,K):
    if not K: return 0,1,1,1,0
    assert 0<p<q and 0<K<q
    a,i,c,j=0,1,1,1
    comparisons=0
    def below(n,d):
        nonlocal comparisons
        comparisons+=1
        return n*q<p*d
    while i+j<=K:
        if below(a+c,i+j):
            l,h=1,(K-i)//j
            while l<h:
                v=(l+h+1)//2
                if below(a+v*c,i+v*j):l=v
                else:h=v-1
            a,i=a+l*c,i+l*j
        else:
            l,h=1,(K-j)//i
            while l<h:
                v=(l+h+1)//2
                if not below(c+v*a,j+v*i):l=v
                else:h=v-1
            c,j=c+l*a,j+l*i
    assert i*c-j*a==1 and a*q<p*i and c*q>p*j
    return a,i,c,j,comparisons

def sorted_block(lo,n,p,q):
    """Ascending fractional phase of lo..lo+n-1 with Farey successor; O(n) steps."""
    if n==1:return [((lo*p)%q,lo)],0
    a,i,c,j,cc=farey(p,q,n-1)
    s=j
    upper=[]
    for _ in range(n-1):
        upper.append(s)
        s=s-i if s>i else (s+j if s+j<=n-1 else s+j-i)
    assert s==j and len(set(upper))==n-1
    cyclic=[lo]+[lo+k for k in reversed(upper)]
    values=[((t*p)%q,t) for t in cyclic]
    pivot=min(range(n),key=lambda k:values[k][0])
    values=values[pivot:]+values[:pivot]
    assert all(values[k][0]<values[k+1][0] for k in range(n-1))
    return values,cc

def split_ages(j,p,q,m,h):
    """Only sort/merge m historical + h source nodes, regardless of index gap."""
    assert m>=1 and h>=1 and max(m,h)<=q
    boundaries,bc=sorted_block(0,m,p,q)
    sources,sc=sorted_block(j-h,h,p,q)
    ages=[None]*m
    owner=boundaries[-1][1]
    a=b=0
    while a<m or b<h:
        # Boundary first in case of a source exactly on a boundary.
        if a<m and (b==h or boundaries[a][0]<=sources[b][0]):
            owner=boundaries[a][1]
            a+=1
        else:
            r=j-sources[b][1]
            if ages[owner] is None or r<ages[owner]: ages[owner]=r
            b+=1
    return tuple(ages),dict(farey_compares=bc+sc,nodes=m+h,index_span=max(m-1,j-1)-min(0,j-h))

def direct_ages(j,p,q,m,h):
    bounds=sorted(((z*p)%q,z) for z in range(m))
    phases=[x for x,_ in bounds]
    ages=[None]*m
    for r in range(1,h+1):
        phase=((j-r)*p)%q
        z=bounds[bisect_right(phases,phase)-1][1]
        if ages[z] is None or r<ages[z]:ages[z]=r
    return tuple(ages)

def advance(j,d,ages,p,q,m,h):
    """Newest-only sufficient statistic, batch d>=1. No older-source lists."""
    assert d>=1
    newest=[None if age is None else j-age for age in ages]
    bounds=sorted(((z*p)%q,z) for z in range(m))
    phases=[x for x,_ in bounds]
    if d>=h:
        newest=[None]*m
        first=j+d-h
    else:
        first=j
    for t in range(first,j+d):
        z=bounds[bisect_right(phases,(t*p)%q)-1][1]
        newest[z]=t
    j1=j+d
    return tuple(None if t is None or t<j1-h else j1-t for t in newest)

def tests():
    rng=Random(560011)
    n=0; large=0; movements=0; future_checks=0
    gap_cases=[-10**18,-10**12,-101,-1,0,1,61,225,389,10**12,10**18]
    for m in range(1,12):
        for h in range(1,16):
            for rep in range(4):
                p=rng.randrange(1,1009)
                j=gap_cases[(m+h+rep)%len(gap_cases)]
                x,c=split_ages(j,p,1009,m,h)
                y=direct_ages(j,p,1009,m,h)
                assert x==y,(m,h,j,p,x,y)
                n+=1
                if abs(j)>10**11:
                    large+=1
                    assert c['nodes']==m+h
                    assert c['index_span']>10**11
                for d in (1,2,max(1,h//2),h,h+3):
                    z=advance(j,d,x,p,1009,m,h)
                    assert z==direct_ages(j+d,p,1009,m,h)
                    future_checks+=1
                    movements+=min(d,h)
    frozen={}
    for j in (61,225):
        x,c=split_ages(j,LO,D,128,225)
        assert x==split_ages(j,HI,D,128,225)[0]
        assert x==direct_ages(j,LO,D,128,225)
        frozen[j]={'age_vector_sha256':sha256(json.dumps(x).encode()).hexdigest(), 'max_age':max(x),'farey_compares':c['farey_compares'],'nodes':c['nodes'],'index_span':c['index_span']}
    extreme={}
    for j in (-10**18,10**18):
        for p in (LO,HI):
            x,c=split_ages(j,p,D,128,225)
            assert x==direct_ages(j,p,D,128,225)
            extreme[f'{j}:{p}']={'nodes':c['nodes'],'span':str(c['index_span']),'active_labels':sum(t is not None for t in x)}
    return dict(schema='R56_SPLIT_MERGE_NEWEST_SUFFICIENT_V1',scientific_pin=PIN,rational_small_cases=n,large_gap_cases=large,future_state_checks=future_checks,batch_insertions_checked=movements,frozen_ages=frozen,extreme_gap=extreme)

if __name__=='__main__':
    result=tests()
    from pathlib import Path
    here=Path(__file__).resolve().parent
    (here/'R56_CERTIFICATE.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print('PASS_R56_SPLIT_AND_NEWEST_ONLY',result['rational_small_cases'],result['future_state_checks'],result['batch_insertions_checked'])
    print('PASS_R56_S23_FROZEN',result['frozen_ages'])
    print('PASS_R56_EXTREME_INDEX_GAPS',result['extreme_gap'])
