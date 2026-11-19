"""Exact modular differences between even and odd finite witness matchings."""
import argparse
import json
from fractions import Fraction
from functools import reduce
from itertools import combinations, permutations
from math import factorial, gcd, isqrt, prod
from pathlib import Path


def factors(n):
    pieces = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            pieces[p] = pieces.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        pieces[n] = 1
    return pieces


def chi(p, a):
    value = pow(a % p, (p - 1) // 2, p)
    return -1 if value == p - 1 else value


def chi4(a):
    assert a % 2 == 1
    return 1 if a % 4 == 1 else -1


def ramanujan(n, b):
    result = 1
    for p, e in factors(n).items():
        scale = p ** (e - 1)
        if b % scale:
            return 0
        result *= scale * ((p - 1) if b % (scale * p) == 0 else -1)
    return result


def full_formula(n, b):
    data = factors(n)
    if n % 2 == 0:
        e = data[2]
        if e == 1:
            return (-1) ** ((n + 2) // 4) * n ** (n // 2 - 1) * ramanujan(n, b)
        m = n // 2**e
        scale = 2 ** (e - 2)
        if b % scale or (b // scale) % 2 == 0:
            return 0
        return ((-1) ** (n // 4) * n ** (n // 2 - 1) * 2 ** (e - 1)
                * chi4(m * (b // scale)) * ramanujan(m, b))

    conductor = prod(p for p, e in data.items() if e % 2)
    phase = n * (n - 1) // 2 + sum(p % 4 == 3 for p in factors(conductor))
    assert phase % 2 == 0
    result = (-1) ** (phase // 2) * n ** ((n - 3) // 2) * isqrt(n * conductor)
    for p, e in data.items():
        if e % 2 == 0:
            result *= ramanujan(p**e, b)
        else:
            scale = p ** (e - 1)
            if b % scale:
                return 0
            twist = pow(n // (p**e), -1, p)
            result *= scale * chi(p, -(b // scale) * twist)
    return result


def even_odd(u, v, modulus):
    """Subset DP; extending a prefix counts inversions with its new last column."""
    n = len(u)
    initial = [0] * (2 * modulus)
    initial[0] = 1
    layer = {0: initial}
    for row in range(n):
        next_layer = {}
        for mask, counts in layer.items():
            for col in range(n):
                bit = 1 << col
                if mask & bit:
                    continue
                key = mask | bit
                if key not in next_layer:
                    next_layer[key] = [0] * (2 * modulus)
                out = next_layer[key]
                odd = (mask >> (col + 1)).bit_count() % 2
                shift = (u[row] * v[col]) % modulus
                for i in range(modulus):
                    target = (i + shift) % modulus
                    out[odd * modulus + target] += counts[i]
                    out[(1 - odd) * modulus + target] += counts[modulus + i]
        layer = next_layer
    counts = layer[(1 << n) - 1]
    return counts[:modulus], counts[modulus:]


def signed(u, v, modulus):
    pos, neg = even_odd(u, v, modulus)
    assert sum(pos) == sum(neg) == factorial(len(u)) // 2
    return [a - b for a, b in zip(pos, neg)]


def sign_of_perm(images):
    inversions = sum(x > y for i, x in enumerate(images) for y in images[i + 1:])
    return (-1) ** inversions


def brute_force(u, v, p):
    counts = [0] * p
    for pi in permutations(range(len(u))):
        value = sum(a * v[j] for a, j in zip(u, pi)) % p
        counts[value] += sign_of_perm(pi)
    return counts


def p_valuation(x, p):
    assert x > 0
    k = 0
    while x % p == 0:
        k += 1
        x //= p
    return k


def permutation_sign_checks(limit):
    cases = 0
    for n in range(2, limit + 1):
        for k in range(1, n):
            if gcd(k, n) != 1:
                continue
            if n % 2:
                expect = prod(chi(p, k) ** e for p, e in factors(n).items())
            else:
                expect = 1 if n % 4 == 2 else chi4(k)
            assert sign_of_perm([(k * i) % n for i in range(n)]) == expect
            cases += 1
    return cases


def finite_field_fourier_check(n):
    """All DFT frequencies via Vandermonde determinants in two prime fields."""
    test_primes = []
    q = n + 1
    while len(test_primes) < 2:
        if all(q % d for d in range(2, isqrt(q) + 1)):
            test_primes.append(q)
        q += n
    bins = [full_formula(n, b) for b in range(n)]
    for q in test_primes:
        root = next(x for x in range(2, q)
                    if pow(x, n, q) == 1 and all(pow(x, n // p, q) != 1 for p in factors(n)))
        powers = [pow(root, j, q) for j in range(n)]
        for k in range(n):
            nodes = [powers[k * j % n] for j in range(n)]
            det = 1
            for j, y in enumerate(nodes):
                for x in nodes[:j]:
                    det = det * (y - x) % q
            assert det == sum(c * y for c, y in zip(bins, nodes)) % q
    return test_primes


def check():
    full = []
    for n in range(2, 17):
        h = signed(range(n), range(n), n)
        assert h == [full_formula(n, b) for b in range(n)]
        if n <= 8:
            assert h == brute_force(range(n), range(n), n)
        data = factors(n)
        phi = prod((p - 1) * p ** (e - 1) for p, e in data.items())
        if n % 2:
            s = prod(p for p, e in data.items() if e % 2)
            norm = n ** ((n - 3) // 2) * isqrt(n * s) * phi * 2**sum(e % 2 == 0 for e in data.values())
            assert sum(x != 0 for x in h) == prod(p - 1 if e % 2 else p for p, e in data.items())
            if n in data:
                assert h == [chi(n, 2 * b) * n ** ((n - 1) // 2) for b in range(n)]
        else:
            norm = n ** (n // 2 - 1) * 2**len(data) * phi
        assert sum(map(abs, h)) == norm
        full.append(dict(modulus=n, signed_bins=h, total_variation=str(Fraction(norm, factorial(n)))))

    prime_cases = {}
    for p in (2, 3, 5, 7):
        cases = 0
        for n in range(2, p + 1):
            subsets = list(combinations(range(p), n))
            for u in subsets:
                for v in subsets:
                    h = signed(u, v, p)
                    exponent = (n * (n - 1) // 2 - 1) // (p - 1)
                    assert p_valuation(reduce(gcd, h, 0), p) == exponent
                    cases += 1
        prime_cases[p] = cases

    duplicate = signed([1, 6, 8], [0, 1, 2], 5)
    assert duplicate == [0] * 5
    assert signed([0, 1, 2], [1, 6, 8], 5) == duplicate
    u, v = [1, 3, 7, 8, 9, 10], [0, 2, 3, 4, 6, 8]
    irregular = signed(u, v, 11)
    assert p_valuation(reduce(gcd, irregular, 0), 11) == 1
    assert irregular == brute_force(u, v, 11)
    signed_count = permutation_sign_checks(80)
    extra_fourier = {n: finite_field_fourier_check(n) for n in (18, 20, 24, 25, 27, 36, 45, 63, 72, 75, 81, 105)}
    return {
        "method": "exact integer parity subset DP; direct permutation cross-check for full tables through 8",
        "full_tables": full,
        "additional_full_table_fourier_mod_primes_by_modulus": extra_fourier,
        "independent_multiplication_permutation_signs_through_80": signed_count,
        "unordered_pairwise_distinct_subset_pairs_exhausted_by_prime": prime_cases,
        "duplicate_on_either_side_mod5": duplicate,
        "irregular_mod_11": dict(input=u, output=v, signed_bins=irregular, gcd=reduce(gcd, irregular, 0)),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = json.dumps(check(), indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
