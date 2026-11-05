"""Fully rational outward-interval continuum certificate for S23 K=17, s in [11/12,12/13].
Auxiliary source/projection model only. Requires Python 3 standard library.
"""
from fractions import Fraction as Q
from math import isqrt, gcd
from functools import lru_cache
A, B = Q(11,21), Q(10,21)
SCALE, TERMS = 10**36, 34
CERTS=[]

def I(x): return x if isinstance(x,tuple) else (Q(x),Q(x))
def add(x,y):
 x,y=I(x),I(y); return x[0]+y[0],x[1]+y[1]
def neg(x):
 x=I(x); return -x[1],-x[0]
def sub(x,y): return add(x,neg(y))
def mul(x,y):
 x,y=I(x),I(y);v=[p*q for p in x for q in y];return min(v),max(v)
def div(x,y):
 y=I(y);assert y[0]>0;return mul(x,(1/y[1],1/y[0]))
def sqrt_i(x):
 x=Q(x);assert x>0
 k=isqrt(x.numerator*SCALE*SCALE//x.denominator)
 z=Q(k,SCALE),Q(k+1,SCALE)
 assert z[0]**2<=x<z[1]**2
 return z
def lnq(x):
 x=Q(x);assert x>0
 v=(x-1)/(x+1);assert abs(v)<Q(1,3),('LN_RANGE',str(x))
 power=v;out=Q(0)
 for j in range(TERMS):
  out+=2*power/Q(2*j+1);power*=v*v
 err=2*abs(power)/(Q(2*TERMS+1)*(1-v*v))
 return out-err,out+err
def lni(x):
 x=I(x);assert x[0]>0;return lnq(x[0])[0],lnq(x[1])[1]
def quant(x):
 x=I(x)
 return Q(x[0].numerator*SCALE//x[0].denominator,SCALE),Q(-((-x[1].numerator*SCALE)//x[1].denominator),SCALE)
@lru_cache(None)
def info(s):
 s=Q(s)
 u=mul(s,sqrt_i(A*B))
 ct=neg(lni(add(1-s,mul(2,u))))
 h=neg(lni(add(u,sqrt_i((1-A*s)*(1-B*s)))))
 L=lni(A/B);J=lni((1-B*s)/(1-A*s))
 rho=quant(div(J,add(L,J)))
 assert 0<rho[0]<=rho[1]<1
 cb=add(mul(rho,lni(div(rho,A*s))),mul(sub(1,rho),lni(div(sub(1,rho),1-A*s))))
 return ct,h,cb

def positive(tag,x):
 x=I(x);assert x[0]>0,(tag,float(x[0]),float(x[1]))
 CERTS.append(tag)
 print(tag,'STRICT_POSITIVE_LOWER_BOUND_1e12',x[0].numerator*10**12//x[0].denominator)
def counts(s):
 s=Q(s); return [(m,17-2*m+(m*s).__floor__()) for m in range(18) if 17-2*m+(m*s).__floor__()>=0]
def hull(points):
 h=[]
 for x,y in points:
  while len(h)>1:
   (u,v),(w,z)=h[-2:]
   if (w-u)*(y-z)-(z-v)*(x-w)>=0:h.pop()
   else:break
  h.append((x,y))
 return h

def derivative_bounds(lo,hi,m,n,parts=16):
 delta=Q(1,10000)
 for i in range(parts):
  x=lo+(hi-lo)*Q(i,parts); y=lo+(hi-lo)*Q(i+1,parts)
  _,_,cbx=info(x);_,_,cbprev=info(x-delta)
  cty,hy,_=info(y);ctnext,_,cbnext=info(y+delta)
  cbprime=div(sub(cbx,cbprev),delta)
  fprime=div(sub(add(mul(m,ctnext),mul(n,cbnext)),add(mul(m,cty),mul(n,hy))),delta)
  positive(f'G_STRICT_DEC_{i:02d}',sub(mul(17,cbprime),fprime))
  ctprime=div(sub(ctnext,cty),delta)
  positive(f'D_STRICT_INC_{i:02d}',sub(mul(17,cbprime),mul(15,ctprime)))

def main():
 lo,hi=Q(11,12),Q(12,13)
 breaks=sorted({Q(k,m) for m in range(1,18) for k in range(m+1) if lo<=Q(k,m)<=hi})
 assert breaks==[lo,hi],breaks
 for s in [lo,(2*lo+hi)/3,(lo+hi)/2,(lo+2*hi)/3,(lo+hi*999)/1000]:
  assert hull(counts(s))==[(0,17),(12,4),(15,0)],(s,hull(counts(s)))
 assert hull(counts(hi))==[(0,17),(13,3),(15,0)]
 for points in [[(0,17),(12,4),(15,0)],[(0,17),(13,3),(15,0)]]:
  for (m,n),(p,q) in zip(points,points[1:]):assert gcd(p-m,abs(q-n))==1
 print('COST_BREAKPOINTS',breaks)
 print('OPEN_HULL',[(0,17),(12,4),(15,0)],'RIGHT_HULL',[(0,17),(13,3),(15,0)])
 derivative_bounds(lo,hi,12,4,parts=16)
 ct,h,cb=info(lo)
 positive('LEFT_12T4B_GT_17B',sub(add(mul(12,ct),mul(4,h)),mul(17,cb)))
 positive('LEFT_17B_GT_15T',sub(mul(17,cb),mul(15,ct)))
 for tag,s,side in [('ALPHA_LOW',Q(91678,100000),'lo'),('ALPHA_HIGH',Q(91679,100000),'hi')]:
  ct,h,cb=info(s)
  positive(tag+'_SIGN',sub(add(mul(12,ct),mul(4,h)),mul(17,cb)) if side=='lo' else sub(mul(17,cb),add(mul(12,ct),mul(4,cb))))
 ct,h,cb=info(hi)
 positive('RIGHT_13T3B_GT_17B',sub(add(mul(13,ct),mul(3,h)),mul(17,cb)))
 positive('RIGHT_13T3B_GT_15T',sub(mul(3,h),mul(2,ct)))
 assert len(CERTS)==38,len(CERTS)
 print('STRICT_RATIONAL_ASSERTIONS',len(CERTS))
 print('PASS_K17_S23_PHASE_11_12_TO_12_13_EXACT_20261105')
if __name__=='__main__':main()
