"""Unit-twist covariance of complete cubic additive sums. Standard Python 3."""

from collections import Counter
from fractions import Fraction
from functools import cache
from itertools import product
from math import gcd, prod


def factors(n):
    p = 2
    out = []
    while p * p <= n:
        k = 0
        while n % p == 0:
            n //= p
            k += 1
        if k:
            out.append((p, k))
        p += 1
    if n > 1:
        out.append((n, 1))
    return out


@cache
def cube_counts(d):
    return Counter(pow(x, 3, d) for x in range(d))


def gram_from_counts(q, b, factorization):
    # Expand the Ramanujan sum c_q(n) = sum_{d|gcd(q,n)} d mu(q/d).
    total = 0
    for flags in product((0, 1), repeat=len(factorization)):
        divisor = q // prod(p**flag for (p, _), flag in zip(factorization, flags))
        cubes = cube_counts(divisor)
        matches = sum(frequency * cubes[(-b * r) % divisor] for r, frequency in cubes.items())
        total += (-1)**sum(flags) * divisor * (q // divisor)**2 * matches
    phi = prod((p - 1) * p**(k - 1) for p, k in factorization)
    return Fraction(total, q * phi)


def local_formula(p, k, b):
    ell, r = divmod(k, 3)
    factor = p**ell
    if r == 0:
        return factor
    if r == 1:
        if p % 3 != 1:
            return 0
        return factor * (2 if pow(b, (p - 1) // 3, p) == 1 else -1)
    if p == 3:
        return factor * (3 if b % 9 in (1, 8) else 0)
    return factor


def matrix_rank(matrix):
    a = [list(map(Fraction, row)) for row in matrix]
    rank = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        for i in range(rank + 1, len(a)):
            if a[i][j]:
                ratio = a[i][j] / a[rank][j]
                a[i] = [x - ratio*y for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def main():
    moduli = sorted(set(range(2, 201)) | {216, 243, 343, 441, 512, 729, 819, 2401})
    total = 0
    for q in moduli:
        decomposition = factors(q)
        values = {}
        for b in range(1, q):
            if gcd(q, b) != 1:
                continue
            prediction = prod(local_formula(p, k, b) for p, k in decomposition)
            values[b] = gram_from_counts(q, b, decomposition)
            assert values[b] == prediction, (q, b, values[b], prediction)
        if q in (7, 9, 14, 27, 49, 63, 91, 125, 819):
            # Retain every distinct column of the directly counted matrix.
            units = tuple(values)
            columns = {tuple(values[a*b % q] for a in units) for b in units}
            # Equal row patterns can now be removed without changing rank.
            row_patterns = set(zip(*columns))
            rank = matrix_rank(row_patterns)
            expected_rank = 1
            for p, k in decomposition:
                if k % 3 == 1:
                    expected_rank *= 2 if p % 3 == 1 else 0
                elif p == 3 and k % 3 == 2:
                    expected_rank *= 3
            assert rank == expected_rank, (q, rank, expected_rank)
            # A Fourier transform in h takes the actual integer cube histogram
            # twisted by a unit to the list of all additive frequencies h.
            fibers = cube_counts(q)
            rows = {tuple(fibers[a*y % q] for y in range(q)) for a in units}
            real_rank = matrix_rank(set(zip(*rows)))
            expected_full = 3**sum(p % 3 == 1 or (p == 3 and k >= 2)
                                   for p, k in decomposition)
            assert real_rank == expected_full, (q, real_rank, expected_full)
            print(f"q={q}, unit rank={rank}, all-frequency rank={real_rank}")
        total += len(values)
    print(f"{len(moduli)} moduli, {total} exact unit covariances")

    cases = 0
    for q in range(2, 73):
        units = [a for a in range(1, q) if gcd(a, q) == 1]
        for degree in range(2, 7):
            histogram = Counter(pow(x, degree, q) for x in range(q))
            rows = {tuple(histogram[a*y % q] for y in range(q)) for a in units}
            # Full Fourier inversion in the additive variable preserves complex rank.
            actual = matrix_rank(set(zip(*rows)))
            image = {pow(a, degree, q) for a in units}
            assert actual * len(image) == len(units)
            cases += 1
    print(f"{cases} general power-map ranks from complete integer fiber tables")


if __name__ == "__main__":
    main()
