#!/usr/bin/env python3
"""Exact Groebner/Sturm and finite-rational-root-neighborhood certificate, PREFIX-375."""
import sympy as S
x,c,d=S.symbols('x c d')
a=14*c-6*d+S.Rational(39,2); b=-6*c-14*d+2
p=(245*c-123*d)/32+S.Rational(709,64); q=(-123*c-245*d)/32
r4=(-72*c+40*d+257*x-132)/4
r5=(-51940*c+26076*d+158627*x-91398)/6784
K=S.Rational(1101,424)-S.Rational(995,106)*x
G=S.groebner([c*c+d*d-K,a*q-b*p,a*r5-p*r4,b*r5-q*r4],c,d,x,order='lex',domain=S.QQ)
P=969505478041769500*x**3-252816887318686105*x**2+21782521288209164*x-619641499680032
cx=(836683227550047078500*x**2-146252284556197622175*x+4948966322288902942)/S.Integer(1172832320624741976)
dx=5*(295311368611522989700*x**2-52906334345592005367*x+2487897947259729302)/S.Integer(1172832320624741976)
assert G == S.groebner([c-cx,d-dx,P],c,d,x,order='lex',domain=S.QQ)
assert S.gcd(S.Poly(P,x),S.Poly(S.diff(P,x),x)).degree()==0
L=S.Rational(8,85); U=S.Rational(4321,21259)
assert S.Poly(P,x).count_roots(-S.oo,L)==2
assert S.Poly(P,x).count_roots(L,U)==1
assert S.Poly(P,x).count_roots(-S.oo,S.oo)==3
lo=S.Rational(100169778291,10**12); hi=S.Rational(100169778292,10**12)
assert L<lo<hi<U and P.subs(x,lo)<0<P.subs(x,hi)
A=a.subs({c:cx,d:dx}); B=b.subs({c:cx,d:dx})
N=S.expand(A*A+B*B)
R=r4.subs({c:cx,d:dx})
slack=S.expand(x*N-R*R)
margin=S.expand(16*B*B*slack-N*N)
for expr in [N-S.Rational(1,10),slack-S.Rational(1,125),margin-S.Rational(1,2000)]:
    poly=S.Poly(expr,x,domain=S.QQ)
    assert poly.count_roots(lo,hi)==0 and poly.eval(lo)>0
T=(200-2125*x)/(12759*x-3521)
assert T.subs(x,lo)>0 and T.subs(x,hi)<S.Rational(1,4)
assert (12759*lo-3521)<0 and (12759*hi-3521)<0
assert S.diff(T,x).subs(x,lo)>0 and S.diff(T,x).subs(x,hi)>0
print('P(x) =',P)
print('physical roots: 1; below range: 2; exact physical root: ('+str(lo)+','+str(hi)+')')
print('N > 1/10, slack > 1/125, (16 beta^2 slack - N^2) > 1/2000')
print('C_v(x,v)=1+K(x)+2*Re(v): equal C_v iff same Re(v); then v or conjugate(v).')
print('PASS_PREFIX375_UNIQUE_GLOBAL_SAME_V_DOUBLE_SOURCE')
