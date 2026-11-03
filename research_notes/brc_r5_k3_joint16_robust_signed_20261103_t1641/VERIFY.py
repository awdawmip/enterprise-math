#!/usr/bin/env python3
"""Exact joint p/q/r/v K3 supports and rigorous uniform perturbation bound."""
from fractions import Fraction as F
from itertools import product

Z, O = F(0), F(1)
alpha = (F(1,2), F(2,3), F(1,2), F(3,4))
base_p = (F(1,4),F(1,2),F(3,4),F(1,2))
base_q = (F(3,4),F(1,2),F(1,4),F(1,2))
base_r = (F(3,4),)*4
base_v = base_r
eta = F(1,1000)
sgn = (1,-1,1,-1)
p = tuple(base_p[j]+sgn[j]*eta for j in range(4))
q = tuple(base_q[j]-sgn[j]*eta for j in range(4))
r = tuple(base_r[j]+sgn[j]*eta for j in range(4))
v = tuple(base_v[j]-sgn[j]*eta for j in range(4))
nP=(F(8),Z,-F(8,9),F(88,9))
nQ=(Z,-F(32),Z,F(8))
stages=((0,0,0),(1,0,0),(1,1,0),(1,1,1))
full_up=((0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,1,0))
lr_up=((0,0,0),(0,1,1),(1,0,0),(1,1,0))

def masses(x,y,i,z,t,u):
    w=(F(1,4),(O-x)/4,y/8,i/8)
    c=tuple(w[j]*alpha[j] for j in range(4))
    M=tuple(c[j]*z[j] for j in range(4))
    S=tuple(F(2,3)*M[j]*t[j] for j in range(4))
    U=tuple(S[j]*u[j] for j in range(4))
    d=y/16+3*i/32
    return c,M,S,U,d

def observer(x,y,i,z,t,u,params):
    p,q,r,v=params
    c,M,S,U,d=masses(x,y,i,z,t,u)
    return (F(107,128)-F(21,128)*x+d/4-sum(S)/2+sum(p[j]*U[j] for j in range(4))/8,
            F(13,64)+3*x/64-d/2+sum(S)/8+sum(q[j]*U[j] for j in range(4))/32,
            3+sum(M)+F(3,2)*sum(S)+sum(r[j]*U[j] for j in range(4)),
            3+sum(M)/2+F(3,8)*sum(S)+sum(v[j]*U[j] for j in range(4))/4)

def dot(a,b):return sum(v*w for v,w in zip(a,b))

def enumerated(n,params,kind):
    best=None; witness=None
    if kind=='FULL':
        for x,y,i in full_up:
            for local in product(stages,repeat=4):
                z,t,u=(tuple(F(local[j][k]) for j in range(4)) for k in range(3))
                obs=observer(F(x),F(y),F(i),z,t,u,params)
                value=dot(n,obs)
                if best is None or value>best:best,witness=value,(x,y,i,local,obs)
    else:
        for x,y,i in lr_up:
            for triple in stages:
                z,t,u=(tuple(F(triple[k]) for j in range(4)) for k in range(3))
                obs=observer(F(x),F(y),F(i),z,t,u,params)
                value=dot(n,obs)
                if best is None or value>best:best,witness=value,(x,y,i,triple,obs)
    return best,witness

def envelope(n,params,kind):
    A,B,C,D=n; p,q,r,v=params
    K=C+D/2
    L=-A/2+B/8+3*C/2+3*D/8
    J=tuple(A*p[j]/8+B*q[j]/32+C*r[j]+D*v[j]/4 for j in range(4))
    candidates=[]
    for x,y,i in full_up if kind=='FULL' else lr_up:
        x,y,i=F(x),F(y),F(i)
        c,_,_,_,d=masses(x,y,i,(Z,)*4,(Z,)*4,(Z,)*4)
        b=A*(F(107,128)-21*x/128+d/4)+B*(F(13,64)+3*x/64-d/2)+3*(C+D)
        if kind=='FULL':
            val=b+sum(c[j]*max(Z,K,K+2*L/3,K+2*(L+J[j])/3) for j in range(4))
        else:
            s=sum(c); u=sum(c[j]*J[j] for j in range(4))
            val=b+max(Z,K*s,(K+2*L/3)*s,(K+2*L/3)*s+2*u/3)
        candidates.append(val)
    return max(candidates)

params0=(base_p,base_q,base_r,base_v)
params1=(p,q,r,v)
assert all(Z<value<O for block in params1 for value in block)
assert sum(alpha[j]*w for j,w in enumerate((F(1,4),F(1,4),F(1,8),F(1,8)))) < O
assert F(43,144)==F(2,3)*sum((F(1,8),F(1,6),F(1,16),F(3,32)))
checks=0
for idx,params in enumerate((params0,params1)):
    for label,n in (('nP',nP),('nQ',nQ),("mixed",(F(7),F(-3),F(2),F(-5)))):
        f,wf=enumerated(n,params,'FULL')
        l,wl=enumerated(n,params,'LR')
        assert f==envelope(n,params,'FULL')
        assert l==envelope(n,params,'LR')
        checks+=2
        print('kernel',idx,'direction',label,'FULL',f,'LR',l,'gap',f-l)
        if idx==1 and label in ('nP','nQ'):
            bound=(f-l)/sum(abs(i) for i in n)
            print('witness',label,'observer',','.join(map(str,wf[4])),'distance_inf_lower',bound)
            assert f>l and bound>0
            checks+=2
        if idx==0 and label in ('nP','nQ'):
            assert f-l==F(1,96)
            checks+=1

L_P=F(43,144)*F(13,3)
L_Q=F(43,144)*F(3)
assert L_P==F(559,432) and L_Q==F(43,48)
boundP=F(1,96)-2*eta*L_P
boundQ=F(1,96)-2*eta*L_Q
assert boundP>0 and boundQ>0 and eta<F(9,2236)
assert (enumerated(nP,params1,'FULL')[0]-enumerated(nP,params1,'LR')[0])>=boundP
assert (enumerated(nQ,params1,'FULL')[0]-enumerated(nQ,params1,'LR')[0])>=boundQ
checks+=7
for j in range(4):
    for law in ('P','Q'):
        for gate in (0,1):
            delay = r[j] if law=='P' else v[j]
            labelQ = F(1,2) if not gate else (F(1,2)+p[j]/8 if law=='P' else F(1,2)-q[j]/8)
            rows=[]
            for b, lab in product((0,1),repeat=2):
                for d in ((0,1) if gate else (0,)):
                    db=(delay if d else O-delay) if gate else O
                    weight=F(1,2)*db*(labelQ if lab else O-labelQ)
                    assert weight>0
                    rows.append((weight,5+b+d,lab))
            assert sum(t[0] for t in rows)==O
            assert sum(t[0]*t[1] for t in rows)==F(11,2)+(delay if gate else Z)
            err=sum(t[0] for t in rows if t[2]==(1 if law=='P' else 0))
            assert err== (F(1,2)+(p[j]/8 if gate else Z) if law=='P' else F(1,2)+(q[j]/8 if gate else Z))
            checks+=4
print('exact_checks',checks)
print('uniform_flow_bound',F(43,144))
print('uniform_direction_lipschitz',L_P,L_Q)
print('uniform_gap_lower',boundP,boundQ)
print('strict_uniform_radius',F(9,2236))
print('PASS_EXACT_R5_K3_JOINT16_SIGNED_ENVELOPE_ROBUSTNESS')
