#!/usr/bin/env python3
"""Author check of balanced 2+2 observer-fiber counts; prime fields only."""
from itertools import product
from collections import defaultdict, Counter

def rank(M,p):
    a,b,c,d=M
    return 2 if (a*d-b*c)%p else int(any(M))

def product2(A,B,p):
    a,b,c,d=A; e,f,g,h=B
    return ((a*e+b*g)%p,(a*f+b*h)%p,(c*e+d*g)%p,(c*f+d*h)%p)

def labels(X,Y,p):
    C=product2(Y,X,p); rx=rank(X,p); ry=rank(Y,p)
    t=(C[0]+C[3])%p; det=(C[0]*C[3]-C[1]*C[2])%p
    observed=(rx,ry,t,det)
    if rx==0: orbit=('zeroX',ry)
    elif rx==1:
        if t: orbit=('rank1_nonzero_t',t,ry)
        elif ry==0: orbit=('rank1_zeroY',)
        elif ry==2: orbit=('rank1_fullY',)
        else: orbit=('rank1_direction',rank(product2(X,Y,p),p),rank(C,p))
    else:
        repeated=(t*t-4*det)%p==0
        lam=t*pow(2,-1,p)%p
        orbit=('invertibleX',t,det,int(repeated and C!=(lam,0,0,lam)))
    return observed,orbit

for p in (3,5,7,11,13):
    fiber=defaultdict(set)
    for X in ((0,0,0,0),(1,0,0,0),(1,0,0,1)):
        for Y in product(range(p),repeat=4):
            o,c=labels(X,Y,p); fiber[o].add(c)
    histogram=Counter(map(len,fiber.values()))
    assert len(fiber)==p*p+2*p+5
    assert sum(map(len,fiber.values()))==p*p+3*p+6
    assert histogram==Counter({1:p*p+p+5,2:p-1,3:1})
    print('PASS p=',p,'observers=',len(fiber),'orbits=',sum(map(len,fiber.values())))

p=373
X=(1,0,0,0)
three=[labels(X,Y,p) for Y in ((0,0,0,1),(0,1,0,0),(0,0,1,0))]
assert len({o for o,c in three})==1 and len({c for o,c in three})==3
X=(1,0,0,1)
assert labels(X,(1,0,0,1),p)[0]==labels(X,(1,1,0,1),p)[0]
assert labels(X,(1,0,0,1),p)[1]!=labels(X,(1,1,0,1),p)[1]
print('PASS p=373 exact witnesses; O=139880; gauge orbits=140254')
