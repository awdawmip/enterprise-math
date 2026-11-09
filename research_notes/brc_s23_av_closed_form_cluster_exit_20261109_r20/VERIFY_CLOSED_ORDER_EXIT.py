#!/usr/bin/env python3
"""Independent exact certificate of the nominal-gap exit formula.

This validates the finite rational tests and the certified S23 enclosure;
it does not claim to certify the frozen transcendental theta anew.
"""
from fractions import Fraction as F
from math import gcd
from pathlib import Path

def ceil_fraction(x: F) -> int:
    return -((-x.numerator) // x.denominator)

def exit_closed_form(q: int, h: int, eta: F) -> int:
    assert q >= 1 and eta > 0
    if q == 1:
        return ceil_fraction(1 / eta)
    assert 1 <= h < q
    z = q - h
    tmax = ceil_fraction((F(h) + 1 / (q * eta)) / q) - 1
    return q * tmax + z

def nominal_min_gap(n: int, q: int, h: int, eta: F) -> F:
    assert n >= q
    a, b = divmod(n, q)
    if q == 1:
        jmax = 0
    else:
        jmax = 2 if b > q - h else 1
    return F(1, q) + (h - q * (a - 1 + jmax)) * eta

def explicit_nominal_min_gap(n: int, q: int, h: int, eta: F) -> F:
    """Independent enumeration of cyclic rational cluster boundary gaps."""
    k = pow(h, -1, q) if q > 1 else 0
    m = None
    for r in range(q):
        ell = r + q * ((n - 1 - r) // q)
        rnext = (r + h) % q
        gap = F(1, q) + (rnext - ell) * eta
        m = gap if m is None else min(m, gap)
    return m

def run():
    cases = 0
    checked_gap = 0
    first_fail = 0
    for q in range(1, 27):
        for p in range(q+1):
            for sign in (+1, -1):
                if (p == 0 and sign < 0) or (p == q and sign > 0):
                    continue
                if gcd(p, q) != 1:
                    continue
                k = p if sign > 0 else q - p
                h = pow(k, -1, q) if q > 1 else 0
                for denom in (2*q*q+1, 3*q*q+7, 5*q*q+1, 13*q*q+5, 31*q*q+7):
                    eta = F(1, denom)
                    theta = F(p, q) + sign*eta
                    if not 0 < theta < 1:
                        continue
                    cutoff = exit_closed_form(q, h, eta)
                    assert q == 1 or (cutoff - (q-h)) % q == 0
                    positions = set(range(q, min(q+45,cutoff+3)))
                    positions.update(range(max(q, cutoff-2), cutoff+4))
                    for n in sorted(positions):
                        if n < q:
                            continue
                        g1 = nominal_min_gap(n,q,h,eta)
                        g2 = explicit_nominal_min_gap(n,q,h,eta)
                        assert g1 == g2,(q,p,sign,n,g1,g2)
                        assert (g1 > 0) == (n <= cutoff), (q,p,sign,n,cutoff,g1)
                        checked_gap += 1
                    assert nominal_min_gap(max(q,cutoff+1),q,h,eta) <= 0
                    first_fail += 1
                    cases += 1
    theta_lo = F(262204504569236716045286,10**24)
    theta_hi = F(262204504569236716045287,10**24)
    for theta in [theta_lo,theta_hi]:
        q,p,h=61,16,19
        eta = F(p,q)-theta
        cutoff = exit_closed_form(q,h,eta)
        assert cutoff == 225
        g225 = nominal_min_gap(225,q,h,eta)
        g226 = nominal_min_gap(226,q,h,eta)
        assert g225 == 164*theta -43 > 0
        assert g226 == 225*theta -59 < 0
        delta = q*eta
        x = 59-225*theta
        assert 0 < delta-x < x < delta
    tab=Path('/mnt/data/em_r16/AFFINE_RUNS_2M.tsv')
    if tab.exists():
        rows=[]
        for line in tab.read_text().splitlines()[1:]:
            a,b,A,B,dA,dB=map(int,line.split('\t'))
            rows.append((a,b,A,B,dA,dB))
        def risk(n,theta):
            for a,b,A,B,dA,dB in rows:
                if a <= n <= b:
                    return F(A)+B*theta+(n-a)*(dA+dB*theta)
            raise ValueError(n)
        for theta in [theta_lo,theta_hi]:
            for n in (225,226,292):
                assert risk(n,theta)-risk(n-1,theta) == 164*theta-43
        print('EXISTING_AFFINE_TABLE_REFERENCE_CHECK=PASS (n=225,226,292; two rational endpoints)')
    print('EXACT_RATIONAL_PARAMETER_CASES=',cases)
    print('EXACT_NOMINAL_GAP_COMPARISONS=',checked_gap)
    print('STRICT_FIRST_FAILURE_WITNESSES=',first_fail)
    print('S23_CUTOFF=225; FIRST_FAILURE=226; FIRST_FAILURE_RESIDUE=43 mod 61')
    print('S23_GAP_225=164*theta-43>0')
    print('S23_GAP_226=225*theta-59<0')
    print('S23_FIRST_SWAP_DISTANCE=59-225*theta')
    print('PASS_CLOSED_FORM_CLUSTER_ORDER_EXIT_R20')

if __name__ == '__main__':
    run()
