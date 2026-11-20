#!/usr/bin/env python3
"""Exact rational certificates for a 2-point saddle in the frozen EC49 binary observer.
Parent EC49FUI proves the continuum nuisance minimization for the sample width.
This checker establishes only the algebraic saddle equations and finite crosschecks.
"""
from fractions import Fraction as Q
from math import comb
BETA=Q(3,637)
THETA_E=Q(31597745,1653649)
C=Q(21829245984)
H=Q(45529434409)
B=Q(456083905)

def pq(theta,x):
    t=(1-x)*(1-BETA*x+BETA*x*theta)
    u=C/(H-B*theta)
    return 1-t,1-u*t

def b(n,z,k):
    return comb(n,k)*z**k*(1-z)**(n-k)

def diff(n,theta,x,k):
    p,q=pq(theta,x)
    return b(n,q,k)-b(n,p,k)

def atleastone(n,theta,x):
    p,q=pq(theta,x)
    return (1-p)**n-(1-q)**n

def witness(n=15,x=Q(7,25000)):
    a0=atleastone(n,Q(0),x); ae=atleastone(n,THETA_E,x)
    d0=diff(n,Q(0),x,1); de=diff(n,THETA_E,x,1)
    alpha=1-(ae-a0)/(de-d0)
    lam=-d0/(de-d0)
    assert d0<0<de and Q(0)<alpha<1 and Q(0)<lam<1
    def D(theta):
        return atleastone(n,theta,x)-(1-alpha)*diff(n,theta,x,1)
    assert D(Q(0)) == D(THETA_E)
    assert lam*de+(1-lam)*d0==0
    # 2-point mixture of signed count masses has a Bayes-threshold sign pattern.
    mix=[lam*diff(n,THETA_E,x,k)+(1-lam)*diff(n,Q(0),x,k) for k in range(n+1)]
    assert mix[1]==0
    assert mix[0]<0 and all(m>0 for m in mix[2:])
    # Finite checks of min over theta; full continuum inequality is cited from EC49FUI.
    for i in range(1001):
        theta=THETA_E*Q(i,1000)
        assert D(theta)>=D(Q(0))
    print('PASS: endpoint equality, zero mixed k=1 density, 1001 nuisance mesh checks')
    print('n=',n,' x=',x,' alpha≈',float(alpha),' least_favorable_weight_thetaE≈',float(lam))
    print('minimax_error≈',float((1-D(Q(0)))/2))
    print('alpha numerator/denominator digits=',len(str(alpha.numerator)),len(str(alpha.denominator)))
    return alpha,lam

if __name__=='__main__': witness()
