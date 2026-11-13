#!/usr/bin/env python3
"""Exact R5 C->B and A->B atom witnesses (standard-library Fraction).
Frozen object: R5 7-ratio P/Q-BRC Blackwell fiber, prior commit
9708a8b5ba1870bb423577c50144c1acfa7606dd.
This is a constructive verification, not a two-atom A->B no-go proof.
"""
from fractions import Fraction as F
R=(2,10,15,20,25,30,38)
S=(1,2,3,5)
ARCS=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7)
           if j not in (0,6) or i==j)
E0=tuple(map(F,(
 '219346331/10192753200,7664319/135903376,2813871/16987922,'
 '196521/33975844,196521/33975844,196521/33975844,196521/33975844,'
 '196521/33975844,196521/33975844,393042/8493961,196521/33975844,'
 '196521/33975844,196521/33975844,196521/33975844,196521/33975844,'
 '196521/33975844,196521/33975844,5251441/33975844,166713611/1274094150,'
 '2500147/33975844,393042/8493961,196521/33975844,196521/33975844,'
 '196521/33975844,196521/33975844,196521/33975844,196521/33975844,'
 '196521/33975844,7664319/135903376,451274777/3397584400').split(',')))
assert len(ARCS)==len(E0)==30 and min(E0)>0
V=tuple((i,j) for j in S for i in range(7))
ix={e:k for k,e in enumerate(V)}
A=[[int(ii==i) for ii,jj in V] for i in range(7)]
A += [[int(jj==j) for ii,jj in V] for j in S]
A += [[R[ii]*int(jj==j) for ii,jj in V] for j in S]
b=[sum((z for (ii,j),z in zip(ARCS,E0) if ii==i and j in S),F(0))
   for i in range(7)]
b += [sum((z for (ii,j),z in zip(ARCS,E0) if j==source),F(0)) for source in S]
b += [sum((R[ii]*z for (ii,j),z in zip(ARCS,E0) if j==source),F(0))
      for source in S]
assert len(A)==len(b)==15
MA,MC,MB={1,3,4,6},{2,3,4,6},{2,3,4,5}
def transfer(string):
    v=tuple(map(F,string.split(',')))
    assert len(v)==28
    return v
def atom(other,row):
    h=[F(0)]*28
    assert len(row)==3 and other in (1,2,5)
    for target,value in row.items():
        h[ix[(target,3)]]=F(value)
        h[ix[(target,other)]]=-F(value)
    assert all(sum(A[r][k]*h[k] for k in range(28))==0 for r in range(15))
    return h
def step(v,h,t):
    assert t>0
    return tuple(x+t*y for x,y in zip(v,h))
def check(v,mask):
    assert min(v)>=0 and len(v)==28
    assert all(sum(A[r][k]*v[k] for k in range(28))==b[r] for r in range(15))
    assert {i for i in range(7) if v[ix[(i,3)]]>0}==mask
    return sum(z>0 for z in v)
XC=transfer('61299435/951323632,1523703/9707384,0,0,256989/16987922,3431559/237830908,0,'
            '0,4519983/67951688,0,0,0,0,982605/67951688,'
            '0,0,1460251/8493961,377644447/2548188300,643933/8493961,0,226755/8493961,'
            '4429281/475661816,0,0,0,0,5850279/118915454,4429281/135903376')
HCB=atom(5,{2:F(-8,15),5:F(23,15),6:-1})
tCB=F('226755/8493961')
YC=step(XC,HCB,tCB)
print('C_TO_B_ONE_ATOM',check(XC,MC),check(YC,MB),'t=',tCB)
XA=transfer('10022571/135903376,1383455/16987922,1544855/16987922,0,0,0,5863/1213423,'
            '0,0,196521/2426846,0,0,0,0,'
            '0,33585773/237830908,0,377644447/2548188300,643933/8493961,0,13650395/237830908,'
            '0,196521/237830908,0,0,256989/16987922,2161731/33975844,10959825/951323632')
H1=atom(1,{1:-23,2:28,6:-5})
H2=atom(2,{1:-23,2:28,6:-5})
t1,t2,t3=F('1544855/475661816'),F('196521/67951688'),tCB
W1=step(XA,H1,t1)
W2=step(W1,H2,t2)
YA=step(W2,HCB,t3)
checks=[check(z,mask) for z,mask in zip((XA,W1,W2,YA),(MA,MA|MC,MC,MB))]
print('A_TO_B_THREE_ATOMS',checks,'steps=',(t1,t2,t3))
print('SOURCE3_SUPPORT_SEQUENCE',[(1,3,4,6),(1,2,3,4,6),(2,3,4,6),(2,3,4,5)])
print('SOURCE3_INTERIOR_PEAK',5)
print('A_TO_B_ONE_ATOM_EXCLUDED_BY_FOUR_CHANGED_TARGETS',sorted(MA^MB))
print('A_TO_B_TWO_ATOM_MINIMALITY','UNRESOLVED')
print('PASS_EXACT_R5_C_B_ONE_ATOM_AND_A_B_THREE_ATOM_WITNESSES')
