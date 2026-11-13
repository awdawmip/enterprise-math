"""Check depth-two block formulas against the original three-state kernel.

The analytic density theorem does not depend on floating-point data. This file
checks exact identities and records coarse, reproducible error brackets.
"""
from argparse import ArgumentParser
from fractions import Fraction as Q
from functools import cache
from math import comb, gamma, lgamma, exp
from pathlib import Path
import json
import sys


@cache
def block(k, initial, final):
    rho = Q(k + 4*final, k + final)
    tau = Q(28*(k + 4*final)*(k - 1 + 4*final),
            (4*k + final)*(k - 1 + final))
    for n in range(final + 1, initial + 1):
        rho *= Q(k + 4*n, 4*(k + n))
        tau *= Q(k + 4*n, 4*(4*k + n))
    return rho, tau


def gamma_block(k, initial, final):
    def ratio(a, b):
        return exp(lgamma(initial + 1 + a) - lgamma(initial + 1 + b)
                   - lgamma(final + 1 + a) + lgamma(final + 1 + b))
    rho = (k + 4*final)/(k + final) * ratio(k/4, k)
    tau = (28*(k + 4*final)*(k - 1 + 4*final)
           / ((4*k + final)*(k - 1 + final)) * ratio(k/4, 4*k))
    return rho, tau


def tail(stock, y):
    p = Q(840, (stock+2)*(stock+3)*(stock+4))
    a = (Q(3,32), Q(3,2), Q(6))
    b = (Q(15,32), Q(15,8), Q(3))
    return [y*(p*a_j+b_j)/(1+p*y*a_j) for a_j,b_j in zip(a,b)]


def propagate(points, parameters):
    rho, tau = parameters
    return [(rho+tau*t)/(1+tau*t) for t in points]


def inside(c, v, w):
    """Strict open comparability conditions without taking any roots."""
    return 4**4*v**15 < c**15 and 40**4*w**9 > 11**4*v**9 and w < v


def count_open(c):
    smallest = 0
    count = 0
    for v in range(2, c+1):
        if 4**4*v**15 >= c**15:
            break
        smallest = max(smallest,2)
        while smallest < v and 40**4*smallest**9 <= 11**4*v**9:
            smallest += 1
        count += v-smallest
    return count


def run(prior):
    sys.path.insert(0, str(prior.resolve()))
    from mixed_kernel import responses
    checks = 0
    for c in range(2,13):
        for v in range(2,c+1):
            for w in range(2,v+1):
                y = Q(1)
                for i in range(3,w+1):
                    y *= Q(4*i+1,4*i+4)
                points = propagate(propagate(tail(w,y), block(3,v,w)), block(5,c,v))
                rows,_ = responses(2,c,(c-v,v-w,w-2))
                native = [(7*rows[0][j]+rows[1][j])/(7*rows[0][j]+rows[2][j])
                          for j in range(3,6)]
                assert native==points
                for k,i,f in ((3,v,w),(5,c,v)):
                    assert all(abs(float(a)-b)<1e-10 for a,b in zip(block(k,i,f),gamma_block(k,i,f)))
                checks += 1
    b = Q(7,16)
    n = Q(11,10)
    # e^x <= 1/(1-x), for 0<=x<1.
    assert 1/(1-b*n)<2
    assert 2**3*Q(14,17)**14*Q(3,17)**3 < n**14*(n-1)**3
    counts={}
    for c in (10,100,1000,10000,100000):
        count = count_open(c)
        if c<=100:
            assert count==sum(inside(c,v,w) for v in range(2,c+1) for w in range(2,v+1))
        counts[c] = dict(region_words=count,all_words=comb(c,2))
    examples = []
    L = gamma(4)/gamma(3.25)
    for s_n,u_n in ((10,8),(15,10),(17,14)):
        s,u=s_n/20,u_n/20
        A,D = 4*s**3.75, 4*(u/s)**2.25
        B,E = 7*A**5/16, 7*D**5/16
        center, width = (A+B*D)/(1+B*D), B*E*abs(1-A)*abs(1-D)*u**(-.75)/(1+B*D)**2
        for c in (10**4,10**6):
            v,w = c*s_n//20,c*u_n//20
            y = L*exp(lgamma(w+1.25)-lgamma(w+2))
            z = propagate(propagate(tail(w,y), gamma_block(3,v,w)),gamma_block(5,c,v))
            calculated = ((max(z)+min(z))/2, c**.75*(max(z)-min(z))/(L*81/32))
            errors = (abs(calculated[0]-center)/center,abs(calculated[1]-width)/width)
            # Count stable binary digits of relative agreement by coarse thresholds.
            errors_below = [next(k for k in range(30,-1,-1) if e<2**(-k)) for e in errors]
            examples.append(dict(c=c,v=v,w=w,relative_errors_below_binary_powers=errors_below))
    return dict(complete_native_words=checks, native_columns=3*checks,
                region_grid_counts=counts,asymptotic_controls=examples)


if __name__=='__main__':
    p = ArgumentParser(description=__doc__)
    p.add_argument('--prior',type=Path, required=True,help='C67/joint directory')
    print(json.dumps(run(p.parse_args().prior),indent=2))
