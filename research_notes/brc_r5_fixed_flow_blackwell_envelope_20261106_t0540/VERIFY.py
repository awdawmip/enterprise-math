#!/usr/bin/env python3
"""Exact R5 fixed-flow Blackwell/zonotope envelope and global repair."""
from fractions import Fraction as F
from random import Random
R=(F(1,10),F(1,2),F(3,4),F(1),F(5,4),F(3,2),F(19,10))
alpha=F(47,180); beta=F(67,162); d=beta-alpha
q3=((F(13,20),F(1,5),F(3,20)),(F(1,40),F(9,20),F(21,40)))
assert d==F(247,1620)

def setting(g,u0,u1,zs):
    u=(u0,u1)
    b=[[F(1,2)*q3[i][j]*u[i] for j in range(3)] for i in range(2)]
    V=[sum((b[i][j] for i in range(2)),F(0)) for j in range(3)]
    return V,[V[j]*zs[j] for j in range(3)]

def bounds(u0,u1,X):
    A=u0/10; B=F(9,40)*u1
    lo=max(alpha*X,beta*X-d*A)
    hi=min(beta*X,alpha*X+d*B)
    lr=X*(alpha*A+beta*B)/(A+B) if A+B else F(0)
    premium=d*min(A*X,B*(A+B-X))/(A+B) if A+B else F(0)
    assert lo<=lr<=hi and hi-lr==premium
    return lo,lr,hi,premium

def masses(g,u0,u1,X,J):
    V,_=setting(g,u0,u1,[F(0)]*3)
    M={r:F(0) for r in R}
    M[F(1)]+=1-g
    M[F(3,4)]+=(g-u0)/2; M[F(5,4)]+=(g-u1)/2
    for j,r in enumerate((F(1,2),F(1),F(3,2))): M[r]+=V[j]-X[j]
    M[F(1,10)]+=F(509,900)*X[0]+F(9,900)*X[2]+J
    M[F(1)]+=F(382,900)*(X[0]+X[2])+X[1]-2*J
    M[F(19,10)]+=F(9,900)*X[0]+F(509,900)*X[2]+J
    return M

def limits(M,rho):
    return (1+sum(((rho-r)*M[r] for r in R if r>rho),F(0)),
            1+sum(((rho-r)*M[r] for r in R if r<rho),F(0)))

def times(g,u0,u1,X):
    return (1+g+(3*u0+5*u1)/8+X[0]/2+X[1]+F(3,2)*X[2],
            1+g+(u0+u1)/2+sum(X))

rng=Random(202611060540)
for k in range(720):
    g=F(rng.randrange(21),20)
    u0=g*F(rng.randrange(21),20)
    u1=g*F(rng.randrange(21),20)
    V,X=setting(g,u0,u1,[F(rng.randrange(21),20) for _ in range(3)])
    jl,jlr,ju,premium=bounds(u0,u1,X[1])
    J=jl+(ju-jl)*F(rng.randrange(21),20)
    M=masses(g,u0,u1,X,J)
    ML=masses(g,u0,u1,X,jl)
    MH=masses(g,u0,u1,X,ju)
    MP=masses(g,u0,u1,X,jlr)
    for m in (M,ML,MH,MP):
        assert all(v>=0 for v in m.values())
        assert sum(m.values(),F(0))==1
        assert sum((r*m[r] for r in R),F(0))==1
    assert all(F(1)<=v<=F(4) for v in times(g,u0,u1,X))
    p=beta*X[1];q=alpha*X[1]+d*F(9,40)*u1
    assert ju==min(p,q)
    Mp=masses(g,u0,u1,X,p); Mq=masses(g,u0,u1,X,q)
    for rho in R:
        c=min(rho-R[0],R[-1]-rho)
        l,h=limits(M,rho);ll,hl=limits(ML,rho)
        lu,hu=limits(MH,rho);lp,hp=limits(Mp,rho)
        lq,hq=limits(Mq,rho);lpool,hpool=limits(MP,rho)
        assert lu<=l<=ll and hl<=h<=hu
        assert lu==max(lp,lq) and hu==min(hp,hq)
        assert lu==lpool-c*premium and hu==hpool+c*premium
        assert l==ll-c*(J-jl) and h==hl+c*(J-jl)

g=u0=u1=F(1); X=(F(0),F(9,40),F(0))
jl,jlr,ju,premium=bounds(u0,u1,X[1])
assert (jlr,ju,premium)==(F(33,400),F(67,720),F(19,1800))
MH=masses(g,u0,u1,X,ju);MP=masses(g,u0,u1,X,jlr)
tp,tq=times(g,u0,u1,X)
assert (tp,tq)==(F(129,40),F(129,40))
eQ=MH[F(1,10)]+MH[F(1,2)]+MH[F(3,4)]
eP=1-(F(1,10)*MH[F(1,10)]+F(1,2)*MH[F(1,2)]+F(3,4)*MH[F(3,4)])
assert (eP,eQ)==(F(2959,3600),F(31,72))
uh=limits(MH,F(1))[1]; up=limits(MP,F(1))[1]
assert eP+eQ==uh==F(501,400)
assert up==F(1243,1000) and uh-up==F(19,2000)
A=F(1,10);B=F(9,40)
assert (beta*X[1]-ju)/d==0 and X[1]==B

t=F(49,50);XP=(F(0),F(53,200),F(0))
AP=t/10;BP=F(9,40)*t
z1=XP[1]/(AP+BP)
assert z1==F(530,637) and 0<=z1<=1
Jp=XP[1]*(alpha*AP+beta*BP)/(AP+BP)
assert Jp==F(583,6000) and bounds(t,t,XP[1])[1]==Jp
MQ=masses(t,t,t,XP,Jp)
ell={r:F(0) for r in R}
ell[F(1,10)]=F(583,6000);ell[F(1,2)]=F(3301,10000)
ell[F(1)]=F(37,11250)
assert all(0<=ell[r]<=MQ[r] for r in R)
assert ell[F(1,10)]/MQ[F(1,10)]==1
assert ell[F(1,2)]/MQ[F(1,2)]==F(6602,6615)
assert ell[F(1)]/MQ[F(1)]==F(296,12975)
assert sum(ell.values(),F(0))==eQ
assert sum((r*ell[r] for r in R),F(0))==1-eP
assert times(t,t,t,XP)==(tp,tq)
assert all(limits(MQ,rho)[0]<=eP+rho*eQ<=limits(MQ,rho)[1] for rho in R)
print("PASS_EXACT_R5_FIXED_FLOW_ZONOTOPE_ENVELOPE")
print("profiles",720,"ratio_checks",5040)
print("premium",premium,"fixed_flow_support_gap",uh-up)
print("W",(eP,eQ,tp,tq))
print("repaired_LR",(t,XP[1],z1,Jp))
print("declaration_P_ratios",((F(1,10),F(1)),(F(1,2),F(6602,6615)),(F(1),F(296,12975))))
