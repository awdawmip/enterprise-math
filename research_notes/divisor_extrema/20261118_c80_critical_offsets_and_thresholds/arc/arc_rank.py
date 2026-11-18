"""Certify Hilbert function ranks of the C76 first-gap/middle-gap real arc."""
import argparse
from fractions import Fraction as Q
import json
import math
import sys
sys.set_int_max_str_digits(0)
import mpmath as mp
from rational_interval_high import box, Interval, BITS
from stream_jets import solve_series

def center(x,y):
    return x**9/((1+112*x**15)*y**12)

def signed(x,y):
    a=4*x.sqrt().sqrt()**15
    d=4*(y/x).sqrt().sqrt()**9
    b=Q(7,16)*a**5
    ell=Q(7,16)*d**5
    return b*ell*(1-a)*(1-d)/(y.sqrt().sqrt()**3*(1+b*d)*(a+b*d))

def approximate_roots(digits):
    # The next routine treats candidates as rationals and verifies them.
    mp.mp.dps=digits+45
    m=mp.mpf(1)/5
    def physical(x,y):
        A=4*x**(mp.mpf(15)/4)
        d=4*(y/x)**(mp.mpf(9)/4)
        b=7*A**5/16
        return b*7*d**5*(1-A)*(1-d)/(16*y**(mp.mpf(3)/4)*(1+b*d)*(A+b*d))
    def equations(y,u):
        return center(1-m,y)-center(u,u-m), physical(1-m,y)-physical(u,u-m)
    y,u=mp.findroot(equations, (mp.mpf('.3876786387'),mp.mpf('.5208154217')),tol=mp.mpf(10)**(-digits-25))
    return Q(mp.nstr(y,digits+15)),Q(mp.nstr(u,digits+15))

def base_box(digits):
    m=Q(1,5)
    y0,u0=approximate_roots(digits)
    rad=Q(1,10**digits)
    # For fixed m, center(u,u-m) is strictly decreasing:
    # its log derivative is 9/u-12/(u-m)-1680*u**14/(1+112*u**15)<0.
    # The implicit u solving the center equation increases with y.
    # At both y endpoints verify a narrow u bracket about the first-order
    # estimate; only the signs at the bracket endpoints certify it.
    for s in (-1,1):
        y=y0+s*rad
        target=center(1-m,y)
        def centered(u):
            return center(u,u-m)-target
        loc=u0-centered(u0)/(center(u0,u0-m)*(9/u0-12/(u0-m)-1680*u0**14/(1+112*u0**15)))
        grid=10**(digits+12)
        loc=Q((loc.numerator*grid)//loc.denominator,grid)
        eps=rad/10**6
        low,high=loc-eps,loc+eps
        assert u0-3*rad<low<high<u0+3*rad
        assert centered(low)>0>centered(high)
        U=Interval(low,high)
        err=signed(box(1-m),box(y))-signed(U,U-m)
        assert err.a>0 if s>0 else err.b<0
    return box(m),Interval(y0-rad,y0+rad),Interval(u0-3*rad,u0+3*rad)

def determinant(matrix):
    arr = [row.copy() for row in matrix]
    result=box(1)
    for k in range(len(arr)):
        j=max(range(k,len(arr)),key=lambda i:abs(arr[i][k].a+arr[i][k].b))
        if k!=j:
            arr[k],arr[j]=arr[j],arr[k]
            result=-result
        pivot=arr[k][k]
        if pivot.a*pivot.b<=0:
            raise ArithmeticError(f'pivot {k} after {len(arr)} rows')
        result=result*pivot
        for i in range(k+1,len(arr)):
            factor=arr[i][k]/pivot
            for t in range(k+1,len(arr)):
                arr[i][t]=arr[i][t]-factor*arr[k][t]
    return result

def run(deg,digits):
    h=math.comb(deg+3,3)
    M,Y,U=solve_series(*base_box(digits),h-1)
    # Set constant coefficients to exact zero. For each unknown true center
    # subtract its true value; this effects a unitriangular column operation.
    for f in (M,Y,U):
        f[0]=box(0)
    # M(t) = t exactly, so M^i is a coefficient shift. Reuse products
    # Y^j U^k when different powers of M multiply the same product.
    zero=box(0)
    pair={(0,0):[box(1)]+[zero]*(h-1)}
    for d in range(1,deg+1):
        for j in range(d+1):
            k=d-j
            previous,extra=(pair[j-1,k],Y) if j else (pair[0,k-1],U)
            # The previous factor has order at least d-1; the new factor
            # has order at least 1. Omitted terms are exactly zero.
            pair[j,k]=[zero]*d+[sum((previous[a]*extra[t-a] for a in range(d-1,t)),zero)
                                 for t in range(d,h)]
    exps=[(i,j,d-i-j) for d in range(deg+1) for i in range(d,-1,-1) for j in range(d-i,-1,-1)]
    matrix=[[pair[j,k][t-i] if t>=i else box(0) for i,j,k in exps] for t in range(h)]
    det=determinant(matrix)
    assert det.a*det.b>0
    lower,upper=det.lo,det.hi
    # Outward decimal scientific bounds obtained solely by integer comparisons.
    n=len(str(abs(lower.numerator)))-len(str(lower.denominator))-4
    scale=Q(10)**n
    left,right=lower/scale,upper/scale
    lo=left.numerator//left.denominator
    hi=-(-right.numerator//right.denominator)
    assert lo*hi>0
    return dict(study='C76 first/middle alias arc',m='1/5',degree=deg,columns=h,
                jet_order=h-1,root_box_radius=f'1e-{digits}',binary_precision=BITS,
                determinant_lower=f'{lo}e{n}',determinant_upper=f'{hi}e{n}',
                projective_degree_lower_bound=(h-1+deg-1)//deg)
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('degree',type=int)
    parser.add_argument('digits',type=int)
    args=parser.parse_args()
    print(json.dumps(run(args.degree,args.digits),indent=2))
