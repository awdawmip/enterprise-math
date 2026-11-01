#!/usr/bin/env python3
import sympy as S
a,b,x,y=S.symbols('a b x y',real=True); I=S.I
u=a+I*b; v=x+I*y
H=(5+9*I)/2+(3+7*I)*u/2
z4=H+4*I*v
z5=(22+15*I)*(1+u)/8+(5+9*I)*v/4
norm=lambda z:S.expand(S.re(z*S.conjugate(z)))
I4=norm(z4); K=S.expand(norm(z5)-S.Rational(709,32))
r=a*a+b*b; s=1+2*a+r; J=norm(H)
A=S.expand(I4.diff(x).subs({x:0,y:0}))
B=S.expand(I4.diff(y).subs({x:0,y:0}))
P=S.expand(K.diff(x).subs({x:0,y:0}))
Q=S.expand(K.diff(y).subs({x:0,y:0}))
check=[
 J-(7-5*r+S.Rational(39,2)*s-4*b),
 I4-(J+A*x+B*y+16*(x*x+y*y)),
 K-(S.Rational(709,64)*(s-2)+P*x+Q*y+S.Rational(53,8)*(x*x+y*y)),
 A-(36+28*a+12*b), B-(-20-12*a+28*b),
 P-(245*(1+a)+123*b)/16,
 Q-(-123*(1+a)+245*b)/16,
 A*A+B*B-64*J,
 P*P+Q*Q-S.Rational(37577,128)*s,
 A*P+B*Q-(705+521*r+1226*a-61*b),
 P*B-Q*A-(63*r+4*a-368*b-59)/2]
for i,item in enumerate(check):
 assert S.expand(item)==0,i
 print('PASS_RAW_MATRIX',i+1)
rho,h,t=S.symbols('rho h t',positive=True,real=True)
x0=-rho*A/(8*h);y0=-rho*B/(8*h)
xt=(x0*(1-t*t)-2*t*y0)/(1+t*t)
yt=(y0*(1-t*t)+2*t*x0)/(1+t*t)
D=rho*(P*B-Q*A)/(8*h);M=rho*(A*P+B*Q)/(8*h)
assert S.simplify(P*(xt-x0)+Q*(yt-y0)-(2*D*t+2*M*t*t)/(1+t*t))==0
assert S.simplify(A*(xt-x0)+B*(yt-y0)-rho*t*t*(A*A+B*B)/(4*h*(1+t*t)))==0
eps=S.symbols('eps',nonnegative=True)
w=S.sqrt(1+eps-eps**2);g=4+59*eps+368*w
assert S.simplify((P*B-Q*A).subs({a:-eps,b:-w})-g/2)==0
print('PASS_PREFIX427_INDEPENDENT_RAW_MATRIX')
