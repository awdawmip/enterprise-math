#!/usr/bin/env python3
"""Author-side EC49FTN regression for the exact analytic prior-tilt theorem.
Parent native 228-query Bellman solver is not rerun here.
Uses Fraction for breakpoint geometry, double arithmetic for independent numeric probes.
"""
from fractions import Fraction as F
from math import exp, expm1, log1p, isclose

A0,A1=F(3,4),F(49,64)
B0,B1=F(7,16),F(57,128)
m0,m1,m2,m3=(F(11457,512),F(1461,64),F(1469,64),F(187,8))

def P(t, x, y):
    x,y=float(x),float(y)
    if abs(t)<1e-12: return y-x
    return exp(t*x)*expm1(t*(y-x))/t

def G(t, d):
    if abs(t)<1e-12: return d
    return expm1(t*d)/t

def L_and_U(m):
    m=F(m)
    if m < m1: L=(4*m+2647)/3696
    else: L=(8*m+173)/480
    U=(64*m+1411)/3840 if m < m2 else F(3,4)
    return float(L),float(U)

def clip_weight(m, lam, mu):
    if m <= m2:return 0.0
    if m>=m3:return 1.0
    b0=float((47-m)/54)
    ac=float(F(740,945)-m/945)
    d=float(A1)-ac
    L,U=L_and_U(m)
    k=44*lam/45+10*mu/9
    clip=35*G(lam,d)
    cont=32*G(-k,U-L)
    return clip/(clip+cont)

def q(m,u,lam,mu):
    L,U=L_and_U(m)
    p=clip_weight(m,lam,mu)
    if u >=1-p:return U
    t=u/(1-p)
    k=44*lam/45+10*mu/9
    if abs(k)<1e-12:return L+t*(U-L)
    return L+log1p(k*t*G(k,U-L))/k

def moment1(t,x,y):
    x,y=float(x),float(y)
    if abs(t)<1e-12:return (y*y-x*x)/2
    return (y*exp(t*y)-x*exp(t*x))/t - P(t,x,y)/t

def clip_mass(lam,mu):
    phi_b=P(mu,B0,B1)
    if abs(lam)<1e-12:
        numerator=(float(A1)-77/105)*phi_b - 2/35*moment1(mu,B0,B1)
    else:
        numerator=(exp(lam*float(A1))*phi_b - exp(lam*77/105)*P(mu+2*lam/35,B0,B1))/lam
    return numerator/(P(lam,A0,A1)*phi_b)

def simpson(f,x,y,n=500):
    h=(y-x)/n
    return h/3*(f(x)+f(y)+sum((4 if k%2 else 2)*f(x+k*h) for k in range(1,n)))

assert m0<m1<m2<m3
for m in (m0,m1,m2,m3):
    L,U=L_and_U(m)
    assert L<=U and float(F(11,16))<=L<=float(F(3,4)) and U<=float(F(3,4))
assert (A1-A0)*(B1-B0)==F(1,8192)
# The clipping area is exactly a fraction of the source rectangle.
num=(A1-F(77,105))*(B1-B0)-F(2,35)*(B1*B1-B0*B0)/2
assert num/((A1-A0)*(B1-B0))==F(19,42)
assert isclose(clip_mass(0,0),float(F(19,42)),abs_tol=1e-11)

pairs=[(0,0),(8,0),(-8,4),(12,-5),(3,-2.64),(0,9),(-12,-12)]
for lam,mu in pairs:
    # Two genuinely different routes for clipping probability: analytic exp-integrals vs Simpson.
    denom=P(lam,A0,A1)*P(mu,B0,B1)
    b_clip=lambda b: exp(mu*b)*P(lam,(77+6*b)/105,A1)
    alt=simpson(b_clip,float(B0),float(B1))/denom
    ana=clip_mass(lam,mu)
    assert abs(ana-alt)<2e-10,(lam,mu,ana,alt)
    # Interior conditional law: same exponential tilt k in every m fiber.
    ms=[]
    for lo,hi in ((m0,m1),(m1,m2),(m2,m3)):
        ms += [lo+(hi-lo)*F(i,101) for i in range(1,101)]
    for u in [i/33 for i in range(1,33)]:
        prev=-1e9
        for m in ms:
            now=q(m,u,lam,mu)
            assert now>=prev-1e-12,(lam,mu,m,u,now,prev)
            prev=now
    # p strictly increasing through upper component, including the atom at the upper endpoint.
    upper=[m2+(m3-m2)*F(i,101) for i in range(1,101)]
    ps=[clip_weight(m,lam,mu) for m in upper]
    assert all(ps[i]<ps[i+1] for i in range(len(ps)-1))
    print(f'lambda={lam:+g}, mu={mu:+g}, kappa={44*lam/45+10*mu/9:+.8f}, clip={ana:.12f}, quantile_tests={len(ms)*32}, upper_p_tests={len(ps)-1}')

# Exact uniform-case endpoint recheck, from independent simple rational formula.
d= A1-(F(740,945)-m2/945)
T=F(3,4)-(8*m2+173)/480
assert 35*d/(35*d+32*T)==F(115,223)
print('PASS: exact geometry and 19/42, 115/223 endpoints; 7 tilted priors; 67200 quantile checks; 693 p comparisons; 7 independent integration comparisons')
