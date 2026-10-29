#!/usr/bin/env python3
"""Exact QQ(i)[t]/H3 author-side test. Requires SymPy, Python 3."""
import sympy as s
from fractions import Fraction as F
T,U,V=s.symbols('t u v'); I=s.I; R=s.Rational
H=s.Poly(20146977828425934386944*T**3-1153636440395600981600*T**2-3151971160768643750*T-1890887364703125,T,domain=s.QQ_I)
assert H.is_irreducible
class K:
 def __init__(self,x=0):
  self.p=(x.p if isinstance(x,K) else s.Poly(x.as_expr() if isinstance(x,s.Poly) else x,T,domain=s.QQ_I)).rem(H)
 def __add__(self,x):return K(self.p+K(x).p)
 def __radd__(self,x):return self+x
 def __neg__(self):return K(-self.p)
 def __sub__(self,x):return self+-K(x)
 def __mul__(self,x):return K(self.p*K(x).p)
 def __rmul__(self,x):return self*x
 def __truediv__(self,x):return self*K(s.invert(K(x).p,H))
 def __eq__(self,x):return (self-K(x)).p.is_zero
 def bar(self):return K(sum(s.conjugate(c)*T**m[0] for m,c in self.p.terms()))
 def zero(self):return self.p.is_zero

def trim(a):
 while a and a[-1].zero():a.pop()
 return a

def div(a,b):
 a=list(a); q=[K() for _ in range(max(0,len(a)-len(b)+1))]
 while len(a)>=len(b):
  n=len(a)-len(b); x=a[-1]/b[-1]; q[n]=x
  for j in range(len(b)):a[n+j]=a[n+j]-x*b[j]
  trim(a)
 return q,a

def gcd(a,b):
 while b:_,r=div(a,b);a,b=b,r
 return [x/a[-1] for x in a]

def coef(expr):return [K(x) for x in reversed(s.Poly(expr,U).all_coeffs())]

def at(expr,x):
 y=K()
 for c in s.Poly(expr,U).all_coeffs():y=y*x+K(c)
 return y
A=s.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],[-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
Q=[34000+204144*T,3200+56336*T,58250+1286*T,46600+12936*T,31525+28011*T]
B=s.simplify(A[3:,:]*A[:3,:].inv())
Fs=[]
for j in range(2):
 z=list(B.row(j));h=z[0]+z[1]*U+z[2]*V
 hstar=s.conjugate(z[0])*Q[0]*U*V+s.conjugate(z[1])*Q[1]*V+s.conjugate(z[2])*Q[2]*U
 Fs.append(s.expand(h*hstar-Q[3+j]*U*V))
(a,b,c),(d,e,f)=[s.Poly(x,V).all_coeffs() for x in Fs]
D=s.expand(d*b-a*e); E=s.expand(d*c-a*f)
u0=-gcd(coef(D),coef(E))[0]
assert at(D,u0)==0 and at(E,u0)==0
num=s.expand((a*f-c*d)**2-(a*e-b*d)*(b*f-c*e))
assert s.Poly(num,U).eval(0)==0
P=s.cancel(num/U)
assert s.degree(P,U)==6
assert gcd(coef(P),coef(s.diff(P,U)))==[-u0,K(1)]
assert at(s.diff(P,U,2),u0)!=0
assert K(Q[0])*u0*u0.bar()==K(Q[1])
F4=[at(x,u0) for x in (a,b,c)];F5=[at(x,u0) for x in (d,e,f)]
alpha,beta,gamma=F4; assert not alpha.zero()
lam=F5[0]/alpha; assert F5==[lam*x for x in F4]
r3=K(Q[2])/K(Q[0]);rev=[gamma.bar(),beta.bar()*r3,alpha.bar()*r3*r3]
assert rev==[rev[0]/alpha*x for x in F4]
gap=K(Q[0])*beta*beta.bar()-4*K(Q[2])*alpha*alpha.bar()
sep=5*gap+K(Q[0])*alpha*alpha.bar()
assert gap==gap.bar() and sep==sep.bar()
left,right=F('0.0598990506977195435624'),F('0.0598990506977195435625')
QQ=lambda f:R(f.numerator,f.denominator)
assert right-left==F(1,10**22)
assert H.eval(QQ(left))*H.eval(QQ(right))<0
assert s.Poly(H.as_expr(),T,domain=s.QQ).count_roots(0,R(1,4))==1

def interval(x):
 y=(F(0),F(0))
 for coeff in x.p.all_coeffs():
  assert s.im(coeff)==0
  mul=(y[0]*left,y[0]*right,y[1]*left,y[1]*right)
  v=s.Rational(s.re(coeff)); f=F(int(v.p),int(v.q))
  y=(min(mul)+f,max(mul)+f)
 return y
assert interval(gap)[1]<-F(10**14)
assert interval(sep)[1]<0
Fu=[[at(x,u0) for x in s.Poly(s.diff(z,U),V).all_coeffs()] for z in Fs]
xx,yy,zz=[lam*Fu[0][k]-Fu[1][k] for k in range(3)]
res=(alpha*zz-gamma*xx)*(alpha*zz-gamma*xx)-(alpha*yy-beta*xx)*(beta*zz-gamma*yy)
assert not res.zero()
print('PASS_PREFIX357_EXACT_CUBIC_PROJECTION_HAS_TWO_REGULAR_PHYSICAL_LIFTS')
print('t_c:',left,right,'; strict |v1-v2|^2 > 1/5')
print('gcd(D,E)=u-u0; gcd(P,P_u)=u-u0; real-Jacobian resultant nonzero')
