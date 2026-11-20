#!/usr/bin/env python3
"""EC49FUR: exact rational certificates for an all-n first mixed phase.

Universal n>=15 inequalities are proved symbolically in the companion note;
this script certifies their rational constant comparisons, the n=15,16
base witnesses, and selected finite primal/dual saddle witnesses.
"""
from fractions import Fraction as Q
from math import comb

beta = Q(3, 637)
theta_E = Q(31597745, 1653649)
a = Q(21829245984, 45529434409)
b = Q(21829245984) / (Q(45529434409) - Q(456083905)*theta_E)
d = beta*(theta_E-1)
c = beta*theta_E

def T(x,t):
    return (1-x)*(1-beta*x+beta*x*t)

def masses(n,x,t):
    u=Q(21829245984)/(Q(45529434409)-Q(456083905)*t)
    tt=T(x,t);p,q=1-tt,1-u*tt
    assert 0 <= p < q <= 1
    return [Q(comb(n,k))*(q**k*(1-q)**(n-k)-p**k*(1-p)**(n-k))
            for k in range(n+1)]

def verify_rational_witness(n,x):
    tt0,tte=T(x,Q(0)),T(x,theta_E)
    A0,AE=tt0**n*(1-a**n),tte**n*(1-b**n)
    assert A0 < AE                           # x_s(n) < x
    assert tte > (1-b**(n-1))/(1-b**n)    # x < x_B,E(n)
    z,e=masses(n,x,Q(0)),masses(n,x,theta_E)
    assert z[1] < 0 < e[1]
    a0,ae=sum(z[2:],Q(0)),sum(e[2:],Q(0))
    gamma=(ae-a0)/(z[1]-e[1])
    lam=-z[1]/(e[1]-z[1])
    assert 0 < gamma < 1 and 0 < lam < 1
    D0=a0+gamma*z[1]
    DE=ae+gamma*e[1]
    assert D0 == DE
    dual=[(1-lam)*z[k]+lam*e[k] for k in range(n+1)]
    assert dual[0]<0 and dual[1]==0 and all(v>0 for v in dual[2:])
    assert sum(dual[2:],Q(0))+gamma*dual[1] == D0
    # Compare against all count-threshold candidates at this rational width.
    for j in range(n+1):
        zz=sum(z[j+1:],Q(0));ee=sum(e[j+1:],Q(0))
        opts=[Q(0),Q(1)]
        if z[j]!=e[j]:
            g=(ee-zz)/(z[j]-e[j])
            if 0 < g < 1: opts.append(g)
        for g in opts:
            assert min(zz+g*z[j],ee+g*e[j])<=D0
    return gamma,lam,(1-D0)/2

def main():
    assert Q(47,100)<a<Q(1,2)
    assert Q(59,100)<b<Q(3,5)
    assert b/a>Q(6,5)
    assert Q(89,1000)<c
    assert d<Q(43,500) and beta<Q(1,200)
    assert b/(c*(1-b))<17
    assert Q(6,5)**15>Q(40*15,47)
    assert Q(5,6)**15<Q(1,2)
    # Exact bridges for n=15,16: x_s < rational witness < x_B,E.
    for n,x in [(15,Q(1,3500)),(16,Q(1,6000))]:
        t0,te=T(x,Q(0)),T(x,theta_E)
        assert te**n*(1-b**n)>t0**n*(1-a**n)
        assert te>(1-b**(n-1))/(1-b**n)
    for n,x in [(15,Q(1,3500)),(16,Q(1,6000)),
                (17,Q(1,10000)),(18,Q(1,18000)),(20,Q(1,50000))]:
        gamma,lam,risk=verify_rational_witness(n,x)
        print(f'n={n} x={x} gamma={float(gamma):.12f} '
              f'lambda_E={float(lam):.12f} risk={float(risk):.12f}')
    print('PASS: rational constants, n=15/16 bridges and five exact mixed saddles')

if __name__=='__main__': main()
