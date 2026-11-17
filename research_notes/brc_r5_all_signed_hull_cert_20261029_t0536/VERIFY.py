#!/usr/bin/env python3
"""Exact rational finite-strategy hull certificates for two-law finite-horizon policies.

The mathematical reduction requires that each (time, information-state)
node is visited at most once along a trajectory. Inputs are exact Fractions;
SymPy simplex only produces candidate rational witnesses, checked again by Fraction.
"""
from fractions import Fraction as F
from itertools import product
from sympy.solvers.simplex import linprog, InfeasibleLPError
from sympy import Rational, Matrix

S=(F(1,2),F(1),F(3,2))


def f4(v):
    assert len(v)==4
    return tuple(map(F,v))


def add(a,b):
    return tuple(x+y for x,y in zip(a,b))


def mul(q,v):
    return tuple(q*x for x in v)


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F(0))


def basic_kernel(p):
    assert F(0)<p<F(1,2)
    q=(p,F(1)-2*p,p)
    assert sum(q)==1 and sum(x*y for x,y in zip(S,q))==1
    return q


def origin_plan(p,plan,root_mass=F(1,2)):
    """Origin-level contribution to (e_P,e_Q,T_P,T_Q)."""
    q=basic_kernel(p)
    if plan=='STOP_Q':
        return (root_mass,F(0),root_mass,root_mass)
    if plan=='STOP_P':
        return (F(0),root_mass,root_mass,root_mass)
    assert len(plan)==3 and set(plan)<=set('PQ')
    ep=sum((root_mass*qj*sj for sj,qj,a in zip(S,q,plan) if a=='Q'),F(0))
    eq=sum((root_mass*qj for sj,qj,a in zip(S,q,plan) if a=='P'),F(0))
    return (ep,eq,2*root_mass,2*root_mass)


PLANS=('STOP_Q','STOP_P')+tuple(''.join(x) for x in product('PQ',repeat=3))


def vertices(pa,pb):
    full=[]
    lr=[]
    for plan_a in PLANS:
        for plan_b in PLANS:
            full.append(add(origin_plan(pa,plan_a),origin_plan(pb,plan_b)))
        lr.append(add(origin_plan(pa,plan_a),origin_plan(pb,plan_a)))
    return tuple(dict.fromkeys(full)),tuple(dict.fromkeys(lr))


def to_sym(x):
    return Rational(x.numerator,x.denominator)


def to_frac(x):
    n,d=Rational(x).as_numer_denom()
    return F(int(n),int(d))


def primal_membership(target, lr):
    """Return <=5-sparse rational convex combination or None (exact LP)."""
    lr=tuple(dict.fromkeys(lr))
    k=len(lr)
    Aeq=[[to_sym(v[j]) for v in lr] for j in range(4)] + [[Rational(1)]*k]
    beq=[to_sym(z) for z in target]+[Rational(1)]
    try:
        obj,weights=linprog([Rational(0)]*k,A=[[Rational(0)]*k],b=[Rational(0)],A_eq=Aeq,b_eq=beq)
    except InfeasibleLPError:
        return None
    z=[to_frac(x) for x in weights]
    assert all(x>=0 for x in z) and sum(z)==1
    assert all(sum(z[i]*lr[i][j] for i in range(k))==target[j] for j in range(4))
    while sum(x>0 for x in z)>5:
        supp=[i for i,x in enumerate(z) if x]
        A=Matrix([[to_sym(lr[i][j]) for i in supp] for j in range(4)]+[[Rational(1)]*len(supp)])
        dependence=A.nullspace()[0]
        alpha=[to_frac(t) for t in dependence]
        assert any(t>0 for t in alpha) and any(t<0 for t in alpha)
        t=min(z[i]/ai for i,ai in zip(supp,alpha) if ai>0)
        for i,ai in zip(supp,alpha): z[i]-=t*ai
    assert all(x>=0 for x in z) and sum(z)==1
    assert all(sum(z[i]*lr[i][j] for i in range(k))==target[j] for j in range(4))
    return tuple((i,w) for i,w in enumerate(z) if w)


