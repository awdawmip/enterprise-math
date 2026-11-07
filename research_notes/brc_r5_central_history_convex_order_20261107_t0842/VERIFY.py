#!/usr/bin/env python3
"""Exact rational certificate for R5 central-history split monotonicity.

This checks formal mass identities (at affine basis), exact published toy
strategies, and a nontrivial full-history / pooled-LR two-flow realization.
The general inclusion proof is algebraic (RESEARCH.md), not inferred from a grid.
"""
from fractions import Fraction as Q

R=(Q(1,10), Q(1,2), Q(3,4), Q(1), Q(5,4), Q(3,2), Q(19,10))
K=Q(247,1620)


def model(g,a,b,xa,xb, E=None):
    A=(Q(13,40)*a, a/10, Q(3,40)*a)
    B=(b/80, Q(9,40)*b, Q(21,80)*b)
    x=tuple(xa[i]+xb[i] for i in range(3))
    M=(Q(509,900)*x[0]+Q(47,180)*xa[1]+Q(67,162)*xb[1]+x[2]/100,
       A[0]+B[0]-x[0], (g-a)/2,
       1-g+A[1]+B[1]-x[1]+Q(191,450)*(x[0]+x[2])+
           Q(43,90)*xa[1]+Q(14,81)*xb[1],
       (g-b)/2, A[2]+B[2]-x[2],
       x[0]/100+Q(47,180)*xa[1]+Q(67,162)*xb[1]+Q(509,900)*x[2])
    TQ=1+g+(a+b)/2+sum(x)
    TP=1+g+(3*a+5*b)/8+x[0]/2+x[1]+Q(3,2)*x[2]
    if E is None: return M,(TP,TQ)
    eQ=sum(E)
    eP=1-sum((R[i]*E[i] for i in range(7)),Q(0))
    W=(eP,eQ,TP,TQ)
    L=21126*(TQ-1)-13604*(TP-1)-83401*eQ+114010*(1-eP)
    return M,W,L


def legal(g,a,b,xa,xb,E):
    assert Q(0)<=a<=g<=1 and Q(0)<=b<=g
    ca=(Q(13,40)*a,a/10,Q(3,40)*a)
    cb=(b/80,Q(9,40)*b,Q(21,80)*b)
    assert all(0<=xa[i]<=ca[i] and 0<=xb[i]<=cb[i] for i in range(3))
    M,W,L=model(g,a,b,xa,xb,E)
    assert all(0<=E[i]<=M[i] for i in range(7))
    assert sum(M)==1 and sum((R[i]*M[i] for i in range(7)),Q(0))==1
    assert L>=0
    return M,W,L


def central_split(g,a,b,x0,x1,x2,z):
    A=a/10; B=Q(9,40)*b
    assert max(Q(0),x1-B)<=z<=min(A,x1)
    # Side flows may be split proportional to their Q capacities (valid pooling).
    C0=Q(13,40)*a+b/80
    C2=Q(3,40)*a+Q(21,80)*b
    assert C0>=x0>=0 and C2>=x2>=0
    xa0=Q(13,40)*a*x0/C0 if C0 else Q(0)
    xb0=x0-xa0
    xa2=Q(3,40)*a*x2/C2 if C2 else Q(0)
    xb2=x2-xa2
    return (xa0,z,xa2),(xb0,x1-z,xb2)

# Formal coefficient check of central row difference; no sampled inference.
assert Q(47,180)-Q(67,162)==-K
assert Q(43,90)-Q(14,81)==2*K
assert R[0]+R[6]==2*R[3]
print('PASS_EXACT_CENTRAL_ROW_DIFFERENCE_247_OVER_1620')

# Nontrivial rational example with nonuniform declaration: same early flows,
# full vs pooled mass differs, but a convex-order transfer preserves W.
g=a=b=Q(1)
x0=x2=Q(0); x1=Q(1,10)
zlo=Q(0); zpool=(a/10)*x1/(a/10+Q(9,40)*b)
xa_lo,xb_lo=central_split(g,a,b,x0,x1,x2,zlo)
xa_pool,xb_pool=central_split(g,a,b,x0,x1,x2,zpool)
Mlo,_=model(g,a,b,xa_lo,xb_lo)
Mpool,_=model(g,a,b,xa_pool,xb_pool)
eta=K*(zpool-zlo)
assert eta>0
assert tuple(Mlo[i]-Mpool[i] for i in range(7))==(eta,Q(0),Q(0),-2*eta,Q(0),Q(0),eta)
Elo=tuple(Mlo[i]*Q((i%3)+1,5) for i in range(7))
p3=Elo[3]/Mlo[3]
Epool=list(Elo)
Epool[0]+=eta*p3;Epool[3]-=2*eta*p3;Epool[6]+=eta*p3
Mcheck_lo,Wlo,Llo=legal(g,a,b,xa_lo,xb_lo,Elo)
Mcheck_pool,Wpool,Lpool=legal(g,a,b,xa_pool,xb_pool,tuple(Epool))
assert Wlo==Wpool and Llo==Lpool>0
print('PASS_EXACT_STRICT_INCLUSION_TRANSFER_2D_EXAMPLE')
print('z_min =',zlo,'z_pool =',zpool,'eta =',eta)
print('W_transfer =',Wlo,'support_L =',Llo)

# Fixed-flow separation using LR=19/10 as the unique maximal key.
E6only=(Q(0),)*6+(Mlo[6],)
_,Wsep,Lsep=legal(g,a,b,xa_lo,xb_lo,E6only)
assert Mpool[6]<Mlo[6]
assert Wsep[:2]==(1-R[6]*Mlo[6], Mlo[6])
# For any feasible pooled declaration achieving (1-eP)=rmax*eQ,
# every E_j with r_j<rmax must vanish, requiring E6=eQ>Mpool[6].
print('PASS_FIXED_FLOW_STRICTNESS_BY_MAX_LR_KEY')
print('W_fixed_flow_witness =',Wsep,'support_L =',Lsep)
print('M6_full =',Mlo[6],'M6_same_flow_LR =',Mpool[6])

# But the exact same W is globally seedless-LR accessible after reallocating
# early flows: g=1,a=1,b=1/2, x0=1/20,x1=1/8,x2=7/40.
g2=Q(1); a2=Q(1); b2=Q(1,2)
y0=Q(1,20);y1=Q(1,8);y2=Q(7,40)
yA,yB=central_split(g2,a2,b2,y0,y1,y2,(a2/10)*y1/(a2/10+Q(9,40)*b2))
Mlr,_=model(g2,a2,b2,yA,yB)
assert Mlr[6]>=Mlo[6]
Elr=(Q(0),)*6+(Mlo[6],)
_,Wlr,Llr=legal(g2,a2,b2,yA,yB,Elr)
assert Wlr==Wsep and Llr==Lsep
print('PASS_GLOBAL_LR_RESCUE_OF_FIXED_FLOW_WITNESS')
print('W_rescued =',Wlr,'M6_new_LR =',Mlr[6])
print('new_LR_flow =',{'g':g2,'a':a2,'b':b2,'x0':y0,'x1':y1,'x2':y2,
                       'xA':yA,'xB':yB,'E6':Mlo[6]})
print('NEXT: Search for a truly global separation certificate at positive support L, using fiber extremal reduction and K(W).')
