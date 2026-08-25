#!/usr/bin/env python3
"""Independent checker for RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-INDEPENDENT-REPLICATION.

No source checker or withheld proof is used. Standard-library only.
"""
from math import isqrt
from fractions import Fraction

def is_prime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True

def primes_upto(n):
    return [x for x in range(2, n + 1) if is_prime(x)]

def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1

def inv(a, p):
    return pow(a % p, -1, p)


def check_h1_prime(q):
    """Finite-pressure check of H1a/H1b/H1c; symbolic proof is in the return."""
    inv2 = inv(2, q)
    cases = 0
    for B in range(1, q):
        inv2B = inv(2*B, q)
        for d0 in range(q):
            for d1 in range(q):
                if d0 == d1:
                    continue
                C = (2*(d0-d1)) % q
                for u in range(q):
                    for v in range(q):
                        if u == v:
                            continue
                        # Intersection of T_(0,u), T_(0,v).
                        X = (-B*(u+v)*inv2) % q
                        Y = (B*u*v*inv2-d0) % q
                        for w in range(q):
                            on_third = (Y - (-w*X-B*w*w*inv2-d1)) % q == 0
                            hyper = (B*(w-u)*(w-v)-C) % q == 0
                            assert on_third == hyper
                            cases += 1

                # H1b/H1c: dual overlap <-> difference of squares <-> Bab=C.
                for x in range(q):
                    for y in range(q):
                        negdual0 = (-B*x*x*inv2-d0) % q
                        negdual1 = (-B*y*y*inv2-d1) % q
                        overlap = negdual0 == negdual1
                        diff_sq = (B*(y*y-x*x)-C) % q == 0
                        a, b = (y-x) % q, (y+x) % q
                        split = (B*a*b-C) % q == 0
                        assert overlap == diff_sq == split
                        # Inverse Phi is valid in odd characteristic.
                        xx = (b-a)*inv2 % q
                        yy = (a+b)*inv2 % q
                        assert (xx, yy) == (x, y)
    return cases

def check_h1_narrowing_counterexample():
    # K=Q, B=1, d0=1/2, d1=0, C=1.
    B = Fraction(1)
    d0, d1 = Fraction(1, 2), Fraction(0)
    C = 2*(d0-d1)
    x, y = Fraction(0), Fraction(1)
    f0 = -B*x*x/2-d0
    f1 = -B*y*y/2-d1
    a, b = y-x, y+x
    assert C == 1 and f0 == f1 == Fraction(-1, 2)
    assert B*a*b == C and a == b == 1
    # If (a,b)=(w-u,w-v) then a=b forces u=v, forbidden in H1a.
    return (str(f0), str(a), str(b))

def h2_orbits(q, B, C):
    R = {(x, y) for x in range(q) for y in range(q)
         if (B * (y*y - x*x) - C) % q == 0}
    pending = set(R)
    orbits = []
    while pending:
        x, y = next(iter(pending))
        orb = {(sx*x % q, sy*y % q)
               for sx in (1, -1) for sy in (1, -1)}
        orb &= R
        orbits.append(orb)
        pending -= orb
    return R, orbits

def check_h2_prime(q):
    inv2 = inv(2, q)
    orbit_counts = set()
    orbit_size_patterns = set()
    cases = 0
    for B in range(1, q):
        for C in range(1, q):
            cases += 1
            R, orbits = h2_orbits(q, B, C)
            assert len(R) == q - 1
            expected = (q + 1 + legendre(B*C, q) + legendre(-B*C, q)) // 4
            assert len(orbits) == expected

            # Realize C = 2(d0-d1) with d1=0 and verify that common
            # negative-dual values are exactly the G-orbits.
            d0 = C * inv2 % q
            fibers = {}
            for x, y in R:
                z0 = (-B*x*x*inv2 - d0) % q
                z1 = (-B*y*y*inv2) % q
                assert z0 == z1
                fibers.setdefault(z0, set()).add((x, y))
            assert len(fibers) == len(orbits)
            for pts in fibers.values():
                x, y = next(iter(pts))
                orb = {(sx*x % q, sy*y % q)
                       for sx in (1, -1) for sy in (1, -1)}
                assert pts == orb

            orbit_counts.add(len(orbits))
            orbit_size_patterns.add(tuple(sorted(map(len, orbits))))
    return cases, sorted(orbit_counts), sorted(orbit_size_patterns)

def Jset(s, q):
    h = (s - 1) // 2
    return {j % q for j in range(-h, h + 1)}

def lambda_image(s, q):
    return {(-s*a - inv(2*a, q)) % q for a in range(1, q)}

def central_saturates_prime(s, q):
    h = (s - 1) // 2
    missed = []
    for a in range(1, q):
        if not any((2*s*a*a + 2*j*a + 1) % q == 0
                   for j in range(-h, h + 1)):
            missed.append(a)
    return not missed, missed

def central_saturates_mod_n(s, n):
    h = (s - 1) // 2
    missed = []
    for a in range(1, n):
        if not any((2*s*a*a + 2*j*a + 1) % n == 0
                   for j in range(-h, h + 1)):
            missed.append(a)
    return not missed, missed

