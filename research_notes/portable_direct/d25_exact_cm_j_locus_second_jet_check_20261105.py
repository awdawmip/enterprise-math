#!/usr/bin/env python3
"""D25 2026-11-05: exact CM j-locus/second jet and quadratic-ring checks."""
import sympy as S
T=S.sqrt(2); R=S.Rational; u,v,X=S.symbols("u v X")
u0=R(1,2)-T/4;v0=R(1,2)-T/3
J3=27*(1+8*u)**3/(u*(1-u)**3)
J4=64*(1+3*v)**3/(v*(1-v)**2)
j=S.simplify(J3.subs(u,u0))
assert S.simplify(j-J4.subs(v,v0))==0
assert S.simplify(j-(2417472-1707264*T))==0
assert S.minimal_polynomial(j,X)==X**2-4834944*X+14670139392
J4p=S.simplify(S.diff(J4,v).subs(v,v0))
assert S.simplify(J4p-(172005120-121678848*T))==0
assert S.simplify(J4p*J4p.xreplace({T:-T})+2**16*3**10*17**2*23)==0
vu=S.simplify(S.diff(J3,u).subs(u,u0)/J4p)
vuu=S.simplify((S.diff(J3,u,2).subs(u,u0)-S.diff(J4,v,2).subs(v,v0)*vu**2)/J4p)
zu=4*(1-2*u0); tv=4*(1-2*v0)
t1=S.simplify(tv*vu/zu)
tder2=S.simplify(((-8*vu**2+tv*vuu)*zu-tv*vu*(-8))/zu**3)
assert S.simplify(vu+2*T/9)==0
assert S.simplify(vuu-(40+56*T)/27)==0
assert S.simplify(t1+8*T/27)==0
assert S.simplify(tder2-(104+16*T)/81)==0
assert S.simplify(t1/(3*T/4)+R(32,81))==0
z0=R(1,2);t0=R(1,9)
P=lambda z:(1-R(3,2)*z)/(z*(1-z))
forced=S.simplify((P(t0)*t1-tder2/t1-P(z0))/2)
assert S.simplify(forced+(1+T)/6)==0
assert t1.is_negative is True and forced.is_negative is True
class Q:
 def __init__(self,a,b=0,m=13):self.a=a%m;self.b=b%m;self.m=m
 def __add__(x,y):
  if not isinstance(y,Q):y=Q(y,0,x.m)
  return Q(x.a+y.a,x.b+y.b,x.m)
 __radd__=__add__
 def __neg__(x):return Q(-x.a,-x.b,x.m)
 def __sub__(x,y):return x+(-y if isinstance(y,Q) else -y)
 def __rsub__(x,y):return -x+y
 def __mul__(x,y):
  if not isinstance(y,Q):y=Q(y,0,x.m)
  return Q(x.a*y.a+2*x.b*y.b,x.a*y.b+x.b*y.a,x.m)
 __rmul__=__mul__
 def __pow__(x,n):
  if n<0:return x.inv()**(-n)
  y=Q(1,0,x.m)
  while n:
   if n&1:y=y*x
   x=x*x;n//=2
  return y
 def inv(x):
  t=pow((x.a*x.a-2*x.b*x.b)%x.m,-1,x.m)
  return Q(x.a*t,-x.b*t,x.m)
 def __truediv__(x,y):
  if not isinstance(y,Q):y=Q(y,0,x.m)
  return x*y.inv()
 def __eq__(x,y):
  if not isinstance(y,Q):y=Q(y,0,x.m)
  return x.a==y.a and x.b==y.b
count=0
for p in S.primerange(5,10000):
 if p%24 not in (13,19):continue
 m=int(p)**3; one=Q(1,0,m);rt=Q(0,1,m)
 U=one/2-rt/4;V=one/2-rt/3
 j3=lambda w:27*(one+8*w)**3/(w*(one-w)**3)
 j4=lambda w:64*(one+3*w)**3/(w*(one-w)**2)
 assert j3(U)==j4(V)
 a=-8*rt/27;b=(52+8*rt)/81
 assert a/(3*rt/4)==Q(-32,0,m)/81
 for h in (1,2,3):
  e=int(p)*h;dt=a*e+b*e*e
  up=U+rt*e/4+rt*e*e/8
  vp=V+3*rt*dt/16+27*rt*dt*dt/512
  assert j3(up)==j4(vp),(p,h)
 count+=1
assert count==312
print("EXACT PASS: symbolic CM j+2jet+gauge sign, 312 target primes mod p^3, 3 perturbations each")
