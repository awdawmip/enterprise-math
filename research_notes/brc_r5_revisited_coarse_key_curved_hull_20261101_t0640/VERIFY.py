#!/usr/bin/env python3
"""Exact rational checks for R5 two-visit stationary LR-key carrier.
Only the finite checks identified below are computation; continuum results
are proved algebraically in RESEARCH.md.
"""
from fractions import Fraction as F
from itertools import product

ONE = F(1)
ZERO = F(0)

def lr(p, rho):
    return (p, (ONE-rho)*(ONE-p), rho*(ONE-p)*p, rho*(ONE-p)**2)

def full(p1, p2, rho):
    return (p1, (ONE-rho)*(ONE-p1), rho*(ONE-p1)*p2,
            rho*(ONE-p1)*(ONE-p2))

def convex_mix(weights, vectors):
    return tuple(sum((w*v[k] for w,v in zip(weights,vectors)), ZERO)
                 for k in range(4))

def exact_qp_atoms(masses):
    # two equiprobable hidden origins i, final label s=0/1.
    Q = {(i,k,s): masses[k]*F(1,2)*F(1,2)
         for i in (0,1) for k in range(4) for s in (0,1)}
    P = {(i,k,s): masses[k]*F(1,2)*(F(1,4) if s == 0 else F(3,4))
         for i in (0,1) for k in range(4) for s in (0,1)}
    assert sum(Q.values(),ZERO) == ONE
    assert sum(P.values(),ZERO) == ONE
    for atom,q in Q.items():
        if q:
            assert P[atom]/q == (F(1,2) if atom[-1] == 0 else F(3,2))
    return Q,P

def main():
    rhos = [F(1,3),F(1,2),F(2,3)]
    grid = [F(j,12) for j in range(13)]
    checked=0
    for rho,p in product(rhos,grid):
        z=lr(p,rho)
        assert sum(z,ZERO)==ONE
        assert z[2]+z[3]==rho*(ONE-p)
        exact_qp_atoms(z)
        assert z[2]<=rho/F(4)
        checked+=1
    print('Q_P_NORMALIZED_RATIO_AND_LR_BRANCH_CHECKS',checked)

    full_checks=0
    for rho in rhos:
        for a,b,c,d in product([ZERO,F(1,2),ONE],repeat=4):
            z=convex_mix([F(1,2),F(1,2)], [full(a,b,rho),full(c,d,rho)])
            p1=z[0]
            p2= z[2]/(rho*(ONE-p1)) if p1!=ONE else ZERO
            assert ZERO<=p2<=ONE
            assert z==full(p1,p2,rho)
            full_checks+=1
    print('SOURCE_AGGREGATION_FLOW_MARKOVIZATION_CHECKS',full_checks)

    exposed_checks=0
    for rho,p0,p in product(rhos,grid,grid):
        # L_p0= -qF-2*rho*(1-p0)*qS1
        ell=lambda z: -z[3]-2*rho*(ONE-p0)*z[0]
        assert ell(lr(p0,rho))-ell(lr(p,rho))==rho*(p-p0)**2
        exposed_checks+=1
    print('EXPOSED_QUADRATIC_IDENTITY_CHECKS',exposed_checks)

    hull_checks=0
    for rho,t,theta in product(rhos,grid,[ZERO,F(1,4),F(1,2),F(3,4),ONE]):
        low=lr(t,rho)
        upper=convex_mix([ONE-t,t],[lr(ZERO,rho),lr(ONE,rho)])
        z=convex_mix([ONE-theta,theta],[low,upper])
        r=(ONE-theta)*rho*(ONE-t)**2+theta*rho*(ONE-t)
        assert z==(t,(ONE-rho)*(ONE-t),rho*(ONE-t)-r,r)
        assert rho*(ONE-t)**2<=r<=rho*(ONE-t)
        hull_checks+=1
    print('EXACT_CURVED_HULL_WITNESS_CHECKS',hull_checks)

    rho=F(1,2)
    witness=full(ZERO,ONE,rho)
    assert witness==(ZERO,F(1,2),F(1,2),ZERO)
    assert max(lr(p,rho)[2] for p in grid)==F(1,8)
    assert witness[2]-F(1,8)==F(3,8)
    assert lr(F(1,2),rho)==(F(1,2),F(1,4),F(1,8),F(1,8))
    # delta is the root of z^2-3z+1=0 in (3/8,2/5).
    assert F(3,8)**2-3*F(3,8)+ONE>0
    assert F(2,5)**2-3*F(2,5)+ONE<0
    assert (F(1,2)-F(3,8)* (ONE-F(3,8))/2)>F(3,8)
    print('RHO',rho)
    print('FULL_WITNESS',witness)
    print('LR_MAX_SECOND_STOP',F(1,8))
    print('SIGNED_SUPPORT_GAP',F(3,8))
    print('EXACT_LINF_DISTANCE', '(3-sqrt(5))/2')
    print('PASS_EXACT_R5_REVISITED_KEY_NONPOLYHEDRAL_HULL_AND_FLOW')

if __name__=='__main__':
    main()
