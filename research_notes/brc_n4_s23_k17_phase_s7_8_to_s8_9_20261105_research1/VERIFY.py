"""Exact rational certificate for auxiliary BRC S23 N=4, K=17, s in [7/8,8/9].

All computations in Fraction; outward intervals for sqrt/log.  For real s,
continuum conclusions use convexity of Chernoff information in s and
non-overlapping derivative/secant estimates on a finite rational partition.
"""
from functools import lru_cache
from fractions import Fraction as Q
from math import isqrt

A, B = Q(11,21), Q(10,21)
SCALE, TERMS = 10**35, 32
CERTS=[]

def I(x):return x if isinstance(x,tuple) else (Q(x),Q(x))
def add(x,y): x,y=I(x),I(y);return (x[0]+y[0],x[1]+y[1])
def neg(x):x=I(x);return (-x[1],-x[0])
def sub(x,y):return add(x,neg(y))
def mul(x,y):
    x,y=I(x),I(y)
    v=[p*q for p in x for q in y]
    return (min(v),max(v))
def div(x,y):
    y=I(y)
    assert y[0]>0,('DIV_NONPOSITIVE',y)
    return mul(x,(1/y[1],1/y[0]))
def sqrt_i(x):
    x=Q(x)
    assert x>0
    k=isqrt(x.numerator*SCALE*SCALE//x.denominator)
    lo,hi=Q(k,SCALE),Q(k+1,SCALE)
    assert lo*lo<=x<hi*hi
    return (lo,hi)
def lnq(x):
    x=Q(x)
    assert x>0
    v=(x-1)/(x+1)
    assert abs(v)<Q(1,3),('LN_RANGE',x,v)
    term,total=v,Q(0)
    for j in range(TERMS):
        total+=2*term/Q(2*j+1)
        term*=v*v
    err=2*abs(term)/(Q(2*TERMS+1)*(1-v*v))
    return (total-err,total+err)
def lni(x):
    x=I(x)
    assert x[0]>0
    return (lnq(x[0])[0],lnq(x[1])[1])
def quant(x):
    x=I(x)
    return (Q(x[0].numerator*SCALE//x[0].denominator,SCALE),
            Q(-((-x[1].numerator*SCALE)//x[1].denominator),SCALE))

@lru_cache(None)
def info(s):
    s=Q(s)
    rootab=sqrt_i(A*B)
    u=mul(s,rootab)
    ct=neg(lni(add(1-s,mul(2,u))))
    h=neg(lni(add(u,sqrt_i((1-A*s)*(1-B*s)))))
    L=lni(A/B)
    J=lni((1-B*s)/(1-A*s))
    rho=quant(div(J,add(L,J)))
    assert Q(0)<rho[0]<=rho[1]<Q(1)
    cb=add(mul(rho,lni(div(rho,A*s))),
           mul(sub(1,rho),lni(div(sub(1,rho),1-A*s))))
    return ct,h,cb

def positive(name,x):
    x=I(x)
    assert x[0]>0,(name,float(x[0]),float(x[1]))
    CERTS.append(name)
    # decimal threshold: positive lower bound truncated toward -infinity
    z=x[0].numerator*10**12//x[0].denominator
    print(name,'GT',str(z)+'/1000000000000')

def counts(s):
    s=Q(s)
    return [(m,17-2*m+(m*s).__floor__()) for m in range(18)
            if 17-2*m+(m*s).__floor__()>=0]

def hull(points):
    h=[]
    for x,y in points:
        while len(h)>1:
            (u,v),(w,z)=h[-2:]
            if (w-u)*(y-z)-(z-v)*(x-w)>=0: h.pop()
            else:break
        h.append((x,y))
    return h

def g_decrease(left,right,m,n,tag,parts=12):
    """G = F(m,n;s)-17 CB(s) decreases strictly over real interval.
    For F: sup-of-convex => convex in s, and F(y)>=m CT(y)+n H(y),
    F(y+delta)<=m CT(y+delta)+n CB(y+delta).
    For CB: convex, hence left finite secant lower-bounds CB' on [x,y].
    Convex secants bound right derivatives of F over [x,y].
    """
    delta=Q(1,10000)
    for i in range(parts):
        x=left+(right-left)*Q(i,parts)
        y=left+(right-left)*Q(i+1,parts)
        _,_,cbx=info(x)
        _,_,cbprev=info(x-delta)
        cty,hy,_=info(y)
        ctnext,_,cbnext=info(y+delta)
        lower_cb_prime=div(sub(cbx,cbprev),delta)
        upper_F_prime=div(sub(add(mul(m,ctnext),mul(n,cbnext)),
                             add(mul(m,cty),mul(n,hy))),delta)
        positive(tag+f'_STRICT_DEC_{i:02d}',sub(mul(17,lower_cb_prime),upper_F_prime))

def d_increase(left,right,parts=16):
    """D=17CB-15CT is strictly increasing: secant derivative enclosures."""
    delta=Q(1,10000)
    for i in range(parts):
        x=left+(right-left)*Q(i,parts)
        y=left+(right-left)*Q(i+1,parts)
        _,_,cbx=info(x)
        _,_,cbprev=info(x-delta)
        cty,_,_=info(y)
        ctnext,_,_=info(y+delta)
        dcb=div(sub(cbx,cbprev),delta)
        dct=div(sub(ctnext,cty),delta)
        positive(f'D_STRICT_INC_{i:02d}',sub(mul(17,dcb),mul(15,dct)))

def main():
    lo, hi = Q(7,8), Q(8,9)
    intermediate=Q(15,17)
    breaks=sorted({Q(k,m) for m in range(1,18) for k in range(m+1)
                   if lo<=Q(k,m)<=hi})
    assert breaks==[lo,intermediate,hi],breaks
    print('ALL_COST_BREAKPOINTS',','.join(map(str,breaks)))
    hull_interior=[(0,17),(8,8),(15,0)]
    for s in [lo,(lo+intermediate)/2,intermediate,
              (intermediate+hi)/2,(intermediate+hi*2)/3]:
        assert hull(counts(s))==hull_interior,(s,hull(counts(s)))
    print('INTERIOR_HULL',str(hull_interior))
    boundary=[(0,17),(9,7),(15,0)]
    assert hull(counts(hi))==boundary
    print('RIGHT_HULL',str(boundary))
    # The 15/17 floor breakpoint changes neither feasible pairs nor upper hull.
    assert counts(intermediate)==counts((lo+intermediate)/2)
    assert counts(intermediate)==counts((intermediate+hi)/2)
    print('15_17_SILENT_BREAKPOINT_VERIFIED')

    g_decrease(lo,hi,8,8,'G',parts=16)
    d_increase(lo,hi,parts=16)
    ct,h,cb=info(lo)
    positive('LEFT_8T8B_GT_17B',sub(add(mul(8,ct),mul(8,h)),mul(17,cb)))
    positive('LEFT_17B_GT_15T',sub(mul(17,cb),mul(15,ct)))
    alpha_lo,alpha_hi=Q(87516,100000),Q(87517,100000)
    ct,h,cb=info(alpha_lo)
    positive('ALPHA_LO_8T8B_GT_17B',sub(add(mul(8,ct),mul(8,h)),mul(17,cb)))
    ct,h,cb=info(alpha_hi)
    positive('ALPHA_HI_17B_GT_8T8B',sub(mul(9,cb),mul(8,ct)))
    ct,h,cb=info(hi)
    positive('RIGHT_9T7B_GT_17B',sub(add(mul(9,ct),mul(7,h)),mul(17,cb)))
    positive('RIGHT_9T7B_GT_15T',sub(mul(7,h),mul(6,ct)))
    assert len(CERTS)==16+16+6,len(CERTS)
    print('STRICT_RATIONAL_ASSERTIONS',len(CERTS))
    print('PASS_BRC_S23_K17_PHASE_S7_8_TO_S8_9_EXACT_20261105')

if __name__=='__main__':main()
