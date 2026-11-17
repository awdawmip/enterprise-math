#!/usr/bin/env python3
"""Exact rational/int checks of the 2-parameter three-child STOP tree theorem."""
from fractions import Fraction as F
from itertools import product
from math import lcm
Q_XU={(0,0):F(3,8),(0,1):F(1,8),(1,0):F(1,8),(1,1):F(3,8)}
R_U=(F(3,4),F(5,4))
R_V=(F(1,2),F(1),F(3,2))
def kernel(t,u):
    return (F(1,2)+t,F(1,2)-2*t,t) if u==0 else (t,F(1,2)-2*t,F(1,2)+t)
def ell(t):
    return (5-2*t)/(6-4*t)
def analyze(t0,t1):
    assert F(0)<t0<F(1,4) and F(0)<t1<F(1,4)
    ts=(t0,t1)
    c=(ell(t0),ell(t1))
    w0,w1=F(3,8)*(F(3,2)-t0),F(1,8)*(F(3,2)-t1)
    lam=(w0*c[0]+w1*c[1])/(w0+w1)
    gap=3*abs(t1-t0)/(16*(6-3*t0-t1))
    assert F(5,6)<lam<F(9,10)
    assert c[1]-c[0]==2*(t1-t0)/((3-2*t0)*(3-2*t1))
    leaves=[]
    for x,u,v in product((0,1),(0,1),range(3)):
        k=kernel(ts[x],u)
        assert all(kv>0 for kv in k) and sum(k)==1
        assert sum(k[j]*R_V[j] for j in range(3))==R_U[u]
        q=Q_XU[x,u]*k[v]
        p=R_V[v]*q
        assert q>0 and p>0
        leaves.append((x,u,v,p,q))
    assert sum(row[3] for row in leaves)==sum(row[4] for row in leaves)==1
    assert [sum(row[3] for row in leaves if row[0]==x)/sum(row[4] for row in leaves if row[0]==x) for x in (0,1)]==[F(7,8),F(9,8)]
    L=tuple(max(F(0),r-lam) for r in R_V)
    assert L==(F(0),1-lam,F(3,2)-lam)
    G={(x,u):R_U[u]-lam+sum(kernel(ts[x],u)[v]*L[v] for v in range(3)) for x,u in product((0,1),repeat=2)}
    for x in (0,1):
        assert G[x,0]==(F(3,2)-ts[x])*(c[x]-lam)
        assert G[x,1]==F(5,2)-2*lam+ts[x]*(lam-F(1,2))>0
    assert 3*G[0,0]+G[1,0]==0
    E={x:sum(Q_XU[x,u]*(R_U[u]-lam+max(F(0),G[x,u])) for u in (0,1)) for x in (0,1)}
    assert E[0]>=F(3,4)*(1-lam)>0
    assert E[1]>=F(3,2)-F(5,4)*lam>0
    full=2*(1-lam)+sum(E.values())
    LR={}
    for h in product((0,1),repeat=2):
        ex={x:sum(Q_XU[x,u]*(R_U[u]-lam+h[u]*G[x,u]) for u in (0,1)) for x in (0,1)}
        LR[h]=2*(1-lam)+sum(max(F(0),z) for z in ex.values())
    lr=max(LR.values())
    assert LR[(0,1)]==LR[(1,1)]==lr
    assert lr==F(17,4)-4*lam+(t0+3*t1)/8*(lam-F(1,2))
    assert full-lr==gap
    if t0!=t1: assert G[0,0]*G[1,0]<0 and gap>0
    else: assert gap==G[0,0]==G[1,0]==0
    return lam,gap,full,lr,leaves
def brute(leaves,lam,is_full):
    den=lcm(*(z.denominator for row in leaves for z in row[3:]))
    a,b=lam.denominator,lam.numerator
    entries=[(x,u,v,a*int(p*den)-b*int(q*den)) for x,u,v,p,q in leaves]
    N=18 if is_full else 7
    best=None
    for bits in range(1<<N):
        value=0
        for x,u,v,co in entries:
            if is_full:
                early=(bits>>x)&1
                middle=(bits>>(2+2*x+u))&1
                last=(bits>>(6+6*x+3*u+v))&1
            else:
                early=(bits>>x)&1
                middle=(bits>>(2+u))&1
                last=(bits>>(4+v))&1
            t=2 if not early else (3 if not middle else (4 if not last else 5))
            value+=t*co
        if best is None or value>best: best=value
    return F(best,den*a)
if __name__=='__main__':
    grid=(F(1,32),F(1,16),F(3,32),F(1,8),F(5,32),F(3,16),F(7,32))
    for a,b in product(grid,repeat=2): analyze(a,b)
    print('EXACT_PARAMETER_PAIRS',len(grid)**2)
    for a,b in ((F(1,16),F(1,8)),(F(1,8),F(1,16)),(F(1,8),F(1,8))):
        lam,gap,f,l,leaves=analyze(a,b)
        assert brute(leaves,lam,True)==f and brute(leaves,lam,False)==l
        print(f't0={a} t1={b} lambda={lam} FULL={f} LR={l} GAP={gap}')
    lam,gap,*_=analyze(F(1,16),F(1,8))
    assert lam==F(155,182) and gap==F(3,1456)
    assert 182*gap==F(3,8) and gap/(1+lam)==F(3,2696)
    print('FULL_DETERMINISTIC_EACH 262144 LR_DETERMINISTIC_EACH 128')
    print('OPTIMIZED_FIXED_EXAMPLE H=182TP-155TQ GAP=3/8 LINFINITY_BOUND=3/2696')
    print('PASS_EXACT_R5_THREECLASS_AFFINE_TIME_HULL_RIGIDITY')
