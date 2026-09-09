"""Exact Q(sqrt(2),i) specialization of the inherited Fourier packet algebra.
The source algorithms (convection/Leray/heat resolvent) are unchanged; this
extension avoids symbolic-expression growth. Every omitted source must be
accounted for separately. It never truncates Fourier outputs.
"""
from fractions import Fraction as F
from collections import defaultdict
from math import factorial
import sympy as s
Z=(F(0),)*4
VZ=(Z,Z,Z)
rt=s.sqrt(2)
def ca(x,y):return tuple(a+b for a,b in zip(x,y))
def cn(x):return tuple(-a for a in x)
def cs(x,a):return tuple(a*b for b in x)
def prod(a,b):return (a[0]*b[0]+2*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cm(a,b):
 rr=prod(a[:2],b[:2]);ii=prod(a[2:],b[2:]);ri=prod(a[:2],b[2:]);ir=prod(a[2:],b[:2])
 return (rr[0]-ii[0],rr[1]-ii[1],ri[0]+ir[0],ri[1]+ir[1])
def minus_i(a):return (a[2],a[3],-a[0],-a[1])
def va(a,b):return tuple(ca(x,y) for x,y in zip(a,b))
def vs(a,c):return tuple(cs(x,c) for x in a)
def dotk(a,k):
 out=Z
 for x,t in zip(a,k):
  if t:out=ca(out,cs(x,t))
 return out
def rat(x):
 assert x.is_Rational, x
 return F(int(s.numer(x)),int(s.denom(x)))
def scalar_in(x):
 re,im=s.expand(x).as_real_imag()
 br=s.expand(re).coeff(rt);bi=s.expand(im).coeff(rt)
 return (rat(s.expand(re-br*rt)),rat(br),rat(s.expand(im-bi*rt)),rat(bi))
def scalar_out(a):return s.Rational(a[0].numerator,a[0].denominator)+s.Rational(a[1].numerator,a[1].denominator)*rt+s.I*(s.Rational(a[2].numerator,a[2].denominator)+s.Rational(a[3].numerator,a[3].denominator)*rt)
def import_packets(A):return {key:tuple(scalar_in(x) for x in vec) for key,vec in A.items()}
def export_packets(A):return {key:s.Matrix([scalar_out(x) for x in vec]) for key,vec in A.items()}
def sq(k):return sum(x*x for x in k)
def put(out,k,z):out[k]=va(out.get(k,VZ),z)
def plus(A,B):
 out=dict(A)
 for key,vec in B.items():put(out,key,vec)
 return {k:v for k,v in out.items() if v!=VZ}
def scale(A,c):return {k:vs(v,c) for k,v in A.items() if c}
def ntime(A,B):
 out={}
 for (p,rp,mp),a in A.items():
  for (q,rq,mq),b in B.items():
   k=tuple(x+y for x,y in zip(p,q))
   if not any(k):continue
   dot=dotk(a,q)
   if dot==Z:continue
   vec=tuple(minus_i(cm(dot,z)) for z in b)
   put(out,(k,rp+rq,mp+mq),vec)
 result={}
 for (k,rate,power),v in out.items():
  div=cs(dotk(v,k),F(1,sq(k)))
  vv=tuple(ca(z,cs(div,-x)) for z,x in zip(v,k))
  if vv!=VZ:result[k,rate,power]=vv
 return result
def solve_heat(A):
 out={}
 for (k,rate,m),v in A.items():
  lam=sq(k);gap=lam-rate
  if gap==0:put(out,(k,lam,m+1),vs(v,F(1,m+1)))
  else:
   for j in range(m+1):put(out,(k,rate,m-j),vs(v,F((-1)**j*factorial(m),factorial(m-j)*gap**(j+1))))
   put(out,(k,lam,0),vs(v,-F((-1)**m*factorial(m),gap**(m+1))))
 return {k:v for k,v in out.items() if v!=VZ}
def heat_derivative(A):
 out={}
 for (k,r,m),v in A.items():
  put(out,(k,r,m),vs(v,sq(k)-r))
  if m:put(out,(k,r,m-1),vs(v,m))
 return {k:v for k,v in out.items() if v!=VZ}
def initial(A):
 out={}
 for (k,r,m),v in A.items():
  if m==0:put(out,k,v)
 return {k:v for k,v in out.items() if v!=VZ}
def gram_coeff(A,B):
 by=defaultdict(list)
 for (k,r,m),v in B.items():by[k].append((r,m,v))
 out=defaultdict(lambda:[F(),F()])
 for (k,ra,ma),aa in A.items():
  n=sq(k)
  for rb,mb,bb in by[k]:
   fac=F(factorial(ma+mb),(ra+rb)**(ma+mb+1));c0=c1=F()
   for a,b in zip(aa,bb):
    rr=prod(a[:2],b[:2]);ii=prod(a[2:],b[2:]);c0+=rr[0]+ii[0];c1+=rr[1]+ii[1]
   out[n][0]+=fac*c0;out[n][1]+=fac*c1
 return dict(out)
def gram_expr(A,B,power=-1):
 c=gram_coeff(A,B)
 return s.expand(sum(s.Integer(n)**s.Rational(power,2)*(s.Rational(a.numerator,a.denominator)+s.Rational(b.numerator,b.denominator)*rt) for n,(a,b) in c.items()))
