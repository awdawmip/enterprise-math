#!/usr/bin/env python3
"""Author-side exact checks for the N32 threshold theorem.

The universal proof is in PROOF.md. This script does not replace it.
Python standard library only: exact Fraction arithmetic, no floating-point proofs.
"""
from fractions import Fraction as F
import json
from pathlib import Path

def zpoly(n, z):
    m=n-2
    return (4-2**m-2*(1-z)*(2+z)**m-(1+z)*(2-z)**m
            +(2-z)*(1+z)**m)

def root_interval(n, steps=92):
    """Exact dyadic isolating bracket using N31 positive-root uniqueness."""
    d,L,H=1,0,1
    for _ in range(steps):
        d*=2
        L*=2
        H*=2
        mid=(L+H)//2
        f=zpoly(n,F(mid,d))
        if f<0:
            L=mid
        elif f>0:
            H=mid
        else:
            return {"exact_root_dyadic":f"{mid}/{d}"}
    assert H-L==1 and zpoly(n,F(L,d))<0 and zpoly(n,F(H,d))>0
    return {"lower_numerator":str(L),"upper_numerator":str(H),"denominator":str(d)}

def run():
    checks={"rational_recurrence":0,"uniform_brackets":0,
            "threshold_dyadic_roots":0,"nonpositive_gain_witnesses":0}
    zs=[F(0),F(1,7),F(1,3),F(1,2),F(9,10),F(99,100),F(999,1000),F(1)]
    for n in range(4,51):
        m=n-2
        zl=1-F(2,3**m)
        zh=1-F(1,2*3**m)
        assert F(0)<zl<zh<F(1)
        assert zpoly(n,zl)<0 and zpoly(n,zh)>0
        checks["uniform_brackets"]+=1
        for z in zs:
            w=1-z
            expr=(-4-2*z*w*(2+z)**m+z*(1+z)*(2-z)**m
                  -w*(2-z)*(1+z)**m)
            assert zpoly(n+1,z)-2*zpoly(n,z)==expr
            checks["rational_recurrence"]+=1
    roots={}
    for n in (4,5,6,7,8,9,10,15,20,25,30,31,32):
        roots[str(n)]=root_interval(n)
        checks["threshold_dyadic_roots"]+=1
    samples={}
    for z in (F(9,10),F(99,100),F(999,1000),F(9999,10000)):
        m=2
        while (1-z)*3**m<2:
            m+=1
        n=m+2
        assert zpoly(n,z)<0
        checks["nonpositive_gain_witnesses"]+=1
        samples[str(z)]={
            "finite_lifespan_from_n":n,
            "Z_n_sign":"negative",
            "Z_previous_sign":("positive" if n>4 and zpoly(n-1,z)>0 else
                               "zero" if n>4 and zpoly(n-1,z)==0 else
                               "negative" if n>4 else None)
        }
    report={"schema":"EM_BRC_N32_AUTHOR_EXACT_CHECKS_V1",
            "model":"four-label independent positive-mass auxiliary occupancy observer",
            "source":"N31 author-side Z_n and unique positive root; not Source admitted",
            "methods":["Fraction exact endpoint polynomial evaluation",
                       "dyadic rational bisection","exact rational recurrence identity",
                       "finite z witness checks"],
            "checks":checks,"dyadic_isolations":roots,
            "lifespan_examples":samples,
            "limitations":"Finite checks are not a universal proof; no native X6 bridge or Driver review."}
    dest=Path(__file__).with_name("EXACT_CHECKS.json")
    dest.write_text(json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2)+"\n",
                    encoding="utf-8")
    print(json.dumps({"checks":checks,"lifespan_examples":samples},sort_keys=True))

if __name__=="__main__":
    run()
