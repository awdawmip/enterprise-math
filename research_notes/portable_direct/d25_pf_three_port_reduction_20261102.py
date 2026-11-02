#!/usr/bin/env python3
"""Exact p-adic check of model-specific PF three-port Teichmuller reduction; not a native experiment."""
import json
from math import isqrt, comb

def primes_through(limit):
    composite=bytearray(limit+1)
    for d in range(2,isqrt(limit)+1):
        if not composite[d]:
            composite[d*d::d]=b'\x01'*((limit-d*d)//d+1)
    return [p for p in range(5,limit+1) if not composite[p]]

def evaluate(p,name,power):
    M=p**power
    if name=="A":
        numerator=lambda k:(2*k+1)*(3*k+1)*(3*k+2)
        den_const,zden,weight=18,2,6
    else:
        numerator=lambda k:(4*k+1)*(2*k+1)*(4*k+3)
        den_const,zden,weight=32,9,8
    z=pow(zden,-1,M)
    omega=pow(z,p*p,M)
    f=[0]*9
    coeff=1
    for k in range(p):
        kj=1
        for j in range(9):
            f[j]=(f[j]+coeff*kj)%M
            kj=(kj*k)%M
        if k+1<p:
            coeff=coeff*numerator(k)*z*pow(den_const*(k+1)**3,-1,M)%M
    coeff_w=1
    y_w=0
    for k in range(p):
        y_w=(y_w+(1+weight*k)*coeff_w)%M
        if k+1<p:
            coeff_w=coeff_w*numerator(k)*omega*pow(den_const*(k+1)**3,-1,M)%M
    y_z=(f[0]+weight*f[1])%M
    q=((pow(z,p-1,M)-1)%M)//p
    return f,q,(y_w-y_z)%M,z

def ratiomod(a,b,M):
    return a*pow(b,-1,M)%M

def verify_one(p):
    M=p**3
    out={}
    for name in ("A","B"):
        f,q,diff,z=evaluate(p,name,3)
        assert f[0]%p==0 and f[1]%p==0,(p,name,"CM double zero",f[:2])
        if name=="A":
            s1=ratiomod(3,2,M);s2=ratiomod(13,18,M);s3=ratiomod(1,9,M)
            c=6;alpha=2
        else:
            s1=ratiomod(3,2,M);s2=ratiomod(11,16,M);s3=ratiomod(3,32,M)
            c=8;alpha=ratiomod(-11,4,M)
        ratio=z*pow(1-z,-1,M)%M
        f3model=ratio*(s1*f[2]+s2*f[1]+s3*f[0])%M
        assert f3model==f[3],(p,name,"PF closure")
        for j in range(6):
            lower=sum(comb(j,h)*f[h+3] for h in range(j))
            rhs=sum(comb(j,h)*(s1*f[h+2]+s2*f[h+1]+s3*f[h]) for h in range(j+1))
            assert ratio*(lower+rhs)%M==f[j+3],(p,name,"PF recurrence",j)
        reduced=(c*q*f[2]+p*(q*(f[1]//p)+c*q*f[2]+alpha*q*q*f[2]))%(p*p)
        assert diff%p==0
        delta=diff//p
        assert reduced==delta,(p,name,"reduced vs direct",reduced,delta)
        generic=(c*q*f[2]+p*(q*(f[1]//p)+c*q*f[2]+ratiomod(1,2,p*p)*q*q*(f[2]+c*(f[3]-f[2]))))%(p*p)
        assert generic==delta,(p,name,"generic vs direct")
        out[name]={"q":q,"f0_over_p":f[0]//p,"f1_over_p":f[1]//p,"f2_mod_p2":f[2]%(p*p),"f3_mod_p":f[3]%p,"delta":delta,"pf_boundary_mod_p3":(f[3]-f3model)%M}
    G=(out["A"]["delta"]-2*out["B"]["delta"])%(p*p)
    return {"p":p,"A":out["A"],"B":out["B"],"G":G,"digits":[G%p,G//p]}

def main():
    ps=[p for p in primes_through(3000) if p%24 in (13,19)]
    certs=[]
    for p in ps:
        v=verify_one(p)
        if p in (13,19,37,61,373,1171):
            certs.append(v)
    print("THEOREM_CHECK: PF_REDUCTION_AND_3PORT_TEICH = PASS")
    print("DOMAIN: all p<=3000 with p%24 in (13,19)")
    print("TARGET_PRIMES_CHECKED:",len(ps))
    print("ALL_CHECKS: CM_DOUBLE_ZERO, PF_CLOSURE_AND_JETS_3_TO_8_MOD_P3, REPAIRED_DELTA_MOD_P2, GENERIC_FOUR_JET, DIRECT_WEIGHTED_LIFT")
    for v in certs:
        print("CERT",json.dumps(v,separators=(',',':'),sort_keys=True))

if __name__=="__main__":
    main()
