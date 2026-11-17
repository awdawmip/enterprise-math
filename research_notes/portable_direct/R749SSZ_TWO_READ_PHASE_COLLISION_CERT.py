#!/usr/bin/env python3
"""R749SSZ: exact two-read collisions with strict third-read separation.
Frozen scientific input: enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Exact integer and rational arithmetic throughout; requires Python 3 and SymPy.
"""
import json
from functools import lru_cache
from pathlib import Path
import sympy as sp

q,k=sp.symbols("q k",integer=True,nonnegative=True)
S=18*q**4+54*q**3-345*q**2+2070*q-16315

@lru_cache(maxsize=None)
def counts(m):
    a=[0]*m;a[0]=1
    for w in (1,1,2,3,6):
        for n in range(w,m):
            a[n]+=a[n-w]
    C=sum(a)
    a=[0]*m;a[0]=1
    for w in (1,2,3,6):
        for n in range(w,m):
            a[n]+=a[n-w]
    b=[0]*m
    for n in range(1,m):
        b[n]=sum(j*a[n-j] for j in range(1,n+1))
    return int(C),int(sum(b))

def phases():
    out={}
    for r in range(6):
        data=[(6+r+6*j,counts(6+r+6*j)) for j in range(9)]
        C=sp.interpolate([(n,v[0]) for n,v in data[:6]],q)
        T=sp.interpolate([(n,v[1]) for n,v in data[:7]],q)
        assert sp.degree(C,q)==5 and sp.degree(T,q)==6
        assert all(C.subs(q,n)==v[0] and T.subs(q,n)==v[1] for n,v in data)
        out[r]=(sp.factor(C),sp.factor(T))
    return out

def two_read(phase,r1,r2,h):
    C1,T1=phase[r1];C2,T2=phase[r2]
    vals=[]
    for j in (0,1):
        a=q+6*j;b=q+h+6*j
        Y=a**3*T1.subs(q,a)/C1.subs(q,a)-S.subs(q,a)/108
        X=sp.factor((Y+S.subs(q,b)/108)/b**3)
        B=sp.factor(X*C2.subs(q,b)-T2.subs(q,b))
        vals.append((X,B))
    (x0,b0),(x1,b1)=vals
    D=sp.factor((b0-b1)/(x1-x0))
    E=sp.factor(b0+x0*D)
    for j in (0,1):
        a=q+6*j;b=q+h+6*j
        A=a**3*T1.subs(q,a)/C1.subs(q,a)-S.subs(q,a)/108
        B=b**3*(T2.subs(q,b)+E)/(C2.subs(q,b)+D)-S.subs(q,b)/108
        assert sp.cancel(A-B)==0
    return E,D

def positive_shifted(poly,lower):
    coeff=sp.Poly(sp.expand(poly.subs(q,lower+k)),k).all_coeffs()
    assert all(c.is_Integer and c>0 for c in coeff)
    return {"degree":len(coeff)-1,"min_coefficient":str(min(coeff)),
            "coefficients_high_to_low":[str(c) for c in coeff]}

def parameter_certificate(value,lower):
    num,den=sp.fraction(sp.factor(value))
    return {label:positive_shifted(expr,lower) for label,expr in (
        ("den",den),("upper",2*den-num),("lower",2*den+num))}

def exact_read(n,e,d):
    C,T=counts(n)
    return sp.factor(n**3*(T+e)/(C+d)-S.subs(q,n)/108)

def main():
    assert counts(500)==(7677066992,643545647661)
    phase=phases()
    cases={}
    for label,r1,r2,h,lower in (
        ("residues_1_5",1,5,4,73),("residues_2_4",2,4,2,14)):
        E,D=two_read(phase,r1,r2,h)
        bounds={"E":parameter_certificate(E,lower),
                "D":parameter_certificate(D,lower)}
        C1,T1=phase[r1];C2,T2=phase[r2]
        a=q+12;b=q+h+12
        first=a**3*T1.subs(q,a)/C1.subs(q,a)-S.subs(q,a)/108
        third=b**3*(T2.subs(q,b)+E)/(C2.subs(q,b)+D)-S.subs(q,b)/108
        residual=sp.factor(third-first)
        rn,rd=sp.fraction(residual)
        future={"negative_numerator":positive_shifted(-rn,lower),
                "positive_denominator":positive_shifted(rd,lower)}
        ev=sp.factor(E.subs(q,lower));dv=sp.factor(D.subs(q,lower))
        assert -2<ev<2 and -2<dv<2
        y0=exact_read(lower,sp.Integer(0),sp.Integer(0))
        y1=exact_read(lower+6,sp.Integer(0),sp.Integer(0))
        assert y0==exact_read(lower+h,ev,dv)
        assert y1==exact_read(lower+h+6,ev,dv)
        cases[label]={
            "q_mod_6":r1,"p_mod_6":r2,"p_minus_q":h,
            "lower_q":lower,"E_of_q":str(E),"D_of_q":str(D),
            "limit_E":str(sp.limit(E,q,sp.oo)),
            "limit_D":str(sp.limit(D,q,sp.oo)),
            "strict_bounds_coefficient_guards":bounds,
            "third_read_difference_alternative_minus_original":str(residual),
            "third_read_negative_coefficient_guards":future,
            "witness":{"q":lower,"p":lower+h,"E":str(ev),"D":str(dv),
                "first_equal_read":str(y0),"second_equal_read":str(y1),
                "third_difference":str(sp.factor(residual.subs(q,lower)))}
        }
    result={
        "unit":"R749SSZ","status":"PASS",
        "evidence":"AUTHOR_EXACT_NOT_REVIEWED",
        "scientific_pin":"awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389",
        "methods":"exact six-phase generating functions and rational polynomial sign certificates",
        "statement":"two-read exact collisions exist at arbitrarily large cutoffs for residue pairs (1,5) and (2,4); the constructed collisions always separate at third read",
        "cases":cases
    }
    dest=Path(__file__).with_name("R749SSZ_TWO_READ_PHASE_COLLISION_RESULTS.json")
    dest.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print("PASS: 2 infinite rational collision families, 156 positive parameter-guard coefficients, 74 positive third-read sign coefficients")
    print(dest)

if __name__=="__main__":
    main()
