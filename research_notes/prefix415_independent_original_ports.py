#!/usr/bin/env python3
"""PREFIX-415: independent raw five-port symbolic identities."""
import sympy as s
I=s.I
A=s.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],[-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
T=s.simplify(A*A[:3,:].inv())
a,b,d,e=(5+9*I)/2,(3+7*I)/2,(22+15*I)/8,(5+9*I)/4
assert s.simplify(T[3,:]-s.Matrix([[a,b,4*I]]))==s.zeros(1,3)
assert s.simplify(T[4,:]-s.Matrix([[d,d,e]]))==s.zeros(1,3)
x,y,t,eta=s.symbols('x y t eta',real=True)
def norm2(z):return s.expand_complex(z*s.conjugate(z)).expand()
for sigma in (1,-1):
 u=sigma*I;v=x+I*y
 i4=norm2(a+b*u+4*I*v)
 k=norm2(d*(1+u)+e*v)-s.Rational(709,32)
 if sigma==1:
  assert s.expand(i4-(37+48*x+8*y+16*(x*x+y*y)))==0
  assert s.expand(k-(23*x+s.Rational(61,8)*y+s.Rational(53,8)*(x*x+y*y)))==0
 else:
  assert s.expand(i4-(45+24*x-48*y+16*(x*x+y*y)))==0
  assert s.expand(k-(s.Rational(61,8)*x-23*y+s.Rational(53,8)*(x*x+y*y)))==0
xt=-(eta+t)/2;yt=s.Rational(45,368)*(t-eta)
assert s.expand(2*xt+t+eta)==0
assert s.expand(s.Rational(61,8)*xt-23*yt+s.Rational(53,8)*t+eta)==0
assert s.expand(45-(45+24*xt-48*yt+16*t)-(141*eta+43*t)/23)==0
assert T[:3,:]==s.eye(3) and A[:3,:].det()!=0
print("PASS_PREFIX415_INDEPENDENT_ORIGINAL_FIVE_PORT_ALGEBRA")