def exact_separating_hyperplane(target,lr):
    """Return integer w and rational intercept with w.target < intercept <= w.LR.

    Strong separation is rescaled so (w.target)-(intercept) <= -1.
    """
    lr=tuple(dict.fromkeys(lr))
    # x=(w0,w1,w2,w3,b).  Require b-w.v_j<=0; w.target-b<=-1.
    A=[[-to_sym(v[j]) for j in range(4)]+[Rational(1)] for v in lr]
    B=[Rational(0)]*len(lr)
    A.append([to_sym(z) for z in target]+[Rational(-1)])
    B.append(Rational(-1))
    _,sol=linprog([Rational(0)]*5,A=A,b=B,bounds=[(None,None)]*5)
    w=tuple(to_frac(q) for q in sol[:4]); intercept=to_frac(sol[4]);
    assert dot(w,target)<intercept
    assert all(dot(w,v)>=intercept for v in lr)
    return w,intercept


def main():
    pa,pb=F(1,4),F(1,8)
    positive_full,positive_lr=vertices(pa,pa)
    assert len(positive_full)>=len(positive_lr)
    # Complete, closed-form 2-sparse certificate for *every* full deterministic policy.
    for a,b in product(PLANS,repeat=2):
        lhs=add(origin_plan(pa,a),origin_plan(pa,b))
        lr_a=mul(2,origin_plan(pa,a))
        lr_b=mul(2,origin_plan(pa,b))
        assert lhs==mul(F(1,2),add(lr_a,lr_b))
    print('POSITIVE_IDENTICAL_ORIGINS: 100/100 exact 2-support hull certificates')
    witness=add(origin_plan(pa,'QQP'),origin_plan(pb,'STOP_Q'))
    full,lr=vertices(pa,pb)
    assert witness in full
    w=(F(32),F(32),F(3),F(0))
    v_lr=min(dot(w,v) for v in lr)
    v_full=min(dot(w,v) for v in full)
    gap=v_lr-v_full
    assert witness==(F(13,16),F(1,8),F(3,2),F(3,2))
    assert (v_full,v_lr,gap)==(F(69,2),F(35),F(1,2))
    assert all(dot(w,v)>=35 for v in lr)
    print('DISTINCT_ORIGINS: full_distinct='+str(len(full))+' lr_distinct='+str(len(lr)))
    print('WITNESS: '+str(witness))
    print('INTEGER_SEPARATING_DIRECTION: '+str(w))
    print('MIN_FULL='+str(v_full)+' MIN_LR='+str(v_lr)+' GAP='+str(gap))
    print('ALL_REAL_SEEDLESS_LR_LINFTY_DISTANCE_BOUND='+str(gap/sum(map(abs,w))))
    # Nontrivial primal example (source-distributed policy with genuine averaging)
    target=add(origin_plan(pa,'QQP'),origin_plan(pa,'STOP_Q'))
    primal=primal_membership(target,positive_lr)
    assert primal is not None
    print('SYMPY_EXACT_PRIMAL_CERTIFICATE='+str(primal))
    # Solver produces exact dual; verify separately using Fraction.
    d_w,d_b=exact_separating_hyperplane(witness,lr)
    assert dot(d_w,witness)<d_b<=min(dot(d_w,v) for v in lr)
    print('SYMPY_EXACT_FARKAS_DIRECTION='+str(d_w))
    print('SYMPY_EXACT_FARKAS_INTERCEPT='+str(d_b))
    # Parametric all-signed gap formula on all 4 observer coordinates.
    cases=0
    for p,q in product((F(1,8),F(1,6),F(1,4),F(1,3)),repeat=2):
        ff,ll=vertices(p,q)
        for a,b,tc,td in product((F(-2),F(0),F(1),F(2)),(F(-1),F(0),F(1)),(F(-1,2),F(0),F(1,3)),(F(-1,4),F(1,4))):
            m=min(a,b)
            h=min(a/2,b)+min(3*a/2,b)-2*m
            d1=tc+td+p*h;d2=tc+td+q*h
            formula=(abs(d1)+abs(d2)-abs(d1+d2))/4
            cc=(a,b,tc,td)
            lhs=min(dot(cc,v) for v in ll)-min(dot(cc,v) for v in ff)
            assert lhs==formula, (p,q,cc,lhs,formula)
            cases+=1
    print('ALL_SIGNED_GAP_FORMULA: '+str(cases)+' exact rational model-direction cases (including negative coefficients)')
    print('PASS_EXACT_R5_ALL_SIGNED_FINITE_HULL_CERT')

if __name__=='__main__':
    main()
