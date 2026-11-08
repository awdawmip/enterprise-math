#!/usr/bin/env python3
"""Exact Q[w,z,t] spectral collision certificate (native X6-BRC, frozen f42f2906)."""
import sympy as S
w,z,t,s=S.symbols('w z t s')
L=s*s+4*(w+1)*s-48*w
cp=(t**3-2*t**2-12*t*w-72*w)*(t**3+2*t**2-12*t*w+72*w)
cm=(t**3-2*t**2+4*t*w+24*w)*(t**3+2*t**2+4*t*w-24*w)
P=S.expand((t*t-4)*L.subs(s,t*t)*cp*cm)
B=S.expand(4*((4*w+1)*(t*t)**7+4*(16*w*w-11*w-2)*(t*t)**6
 +16*(24*w**3+34*w*w-2*w+1)*(t*t)**5
 +64*w*(48*w**3-270*w*w-92*w+9)*(t*t)**4
 +768*w*w*(12*w**3-81*w*w+140*w-18)*(t*t)**3
 -27648*w**3*(21*w*w+38*w+10)*(t*t)**2
 +995328*w**4*(10*w+7)*(t*t)-35831808*w**5))
H=(t*t-4)*(t*t-4*w)*(t*t+12*w)*L.subs(s,t*t)
R=P-(z-1)*B
def even_to_s(expr):
    poly=S.Poly(S.expand(expr),t)
    assert all(poly.nth(2*k+1)==0 for k in range(poly.degree()//2+1))
    return S.expand(sum(poly.nth(2*k)*s**k for k in range(poly.degree()//2+1)))
pu=even_to_s(P); bu=even_to_s(B)
assert S.expand(pu.subs(s,t*t)-P)==0
assert S.expand(bu.subs(s,t*t)-B)==0
assert S.factor(pu.subs(s,4))==0
assert S.factor(bu.subs(s,4))==-6291456*w**2*(w-1)**2*(3*w+1)
assert S.factor(pu.subs(s,4*w))==8388608*w**5*(w-25)*(w-1)**3
assert S.factor(bu.subs(s,4*w))==2097152*w**5*(w-1)**2*(4*w-25)
assert S.factor(pu.subs(s,-12*w))==-679477248*w**5*(w-1)*(w+3)*(3*w+1)**2
assert S.factor(bu.subs(s,-12*w))==-169869312*w**5*(3*w+1)*(5*w+3)
assert S.factor(S.resultant(L,bu,s))==-712483534798848*w**7*(w-1)**2*(3*w**3+42*w**2+2*w+1)
zA=(4*w*w-100*w+75)/(4*w-25)
zB=(12*w**3+28*w*w-23*w-9)/(5*w+3)
assert S.factor(zA-(1+4*(w-25)*(w-1)/(4*w-25)))==0
assert S.factor(zB-(1+4*(w-1)*(w+3)*(3*w+1)/(5*w+3)))==0
assert S.factor(zA-zB)==-16*w*(w-1)*(3*w**2-10*w-29)/((4*w-25)*(5*w+3))
g=S.gcd(S.Poly(H.subs(w,1),t,domain=S.QQ.frac_field(z)),
        S.Poly(R.subs(w,1),t,domain=S.QQ.frac_field(z))).as_expr()
assert S.simplify(g-(t*t-4)**2)==0
ru=pu-(z-1)*bu
assert S.factor((ru.subs(z,zA)*(4*w-25)).subs(s,4*w))==0
assert S.factor((ru.subs(z,zB)*(5*w+3)).subs(s,-12*w))==0
wstar=(5+4*S.sqrt(7))/3
assert S.simplify(zA.subs(w,wstar)-zB.subs(w,wstar))==0
assert S.N(zA.subs(w,wstar))>0
for w0 in (S.Rational(1,2),S.Rational(4,5),S.Integer(2),S.Integer(5),
           S.Integer(6),S.Integer(7),S.Integer(10),S.Integer(30)):
    for zform,quad in ((zA,t*t-4*w),(zB,t*t+12*w)):
        zz=zform.subs(w,w0)
        if zz<0 or zz==1 or w0==S.Rational(25,4): continue
        gg=S.gcd(S.Poly(H.subs(w,w0),t),S.Poly(R.subs({w:w0,z:zz}),t)).as_expr()
        assert S.rem(S.Poly(gg,t),S.Poly(quad.subs(w,w0),t))==0
print("ALL_ASSERTIONS_PASS: exact positive spectral-collision locus")
print("w*=(5+4sqrt(7))/3; z*=(14635+6848sqrt(7))/411")
