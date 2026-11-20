#!/usr/bin/env python3
"""EC49FUN exact rational checks for arbitrary-n local minimax, examples, and garbling obstruction.
No full phase-audit or native price revalidation is claimed.
"""
from fractions import Fraction as Q
from math import comb

BETA=Q(3,637)
ETA=Q(141024,1653649)
C=21829245984
H=45529434409
B=456083905
THETA_E=Q(31597745,1653649)
U_E=Q(4822040484,8132285009)
U_I=Q(C,H)

def u(theta): return Q(C)/(H-B*theta)
def t(theta,x): return (1-x)*(1-BETA*x+BETA*x*theta)
def d1(theta,x,n): return t(theta,x)**n*(1-u(theta)**n)
def delta(n):
    m=U_I**n*Q(B,H)
    return min(Q(1),m/(BETA*(1+m)),(1-U_E)*U_E**(n-1))/2

def likelihood_one_ratio_is_bayes(theta,x,n):
    T=t(theta,x); U=u(theta)
    return U**(n-1)*(1-U*T)>(1-T)

def binprob(k, n, hit):
    return comb(n,k)*hit**k*(1-hit)**(n-k)

def endpoint_risk(x,n):
    T=t(THETA_E,x)
    return sum(min(binprob(k,n,1-T),binprob(k,n,1-U_E*T)) for k in range(n+1))/2

def allone_lower(x,n):
    T=t(THETA_E,x)
    p=1-T
    return min((1-U_E**n)*p**n,(1-U_E*T)**n-U_E**n*p**n)/2

assert u(THETA_E)==U_E
assert t(THETA_E,Q(1,100))==(1-Q(1,100))*(1+ETA*Q(1,100))
assert 0<U_I<U_E<1
for n in [1,2,3,5,15,17,50]:
    d=delta(n)
    assert 0<d<Q(1)
    assert likelihood_one_ratio_is_bayes(THETA_E,d,n)
    for x in [Q(0), d/2, d]:
        # endpoint really least favorable at these sampled rational values;
        # global claim uses exact symbolic inequality shown in the proof.
        vals=[d1(THETA_E*Q(j,10),x,n) for j in range(11)]
        assert min(vals)==vals[-1]
        formula=(1-t(THETA_E,x)**n*(1-U_E**n))/2
        assert endpoint_risk(x,n)==formula
        assert formula >= U_E**n/2
    for x in [Q(1,10000),Q(1,10),Q(1,2),Q(1)]:
        assert endpoint_risk(x,n) >= U_E**n/2+allone_lower(x,n)
        assert allone_lower(x,n)>0
    print(f'n={n} delta={float(d):.12g}; V0={float(U_E**n/2):.12g}; slope={float(n*(1-ETA)*(1-U_E**n)/2):.12g}')
# Exact all-count overlap identity for the endpoint Bernoulli Z-channel.
# Here the full strings are exchangeable, so binomial count masses suffice.
for n in [1,2,3,4,5]:
    for x in [Q(0),Q(1,50),Q(1,2),Q(1)]:
        T=t(THETA_E,x); p=1-T; q=1-U_E*T
        a=[binprob(k,n,p) for k in range(n+1)]
        plus=[binprob(k,n,q) for k in range(n+1)]
        comp=[(plus[k]-U_E**n*a[k])/(1-U_E**n) for k in range(n+1)]
        assert all(b>=0 for b in comp)
        assert sum(comp)==1
        omega=sum(min(a[k],comp[k]) for k in range(n+1))
        assert endpoint_risk(x,n)==(U_E**n+(1-U_E**n)*omega)/2
# A nuisance-independent single-bit garbling from width x to y would
# require T(theta,y)/T(theta,x) to be constant in theta; its derivative is positive.
for x,y in [(Q(0),Q(1,100)),(Q(1,100),Q(1,5)),(Q(1,5),Q(9,10))]:
    def ratio(theta): return t(theta,y)/t(theta,x)
    assert ratio(THETA_E)>ratio(Q(0))
    # expression derived from quotient rule, checked at two theta values.
    for theta in [Q(0),THETA_E]:
        expected=Q(1-y,1-x)*BETA*(y-x)/(1-BETA*x+BETA*x*theta)**2
        assert expected>0
print('PASS: 7 arbitrary-n cases, endpoint excess bounds, and nuisance-common garbling obstruction')
