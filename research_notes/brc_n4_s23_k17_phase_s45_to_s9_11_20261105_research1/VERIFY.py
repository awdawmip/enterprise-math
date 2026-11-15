"""Exact rational interval certificate: BRC auxiliary S23, N4, K17, 4/5 <= s <= 9/11.
No floating-point calls in any assertion.
"""
from functools import lru_cache
from fractions import Fraction as Q
from math import isqrt

A,B=Q(11,21),Q(10,21)
SCALE=10**33; N=27
COUNT=0

def I(x): return x if isinstance(x, tuple) else (Q(x),Q(x))
def add(x,y):
 x,y=I(x),I(y);return (x[0]+y[0],x[1]+y[1])
def neg(x):
 x=I(x);return (-x[1],-x[0])
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 x,y=I(x),I(y);p=[v*w for v in x for w in y];return (min(p),max(p))
def div(x,y):
 y=I(y);assert y[0]>0;return mul(x,(1/y[1],1/y[0]))
def sqrt_i(x):
 x=Q(x);assert x>0;k=isqrt(x.numerator*SCALE*SCALE//x.denominator)
 lo,hi=Q(k,SCALE),Q(k+1,SCALE);assert lo**2<=x<hi**2;return lo,hi
def lnq(x):
 x=Q(x);assert x>0
 v=(x-1)/(x+1);assert abs(v)<Q(1,3),(x,v)
 term=v;tot=Q(0)
 for j in range(N):
  tot+=2*term/Q(2*j+1);term*=v*v
 err=2*abs(term)/(Q(2*N+1)*(1-v*v))
 return tot-err,tot+err
def lni(x):
 x=I(x);assert x[0]>0;return lnq(x[0])[0],lnq(x[1])[1]
def quant(x):
 x=I(x);return (Q(x[0].numerator*SCALE//x[0].denominator,SCALE),Q(-((-x[1].numerator*SCALE)//x[1].denominator),SCALE))
@lru_cache(None)
def info(s):
 s=Q(s)
 u=mul(s,sqrt_i(A*B))
 ct=neg(lni(add(1-s,mul(2,u))))
 h=neg(lni(add(u,sqrt_i((1-A*s)*(1-B*s)))))
 H=lni(A/B);J=lni((1-B*s)/(1-A*s))
 rho=quant(div(J,add(H,J)))
 assert Q(0)<rho[0]<=rho[1]<Q(1)
 cb=add(mul(rho,lni(div(rho,A*s))),mul(sub(1,rho),lni(div(sub(1,rho),1-A*s))))
 return ct,h,cb

def positive(label,x):
 global COUNT
 x=I(x); assert x[0]>0,(label,float(x[0]),float(x[1]))
 COUNT+=1
 print(label,'GT',f'{(x[0]*10**11)//1}/100000000000')
def counts(s):return [(m,17-2*m+(m*s).__floor__()) for m in range(17) if 17-2*m+(m*s).__floor__()>=0]
def hull(points):
 out=[]
 for x,y in points:
  while len(out)>1:
   (u,v),(w,z)=out[-2:]
   if (w-u)*(y-z)-(z-v)*(x-w)>=0:out.pop()
   else:break
  out.append((x,y))
 return out

def dec_G(l,r,m,n,parts=12):
 delta=Q(1,10000)
 for i in range(parts):
  x=l+(r-l)*Q(i,parts);y=l+(r-l)*Q(i+1,parts)
  _,_,cbx=info(x);_,_,cbprev=info(x-delta)
  cty,hy,_=info(y);ctnext,_,cbnext=info(y+delta)
  L=div(sub(cbx,cbprev),delta)
  U=div(sub(add(mul(m,ctnext),mul(n,cbnext)),add(mul(m,cty),mul(n,hy))),delta)
  positive('G_DEC_'+str(i),sub(mul(17,L),U))

def increase_D(l,r,parts=4):
 delta=Q(1,10000)
 for i in range(parts):
  x=l+(r-l)*Q(i,parts);y=l+(r-l)*Q(i+1,parts)
  ctx,_,cbx=info(x);cty,_,_=info(y)
  ctnext,_,_=info(y+delta);_,_,cbprev=info(x-delta)
  positive('17CB_14CT_VAL_'+str(i),sub(mul(17,cbx),mul(14,ctx)))
  L=div(sub(cbx,cbprev),delta);U=div(sub(ctnext,cty),delta)
  positive('17CB_14CT_SLOPE_'+str(i),sub(mul(17,L),mul(14,U)))

def main():
 l,r=Q(4,5),Q(9,11)
 breaks=sorted({Q(k,m) for m in range(1,17) for k in range(m+1) if l<=Q(k,m)<=r})
 assert breaks==[Q(4,5),Q(13,16),Q(9,11)],breaks
 for x,y in zip(breaks,breaks[1:]):
  for s in [x,(x+y)/2]:
   assert hull(counts(s))==[(0,17),(10,5),(14,0)],(s,hull(counts(s)))
  print('HULL',x,y,[(0,17),(10,5),(14,0)])
 assert hull(counts(r))==[(0,17),(11,4),(14,0)]
 print('RIGHT_BOUNDARY_HULL',r,[(0,17),(11,4),(14,0)])
 dec_G(l,r,10,5)
 ct,h,cb=info(l);positive('LEFT_10T5B_BEATS_17B',sub(add(mul(10,ct),mul(5,h)),mul(17,cb)))
 ct,h,cb=info(Q(8002,10000));positive('AT_8002_10T5B_BEATS_17B',sub(add(mul(10,ct),mul(5,h)),mul(17,cb)))
 ct,h,cb=info(Q(8003,10000));positive('RIGHT_10T5B_LOSES_17B',sub(mul(12,cb),mul(10,ct)))
 increase_D(l,r)
 ct,h,cb=info(r)
 positive('AT_9_11_11T4B_BEATS_17B',sub(add(mul(11,ct),mul(4,h)),mul(17,cb)))
 positive('AT_9_11_11T4B_BEATS_14T',sub(mul(4,h),mul(3,ct)))
 assert COUNT==12+3+8+2,COUNT
 print('ASSERTIONS',COUNT)
 print('PASS_EXACT_K17_S23_PHASE_4_5_TO_9_11_20261105')
if __name__=='__main__':main()
