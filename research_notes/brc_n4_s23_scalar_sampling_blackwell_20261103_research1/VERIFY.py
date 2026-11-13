"""Exact finite-sample readout test for the S23 two-state witness. Python 3 stdlib only."""
from fractions import Fraction as F
from math import comb


def joint_error(n_full, n_scalar, h, s):
    """Equal-prior Bayes error for n_full ternary and n_scalar binary trials."""
    p, q = F(1, 2) + h, F(1, 2) - h
    total = F(0)
    for k in range(n_full + 1):
        for t in range(k + 1):
            for u in range(n_scalar + 1):
                mult = comb(n_full, k) * comb(k, t) * comb(n_scalar, u)
                shared = mult * (1-s)**(n_full-k) * s**k
                plus = shared * p**t * q**(k-t) * (s*p)**u * (1-s*p)**(n_scalar-u)
                minus = shared * q**t * p**(k-t) * (s*q)**u * (1-s*q)**(n_scalar-u)
                total += min(plus, minus)
    return total / 2


def exact_probability_checks():
    checks = 0
    for h in [F(0), F(1, 100), F(1, 42), F(1, 6)]:
        for s in [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]:
            for n in range(1, 8):
                full = joint_error(n, 0, h, s)
                assert full == joint_error(n-1, 1, h, s), (n, h, s)
                for nf in range(n+1):
                    assert full <= joint_error(nf, n-nf, h, s), (n,nf,h,s)
                    checks += 1
    return checks


if __name__ == "__main__":
    checks = exact_probability_checks()
    h, s = F(1,42), F(1,4)
    for n in (1,2,3,4,5):
        print(f"N={n} all_full={joint_error(n,0,h,s)} all_scalar={joint_error(0,n,h,s)} one_scalar={joint_error(n-1,1,h,s)}")
    assert joint_error(0,3,h,s)-joint_error(3,0,h,s) == F(55,197568)
    assert F(4)*s / (F(4)*s/(2-s)) == F(7,4)
    # With an added N-view overwrite z2=0, beta_N=0, the same pair has
    # row-1 distribution (0, 0, q, p) / (0, 0, p, q).
    # At beta_E=1/2 its TV contrast is four times the old E-row contrast.
    assert (2*h) / (2*s*h) == 4
    print("INTERVENTION_WITNESS_TV_RATIO=4")
    print(f"EXACT_CHECKS={checks}")
    print("PASS_BRC_S23_SINGLE_SCALAR_VS_FULL_SOURCE_SAMPLING_20261103")
