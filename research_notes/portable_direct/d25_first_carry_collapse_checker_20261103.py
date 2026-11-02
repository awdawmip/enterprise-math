#!/usr/bin/env python3
"""Author-side exact D25 first-carry/second-carry verification.
Independent recurrences for original finite 216 F and Gauss G.
No use of native H0/B0 or formal Source service.
"""
from math import comb
import json

def recurrences(p):
    M=p**3
    gk=fk=1
    G=DG=W=0
    for k in range(p):
        G=(G+gk)%M
        DG=(DG+2*k*gk)%M
        W=(W+(6*k+1)*fk)%M
        if k<p-1:
            n=k+1
            gk=(gk*(6*k+1)*(3*k+1)*pow(36*n*n,-1,M))%M
            fk=(fk*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*n*n*n,-1,M))%M
    return G,DG,W

def defect_two_prefix(p):
    r=(p-1)//6
    ak=1; Lam=Gam=0; S=0
    for k in range(1,r+1):
        s=k-1
        Lam=(Lam+pow(2,s,p)*ak)%p
        Gam=(Gam+s*pow(2,s,p)*ak)%p
        L=comb(r,k)*comb(2*r,k)%p
        S=(S+L*pow(2,-k,p)*((6*k-5)*Lam-6*Gam))%p
        if k<r:
            ak=(ak*18*(s+1)**2*pow((6*s+11)*(3*s+5),-1,p))%p
    return -S*pow(5,-1,p)%p

def run(p):
    assert p>3 and p%24 in (13,19)
    M=p**3
    G,d,W=recurrences(p)
    assert G%p==0 and W%p**2==p
    H=G//p
    h=H%p
    d0=d%p
    j=(d0*pow(2,-1,p))%p
    term1=(6*H*d-1)%(p*p)
    assert term1%p==0
    carry1=term1//p
    E_direct=((W-(G*G+6*G*d))%M)//(p*p)
    E_prefix=defect_two_prefix(p)
    assert E_direct==E_prefix
    second=(carry1+h*h+E_prefix)%p
    scalar=(W-p)%(p*p*p)//(p*p)
    assert second==scalar==0
    root_by_h=(pow(2,-1,p*p)-6*p*h*h)%(p*p)
    root_by_newton=(pow(2,-1,p*p)-p*h*pow(d0,-1,p))%(p*p)
    assert root_by_h==root_by_newton
    assert (G+(root_by_h-pow(2,-1,p*p))*d)%(p*p)==0
    assert 12*j*h%p==1
    return {"p":p,"gauss_value_over_p_mod_p2":H,"gauss_derivative_mod_p2":d%(p*p),
            "h_mod_p":h,"j_mod_p":j,"first_carry":12*j*h%p,
            "second_product_carry":carry1,"square_carry":h*h%p,
            "clausen_defect":E_prefix,"second_residue":second,
            "root_mod_p2":root_by_h,"W_mod_p3":W}

if __name__=='__main__':
    samples=[13,19,37,43,181,373,1171,3019]
    out=[run(p) for p in samples]
    print(json.dumps({"status":"PASS","count":len(out),"results":out},indent=2))
    with open('/mnt/data/d25_first_carry_collapse_results_20261103.json','w') as f:
        json.dump({"status":"PASS","results":out},f,indent=2)
