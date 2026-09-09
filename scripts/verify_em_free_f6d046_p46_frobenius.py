#!/usr/bin/env python3
"""Finite-field Frobenius census for the dimension-4 mixed Prym P46.

Curve E: v^2=A(t)
Double cover C46: m^2=(-1/288)*v*D(t)
P46 is Prym(C46/E). For each good prime p we count E and C46 over
F_{p^n}, n=1..4, recover the degree-8 local polynomial by Newton identities,
check the weight-one functional equation, and factor over Z when sympy exists.
"""
from itertools import product
import json

try:
    import sympy as sp
except Exception:
    sp = None


def trim_poly(a, p):
    a = [x % p for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def poly_divmod(a, b, p):
    a = trim_poly(a, p)
    b = trim_poly(b, p)
    inv = pow(b[-1], -1, p)
    q = [0] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and a != [0]:
        k = len(a) - len(b)
        c = a[-1] * inv % p
        q[k] = c
        for j, x in enumerate(b):
            a[j + k] = (a[j + k] - c * x) % p
        a = trim_poly(a, p)
    return trim_poly(q, p), a


def monic_polys(p, d):
    for cs in product(range(p), repeat=d):
        yield list(cs) + [1]


def irreducible(poly, p):
    n = len(poly) - 1
    for d in range(1, n // 2 + 1):
        for f in monic_polys(p, d):
            _, r = poly_divmod(poly, f, p)
            if r == [0]:
                return False
    return True


def first_irreducible(p, n):
    if n == 1:
        return [0, 1]
    for poly in monic_polys(p, n):
        if poly[0] != 0 and irreducible(poly, p):
            return poly
    raise RuntimeError((p, n))


class FF:
    def __init__(self, p, n):
        self.p = p
        self.n = n
        self.q = p**n
        self.mod = first_irreducible(p, n)
        self.coeffs = [self.decode_raw(i) for i in range(self.q)]

    def decode_raw(self, x):
        c = []
        for _ in range(self.n):
            c.append(x % self.p)
            x //= self.p
        return tuple(c)

    def enc(self, c):
        x = 0
        m = 1
        for a in c:
            x += (a % self.p) * m
            m *= self.p
        return x

    def add(self, a, b):
        return self.enc([(x + y) % self.p for x, y in zip(self.coeffs[a], self.coeffs[b])])

    def neg(self, a):
        return self.enc([(-x) % self.p for x in self.coeffs[a]])

    def scalar(self, k):
        return k % self.p

    def mul(self, a, b):
        ca = self.coeffs[a]
        cb = self.coeffs[b]
        n = self.n
        p = self.p
        z = [0] * (2 * n - 1)
        for i, x in enumerate(ca):
            if x:
                for j, y in enumerate(cb):
                    if y:
                        z[i + j] = (z[i + j] + x * y) % p
        for k in range(2 * n - 2, n - 1, -1):
            c = z[k] % p
            if c:
                for j in range(n):
                    z[k - n + j] = (z[k - n + j] - c * self.mod[j]) % p
        return self.enc(z[:n])

    def eval(self, coeff, t):
        o = 0
        for c in reversed(coeff):
            o = self.add(self.mul(o, t), self.scalar(c))
        return o


ACOEF = [144, 528, 192, 24, 1]
DCOEF = [24, 12, 1]


def count_pair(p, n):
    field = FF(p, n)
    q = field.q
    roots = {}
    for x in range(q):
        xx = field.mul(x, x)
        roots.setdefault(xx, []).append(x)
    squares = set(roots)

    def chi(x):
        if x == 0:
            return 0
        return 1 if x in squares else -1

    constant = field.scalar((-pow(288, -1, p)) % p)
    affine_e = 0
    affine_c = 0
    for t in range(q):
        av = field.eval(ACOEF, t)
        dv = field.eval(DCOEF, t)
        vs = roots.get(av, [])
        affine_e += len(vs)
        for v in vs:
            fv = field.mul(constant, field.mul(v, dv))
            affine_c += 1 + chi(fv)

    n_e = affine_e + 2
    n_c = affine_c + 2 + chi(constant) + chi(field.neg(constant))
    return {
        "p": p,
        "n": n,
        "q": q,
        "field_modulus": field.mod,
        "N_E": n_e,
        "N_C46": n_c,
        "power_sum_P46": n_e - n_c,
    }


def local_poly(p, counts):
    power_sums = [None] + [counts[n - 1]["power_sum_P46"] for n in range(1, 5)]
    coeff = [1]
    for k in range(1, 5):
        total = power_sums[k]
        for i in range(1, k):
            total += coeff[i] * power_sums[k - i]
        assert total % k == 0, (p, k, total)
        coeff.append(-total // k)
    full = coeff + [p * coeff[3], p * p * coeff[2], p**3 * coeff[1], p**4]
    checks = {
        "degree8": len(full) == 9,
        "functional_c8": full[8] == p**4,
        "functional_c7": full[7] == p**3 * full[1],
        "functional_c6": full[6] == p**2 * full[2],
        "functional_c5": full[5] == p * full[3],
    }
    factors = []
    factorization = "sympy unavailable"
    irreducible_over_z = None
    if sp is not None:
        t = sp.symbols("T")
        expr = sum(full[i] * t**i for i in range(9))
        fac = sp.factor_list(expr)
        factorization = str(sp.factor(expr))
        irreducible_over_z = bool(sp.Poly(expr, t, domain=sp.ZZ).is_irreducible)
        factors = [
            {"factor": str(f), "multiplicity": int(e), "degree": int(sp.degree(f, t))}
            for f, e in fac[1]
        ]
    return {
        "coefficients_ascending": full,
        "power_sums_1_to_4": power_sums[1:],
        "factorization_over_Z": factorization,
        "irreducible_over_Z": irreducible_over_z,
        "factors": factors,
        "checks": checks,
    }


def main():
    primes = [5, 7, 11, 13]
    records = []
    all_checks = True
    for p in primes:
        counts = [count_pair(p, n) for n in range(1, 5)]
        lp = local_poly(p, counts)
        all_checks &= all(lp["checks"].values())
        records.append({"prime": p, "counts": counts, "local_polynomial": lp})
    patterns = []
    for record in records:
        factors = record["local_polynomial"]["factors"]
        patterns.append([f["degree"] for f in factors for _ in range(f["multiplicity"])])
    result = {
        "schema": "EM_FREE_F6D046_P46_FROBENIUS_CENSUS_V1",
        "researcher_id": "EM-FREE-F6D046",
        "research_unit": "EM-FREE-F6D046-R13-P46-FROBENIUS-CENSUS",
        "model": {
            "E": "v^2=A(t)",
            "C46": "m^2=(-1/288)*v*D(t)",
            "A": "t^4+24t^3+192t^2+528t+144",
            "D": "t^2+12t+24",
        },
        "good_primes": primes,
        "all_internal_checks_passed": all_checks,
        "records": records,
        "factor_degree_patterns": patterns,
        "verdict": "COMPUTATIONAL_EVIDENCE_ONLY__NO_ABSOLUTE_SIMPLICITY_CLAIM",
        "boundary": (
            "Four local polynomials can falsify proposed stable decompositions, "
            "but without an endomorphism/correspondence theorem they are not by "
            "themselves a proof of geometric simplicity."
        ),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if all_checks else 1)


if __name__ == "__main__":
    main()
