#!/usr/bin/env python3
"""R253: exact singleton-mask denominator and output-size obstruction.

Uses only integer/Fraction arithmetic; fixed frozen R252 input at s=2/5.
"""
from fractions import Fraction
from math import gcd
import json,hashlib
from pathlib import Path

SOURCE='43ec6098b1330ae86d0a7863be336c5d97f6ef34'
A,B=37422,2053

def singleton(k):
    assert isinstance(k,int) and k>=0
    return Fraction(A*pow(5,k),B*pow(12,k))

def denominator_formula(k):
    return B * 2**max(2*k-1,0) * 3**max(k-5,0)

def modular_closed(k,p):
    assert gcd(B*12,p)==1
    return (A*pow(5,k,p)*pow(B*pow(12,k,p)%p,-1,p))%p

def reconstruct_from_frozen_model():
    s=Fraction(2,5)
    t=(1691*s-2615)/(2615*s-3539)
    a=[Fraction(1,5),Fraction(1,4),Fraction(3,10),Fraction(9,20),s,Fraction(2,3),t]
    b=[Fraction(13,60)]+[Fraction(5,18)*abs(Fraction(1,2)-x) for x in a[1:]]
    pi=[bi/(1-ai) for ai,bi in zip(a,b)]
    assert sum(pi)==1
    z=sum(bi/(1-ai)**2 for ai,bi in zip(a,b))
    rho0=b[0]/(z*(1-a[0])**2)
    P00=a[0]+(1-a[0])*pi[0]
    return 144*rho0,P00

def checked():
    scalar,transition=reconstruct_from_frozen_model()
    assert scalar==Fraction(A,B) and transition==Fraction(5,12)
    assert gcd(A,B)==1
    assert A%2==0 and A%4!=0
    assert A%3**5==0 and A%3**6!=0
    assert gcd(A,5)==1 and gcd(B,60)==1
    evidence=[]
    iterated=scalar
    checkpoints=set([0,1,2,5,6,7,12,63,127,234,500,1000])
    for k in range(1001):
        if k in checkpoints: assert iterated==singleton(k)
        iterated*=transition
    for k in [0,1,2,5,6,7,12,63,127,234,500,1000]:
        v=singleton(k)
        d=denominator_formula(k)
        assert v.denominator==d
        for p in [1000000007,1000000009]:
            left=v.numerator%p*pow(v.denominator%p,-1,p)%p
            assert left==modular_closed(k,p)
        evidence.append({'k':k,'event_n':k+1,'denominator_bits':d.bit_length(),'numerator_bits':v.numerator.bit_length(),'value_mod_p':[modular_closed(k,p) for p in (1000000007,1000000009)]})
    data={'schema':'EM_R253_EXACT_SINGLETON_OUTPUT_SIZE_V1','source_pin':SOURCE,'parameter_s':'2/5','mask':0,'weight':144,'rho_0':'2079/16424','weighted_rho_0':'37422/2053','self_loop':'5/12','formula':'h_0,k=(37422/2053)*(5/12)^k','reduced_denominator':'2053*2^max(2k-1,0)*3^max(k-5,0)','valuation_facts':{'v2_37422':1,'v3_37422':5,'gcd_37422_2053':1,'gcd_2053_60':1},'consequence':'omega(k) output bit length of 63-label exact rational result for s=2/5','checks':evidence,'exact_checks':len(evidence),'independent_recurrence_iterations':1001,'modular_checks':len(evidence)*2,'all_pass':True,'review':'NOT_REVIEWED','scope':'fixed rational parameter, singleton m=0; no claim of global scalar output lower bound or full native BRC histogram'}
    out=Path(__file__).with_name('R253_verification.json')
    raw=json.dumps(data,indent=2,sort_keys=True,ensure_ascii=False)+'\n'
    out.write_text(raw,encoding='utf-8')
    print('PASS',data['exact_checks'],'integer denominators',data['modular_checks'],'modular crosschecks')
    print('SHA256',hashlib.sha256(raw.encode()).hexdigest())
    print('BITS',[(a['k'],a['denominator_bits']) for a in evidence])
    return data

if __name__=='__main__': checked()
