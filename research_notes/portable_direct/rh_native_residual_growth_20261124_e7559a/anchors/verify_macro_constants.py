#!/usr/bin/env python3
"""Exact finite checks for the Mellin seams and two macro-hat constants."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import argparse
import json


def add(a,b):
    return a[0]+b[0],a[1]+b[1]


def sub(a,b):
    return a[0]-b[1],a[1]-b[0]


def scale(a,c):
    return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])


def inverse(a):
    assert a[0]>0
    return 1/a[1],1/a[0]


def sqrt_interval(x,digits=90):
    S=10**digits
    k=isqrt(x.numerator*S*S//x.denominator)
    lo=F(k,S);hi=F(k+1,S)
    assert lo*lo<=x<hi*hi
    return lo,hi


def decimal_interval(a,digits=65):
    S=10**digits
    lo=a[0].numerator*S//a[0].denominator
    hi=-((-a[1].numerator*S)//a[1].denominator)
    def display(n):
        sign='-' if n<0 else ''
        n=abs(n)
        return f'{sign}{n//S}.{n%S:0{digits}d}'
    return {'lower':display(lo),'upper':display(hi),
            'integer_bounds':[str(lo),str(hi)],'denominator_power_of_10':digits}


def macro_constant(xi,r):
    sx=sqrt_interval(xi);sr=sqrt_interval(r);inv=inverse(sx)
    left=scale(sub(add(sx,inv),(F(2),F(2))),1/(xi-1))
    right=scale(sub(add(scale(inv,r),sx),scale(sr,2)),1/(r-xi))
    value=add(left,right)
    assert value[0]>0
    return value


def polynomial_add(*ps):
    result={}
    for p in ps:
        for key,value in p.items():result[key]=result.get(key,F(0))+value
    return {key:value for key,value in result.items() if value}


def polynomial_mul(p,q):
    result={}
    for (a,b),u in p.items():
        for (c,d),v in q.items():
            key=(a+c,b+d);result[key]=result.get(key,F(0))+u*v
    return {key:value for key,value in result.items() if value}


def polynomial_scale(p,c):
    return {key:c*value for key,value in p.items()}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('macro_constant_certificate.json'))
    args=parser.parse_args()
    kernels=0
    for n in range(1,65):
        for s in range(2,10):
            for multiplier in (3,5):
                T=n*multiplier
                finite=(F(n)**(1-s)-F(T)**(1-s))/(n*(s-1))-(F(n)**(-s)-F(T)**(-s))/s
                tail=F(T)**(1-s)/(n*(s-1))-F(T)**(-s)/s
                exact=F(n)**(-s)/(s*(s-1))
                assert finite+tail==exact
                kernels+=1
    one={(0,0):F(1)};g={(1,0):F(1)};t={(0,1):F(1)}
    one_g=polynomial_add(one,g);one_t=polynomial_add(one,t)
    # Numerator of B+(1/t-g)/(t(1+t))-(1+g)/(1+t).
    identity=polynomial_add(
        polynomial_mul(polynomial_mul(one_g,t),one_t),
        polynomial_scale(one_t,-1),one,
        polynomial_scale(polynomial_mul(g,t),-1),
        polynomial_scale(polynomial_mul(one_g,polynomial_mul(t,t)),-1))
    assert identity=={}
    rows=[]
    for name,xi in [('midpoint',F(3,2)),('seam',F(4,3))]:
        rows.append({'shape':name,'xi':str(xi),'r':'2','C':decimal_interval(macro_constant(xi,F(2)))})
    result={'schema':'EM_MACRO_PRIME_SQUARE_CONSTANT_V1','status':'PASS',
            'arithmetic':'Exact rational operations; square roots enclosed by integer square-root inequalities.',
            'mellin_single_source_checks':kernels,
            'mellin_kernel_domain':'n=1..64; integer s=2..9; split tail at T=3n and5n',
            's1_laurent_cancellation':'Exact bivariate polynomial identity in gamma and t=s−1',
            'macro_constants':rows,
            'scope':'Finite arithmetic checks and exact constants; unbounded Mellin/RH equivalence and prime-square limit use the analytical proof.'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))


if __name__=='__main__':main()
