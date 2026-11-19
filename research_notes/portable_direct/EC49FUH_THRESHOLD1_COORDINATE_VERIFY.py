#!/usr/bin/env python3
"""EC49FUH exact Fraction checks; no floating-point decisions or dependencies.

Universal concavity proof is in EC49FUH_THRESHOLD1_COORDINATE_THEOREM.md;
this program verifies rational identities, model transformations, isolation intervals
and strict witness signs.
"""
from fractions import Fraction as F

E=F(1048576,18958647)
m,L,U=F(1469,64),F(951,1280),F(3,4)
a=m*(L+U)/2
c1=m*(U-L)/2
beta=c1/a
B0,B1,Q0,Q1=2630615040,45529434409,2359296,41217719
C=B1-575*Q1
B=a*B0-B1
Acoeff=a*(B0-575*Q0)-C
assert a==F(2807259,163840)
assert c1==F(13221,163840)
assert beta==F(3,637)
assert B==-456083905 and C==21829245984 and Acoeff==0
assert a*E<1

def theta(e):return 1/(1-a*e)
def p(e,x):return x*(1-e*(m*U-c1*x))/(1-e*a)
def q(e):return F(575)*(Q1*e-Q0)/(B1*e-B0)
def u(e):return 1-q(e)
def D(e,n,x):return (1-p(e,x))**n*(1-u(e)**n)
def Dc(n,x,t):
 return (1-x)**n*(1-beta*x+beta*x*t)**n*(1-(F(C)/(B1+B*t))**n)

for ee in [E,F(0),F(-1),F(-100),F(-100000)]:
 t=theta(ee)
 assert u(ee)==F(C)/(B1+B*t)
 assert 0<u(ee)<1
 for xx in [F(1,3500),F(7,25000),F(1,2),F(99,100)]:
  assert 0<p(ee,xx)<1
  assert 1-p(ee,xx)==(1-xx)*(1-beta*xx+beta*xx*t)
  for n in [1,2,15,17,31]:
   assert D(ee,n,xx)==Dc(n,xx,t)

uinf=F(C,B1)
uE=F(4822040484,8132285009)
qE=1-uE
assert u(E)==uE
eta=E*c1/(1-E*a)
assert eta==F(141024,1653649)
def Dinf(n,xx):
 return (1-xx)**n*(1-beta*xx)**n*(1-uinf**n)

n=15
lo,hi=F(2797,10**7),F(2798,10**7)
assert Dinf(n,lo)>D(E,n,lo)
assert Dinf(n,hi)<D(E,n,hi)
pBayes=qE*uE**(n-1)/(1-uE**n)
def pE(xx):return (F(1512625)*xx+F(141024)*xx*xx)/F(1653649)
bl,bh=F(2956,10**7),F(2957,10**7)
assert pE(bl)<pBayes<pE(bh)
assert hi<bl
witness=F(7,25000)
assert hi<witness<bl
assert Dinf(n,witness)<D(E,n,witness)
pw=p(E,witness)
rw=pw+qE*(1-pw)
assert rw*uE**(n-1)>pw
for k in range(1,n+1):
 assert rw**k*(1-rw)**(n-k)>pw**k*(1-pw)**(n-k)
assert (1-rw)**n<(1-pw)**n

print("PASS: exact reciprocal-coordinate cancellation and rational model identities")
print("PASS: x_crit in (2797/10^7,2798/10^7); x_Bayes in (2956/10^7,2957/10^7)")
print("PASS: unique endpoint Bayes K>=1 at x=7/25000 and Dinf<D_E")
print("endpoint-composite-risk lower-bound gap at rational witness:",
      float((D(E,n,witness)-Dinf(n,witness))/2))
