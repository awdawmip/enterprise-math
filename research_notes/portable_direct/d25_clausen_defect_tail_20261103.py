#!/usr/bin/env python3
"""D25 exact finite-Clausen defect via far-upper Gauss tail and two low-prefix moments."""
import json
from d25_hensel_root_20261103 import primes,gauss_coefficients,original_coefficients,ell_coefficients,jets

def check(p):
    r=(p-1)//6
    m=p**3;z0=pow(2,-1,m)
    G=gauss_coefficients(p,3)
    F=original_coefficients(p,3)
    gv,gd,_=jets(G,z0,m)
    fv,fd,_=jets(F,z0,m)
    original_diff=(fv+3*fd-gv*gv-6*gv*gd)%m
    assert original_diff%(p*p)==0
    E=(original_diff//(p*p))%p
    assert G[-1]%(p*p)==0
    U=(G[-1]//(p*p))%p
    ell=ell_coefficients(p,1)
    a=1
    Lam=0;Gam=0;total=0
    for k in range(1,r+1):
        s=k-1
        val=a*pow(2,s,p)%p
        Lam=(Lam+val)%p
        Gam=(Gam+s*val)%p
        term=(6*k-5)*Lam-6*Gam
        total+=ell[k]*pow(2,-k,p)*term
        den=(6*s+11)*(3*s+5)
        a=(a*(s+1)*(s+1)*18*pow(den,-1,p))%p
    Econj=(-2*U*total)%p
    assert E==Econj,(p,E,Econj)
    return {"p":p,"r":r,"U":U,"defect_original":E,
            "defect_prefix":Econj,"prefix_final":[Lam,Gam],"status":"PASS"}

def main():
    out=[check(p) for p in primes(10000)]
    sample=[v for v in out if v['p'] in (13,19,37,43,181,373,1171)]
    print(json.dumps({"schema":"D25_CLAUSEN_DEFECT_LOWHIGH_PREFIX_V1",
        "p_range":"7<=p<=10000,p mod24=13 or 19",
        "checked":len(out),"status":"PASS","samples":sample,
        "native_H0_B0":"NOT_EXECUTED",
        "mathematical_admission":"UNREVIEWED_NOT_ADMITTED"},indent=2))
if __name__=='__main__':main()
