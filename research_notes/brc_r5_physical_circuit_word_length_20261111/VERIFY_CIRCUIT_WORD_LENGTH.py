#!/usr/bin/env python3
"""Exact rational certificates for frozen R5 P/Q-BRC Blackwell transport.
Scientific pins: GK a01383f825ef9d43b4b754254303298c64041568;
EM 86149263e38c22292c9def1e0f69092efa1be77e.
Pinned PR #2017 fixture: WITNESS.txt, Git blob f9e3671e12604bc29ee2cc07ffc59724bafacc90.
Integer-minor polynomial lemma is proved in the companion RESEARCH.md.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial

R = (2, 10, 15, 20, 25, 30, 38)
r = tuple(F(v, 20) for v in R)
J = (1, 2, 3, 5)
D = tuple((i, j) for j in (0, 1, 2, 3, 5, 6)
          for i in range(7) if j not in (0, 6) or i == j)
assert len(D) == 30
WITNESS_PHYS = '1,1016902/1213423,1,2304159/67951688,0,2273985/9707384,0,1,5573459/8493961,6949106/8493961,0,8483579/33975844,1701717/8493961,5573459/84939610'
WITNESS_ARCS = '219346331/10192753200,7664319/135903376,2813871/16987922,196521/33975844,196521/33975844,196521/33975844,196521/33975844,196521/33975844,196521/33975844,393042/8493961,196521/33975844,196521/33975844,196521/33975844,196521/33975844,196521/33975844,196521/33975844,196521/33975844,5251441/33975844,166713611/1274094150,2500147/33975844,393042/8493961,196521/33975844,196521/33975844,196521/33975844,196521/33975844,196521/33975844,196521/33975844,196521/33975844,7664319/135903376,451274777/3397584400'
p = tuple(map(F, WITNESS_PHYS.split(',')))
E0 = dict(zip(D, map(F, WITNESS_ARCS.split(','))))
m = F(196521, 33975844)
assert len(p) == 14 and len(E0) == 30 and min(E0.values()) == m > 0

def mass(x):
    g, a, b, u, v, w, z = x
    return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
      F(13,40)*a+b/80-u, (g-a)/2,
      1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
      (g-b)/2, F(3,40)*a+F(21,80)*b-w,
      u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)

def times(x):
    g,a,b,u,v,w,z=x
    return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
            1+g+(a+b)/2+u+v+w)

def slacks(x):
    g,a,b,u,v,w,z=x
    return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,w,
            F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)

def q21(x,y):
    mu,nu=mass(y),mass(x)
    return mu+nu+tuple(r[j]*nu[j] for j in range(7))

def coupling21(e):
    q=[F(0)]*21
    for (i,j),v in e.items():
        q[i]+=v; q[7+j]+=v; q[14+j]+=r[i]*v
    return tuple(q)

def H(ja,jb,a,b,c):
    assert ja<jb and ja in J and jb in J and a<b<c
    h={e:F(0) for e in D}
    z=(R[b]-R[c],R[c]-R[a],R[a]-R[b])
    for i,v in zip((a,b,c),z):
        h[(i,ja)]=F(v)
        h[(i,jb)]=F(-v)
    return h

def add(*terms):
    return {e:sum((coeff*h[e] for coeff,h in terms),F(0)) for e in D}

def support(h):
    return {e for e,v in h.items() if v}

def check_pair(h,eps):
    assert coupling21(h)==(F(0),)*21
    plus={e:E0[e]+eps*h[e] for e in D}
    minus={e:E0[e]-eps*h[e] for e in D}
    assert all(x>0 for x in plus.values()) and all(x>0 for x in minus.values())
    assert coupling21(plus)==coupling21(minus)==coupling21(E0)==q21(p[:7],p[7:])

assert p[0]==p[2] and p[7]==1 and p[13]==p[8]/10
assert times(p[:7])==times(p[7:])
assert len(slacks(p[:7])+slacks(p[7:]))==26
assert all(x>=0 for x in slacks(p[:7])+slacks(p[7:]))
assert all(x>=0 for x in mass(p[:7])+mass(p[7:]))
assert sum(mass(p[:7]))==sum(mass(p[7:]))==1
assert sum(E0.values())==1 and coupling21(E0)==q21(p[:7],p[7:])
circuits=[]
for j,k in combinations(J,2):
    for a,b,c in combinations(range(7),3):
        h=H(j,k,a,b,c)
        assert len(support(h))==6 and coupling21(h)==(F(0),)*21
        circuits.append(h)
assert len(circuits)==210

h5=add((1,H(1,2,0,1,2)),(1,H(1,2,3,4,5)),
       (1,H(3,5,0,1,2)),(1,H(3,5,3,4,5)),
       (F(1,100),H(1,3,4,5,6)))
assert len(support(h5))==26 and max(abs(x) for x in h5.values())<37
check_pair(h5,m/100)

basis=[]
for j in (2,3,5):
    for k in (1,2,3,4,5):
        b=H(1,j,0,k,6)
        for j2 in (2,3,5):
            for k2 in (1,2,3,4,5):
                assert b[(k2,j2)]==(-36 if (j2,k2)==(j,k) else 0)
        basis.append(b)
assert len(basis)==15
for h in circuits:
    coords=[-h[(k,j)] for j in (2,3,5) for k in (1,2,3,4,5)]
    assert all(v.denominator==1 and abs(v)<=36 for v in coords)
    assert add(*((F(v,36),b) for v,b in zip(coords,basis)))==h

K=factorial(14)*36**14
T=K+2
h15=add(*((T**i,b) for i,b in enumerate(basis)))
assert len(support(h15))==28
assert max(abs(v) for v in h15.values())<=540*T**14
check_pair(h15,m/(1080*T**14))
print('FROZEN_PHYSICAL_5_EQ_26_SLACK_21_OBS PASS')
print('210_SIX_ARC_CIRCUITS_ALL_NULL PASS')
print('15_REPAIR_BASIS_ALL_210_EXACT_RECONSTRUCTIONS PASS')
print('EXPLICIT_FIVE_WORD_LENGTH 5 SUPPORT 26 POSITIVE_COUPLING_PAIR PASS')
print('INTEGER_MINOR_BOUND_K',K)
print('ROOT_AVOIDANCE_PARAMETER_T',T)
print('EXPLICIT_MAX_WORD_LENGTH 15 SUPPORT 28 POSITIVE_COUPLING_PAIR PASS')
print('PASS_EXACT_R5_PHYSICAL_CIRCUIT_WORD_LENGTH_5_AND_15')
