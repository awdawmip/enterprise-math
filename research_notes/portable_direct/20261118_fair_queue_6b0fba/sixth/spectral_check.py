"""Integral congruence defects for real finite-chain primitive spectra."""

from functools import cache
from itertools import combinations
from math import gcd, lcm, prod

from sympy import Matrix, Poly, ZZ, divisors, factorint, primefactors, symbols, totient
from sympy.matrices.normalforms import smith_normal_form

t = symbols("t")
one = Poly(1, t, domain=ZZ)
variable = Poly(t, t, domain=ZZ)


@cache
def continuant(n):
    if n == 1:
        return one
    if n == 2:
        return variable
    return variable * continuant(n-1) - continuant(n-2)


@cache
def primitive(n):
    proper = prod((primitive(d) for d in divisors(n) if 1 < d < n), start=one)
    return continuant(n).exquo(proper)


def integral_matrix(indices):
    """Use the ordinary power basis in both the domain and the targets."""
    total = sum(int(totient(n)) for n in indices)
    rows = []
    for n in indices:
        f = primitive(n)
        residue = one
        columns = []
        for _ in range(total):
            columns.append([residue.nth(i) for i in range(f.degree())])
            residue = (variable * residue).rem(f)
        rows.extend(zip(*columns))
    return Matrix(rows)


def combine_primary(primary):
    rank = max((len(exponents) for exponents in primary.values()), default=0)
    factors = [1] * rank
    for p, exponents in primary.items():
        for i, v in enumerate(sorted(exponents), start=rank-len(exponents)):
            factors[i] *= p**v
    return [d for d in factors if d > 1]


def predicted(indices):
    primary = {}
    for p in set().union(*(set(primefactors(n)) for n in indices)):
        chains = {}
        for n in indices:
            c = n
            while c % p == 0:
                c //= p
            chains.setdefault(c, []).append(n)
        primary[p] = []
        for chain in chains.values():
            for power, n in enumerate(sorted(chain, reverse=True)):
                if power:
                    primary[p].extend([power] * int(totient(n)))
    return combine_primary(primary)


def full_formula(m):
    primary = {}
    for p, a in factorint(m).items():
        c = m // p**a
        primary[p] = [h for h in range(1, a+1)
                      for _ in range(c * int(totient(p**(a-h))) - (h == a))]
    return combine_primary(primary)


def main():
    pairs = 0
    for i, j in combinations(range(2, 30), 2):
        p = None
        if j % i == 0:
            candidates = primefactors(j // i)
            if len(candidates) == 1:
                p = candidates[0]
        f, g = primitive(i), primitive(j)
        assert abs(f.resultant(g)) == (p**f.degree() if p else 1)
        if p:
            reduced = g.rem(f)
            divided = reduced.exquo_ground(p)
            assert abs(f.resultant(divided)) == 1
        pairs += 1
    samples = [(2, 6, 18), (3, 6, 12, 24), (4, 7, 12), (3, 9, 12, 18),
               (5, 10, 15), (6, 12, 18), (2, 3, 4, 6, 12), (6, 24, 30)]
    for m in range(2, 34):
        indices = tuple(d for d in divisors(m) if d > 1)
        decreasing = [gcd(m, lcm(*range(1, m // (k+1) + 1))) for k in range(1, m)]
        assert predicted(indices) == full_formula(m) == [v for v in reversed(decreasing) if v > 1]
        degree = int(totient(m))
        primes = primefactors(m)
        mass = primes[0] if len(primes) == 1 else 1
        denominator = mass * prod(p**(degree // (p-1)) for p in primes)
        assert abs(primitive(m).discriminant()) * denominator == (2*m)**degree
        # This form includes m=2 without a negative exponent.
        assert abs(continuant(m).discriminant()) * m**3 == 2**(m-1) * m**m
        samples.append(indices)
    for indices in samples:
        snf = smith_normal_form(integral_matrix(indices), domain=ZZ)
        actual = [abs(int(k)) for k in snf.diagonal() if abs(k) != 1]
        assert actual == predicted(indices), (indices, actual)
    print(f"{pairs} resultants, {len(samples)} integral Smith matrices")
    print("M=12:", full_formula(12), "M=24:", full_formula(24))


if __name__ == "__main__":
    main()
