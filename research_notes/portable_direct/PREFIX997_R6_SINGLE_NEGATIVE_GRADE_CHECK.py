#!/usr/bin/env python3
"""PREFIX-997: signed Stage46 one-negative grade, exact integer and brute word checks."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
import json

D = 6
MAX_N = 12

def dynamic_amplitude():
    states = {((0,)*D,-1,0):1}  # (relative displacement,incoming label,negative count)
    result = []
    for n in range(1,MAX_N+1):
        nxt = defaultdict(int)
        for (x,h,c),amp in states.items():
            for j in range(1,D+1):
                v=list(x);v[j-1]+=1
                nxt[(tuple(v),-j,c)]+=amp*(-5 if h==j else 1)
                if c==0:
                    v=list(x);v[j-1]-=1
                    nxt[(tuple(v),j,1)]+=amp*(-5 if h==-j else 1)
        states=nxt
        numerator=sum(amp*amp for (x,h,c),amp in states.items() if c==1)
        result.append(dict(n=n,one_negative_mass_num=numerator,
                           denominator=36**n,
                           fraction=str(Fraction(numerator,36**n)),
                           retained_states_total=len(states)))
    return result

def independent_enumeration(n):
    # Explicitly enumerate n*6**n words. Do not reuse the dynamic recurrence.
    fibers=defaultdict(int)
    diagonal=0
    for s in range(n):
        for axes in product(range(1,D+1),repeat=n):
            r=axes[s]
            left=1 if s==0 else axes[s-1]
            b=int(left==r)+(int(axes[s+1]==r) if s+1<n else 0)
            weight=(-5)**b
            diagonal+=weight*weight
            k=[0]*D
            for t,j in enumerate(axes):
                k[j-1]+=(-1 if t==s else 1)
            last_incoming=axes[-1] if s==n-1 else -axes[-1]
            fibers[(tuple(k),last_incoming)]+=weight
    return sum(z*z for z in fibers.values()),diagonal,len(fibers)

def run():
    res=dynamic_amplitude()
    checks=[]
    for n in range(1,6):
        observed,diagonal,fibers=independent_enumeration(n)
        assert observed==res[n-1]["one_negative_mass_num"],(n,observed)
        checks.append(dict(n=n,signed_words_enumerated=n*D**n,
                           endpoint_port_fibers=fibers,
                           coherent_numerator=observed,incoherent_diagonal_numerator=diagonal))
    assert res[0]["fraction"]=="5/6"
    assert res[1]["fraction"]=="5/6"
    assert res[2]["fraction"]=="25/432"
    assert checks[2]["incoherent_diagonal_numerator"]==11880
    assert checks[4]["incoherent_diagonal_numerator"]==816480
    return dict(schema="PREFIX997_ONE_NEGATIVE_GRADE_EXACT_V1",
        status="AUTHOR_ANALYTIC_LEMMA_EXACT_INTEGER_CHECKED_NOT_REVIEWED",
        frozen_p000="f42f2906d77f24085c123f3ccfe9667d41caa96d",
        candidate="Stage46 C[h,j]=1/6-1[h=j]",
        max_n=MAX_N,integer_dp=res,independent_exhaustive_word_checks=checks)

if __name__=="__main__":
    out=run()
    with open("PREFIX997_R6_EXACT_RESULTS.json","w",encoding="utf-8") as f:
        json.dump(out,f,indent=2,sort_keys=True);f.write("\n")
    print("RESULTS:",[(z["n"],z["fraction"]) for z in out["integer_dp"]])
    print("BRUTE:",out["independent_exhaustive_word_checks"])
    print("ALL_ASSERTIONS_PASSED")
