#!/usr/bin/env python3
"""Exact two-law terminal event replacement at K3, with fixed frozen R5 flow."""
from fractions import Fraction as F
from itertools import product

ONE, ZERO = F(1), F(0)
ALPHA = (F(1,2),F(2,3),F(1,2),F(3,4))

def source_flows(x,y,i,z,t,u):
    assert ZERO <= x <= ONE and ZERO <= y <= ONE and ZERO <= i <= ONE-x
    w=(F(1,4),(ONE-x)/4,y/8,i/8)
    c=tuple(w[j]*ALPHA[j] for j in range(4))
    M=tuple(c[j]*z[j] for j in range(4))
    S=tuple(F(2,3)*M[j]*t[j] for j in range(4))
    U=tuple(S[j]*u[j] for j in range(4))
    return M,S,U,y/16+3*i/32

def old_observer(x,y,i,z,t,u):
    M,S,U,d=source_flows(x,y,i,z,t,u)
    return (F(107,128)-F(21,128)*x+d/4-sum(S)/2,
            F(13,64)+F(3,64)*x-d/2+sum(S)/8,
            3+sum(M)+F(3,2)*sum(S)+F(3,4)*sum(U),
            3+sum(M)/2+F(3,8)*sum(S)+F(3,16)*sum(U))

def new_observer(x,y,i,z,t,u,p,q):
    o=old_observer(x,y,i,z,t,u)
    U=source_flows(x,y,i,z,t,u)[2]
    return (o[0]+sum(p[j]*U[j] for j in range(4))/8,
            o[1]+sum(q[j]*U[j] for j in range(4))/32,o[2],o[3])

def table(K3_mass, u, p, q, law, modified=True):
    """Joint rows (action, baseline-delay, extra-delay, decision-label, mass, time)."""
    assert law in ('P','Q')
    mass=K3_mass if law=='P' else K3_mass/4
    rows=[]
    for a in (0,1):
        action_prob = (ONE-u) if a==0 else u
        for b in (0,1):
            for d in ((0,) if a==0 else (0,1)):
                clock_prob=(ONE if a==0 else (F(1,4) if d==0 else F(3,4)))
                prob_Q=F(1,2)
                if modified and a==1:
                    prob_Q=F(1,2)+p/8 if law=='P' else F(1,2)-q/8
                for label in ('P','Q'):
                    prob_label=prob_Q if label=='Q' else ONE-prob_Q
                    m=mass*action_prob*F(1,2)*clock_prob*prob_label
                    rows.append((a,b,d,label,m,5+b+d))
    return rows

def increments(S,U,p,q):
    u=U/S if S else ZERO
    P0=table(S,u,p,q,'P',False)
    P1=table(S,u,p,q,'P',True)
    Q0=table(S,u,p,q,'Q',False)
    Q1=table(S,u,p,q,'Q',True)
    assert sum(row[4] for row in P0)==sum(row[4] for row in P1)==S
    assert sum(row[4] for row in Q0)==sum(row[4] for row in Q1)==S/4
    err=lambda rows,law:sum(row[4] for row in rows if row[3]==('Q' if law=='P' else 'P'))
    time=lambda rows:sum(row[4]*row[5] for row in rows)
    assert time(P1)==time(P0) and time(Q1)==time(Q0)
    assert err(P1,'P')-err(P0,'P')==p*U/8
    assert err(Q1,'Q')-err(Q0,'Q')==q*U/32
    assert err(P0,'P')==S/2 and err(Q0,'Q')==S/8
    return 8

checks=0
for p,q in [((F(1,4),F(1,2),F(3,4),F(1,2)),(F(3,4),F(1,2),F(1,4),F(1,2))),
            ((F(1,16),F(15,16),F(7,13),F(1,3)),(F(12,13),F(1,17),F(5,8),F(1,2)))]:
    for seed in range(24):
        x=F((seed*3)%7,9)
        y=F((seed*5)%13,14)
        i=(ONE-x)*F((seed*7)%11,12)
        z=tuple(F((seed+j*3)%7+1,9) for j in range(4))
        t=tuple(F((seed+j*5)%11+1,13) for j in range(4))
        u=tuple(F((seed+j*2)%9+1,11) for j in range(4))
        M,S,U,_=source_flows(x,y,i,z,t,u)
        for j in range(4):
            checks+=increments(S[j],U[j],p[j],q[j])
        old=old_observer(x,y,i,z,t,u)
        new=new_observer(x,y,i,z,t,u,p,q)
        assert new[0]-old[0]==sum(p[j]*U[j] for j in range(4))/8
        assert new[1]-old[1]==sum(q[j]*U[j] for j in range(4))/32
        assert new[2:]==old[2:]
        assert all(ZERO<e<ONE for e in new[:2])
        checks+=4

p=(F(1,4),F(1,2),F(3,4),F(1,2))
q=(F(3,4),F(1,2),F(1,4),F(1,2))
nP=(F(8),F(0),-F(8,9),F(88,9))
nQ=(F(0),-F(32),F(0),F(8))
N=(nP,nQ)
def dot(n,o):return sum(a*b for a,b in zip(n,o))
stages=((0,0,0),(1,0,0),(1,1,0),(1,1,1))
full=[None,None]
lr=[None,None]
for x,y,i in ((F(x),F(y),F(i)) for x in (0,1) for y in (0,1) for i in (0,1-x)):
    for local in product(stages,repeat=4):
        z,t,u=(tuple(F(local[j][k]) for j in range(4)) for k in range(3))
        o=new_observer(x,y,i,z,t,u,p,q)
        for k in range(2):
            v=dot(N[k],o)
            if full[k] is None or v>full[k]:full[k]=v
for x,y in product((F(0),F(1)),repeat=2):
    i=(ONE-x)*y
    for z0,t0,u0 in stages:
        z,t,u=(tuple(F(v) for _ in range(4)) for v in (z0,t0,u0))
        o=new_observer(x,y,i,z,t,u,p,q)
        for k in range(2):
            v=dot(N[k],o)
            if lr[k] is None or v>lr[k]:lr[k]=v
assert full==[F(1135,32),F(2093,96)]
assert lr==[F(851,24),F(523,24)]
assert [full[k]-lr[k] for k in range(2)]==[F(1,96),F(1,96)]
checks+=6
print('EXACT_K3_SEMANTIC_EVENT_BRIDGE')
print('source_kernel_checks',checks)
print('full_supports',*[str(s) for s in full])
print('lr_supports',*[str(s) for s in lr])
print('gaps',*[str(full[k]-lr[k]) for k in range(2)])
print('PASS_EXACT_R5_K3_PHYSICAL_TERMINAL_EVENT_BRIDGE')
