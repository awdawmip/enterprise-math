#!/usr/bin/env python3
"""Exact two-path integer certificate for D25 composite-modulus Clausen ports.

Finite domain: 0<=m<=1000, epsilon=0 or 1, N=6m+1+4*epsilon>=5.
Neither this script nor finite agreement proves the conjecture for all m.
"""
import json
from math import comb, isqrt
from pathlib import Path
import sys

def prime(n):
    if n<2: return False
    return all(n%d for d in range(2,isqrt(n)+1))

def ports_by_binom(m,e):
    a=b=0
    for k in range(m+1):
        t=comb(m,k)*comb(2*m+e,k)*(1<<(m-k))
        a+=t
        b+=(1-6*e+12*k)*t
    return a,b

def ports_by_recurrence(m,e):
    a=b=0
    c1=c2=1
    for k in range(m+1):
        t=(c1*c2)<<(m-k)
        a+=t
        b+=(1-6*e+12*k)*t
        if k<m:
            assert c1*(m-k)%(k+1)==0
            assert c2*(2*m+e-k)%(k+1)==0
            c1=c1*(m-k)//(k+1)
            c2=c2*(2*m+e-k)//(k+1)
    return a,b

def certify(max_m=1000):
    rows=[]
    totals={}
    keys=("cases","prime","composite","A_zero","B_zero","both_zero",
          "neither_zero","product_zero","product_nonzero",
          "split_composite","prime_rule_pass","prime_rule_fail")
    for e in (0,1):
        c={k:0 for k in keys}
        for m in range(max_m+1):
            n=6*m+1+4*e
            if n<5: continue
            a,b=ports_by_binom(m,e)
            assert (a,b)==ports_by_recurrence(m,e),(e,m,"crosscheck")
            x,y=a%n,b%n
            is_p=prime(n)
            c["cases"]+=1
            c["prime" if is_p else "composite"]+=1
            c["A_zero"]+=(x==0)
            c["B_zero"]+=(y==0)
            c["both_zero"]+=(x==0 and y==0)
            c["neither_zero"]+=(x!=0 and y!=0)
            c["product_zero"]+=(x*y%n==0)
            c["product_nonzero"]+=(x*y%n!=0)
            c["split_composite"]+=(not is_p and x!=0 and y!=0 and x*y%n==0)
            if is_p:
                a_expected=m%4 in (2,3)
                valid=(x==0 and y!=0) if a_expected else (y==0 and x!=0)
                c["prime_rule_pass" if valid else "prime_rule_fail"]+=1
                assert pow(n-6,(n-1)//2,n)==(n-1 if a_expected else 1)
            assert x*y%n==0,(e,m,n,x,y,"counterexample")
            rows.append(dict(epsilon=e,m=m,N=n,is_prime=is_p,
                 A_scaled_mod_N=x,B_scaled_mod_N=y,AB_scaled_mod_N=x*y%n))
        totals[str(e)]=c
    by_n={r["N"]:r for r in rows}
    for n,expected in ((65,(26,5)),(85,(68,15)),(169,(39,117))):
        r=by_n[n]
        assert (r["A_scaled_mod_N"],r["B_scaled_mod_N"])==expected
    assert totals["0"]["cases"]==1000 and totals["1"]["cases"]==1001
    assert totals["0"]["split_composite"]==totals["1"]["split_composite"]==287
    return dict(schema="D25_COMPOSITE_CRT_TWO_PORT_FINITE_CERTIFICATE_V1",
           source="exact integer binomial recurrence and direct math.comb",
           max_m=max_m,totals=totals,
           illustrations={str(n):by_n[n] for n in (65,85,169)},
           rows=rows,finite_only=True)

if __name__=="__main__":
    result=certify()
    blob=json.dumps(result,ensure_ascii=False,indent=2)+"\n"
    if len(sys.argv)>1: Path(sys.argv[1]).write_text(blob,encoding="utf-8")
    print(json.dumps({k:v for k,v in result.items() if k!="rows"},
                     ensure_ascii=False,indent=2))
