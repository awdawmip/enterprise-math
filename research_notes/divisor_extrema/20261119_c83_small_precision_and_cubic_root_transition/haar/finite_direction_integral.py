"""Exact inner integral in the C83 finite-direction formula (a > 1/4).

The Fraction path is exact. Optional outer quadrature is exploratory only.
"""
from fractions import Fraction as F
from math import pi
import argparse


def product_linear(factors):
    poly=[1]
    for constant,slope in factors:
        out=[0]*(len(poly)+1)
        for k,value in enumerate(poly):
            out[k]+=constant*value
            out[k+1]+=slope*value
        poly=out
    return poly


def inner_integral(a,x,y):
    """Return integral_-1^1 (W2-W3) ds; exact for Fraction inputs."""
    zero=a*0
    one=zero+1
    p=(x,y,2*y-x)
    if any(abs(z)>=1 for z in p):
        return a*0
    lines=((zero,one),(a/x,y/x),(2*a/x,2*y/x-one))
    cuts={-one,one}
    for z,(intercept,slope) in zip(p,lines):
        if slope==0:
            continue
        levels=(0,z,-1+max(0,z),1+min(0,z),
                1-abs(z),-1+abs(z))
        for level in levels:
            q=(level-intercept)/slope
            if -1<q<1:
                cuts.add(q)
    cuts=sorted(cuts)
    value=a*0
    for lo,hi in zip(cuts,cuts[1:]):
        middle=(lo+hi)/2
        factors2=[]
        factors3=[]
        for z,(intercept,slope) in zip(p,lines):
            q=intercept+slope*middle
            options=[(zero,zero),(z,zero),(intercept,slope)]
            upper=max(options,key=lambda k:k[0]+k[1]*middle)
            lower=min(options,key=lambda k:k[0]+k[1]*middle)
            factor=(1-upper[0]+lower[0],-upper[1]+lower[1])
            factors2.append(factor if factor[0]+factor[1]*middle>0 else (zero,zero))
            sign=(q>0)-(q<0)
            factor=(1-abs(z)-sign*intercept,-sign*slope)
            factors3.append(factor if factor[0]+factor[1]*middle>0 else (zero,zero))
        p2=product_linear(factors2)
        p3=product_linear(factors3)
        value+=sum((v-w)*(hi**(k+1)-lo**(k+1))/(k+1)
                   for k,(v,w) in enumerate(zip(p2,p3)))
    return value


def quadrature_old(a,n):
    import numpy as np
    z,w=np.polynomial.legendre.leggauss(n)
    z=(z+1)/2
    w=w/2
    total=0.
    for x,wx in zip(z,w):
        for q,wq in zip(z,w):
            y=(x-1)/2+q
            total+=wx*wq*inner_integral(a,float(x),float(y))/x
    correction=12*total/(pi*pi*a)
    return 1-161/(80*pi*pi*a)+correction,correction


def quadrature(a,n):
    """Nonsingular rectangle: r in [a,1], q in [-1,1]."""
    import numpy as np
    z,w=np.polynomial.legendre.leggauss(n)
    unit=(z+1)/2
    weights=w/2
    total=0.
    for u,wu in zip(unit,weights):
        r=a+(1-a)*u
        for q,wq in zip(z,w):
            total+=wu*wq*inner_integral(a,float(r),float(r*(1+q)/2))
    correction=12*(1-a)*total/(pi*pi*a)
    return 1-161/(80*pi*pi*a)+correction,correction


def checks():
    for a in [F(1,2),F(3,4),F(1)]:
        for x in [F(1,5),F(1,2),F(9,10)]:
            for q in [F(1,4),F(1,2),F(3,4)]:
                y=(x-1)/2+q
                value=inner_integral(a,x,y)
                assert isinstance(value,F)
                assert value==0
    for a in [F(3,10),F(1,3),F(2,5),F(49,100)]:
        for x in [F(1,5),F(1,2),F(9,10)]:
            for q in [F(1,4),F(1,2),F(3,4)]:
                y=(x-1)/2+q
                assert inner_integral(a,x,y)>=0
    assert inner_integral(F(3,10),F(9,10),F(9,20))>0
    print('Exact inner-integral checks passed.')


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--quadrature',type=int)
    args=parser.parse_args()
    checks()
    if args.quadrature:
        print('EXPLORATORY outer quadrature; not an error-certified enclosure.')
        for a in [0.26,0.3,1/3,0.4,0.49,0.5]:
            value,correction=quadrature(a,args.quadrature)
            print(a,value,correction)
