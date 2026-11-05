#!/usr/bin/env python3
"""D25 exact author-side two-moment 216/2304 scan; Python stdlib only.
Sun 2022 Conjecture 5.28, DOI 10.3934/math.2022153; not a proof.
"""
import json
from collections import Counter
from math import comb

CLASSES=(13,17,19,23)

def primes(limit):
    a=bytearray([1])*limit
    a[:2]=b"\0\0"
    for i in range(2,int((limit-1)**.5)+1):
        if a[i]:
            a[i*i::i]=bytes(((limit-1-i*i)//i)+1)
    return (p for p in range(5,limit) if a[p])

def moments(p,power=3,raw=False):
    q=p**power
    a=b=1
    A=B=DA=DB=W=V=0
    for k in range(p):
        if raw:
            a=comb(2*k,k)**2*comb(3*k,k)*pow(pow(216,k,q),-1,q)%q
            b=comb(2*k,k)**2*comb(4*k,2*k)*pow(pow(2304,k,q),-1,q)%q
        A=(A+a)%q;B=(B+b)%q
        DA=(DA+k*a)%q;DB=(DB+k*b)%q
        W=(W+(6*k+1)*a)%q;V=(V+(8*k+1)*b)%q
        if k+1<p and not raw:
            a=a*(2*k+2)*(2*k+1)*(3*k+3)*(3*k+2)*(3*k+1)*pow(216*(k+1)**5,-1,q)%q
            b=b*(4*k+4)*(4*k+3)*(4*k+2)*(4*k+1)*pow(2304*(k+1)**4,-1,q)%q
    chi=1 if p%3==1 else -1
    H=(A+7*chi*B)%q
    G=(6*DA-8*DB-(1+7*chi)*B)%q
    E=(W-V)%q
    assert (H+G-E)%q==0
    return dict(p=p,chi=chi,q=q,A=A,B=B,DA=DA,DB=DB,W=W,V=V,H=H,G=G,E=E)

def run():
    rows=[moments(p) for p in primes(10000) if p%24 in CLASSES]
    assert len(rows)==616
    failures=[x['p'] for x in rows if (x['H'],x['G'],x['E'])!=(0,0,0)]
    assert not failures,failures
    checks=(13,17,19,23,37,43,139,373)
    for p in checks:
        assert moments(p)==moments(p,raw=True),p
    sharp=[dict(p=p,H_over_p3=moments(p,4)['H']//p**3,
                E_over_p3=moments(p,4)['E']//p**3) for p in (13,17,19,23,37,43)]
    counts=Counter(x['p']%24 for x in rows)
    output={'schema':'D25_INERT_DUAL_MOMENT_EXACT_COMPUTATION_V1',
            'date':'2026-11-06','count':len(rows),'counts':dict(sorted(counts.items())),
            'failures':failures,'direct_binomial_crosschecks':checks,'p4_sharpness':sharp,
            'samples':[x for x in rows if x['p'] in (13,17,19,23,139,373)],
            'out_of_domain': [moments(p) for p in (5,7,11)],
            'claim':'EXACT_FINITE_VALIDATION_ONLY_NOT_A_PROOF_OR_NATIVE_RESULT'}
    print(json.dumps(output,indent=2,sort_keys=True))
    return output

if __name__=="__main__":
    run()
