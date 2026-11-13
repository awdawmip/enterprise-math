#!/usr/bin/env python3
"""Exact Phase-I simplex feasibility for seven-node martingale coupling.
Works over Fraction; Bland entering and leaving pivot rules; no float/sympy.
For rational source and target satisfying convex order, returns an exact
nonnegative matrix E with the stated target/source martingale marginals.
"""
from fractions import Fraction as F
from VERIFY_PGEQ import R,mass,source,target,lawful,tp,tq


def exact_coupling(x,y, max_pivots=10000):
    lawful(x);lawful(y)
    assert tp(x)==tp(y) and tq(x)==tq(y)
    old=mass(x);new=mass(y)
    n=49;m=21;N=n+m
    a=[[F(0)]*(N+1) for _ in range(m)]
    for i in range(7):
        for j in range(7): a[i][7*i+j]=F(1)
        a[i][-1]=new[i]
    for j in range(7):
        for i in range(7):
            a[7+j][7*i+j]=F(1)
            a[14+j][7*i+j]=R[i]
        a[7+j][-1]=old[j]
        a[14+j][-1]=R[j]*old[j]
    for i in range(m): a[i][n+i]=F(1)
    basis=[n+i for i in range(m)]
    costs=[F(0)]*n+[-F(1)]*m
    for iteration in range(max_pivots+1):
        cB=[costs[b] for b in basis]
        # Reduced costs: maximizing -sum artificial variables.
        entering=None
        basis_set=set(basis)
        for j in range(N):
            if j in basis_set: continue
            rc=costs[j]-sum(cB[i]*a[i][j] for i in range(m))
            if rc>0:
                entering=j
                break  # Bland smallest-index entering variable
        if entering is None:
            obj=sum(cB[i]*a[i][-1] for i in range(m))
            if obj<0: raise ValueError('No nonnegative martingale coupling: exact Farkas witness requires separate extraction')
            if obj!=0: raise AssertionError('Phase I objective positive despite nonnegative artificial vars')
            vals=[F(0)]*N
            for row,b in enumerate(basis):vals[b]=a[row][-1]
            assert all(vals[i]==0 for i in range(n,N))
            E=tuple(tuple(vals[7*i+j] for j in range(7)) for i in range(7))
            assert all(z>=0 for row in E for z in row)
            assert all(sum(E[i])==new[i] for i in range(7))
            assert all(sum(E[i][j] for i in range(7))==old[j] for j in range(7))
            assert all(sum(R[i]*E[i][j] for i in range(7))==R[j]*old[j] for j in range(7))
            return E,iteration
        candidates=[(a[i][-1]/a[i][entering],basis[i],i)
                    for i in range(m) if a[i][entering]>0]
        if not candidates: raise ArithmeticError('Unbounded Phase-I simplex objective')
        ratio,old_basis,leaving=min(candidates)
        pivot=a[leaving][entering]
        assert pivot>0
        a[leaving]=[v/pivot for v in a[leaving]]
        for i in range(m):
            if i==leaving:continue
            z=a[i][entering]
            if z: a[i]=[v-z*w for v,w in zip(a[i],a[leaving])]
        basis[leaving]=entering
    raise TimeoutError(f'Exceeded max_pivots={max_pivots}')

if __name__=='__main__':
    from time import perf_counter
    tests=[(F(1,10),F(3,4),F(1,4),F(1),F(0)),
           (F(1,5),F(1),F(0),F(1),F(0)),
           (F(1,13),F(1),F(1),F(0),F(1)),
           (F(1,7),F(1,2),F(1,4),F(1,2),F(1,2)),
           (F(3,20),F(0),F(0),F(1),F(1)),
           (F(1,10),F(0),F(0),F(0),F(0))]
    for ix,params in enumerate(tests):
        print('TEST',ix+1, 'params',' '.join(map(str,params)),flush=True)
        tic=perf_counter()
        E,it=exact_coupling(source(*params),target(*params))
        print('PASS',it,'pivots',sum(z>0 for row in E for z in row),'positive edges',round(perf_counter()-tic,4),'seconds',flush=True)
