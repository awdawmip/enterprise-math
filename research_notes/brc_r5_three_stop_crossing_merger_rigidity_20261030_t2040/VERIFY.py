#!/usr/bin/env python3
"""Exact rational R5 crossing-merger three-stop certificate; stdlib only."""
from fractions import Fraction as F
from itertools import product
Q_XU = {(0,0):F(3,8),(0,1):F(1,8),(1,0):F(1,8),(1,1):F(3,8)}
W0 = {0:F(3,4),1:F(1,4)}
R = {0:F(1,2),1:F(3,2)}
Q = {(x,u,v): mass*(W0[u] if v==0 else 1-W0[u]) for (x,u),mass in Q_XU.items() for v in (0,1)}
P = {k:Q[k]*R[k[2]] for k in Q}
PATHS = tuple(Q)
assert sum(P.values())==sum(Q.values())==1
assert all(P[k]>0 and Q[k]>0 for k in PATHS)
assert [sum(P[x,u,v] for u in (0,1) for v in (0,1))/sum(Q[x,u,v] for u in (0,1) for v in (0,1)) for x in (0,1)]==[F(7,8),F(9,8)]
assert all(sum(P[x,u,v] for v in (0,1))/sum(Q[x,u,v] for v in (0,1))==(F(3,4) if u==0 else F(5,4)) for x in (0,1) for u in (0,1))
assert all(P[k]/Q[k]==R[k[2]] for k in PATHS)
def slope(k,a,b,d):
    if k==(0,0,0): return a
    if k==(1,0,0): return -b
    return d if k[2]==1 else F(0)
def obs(bits,full,a,b,d):
    ep=eq=F(1,2)
    tp=tq=F(0)
    for x,u,v in PATHS:
        s=bits[x]
        h=bits[2+2*x+u] if full else bits[2+u]
        z=bits[6+4*x+2*u+v] if full else bits[4+v]
        tm=2+s*(1+h*(2-z))
        incr=s*h*z*slope((x,u,v),a,b,d)
        ep+=P[x,u,v]*incr
        eq+=Q[x,u,v]*incr
        tp+=P[x,u,v]*tm
        tq+=Q[x,u,v]*tm
    return (ep,eq,tp,tq)
def H(o): return o[0]+4*o[2]-2*o[3]
def det4(rows):
    mat=[list(row) for row in rows]; ans=F(1); sign=1
    for j in range(4):
        k=next((i for i in range(j,4) if mat[i][j]),None)
        if k is None: return F(0)
        if k!=j: mat[k],mat[j]=mat[j],mat[k]; sign=-sign
        piv=mat[j][j]; ans*=piv
        for i in range(j+1,4):
            fac=mat[i][j]/piv
            for k in range(j+1,4): mat[i][k]-=fac*mat[j][k]
    return sign*ans
def check(a,b,d):
    assert 0<a<F(1,2) and 0<b<F(1,2) and -F(1,2)<d<F(1,2) and d!=0
    assert all(0<F(1,2)+slope(k,a,b,d)<1 for k in PATHS)
    LR=[(bs,obs(bs,False,a,b,d)) for bs in product((0,1),repeat=6)]
    FULL=[(bs,obs(bs,True,a,b,d)) for bs in product((0,1),repeat=14)]
    L=max(H(o) for _,o in LR)
    M=max(H(o) for _,o in FULL)
    gap=min(9*a,3*b)/64
    assert L==F(21,2)+max(F(0),(9*a-3*b)/64)
    assert M==F(21,2)+9*a/64 and M-L==gap>0
    five=[LR[i][1] for i in (0,16,20,21,26)]
    mat=[tuple(y-x for x,y in zip(five[0],o)) for o in five[1:]]
    det=det4(mat)
    assert det==F(81,65536)*b*d and det!=0
    bits=(1,1,1,1,1,1,1,0,0,0,0,0,0,0)
    witness=obs(bits,True,a,b,d)
    assert witness==(F(1,2)+9*a/64,F(1,2)+9*a/32,F(5)-F(9,64),F(5)-F(9,32))
    assert H(witness)==M
    return L,M,gap,det,witness
if __name__=="__main__":
    print("P=Q=1, positive eight-path masses; LR ratios: t2=7/8,9/8; t3=3/4,5/4; t4=1/2,3/2")
    for a,b,d in [(F(1,4),F(1,4),F(1,8)),(F(1,8),F(3,8),-F(1,4)),(F(3,8),F(1,8),F(1,4))]:
        L,M,gap,det,witness=check(a,b,d)
        print(f"a={a}, b={b}, d={d}: LR={L}; FULL={M}; gap={gap}; LR-rank4-det={det}; witness={witness}")
    print("Policy enumeration for each tuple: 64 LR + 16384 FULL deterministic policies")
    print("All-real validity: see analytic continuation and terminal-reward proof in RESEARCH.md")
    print("PASS_EXACT_R5_CROSSING_THREE_STOP_FULLRANK_NO_GO")
