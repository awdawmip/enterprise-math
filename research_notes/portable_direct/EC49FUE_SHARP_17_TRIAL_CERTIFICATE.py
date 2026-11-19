#!/usr/bin/env python3
"""EC49FUE-S: exact n=17 composite-minimax half-line certificate.

Standard library only, integer/rational operations throughout.
Scientific pin: BRC16943@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab
Earlier Bernoulli derivation: EC49FUD@26da0d004d175bff1ff99a7aa8e94bf029349039
"""
from fractions import Fraction as F
from math import comb, lcm

N = 17
E = F(1048576, 18958647)
M = F(1469, 64)
L = F(951, 1280)
U = F(3, 4)
W = U - L
X = F(5, 123)
A_MEAN = M * (L + U) / 2
C_MEAN = M * (U - X * W / 2)


def p(e):
    if e is None:  # e -> negative infinity, an exact limit
        return X * C_MEAN / A_MEAN
    return X * (1 - e * C_MEAN) / (1 - e * A_MEAN)


def q(e):
    if e is None:
        return F(575 * 41217719, 45529434409)
    return F(575) * (41217719 * e - 2359296) / (
        45529434409 * e - 2630615040
    )


def r(e):
    pe = p(e)
    return pe + q(e) * (1 - pe)


def signed_mass(e, k):
    pe, re = p(e), r(e)
    return F(comb(N, k)) * (
        re**k * (1 - re)**(N-k) -
        pe**k * (1 - pe)**(N-k)
    )


def tail_adv(e, j):
    return sum((signed_mass(e, k) for k in range(j, N+1)), F(0))


def padd(v, w):
    a = [0] * max(len(v), len(w))
    for i, value in enumerate(v):
        a[i] += value
    for i, value in enumerate(w):
        a[i] += value
    return a


def pscale(v, factor):
    return [factor * x for x in v]


def psub(v, w):
    return padd(v, pscale(w, -1))


def pmul(v, w):
    out = [0] * (len(v) + len(w) - 1)
    for i, a in enumerate(v):
        for j, b in enumerate(w):
            out[i+j] += a*b
    return out


def ppow(v, exponent):
    result = [1]
    while exponent:
        if exponent & 1:
            result = pmul(result, v)
        if exponent > 1:
            v = pmul(v, v)
        exponent >>= 1
    return result


def jointly_clear(den, num):
    """Scale denominator and numerator by the SAME positive integer."""
    factor = lcm(*(value.denominator for value in den + num))
    return (
        [int(factor * value) for value in den],
        [int(factor * value) for value in num],
    )


def signed_tail_polynomial(j_num, v_den, g_num, g_den):
    other = psub(v_den, j_num)
    total = [0]
    for k in range(4, N + 1):
        term = pmul(ppow(j_num, k), ppow(other, N-k))
        total = padd(total, pscale(term, g_den * comb(N, k)))
    term3 = pmul(ppow(j_num, 3), ppow(other, N-3))
    return padd(total, pscale(term3, g_num * comb(N, 3)))


def verify():
    assert W == F(9, 1280) and X*W == F(3, 10496)
    assert q(E) == F(3310244525, 8132285009)
    assert p(E) == F(311263325, 8339351907)
    assert r(E) == F(5867068998425, 13670371100129)
    assert 0 < p(E) < r(E) < 1
    assert 0 < p(None) < r(None) < 1

    # Verify the complete finite count domain and mixture signs.
    for k in range(N+1):
        assert (signed_mass(E, k) < 0) if k < 3 else (signed_mass(E, k) > 0)
        assert (signed_mass(None, k) < 0) if k < 4 else (signed_mass(None, k) > 0)

    ae = signed_mass(E, 3)
    ai = signed_mass(None, 3)
    assert ae > 0 > ai
    mix_weight = ae / (ae - ai)
    gamma = (tail_adv(None, 4) - tail_adv(E, 4)) / (ae-ai)
    assert F(0) < mix_weight < F(1)
    assert F(0) < gamma < F(1)
    for k in range(N+1):
        mixture_mass = ((1-mix_weight) * signed_mass(E,k)
                        + mix_weight * signed_mass(None,k))
        if k <= 2:
            assert mixture_mass < 0
        elif k == 3:
            assert mixture_mass == 0
        else:
            assert mixture_mass > 0

    d0 = tail_adv(E,4) + gamma*ae
    assert d0 == tail_adv(None,4) + gamma*ai
    endpoint_bayes_risk = (1 - tail_adv(E,3))/2
    minimax_risk = (1-d0)/2
    assert minimax_risk > endpoint_bayes_risk
    mixed_adv = ((1-mix_weight)*tail_adv(E,4)
                 + mix_weight*tail_adv(None,4))
    assert mixed_adv == d0

    # Set s=E-e >=0. Preserve joint integer scalings in each ratio.
    AD, PN = jointly_clear(
        [F(1) - E*A_MEAN, A_MEAN],
        [X*(1-E*C_MEAN), X*C_MEAN]
    )
    QD, QN = jointly_clear(
        [F(2630615040)-45529434409*E, F(45529434409)],
        [F(575)*(2359296-41217719*E), F(575*41217719)]
    )
    assert all(value > 0 for value in AD + QD)
    BD = pmul(AD,QD)
    RN = psub(padd(pmul(PN,QD),pmul(QN,AD)),pmul(PN,QN))
    assert 0 < RN[0] < BD[0]

    gn, gd = gamma.numerator, gamma.denominator
    dn, dd = d0.numerator, d0.denominator
    first = signed_tail_polynomial(RN,BD,gn,gd)
    second = pmul(signed_tail_polynomial(PN,AD,gn,gd), ppow(QD,N))
    H = psub(pscale(psub(first,second),dd),
             pscale(ppow(BD,N),dn*gd))
    while len(H)>1 and H[-1]==0:
        H.pop()

    assert len(H)==34           # polynomial degree 33
    assert H[0]==0              # exact equality at e=E
    assert all(isinstance(c,int) and c>0 for c in H[1:])  # ALL 33 coefficients
    assert all(isinstance(c,int) for c in H)

    # H(s)/(dd*gd*BD(s)^17) = D_gamma(E-s)-D_gamma(E) > 0 (s>0).
    # This is a full half-line certificate, not finite-parameter sampling.
    assert dd>0 and gd>0
    print("EC49FUE-S EXACT COMPOSITE MINIMAX CERTIFICATE PASS")
    print("n =",N,"x =",X,"delta =",X*W)
    print("mixture weight ~",float(mix_weight),"randomization ~",float(gamma))
    print("33/33 strictly positive nonconstant polynomial coefficients")
    print("H degree =",len(H)-1,"H constant =",H[0])
    print("endpoint Bayes risk ~",float(endpoint_bayes_risk))
    print("exact all-real-parameter minimax risk ~",float(minimax_risk))
    print("strict saddle excess ~",float(minimax_risk-endpoint_bayes_risk))
    print("integer H coefficient min bit-length =",
          min(v.bit_length() for v in H[1:]))


if __name__=="__main__":
    verify()
