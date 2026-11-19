#!/usr/bin/env python3
"""EC49FUI: exact rational verifier of global n=15 failure-window minimax.
The real-interval proof is in the companion theorem. Python stdlib only.
"""
from fractions import Fraction as F
from math import comb

n=15
E=F(1048576,18958647)
a=F(2807259,163840)
beta=F(3,637)
eta=F(141024,1653649)
C=F(21829245984)
H=F(45529434409)
B=F(-456083905)
thetaE=1/(1-a*E)
uE=F(4822040484,8132285009)
uI=C/H
root_l,root_u=F(2797,10**7),F(2798,10**7)
bayes_l,bayes_u=F(2956,10**7),F(2957,10**7)

def T(x,th):return (1-x)*(1-beta*x+beta*x*th)
def u(th):return C/(H+B*th)
def F_j(j,x,th):return T(x,th)**j*(1-u(th)**j)
def d1(x,th):
    v=T(x,th);z=u(th)
    return n*v**(n-1)*(z**(n-1)*(1-v*z)-(1-v))
def D2(x,th):return n*F_j(n-1,x,th)-(n-1)*F_j(n,x,th)
def mass(k,x,th):
    p=1-T(x,th);r=1-T(x,th)*u(th)
    return comb(n,k)*(r**k*(1-r)**(n-k)-p**k*(1-p)**(n-k))

assert u(thetaE)==uE and u(F(0))==uI
assert T(F(1,3500),thetaE)==(1-F(1,3500))*(1+eta*F(1,3500))
assert F(0)<uI<F(1,2) and F(2,5)<uI<uE<F(1)
assert F(0)<root_l<root_u<bayes_l<bayes_u<F(3,10000)

# Prior EC49FUH certified algebraic endpoints. Recheck exact rational brackets.
def first_gap(x):return F_j(n,x,thetaE)-F_j(n,x,F(0))
assert first_gap(root_l)<0<first_gap(root_u)
assert mass(1,bayes_l,thetaE)>0>mass(1,bayes_u,thetaE)

# Uniform rational estimates valid on x15 < x < x_B.
assert F(0)<eta<F(1,10) and F(0)<beta<F(1,200)
assert (1+F(3,100000))**14<F(101,100)
assert n*(F(1,10)*F(101,100)+F(1,200))<2
assert 2*(bayes_u-root_l)==F(1,31250)<F(1,30000)
assert (F(2999,3000))**14>F(99,100)
assert n*F(99,100)*(root_l-F(1,2**14))>F(1,400)
assert 1-F(1,30000)/F(1,400)==F(74,75)>F(14,15)

# Continuous-coordinate strict concavity: F_14'' and F_15'' negative.
assert beta*F(3,10000)/(1-beta*F(3,10000))<F(1,500000)
assert -B/H>F(1,100)
assert (F(2,5)**8)/100>F(1,500000)
# At theta=0, signed mass for k>=2 is positive throughout the interval:
assert 1500**2*(F(2,5)**13)>1
assert F(1,2)*3000==1500

# Five rational widths verify exact saddlepoint identities and finite-nuisance checks.
widths=[F(2799,10**7),F(7,25000),F(1,3500),F(29,100000),F(739,2500000)]
for x in widths:
    assert root_u<x<bayes_u
    AE=F_j(n,x,thetaE);AI=F_j(n,x,F(0))
    de=d1(x,thetaE);di=d1(x,F(0))
    assert AE>AI and de>0>di
    alpha=1-(AE-AI)/(de-di)
    lam=-di/(de-di)
    assert F(74,75)<alpha<1 and F(0)<lam<1
    assert all(mass(k,x,thetaE)>0 for k in range(1,n+1))
    assert all(mass(k,x,F(0))>0 for k in range(2,n+1))
    assert all(mass(0,x,th)<0 for th in (F(0),thetaE))
    assert mass(1,x,thetaE)==de and mass(1,x,F(0))==di
    assert D2(x,thetaE)==sum(mass(k,x,thetaE) for k in range(2,n+1))
    assert lam*de+(1-lam)*di==0
    def Da(th):return (n*alpha-(n-1))*F_j(n,x,th)+n*(1-alpha)*F_j(n-1,x,th)
    assert Da(F(0))==Da(thetaE)
    assert Da(thetaE)==AE-(1-alpha)*de
    assert Da(thetaE)==lam*D2(x,thetaE)+(1-lam)*D2(x,F(0))
    for th in (thetaE/10,thetaE/2,thetaE*F(9,10)):
        assert Da(th)>Da(F(0))
    R=(1-Da(F(0)))/2
    print('PASS x=',x,'alpha~',format(float(alpha),'.15f'),
          'lambda_E~',format(float(lam),'.15f'),
          'R*~',format(float(R),'.15f'))
print('PASS EC49FUI: exact endpoint brackets, uniform inequalities and 5 rational spot identities')
print('Real width-continuum and all finite nuisance: analytic strict-concavity + mixed-Bayes proof in companion theorem')
