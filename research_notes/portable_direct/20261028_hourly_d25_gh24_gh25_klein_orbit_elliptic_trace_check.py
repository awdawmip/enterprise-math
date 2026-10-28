"""GH-24/25 portable exact checker, no external dependencies.

Checks finite-field transformations, the provenance-retaining Klein-four orbit
partition, exceptional G-channel boundary at p=11, and the independent
GH-19 binomial-coefficient evaluation. Finite checks are not universal proofs.
"""
from fractions import Fraction
from math import comb, isqrt


def primes_under(limit):
    for p in range(11, limit):
        if all(p % q for q in range(2, isqrt(p) + 1)):
            yield p


def char(a, p):
    z = pow(a % p, (p - 1) // 2, p)
    return 0 if z == 0 else (1 if z == 1 else -1)


def inspect(p):
    assert p >= 11 and p % 8 == 3
    m, k = (p - 3) // 8, (p + 1) // 4
    I = lambda a: pow(a % p, -1, p)
    U = {x for x in range(p) if x * (x + 1) * (9 * x + 1) % p}
    assert len(U) == p - 3
    phi = lambda x: (9 * x + 1) * I(9 * x * (x + 1)) % p
    A = lambda x: -(x + 1) * I(9 * x + 1) % p
    B = lambda x: I(9 * x)
    C = lambda x: -(9 * x + 1) * I(9 * (x + 1)) % p
    h = lambda x: char(x, p) * pow(x * (x + 1), 3 * m + 1, p) * pow(9 * x + 1, m, p) % p
    hg = lambda x: char(x, p) * pow(x * (x + 1), 3 * m + 1, p) * pow(9 * x + 1, m - 1, p) * (5 - 9 * x) % p
    sum_f = 0
    for x in U:
        v = phi(x)
        rA, rB, rC = -char(v, p) % p, pow(v, k, p), -pow(I(v), 2*m, p) % p
        assert A(A(x)) == x and B(B(x)) == x and C(C(x)) == x
        assert A(B(x)) == B(A(x)) == C(x)
        assert phi(A(x)) == v and phi(B(x)) == I(v)
        assert h(A(x)) == rA * h(x) % p
        assert h(B(x)) == rB * h(x) % p
        assert h(C(x)) == rC * h(x) % p
        assert rC == rA*rB % p
        sum_f = (sum_f + h(x)) % p

    tau = -sum(char(x*(x+1)*(9*x+1),p) for x in range(p))
    curve_points = p + 1 - tau
    assert curve_points % 8 == 0  # P=(1/3,4/3) doubles to (0,0)
    assert tau % 8 == (p + 1) % 8

    remaining = U.copy()
    free_active, free_killed, fixed_A, fixed_B = [], [], [], []
    while remaining:
        x = min(remaining)
        orb = {x,A(x),B(x),C(x)}
        assert orb <= remaining
        remaining.difference_update(orb)
        val = sum(h(y) for y in orb) % p
        if len(orb) == 2:
            if any(A(y) == y for y in orb):
                assert all(char(phi(y), p) == -1 for y in orb)
                assert val == h(x) * (1 + pow(phi(x), k, p)) % p
                fixed_A.append((tuple(sorted(orb)),val))
            else:
                assert all(B(y) == y for y in orb)
                assert all(phi(y) == 1 for y in orb)
                assert val == 0
                fixed_B.append((tuple(sorted(orb)),val))
        else:
            assert len(orb) == 4
            assert val == h(x) * (1 - char(phi(x), p)) * (1 + pow(phi(x), k, p)) % p
            if char(phi(x), p) == -1:
                free_active.append((tuple(sorted(orb)),val))
            else:
                assert val == 0
                free_killed.append(tuple(sorted(orb)))
    assert len(fixed_A) == len(fixed_B) == 1
    assert len(free_active) + len(free_killed) == 2*m - 1
    assert len(free_active) == (p - 7 + tau) // 8
    assert sum_f == (sum(v for _,v in fixed_A+free_active)) % p

    df = sum(comb(3*m+1, m-r)*comb(m,r)*pow(9,r,p) for r in range(m+1))%p
    dg = sum((16*r+5)*comb(3*m+1,m-r)*comb(m,r)*pow(9,r,p) for r in range(m+1))%p
    sg = sum(hg(x) for x in range(p))%p
    assert sum_f == -df%p and sg == -dg%p
    sg_U = sum(hg(x) for x in U)%p
    if p == 11:  # m=1, G loses one vanishing factor at -1/9
        omitted_x = -I(9) % p
        assert hg(omitted_x) == 3 and (sg_U+3)%p==sg
    else:
        assert sg_U == sg
    return {'p':p,'tau':tau,'A':fixed_A,'B':fixed_B,'active':free_active,
            'inactive_count':len(free_killed),'sum_f':sum_f,'sum_g':sg}


def main():
    assert Fraction(4*73**3,81).denominator == 81
    checked = 0
    for p in primes_under(2000):
        if p % 8 == 3:
            r=inspect(p)
            checked += 1
            if p in (11,19,43,59,67):
                print('WITNESS',r)
    print('PASS_GH24_KLEIN_FOUR_WEIGHTED_SOURCE_TRANSPORT')
    print('PASS_GH25_ORDER_EIGHT_ELLIPTIC_TRACE_AND_ORBIT_COUNT')
    print('PASS_GH22_BINOMIAL_TWO_CHANNEL_FULL_SUM_AND_P11_BOUNDARY')
    print('target_primes_p_lt_2000:',checked)
    print('complex_j_exact:',Fraction(4*73**3,81))


if __name__ == '__main__':
    main()
