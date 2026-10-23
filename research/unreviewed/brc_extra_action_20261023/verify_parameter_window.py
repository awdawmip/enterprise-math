#!/usr/bin/env python3
"""Exact coefficient and rational-root-bracket checks, no floating point or sympy."""
from fractions import Fraction as F
from collections import defaultdict
import json

def normal(p):
    p=tuple(F(x) for x in p)
    while len(p)>1 and p[-1]==0:p=p[:-1]
    return p
def add(a,b):
    return normal([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                   for i in range(max(len(a),len(b)))])
def sub(a,b):return add(a,[-v for v in b])
def mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return normal(out)
def prod(xs):
    p=(F(1),)
    for q in xs:p=mul(p,q)
    return p
def value(p,z):
    r=F(0)
    for a in reversed(p):r=r*z+a
    return r

Q={'0':((F(0),),(F(1,3),F(1,3)),(F(1,3),-F(1,3)),(F(1,3),)),
   '2':((F(1,3),),(F(1,3),),(F(0),),(F(1,3),)),
   'X':((F(0),),(F(1),),(F(0),),(F(0),))}
pairs=((0,1),(1,2),(1,3),(2,3))
def occupancy_polynomial(word):
    total=(F(0),)
    for i,j in pairs:
        b=prod([add(Q[a][i],Q[a][j]) for a in word])
        si=prod([Q[a][i] for a in word])
        sj=prod([Q[a][j] for a in word])
        total=add(total,sub(sub(b,si),sj))
    return total

w='000200X'
d=[(F(0),)]+[occupancy_polynomial(w[:n]) for n in range(1,8)]
assert d[2]==normal((F(6,9),F(0),F(-2,9)))
assert d[3]==(F(2,3),)
assert d[4]==normal([F(a,81) for a in (29,9,15)])
assert d[5]==normal([F(a,243) for a in (61,28,66,4,2)])
assert d[6]==normal([F(a,729) for a in (125,75,230,30,25)])
assert d[7]==normal([F(a,729) for a in (95,155,150,70,15,1)])
a5=tuple(F(i) for i in (-26,1,21,4,2))
a6=tuple(F(i) for i in (-58,-9,32,18,19))
assert sub(d[5],d[4])==tuple(i/243 for i in a5)
assert sub(d[6],d[5])==tuple(i/729 for i in a6)
assert sub(d[7],d[6])==tuple(F(i,729) for i in (-30,80,-80,40,-10,1))
assert value(a5,F(9,10))==F(-19309,5000)
assert value(a5,F(31,32))==F(39233,524288)
assert value(a6,F(31,32))==F(-3763117,1048576)
assert value(a6,F(1))==2
assert all(all(c>=0 for c in d[i]) for i in range(4,8))
assert all(value(d[i],F(1))<F(2,3) for i in range(4,7))
assert value(d[7],F(1))==F(2,3)
def isolate(poly):
    a,b=F(0),F(1)
    assert value(poly,a)<0<value(poly,b)
    for _ in range(110):
        m=(a+b)/2
        if value(poly,m)<0:a=m
        elif value(poly,m)>0:b=m
        else:return (m,m)
    return a,b
r5=isolate(a5);r6=isolate(a6)
assert F(9,10)<r5[0]<r5[1]<F(31,32)<r6[0]<r6[1]<F(1)
print(json.dumps({'PASS':True,
                  'A5_high_to_low':[2,4,21,1,-26],
                  'A6_high_to_low':[19,18,32,-9,-58],
                  'theta5_bracket':[str(v) for v in r5],
                  'theta6_bracket':[str(v) for v in r6],
                  'split_region':'theta5<z<=theta6',
                  'admission':'UNREVIEWED_AUTHOR_SIDE'}))
