#!/usr/bin/env python3
"""D25 original finite Clausen two-port prime-power valuation strata.
AUTHOR_SIDE / FINITE_EXACT / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0.
Frozen science: c47e13e4aba0e006366f989d6334d443f6333ae3.
Domain: 5<=p<=167 prime, p**r<=2_000_000, r>=1.
No floating arithmetic, no division by a p-nonunit.
"""
import math
import json
import hashlib
from pathlib import Path

LIMIT=2_000_000
PMAX=167

def primes(n):
    return [p for p in range(5,n+1)
            if all(p%d for d in range(2,math.isqrt(p)+1))]

def vpunit(x,p):
    assert x>0
    v=0
    while x%p==0:
        x//=p;v+=1
    return v,x

def ports(p,r):
    q=p**r
    if q%6==1:
        e=0;m=(q-1)//6
    elif q%6==5:
        e=1;m=(q-5)//6
    else:
        raise AssertionError((p,r,q))
    unit=pow(2,m,q)
    v=0
    U=unit
    V=((1-6*e)*unit)%q
    inv2=pow(2,-1,q)
    for k in range(m):
        v1,a=vpunit(m-k,p)
        v2,b=vpunit(2*m+e-k,p)
        v3,d=vpunit(k+1,p)
        v+=v1+v2-2*v3
        assert v>=0,("integrality",p,r,k)
        unit=(unit*a*b*inv2*pow(d,-2,q))%q
        c=(unit*pow(p,v,q))%q if v<r else 0
        U=(U+c)%q
        V=(V+(1-6*e+12*(k+1))*c)%q
    def truncated_vp(x):
        if x==0:return r
        v=0
        while x%p==0:
            x//=p;v+=1
        return v
    return {"p":p,"r":r,"N":q,"epsilon":e,"m":m,
            "U_mod_N":U,"V_mod_N":V,
            "truncated_vp_U":truncated_vp(U),
            "truncated_vp_V":truncated_vp(V),
            "product_mod_N":U*V%q}

def independent_ports(m,e):
    q=6*m+1+4*e
    terms=[2**(m-k)*math.comb(m,k)*math.comb(2*m+e,k)
           for k in range(m+1)]
    return (sum(terms)%q,
            sum((1-6*e+12*k)*v for k,v in enumerate(terms))%q)

def chi_minus_six(p):
    a=pow((-6)%p,(p-1)//2,p)
    assert a in (1,p-1)
    return 1 if a==1 else -1

def run():
    records=[]
    cross=[]
    for p in primes(PMAX):
        chi=chi_minus_six(p)
        for r in range(1,20):
            if p**r>LIMIT:break
            z=ports(p,r)
            z["chi_minus_six"]=chi
            expected=(0,r) if chi==1 else ((r+1)//2,r//2)
            observed=(z["truncated_vp_U"],z["truncated_vp_V"])
            assert observed==expected,("valuation-stratum",z,expected)
            assert z["product_mod_N"]==0,("composite-candidate",z)
            if z["m"]<=300:
                assert (z["U_mod_N"],z["V_mod_N"])==independent_ports(z["m"],z["epsilon"]),("independent",z)
                cross.append({"p":p,"r":r,"m":z["m"]})
            records.append(z)
    assert len(records)==124
    assert len(cross)==52
    assert sum(z["m"]>1000 for z in records)==60
    assert sum(z["chi_minus_six"]==1 for z in records)==65
    assert sum(z["chi_minus_six"]==-1 for z in records)==59
    d={"schema":"D25_COMPOSITE_CRT_PRIME_POWER_BRC_EXACT_V1",
       "status":"AUTHOR_SIDE_FINITE_EXACT_UNREVIEWED_NOT_ADMITTED_NOT_NATIVE_H0B0",
       "frozen_science_pin":"c47e13e4aba0e006366f989d6334d443f6333ae3",
       "scope":"All p prime 5<=p<=167 and r>=1 with p^r<=2000000",
       "records":records,"independent_bigint_crosschecks":cross}
    dest=Path("d25_primepower_two_port_valuation_records_20261111.json")
    dest.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
    print(json.dumps({"cases":len(records),"independent_cases":len(cross),
          "above_H40_m1000":60,"ordinary":65,"inert":59,
          "sha256":hashlib.sha256(dest.read_bytes()).hexdigest()},
          ensure_ascii=False))
if __name__=="__main__":run()
