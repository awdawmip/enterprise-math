#!/usr/bin/env python3
"""D25 exact coordinate gauge: original E3 published coefficient + independent direct polynomial toy.
AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0.
Source: 20261111_onhour_d25_E3_actual_formal_p_series_zp_p3.md
"""
from math import comb

def mul(a, b, degree, modulus):
    out=[0]*(degree+1)
    for i,x in enumerate(a[:degree+1]):
        if not x: continue
        for j,y in enumerate(b[:degree+1-i]):
            out[i+j]=(out[i+j]+x*y)%modulus
    return out

def compose(f, g, degree, modulus):
    out=[0]*(degree+1)
    power=[1]+[0]*degree
    for coeff in f[:degree+1]:
        if coeff:
            out=[(u+coeff*v)%modulus for u,v in zip(out,power)]
        power=mul(power,g,degree,modulus)
    return out

def direct_checks():
    cases=[]
    for p in (5,7,11,13):
        mod=p**3
        series=[0]+[comb(p,j)%mod for j in range(1,p+1)]
        for c in (1,2,p-1):
            f=[0,1]+[0]*(p-2)+[c]
            inverse=[0,1]+[0]*(p-2)+[-c%mod]
            assert compose(f,inverse,p,mod)==[0,1]+[0]*(p-1)
            transformed=compose(f,compose(series,inverse,p,mod),p,mod)
            assert transformed[p] == (series[p] + (pow(p,p,mod)-p)*c)%mod
            cases.append((p,c,transformed[p]))
    return cases

def original_e3_p373():
    p=373
    mod=p**3
    # Previously independent-original-E3-computed [z^p][p] coefficient, from immutable source note.
    old=(42842780,8783031)
    assert tuple(x%p for x in old)==(0,0)
    assert tuple(x%p**2 for x in old)==(130177,17904)
    assert tuple((x//p)%p for x in old)==(349,48)
    out={}
    for label,c in (("0",(0,0)),("1",(1,0)),("T",(0,1)),("1+T",(1,1))):
        shifted=tuple((old[i]+(pow(p,p,mod)-p)*c[i])%mod for i in (0,1))
        out[label]=shifted
        assert tuple(x%p for x in shifted)==(0,0)
        assert tuple((x//p)%p for x in shifted)==((349-c[0])%p,(48-c[1])%p)
    assert out=={"0":(42842780,8783031),"1":(42842407,8783031),
                 "T":(42842780,8782658),"1+T":(42842407,8782658)}
    return out

if __name__=="__main__":
    checks=direct_checks()
    print("12 independent direct-composition cases PASS:",checks)
    print("original E3 p373 source-based gauge predictions:",original_e3_p373())
