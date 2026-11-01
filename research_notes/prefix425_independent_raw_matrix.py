#!/usr/bin/env python3
"""PREFIX-425 independent SymPy check from raw 5x3 matrix and exact support algebra.
The only continuous-domain proof is the accompanying outward interval checker.
"""
import sympy as sp
I=sp.I
M=sp.Matrix([(4,4,0),(0,-4,4),(-5+3*I,0,-3+I),(-2-2*I,4+4*I,2+2*I),(-2,0,5+2*I)])
u,v=sp.symbols('u v')
w=M[:3,:].inv()*sp.Matrix([1,u,v])
z4=sp.expand((M[3,:]*w)[0]);z5=sp.expand((M[4,:]*w)[0])
assert sp.simplify(z4-((5+9*I)/2+(3+7*I)*u/2+4*I*v))==0
assert sp.simplify(z5-((22+15*I)*(1+u)/8+(5+9*I)*v/4))==0

a,b,x,y=sp.symbols('a b x y',real=True)
r=a*a+b*b;s=(1+a)**2+b*b;t=x*x+y*y
J=(53+29*r)/2+39*a-4*b
A=36+28*a+12*b;B=-20-12*a+28*b
P=(245*(1+a)+123*b)/16;Q=(-123*(1+a)+245*b)/16
c=sp.Rational(709,64)*(s-2);E=sp.Rational(53,8)
z4a=sp.expand(z4.subs({u:a+I*b,v:x+I*y}))
z5a=sp.expand(z5.subs({u:a+I*b,v:x+I*y}))
assert sp.expand(z4a*sp.conjugate(z4a)-(J+A*x+B*y+16*t))==0
assert sp.expand(z5a*sp.conjugate(z5a)-sp.Rational(709,32)-(c+P*x+Q*y+E*t))==0

J,A,B,P,Q,c,eta,beta,D,mu=sp.symbols('J A B P Q c eta beta D mu',real=True,nonzero=True)
k=c+P*x+Q*y+E*t
Cx=A-mu*P;Cy=B-mu*Q
Tau=D-16+E*mu
H=J-mu*(c+eta)-Tau*beta-(Cx**2+Cy**2)/(4*D)
assert sp.cancel(J+A*x+B*y+16*t-H-(mu*(k+eta)+Tau*(beta-t)+D*((x+Cx/(2*D))**2+(y+Cy/(2*D))**2)))==0

rr,ss,ee=sp.symbols('rr ss ee',real=True)
aa=(ss-rr-1)/2;bb=-sp.sqrt(rr-aa**2)
JJ=(53+29*rr)/2+39*aa-4*bb
AA=36+28*aa+12*bb;BB=-20-12*aa+28*bb
PP=(245*(1+aa)+123*bb)/16;QQ=(-123*(1+aa)+245*bb)/16
cc=sp.Rational(709,64)*(ss-2);nn=PP*PP+QQ*QQ
kk=-ee-cc-E*sp.Rational(1,10**6)
ssr=sp.sqrt(nn*sp.Rational(1,10**6)-kk*kk)
V=JJ+(AA*PP+BB*QQ)/nn*kk+(AA*QQ-BB*PP)/nn*ssr+sp.Rational(16,10**6)
point={rr:sp.Integer(1),ss:sp.Integer(2),ee:sp.Rational(1,100)}
vals=[sp.N(expr.subs(point),50) for expr in [V,sp.diff(V,rr),sp.diff(V,ss),sp.diff(sp.diff(V,ss),ee)]]
assert sp.Rational(449,10)<vals[0]<sp.Rational(45,1)
assert -sp.Rational(301,100)<vals[1]<-sp.Rational(299,100)
assert -sp.Rational(321,100)<vals[2]<-sp.Rational(318,100)
assert sp.Integer(190)<vals[3]<sp.Integer(194)
print('INDEPENDENT_RAW_PORT_AND_SUPPORT_IDENTITIES: PASS')
print('INDEPENDENT_V_Vr_Vs_VsEta_AT_(1,2,0.01):',*[str(v) for v in vals])
print('PASS_PREFIX425_INDEPENDENT_RAW_MATRIX_AND_SYMBOLIC_DERIVATIVES')
