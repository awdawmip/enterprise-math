#!/usr/bin/env python3
"""Exact frozen R5 auxiliary Blackwell-fiber A->C->B path.
Arithmetic is Python Fraction throughout. Frozen observer input and two
initial steps are reproduced from R5 Draft PR #2072 (commit 9708a8b5...).
No new scientific pin or native X6 physical dynamics interpretation.
"""
from fractions import Fraction as F
R = (2, 10, 15, 20, 25, 30, 38)
SOURCES = (1, 2, 3, 5)
ARCS30 = tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7)
               if j not in (0,6) or i == j)
E0 = tuple(map(F, (
    '219346331/10192753200,7664319/135903376,2813871/16987922,'
    '196521/33975844,196521/33975844,196521/33975844,196521/33975844,'
    '196521/33975844,196521/33975844,393042/8493961,196521/33975844,'
    '196521/33975844,196521/33975844,196521/33975844,196521/33975844,'
    '196521/33975844,196521/33975844,5251441/33975844,166713611/1274094150,'
    '2500147/33975844,393042/8493961,196521/33975844,196521/33975844,'
    '196521/33975844,196521/33975844,196521/33975844,196521/33975844,'
    '196521/33975844,7664319/135903376,451274777/3397584400').split(',')))
assert len(ARCS30) == len(E0) == 30 and min(E0)>0
V=tuple((i,j) for j in SOURCES for i in range(7))
idx={arc:k for k,arc in enumerate(V)}
OBS=([[(ii==i)*1 for ii,jj in V] for i in range(7)] +
     [[(jj==j)*1 for ii,jj in V] for j in SOURCES] +
     [[R[ii]*(jj==j) for ii,jj in V] for j in SOURCES])
M=[sum((z for (ii,j),z in zip(ARCS30,E0) if ii==i and j in SOURCES),F(0)) for i in range(7)]
Q=[sum((z for (i,jj),z in zip(ARCS30,E0) if jj==j),F(0)) for j in SOURCES]
T=[sum((R[i]*z for (i,jj),z in zip(ARCS30,E0) if jj==j),F(0)) for j in SOURCES]
b=M+Q+T
assert len(OBS)==len(b)==15 and len(V)==28
def atom(other, source3_row):
    assert other in (1,2,5)
    assert sum(source3_row.values(),F(0))==0
    assert sum((R[i]*v for i,v in source3_row.items()),F(0))==0
    h=[F(0)]*28
    for i,v in source3_row.items():
        h[idx[(i,3)]] = v
        h[idx[(i,other)]] = -v
    assert all(sum(a*z for a,z in zip(row,h)) == 0 for row in OBS)
    return tuple(h)
def advance(x,t,h):
    return tuple(v+t*w for v,w in zip(x,h))
def check(x,mask,label):
    assert len(x)==28 and min(x)>=0,(label,min(x))
    assert all(sum(a*z for a,z in zip(row,x))==rhs for row,rhs in zip(OBS,b)),label
    found=tuple(i for i in range(7) if x[idx[(i,3)]]>0)
    assert found==tuple(sorted(mask)),(label,found,mask)
    return sum(z>0 for z in x)
XA=tuple(map(F,(
    '4257955/58244304,42470639/475661816,16095404/195361103,0,0,0,202668635/32820665304,'
    '0,0,196521/2426846,0,0,0,0,0,63830689/475661816,0,377644447/2548188300,'
    '1544855/16987922,0,23445955/475661816,65507/101927532,0,3340857/390722206,'
    '0,0,2161731/33975844,171431819/9377332944').split(',')))
assert len(XA)==28
H1=atom(1,{1:F(-23),2:F(28),6:F(-5)})
H2=atom(2,{1:F(-23),2:F(28),6:F(-5)})
t1=F('4023851/1367527721')
t2=F('196521/67951688')
X1=advance(XA,t1,H1)
XC=advance(X1,t2,H2)
H3=atom(5,{2:F(-8,15),5:F(23,15),6:F(-1)})
t3=XC[idx[(6,3)]]
assert t3==F('3930420/195361103')
XB=advance(XC,t3,H3)
A={1,3,4,6};C={2,3,4,6};B={2,3,4,5}
assert check(XA,A,'A')>=0
assert check(X1,A|C,'A-C intermediate')>=0
assert check(XC,C,'C')>=0
assert check(XB,B,'B')>=0
assert min((t1,t2,t3))>0
assert sum(R[i]*H3[idx[(i,3)]] for i in range(7))==0
assert min(XB[k] for k,(i,j) in enumerate(V) if j==3 and i in B)>0
assert all(XB[idx[(i,3)]]==0 for i in set(range(7))-B)
print('FROZEN_RATIO',R)
print('A,C,B',tuple(sorted(A)),tuple(sorted(C)),tuple(sorted(B)))
print('STEP_SCALES',t1,t2,t3)
print('SOURCE3_SUPPORT_AT_STATES',4,5,4,4)
print('C_TO_B_ATOM', 'source pair {3,5}; targets {2,5,6}; row(-8/15,23/15,-1)')
print('C_TO_B_ATOM_SINGLE_MOVE_MINIMUM',1)
print('A_TO_B_EXPLICIT_THREE_MOVE_UPPER_BOUND',3)
print('A_TO_B_ONE_ATOM_IMPOSSIBLE_4_CHANGED_TARGETS_GT_3',True)
print('A_TO_B_TWO_ATOM_STATUS','CHECK_WITH_VERIFY_NO_TWO_ATOMS')
print('FULL_TRANSPORTS_NONNEGATIVE',True)
print('OBSERVER_EQUATIONS_EXACT',15)
print('END_B_SOURCE3',','.join(f'{i}:{XB[idx[(i,3)]]}' for i in sorted(B)))
print('END_B_SOURCE5_COMPENSATORS',','.join(f'{i}:{XB[idx[(i,5)]]}' for i in (2,5,6)))
print('PASS_R5_EXACT_C_TO_B_ONE_ATOM_AND_A_TO_B_THREE_MOVE_WITNESS')
