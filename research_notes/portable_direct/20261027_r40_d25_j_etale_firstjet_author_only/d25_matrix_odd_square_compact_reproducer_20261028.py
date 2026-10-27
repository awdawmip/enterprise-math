#!/usr/bin/env python3
"""Auxiliary semilinear-matrix certificate (NOT native H0/B0). Python stdlib."""
from itertools import product
from collections import Counter
import random

def Z(r): return tuple(tuple(0 for _ in range(r)) for _ in range(r))
def I(r): return tuple(tuple(int(i==j) for j in range(r)) for i in range(r))
def plus(a,b,m): return tuple(tuple((x+y)%m for x,y in zip(s,t)) for s,t in zip(a,b))
def times(a,k,m): return tuple(tuple(k*x%m for x in s) for s in a)
def mm(a,b,m):
    r=len(a)
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(r))%m for j in range(r)) for i in range(r))
def minus(a,b,m): return plus(a,times(b,-1,m),m)
def comm(a,b,m): return minus(mm(a,b,m),mm(b,a,m),m)
def prod(x,y,m):
    a,b=x;c,d=y
    return plus(mm(a,c,m),times(mm(b,d,m),2,m),m),plus(mm(a,d,m),mm(b,c,m),m)
def sig(x,m): return x[0],times(x[1],-1,m)
def randmat(r,p,rng): return tuple(tuple(rng.randrange(p) for _ in range(r)) for _ in range(r))
def eta(p,A,B,C,D):
    q=p**3;r=len(A)
    return plus(plus(I(r),times(A,p,q),q),times(C,p*p,q),q),plus(times(B,p,q),times(D,p*p,q),q)

def run():
    rng=random.Random(20261028)
    checks=0
    for p in [3,5,7,13,19,37,373]:
        q=p**3
        for r in (1,2,3):
            for _ in range(30):
                A,B,C,D=[randmat(r,p,rng) for j in range(4)]
                x=eta(p,A,B,C,D); square=prod(x,sig(x,q),q)
                even=plus(plus(I(r),times(A,2*p,q),q),times(minus(plus(times(C,2,q),mm(A,A,q),q),times(mm(B,B,q),2,q),q),p*p,q),q)
                odd=times(comm(B,A,q),p*p,q)
                assert square==(even,odd)
                assert square==(minus(mm(x[0],x[0],q),times(mm(x[1],x[1],q),2,q),q),comm(x[1],x[0],q))
                if r==1: assert square[1]==Z(1)
                Cg,Dg=[randmat(r,p,rng) for j in range(2)]
                z=times(Cg,p,q),times(Dg,p,q)
                u=plus(I(r),z[0],q),z[1]
                z2=prod(z,z,q)
                inv=plus(minus(I(r),z[0],q),z2[0],q),plus(times(z[1],-1,q),z2[1],q)
                xp=prod(prod(u,x,q),sig(inv,q),q)
                sqp=prod(xp,sig(xp,q),q)
                assert sqp==prod(prod(u,square,q),inv,q)
                Ap=tuple(tuple(((xp[0][i][j]-int(i==j))//p)%p for j in range(r)) for i in range(r))
                Bp=tuple(tuple((xp[1][i][j]//p)%p for j in range(r)) for i in range(r))
                assert Ap==A and Bp==plus(B,times(Dg,2,p),p)
                assert sqp[1]==times(comm(Bp,A,q),p*p,q)
                checks+=1
    histogram=[]
    for p in (3,5):
        A=((0,0),(0,1)); h=Counter()
        for x in product(range(p),repeat=4):
            B=((x[0],x[1]),(x[2],x[3]))
            h[comm(B,A,p)]+=1
        assert len(h)==p*p and set(h.values())=={p*p}
        histogram.append([p,len(h),p*p])
    p=373;q=p**3
    A=((1,0),(0,0)); B=((0,1),(0,0))
    s0=prod(eta(p,A,Z(2),Z(2),Z(2)),sig(eta(p,A,Z(2),Z(2),Z(2)),q),q)
    s1=prod(eta(p,A,B,Z(2),Z(2)),sig(eta(p,A,B,Z(2),Z(2)),q),q)
    assert s0[0]==s1[0] and s1[1]==((0,51755988),(0,0))
    print({'status':'AUTHOR_EXACT_CHECK_PASS','finite_ring_cases':checks,'gauge_checks':checks,
           'rank_one_zero_checks':210,'small_prime_histograms':histogram,
           'p373_auxiliary_odd_square_12':s1[1][0][1],'native_H0_B0':'NOT_RUN'})
if __name__=='__main__': run()
