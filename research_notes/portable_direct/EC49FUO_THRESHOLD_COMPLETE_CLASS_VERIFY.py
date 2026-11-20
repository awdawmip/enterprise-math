#!/usr/bin/env python3
"""Exact rational crosschecks of the EC49FUO all-n robust threshold complete class.
Finite arithmetic tests corroborate, but do not replace, the universal proof.
"""
from fractions import Fraction as Q
from math import comb

BETA = Q(3, 637)
ETA = Q(141024, 1653649)
C = 21829245984
H = 45529434409
B = 456083905
THETA_E = Q(31597745, 1653649)
U_E = Q(4822040484, 8132285009)


def pq(theta, x):
    T = (1 - x) * (1 - BETA * x + BETA * x * theta)
    u = Q(C, 1) / (H - B * theta)
    return 1 - T, 1 - u * T


def masses(n, z):
    return [comb(n, k) * z**k * (1-z)**(n-k) for k in range(n+1)]


def reference(n, x):
    p_max = pq(Q(0), x)[0]
    q_min = pq(THETA_E, x)[1]
    assert q_min - p_max == (1-x) * ((1-U_E) - (BETA+U_E*ETA)*x)
    assert 0 < p_max < q_min < 1
    r = (p_max + q_min) / 2
    return r, masses(n, r)


def upper_tail_rearrangement(phi, b):
    remaining = sum(z*f for z, f in zip(b, phi))
    new = [Q(0)] * len(b)
    for k in range(len(b)-1, -1, -1):
        new[k] = min(Q(1), remaining / b[k])
        remaining -= b[k] * new[k]
    assert remaining == 0
    assert sum(z*f for z, f in zip(b, new)) == sum(z*f for z, f in zip(b, phi))
    assert all(new[k] <= new[k+1] for k in range(len(new)-1))
    assert sum(Q(0) < z < Q(1) for z in new) <= 1
    return new


def verify(n, x, theta, phi, new, b):
    p, q = pq(theta, x)
    assert 0 < p < q < 1
    minus, plus = masses(n, p), masses(n, q)
    delta = [plus[k] - minus[k] for k in range(n+1)]
    g = [delta[k] / b[k] for k in range(n+1)]
    assert sum(delta) == 0
    assert all(g[k+1] > g[k] for k in range(n))
    w = [b[k]*(new[k]-phi[k]) for k in range(n+1)]
    assert sum(w) == 0
    tails = [sum(w[j:]) for j in range(1,n+1)]
    assert all(t >= 0 for t in tails)
    improvement = sum((new[k]-phi[k])*delta[k] for k in range(n+1))
    telescoped = sum(tails[j-1] * (g[j]-g[j-1]) for j in range(1,n+1))
    assert improvement == telescoped and improvement >= 0
    if new != phi:
        assert improvement > 0
    return improvement


def main():
    exact_gap = (1-U_E) - (BETA+U_E*ETA)
    assert exact_gap == Q(1822277955590, 5180265550733) > 0
    assert pq(THETA_E, Q(1, 4))[1] > pq(Q(0), Q(1, 4))[0]
    checks = 0
    smallest_positive = None
    for n in (1, 2, 3, 5, 10, 15, 17, 30):
        for x in (Q(1, 100000), Q(7, 25000), Q(1, 4), Q(1, 2), Q(99, 100)):
            _, b = reference(n, x)
            cases = (
                [Q((7*k+3) % 11, 10) for k in range(n+1)],
                [Q((3*k+5) % 7, 6) for k in range(n+1)],
                [Q(int(k >= (n+1)//2)) for k in range(n+1)],
            )
            for phi in cases:
                new = upper_tail_rearrangement(phi, b)
                for theta in (Q(0), THETA_E / 3, THETA_E / 2, THETA_E):
                    gain = verify(n, x, theta, phi, new, b)
                    if gain > 0 and (smallest_positive is None or gain < smallest_positive):
                        smallest_positive = gain
                    checks += 1
    n, x = 3, Q(1, 4)
    phi = [Q(1, 4), Q(3, 4), Q(1, 3), Q(1)]
    r, b = reference(n, x)
    new = upper_tail_rearrangement(phi, b)
    assert new == [Q(0), Q(8584211795208246558402214228, 19757499438344405608158829605), Q(1), Q(1)]
    sample_gain_E = verify(n, x, THETA_E, phi, new, b)
    print('PASS: exact gap,', checks, 'pointwise dominance + telescoping checks')
    print('sample_n=3 x=1/4 threshold_randomization_k=1:', new[1])
    print('sample_risk_reduction_at_theta_E:', float(sample_gain_E / 2))
    print('gap_coefficient:', exact_gap)


if __name__ == '__main__':
    main()
