#!/usr/bin/env python3
"""Exact Fraction certificate for n=15, x=7/25000 composite minimax.

Analytic concavity and matching two-point Bayes proof are in the paired .md.
No floating-point operations determine signs; no nonstdlib dependencies.
"""
from fractions import Fraction as F
from math import comb
E=F(1048576,18958647)
a=F(2807259,163840)
beta=F(3,637)
C,B,H=21829245984,-456083905,45529434409
x=F(7,25000);n=15
TE=1/(1-a*E)
def T(t):return (1-x)*(1-beta*x+beta*x*t)
def u(t):return F(C)/(H+B*t)
def Dj(j,t):return T(t)**j*(1-u(t)**j)
def countmass(k,t):
 p=1-T(t);r=1-T(t)*u(t)
 return comb(n,k)*(r**k*(1-r)**(n-k)-p**k*(1-p)**(n-k))
def D2(t):return 15*Dj(14,t)-14*Dj(15,t)

dE,dI=countmass(1,TE),countmass(1,F(0))
DE,DI=Dj(15,TE),Dj(15,F(0))
assert dE>0 and dI<0 and DE>DI
assert all(countmass(0,t)<0 and countmass(2,t)>0 for t in [F(0),TE])
assert all(countmass(k,t)>0 for t in [F(0),TE] for k in range(2,16))
assert all(D2(t)==sum(countmass(k,t) for k in range(2,16)) for t in [F(0),TE])
alpha=1-(DE-DI)/(dE-dI)
lambdaE=-dI/(dE-dI)
assert F(14,15)<alpha<1 and 0<lambdaE<1
assert lambdaE*dE+(1-lambdaE)*dI==0
def Dalpha(t):return (15*alpha-14)*Dj(15,t)+15*(1-alpha)*Dj(14,t)
assert Dalpha(TE)==Dalpha(F(0))

# Exact global sufficient concavity inequalities for Dj, j=14 and 15.
assert beta*x/(1-beta*x)<F(1,500000)
assert F(C,H)>F(2,5)
assert F(-B,H)>F(1,100)
assert F(2,5)**8/F(100)>F(1,500000)

risk=(1-Dalpha(F(0)))/2
print("PASS exact endpoint mixed-Bayes signs and equalizing alpha")
print("PASS global nuisance concavity bounds for j=14 and 15")
print("alpha",float(alpha),"lambda_E",float(lambdaE))
print("minimax_risk",float(risk))
print("endpoint_Bayes_risk",float((1-DE)/2))
