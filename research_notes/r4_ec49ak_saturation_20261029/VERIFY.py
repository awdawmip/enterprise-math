#!/usr/bin/env python3
"""EC49AK exact rational author verification; no external packages."""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
import json

K=F(177,172); L=F(27,172); C1=F(43,48)
NAMES=('A0','A1','B0','B1','STOP')
def t(w,u,eta): return F(1,2)+(2*u-1)*(1-w)*eta
def P(w,u,z,eta): return t(w,u,eta)*(F(1,6) if z==w else F(1,12))
def Q(w,u,z,eta): return t(w,u,eta)/9
X=((F(1),F(0),F(0),F(0),F(0)),
   (F(0),F(1),F(0),F(0),F(0)),
   (F(0),F(0),F(11,32),F(0),F(21,32)))
def check_witness(eta,C2):
    assert 0<=eta<F(1,2) and 0<=C2<=F(25,32)
    assert all(sum(row)==1 and all(z>=0 for z in row) for row in X)
    assert all(t(w,u,eta)>0 for w in range(3) for u in range(2))
    assert sum((P(w,u,z,eta) for w in range(3) for u in range(2) for z in range(3)),F(0))==1
    assert sum((Q(w,u,z,eta) for w in range(3) for u in range(2) for z in range(3)),F(0))==1
    assert all(sum(P(w,u,z,eta) for z in range(3))==sum(Q(w,u,z,eta) for z in range(3)) for w in range(3) for u in range(2))
    assert sum(sum(X[w][c]*(2 if c in (2,3) else 1) for c in range(4)) for w in range(3))/3==C1
    r=F(32,25)*C2
    cost2=sum((X[w][c]*r*sum(Q(w,u,z,eta) for z in range(3)) for w in range(3) for c in range(4) for u in range(2)),F(0))
    assert cost2==C2
    label_to_w={0:0,1:1,2:2}
    a=sum((X[w][c]*r*P(w,u,z,eta) for w in range(3) for c in label_to_w for u in range(2) for z in range(3) if z==label_to_w[c]),F(0))
    b=sum((X[w][c]*r*Q(w,u,z,eta) for w in range(3) for c in label_to_w for u in range(2) for z in range(3) if z==label_to_w[c]),F(0))
    assert a==C2/2 and b==C2/3 and a-K*b==L*C2
    assert F(1,2)-K/3==L and F(1,4)-K/3==-F(4,43)
    return dict(eta=str(eta),C2=str(C2),r=str(r),alpha=str(a),beta=str(b),H=str(a-K*b))
# All first-stage support-bases for exact epsilon=1/10, C2=31/40.
A=[[int(j//5==w) for j in range(15)] for w in range(3)]
A.append([1 if j%5==4 else (-1 if j%5 in (2,3) else 0) for j in range(15)])
B=[int(j%5 in (2,3)) for j in range(15)]
BC=F(29,80)
def basis_solve(cols,cap):
    rows=A+([B] if cap else [])
    rhs=[F(1)]*3+[F(5,16)]+([BC] if cap else [])
    M=[[F(row[j]) for j in cols]+[v] for row,v in zip(rows,rhs)]
    n=len(cols)
    for i in range(n):
        j=next((j for j in range(i,n) if M[j][i]!=0),None)
        if j is None:return None
        M[i],M[j]=M[j],M[i]
        v=M[i][i];M[i]=[z/v for z in M[i]]
        for j in range(n):
            if j==i:continue
            v=M[j][i]
            if v:M[j]=[z-v*q for z,q in zip(M[j],M[i])]
    vals=[row[-1] for row in M]
    if any(v<0 for v in vals):return None
    x=[F(0)]*15
    for j,v in zip(cols,vals):x[j]=v
    if sum(x[j] for j in range(15) if j%5 in (2,3))>BC:return None
    assert all(sum(A[i][j]*x[j] for j in range(15))==rhs[i] for i in range(4))
    return tuple(x)
def pure_mass(x):
    return sum((sum(x[5*w+c] for w in range(3)) for c in range(4)
                if sum(x[5*w+c]>0 for w in range(3))<=1),F(0))/3
def run():
    cases=[check_witness(eta,c2) for eta in (F(0),F(1,200),F(3,10),F(49,100)) for c2 in (F(0),F(1,2),F(31,40),F(25,32))]
    vs=set();bases=0
    for cap in (False,True):
        for cols in combinations(range(15),5 if cap else 4):
            bases+=1
            x=basis_solve(cols,cap)
            if x is not None:vs.add(x)
    hist=Counter(str(sum(x[j] for j in range(15) if j%5 in (2,3))) for x in vs)
    assert bases==4368 and len(vs)==288
    assert hist=={'0':24,'11/32':24,'29/80':240},hist
    assert max(pure_mass(x) for x in vs)==F(25,32)
    p=check_witness(F(3,10),F(31,40))
    assert p==dict(eta='3/10',C2='31/40',r='124/125',alpha='31/80',beta='31/120',H='837/6880')
    return dict(schema='EC49AK_EXACT_V1',
      result='PASS_EXACT_FRACTION_AUTHOR_UNREVIEWED',
      universal_claim='analytic proof, not inferred from finite tests',
      eta_sample_values=['0','1/200','3/10','49/100'],
      C2_sample_values=['0','1/2','31/40','25/32'],
      witness_exact_check_count=len(cases),point=p,
      capacity_test=dict(epsilon='1/10',bases_checked=bases,vertices=len(vs),b_histogram=dict(hist),pure_mass_max='25/32'),
      native_BRC='NOT_CLAIMED',independent_review='NOT_PERFORMED')
if __name__=='__main__':
    print(json.dumps(run(),indent=2,ensure_ascii=False))
