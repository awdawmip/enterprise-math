#!/usr/bin/env python3
"""T6 p13 vertical order one (0,1): complete exact affine q0 search.
Companion: T6_P13_Q0_STATIC_GS_EXACT_CHECK_20261123.py.
Author executed finite result, not independent review or Native admission.
"""
import importlib.util
import math
from pathlib import Path
from fractions import Fraction
from sympy import Matrix

src=Path(__file__).with_name("T6_P13_Q0_STATIC_GS_EXACT_CHECK_20261123.py")
spec=importlib.util.spec_from_file_location("t6_p13_q0", src)
base=importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
P,CAP,N,W=base.P,base.CAP,base.N,base.W
U=base.R*Matrix.diag(*(Fraction(1,w) for w in W))
assert all(x.q==1 for x in U)
UI=U.inv()
D,mu,dmin=base.D,base.mu,base.d

def particular(q,r):
    u=[0]*N
    A=[[int(i==j) for j in range(N)] for i in range(N)]
    for k in range(1,7):
        mod=P**k
        h=[pow(j,-k,mod) for j in range(1,P)]
        res=(-pow(P*q+r,-k,mod)-sum(a*b for a,b in zip(u,h)))%mod
        v=[sum(a*b for a,b in zip(row,h))%mod for row in A]
        piv=next(i for i,x in enumerate(v) if x%P)
        inv=pow(v[piv],-1,mod)
        u=[a+((res*inv)%mod)*b for a,b in zip(u,A[piv])]
        old=A[piv]
        A=[[mod*x for x in row] if i==piv else
           [a-((v[i]*inv)%mod)*b for a,b in zip(row,old)]
           for i,row in enumerate(A)]
    for k in range(1,7):
        mod=P**k
        assert (sum(x*pow(j,-k,mod) for j,x in enumerate(u,1))+
                pow(P*q+r,-k,mod))%mod==0
    return u

def check(r):
    a=P*(P+r)
    mass=a-1
    radius=(CAP-mass)**2+CAP**2
    assert radius<dmin
    u0=particular(1,r)
    c=[Fraction(x) for x in Matrix(1,N,u0)*UI]
    z=c[:]; n=[0]*N
    nodes=0; leaves=0; budget_valid=0
    def walk(i,spent):
        nonlocal nodes,leaves,budget_valid
        if i<0:
            leaves+=1
            final=[sum((c[j]+n[j])*Fraction(int(U[j,t])) for j in range(N))
                   for t in range(N)]
            assert all(x.denominator==1 for x in final)
            q0=[int(x) for x in final]
            plus=sum(w*max(0,x) for w,x in zip(W,q0))
            minus=sum(w*max(0,-x) for w,x in zip(W,q0))
            budget_valid+=int(plus+mass<=CAP and minus<=CAP)
            return
        nodes+=1
        center=c[i]+sum(z[j]*mu[j][i] for j in range(i+1,N))
        near=math.floor(-center)
        for ni in (near,near+1):
            new=spent+D[i]*(center+ni)**2
            if new<=radius:
                z[i]=c[i]+ni
                n[i]=ni
                walk(i-1,new)
        z[i]=c[i]
    walk(N-1,Fraction(0))
    return {'r':r,'denominator':a,'vertical_cost':mass,'radius_squared':radius,
            'GS_nodes':nodes,'sphere_leaves':leaves,'budget_valid':budget_valid}

rows=[check(r) for r in range(1,P)]
expect=[5,5,2,6,6,8,2,2,6,3,4,2]
assert [x['GS_nodes'] for x in rows]==expect
assert sum(expect)==51
assert all(x['sphere_leaves']==0 and x['budget_valid']==0 for x in rows)
print('AUTHOR_EXACT_Q1_SPLIT0_1_GLOBAL_EMPTY',rows)
print('Summary: 12 states, 51 exact GS nodes, 0 sphere leaves; T6 OPEN')
