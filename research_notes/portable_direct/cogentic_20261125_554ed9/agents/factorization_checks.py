"""Exact small-instance checks for extracted local arithmetic mechanisms.

Source: google-research/google-research@4a7bc8ab0bc7,
cogentic_research_papers/{integer_factorization,deterministic_factoring_l34}.
These checks cover the declared finite cases, not the papers' asymptotic theorems.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import comb, factorial, gcd, lcm, prod
import json


def primes_upto(n):
    return [k for k in range(2, n + 1) if all(k % d for d in range(2, int(k**0.5) + 1))]


def hybrid_check(y=20, length=4):
    primes = [p for p in primes_upto(y) if 2 * p > y]
    counts = Counter(m * prod(ps) for m in range(y // 2 + 1, y + 1)
                     for ps in product(primes, repeat=length - 1))
    for n, count in counts.items():
        rest, exponents = n, []
        for p in primes:
            e = 0
            while rest % p == 0:
                e += 1
                rest //= p
            exponents.append(e)
        denominator = prod(factorial(e) for e in exponents)
        if rest == 1:
            expected = Fraction(int(sum(exponents) == length), denominator)
        else:
            expected = Fraction(int(y / 2 < rest <= y and sum(exponents) == length - 1),
                                length * denominator)
        assert expected == Fraction(count, factorial(length)), (n, expected, count)
        assert 0 < expected <= 1
    return {"y": y, "length": length, "ordered_representations": sum(counts.values()),
            "distinct_supported_integers": len(counts), "exact_weight_identity": True,
            "scope": "Small combinatorial identity; outside the analytic asymptotic regime."}


def dixon_check(n):
    fibers = defaultdict(list)
    for z in range(1, n):
        if gcd(z, n) == 1:
            fibers[z*z % n].append(z)
    prime_count = len([p for p in primes_upto(n) if n % p == 0])
    expected = 1 - Fraction(2, 2**prime_count)
    observed = set()
    for w, roots in fibers.items():
        # This choice sees only w, not which hidden root z was sampled.
        canonical_root = min(roots)
        successful = sum(1 < gcd(z - canonical_root, n) < n for z in roots)
        observed.add(Fraction(successful, len(roots)))
    assert observed == {expected}
    return {"N": n, "omega": prime_count, "square_fibers": len(fibers),
            "conditional_success_probability_on_every_fiber": str(expected)}


def index_saturation_check():
    p, small_primes, bound, exponent = 31, [2, 5], 5, 15
    assert all(pow(a, exponent, p) == 1 for a in small_primes)
    k = 0
    while bound**(k + 1) <= p - 1:
        k += 1
    group = {1}
    while True:
        enlarged = group | {x * a % p for x in group for a in small_primes}
        if enlarged == group:
            break
        group = enlarged
    count_lower_bound = comb(len(small_primes) + k - 1, k)
    index_bound = (p - 1) // count_lower_bound
    saturation = lcm(*range(1, index_bound + 1))
    assert len(group) >= count_lower_bound
    assert exponent % (p - 1) != 0
    assert exponent * saturation % (p - 1) == 0
    return {"p": p, "prime_generators": small_primes, "B": bound, "k": k,
            "multiset_lower_bound": count_lower_bound, "actual_group_size": len(group),
            "actual_index": (p - 1)//len(group), "proved_index_bound": index_bound,
            "M": exponent, "lcm_1_through_K": saturation,
            "saturated_exponent": exponent * saturation,
            "scope": "Generic elementary core; not the original large-parameter specialization."}


def walsh_check():
    def sign_dot(a, b):
        return 1 if (a & b).bit_count() % 2 == 0 else -1
    dimension = 3
    size = 1 << dimension
    mu = [2, 1, 0, 3, 1, 0, 0, 1]
    nu = [1, 0, 2, 0, 0, 1, 1, 0]
    a = [sum(mu[w] * sign_dot(ell, w) for w in range(size)) for ell in range(size)]
    b = [sum(nu[w] * sign_dot(ell, w) for w in range(size)) for ell in range(size)]
    convolution = [sum(mu[w] * nu[w ^ z] for w in range(size)) for z in range(size)]
    assert all(a[ell] * b[ell] == sum(convolution[w] * sign_dot(ell, w)
                                    for w in range(size)) for ell in range(size))
    assert sum(x*y for x, y in zip(a, b)) == size * convolution[0] >= 0
    incompatible = [1, -1, -1, -1]
    return {"dimension": dimension, "positive_transform_product_identity": True,
            "sum_of_products": sum(x*y for x, y in zip(a, b)),
            "incompatible_K2_signs": incompatible, "incompatible_sum": sum(incompatible),
            "scope": "Finite Fourier algebra only; arithmetic lifting hypotheses are separate."}


if __name__ == "__main__":
    result = {"hybrid_weight": hybrid_check(),
              "dixon": [dixon_check(n) for n in [15, 45, 105, 225]],
              "subgroup_saturation": index_saturation_check(),
              "walsh": walsh_check()}
    print(json.dumps(result, ensure_ascii=False, indent=2))
