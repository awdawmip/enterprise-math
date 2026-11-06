#!/usr/bin/env python3
"""PREFIX-528 exact rational identity and generic recurrence certificate; SymPy 1.14+."""
import sympy as s
q,u,t,z=s.symbols('q u t z')
E=1-4*u-(192+480*q)*u**2-(2304+8064*q+2304*q**2)*u**3-(82944*q+62208*q**2)*u**4-746496*q**2*u**5
D1=1+2*u-3*q*u**2
D2=1+(4+2*q)*u**2-(12*q+4*q**2)*u**3+9*q**2*u**4
D3=1-u-(12+30*q)*u**2-(36+126*q+36*q**2)*u**3-(324*q+243*q**2)*u**4-729*q**2*u**5
assert s.expand(D3.subs(u,4*u)-E)==0
c=[48,288,288*q+1248,3456*q+5760,8832*q+14208,
   13824*q**2+69120*q+55296,4608*q**2+152064*q+64512,
   331776*q**2+829440*q+165888,165888*q**2+829440*q,
   3981312*q**2+1990656*q]
N0=sum(a*t**i for i,a in enumerate(c))
k=[0,0,20*q,160*q**2+368*q,2560*q**2+5120*q,
   -27648*q**3+16384*q**2+27648*q,
   -73728*q**4-774144*q**3-485376*q**2+147456*q,
   -1400832*q**4-9732096*q**3-3833856*q**2,
   7077888*q**5-8847360*q**4-58392576*q**3-31850496*q**2,
   127401984*q**5+445906944*q**4-191102976*q**3,
   573308928*q**5+5733089280*q**4,-20639121408*q**5]
K=sum(v*u**i for i,v in enumerate(k))
A=1-2*t-48*(1+q)*t**3-144*q*t**4-864*q*t**5
B=1+2*t+48*(1+q)*t**3-144*q*t**4+864*q*t**5
U=(1+2*t)*(1+2*t+12*t**2)*B
Vm=8*t**2*(1+12*t**2)**2
Vp=8*t**3*(15552*q*t**6+1296*q*t**4+864*t**4+48*q*t**2+84*t**2+5)
JN=s.expand(9*q*t**2*((U+Vm+Vp)**2+(q-1)*(Vm**2+Vp**2)))
F=s.expand((D1*D2).subs(u,4*t**2))
Et=s.expand(E.subs(u,t**2))
Kt=s.expand(K.subs(u,t**2))
H,r=s.div(s.Poly(s.expand(JN*F-N0*Kt),t),s.Poly(Et,t))
assert r.is_zero
Num=s.expand(N0*F+(z-1)*H.as_expr())
Den=s.expand(Et*F-(z-1)*Kt)
assert s.degree(Den,t)==22
# Nonzero exact resultant witness: full degrees survive, and gcd_t=1.
for a,b in [(2,3),(3,5),(5,2)]:
 n=s.Poly(Num.subs({q:a,z:b}),t);d=s.Poly(Den.subs({q:a,z:b}),t)
 assert n.degree()==s.degree(Num,t) and d.degree()==22
 assert s.gcd(n,d).degree()==0
assert s.cancel((N0/Et).subs(q,1)-48/(1-6*t))==0
print('ALL_CHECKS_PASS; generic reduced denominator degree 22; three coprimality witnesses')
