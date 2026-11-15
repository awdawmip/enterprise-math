"""Reproducible rational-interval certificate for BRC S23 N=4 K=17, s in [9/11,5/6].
All sign assertions use exact Fraction and outward interval bounds; no floating arithmetic.
"""
from functools import lru_cache
from fractions import Fraction as Q
from math import isqrt

A, B = Q(11,21), Q(10,21)
SCALE, N = 10**34, 28
CERTS = []

def I(x): return x if isinstance(x,tuple) else (Q(x),Q(x))
def add(x,y): x,y=I(x),I(y);return (x[0]+y[0],x[1]+y[1])
def neg(x): x=I(x);return (-x[1],-x[0])
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    x,y=I(x),I(y)
    p=[a*b for a in x for b in y]
    return min(p),max(p)
def div(x,y):
    y=I(y)
    assert y[0]>0
    return mul(x,(1/y[1],1/y[0]))
def sqrt_i(x):
    x=Q(x)
    assert x>0
    k=isqrt(x.numerator*SCALE*SCALE//x.denominator)
    lo,hi=Q(k,SCALE),Q(k+1,SCALE)
    assert lo*lo<=x<hi*hi
    return lo,hi
def lnq(x):
    x=Q(x)
    assert x>0
    v=(x-1)/(x+1)
    assert abs(v)<Q(1,3),(x,v)
    term,tot=v,Q(0)
    for j in range(N):
        tot+=2*term/Q(2*j+1)
        term*=v*v
    err=2*abs(term)/(Q(2*N+1)*(1-v*v))
    return (tot-err,tot+err)
def lni(x):
    x=I(x)
    assert x[0]>0
    return lnq(x[0])[0],lnq(x[1])[1]
def quant(x):
    x=I(x)
    return (Q(x[0].numerator*SCALE//x[0].denominator,SCALE),
        Q(-((-x[1].numerator*SCALE)//x[1].denominator),SCALE))

@lru_cache(None)
def info(s):
    s=Q(s)
    u=mul(s,sqrt_i(A*B))
    ct=neg(lni(add(1-s,mul(2,u))))
    h=neg(lni(add(u,sqrt_i((1-A*s)*(1-B*s)))))
    H=lni(A/B)
    J=lni((1-B*s)/(1-A*s))
    rho=quant(div(J,add(H,J)))
    assert Q(0)<rho[0]<=rho[1]<Q(1)
    cb=add(mul(rho,lni(div(rho,A*s))),mul(sub(1,rho),lni(div(sub(1,rho),1-A*s))))
    return ct,h,cb

def positive(name,x):
    x=I(x)
    assert x[0]>0,(name,float(x[0]),float(x[1]))
    CERTS.append(name)
    print(name,'GT',str(x[0].numerator*10**12//x[0].denominator)+'/1000000000000')

def counts(s):
    s=Q(s)
    return [(m,17-2*m+(m*s).__floor__()) for m in range(18) if 17-2*m+(m*s).__floor__()>=0]

def hull(points):
    h=[]
    for x,y in points:
        while len(h)>1:
            (u,v),(w,z)=h[-2:]
            if (w-u)*(y-z)-(z-v)*(x-w)>=0:
                h.pop()
            else:break
        h.append((x,y))
    return h

def g_dec(l,r,m,n,parts=12):
    delta=Q(1,10000)
    for i in range(parts):
        x=l+(r-l)*Q(i,parts)
        y=l+(r-l)*Q(i+1,parts)
        _,_,cbx=info(x)
        _,_,cbprev=info(x-delta)
        cty,hy,_=info(y)
        ctnext,_,cbnext=info(y+delta)
        L=div(sub(cbx,cbprev),delta)
        U=div(sub(add(mul(m,ctnext),mul(n,cbnext)),add(mul(m,cty),mul(n,hy))),delta)
        positive(f'G_DEC_{i}',sub(mul(17,L),U))

def d_inc(l,r,parts=4):
    delta=Q(1,10000)
    for i in range(parts):
        x=l+(r-l)*Q(i,parts);y=l+(r-l)*Q(i+1,parts)
        ctx,_,cbx=info(x)
        cty,_,_=info(y)
        ctnext,_,_=info(y+delta)
        _,_,cbprev=info(x-delta)
        positive(f'D_VAL_{i}',sub(mul(17,cbx),mul(14,ctx)))
        L=div(sub(cbx,cbprev),delta)
        U=div(sub(ctnext,cty),delta)
        positive(f'D_SLOPE_{i}',sub(mul(17,L),mul(14,U)))

def main():
    l,r=Q(9,11),Q(5,6)
    breaks=sorted({Q(k,m) for m in range(1,18) for k in range(m+1) if l<=Q(k,m)<=r})
    assert breaks==[l,Q(14,17),r],breaks  # 14/17 irrelevant m=17
    for x,y in zip(breaks,breaks[1:]):
        for s in (x,(x+y)/2):
            assert hull(counts(s))==[(0,17),(11,4),(14,0)],(s,hull(counts(s)))
        print('HULL',x,y,[(0,17),(11,4),(14,0)])
    assert hull(counts(r))==[(0,17),(12,3),(14,0)]
    print('RIGHT_BOUNDARY_HULL',r,[(0,17),(12,3),(14,0)])
    g_dec(l,r,11,4)
    ct,h,cb=info(l)
    positive('LEFT_11T4B_BEATS_17B',sub(add(mul(11,ct),mul(4,h)),mul(17,cb)))
    ct,h,cb=info(Q(81839,100000))
    positive('CROSS_LEFT_81839_100000',sub(add(mul(11,ct),mul(4,h)),mul(17,cb)))
    ct,h,cb=info(Q(81841,100000))
    positive('CROSS_RIGHT_81841_100000',sub(mul(13,cb),mul(11,ct)))
    d_inc(l,r)
    ct,h,cb=info(r)
    positive('RIGHT_12T3B_BEATS_17B',sub(add(mul(12,ct),mul(3,h)),mul(17,cb)))
    positive('RIGHT_12T3B_BEATS_14T',sub(mul(3,h),mul(2,ct)))
    assert len(CERTS)==12+3+8+2,len(CERTS)
    print('STRICT_RATIONAL_ASSERTIONS',len(CERTS))
    print('PASS_BRC_S23_K17_PHASE_9_11_TO_5_6_20261105')
if __name__=='__main__':main()
