"""Exact scalar checks for quadratic/quartic first-deviation costs."""
from fractions import Fraction as F
import json
from pathlib import Path
from math import gcd


def multiply(outer,inner):
    a,b,c,d=outer
    e,f,g,h=inner
    out=(a*e+b*g,a*f+b*h,c*e+d*g,c*f+d*h)
    factor=gcd(*out)
    return tuple(x//factor for x in out)


def derivative(matrix,x):
    a,b,c,d=matrix
    return F(abs(a*d-b*c),(c*x+d)**2)


def run():
    hd=F(377,378)*F(99,100)
    assert hd*F(65,66)/1600>F(1,1700)
    assert hd*F(65*64,66**2)/25600>F(1,28000)
    assert F(100,80*16)>F(1,16)
    assert F(100*9,10*80*16)>F(1,16)
    assert F(17,8)**3/16<F(3,5)
    assert F(100,920)>F(1,40)
    assert F(100*64,80*16*(3*64+1))>F(1,40)
    assert F(63,(63+4)**2)>=F(1,80) and F(7,(7+4)**2)>=F(1,80)
    assert F(100)*F(2,5)*F(2,5)/256==F(1,16)
    f0=(0,112,3,115)
    f2=(0,56,-27,110)
    theta=F(56,65)
    lam=F(42,4225)
    constants={word:derivative(matrix,theta)/lam**2 for word,matrix in
               [('02',multiply(f2,f0)),('20',multiply(f0,f2))]}
    assert constants['02'] != constants['20']
    return dict(first_deviation_TV_lower='r^2/1700',aligned_lower='r^4/28000',
                valid_from=66,optimal_order_example_front='3380/1357',
                interior_two_gap_limit={k:str(v) for k,v in constants.items()},
                interior_limit_decimal={k:float(v) for k,v in constants.items()})

if __name__=='__main__':
    print(json.dumps(run(),indent=2))
