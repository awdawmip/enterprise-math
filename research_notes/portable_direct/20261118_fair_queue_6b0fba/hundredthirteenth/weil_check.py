"""Finite branch evidence for the genus-five to genus-two graph obstruction."""
import json
from math import gcd
from pathlib import Path


class Quadratic:
    """Base-degree-two extension with representatives a+n*b and root^2=delta."""

    def __init__(self, n, base_add, base_mul, delta):
        self.n = n
        self.order = n * n
        self.ba = base_add
        self.bm = base_mul
        self.delta = delta

    def add(self, x, y):
        n = self.n
        return self.ba(x % n, y % n) + n * self.ba(x // n, y // n)

    def mul(self, x, y):
        n = self.n
        a, b, c, d = x % n, x // n, y % n, y // n
        real = self.ba(self.bm(a, c), self.bm(self.delta, self.bm(b, d)))
        imag = self.ba(self.bm(a, d), self.bm(b, c))
        return real + n * imag

    def neg(self, x):
        return self.mul(6, x)


def evaluate(f, coeffs, x):
    y = 0
    for a in reversed(coeffs):
        y = f.add(f.mul(y, x), a)
    return y


# Coefficients in F49 are a+7b for a+bi, i^2=-1.
FIVE = [30, 4, 21, 22, 47, 1]
CUBIC = [1, 0, 1, 1]


def curves(f):
    roots = [[] for _ in range(f.order)]
    for y in range(f.order):
        roots[f.mul(y, y)].append(y)
    source = elliptic = target = 1  # unique rational point above infinity
    branch = []
    finite_weierstrass = []
    for x in range(f.order):
        dy = evaluate(f, FIVE, x)
        target += len(roots[dy])
        if dy == 0:
            finite_weierstrass.append(x)
        for y in roots[evaluate(f, CUBIC, x)]:
            elliptic += 1
            # x^2 - 12 = x^2 + 2 in characteristic seven.
            square = f.mul(y, f.add(f.mul(x, x), 2))
            source += len(roots[square])
            if square == 0:
                branch.append([x, y])
    tr_target = f.order + 1 - target
    assert elliptic - source == 2 * tr_target
    return dict(q=f.order, C46=source, E=elliptic, C7=target,
                finite_branch_on_E=branch, finite_weierstrass_x=finite_weierstrass,
                trace_JC7=tr_target, trace_P=elliptic-source)


def trim(a):
    while a and a[-1] == 0:
        a.pop()
    return a


def ppow(f, a, n):
    y = 1
    while n:
        if n % 2:
            y = f.mul(y, a)
        a = f.mul(a, a)
        n //= 2
    return y


def remainder(f, a, b):
    a = a.copy()
    inv = ppow(f, b[-1], f.order-2)
    while len(a) >= len(b):
        delta = len(a)-len(b)
        u = f.neg(f.mul(a[-1], inv))
        for j, v in enumerate(b):
            a[delta+j] = f.add(a[delta+j], f.mul(u, v))
        trim(a)
    return a


def pgcd(f, a, b):
    while b:
        a, b = b, remainder(f, a, b)
    if not a:
        return []
    inv = ppow(f, a[-1], f.order-2)
    return [f.mul(t, inv) for t in a]


def pmul(f, a, b):
    c = [0] * (len(a)+len(b)-1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            c[i+j] = f.add(c[i+j], f.mul(v, w))
    return trim(c)


def frobenius_gcd(f, a, degree):
    qpower = f.order**degree
    x, y = [0, 1], [1]
    while qpower:
        if qpower % 2:
            y = remainder(f, pmul(f, y, x), a)
        x = remainder(f, pmul(f, x, x), a)
        qpower //= 2
    y += [0] * max(0, 2-len(y))
    y[1] = f.add(y[1], 6)
    return pgcd(f, a, trim(y))


def separations():
    """For each possible torsion order, certify Q[alpha^m]=Q[alpha]."""
    h = [2401, 245, 0, 5, 1]

    def primitive_power_rank(m, p):
        def mul4(a, b):
            c = [0]*7
            for j in range(4):
                for t in range(4):
                    c[j+t] += a[j]*b[t]
            for j in range(6, 3, -1):
                for t in range(4):
                    c[j-4+t] -= c[j]*h[t]
            return [v % p for v in c[:4]]

        n = m
        g, unit = [0,1,0,0], [1,0,0,0]
        alpha_m = unit
        while n:
            if n % 2:
                alpha_m = mul4(alpha_m, g)
            g = mul4(g, g)
            n //= 2
        row = unit
        mat = []
        for _ in range(4):
            mat.append(row)
            row = mul4(row, alpha_m)
        for j in range(4):
            pivot = next((k for k in range(j,4) if mat[k][j] % p), None)
            if pivot is None:
                return False
            mat[j], mat[pivot] = mat[pivot], mat[j]
            inv = pow(mat[j][j], -1, p)
            for k in range(j+1,4):
                b = mat[k][j]*inv % p
                mat[k] = [(v-b*w) % p for v,w in zip(mat[k],mat[j])]
        return True

    certs = []
    for m in range(1,513):
        if sum(gcd(i,m)==1 for i in range(1,m+1)) > 16:
            continue
        p = next(p for p in (11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101)
                 if primitive_power_rank(m,p))
        certs.append([m,p])
    assert len(certs)==32 and certs[-1][0]==60
    return certs


def main():
    assert 6 not in {i*i % 7 for i in range(7)}
    f = Quadratic(7, lambda a, b: (a+b) % 7, lambda a, b: a*b % 7, 6)
    add = [[f.add(a, b) for b in range(49)] for a in range(49)]
    mul = [[f.mul(a, b) for b in range(49)] for a in range(49)]
    sq = {mul[i][i] for i in range(49)}
    delta = min(set(range(1, 49)) - sq)
    ext = Quadratic(49, lambda a, b: add[a][b], lambda a, b: mul[a][b], delta)
    rows = [curves(f), curves(ext)]
    assert [(r['C7'], r['trace_JC7']) for r in rows] == [(55, -5), (2377, 25)]
    assert rows[0]['finite_branch_on_E'] == [[21, 27], [21, 29], [28, 22], [28, 34]]
    assert rows[0]['finite_weierstrass_x'] == []
    for a in (CUBIC, FIVE):
        derivative = [f.mul(j % 7, c) for j, c in enumerate(a) if j]
        assert pgcd(f, a, derivative) == [1]
    assert pgcd(f, CUBIC, [2, 0, 1]) == [1]
    assert [len(frobenius_gcd(f, CUBIC, i))-1 for i in (1, 2, 3)] == [0, 0, 3]
    two, three = (frobenius_gcd(f, FIVE, j) for j in (2, 3))
    assert len(two) == 3 and len(three) == 4 and pmul(f, two, three) == FIVE
    assert frobenius_gcd(f, FIVE, 1) == [1]
    # Integer partitions of six allowed by the Weil polynomial mod 2 on J[2].
    # Compute products over F2 by bit masks; no semisimplicity assumption.
    def parts(n, lo=1):
        if n == 0:
            yield []
        for j in range(lo, n+1):
            for tail in parts(n-j, j):
                yield [j]+tail

    def by_binomial(a, degree):
        return a ^ (a << degree)

    expected = by_binomial(by_binomial(0b11011, 1), 1)
    profiles = []
    for v in parts(6):
        prod = 1
        for j in v:
            prod = by_binomial(prod, j)
        if prod == expected:
            profiles.append(v)
    assert profiles == [[1, 1, 1, 3], [1, 2, 3]]
    # Even subsets modulo complement model J(C7)[2] geometrically.
    perm = [0, 2, 1, 4, 5, 3]
    torsion = {min(mask, 63 ^ mask) for mask in range(64) if mask.bit_count() % 2 == 0}
    fixed_torsion = []
    for mask in sorted(torsion):
        rotated = sum(((mask >> i) & 1) << j for i, j in enumerate(perm))
        if min(rotated, rotated ^ 63) == mask:
            fixed_torsion.append(mask)
    assert len(torsion) == 16 and len(fixed_torsion) == 2
    # In the low trace window positive integral elements of Q(sqrt(417))
    # have (H,b) with H and b of the same parity and H^2 > 417*b^2.
    small = [h for h in range(1, 21)
             if any((h-b) % 2 == 0 and h*h > 417*b*b for b in range(-h,h+1))]
    assert small == list(range(2,21,2))
    first_trace, second_trace = (r['trace_JC7'] for r in rows)
    q = f.order
    weil = [q*q, -q*first_trace, (first_trace**2-second_trace)//2, -first_trace, 1]
    assert weil == [2401,245,0,5,1]
    # Closed point counts are for all n by the proved Frobenius orbit lengths.
    def fixed(v, n):
        return sum(j for j in v if n % j == 0)
    witness_fields = []
    for n in range(1, 13):
        r, w = fixed([1]*5+[3], n), fixed([1, 2, 3], n)
        assert (r > 4*w) == (gcd(n, 6) == 1)
        witness_fields.append([n, r, w, r > 4*w])
    checked = dict(
        scope="independent finite-field point, branch, and polynomial calculations; no correspondence equations assumed",
        field_encoding="a+7b stands for a+b*i, i^2=-1; F2401 elements a+49b use t^2=delta",
        quartic_tower_delta=delta, models="C46:w^2=y(x^2-12), y^2=x^3+x^2+1; C7:y^2=FIVE",
        finite_coefficients_ascending=FIVE, explicit_F49_factors_ascending=[two, three],
        point_counts=rows, recovered_weil_ascending=weil,
        root_ratio_order_and_full_power_basis_witness_prime=separations(),
        trace_compatible_with_totally_positive_integer_in_K_through_20=small,
        rational_two_torsion_even_subset_representatives=fixed_torsion,
        source_branch_orbit_degrees=[1]*5+[3], target_weierstrass_orbit_degrees=[1,2,3],
        genus2_profiles_compatible_with_weil_mod2=profiles,
        rational_branch_test_n_1_through_12=witness_fields)
    path = Path(__file__).with_name("weil_checked.json")
    path.write_text(json.dumps(checked, indent=2, ensure_ascii=False)+'\n')


if __name__ == '__main__':
    main()
