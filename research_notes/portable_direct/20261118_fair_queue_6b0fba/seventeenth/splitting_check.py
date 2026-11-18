"""Exact Jacobi sums versus cyclic convolution, and an independent polynomial-gcd test."""
from itertools import combinations
from math import isqrt, prod
from collections import Counter
import json


def prime(n):
    return n >= 2 and all(n % x for x in range(2, isqrt(n) + 1))


class Field:
    """Coordinates a+b*u encoded as a+p*b with u^2=D for the quadratic examples."""

    def __init__(self, p, d):
        assert d in (1, 2)
        self.p, self.d = p, d
        self.size = p**d
        self.D = 0 if d == 1 else next(
            x for x in range(2, p) if pow(x, (p-1)//2, p) == p-1)

    def add(self, x, y):
        p = self.p
        return (x%p + y%p)%p + p*((x//p + y//p)%p)

    def mul(self, x, y):
        p = self.p
        a, b = x%p, x//p
        c, e = y%p, y//p
        return (a*c + self.D*b*e)%p + p*((a*e+b*c)%p)

    def power(self, x, n):
        result = 1
        while n:
            if n % 2:
                result = self.mul(result, x)
            x = self.mul(x, x)
            n //= 2
        return result

    def coordinates(self, x):
        return [x%self.p, x//self.p][:self.d]


def period_example(p, q, ell):
    assert all(prime(x) for x in (p, q, ell))
    assert q < p and ell not in (2, 3, p, q) and (ell-1)%(12*q) == 0
    power = (ell-1)//q
    b = pow(p, power, ell)
    assert b != 1
    d = next(i for i in range(1, q) if pow(p, i, q) == 1)
    K = Field(p, d)
    # The small diagnostic fields allow a finite scan. The theorem takes zeta from Phi_q.
    zeta = next(z for z in range(2, K.size) if K.power(z, q) == 1)
    lookup = {pow(b, i, ell): i for i in range(q)}
    labels = [None] + [
        (-lookup[pow(x, power, ell)]*pow(d, -1, q))%q for x in range(1, ell)]
    roots = [K.power(zeta, k) for k in range(q)]
    c = K.mul(roots[labels[-1]], ell%p)
    jacobi = []
    for j in range(1, q-1):
        total = 0
        for x in range(2, ell):
            total = K.add(total, roots[(j*labels[x] + labels[(1-x)%ell])%q])
        jacobi.append(K.coordinates(total))
        c = K.mul(c, total)

    # Independent verification in K[T]/(T^ell-1), followed by mod Phi_ell.
    # As representatives of length ell, two polys agree modulo Phi iff their
    # difference has every coefficient equal.
    gauss = [0] + [roots[k] for k in labels[1:]]
    frobenius = [0]*ell
    for x, coeff in enumerate(gauss):
        frobenius[(x*K.size)%ell] = coeff
    assert frobenius == [K.mul(zeta, value) for value in gauss]
    power_poly = gauss
    for _ in range(q-1):
        result = [0]*ell
        for i, a in enumerate(power_poly):
            if a:
                for j in range(1, ell):
                    k = (i+j)%ell
                    result[k] = K.add(result[k], K.mul(a, gauss[j]))
        power_poly = result
    assert len(set(power_poly[1:])) == 1
    assert power_poly[0] == K.add(power_poly[1], c)

    cofactor, s = K.size-1, 0
    while cofactor%q == 0:
        s += 1
        cofactor //= q
    omega = K.power(c, cofactor)
    assert K.power(c, (K.size-1)//q) == zeta
    assert K.power(omega, q**(s-1)) == zeta and K.power(omega, q**s) == 1
    if q == 2:
        assert c == ell%p
    return dict(p=p, q=q, ell=ell, d=d, quadratic_radicand=K.D or None,
                zeta=K.coordinates(zeta), J=jacobi, c=K.coordinates(c),
                s=s, omega=K.coordinates(omega))


def trim(f):
    while f and f[-1] == 0:
        f.pop()
    return f


def mul(f, g, p):
    out = [0]*(len(f)+len(g)-1)
    for i, a in enumerate(f):
        for j, b in enumerate(g):
            out[i+j] = (out[i+j]+a*b)%p
    return trim(out)


def rem(f, g, p):
    f = f[:]
    inv = pow(g[-1], -1, p)
    while len(f) >= len(g):
        j, c = len(f)-len(g), f[-1]*inv%p
        for i, x in enumerate(g):
            f[i+j] = (f[i+j]-c*x)%p
        trim(f)
    return f


def gcd(f, g, p):
    while g:
        f, g = g, rem(f, g, p)
    return [x*pow(f[-1], -1, p)%p for x in f]


def pow_mod(g, n, f, p):
    out = [1]
    while n:
        if n%2:
            out = rem(mul(out, g, p), f, p)
        g = rem(mul(g, g, p), f, p)
        n //= 2
    return out


def eval_poly(f, x, p):
    value = 0
    for a in reversed(f):
        value = (x*value+a)%p
    return value


def root_polynomial(S, p):
    f = [1]
    for a in S:
        f = mul(f, [(-a)%p, 1], p)
    return f


def partition(f, g, q, p, omega, s, t):
    z = pow_mod(g, t, f, p)
    e = 0
    for k in range(1, s+1):
        digit = pow_mod(z, q**(s-k), f, p)
        for u in range(q):
            label = e + q**(k-1)*u
            value = pow(omega, label*q**(s-k), p)
            diff = digit[:]
            diff[0] = (diff[0]-value)%p
            factor = gcd(f, trim(diff), p)
            if factor == f:
                e = label
                break
            if len(factor) > 1:
                return factor, k
        else:
            raise AssertionError("no compatible digit")
    return None, None


def cubic_audit(primes):
    totals, cases = {}, []
    for p in primes:
        q, t, s = 3, p-1, 0
        while t%q == 0:
            s, t = s+1, t//q
        omega = next(z for z in range(2, p) if pow(z, q**s, p) == 1
                     and pow(z, q**(s-1), p) != 1)
        counts = Counter()
        for S in combinations(range(p), 3):
            f = root_polynomial(S, p)
            g = [i*f[i]%p for i in range(1, len(f))]
            values = [eval_poly(g, x, p) for x in S]
            R = prod(values)%p
            # Independent discriminant computation of Res(F,F').
            assert R == -prod((x-y)**2 for x, y in combinations(S, 2))%p
            guaranteed = pow(R, (p-1)//q, p) != 1
            factor, k = partition(f, g, q, p, omega, s, t)
            labels = [pow(z, t, p) for z in values]
            split = len(set(labels)) != 1
            assert split == (factor is not None) and (not guaranteed or split)
            if split:
                assert 1 < len(factor) < len(f) and not rem(f, factor, p)
            counts["total"] += 1
            counts["forced_by_resultant"] += int(guaranteed)
            counts["split_by_digits"] += int(split)
            counts["constant_primary"] += int(not split)
            counts["split_after_first_digit"] += int(split and k > 1)
            if (p, S) in {(7,(0,1,2)), (7,(0,1,3)), (19,(0,1,8)), (31,(0,1,2))}:
                cases.append(dict(p=p, roots=S, derivative_values=values,
                                  resultant=R, forced=guaranteed, digit=k,
                                  omega=omega, primary_labels=labels, divisor_ascending=factor))
        totals[p] = dict(counts)
    return dict(counts=totals, selected=cases)


def failure_counts(limit, complete_cubics):
    checked = 0
    worst = []
    samples = {}
    for p in range(7, limit+1, 6):
        if not prime(p):
            continue
        m, t = 1, p-1
        while t%3 == 0:
            m *= 3
            t //= 3
        # H has order t. Compare the coset criterion to the actual three labels.
        H = {x for x in range(1, p) if pow(x, t, p) == 1}
        assert len(H) == t
        C = 0
        for u in range(2, p):
            failed = len({pow(u, t, p), pow(1-u, t, p), pow(u*(u-1), t, p)}) == 1
            assert failed == (u in H and (1-u)%p in H)
            C += int(failed)
        residual = m*m*C - (p+1-3*m)
        assert residual**2 <= p*((m-1)*(m-2))**2
        if m == 3 and p > 16:
            assert C > 0
        if p in complete_cubics:
            assert complete_cubics[p]["constant_primary"] == p*(p-1)*C//6
            samples[p] = dict(index=m, C=C, residual=residual)
        if m == 3:
            worst.append((abs(residual), p, residual))
        checked += 1
    return dict(primes_checked=checked, p_bound=limit, samples=samples,
                largest_abs_trace_for_index_3=max(worst))


def resolvent_audit(p):
    K = Field(p, 1 if p%3 == 1 else 2)
    Q = K.size
    zeta = next(z for z in range(2, Q) if K.power(z, 3) == 1)
    t, s = Q-1, 0
    while t%3 == 0:
        t, s = t//3, s+1
    omega = next(z for z in range(2, Q) if K.power(z, 3**s) == 1
                 and K.power(z, 3**(s-1)) != 1)
    counts = Counter()
    def minus(a, b):
        return K.add(a, K.mul(p-1, b))
    def poly_rem(a, b):
        a = a[:]
        inv = K.power(b[-1], Q-2)
        while len(a) >= len(b):
            offset, ratio = len(a)-len(b), K.mul(a[-1], inv)
            for j, coeff in enumerate(b):
                a[j+offset] = minus(a[j+offset], K.mul(coeff, ratio))
            trim(a)
        return a
    def product(a, b, f):
        result = [0]*(len(a)+len(b)-1)
        for i, v in enumerate(a):
            for j, w in enumerate(b):
                result[i+j] = K.add(result[i+j], K.mul(v, w))
        return poly_rem(trim(result), f)
    def power_mod(a, e, f):
        result = [1]
        while e:
            if e%2:
                result = product(result, a, f)
            a = product(a, a, f)
            e //= 2
        return result
    def monic_gcd(f, a):
        while a:
            f, a = a, poly_rem(f, a)
        inv = K.power(f[-1], Q-2)
        return [K.mul(inv, x) for x in f]
    def log_digits(value, base, length):
        answer = 0
        for k in range(1, length+1):
            reduction = 3**(length-k)
            step = 3**(k-1)
            target = K.power(value, reduction)
            answer = next(e for e in (answer+j*step for j in range(3))
                          if K.power(base, e*reduction) == target)
        return answer
    for S in combinations(range(p), 3):
        f = root_polynomial(S, p)
        fp = [i*f[i]%p for i in range(1,4)]
        # The small-field checker can scan to pick the canonical square root.
        disc = prod((x-y)**2 for x,y in combinations(S,2))%p
        delta = next(x for x in range(1,p) if x*x%p == disc)
        inv = power_mod(fp, Q-2, f)
        for sign in (1,p-1):
            coeff = K.mul(sign*delta%p, minus(zeta, K.mul(zeta,zeta)))
            U = [K.mul(coeff, (inv+[0]*3)[i]) for i in range(3)]
            U[0] = K.add(U[0], f[2])
            U[1] = K.add(U[1], 3)
            U = trim([K.mul(v, pow(2,-1,p)) for v in U])
            if U:
                break
        assert U and len(U) <= 3
        Z = power_mod(U, t, f)
        cube = power_mod(Z, 3, f)
        assert len(cube) == 1
        e = log_digits(cube[0], K.power(omega, 3), s-1)
        got = []
        for j in range(3):
            value = K.power(omega, e+j*3**(s-1))
            eq = Z[:]
            eq[0] = minus(eq[0],value)
            factor = monic_gcd(f, trim(eq))
            assert len(factor) == 2 and factor[1] == 1 and factor[0] < p
            got.append((-factor[0])%p)
        assert sorted(got) == list(S)
        counts["all_three_recovered"] += 1
        counts["first_sign_zero"] += int(sign != 1)
    return dict(p=p, d=K.d, s=s, **counts)


if __name__ == "__main__":
    examples = [(7,2,73), (17,2,73), (5,3,37), (7,3,37), (19,3,37),
                (11,5,181), (19,5,61), (13,7,337)]
    cubics = cubic_audit([7,13,19,31])
    data = dict(jacobi_vs_cyclic_convolution=[period_example(*row) for row in examples],
                cubic_audit=cubics, normalized_audit=failure_counts(2000, cubics["counts"]),
                oriented_resolvent=[resolvent_audit(p) for p in (5,7,11,13,17,19,31)])
    print(json.dumps(data, indent=2, ensure_ascii=False))
