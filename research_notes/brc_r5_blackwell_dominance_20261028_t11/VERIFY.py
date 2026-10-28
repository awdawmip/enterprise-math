"""Exact R5 compression test; uses frozen earlier tree observer module.
Run from a checkout of awdawmip/enterprise-math. No stochastic approximations.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import sys
OLD = Path(__file__).resolve().parents[1]/'brc_r5_two_upstream_signed_phase_transition_20261028_t11'
sys.path.insert(0,str(OLD))
from VERIFY import tree, observation, P, Q, C
th,a,b=F(3,4),F(1,4),F(1,8)

def lift(xu,xv,zu,zv):
    s=xu+xv; D=xu-xv; z=s+th*(zu+zv)
    sp=max(abs(D),z/(1+th)); xp=(sp+D)/2; vp=(sp-D)/2
    y=(z-sp)/(th*sp) if sp else F(0)
    assert 0<=xp<=1 and 0<=vp<=1 and 0<=y<=1
    return xp,vp,xp*y,vp*y,s-sp

def mass(xu,xv,zu,zv,d):
    q=(1-th)*d; h=th*(a*zu+b*zv)/2;s=xu+xv
    m={F(1,2):h,1-d:(1-th)*xv/2,1-q:(1-xv)/2,
       F(1):th*s/2-2*h,1+q:(1-xu)/2,1+d:(1-th)*xu/2,F(3,2):h}
    assert sum(m.values())==1 and sum(r*w for r,w in m.items())==1
    return m

def rocmember(ob,d):
    ep,eq,tp,tq=ob; q=(1-th)*d
    D=2*(tp-tq)/q; Z=2*(tq-1);S=max(abs(D),Z/(1+th))
    if S>min(2-abs(D),Z):return False
    xp,vp=(S+D)/2,(S-D)/2
    y=(Z-S)/(th*S) if S else F(0)
    if not(0<=xp<=1 and 0<=vp<=1 and 0<=y<=1):return False
    m=mass(xp,vp,xp*y,vp*y,d)
    for t in m:
        w=ep-t*(1-eq)
        lo=sum(((r-t)*v for r,v in m.items() if r<t),F(0))
        hi=sum(((r-t)*v for r,v in m.items() if r>t),F(0))
        if not lo<=w<=hi:return False
    return True

def test():
    H=(2+th)*b-th*a
    assert H==F(5,32)
    for d in (F(1,10),F(10,29)):
        q=(1-th)*d; assert 2*th*q/(1-2*q)<=H
        count=0
        for xu,xv in product((F(0),F(1,4),F(1,2),F(3,4),F(1)),repeat=2):
            for uu,vv in product((F(0),F(1,2),F(1)),repeat=2):
                zu,zv=xu*uu,xv*vv
                xp,vp,zup,zvp,delta=lift(xu,xv,zu,zv)
                lhs=(a*zup+b*zvp)-(a*zu+b*zv)
                assert lhs>=H*delta/(2*th)
                for xs,vs,zs,ws in ((xu,xv,zu,zv),(xp,vp,zup,zvp)):
                    assert all(v>=0 for v in mass(xs,vs,zs,ws,d).values())
                old,new=mass(xu,xv,zu,zv,d),mass(xp,vp,zup,zvp,d)
                for k in sorted(set(old)|set(new)):
                    assert sum(w*max(r-k,0) for r,w in new.items()) >= sum(w*max(r-k,0) for r,w in old.items())
                count+=1
        print('flow grid exact',d,count)
    xu,xv,zu,zv=F(1,8),F(1),F(1,8),F(0)
    xp,vp,zup,zvp,delta=lift(xu,xv,zu,zv)
    assert (xp,vp,zup+zvp,delta)==(F(0),F(7,8),F(11,24),F(1,4))
    assert (a*zup+b*zvp)-(a*zu+b*zv)==F(5,192)
    rows=tree(th,F(1,10),a,b)
    full=set();N=0
    for roots in product((P,Q,C),repeat=2):
      for cs in product((P,Q,C),repeat=2):
       for side in product((P,Q),repeat=2):
        for last in product((P,Q),repeat=6):
         full.add(observation(rows,roots,cs,side,last));N+=1
    assert (N,len(full))==(20736,380)
    assert all(rocmember(o,F(1,10)) for o in full)
    print('pure full observers exactly reachable',N,len(full))
    print('ALL EXACT DOMINANCE CHECKS PASSED')
if __name__=='__main__':test()
