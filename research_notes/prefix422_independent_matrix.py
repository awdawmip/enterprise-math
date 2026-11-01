#!/usr/bin/env python3
"""Independent exact algebra and observer reconstruction for PREFIX-422.
SymPy 1.14; no use of the primary interval checker.
"""
import sympy as sp
I=sp.I
M=sp.Matrix([(4,4,0),(0,-4,4),(-5+3*I,0,-3+I),(-2-2*I,4+4*I,2+2*I),(-2,0,5+2*I)])
u,v=sp.symbols('u v')
w=M[:3,:].inv()*sp.Matrix([1,u,v]);z4=sp.expand((M[3,:]*w)[0]);z5=sp.expand((M[4,:]*w)[0]);
assert sp.simplify(z4-((5+9*I)/2+(3+7*I)*u/2+4*I*v))==0
assert sp.simplify(z5-((22+15*I)*(1+u)/8+(5+9*I)*v/4))==0
print('PASS original complex 5x3 inverse and all observation-port formulas')
a,b,x,y=sp.symbols('a b x y',real=True)
r=a*a+b*b;s=(1+a)**2+b*b;t=x*x+y*y
J=(53+29*r)/2+39*a-4*b
A=36+28*a+12*b;B=-20-12*a+28*b
P=(245*(1+a)+123*b)/16;Q=(-123*(1+a)+245*b)/16
c=sp.Rational(709,64)*(s-2);E=sp.Rational(53,8)
zz4=sp.expand(z4.subs({u:a+I*b,v:x+I*y}));zz5=sp.expand(z5.subs({u:a+I*b,v:x+I*y}))
assert sp.simplify(sp.expand(zz4*sp.conjugate(zz4))-(J+A*x+B*y+16*t))==0
assert sp.simplify(sp.expand(zz5*sp.conjugate(zz5)-sp.Rational(709,32))-(c+P*x+Q*y+E*t))==0
print('PASS all-source fourth/fifth Port affine-quadratic relations')
# The source mapping from both baseline intensities is invertible if the sign of Im u is retained.
rr,ss=sp.symbols('r s',real=True)
aa=(ss-rr-1)/2
assert sp.simplify((1+aa)**2+rr-aa**2-ss)==0
print('PASS source parameterization r,s,a,sign(Im u)')
# New supporting hyperplane, with target multiplier constants m,D, tau.
j0,A0,B0,P0,Q0,c0,m,D,eta,beta=sp.symbols('j A B P Q c m D eta beta',real=True,nonzero=True)
T=x*x+y*y;k=c0+P0*x+Q0*y+E*T
V=j0+A0*x+B0*y+16*T
C0=A0-m*P0;C1=B0-m*Q0;tau=D-16+E*m
U=j0-m*(c0+eta)-tau*beta-(C0*C0+C1*C1)/(4*D)
identity=m*(k+eta)+tau*(beta-T)+D*((x+C0/(2*D))**2+(y+C1/(2*D))**2)
assert sp.simplify(V-U-identity)==0
print('PASS complete-square support identity for every complex source')
p,q,K,R,S=sp.symbols('p q K R S',real=True)
N=p*p+q*q
X=(K*p+S*q)/N;Y=(K*q-S*p)/N
assert sp.simplify(p*X+q*Y-K)==0
assert sp.simplify((X*X+Y*Y-R)*N).subs(S*S,N*R-K*K).simplify()==0
print('PASS exact circle/line parametric source: k=-eta and t=beta')
# The intended lambda chosen from the line-circle point makes both stationarity components equal.
Ac,Bc,Pc,Qc,xx,yy=sp.symbols('Ac Bc Pc Qc xx yy',real=True,nonzero=True)
mu=(Ac*yy-Bc*xx)/(Pc*yy-Qc*xx)
DC=-(Ac-mu*Pc)/(2*xx)
assert sp.factor(Bc-mu*Qc+2*DC*yy)==0
assert sp.factor(Ac-mu*Pc+2*DC*xx)==0
print('PASS exact target stationarity for both real source components')
# Independent exact-radical comparison for eps=1e-6, eta=1/50.
be=sp.Rational(1,10**6);eta0=sp.Rational(1,50)
def target_at(rr,ss):
 aa=(ss-rr-1)/2;bb=-sp.sqrt(rr-aa**2)
 jj=(53+29*rr)/2+39*aa-4*bb
 av=36+28*aa+12*bb;bv=-20-12*aa+28*bb
 pp=(245*(1+aa)+123*bb)/16;qq=(-123*(1+aa)+245*bb)/16
 cc=sp.Rational(709,64)*(ss-2)
 kk=-eta0-cc-E*be;nn=pp**2+qq**2;rad=sp.sqrt(nn*be-kk**2)
 X=(kk*pp+rad*qq)/nn;Y=(kk*qq-rad*pp)/nn
 return jj+av*X+bv*Y+16*be
old=target_at(1+be,2+be);new=target_at(1+be,2-be)
print('independent 60-digit old-minus-new:',sp.N(old-new,60))
assert sp.N(old-new,60)>sp.Rational(7,10**7)
print('PASS_PREFIX422_INDEPENDENT_MATRIX_DUAL_IDENTITIES_AND_WITNESS')
