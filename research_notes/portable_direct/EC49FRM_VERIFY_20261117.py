#!/usr/bin/env python3
"""EC49FRM exact symbolic verification. Run: python EC49FRM_VERIFY_20261117.py

Original five full-named tree cost vectors: EC49FRL_GLOBAL_FIVE_TREE_DEPTH3_CERTIFICATE.json
SHA256 2164b2a374c46bad29d5b669573fcafe87218f946e1bdd42e78dc78642ba0dfb
Frozen original BRC input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
The global unrestricted Bellman-envelope theorem is an inherited, not independently
reviewed mathematical premise; this script checks its exact downstream arithmetic.
"""
from fractions import Fraction as F
from itertools import product
import sympy as S

T = {"A": (6,290,6,751), "B": (5,293,5,704),
     "C": (5,295,5,685), "D": (4,296,4,707),
     "E": (4,298,4,688)}  # (U_R,U_T,M_R,M_T)
beta = F(620,3299)


def cost(name,x,l):
    ur,ut,mr,mt = T[name]
    return (1-l)*F(ut+x*ur,141)+l*F(mt+x*mr,310)


def value(x,l):
    return min(cost(n,x,l) for n in T)


def mixture(x):
    if x<=3:
        q=F(310,3299)*(5-x)
        return {"B":q, "C":1-q}
    return {"D":beta, "E":1-beta}


def bound(x):
    return F(19,3299)*(5-x) if x<=3 else F(38,3299)


def verify_symbolic():
    x=S.symbols("x",real=True)
    b=S.Rational(620,3299)
    def c(name,l):
        ur,ut,mr,mt=T[name]
        return (1-l)*(ut+x*ur)/141+l*(mt+x*mr)/310
    def dominated_by(winner,l,left,right=None):
        for n in T:
            d=S.cancel(c(n,l)-c(winner,l))
            assert S.simplify(d.subs(x,left))>=0,(winner,l,n,d)
            if right is None:
                assert S.simplify(S.diff(d,x))>=0,(winner,l,n,d)
            else:
                assert S.simplify(d.subs(x,right))>=0,(winner,l,n,d)
    for l,w in [(S.Integer(0),"A"),(S.Integer(1),"C"),(b,"B")]:
        dominated_by(w,l,S.Integer(1),S.Integer(3))
    for l,w in [(S.Integer(0),"D"),(S.Integer(1),"E"),(b,"D")]:
        dominated_by(w,l,S.Integer(3))
    assert S.cancel(c("B",b)-c("C",b))==0
    assert S.cancel(c("D",b)-c("E",b))==0
    for low in (True,False):
        if low:
            q=310*(5-x)/3299
            u=q*c("B",0)+(1-q)*c("C",0)-c("A",0)
            m=q*c("B",1)+(1-q)*c("C",1)-c("C",1)
            dual=c("B",b)-(1-b)*c("A",0)-b*c("C",1)
            r=S.Rational(19,3299)*(5-x)
        else:
            q=b
            u=q*c("D",0)+(1-q)*c("E",0)-c("D",0)
            m=q*c("D",1)+(1-q)*c("E",1)-c("E",1)
            dual=c("D",b)-(1-b)*c("D",0)-b*c("E",1)
            r=S.Rational(38,3299)
        for z in (u,m,dual):
            assert S.cancel(z-r)==0,(z,r)
    print("SYMBOLIC_FULL_X_DOMAINS_PASSED")


def verify_rational_samples():
    prices=[F(1),F(9,8),F(3,2),F(2),F(5,2),F(3),
            F(25,8),F(4),F(10),F(1000)]
    for x in prices:
        p=mixture(x)
        assert sum(p.values())==1 and all(0<=v<=1 for v in p.values())
        rho=bound(x)
        g=[sum(prob*cost(n,x,l) for n,prob in p.items())-value(x,l)
           for l in (F(0),F(1))]
        assert g==[rho,rho],(x,g,rho)
        dual=value(x,beta)-((1-beta)*value(x,F(0))+beta*value(x,F(1)))
        assert dual==rho,(x,dual,rho)
        for n,l in product(T,(F(0),beta,F(1))):
            assert cost(n,x,l)>=value(x,l)
        worst={n:max(cost(n,x,F(0))-value(x,F(0)),
                     cost(n,x,F(1))-value(x,F(1))) for n in T}
        det=min(worst.values())
        assert det==(F(5-x,141) if x<=3 else F(2,141))
        assert rho==det*(1-beta)
        print("x=%s, trees=%s, exact_minimax_regret=%s, five_tree_deterministic=%s"
              %(x,p,rho,det))
    print("EXACT_RATIONAL_SAMPLES_PASSED")


if __name__=="__main__":
    verify_symbolic()
    verify_rational_samples()
