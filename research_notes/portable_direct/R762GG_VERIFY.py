#!/usr/bin/env python3
"""Exact integer checks for R762GG's *candidate* eight signed STAR events.
Python 3 standard library only. These tests do not grant native-event legality.
"""
from itertools import combinations, product
from collections import defaultdict
from math import factorial
import json

STARS=((0,1,2),(0,3,4),(1,3,5),(2,4,5))
ROWS=tuple(tuple(int(i in s) for s in STARS) for i in range(6))

def image(n):
    return tuple(sum(ROWS[i][j]*n[j] for j in range(4)) for i in range(6))

def member(x):
    return (x[0]+x[5]==x[1]+x[4]==x[2]+x[3]
            and (x[0]+x[1]-x[3])%2==0)

def inverse(x):
    n0=(x[0]+x[1]-x[3])//2
    return (n0,x[0]-n0,x[1]-n0,x[2]-n0)

def det(A):
    if len(A)==1: return A[0][0]
    return sum((-1)**j*A[0][j]*det([row[:j]+row[j+1:] for row in A[1:]])
               for j in range(len(A)))

minors4=[det([[ROWS[i][j] for j in range(4)] for i in inds])
         for inds in combinations(range(6),4)]
minors3=[det([[ROWS[i][j] for j in cols] for i in rows])
         for rows in combinations(range(6),3)
         for cols in combinations(range(4),3)]
assert all(v%2==0 for v in minors4) and any(abs(v)==2 for v in minors4)
assert any(abs(v)==1 for v in minors3)
for n in product(range(-2,3),repeat=4):
    x=image(n)
    assert member(x) and inverse(x)==n
for x in product(range(-1,2),repeat=6):
    if member(x): assert image(inverse(x))==x
assert not member((1,)*6)
assert member((2,)*6) and image((1,)*4)==(2,)*6

def coefficient(m,a):
    if m<4*abs(a) or (m-4*abs(a))%2: return 0
    t=(m-4*abs(a))//2
    pos,neg=max(a,0),max(-a,0)
    value=0
    for u in range(t+1):
      for v in range(t-u+1):
       for w in range(t-u-v+1):
        q=t-u-v-w
        den=1
        for h in (u,v,w,q):
            den*=factorial(h+pos)*factorial(h+neg)
        assert factorial(m)%den==0
        value+=factorial(m)//den
    return value

dist={(0,0,0,0):1}
counts=[]
for m in range(11):
    assert sum(dist.values())==8**m
    hol={}
    for n,value in dist.items():
        x=image(n)
        assert (len(set(x))==1)==(len(set(n))==1)
        if len(set(n))==1:
            a=n[0]
            hol[str(a)]=value
            assert coefficient(m,a)==value and x==(2*a,)*6
    counts.append({"m":m,"states":len(dist),"holonomy_word_counts":hol,
                   "relative_return_words":sum(hol.values()),"all_words":8**m})
    if m==10: break
    next_dist=defaultdict(int)
    for n,value in dist.items():
        for j in range(4):
            for sign in (-1,1):
                new=list(n);new[j]+=sign
                next_dist[tuple(new)]+=value
    dist=dict(next_dist)
assert counts[4]["holonomy_word_counts"]=={"0":168,"-1":24,"1":24}
assert counts[6]["holonomy_word_counts"]=={"0":5120,"-1":1440,"1":1440}
assert counts[8]["holonomy_word_counts"]=={"0":190120,"-1":73920,"1":73920,"-2":2520,"2":2520}
print(json.dumps({
    "schema":"R762GG_EXACT_STAR_SIGNED_CANDIDATE_V1",
    "stars":[list(s) for s in STARS],"B_rows":[list(r) for r in ROWS],
    "smith_diagonal":[1,1,1,2],"checked_n_box":[-2,2],
    "checked_x_box":[-1,1],"masses":counts,
    "claim_type":"AUTHOR_SIDE_EXACT_VERIFICATION_CANDIDATE_EVENT_ONLY",
    "independent_review":"NOT_REVIEWED"
},indent=2))
