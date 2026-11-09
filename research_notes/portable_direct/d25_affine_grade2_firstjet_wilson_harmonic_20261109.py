#!/usr/bin/env python3
"""Exact first-jet block formula for grade-two original 216/2304 coefficients."""
from math import factorial, comb
import json

PRIMES=(5,7,11,13,19,37,43,73,109,373)

def run(p):
    p2,p4=p*p,p**4
    fm=[1]
    for k in range(1,p): fm.append(fm[-1]*k % p2)
    H=[0]
    for k in range(1,p): H.append((H[-1]+pow(k,-1,p))%p)
    wilson=((factorial(p-1)+1)//p)%p
    wa0=wa1=vc0=vc1=0
    wa_direct=vc_direct=0
    for n in range(p):
        if 2*n//p+3*n//p==2:
            r2,r3=2*n-p,3*n-p
            base=fm[r2]*fm[r3]*pow(fm[n],-5,p2)*pow(216,-n,p2)%p2
            jet=(H[r2]+H[r3]-2*wilson)%p
            wa0=(wa0+(6*n+1)*base)%p2
            wa1=(wa1+(6*n+1)*(base%p)*jet)%p
            orig=comb(2*n,n)**2*comb(3*n,n)
            assert orig%p2==0
            wa_direct=(wa_direct+(6*n+1)*(orig//p2)*pow(216,-n,p2))%p2
        if 4*n//p==2:
            r4=4*n-2*p
            base=2*fm[r4]*pow(fm[n],-4,p2)*pow(2304,-n,p2)%p2
            jet=2*(H[r4]-wilson)%p
            vc0=(vc0+(8*n+1)*base)%p2
            vc1=(vc1+(8*n+1)*(base%p)*jet)%p
            orig=comb(4*n,2*n)*comb(2*n,n)**2
            assert orig%p2==0
            vc_direct=(vc_direct+(8*n+1)*(orig//p2)*pow(2304,-n,p2))%p2
    assert (wa0+p*wa1)%p2==wa_direct
    assert (vc0+p*vc1)%p2==vc_direct
    return dict(p=p,wilson_mod_p=wilson,W2_base=wa0,W2_jet=wa1,
        W2_direct=wa_direct,V2_base=vc0,V2_jet=vc1,V2_direct=vc_direct)

if __name__=="__main__":
    rows=[run(p) for p in PRIMES]
    lookup={row["p"]:row for row in rows}
    assert lookup[373]["W2_direct"]==68898
    assert lookup[373]["V2_direct"]==87282
    assert (lookup[373]["W2_jet"]-2*lookup[373]["V2_jet"])%373==341
    print(json.dumps({"schema":"D25_GRADE2_FIRST_JET_EXACT_V1",
        "method":"factorial block proof + independent original binomial",
        "rows":rows},indent=2))
    print("PASS: 10 independent exact grade2 first-jet checks")
