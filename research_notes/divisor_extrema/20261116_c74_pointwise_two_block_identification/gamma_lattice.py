"""Exact coefficients of the shifted Gamma-product asymptotic via its step recurrence."""
from math import comb, lcm
from fractions import Fraction as Q
import json


def coefficients(k, step_exponent=4):
    e=step_exponent
    d=3*k*e//4
    assert d*4==3*k*e
    a=Q(4+k,4)
    b=k+1
    coefficients=[]
    # term[j] multiplies n^(d-j); match powers n^(d+e-j-1).
    for j in range(d+1):
        s=Q(0)
        power=d+e-j-1
        for i,t in enumerate(coefficients):
            # coefficient in (n+a)^e (n+1)^(d-i) - (n+b)^e n^(d-i)
            for l in range(e+1):
                h=power-e+l
                if 0<=h<=d-i:
                    s+=t*comb(e,l)*a**l*comb(d-i,h)
                if h==d-i:
                    s-=t*comb(e,l)*b**l
        if j==0:
            assert s==0
            coefficients.append(Q(1))
        else:
            coefficients.append(s/j)
    return coefficients


if __name__=='__main__':
    # Independently test the general induction at additional odd block inventories.
    for k in range(1,12,2):
        for j,t in enumerate(coefficients(k)):
            num,den=t.as_integer_ratio()
            v2=((abs(num)&-abs(num)).bit_length()-(den&-den).bit_length())
            assert v2==-3*j-(j-j.bit_count())
    results=[]
    for k in (3,5):
        coeff=coefficients(k)
        denom=lcm(*(x.denominator for x in coeff))
        integers=[int(denom*x) for x in coeff]
        vals=[(x&-x).bit_length()-1 for x in integers]
        assert vals[-1]==0 and all(x>0 for x in vals[:-1])
        N=[20,50,101,1200]
        assert all(sum(t*n**(len(integers)-1-j) for j,t in enumerate(integers))%2==1 for n in N)
        results.append(dict(k=k,denominator=denom,coefficient_valuations=vals,
                            coefficients_descending=integers))
    print(json.dumps(results,indent=2))
