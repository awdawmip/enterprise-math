"""Exact outward-rational certificate for S23 auxiliary T/B K17 phase [14/15,15/16].
Python 3 standard library only. Each assertion checks a strictly positive rational lower bound.
This is the auxiliary source/projection statistical experiment, not the ten-label minimax.
"""
from fractions import Fraction as Q
from math import isqrt,gcd
from functools import lru_cache
A,B=Q(11,21),Q(10,21)
SCALE,TERMS=10**36,34
CERTS=[]

def I(x):return x if isinstance(x,tuple) else (Q(x),Q(x))
def add(x,y):
 x,y=I(x),I(y);return x[0]+y[0],x[1]+y[1]
def neg(x):
 x=I(x);return -x[1],-x[0]
def sub(x,y):return add(x,neg(y))
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
 v=(x-1)/(x+1);assert abs(v)<Q(1,3),("LOG_RANGE",str(x))
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
 x=I(x)
 assert x[0]>0,(tag,str(x[0]),str(x[1]))
 CERTS.append(tag)
 print(tag,'STRICT_POSITIVE_LOWER_BOUND_1e12',x[0].numerator*10**12//x[0].denominator)

def counts(s):
 s=Q(s)
 return [(m,17-2*m+(m*s).__floor__()) for m in range(18) if 17-2*m+(m*s).__floor__()>=0]
def hull(points):
 h=[]
 for x,y in points:
  while len(h)>1:
   (u,v),(w,z)=h[-2:]
   if (w-u)*(y-z)-(z-v)*(x-w)>=0:h.pop()
   else:break
  h.append((x,y))
 return h

def derivative_bounds(lo,hi,parts=16):
 # Convex-slope bounds certify G=F(15,1)-17CB is strictly decreasing
 # uniformly in each REAL cell, without sampling assumptions.
 delta=Q(1,10000)
 for i in range(parts):
  x=lo+(hi-lo)*Q(i,parts);y=lo+(hi-lo)*Q(i+1,parts)
  _,_,cbx=info(x);_,_,cbprev=info(x-delta)
  cty,hy,_=info(y);ctnext,_,cbnext=info(y+delta)
  cb_lower_slope=div(sub(cbx,cbprev),delta)
  f_upper_slope=div(sub(add(mul(15,ctnext),cbnext),add(mul(15,cty),hy)),delta)
  positive(f'G_STRICT_DECREASE_CELL_{i:02d}',sub(mul(17,cb_lower_slope),f_upper_slope))

def main():
 lo,hi=Q(14,15),Q(15,16)
 breaks=sorted({Q(k,m) for m in range(1,18) for k in range(m+1) if lo<=Q(k,m)<=hi})
 assert breaks==[lo,hi],breaks
 open_pts=counts(lo);assert open_pts==counts((lo+hi)/2)
 assert hull(open_pts)==[(0,17),(15,1)]
 assert hull(counts(hi))==[(0,17),(16,0)]
 for points in [[(0,17),(15,1)],[(0,17),(16,0)]]:
  for (m,n),(p,q) in zip(points,points[1:]):assert gcd(p-m,abs(q-n))==1
 print('COST_BREAKPOINTS',list(map(str,breaks)))
 print('OPEN_HULL',hull(open_pts),'RIGHT_HULL',hull(counts(hi)))
 derivative_bounds(lo,hi,parts=16)
 ct,h,cb=info(lo)
 positive('LEFT_15T1B_GT_17B',sub(add(mul(15,ct),h),mul(17,cb)))
 for tag,s,side in [('ALPHA_LOWER',Q(93343,100000),'lo'),('ALPHA_UPPER',Q(93344,100000),'hi')]:
  ct,h,cb=info(s)
  positive(tag,sub(add(mul(15,ct),h),mul(17,cb)) if side=='lo' else sub(mul(17,cb),add(mul(15,ct),cb)))
 ct,h,cb=info(hi)
 positive('RIGHT_16T_GT_17B',sub(mul(16,ct),mul(17,cb)))
 positive('RIGHT_CT_GT_CB',sub(ct,cb))
 # Explicit repair of the earlier [13/14,14/15] checker label:
 # 'RIGHT_15T1B_GT_17B' there used 14CT+2H instead of 15CT+H.
 ct,h,cb=info(lo)
 positive('PREVIOUS_RIGHT_CORRECTED_15T1B_GT_17B',sub(add(mul(15,ct),h),mul(17,cb)))
 assert len(CERTS)==22,len(CERTS)
 print('STRICT_RATIONAL_ASSERTIONS',len(CERTS))
 print('PASS_K17_S23_PHASE_14_15_TO_15_16_EXACT_20261105')
if __name__=='__main__':main()
