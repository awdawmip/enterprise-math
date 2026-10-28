"""Exact integer/binomial checks of GH-19, not formal/native authentication."""
from math import comb
from gh17_18_clausen_gauss_check import primes, F_coeff, value


def coeff_q(m):
    # Coefficients of (1+t)^3(1+9t), and square-plus-cube normal form.
    return [1, 12, 30, 28, 9]


def check(limit=1000):
    cases = 0
    for p in primes(limit):
        m = (p-3)//8
        binom_denom = comb(3*m+1, m)
        assert binom_denom % p != 0
        b = sum(comb(3*m+1, m-r) * comb(m,r) * pow(9,r,p)
                for r in range(m+1)) % p
        f = value(F_coeff(p), 9, p)
        assert b == binom_denom*f % p
        cases += 1
    sq = [1,6,-3]
    q = [sum(sq[i]*sq[j] for i in range(3) for j in range(3) if i+j==k) + (64 if k==3 else 0) for k in range(5)]
    assert q == coeff_q(11)
    m = 11
    b11 = sum(comb(3*m+1,m-r)*comb(m,r)*9**r for r in range(m+1))
    assert b11 % (8*m+3) == 13
    print('PASS_GH19_BINOMIAL_NORMALIZATION_QUARTIC_IDENTITY_COMPOSITE_COUNTEREXAMPLE')
    print('exact primes checked:',cases,'range p<',limit)
    print('composite m=11: B_11 mod 91 =',b11%91)


if __name__ == '__main__':
    check()
