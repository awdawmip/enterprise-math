#!/usr/bin/env python3
"""Stage281-B: exact observer-optimal versus action-mass-optimal coins."""
from fractions import Fraction as F
from itertools import product


def coins(a, b, c, d, f1, f2):
    T = a+b+c+d
    x_action = ((a+c)*f1+(b+d)*f2)/T
    x_observer = (a*f1+d*f2)/(a+d)
    risk_opt = a*d*abs(f1-f2)/(a+d)
    def act(x):
        return max(abs(a*f1+b*f2-(a+b)*x),
                   abs(c*f1+d*f2-(c+d)*x))
    def obs(x):
        return max(a*abs(f1-x), d*abs(f2-x))
    assert obs(x_observer) == risk_opt
    assert act(x_action) <= act(x_observer)
    assert obs(x_observer) <= obs(x_action)
    assert x_action-x_observer == (c*d-a*b)*(f1-f2)/(T*(a+d))
    assert (x_action == x_observer) == (f1==f2 or a*b==c*d)
    for n in range(17):
        z=F(n,16)
        assert act(x_action) <= act(z)
        assert obs(x_observer) <= obs(z)
    return x_action,x_observer,obs(x_action),risk_opt


def main():
    k=0
    for a,b,c,d in product((F(1,8), F(1,4), F(3,8)),repeat=4):
        for f1,f2 in product((F(0),F(1)),repeat=2):
            coins(a,b,c,d,f1,f2)
            k+=1
    assert k==324
    sym=coins(F(1,4), F(1,8), F(1,8), F(1,4), F(1), F(0))
    assert sym[0]==sym[1]==F(1,2)
    strict=coins(F(1,4), F(1,8), F(1,8), F(1,8), F(1), F(0))
    assert strict==(F(3,5),F(2,3),F(1,10),F(1,12))
    print('EXACT_RATIONAL_COIN_CASES',k)
    print('SYMMETRIC_ACTION_OBSERVER_COIN',sym[0])
    print('STRICT_ACTION_COIN',strict[0],'OBSERVER_COIN',strict[1])
    print('STRICT_ACTION_COIN_RISK',strict[2],'OBSERVER_OPTIMUM',strict[3])
    print('STRICT_EXCESS_RISK',strict[2]-strict[3])
    print('STAGE281_BRC_OBSERVER_COIN_EXACT_PASS')


if __name__=='__main__':
    main()
