#!/usr/bin/env python3
"""Exact dual-law two-collision six-facet hull audit. Standard library only."""
from fractions import Fraction as F
from itertools import product

ONE,ZERO=F(1),F(0)
P=(F(1,8),F(1,8),F(1,4),F(1,2))
Q=(F(1,8),F(1,8),F(1,8),F(5,8))
PLOW=(F(1,2),F(3,4))
QLOW=(F(1,4),F(3,8))

def flow(actions):
    p1,p2,q1,q2,qb,r=tuple(F(x) for x in actions)
    events=[]
    def add(tag,t,a,lp,lq,f):
        assert lp>0 and lq>0 and ZERO<=f<=ONE
        events.append((tag,t,a,lp*f,lq*f,lp,lq))
    for j,(pj,qj) in enumerate(((p1,q1),(p2,q2))):
        add('A%d-stopI'%(j+1),1,'Q',P[j],Q[j],pj)
        add('A%d-high'%(j+1),2,'P',P[j]*(1-PLOW[j]),Q[j]*(1-QLOW[j]),1-pj)
        cp,cq=P[j]*PLOW[j],Q[j]*QLOW[j]
        add('A%d-stopJ'%(j+1),2,'Q',cp,cq,(1-pj)*qj)
        if j==0:
            add('A1-X',3,'P',cp*F(3,5),cq*F(1,2),(1-pj)*(1-qj))
            add('A1-Y',3,'Q',cp*F(2,5),cq*F(1,2),(1-pj)*(1-qj))
        else:
            add('A2-continueJ',3,'Q',cp,cq,(1-pj)*(1-qj))
    add('B-stopJ',2,'Q',P[2],Q[2],qb)
    add('B-continueJ',3,'Q',P[2],Q[2],1-qb)
    add('C-stop',1,'P',P[3],Q[3],r)
    add('C-continue',3,'Q',P[3],Q[3],1-r)
    assert len(events)==13
    assert sum(e[3] for e in events)==ONE and sum(e[4] for e in events)==ONE
    key_answers={}
    for tag,t,a,mp,mq,np,nq in events:
        key=(t,np/nq)
        assert key_answers.setdefault(key,a)==a,(tag,key,a)
    return events

def obs(actions):
    e=flow(actions)
    return (sum(z[3] for z in e if z[2]=='Q'),
            sum(z[4] for z in e if z[2]=='P'),
            sum(z[1]*z[3] for z in e),sum(z[1]*z[4] for z in e))

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def det(M):
    T=[list(map(F,row)) for row in M];n=len(T);s=ONE
    for k in range(n):
        j=next((i for i in range(k,n) if T[i][k]),None)
        if j is None:return ZERO
        if j!=k:T[k],T[j]=T[j],T[k];s=-s
        pivot=T[k][k];s*=pivot
        for i in range(k+1,n):
            f=T[i][k]/pivot
            for z in range(k,n):T[i][z]-=f*T[k][z]
    return s
def invert(M):
    n=len(M)
    T=[list(map(F,row))+[F(int(i==j)) for j in range(n)] for i,row in enumerate(M)]
    for k in range(n):
        j=next(i for i in range(k,n) if T[i][k])
        T[k],T[j]=T[j],T[k]
        d=T[k][k];T[k]=[t/d for t in T[k]]
        for i in range(n):
            if i!=k:
                d=T[i][k];T[i]=[a-d*b for a,b in zip(T[i],T[k])]
    I=[row[n:] for row in T]
    assert all(sum(M[i][k]*I[k][j] for k in range(n))==F(int(i==j)) for i in range(n) for j in range(n))
    return I

O0=(F(139,160),F(3,16),F(93,32),F(181,64))
B=(F(21,160),-F(3,16),-F(13,32),-F(21,64))
C=(F(3,80),-F(1,64),-F(13,32),-F(13,64))
D=(-F(3,80),F(1,64),F(5,32),F(5,64))
E=(-F(1,2),F(5,8),-ONE,-F(5,4))
A=[[B[i],C[i],D[i],E[i]] for i in range(4)]
assert det(A)==F(233,163840)
AI=invert(A)
def coordinates(O):
    delta=[O[i]-O0[i] for i in range(4)]
    return tuple(dot(row,delta) for row in AI)
def facets(z):
    p,q,s,r=z
    return (s,ONE-p-q+s,p-s,q-s,r,ONE-r)

for p,q,r in product((ZERO,F(1,3),F(1,2),F(2,3),ONE),repeat=3):
    target=tuple(O0[i]+p*B[i]+q*C[i]+p*q*D[i]+r*E[i] for i in range(4))
    actual=obs((p,p,q,q,q,r))
    assert target==actual and coordinates(actual)==(p,q,p*q,r)
    assert all(f>=0 for f in facets(coordinates(actual)))

NAMES=('s','1-p-q+s','p-s','q-s','r','1-r')
ALPHA=(ZERO,ONE,ZERO,ZERO,ZERO,ONE)
COEFF=((0,0,1,0),(-1,-1,1,0),(1,0,-1,0),(0,1,-1,0),(0,0,0,1),(0,0,0,-1))
full=list(product((ZERO,ONE),repeat=6))
lr=list(product((ZERO,ONE),repeat=3))
assert len(full)==64 and len(lr)==8
FULL=[(v,obs(v),coordinates(obs(v))) for v in full]
LR=[(v,obs((v[0],v[0],v[1],v[1],v[1],v[2]))) for v in lr]
mins=[]
for i in range(6):
    vals=[(facets(z)[i],v,O,z) for v,O,z in FULL]
    row=min(vals,key=lambda x:x[0])
    count=sum(t[0]<0 for t in vals)
    assert row[0]<0
    n=tuple(sum(F(COEFF[i][j])*AI[j][k] for j in range(4)) for k in range(4))
    assert all(ALPHA[i]+dot(n,[x[k]-O0[k] for k in range(4)])==facets(z)[i] for _,x,z in FULL)
    d=-row[0]/sum(abs(a) for a in n)
    mins.append((row[0],count,d))
    print('facet',i,NAMES[i],'min',row[0],'violators',count,
          'witness',tuple(map(int,row[1])),'O',tuple(map(str,row[2])),
          'coordinate',tuple(map(str,row[3])),
          'normal',tuple(map(str,n)),'l_infty_lb',d)
assert mins==[
    (-F(2793,1864),22,F(2793,228752)),
    (-F(90,233),16,F(3,520)),
    (-F(3737,1864),18,F(3737,223376)),
    (-F(205,233),8,F(205,16272)),
    (-F(1,932),8,F(1,2312)),
    (-F(1,932),8,F(1,2312))]
inside=0
for v,O,z in FULL:
    if all(f>=0 for f in facets(z)):
        inside+=1
        p,q,s,r=z
        w=(ONE-p-q+s,q-s,p-s,s)
        assert all(a>=0 for a in w) and sum(w)==ONE
        recon=tuple(sum(w[2*i+j]*(r if k else ONE-r)*LR[4*i+2*j+k][1][l]
            for i in range(2) for j in range(2) for k in range(2)) for l in range(4))
        assert recon==O
assert inside==22
assert all(all(f>=0 for f in facets(coordinates(O))) for _,O in LR)
print('FULL_INSIDE',inside,'FULL_OUTSIDE',64-inside)
print('LR_VERTICES',len(LR),'AFFINE_DETERMINANT',det(A))
print('PASS_EXACT_R5_COMPLETE_SIX_FACET_FULL_LR_HULL_AUDIT')
