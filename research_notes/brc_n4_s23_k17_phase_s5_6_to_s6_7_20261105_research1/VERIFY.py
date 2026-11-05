"""Exact rational-interval certificate for BRC S23 N=4, K=17, s∈[5/6,6/7].
Requires only CPython stdlib. All real-domain conclusions rely on convex
secant inequalities and exact interval signs, not on floating sampling.
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
    v=[a*b for a in x for b in y]
    return min(v),max(v)
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
    V=lni(A/B)
    J=lni((1-B*s)/(1-A*s))
    rho=quant(div(J,add(V,J)))
    assert Q(0)<rho[0]<=rho[1]<Q(1)
    cb=add(mul(rho,lni(div(rho,A*s))),
           mul(sub(1,rho),lni(div(sub(1,rho),1-A*s))))
    return ct,h,cb

def positive(name,x):
    x=I(x)
    assert x[0]>0,(name,float(x[0]),float(x[1]))
    CERTS.append(name)
    print(name,'GT',str(x[0].numerator*10**12//x[0].denominator)+'/1000000000000')

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

def g_decrease(l,r,m,n,tag,parts=12):
    delta=Q(1,10000)
    for i in range(parts):
        x=l+(r-l)*Q(i,parts)
        y=l+(r-l)*Q(i+1,parts)
        _,_,cbx=info(x)
        _,_,cbprev=info(x-delta)
        cty,hy,_=info(y)
        ctnext,_,cbnext=info(y+delta)
        L=div(sub(cbx,cbprev),delta)
        U=div(sub(add(mul(m,ctnext),mul(n,cbnext)),
                  add(mul(m,cty),mul(n,hy))),delta)
        positive(f'{tag}_DEC_{i}',sub(mul(17,L),U))

def d_increase(l,r,parts=4):
    delta=Q(1,10000)
    for i in range(parts):
        x=l+(r-l)*Q(i,parts)
        y=l+(r-l)*Q(i+1,parts)
        ctx,_,cbx=info(x)
        cty,_,_=info(y)
        ctnext,_,_=info(y+delta)
        _,_,cbprev=info(x-delta)
        positive(f'D_VALUE_{i}',sub(mul(17,cbx),mul(14,ctx)))
        L=div(sub(cbx,cbprev),delta)
        U=div(sub(ctnext,cty),delta)
        positive(f'D_SLOPE_{i}',sub(mul(17,L),mul(14,U)))

def main():
    l,h,r=Q(5,6),Q(11,13),Q(6,7)
    breaks=sorted({Q(k,m) for m in range(1,18) for k in range(m+1) if l<=Q(k,m)<=r})
    assert breaks==[l,h,r],breaks
    for x,y,p in [(l,h,[(0,17),(12,3),(14,0)]),(h,r,[(0,17),(13,2),(14,0)])]:
        for s in (x,(x+y)/2):
            assert hull(counts(s))==p,(s,hull(counts(s)))
        print('CELL_HULL',x,y,p)
    assert hull(counts(r))==[(0,17),(14,1)]
    print('RIGHT_HULL',r,[(0,17),(14,1)])
    g_decrease(l,h,12,3,'A')
    g_decrease(h,r,13,2,'B')
    for label,s,m,n in [('START_A',l,12,3),
                        ('A_LO',Q(83353,100000),12,3),
                        ('START_B',h,13,2),
                        ('B_LO',Q(84634,100000),13,2)]:
        ct,hh,cb=info(s)
        positive(label,sub(add(mul(m,ct),mul(n,hh)),mul(17,cb)))
    for label,s,m,n in [('A_HI',Q(83355,100000),12,3),
                        ('B_HI',Q(84636,100000),13,2)]:
        ct,_,cb=info(s)
        positive(label,sub(mul(17-n,cb),mul(m,ct)))
    d_increase(l,r)
    ct,hh,cb=info(r)
    positive('RIGHT_14T1B_BEATS_17B',sub(add(mul(14,ct),hh),mul(17,cb)))
    positive('RIGHT_14T1B_BEATS_14T',hh)
    assert len(CERTS)==24+6+8+2,len(CERTS)
    print('STRICT_RATIONAL_ASSERTIONS',len(CERTS))
    print('PASS_BRC_S23_K17_PHASE_5_6_TO_6_7_EXACT_20261105')
if __name__=='__main__':main()
