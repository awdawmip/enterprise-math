#!/usr/bin/env python3
"""Exact all-policy tests for the source-specific C->L compensation theorem.

Requires sibling VERIFY.py for the exact 2D rational convex hull routines.
Universal all-real result follows from the source-specific Bellman proof, not
from this finite rational regression.
"""
from fractions import Fraction as F
from itertools import product
from VERIFY import ONE, ZERO, HALF, hull, inside, cross


def theta(alpha,kappa):
    return (ONE+kappa*(ONE-2*alpha))/alpha


def obs(a0,a1,k0,k1,bits,lr=False):
    tp=tq=pp=qq=ZERO

    def leaf(q,lam,t):
        nonlocal tp,tq,pp,qq
        p=lam*q
        tp+=p*t; tq+=q*t; pp+=p; qq+=q

    def action(i,key):
        if lr:return bits[{'A':0,'D':1,'Y':2,'L':3}[key[0]]]
        m={'A':i,'D':2+i,'Y':4+i}
        return bits[m[key]] if key in m else bits[6+3*i+{'LC':0,'LD':1,'LY':2}[key]]

    for i,(a,k) in enumerate(((a0,k0),(a1,k1))):
        q=HALF
        if not action(i,'A'):
            leaf(q,ONE,1)
            continue
        d=q*a; c=q*(ONE-2*a); y=q*a
        if not action(i,'D'):leaf(d,HALF,2)
        else:
            leaf(d*F(2,3),F(1,4),3)
            leaf(d*F(1,3),ONE,3+action(i,'LD'))
        leaf(c*(ONE-k),ONE,2)
        leaf(c*k,ONE,3+action(i,'LC'))
        if not action(i,'Y'):leaf(y,F(3,2),2)
        else:
            leaf(y*HALF,F(2),3)
            leaf(y*HALF,ONE,3+action(i,'LY'))
    return tp,tq,pp,qq


def test_case(a0,a1,k0,k1,number):
    assert all(ZERO<a<HALF for a in (a0,a1))
    assert all(ZERO<k<ONE for k in (k0,k1))
    T0,T1=theta(a0,k0),theta(a1,k1)
    LR=[]; FULL=[]
    for bits in product((0,1),repeat=4):
        x,y,pm,qm=obs(a0,a1,k0,k1,bits,True)
        assert (pm,qm)==(ONE,ONE)
        LR.append((x,y))
    for bits in product((0,1),repeat=12):
        x,y,pm,qm=obs(a0,a1,k0,k1,bits,False)
        assert (pm,qm)==(ONE,ONE)
        FULL.append((x,y))
    P=hull(LR)
    outsiders=[(x,y) for x,y in FULL if not inside(P,(x,y))]
    if T0==T1:
        assert len(outsiders)==0,(a0,a1,k0,k1,outsiders[:2])
        print(f'case{number:02d} theta_equal={T0} alpha=({a0},{a1}) kappa=({k0},{k1}) FULL_outside_LR_hull=0 LR_vertices={len(P)}')
    else:
        t=(T0+T1)/2
        u=2*(t+ONE);v=-(2*t+3)
        D0=a0*(t-T0);D1=a1*(t-T1)
        expected=(abs(D0)+abs(D1)-abs(D0+D1))/4
        assert expected==min(a0,a1)*abs(T0-T1)/4
        score=lambda xy:u*xy[0]+v*xy[1]
        FM=max(map(score,FULL));LM=max(map(score,LR))
        assert FM-LM==expected,(FM,LM,expected)
        assert outsiders
        print(f'case{number:02d} theta=({T0},{T1}) alpha=({a0},{a1}) kappa=({k0},{k1}) H=({u},{v}) gap={expected} outsiders={len(outsiders)}')
    return len(outsiders)


def main():
    cases=[
        (F(1,4),F(1,5),F(3,4),F(1,6)),  # exact origin compensation, theta=11/2
        (F(1,4),F(1,5),F(9,10),F(4,15)), # exact origin compensation, theta=29/5
        (F(1,4),F(1,4),F(1,4),F(1,4)),
        (F(1,4),F(1,8),F(1,4),F(1,4)),
        (F(1,4),F(1,4),F(1,4),F(3,4)),
        (F(1,4),F(1,5),F(1,4),F(1,6)),
    ]
    for j,x in enumerate(cases,1):test_case(*x,j)
    print('policy_enumeration=4096_FULL+16_LR_each; cases=6; all Fraction arithmetic')
    print('PASS_EXACT_R5_SOURCE_SPECIFIC_C_DETOUR_TIME_HULL_COMPENSATION')

if __name__=='__main__':main()
