"""Exact-rational Chernoff phase certificates for S23 N=4 K=17, 3/4 <= s <= 4/5.
Uses only Fraction/isqrt and outward rigorous rational enclosures.
"""
from functools import lru_cache
from fractions import Fraction as Q
from math import isqrt

A, B, N, SCALE = Q(11,21), Q(10,21), 34, 10**48
COUNT=0

def I(x): return x if isinstance(x,tuple) else (Q(x),Q(x))
def add(x,y):
    x,y=I(x),I(y);return (x[0]+y[0],x[1]+y[1])
def neg(x):
    x=I(x);return (-x[1],-x[0])
def sub(x,y):return add(x,neg(y))
def mul(x,y):
    x,y=I(x),I(y);p=[a*b for a in x for b in y];return (min(p),max(p))
def div(x,y):
    y=I(y);assert y[0]>0;return mul(x,(1/y[1],1/y[0]))
def sqrt_i(x):
    x=Q(x);assert x>0
    k=isqrt(x.numerator*SCALE*SCALE//x.denominator)
    lo,hi=Q(k,SCALE),Q(k+1,SCALE)
    assert lo*lo<=x<hi*hi
    return (lo,hi)
def lnq(x):
    x=Q(x);assert x>0
    v=(x-1)/(x+1);assert abs(v)<Q(1,3),(x,v)
    term=v;total=Q(0)
    for j in range(N):
        total += 2*term/Q(2*j+1)
        term *= v*v
    err=2*abs(term)/(Q(2*N+1)*(1-v*v))
    return (total-err,total+err)
def lni(x):
    x=I(x);assert x[0]>0
    return (lnq(x[0])[0],lnq(x[1])[1])
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
    cb=add(mul(rho,lni(div(rho,A*s))),
           mul(sub(1,rho),lni(div(sub(1,rho),1-A*s))))
    return (ct,h,cb)

def positive(label,x):
    global COUNT
    x=I(x)
    assert x[0]>0,(label,float(x[0]),float(x[1]))
    COUNT+=1
    print(label,'GT',f'{x[0]*10**13//1}/10000000000000')

def candidate_monotone(m,n,l,r,parts=12):
    delta=Q(1,10000)
    for i in range(parts):
        x=l+(r-l)*Q(i,parts)
        y=l+(r-l)*Q(i+1,parts)
        _,_,cbx=info(x)
        _,_,cbprev=info(x-delta)
        cty,hy,cby=info(y)
        ctnext,_,cbnext=info(y+delta)
        L=div(sub(cbx,cbprev),delta)
        U=div(sub(add(mul(m,ctnext),mul(n,cbnext)),add(mul(m,cty),mul(n,hy))),delta)
        positive(f'G_{m}_{n}_DEC_{i}',sub(mul(17,L),U))

def linear_increasing(bcoef,tcoef,l,r,parts=4):
    delta=Q(1,10000)
    for i in range(parts):
        x=l+(r-l)*Q(i,parts)
        y=l+(r-l)*Q(i+1,parts)
        ctx,_,cbx=info(x)
        cty,_,_=info(y)
        ctnext,_,_=info(y+delta)
        _,_,cbprev=info(x-delta)
        positive(f'L_{bcoef}_{tcoef}_LEFT_{i}',sub(mul(bcoef,cbx),mul(tcoef,ctx)))
        positive(f'L_{bcoef}_{tcoef}_SLOPE_{i}',sub(mul(bcoef,div(sub(cbx,cbprev),delta)),mul(tcoef,div(sub(ctnext,cty),delta))))

def winning_at_left(m,n,s):
    ct,h,cb=info(s)
    positive(f'WIN_{m}_{n}_AT_{s}',sub(add(mul(m,ct),mul(n,h)),mul(17,cb)))
def losing_at_right(m,n,s):
    ct,_,cb=info(s)
    positive(f'LOSE_{m}_{n}_AT_{s}',sub(mul(17-n,cb),mul(m,ct)))

BREAKS=[Q(3,4),Q(10,13),Q(7,9),Q(11,14),Q(4,5)]
HULLS=[[(0,17),(12,2),(13,0)],[(0,17),(13,1)],[(0,17),(9,6),(13,1)],[(0,17),(14,0)]]
CASES=[(12,2),(13,1),(9,6),(14,0)]

def pts(s):
    return [(m,17-2*m+(m*s).__floor__()) for m in range(17) if 17-2*m+(m*s).__floor__()>=0]
def hull(points):
    out=[]
    for x,y in points:
        while len(out)>1:
            (u,v),(w,z)=out[-2:]
            if (w-u)*(y-z)-(z-v)*(x-w)>=0:out.pop()
            else:break
        out.append((x,y))
    return out

def main():
    actual_breaks=sorted({Q(k,m) for m in range(1,17) for k in range(m+1) if Q(3,4)<=Q(k,m)<=Q(4,5)})
    assert actual_breaks==BREAKS,(actual_breaks,BREAKS)
    for (l,r),expected in zip(zip(BREAKS,BREAKS[1:]),HULLS):
        actual=hull(pts((l+r)/2))
        assert actual==expected,(l,r,actual)
        assert hull(pts(l))==expected
        print('HULL',l,r,actual)
    assert hull(pts(Q(4,5)))==[(0,17),(10,5),(14,0)]
    print('BOUNDARY HULL 4/5',hull(pts(Q(4,5))))
    for (l,r),(m,n) in zip(zip(BREAKS,BREAKS[1:]),CASES):
        candidate_monotone(m,n,l,r)
        winning_at_left(m,n,l)
        losing_at_right(m,n,l+Q(1,1000))
    linear_increasing(17,13,Q(3,4),Q(10,13))
    linear_increasing(16,13,Q(7,9),Q(11,14))
    ct,h,cb=info(Q(4,5))
    positive('S_4_5_10T5B_BEATS_17B',sub(add(mul(10,ct),mul(5,h)),mul(17,cb)))
    positive('S_4_5_10T5B_BEATS_14T',sub(add(mul(10,ct),mul(5,h)),mul(14,ct)))
    assert COUNT==4*12+4*2+2*4*2+2,COUNT
    print('ASSERTIONS',COUNT)
    print('PASS_BRC_S23_K17_PHASE_THREE_QUARTERS_TO_FOUR_FIFTHS_EXACT_20261105')

if __name__=='__main__':main()
