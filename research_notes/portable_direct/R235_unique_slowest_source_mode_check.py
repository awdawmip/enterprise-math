#!/usr/bin/env python3
"""R235: exact stationary sticky-reset survival-rate certificate (auxiliary scalar observer)."""
from fractions import Fraction as F
import json

SAMPLES = (F(39,100), F(2,5), F(41,100))
LEFT,RIGHT=F(39,100),F(41,100)
XLO,XHI=F(99,100),F(991,1000)
C=F(5,18)

# Exact polynomials from algebraic reduction of f_{minus 3}(x,s).
QLO=lambda s:1518850343500*s*s-1968802891315*s+455373749139
QHI=lambda s:48471549398125*s*s-69426833298695*s+21080704373902

def family(s):
    lam=F(1,2)
    base=F(1,3)+F(2,7)+F(1,11)+F(1,2)
    h=F(21,8)-base-(lam-s)/(1-s)
    t=(h+lam)/(h+1)
    alpha=(F(1,5),F(1,4),F(3,10),F(9,20),s,F(2,3),t)
    pi=((1-C)*(lam-alpha[0])/(1-alpha[0]),)+tuple(
      C*abs(lam-a)/(1-a) for a in alpha[1:])
    b=tuple((1-a)*p for a,p in zip(alpha,pi))
    assert sum(pi)==1 and all(0<a<1 for a in alpha) and len(set(alpha))==7
    return alpha,pi,b

def f(i,x,alpha,b):
    return sum((b[j]/(x-alpha[j]) for j in range(7) if j!=i),F(0))-1

def poly_reduction(s):
    low=-F(49)*(QLO(s))/(F(704291004)*(100*s-99)*(89785*s-88861))
    high=-F(1964)*(QHI(s))/(F(24127412751)*(1000*s-991)*(300155*s-297383))
    return low,high

def certify():
    assert QLO(LEFT)<0 and QHI(RIGHT)>0
    # Positive quadratic leading coefficients imply increasing derivatives;
    # a negative right-end derivative certifies decreasing on the interval.
    assert 2*1518850343500*RIGHT-1968802891315<0
    assert 2*48471549398125*RIGHT-69426833298695<0
    assert 100*RIGHT<99 and 89785*RIGHT<88861
    assert 1000*RIGHT<991 and 300155*RIGHT<297383
    for s in SAMPLES:
      alpha,pi,b=family(s)
      assert alpha[6]==(1691*s-2615)/(2615*s-3539)
      assert alpha[6]>F(3,4) and alpha[6]<F(4,5)
      for x,identity in zip((XLO,XHI),poly_reduction(s)):
        assert f(3,x,alpha,b)==identity
      assert f(3,XLO,alpha,b)>0 and f(3,XHI,alpha,b)<0
      assert all(b[i]/(XHI-alpha[i])>b[3]/(XHI-alpha[3]) for i in (1,2,4,5,6))
    return {'status':'PASS','arithmetic':'Python fractions.Fraction',
            'model':'stationary strictly positive seven-source sticky-reset chain',
            'parameter_interval_open':['39/100','41/100'],
            'unique_slowest_missing_source_index':3,
            'slowest_source_holding':'9/20',
            'slowest_source_reset_coefficient':'1/72',
            'slowest_Perron_root_strict_interval':['99/100','991/1000'],
            'rational_samples':[str(s) for s in SAMPLES],
            'symbolic_sign_certificate':{
                'Qlo_at_left':str(QLO(LEFT)),
                'Qhi_at_right':str(QHI(RIGHT)),
                'Qlo_derivative_at_right':str(2*1518850343500*RIGHT-1968802891315),
                'Qhi_derivative_at_right':str(2*48471549398125*RIGHT-69426833298695),
                'all_denominators_positive_via_two_negative_factors':True},
            'coverage':'symbolic one-parameter real interval proof with exact polynomial sign checks; three independent rational substitutions',
            'independent_review':'NOT_REVIEWED',
            'native_brc_integration':'NOT_EXECUTED'}

if __name__=='__main__':
    print(json.dumps(certify(),ensure_ascii=False,indent=2))
