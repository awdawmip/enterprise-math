#!/usr/bin/env python3
"""PREFIX-431 independent algebra: rederive 2nd jets from original V(r,s,eta)."""
import sympy as S
R,T,E=S.symbols('r s eta',real=True)
x=S.symbols('x',real=True)
beta=S.Rational(1,10**6)
a=(T-R-1)/2
b=-S.sqrt(R-a*a)
J=(53+29*R)/2+39*a-4*b
A=36+28*a+12*b
B=-20-12*a+28*b
P=(245*(1+a)+123*b)/16
Q=(-123*(1+a)+245*b)/16
N=P*P+Q*Q
K=-E-S.Rational(709,64)*(T-2)-S.Rational(53,8)*beta
W=S.sqrt(N*beta-K*K)
V=J+(A*P+B*Q)*K/N+(A*Q-B*P)*W/N+16*beta
Z=S.sqrt(37577-64000000*x*x)
Ax=11776000000*x*x-263748000000*x-3419507
# The target expressions are independent from differentiation process.
Vs=-(Ax+(44932875-488000*x)*Z)/(9394250*Z)
Vse= -((23552000000*x-263748000000)/Z+Ax*64000000*x/Z**3-488000)/9394250
R2=(1507328000000000000*x**4
   -62464000000000*x**3*Z
   -66793472000000000000*x**3
   +363008000000000*x*x*Z
   -885013504000000*x*x
   +36675152000*x*Z
   +59038878088000000*x
   -213136744000*Z
   -439175052854126397)
Vss=-R2/(37577000*Z**3)
Vsr=-(7808000000*x*x+2944000*x*Z-694820000000*x-81180500*Z+4621971)/(37577000*Z)

def evalbase(expr):
    e=S.Rational(1,10**6)
    out=expr.subs({R:1,T:2,E:x-S.Rational(53,8)*e})
    return S.simplify(out)

quartic=512000000000000*x**4-30000000000000000*x**3+661230827328000000*x*x+11482077750000*x-252370368073811
assert S.expand(Ax**2-(44932875-488000*x)**2*(37577-64000000*x*x)-300616*quartic)==0
print('PASS primitive quartic elimination')
cases=[('V_s',S.diff(V,T),Vs),('V_s_eta',S.diff(V,T,E),Vse),
       ('V_ss',S.diff(V,T,2),Vss),('V_sr',S.diff(V,T,R),Vsr)]
for key,raw,formula in cases:
    rawbase=evalbase(raw)
    diff=S.simplify(S.radsimp(rawbase-formula))
    # Squared-radical/rational normal forms sometimes need one cancellation step.
    if diff!=0:
        diff=S.simplify(S.together(S.expand_power_base(diff,force=True)))
    assert diff==0,(key,diff)
    print('PASS',key)
print('PASS_PREFIX431_INDEPENDENT_GENERAL_V_DERIVATIVE_IDENTITIES')
