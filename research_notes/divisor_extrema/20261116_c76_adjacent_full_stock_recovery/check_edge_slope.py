"""Exact local slope and its derivative for the retained outer block at x=1."""
from fractions import Fraction as F
from math import prod
import json

def code(A,T,A1,T1):
    p,q=15,F(75,4)
    k=(p*A-q*T)/(A-T)
    derivative=((p*A1-q*T1)*(A-T)-(p*A-q*T)*(A1-T1))/(A-T)**2
    f=k-p*A/(1+A)-q*T/(1+T)
    df=derivative-p*A1/(1+A)**2-q*T1/(1+T)**2
    return f,df

def main():
    A,T=F(1,112),F(1,448)
    f,df=code(A,T,-15*A,-F(75,4)*T)
    assert 13<f<14 and 9<df<10
    checks=0
    for A in (F(1,112),F(8,931),F(1,100)):
        for rho in (F(31,8),F(4)):
            T=A/rho
            for c in (100,1000):
                k,kp=F(c+21,c+6),F(4*(c+21),4*c+9)
                for lo,hi in ((F(51,50),F(19,18)),(F(1),F(71,66))):
                    ratio=lambda x,a,t:(1+t*x)/(1+a*x)
                    width=lambda a,t:ratio(lo,a,t)/ratio(hi,a,t)-1
                    measured=width(k*A,kp*T)/width(A,T)
                    formula=(k*A-kp*T)/(A-T)*(1+A*lo)/(1+k*A*lo)*(1+T*hi)/(1+kp*T*hi)
                    assert measured == formula
                    checks+=1
    # A mixed-edge coarse match requires X^15 = 1/(112(15/f(1)-1)).
    X15=1/(112*(15/f-1))
    assert F(84,100)**15 < X15 < F(86,100)**15
    # h(X)<=1/(112 X^6),  h(1)=1/113. Allow both 3/4 mid-gap corrections.
    ratio_bound=F(113,112)*F(100,84)**6 * F(449,336)*F(4,3)
    assert ratio_bound < F(6,5)**12
    assert (F(6,5)/F(84,100))**9 < 3**4
    assert F(86,100)**15 < F(1,3)
    corner=F(55,4)
    assert corner!=f and corner!=15
    c15=1/(112*(15/corner-1))
    assert c15 == F(11,112)
    assert 2**4 < 4**4*c15 < 3**4
    assert corner-15-F(75,4)==-20 and 15-F(15,4)-F(15,11)-F(75,88)>0
    derivative=F(15,4)*15/9
    assert derivative==F(25,4)
    # The normalized width recovers the input level to second order.
    q=F(32,5)
    for b in [F(14),F(323)]:
        low,high=1/(1+b*q),1/(1+b)
        assert high/low==q+(1-q)*high
        width=(A-T)*(high-low)/((1+A*low)*(1+T*high))
        assert width>0
    return dict(limit_at_one=str(f),derivative_at_one=str(df),mixed_required_X_power_15=str(X15),
                corner_center_limit=str(corner),corner_physical_limit=-20,
                corner_required_X_power_15=str(c15),corner_derivative=str(derivative),
                mixed_ratio_upper="M<3, a(X)/a(1)>3, t(X)/t(1)>3",
                exact_two_stock_secants=checks)

if __name__=='__main__':
    print(json.dumps(main(),indent=2))
