#!/usr/bin/env python3
"""PREFIX588-R6 exact two-step native BRC observer certificate; stdlib only."""
from collections import Counter
from fractions import Fraction as Q
from PREFIX565_positive_marginal_certificate import edge, ACTIONS, ZERO_ROOT, SCIENCE_PIN
import json
assert SCIENCE_PIN=="f42f2906d77f24085c123f3ccfe9667d41caa96d"
assert len(ACTIONS)==6
def exps(d):
    return [(a,b,k-a-b) for k in range(d+1) for a in range(k+1) for b in range(k-a+1)]
def moment(row,abc):
    a,b,c=abc
    return sum(n*t**a*x**b*y**c for (t,x,y),n in row.items())
def rank(A):
    B=[[Q(x) for x in row] for row in A]; p=0
    for j in range(len(B[0])):
        k=next((k for k in range(p,len(B)) if B[k][j]),None)
        if k is None:continue
        B[p],B[k]=B[k],B[p];v=B[p][j]
        for c in range(j,len(B[0])): B[p][c]/=v
        for k in range(p+1,len(B)):
            if B[k][j]:
                v=B[k][j]
                for c in range(j,len(B[0])):B[k][c]-=v*B[p][c]
        p+=1
        if p==len(B):break
    return p
def det(A):
    B=[[Q(x) for x in row] for row in A];n=len(B);r=Q(1)
    for j in range(n):
        k=next((k for k in range(j,n) if B[k][j]),None)
        if k is None:return Q(0)
        if k!=j:B[j],B[k]=B[k],B[j];r=-r
        v=B[j][j];r*=v
        for k in range(j+1,n):
            if B[k][j]:
                z=B[k][j]/v
                for c in range(j+1,n):B[k][c]-=z*B[j][c]
                B[k][j]=0
    return r
data=[]
for i in range(96):
    row=Counter()
    for a in ACTIONS:
        j,w=edge(i,a,ZERO_ROOT)
        for b in ACTIONS:
            _,v=edge(j,b,ZERO_ROOT)
            r=[w[k]+v[k] for k in range(7)]
            assert sum(r[:6])==2
            p0,p1,p2=r[0]+r[1],r[2]+r[3],r[4]+r[5]
            assert p0+p1+p2==2
            t=192*r[6]-5*r[0]+r[1]-5*r[2]+r[3]+4*r[4]+4*r[5]
            row[(t,p0,p1)]+=1
    assert sum(row.values())==36
    data.append(row)
A=exps(3)
assert len(A)==20
M=[[moment(data[i],m) for m in A] for i in range(96)]
S=sorted({x for row in data for x in row})
assert S==[(-10,1,1),(-4,1,1),(-1,0,1),(-1,1,0),(2,1,1),
          (5,0,1),(5,1,0),(182,1,1),(188,1,1),(191,1,0)]
groups=Counter(tuple(row) for row in M)
assert len(groups)==23
assert Counter(groups.values())=={1:1,2:3,3:1,4:14,6:1,8:3}
assert rank(M)==9
rows=[0,2,7,8,16,18,24,32,34];cols=[0,1,2,3,7,8,9,17,19]
minor=det([[M[i][j] for j in cols] for i in rows])
assert minor==8903588102459890348326912
assert rank([[r[j] for j in cols] for r in M])==9
plus={38:116,24:248,34:60};minus={0:160,2:165,7:11,32:88}
assert sum(plus.values())==sum(minus.values())==424
assert all(sum((plus.get(i,0)-minus.get(i,0))*M[i][j] for i in range(96))==0 for j in range(20))
diff=sum((plus.get(i,0)-minus.get(i,0))*moment(data[i],(4,0,0)) for i in range(96))
assert diff==2545551360
assert Q(diff,424*36)==Q(8838720,53)
assert Q(diff,424*36*192**4)==Q(1705,13893632)
w=[155,-330,0,0,176,0,0,-11,10,0]
assert all(sum(w[i]*S[i][0]**a*S[i][1]**b*S[i][2]**c for i in range(10))==0 for a,b,c in A)
assert sum(w[i]*S[i][0]**4 for i in range(10))==424258560
print("ALL_CHECKS_PASS")
print(json.dumps({"science_pin":SCIENCE_PIN,"paths":3456,"profiles":23,"rank":9,
                  "rank9_minor":str(minor),"positive_laws_equal_20_raw_moments":True,
                  "fourth_Y_cumulant_gap":"1705/13893632"},indent=2))