def check_j1():
    ps = primes_upto(101)
    cases = 0
    saturation_cases = []
    divisor_boundary = []
    for s in range(3, 16, 2):
        for q in ps:
            if q == 2:
                continue
            if (2*s) % q == 0:
                img = {(-s*a - inv(2*a, q)) % q for a in range(1, q)}
                sat, _ = central_saturates_prime(s, q)
                divisor_boundary.append((s, q, len(img), sat))
                continue
            cases += 1
            img = lambda_image(s, q)
            c = inv(2*s, q)
            expected = (q + legendre(c, q)) // 2
            assert len(img) == expected
            sat, _ = central_saturates_prime(s, q)
            assert sat == (img <= Jset(s, q))
            if sat:
                saturation_cases.append((s, q, len(img)))
    return cases, saturation_cases, divisor_boundary

def check_j2():
    minus = []
    plus = []
    tested_minus = 0
    tested_plus = 0
    composite_minus = 0
    composite_plus = 0
    composite_saturations = []
    for s in range(3, 102, 2):
        qm, qp = 2*s - 1, 2*s + 1
        if is_prime(qm):
            tested_minus += 1
            sat, missed = central_saturates_prime(s, qm)
            if sat:
                minus.append((s, qm))
        else:
            composite_minus += 1
            sat, _ = central_saturates_mod_n(s, qm)
            if sat:
                composite_saturations.append(("-", s, qm))
        if is_prime(qp):
            tested_plus += 1
            sat, missed = central_saturates_prime(s, qp)
            if sat:
                plus.append((s, qp))
        else:
            composite_plus += 1
            sat, _ = central_saturates_mod_n(s, qp)
            if sat:
                composite_saturations.append(("+", s, qp))
    assert minus == [(3, 5)]
    assert plus == [(3, 7)]
    return tested_minus, tested_plus, minus, plus, composite_minus, composite_plus, composite_saturations

def check_boundaries():
    # q=2: H2a cannot extend (B=C=1 gives two R-points, not q-1=1).
    q = 2
    R2 = {(x,y) for x in range(q) for y in range(q)
          if (y*y - x*x - 1) % q == 0}
    assert len(R2) == 2

    # C=0 cannot be added to H2: y^2=x^2 has 2q-1 points for odd q.
    zeroC = {}
    for q in (5, 7, 13):
        R = {(x,y) for x in range(q) for y in range(q)
             if (y*y - x*x) % q == 0}
        assert len(R) == 2*q - 1
        zeroC[q] = len(R)

    # s=1 explains why the nontrivial s>=3 cutoff matters at q+=3.
    sat_s1_q3, _ = central_saturates_prime(1, 3)
    assert sat_s1_q3

    return len(R2), zeroC, sat_s1_q3

def check_c1_c2():
    sols = []
    for qb in range(3, 6, 2):
        k = 2*qb - 1
        for s in range(3, 20, 2):
            if k - 4 == 2*s - 1 and k - 2 == 2*s + 1:
                sols.append((s, qb, k))
    assert sols == [(3, 5, 9)]
    M9 = (9 - 4)*(9 - 2)
    assert M9 == 35
    assert 3*M9 == 105
    assert 3*M9 + 1 == 106 == 2*53
    triad = [6*1*1 + 2*j*1 + 1 for j in (-1,0,1)]
    assert triad == [5,7,9]
    return sols, M9, 3*M9, 3*M9+1

def main():
    print("INDEPENDENT_CHECKER_START")
    for q in (5, 7):
        h1cases = check_h1_prime(q)
        print(f"H1 q={q}: finite concurrence/dual/Phi cases PASS; concurrence triples tested={h1cases}")
    h1ce = check_h1_narrowing_counterexample()
    print(f"H1 narrowing counterexample over Q: common_dual={h1ce[0]}, Phi=(a,b)=({h1ce[1]},{h1ce[2]}) lies on diagonal and cannot have u!=v")
    for q in (5, 7, 13, 53):
        cases, counts, patterns = check_h2_prime(q)
        print(f"H2 q={q}: B,C cases={cases}; orbit_counts={counts}; orbit_size_patterns={patterns}")
    j1_cases, sat_cases, divisor_boundary = check_j1()
    print(f"J1 valid (s,q) cases={j1_cases}; all image-size/saturation equivalences PASS")
    print(f"J1 saturation cases (s<=15,q<=101)={sat_cases}")
    print(f"J1 q|s boundary cases={divisor_boundary}")
    jm, jp, minus, plus, cm, cp, comp_sat = check_j2()
    print(f"J2 prime extremals: lower tested={jm}, saturating={minus}; upper tested={jp}, saturating={plus}")
    print(f"J2 composite raw-congruence boundaries: lower tested={cm}, upper tested={cp}, saturating={comp_sat}")
    r2, zeroC, s1 = check_boundaries()
    print(f"BOUNDARY q=2 H2-example |R|={r2} (so H2a extension fails); C=0 counts={zeroC}; s=1,q=3 saturation={s1}")
    sols, M9, gate, obstruction = check_c1_c2()
    print(f"C1/C2 arithmetic: solutions={sols}; M9={M9}; 3*M9={gate}; obstruction={obstruction}=2*53")
    print("INDEPENDENT_CHECKER_PASS")

if __name__ == "__main__":
    main()
