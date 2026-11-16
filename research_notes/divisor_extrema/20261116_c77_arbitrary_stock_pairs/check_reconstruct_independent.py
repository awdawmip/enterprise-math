"""Independent Euclidean rational reconstruction and three coefficient recovery."""
from fractions import Fraction as F
from math import gcd
import json


def dyadic_power(k):
    return F(2**k) if k >= 0 else F(1, 2**(-k))


def valuation(x):
    num=abs(x.numerator)
    den=x.denominator
    if not num:
        raise ValueError("zero coefficient")
    return (num & -num).bit_length()-(den & -den).bit_length()


def reconstruct(y, T):
    # Rows (m,0),(b,1) have r = t*b mod m. Stop at first r <= B.
    scale=dyadic_power(valuation(y))
    unit=y/scale
    B=1<<T
    m=4*B*B
    b=unit.numerator*pow(unit.denominator,-1,m)%m
    old_r,r=m,b
    old_t,t=0,1
    while r>B:
        q,rem=divmod(old_r,r)
        old_r,r=r,rem
        old_t,t=t,old_t-q*t
    assert 0 < r <= B and 0 < abs(t) <= B and t%2 and gcd(r,t)==1
    assert (r-t*b)%m==0
    return scale*F(r,t)


def height(x):
    return (max(abs(x.numerator),x.denominator)-1).bit_length()


def main():
    toy_units=0
    for n in range(-101,102,2):
        for d in range(1,100,2):
            value=F(n,d)
            for k in (-3,0,6):
                true=value*dyadic_power(k)
                y=true*(1+F(3<<64,5))
                assert reconstruct(y,height(true))==true
                toy_units+=1
    inputs=((F(3,2),F(5,3),F(7,4)),(F(91,13),F(9,14),F(1,4)),
            (F(25,2),F(17,8),F(19,9)))
    recoveries=0
    for A,H,L in inputs:
        for H,L in ((H,L),(L,H)):
            P=175
            h=P/(A*H)
            ell=P/(A*L)
            R0=(P+H)*L/((P+L)*H)
            coeff=[R0,R0*(ell-h),-h*R0*(ell-h)]
            T=max(map(height,coeff))
            s=F(1<<(2*T+2+max(height(h),height(ell))),23)
            data=(P+H)/(P+L)*(s*P+A*L)/(s*P+A*H)
            out=[]
            for known in coeff:
                r=reconstruct(data,T)
                assert r==known
                out.append(r)
                data=(data-r)/s
            hh=-out[2]/out[1]
            ee=hh+out[1]/out[0]
            K=out[0]*ee/hh
            recover_A=(1/hh-K/ee)/(K-1)
            assert recover_A==A and P/(A*hh)==H and P/(A*ee)==L
            recoveries+=1
    # Verify constant absorption and derivative uniformly above base without log functions.
    C=30000
    assert C+20<2**15
    assert (166*15+24)*30<13*C
    # ln(2)>1/2 bounds the derivative of 166 log2(C+20) by 332/(C+20)
    assert 332*30<13*(C+20)
    return dict(signed_unit_and_valuation_lifts=toy_units,
                full_three_coefficient_decodes=recoveries,
                threshold_validation="3*C>=770*M+166*log2(C+20)+24 for C>=300*M,M>=100")


if __name__=="__main__":
    print(json.dumps(main(),indent=2))
