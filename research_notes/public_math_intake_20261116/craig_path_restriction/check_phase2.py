"""Integer interval certificate for the exact level-2 extremal phase diameter.

All interval endpoints below are integers representing multiples of 2^-384.
Only exact integer arithmetic and integer square roots are used.
"""
from fractions import Fraction
from functools import lru_cache
from math import isqrt

S = 1 << 384
ONE = (S, S)
ZERO = (0, 0)


def up(x, y):
    return -((-x) // y)


def add(x,y):
    return (x[0]+y[0],x[1]+y[1])


def sub(x,y):
    return (x[0]-y[1],x[1]-y[0])


def scale(x,a):
    assert a>=0
    return (x[0]*a,x[1]*a)


def div(x,a):
    assert a>0
    return (x[0]//a,up(x[1],a))


def ratio(x,y):
    assert x[0]>=0 and y[0]>0
    return (x[0]*S//y[1], up(x[1]*S,y[0]))


def mul(x,y):
    p=[a*b for a in x for b in y]
    return (min(p)//S,up(max(p),S))


def sqrt_interval(x):
    assert x[0]>=0
    lo=isqrt(x[0]*S)
    hisq=x[1]*S
    hi=isqrt(hisq)
    return lo, hi + (hi*hi != hisq)


@lru_cache(maxsize=None)
def root(order_bits):
    """Positive unit root of order 2**order_bits by algebraic halving."""
    assert order_bits>=2
    real=ZERO
    for _ in range(2,order_bits):
        real=sqrt_interval(div(add(ONE,real),2))
    imag=sqrt_interval(sub(ONE,mul(real,real)))
    return (real,imag)


def cmul(z,w):
    a,b=z
    c,d=w
    return sub(mul(a,c),mul(b,d)),add(mul(a,d),mul(b,c))


def cpow(z,n):
    acc=(ONE,ZERO)
    while n:
        if n & 1:
            acc=cmul(acc,z)
        n//=2
        if n:
            z=cmul(z,z)
    return acc


B=48
den=1<<B
r0=139642759441871
bden=1<<80
# alpha=Im lim L(r_L-1). The finite multiple comparison gives 1/(2L).
bound=S//(2*bden)
alphaL=scale(root(83)[1],bden)
alpha=(alphaL[0]-bound,alphaL[1]+bound)
h1=root(3)[1]


def evaluate(j):
    r=div(scale(ONE,j),den)
    c,h=cpow(root(B+3),j)
    deriv=mul(c,alpha)
    F=sub(mul(add(ONE,r),deriv),add(h,h1))
    D=scale(ratio(sub(h,mul(r,h1)),add(ONE,r)),2)
    return F,D


def main():
    Fl,Dl=evaluate(r0)
    Fr,Dr=evaluate(r0+1)
    assert Fl[0]>0 and Fr[1]<0
    # D'(r)=2F(r)/(1+r)^2; F decreases; integrate on this tiny bracket.
    error=up(2*Fl[1],den)
    lower=max(Dl[0],Dr[0])
    upper=Dl[1]+error
    assert lower<=upper
    fscale=10**22
    rounded_low=(lower*fscale)//S
    rounded_high=up(upper*fscale,S)
    assert rounded_high - rounded_low <= 2
    print('r* in',r0,'..',r0+1,'over',den)
    print('sign certificate:',Fl[0]>0,Fr[1]<0)
    print('D_2 in',rounded_low,'..',rounded_high,'over',fscale)
    print('gap less than',Fraction(rounded_high-rounded_low,fscale))


if __name__=='__main__':
    main()
