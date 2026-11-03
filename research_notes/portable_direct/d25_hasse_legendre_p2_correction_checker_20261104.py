#!/usr/bin/env python3
"""Independent exact certificate: original Hasse vs Legendre p^2 harmonic tangent.
No native H0/B0 computation. Standard-library integers only.
"""
from math import comb
import json

def primes_upto(n):
    flag=[True]*(n+1);flag[0:2]=[False,False]
    for i in range(2,int(n**.5)+1):
        if flag[i]:
            for j in range(i*i,n+1,i):flag[j]=False
    return [i for i in range(n+1) if flag[i]]

def invs(p):
    return [0]+[pow(i,-1,p) for i in range(1,p)]

def poly_mul(x,y,m):
    a,b=x;c,d=y
    o8=pow(8,-1,m)
    return ((a*c-b*d*o8)%m,(a*d+b*c+b*d)%m)

def poly_eval(cs,m):
    z=(0,0);powt=(1,0)
    for c in cs:
        z=((z[0]+c*powt[0])%m,(z[1]+c*powt[1])%m)
        powt=poly_mul(powt,(0,1),m)
    return z

def run(p):
    r=(p-1)//6;n=2*r;mod=p*p; invp=invs(p)
    # Independent raw Hasse coefficients, literal Legendre coefficients and harmonic tangent.
    a=[]; ell=[]; rhs=[]
    h=1; d=0
    for j in range(n+1):
        aa=(comb(3*r,j)*pow(4,j,mod)*comb(6*r-2*j,j)*pow(pow(27,j,mod),-1,mod))%mod
        ll=(((-1)**j)*comb(2*r,j)*comb(2*r+j,j))%mod
        a.append(aa);ell.append(ll)
        rhs.append((h*d)%p)
        assert (aa-ll-p*rhs[-1])%mod==0,(p,j,aa,ll,rhs[-1],h,d)
        if j<n:
            d=(d+invp[(6*(j+1))%p]-2*invp[(3*j+2)%p])%p
            h=(h*(3*j+1)*(3*j+2)*pow(9*(j+1)**2,-1,p))%p
    res={"p":p,"r":r,"coefficients_checked":n+1,"coefficient_correction_pass":True}
    if p%24 in (13,19):
        res["target_odd_harmonic_mod_p"]=poly_eval(rhs,p)[1]
    if p in (7,13,19,37,43,373):
        A=poly_eval(a,mod);L=poly_eval(ell,mod);D=poly_eval(rhs,p)
        assert A[0]%p==L[0]%p and A[1]%p==L[1]%p
        delta=(((A[0]-L[0])//p)%p,((A[1]-L[1])//p)%p)
        assert D==delta,(p,A,L,D,delta)
        res.update({"Hasse_ring_mod_p2":list(A),"Legendre_ring_mod_p2":list(L),
                    "normalized_difference_mod_p":list(delta),"harmonic_formula_mod_p":list(D)})
        if p in (13,19,373):
            assert A[0]%p==A[1]%p==L[0]%p==L[1]%p==0,(p,A,L)
            res["CM_supersingular_vanishing"] = True
    return res

if __name__=='__main__':
    ps=[p for p in primes_upto(2000) if p>3 and p%6==1]
    rr=[run(p) for p in ps]
    data={"domain":"all primes 7<=p<=2000 with p=1 mod6", "prime_count":len(ps),
          "coefficient_cases":sum(x['coefficients_checked'] for x in rr),
          "failures":0,"target_primes":sum("target_odd_harmonic_mod_p" in x for x in rr),
          "target_nonzero_odd_correction":sum(x.get("target_odd_harmonic_mod_p",0)!=0 for x in rr),
          "target_odd_zero_primes":[x["p"] for x in rr if "target_odd_harmonic_mod_p" in x and x["target_odd_harmonic_mod_p"]==0],
          "selected":[x for x in rr if "Hasse_ring_mod_p2" in x]}
    print(json.dumps(data,indent=2))
