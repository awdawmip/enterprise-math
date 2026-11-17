#!/usr/bin/env python3
# R249: strict dyadic interval certificate for 42 second derivatives; Python 3 stdlib
from fractions import Fraction as F
import sys,time,json,hashlib,os
D=1<<128

class I:
 __slots__=('l','u')
 def __init__(self,l,u=None,raw=False):
  if raw:self.l=l;self.u=u if u is not None else l
  else:
   a=F(l); b=F(l if u is None else u)
   self.l=a.numerator*D//a.denominator
   self.u=-(-b.numerator*D//b.denominator)
  assert self.l<=self.u
 @classmethod
 def raw(cls,l,u):return cls(l,u,True)
 def __add__(a,b):
  b=iv(b);return I.raw(a.l+b.l,a.u+b.u)
 __radd__=__add__
 def __neg__(a):return I.raw(-a.u,-a.l)
 def __sub__(a,b):return a+-iv(b)
 def __rsub__(a,b):return iv(b)+-a
 def __mul__(a,b):
  b=iv(b);p=[a.l*b.l,a.l*b.u,a.u*b.l,a.u*b.u]
  return I.raw(min(p)//D,-(-max(p)//D))
 __rmul__=__mul__
 def __truediv__(a,b):
  b=iv(b); assert b.l>0 or b.u<0
  # inverse of b with floor/ceil of D^2/b
  if b.l<0:assert b.u<0
  rev=I.raw((D*D)//b.u,-(-(D*D)//b.l))
  return a*rev
 def __rtruediv__(a,b):return iv(b)/a
 def __pow__(a,k):
  assert k>=0
  x=I(1)
  while k:
   if k&1:x=x*a
   if k>1:a=a*a
   k//=2
  return x
 def __repr__(a):return f'[{a.l/D:.9g},{a.u/D:.9g}]'
 def width(a):return (a.u-a.l)/D
 def lfloat(a):return a.l/D
 def ufloat(a):return a.u/D

def iv(a):return a if isinstance(a,I) else I(a)

def ids(mask):return [0]+[i for i in range(1,7) if mask & (1<<(i-1))]

W=(144,576,1440,4320,17280,86400,518400)

def root(par,mask,steps=80):
 a,ad,b,bd,pi,pid,Z,Zd,rho,rhod=par
 ix=ids(mask)
 lo=max(a[i].u for i in ix);up=D
 def fa(x,upper):
  z=I.raw(x,x)
  return sum([I.raw(b[i].u,b[i].u)/(z-I.raw(a[i].u,a[i].u)) if upper else I.raw(b[i].l,b[i].l)/(z-I.raw(a[i].l,a[i].l)) for i in ix],I(0))-1
 # approximate root endpoints can use binary over interval range with endpoint f_l f_u
 # lower needs upper-bound of lower root (bracket f_low); upper needs upper root f_up
 lb=lo;ub=up
 for _ in range(steps):
  m=(lb+ub)//2
  if fa(m,False).l>0:lb=m
  else:ub=m
 low=lb
 lb=lo;ub=up
 for _ in range(steps):
  m=(lb+ub)//2
  if fa(m,True).u>0:lb=m
  else:ub=m
 return I.raw(low,ub)

class J:
 __slots__=('v','d','dd')
 def __init__(self,v,d=0,dd=0):self.v=iv(v);self.d=iv(d);self.dd=iv(dd)
 def __add__(a,b):
  b=j(b);return J(a.v+b.v,a.d+b.d,a.dd+b.dd)
 __radd__=__add__
 def __neg__(a):return J(-a.v,-a.d,-a.dd)
 def __sub__(a,b):return a+-j(b)
 def __rsub__(a,b):return j(b)+-a
 def __mul__(a,b):
  b=j(b);return J(a.v*b.v,a.v*b.d+a.d*b.v,a.v*b.dd+2*a.d*b.d+a.dd*b.v)
 __rmul__=__mul__
 def inv(a):
  v=1/a.v;return J(v,-a.d*v**2,2*a.d*a.d*v**3-a.dd*v**2)
 def __truediv__(a,b):return a*j(b).inv()
 def __rtruediv__(a,b):return j(b)*a.inv()
 def __pow__(a,k):
  assert isinstance(k,int)
  if k<0:return (a.inv())**(-k)
  if k==0:return J(1)
  if k==1:return a
  x=J(1)
  while k:
   if k&1:x=x*a
   if k>1:a=a*a
   k//=2
  return x
 def __repr__(a):return f'J({a.v},{a.d},{a.dd})'

def j(x):return x if isinstance(x,J) else J(x)

def params(s):
 t=(1691*s-2615)/(2615*s-3539)
 a=[j(F(1,5)),j(F(1,4)),j(F(3,10)),j(F(9,20)),s,j(F(2,3)),t]
 b=[j(F(13,60))]+[j(F(5,18))*(j(F(1,2))-x) for x in a[1:5]]+[j(F(5,18))*(x-j(F(1,2))) for x in a[5:]]
 pi=[y/(1-x) for x,y in zip(a,b)]
 Z=sum((y/(1-x)**2 for x,y in zip(a,b)),J(0))
 rho=[y/(1-x)**2/Z for x,y in zip(a,b)]
 return a,b,pi,Z,rho

def mode(par,mask,k):
 a,b,pi,Z,rho=par
 xval=root(( [p.v for p in a],None,[p.v for p in b],None,None,None,None,None,None,None ), mask)
 ix=ids(mask)
 den=[xval-a[i].v for i in ix]
 Q=sum((b[i].v/d**2 for i,d in zip(ix,den)),I(0))
 xp=sum((b[i].d/d+b[i].v*a[i].d/d**2 for i,d in zip(ix,den)),I(0))/Q
 x0=J(xval,xp,0)
 f=sum((b[i]/(x0-a[i]) for i in ix),J(-1))
 xpp=f.dd/Q
 x=J(xval,xp,xpp)
 Qj=sum((b[i]/(x-a[i])**2 for i in ix),J(0))
 Sj=sum((b[i]/((1-a[i])*(x-a[i])) for i in ix),J(0))
 amp=W[mask.bit_count()]*Sj**2/(Z*Qj)
 return amp*x**k

def obs_multiple(par, ns):
 a,b,pi,Z,rho=par
 result={n:J(0) for n in ns}
 steps={n-1:n for n in ns}
 for mask in range(63):
  ix=ids(mask); z=[J(1) for _ in ix]
  for k in range(max(steps)+1):
   if k in steps:
    result[steps[k]]+=W[mask.bit_count()]*sum((rho[i]*z[jj] for jj,i in enumerate(ix)),J(0))
   if k==max(steps):break
   dot=sum((pi[i]*z[jj] for jj,i in enumerate(ix)),J(0))
   z=[a[i]*z[jj]+(1-a[i])*dot for jj,i in enumerate(ix)]
 return result

def certificate():
 import json,hashlib,time,os
 st=time.time(); out=[]
 begin=int(os.environ.get("R249_START",390));end=int(os.environ.get("R249_END",411))
 for jidx in range(begin,end):
  s=F(jidx,1000);par=params(J(I(s),1));obs=obs_multiple(par,[270,403]);row={'s':str(s),'checks':{}}
  for n,floor in ((270,F(1)),(403,F(2,5))):
   phi=obs[n];X=mode(par,59,n-1)+mode(par,55,n-1)
   N=phi.d*X.v-phi.v*X.d
   sec=(phi.dd*X.v-phi.v*X.dd)/X.v**2-2*N*X.d/X.v**3
   lower=I(floor).l
   margin=sec.l-lower
   assert margin>0,(s,n,'lower bound failed',sec)
   row['checks'][str(n)]={'floor':str(floor),
     'sec_lower_decimal_9':str(sec.l*10**9//D),
     'sec_upper_decimal_9':str(-(-sec.u*10**9//D)),
     'positive_margin_bits':margin.bit_length(),
     'positive_margin_sha256':hashlib.sha256(str(margin).encode()).hexdigest()}
  out.append(row);print('OK',str(s),'elapsed',round(time.time()-st,2),flush=True)
 result={'schema':'EM_R249_EXACT_DYADIC_SECOND_DERIVATIVE_GRID_V1','source_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34','rounding':'outward fixed-point dyadic 2^128','root_bisections':80,'masks':63,'parameters':len(out),'checks':2*len(out),'all_pass':True,'rows':out}
 path=f'/mnt/data/R249_verification_{begin}_{end}.json'
 with open(path,'w') as fh:json.dump(result,fh,ensure_ascii=False,sort_keys=True,indent=2)
 print('PASS',2*len(out),'checks; elapsed',time.time()-st,'json_path',path)
 return result

if __name__=='__main__':certificate()
