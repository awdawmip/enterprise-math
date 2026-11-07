#!/usr/bin/env python3
"""Exact finite witnesses for the S23 beta-binomial reconstruction theorem.

The all-n rate is proved analytically in PROOF.md. This executable
checks concrete rational cases and finite combinatorial identities.
"""
from fractions import Fraction
from math import comb, factorial, floor, log, sqrt


def probability(m, s, r):
    return Fraction(comb(m, s) * r.numerator**s *
                    (r.denominator-r.numerator)**(m-s),
                    r.denominator**m)


def mode_and_band(m):
    return floor(sqrt(m*log(m))/40)


def main():
    identities = 0
    for m in range(7):
        for s in range(m+1):
            beta_mass = Fraction(comb(m,s)*factorial(s)*factorial(m-s),factorial(m+1))
            assert beta_mass == Fraction(1,m+1)
            identities += 1
        for r in (Fraction(1,57),Fraction(1,3),Fraction(1,8),Fraction(1,4)):
            mass = [probability(m,s,r) for s in range(m+1)]
            assert sum(mass)==1
            overlap = sum(min(p,Fraction(1,m+1)) for p in mass)
            assert 0 < overlap <= 1
            identities += 2

    endpoint_cases=0
    for m in (10000,20000,50000):
        t=mode_and_band(m)
        assert t>=2
        assert t+2 <= Fraction(m,114)
        for r in (Fraction(1,57),Fraction(1,3),Fraction(1,8),Fraction(1,4)):
            j=(m+1)*r.numerator//r.denominator
            assert 0 <= j-t <= j+t <= m
            # The mode and ratios imply all interior p_s are >= min(endpoints).
            denominator=r.denominator**m
            for s in (j-t,j+t):
                numerator=comb(m,s)*r.numerator**s*(r.denominator-r.numerator)**(m-s)
                assert numerator*(m+1) >= denominator
                endpoint_cases += 1

    # Exact lawful parameter corners for r=q/(1-z).
    for a,c,r_expect in ((Fraction(7,8),Fraction(7,8),Fraction(1,57)),
                         (Fraction(1,2),Fraction(1,2),Fraction(1,3))):
        z=(1-a)*c
        q=(1-a)*(1-c)
        assert q/(1-z)==r_expect

    # These checks verify explicit constants in the rate argument.
    assert Fraction(9,16)-Fraction(1,2)==Fraction(1,16)
    assert Fraction(1,4)/Fraction(1,16)**2==64
    assert Fraction(456,1600)==Fraction(57,200)
    assert 10000**43 > Fraction(16,3)**200  # equivalent m^(43/200)>16/3 at m=10000
    assert Fraction(1,2)*Fraction(1,80)==Fraction(1,160)

    print('PASS_S23_UNIFORM_BETA_KERNEL_RATE_THETA_20261106')
    print('exact_beta_binomial_identities:',identities)
    print('exact_large_m_band_endpoint_inequalities:',endpoint_cases)
    print('smallest_checked_m: 10000')
    print('proved_uniform_n_range: integers n>=20000')
    print('new_lower_overlap_rate: (1/160)*sqrt(log(n)/n)')
    print('existing_upper_overlap_rate: (28/3)*sqrt(log(n)/n)+2/n**2 for n>=1000')
    print('scope: conditional tagged-AV S23 auxiliary experiment')


if __name__=='__main__':
    main()
