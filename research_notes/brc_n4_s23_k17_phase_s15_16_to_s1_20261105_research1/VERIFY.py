"""Exact outward-rational certificate for S23 auxiliary T/B K17 phase [15/16,1].
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
 # For real z in each closed cell [x,y], convexity gives
 # CB'(z)>=[CB(x)-CB(x-delta)]/delta;
 # CT'(z)<=CT'(y)=(1-2sqrt(ab))/(1-y+2y sqrt(ab)).
 delta=Q(1,10000)
 for i in range(parts):
  x=lo+(hi-lo)*Q(i,parts);y=lo+(hi-lo)*Q(i+1,parts)
  _,_,cbx=info(x);_,_,cbprev=info(x-delta)
  low_cb=div(sub(cbx,cbprev),delta)
  d=sub(1,mul(2,sqrt_i(A*B)))
  high_ct=div(d,sub(1,mul(y,d)))
  positive(f'G_STRICT_DECREASE_CELL_{i:02d}',sub(mul(17,low_cb),mul(16,high_ct)))

def main():
 lo,hi=Q(15,16),Q(1)
 breaks=sorted({Q(k,m) for m in range(1,18) for k in range(m+1) if lo<=Q(k,m)<=hi})
 assert breaks==[lo,Q(16,17),hi],breaks
 open_pts=counts(lo)
 assert open_pts==counts(Q(16,17))==counts(Q(999,1000))
 assert open_pts==[(0,17)]+[(m,16-m) for m in range(1,17)]
 assert hull(open_pts)==[(0,17),(16,0)]
 assert gcd(16,17)==1
 assert counts(hi)==[(m,17-m) for m in range(18)]
 assert A+B==1
 print('S1_ALL_OPTIMIZERS',counts(hi))
 print('FORMAL_BREAKPOINTS',list(map(str,breaks)))
 print('FEASIBLE_BOUNDARY_ON_[15/16,1)',open_pts)
 print('UPPER_HULL',hull(open_pts))
 derivative_bounds(lo,hi,parts=16)
 ct,h,cb=info(lo)
 positive('LEFT_16T_GT_17B',sub(mul(16,ct),mul(17,cb)))
 for tag,s,side in [('ROOT_LOWER',Q(937594859,10**9),'lo'),
                    ('ROOT_UPPER',Q(937594860,10**9),'hi')]:
  ct,h,cb=info(s)
  positive(tag,sub(mul(16,ct),mul(17,cb)) if side=='lo'
           else sub(mul(17,cb),mul(16,ct)))
 ct,h,cb=info(hi)
 positive('RIGHT_17B_GT_16T',sub(mul(17,cb),mul(16,ct)))
 assert len(CERTS)==20,len(CERTS)
 print('STRICT_RATIONAL_ASSERTIONS',len(CERTS))
 print('PASS_K17_S23_PHASE_15_16_TO_1_EXACT_20261105')
if __name__=='__main__':main()
