#!/usr/bin/env python3
"""EC49FUE: exact, self-contained rational certificate for n=17 composite-risk separation.

Scientific input: BRC16943 frozen @fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Parent formulas: EC49FUD @26da0d004d175bff1ff99a7aa8e94bf029349039.
No floating-point computation is used for assertions.
"""
from fractions import Fraction as F
from math import comb

M = F(1469, 64)
L = F(951, 1280)
U = F(3, 4)
W = U - L
E = F(1048576, 18958647)
E_ALT = F(-1)
X = F(5, 123)
N = 17
MIX_ALT = F(1, 125)


def q(e):
    return F(575) * (41217719 * e - 2359296) / (
        45529434409 * e - 2630615040
    )


def p(e):
    return X * (1 - e * M * (U - X * W / 2)) / (
        1 - e * M * (L + U) / 2
    )


def r(e):
    pe = p(e)
    return pe + q(e) * (1 - pe)


def binomial_mass(k, y):
    return F(comb(N, k)) * y ** k * (1 - y) ** (N - k)


def signed_mass(e, k):
    return binomial_mass(k, r(e)) - binomial_mass(k, p(e))


def threshold_advantage(e, threshold=3):
    return sum((signed_mass(e, k) for k in range(threshold, N + 1)), F(0))


def mixed_signed_mass(k):
    return (1 - MIX_ALT) * signed_mass(E, k) + MIX_ALT * signed_mass(E_ALT, k)


def verify():
    assert W == F(9, 1280)
    assert X * W == F(3, 10496)
    assert q(E) == F(3310244525, 8132285009)
    assert q(E_ALT) == F(25056783625, 48160049449)

    assert p(E) == F(311263325, 8339351907)
    assert r(E) == F(5867068998425, 13670371100129)
    assert p(E_ALT) == F(611675425, 14983252257)
    assert r(E_ALT) == F(43705915975225, 80957043123769)
    assert 0 < p(E) < r(E) < 1
    assert 0 < p(E_ALT) < r(E_ALT) < 1

    # Complete count-domain verification (18 integer counts, no sampling).
    for k in range(N + 1):
        ae = signed_mass(E, k)
        am = mixed_signed_mass(k)
        if k < 3:
            assert ae < 0
            assert am < 0
        else:
            assert ae > 0
            assert am > 0

    assert sum((signed_mass(E, k) for k in range(N + 1)), F(0)) == 0
    assert sum((signed_mass(E_ALT, k) for k in range(N + 1)), F(0)) == 0

    de = threshold_advantage(E)
    da = threshold_advantage(E_ALT)
    gap = de - da
    assert F(1, 21000) < gap < F(1, 20000)

    endpoint_risk = (1 - de) / 2
    alt_risk = (1 - da) / 2
    mixture_bayes_risk = (
        1 - (1 - MIX_ALT) * de - MIX_ALT * da
    ) / 2
    assert alt_risk > endpoint_risk
    assert mixture_bayes_risk - endpoint_risk == MIX_ALT * gap / 2
    assert mixture_bayes_risk > endpoint_risk + F(1, 5250000)

    print("EC49FUE EXACT FRACTION CERTIFICATE PASS")
    print("n =", N, "x =", X, "delta =", X * W)
    print("signs: endpoint and nuisance mixture: ---,+++++++++++++++")
    print("1/21000 < D3(E)-D3(-1) < 1/20000: TRUE")
    print("1/5250000 < minimax-excess lower bound: TRUE")
    print("endpoint Bayes risk ~", float(endpoint_risk))
    print("test risk at e=-1 ~", float(alt_risk))
    print("mixed-prior Bayes risk ~", float(mixture_bayes_risk))
    print("exact gap numerator digits:", len(str(gap.numerator)))
    print("exact gap denominator digits:", len(str(gap.denominator)))


if __name__ == "__main__":
    verify()
