#!/usr/bin/env python3
"""Exact replay for R126: independent enumeration of q<=11 modulo sign."""
from fractions import Fraction as Q

def port(a):
    return max(sum(max(x, 0) for x in a), sum(max(-x, 0) for x in a))

def sign_canonical(a):
    return a if next(x for x in a if x) > 0 else tuple(-x for x in a)

def gaps(a):
    x, y, z = a
    h = [0, x + 3*y + 6*z, 3*x + 12*y + 30*z, 7*x + 39*y + 126*z]
    return tuple(abs(h[i] - h[j]) for i in range(4) for j in range(i+1, 4))

def build(p):
    return {sign_canonical((x,y,z)):gaps((x,y,z))
            for x in range(-p,p+1) for y in range(-p,p+1) for z in range(-p,p+1)
            if (x,y,z)!=(0,0,0) and port((x,y,z))<=p}

def score(g,D):
    return max(Q(t,den) for t,den in zip(g,(625,288,48+D,817,577+D,240+D)))

def snapshot(data,D,p):
    ranked={a:score(g,D) for a,g in data.items() if port(a)<=p}
    eta=min(ranked.values())
    return eta,tuple(sorted(a for a,s in ranked.items() if s==eta)),tuple(sorted(a for a,s in ranked.items() if 2*s<3*eta))

S=((1,-3,1),(1,0,0),(4,-1,0),(5,-4,1),(5,-1,0),(6,-4,1),(9,-5,1),(9,-2,0))
S=tuple(sorted(S))
U=(10,-5,1)
rows=build(11)
assert len(rows)==2541 and sum(port(a)<=10 for a in rows)==1935
# The first four gap inequalities at D=1008 suffice to isolate the eight rows.
four=tuple(sorted(a for a,g in rows.items() if port(a)<=10
                  and 64*g[0]<625 and 64*g[1]<288 and 64*g[2]<1056 and 64*g[3]<817))
assert four==S, (four,S)
# Similarly, the only Port<=11 vectors passing the constant-gap prefilter.
five=tuple(sorted(a for a,g in rows.items() if g[0]<=1 and g[1]==0 and g[3]<=1))
assert five==tuple(sorted(((2,-3,1),(4,-1,0),(6,-4,1),(8,-7,2),(10,-5,1))))
for D in [Q(900),Q(912),Q(1825,2),Q(976),Q(1953,2),Q(978),Q(1008),Q(1009),Q(1100),Q(6096,5)-Q(1,100),Q(6096,5),Q(6096,5)+Q(1,100),Q(1300)]:
    e10,o10,n10=snapshot(rows,D,10)
    e11,o11,n11=snapshot(rows,D,11)
    expected_eta= min(Q(1,96),Q(11,D+48))
    assert e10==expected_eta,(D,'eta10',e10,expected_eta)
    assert e11==Q(1,625) and o11==(U,) and n11==(U,), (D,'port11',e11,o11,n11)
    if D<=912: expected_count=6
    elif D<=976:expected_count=7
    elif D<Q(6096,5):expected_count=8
    else:expected_count=7
    assert len(n10)==expected_count,(D,len(n10))
    if D>976 and D<Q(6096,5):assert n10==S
    print('D=',D,'eta10=',e10,'near10=',len(n10),'opt10=',len(o10),'near11=',len(n11))
print('PASS: 2541 unoriented q<=11 directions; 13 exact parameter cases; 26 full q10/q11 snapshots; 8-row and 5-row finite certificates.')
