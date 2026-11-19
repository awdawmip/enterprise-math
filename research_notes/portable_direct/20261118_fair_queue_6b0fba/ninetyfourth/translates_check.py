"""Exact cyclotomic and modular-arithmetic checks for the three translates 0, 1, 3."""
import json
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import gcd


def negacyclic(degree, terms):
    coeff = [0] * degree
    for exponent, value in terms:
        wrap, i = divmod(exponent, degree)
        coeff[i] += (-1 if wrap % 2 else 1) * value
    return coeff


def absolute_norm(coeff):
    # Q(zeta_g) -> Q(zeta_g^2) via E(z)E(-z) = A(z^2)^2 - z^2 B(z^2)^2.
    if len(coeff) == 1:
        return abs(coeff[0])
    terms = []
    for parity in (0, 1):
        part = coeff[parity::2]
        sign = 1 - 2 * parity
        for i, a in enumerate(part):
            if a:
                terms.extend((i + j + parity, sign * a * b) for j, b in enumerate(part) if b)
    return absolute_norm(negacyclic(len(coeff) // 2, terms))


def prime_factors(value):
    answer = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            answer.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        answer.append(value)
    return answer


def exceptional_primes(g):
    norms = Counter()
    for i, j, k in permutations(range(1, g), 3):
        terms = [(i + k, 3), (j + k, -2), (i + j, -1), (i, -2), (j, 3), (k, -1)]
        norm = absolute_norm(negacyclic(g // 2, terms))
        assert norm
        norms[norm] += 1
    prime_set = {p for v in norms for p in prime_factors(v) if p % g == 1}
    return sorted(prime_set), {"ordered_cyclotomic_triples": sum(norms.values()),
                              "distinct_positive_norms": len(norms), "maximum_norm": max(norms)}


def roots_unity(p, g, k):
    for b in range(2, p):
        z = pow(b, (p - 1) // g, p)
        if pow(z, g // 2, p) != 1:
            modulus = p ** k
            z = pow(z, p ** (k - 1), modulus)
            roots = [pow(z, i, modulus) for i in range(g)]
            assert roots[0] == 1 and len(set(roots)) == g and pow(z, g, modulus) == 1
            return roots
    raise AssertionError((p, g, k))


def collisions(p, g, k, label):
    M = p ** k
    roots = roots_unity(p, g, k)[1:]
    hits = []
    for a in roots:
        for b in roots:
            if a == b:
                continue
            x = (b - 1) * pow(a - b, -1, M) % M
            y = a * x % M
            assert x != y and pow(x, g, M) == pow(y, g, M) and pow(x + 1, g, M) == pow(y + 1, g, M)
            if pow(x + label, g, M) == pow(y + label, g, M):
                hits.append((x, y))
    return hits


def direct_pairs(modulus, exponent, labels):
    counts = Counter(tuple(pow(x + t, exponent, modulus) for t in labels) for x in range(modulus))
    return sum(n * (n - 1) for n in counts.values())


def min_fixed(p, g):
    if p - 1 == g:
        return p - 1, list(range(p - 1))
    roots = roots_unity(p, g, 1)[1:]
    base = [pow(z - 1, -1, p) for z in roots]
    templates = set()
    for x, y in permutations(base, 2):
        scale = pow(y - x, -1, p)
        templates.add(tuple(sorted((z - x) * scale % p for z in base)))
    forbidden = {z for row in templates for z in row}
    for t in range(2, p):
        if t not in forbidden:
            return 3, [0, 1, t]
    for t in range(2, p):
        still_bad = {z for row in templates if t in row for z in row}
        for u in range(t + 1, p):
            if u not in still_bad:
                return 4, [0, 1, t, u]
    raise AssertionError(("outside checked menu size", p, g))


def single_depth(g):
    primes, norms = exceptional_primes(g)
    rows = []
    for p in primes:
        counts = []
        k = 1
        while True:
            hits = collisions(p, g, k, 3)
            counts.append(len(hits))
            if p ** k <= 15000:
                assert direct_pairs(p ** k, g, (0, 1, 3)) == len(hits)
            if not hits:
                break
            assert hits[0][0] != hits[0][1]
            last_witness = min(hits)
            k += 1
        assert k >= 2
        row = {"p": p, "last_bad_precision": k - 1, "ordered_pair_counts_through_first_good": counts,
               "last_bad_pair": last_witness}
        if g <= 16:
            minimum, labels = min_fixed(p, g)
            assert direct_pairs(p, g, labels) == 0
            row.update(minimum_number_of_fixed_labels=minimum, one_minimum_menu=labels)
        rows.append(row)
    return {"g": g, "norm_certificate": norms, "exception_count": len(rows), "exceptional_local_rows": rows}


def is_prime(n):
    return n >= 2 and prime_factors(n) == [n]


def independent_small_rings(lists):
    evaluated = 0
    prime_powers = 0
    for p in range(3, 500, 2):
        if not is_prime(p):
            continue
        exponent = 2
        while exponent <= 32:
            g = gcd(exponent, p - 1)
            for k in range(1, 6):
                M = p ** k
                if M > 15000:
                    break
                bad_depth = lists.get(g, {}).get(p, 0)
                assert bool(direct_pairs(M, exponent, (0, 1, 3))) == (k <= bad_depth)
                assert bool(direct_pairs(M, exponent, (0, 1, 2))) == (g >= 4)
                evaluated += 1
            exponent *= 2
        prime_powers += 1
    mixed = []
    for n in range(3, 901, 2):
        factors = []
        rest = n
        for p in prime_factors(n):
            depth = 0
            while rest % p == 0:
                depth += 1
                rest //= p
            factors.append((p, depth))
        for exponent in (4, 8, 16, 32):
            predicted = any(k <= lists.get(gcd(exponent, p - 1), {}).get(p, 0) for p, k in factors)
            assert bool(direct_pairs(n, exponent, (0, 1, 3))) == predicted
        mixed.append(n)
    return {"prime_domains": prime_powers, "prime_power_exponent_cases": evaluated,
            "odd_modulus_upper_bound": mixed[-1], "all_odd_modulus_exponent_cases": 4 * len(mixed)}


if __name__ == "__main__":
    rows = [single_depth(g) for g in (4, 8, 16, 32)]
    tables = {d["g"]: {r["p"]: r["last_bad_precision"] for r in d["exceptional_local_rows"]} for d in rows}
    densities = []
    for depth in range(1, 6):
        parts = {p: h for g, val in tables.items() for p, h in val.items() if gcd(2 ** depth, p - 1) == g}
        fraction = Fraction(1)
        for prime, level in parts.items():
            fraction *= 1 - Fraction(1, prime) + Fraction(1, prime ** (level + 1))
        densities.append({"squaring_depth": depth, "bad_primes": len(parts),
                          "density_relative_to_odd_inputs": str(fraction)})
    print(json.dumps({"exact_t3_local_spectra": rows, "fixed_depth_local_densities": densities,
                      "direct_checks": independent_small_rings(tables)},
                     ensure_ascii=False, indent=2))
