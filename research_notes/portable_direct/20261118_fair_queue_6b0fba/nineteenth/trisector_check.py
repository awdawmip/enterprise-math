"""Same-prime centered-lane saturation. Python 3 standard library, exact integers."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import isqrt
import json

GAPS = (1, 2, 4, 8, 16)
DUPLICATES = {(8, 2), (8, 6), (16, 6), (16, 10)}
ROWS = {(k, j): (2*j+1)**2 + 16*k for k in GAPS for j in range(k)}


def squarefree_factors(n):
    factors = set()
    p = 2
    while p*p <= n:
        while n % p == 0:
            factors.symmetric_difference_update({p})
            n //= p
        p += 1
    if n > 1:
        factors.add(n)
    return factors


def is_prime(n):
    return n >= 2 and all(n % a for a in range(2, isqrt(n)+1))


def saturation(k, q):
    return all(pow(ROWS[k, j], (q-1)//2, q) == q-1 for j in range(k))


def direct_original(k, q):
    s = q - 2*k
    target = {b % q for b in range(-(s//2), s//2 + 1)}
    return all((-s*a - pow(2*a, -1, q)) % q in target for a in range(1, q))


def profile(q):
    return ''.join(str(int(saturation(k, q))) for k in GAPS)


def peel(independent):
    remaining = independent.copy()
    certificate = []
    while remaining:
        counts = Counter(p for factors in remaining.values() for p in factors)
        for label, factors in remaining.items():
            private = sorted(p for p in factors if counts[p] == 1)
            if private:
                break
        else:
            raise AssertionError("no unique-prime pivot")
        certificate.append([*label, private[0]])
        del remaining[label]
    return certificate


def intersection_density(mask, factors):
    """Solve every requested sign equation; inconsistent parity gives zero."""
    pivots = {}
    for (k, _), row in factors.items():
        if not mask & (1 << GAPS.index(k)):
            continue
        v, rhs = set(row), 1
        while v and max(v) in pivots:
            vector, parity = pivots[max(v)]
            v ^= vector
            rhs ^= parity
        if v:
            pivots[max(v)] = v, rhs
        elif rhs:
            return Fraction(0)
    return Fraction(1, 2**len(pivots))


def compressed_law():
    law = Counter()
    for x, y, z, a, b, c in product((0, 1), repeat=6):
        mass = Fraction(1, 8)
        for flag, rank in ((a, 4), (b, 6), (c, 14)):
            mass *= Fraction(1 if flag else 2**rank-1, 2**rank)
        observed = (x, y*z, a, x*y*b, x*(1-z)*c)
        law[''.join(map(str, observed))] += mass
    return dict(sorted(law.items()))


def exact_profile_law(factors):
    intersections = [intersection_density(mask, factors) for mask in range(32)]
    masses = {}
    for mask in range(31, -1, -1):
        masses[mask] = intersections[mask] - sum(
            mass for other, mass in masses.items() if mask & other == mask)
    assert all(m >= 0 for m in masses.values())
    return {''.join(str((mask >> i) & 1) for i in range(5)): mass
            for mask, mass in masses.items() if mass}


def main():
    factors = {label: squarefree_factors(n) for label, n in ROWS.items()}
    assert factors[8, 2] == factors[1, 0] == factors[16, 6] == {17}
    assert factors[8, 6] == factors[2, 0] == {3, 11}
    assert factors[16, 10] == factors[1, 0] ^ factors[2, 1] == {17, 41}
    certificate = peel({i: row for i, row in factors.items() if i not in DUPLICATES})
    assert len(certificate) == 27
    support = sorted(set.union(*factors.values()))
    assert len(support) == 29 and {3, 5} <= set(support)
    assert all(n % 8 == 1 for n in ROWS.values())
    assert len({3**a * 5**b % 8 for a, b in product(range(2), repeat=2)}) == 4
    gauge = {
        "minus_one": [p for p in support if p % 4 == 3],
        "two": [p for p in support if p % 8 in (3, 5)],
    }
    for row in factors.values():
        assert all(len(row & set(negative)) % 2 == 0 for negative in gauge.values())
    law = compressed_law()
    assert exact_profile_law(factors) == law
    assert len(law) == 16 and sum(law.values()) == 1
    assert law['11110'] == Fraction(1, 2**13) and law['10111'] == Fraction(1, 2**27)
    assert max(key.count('1') for key in law) == 4
    assert all(sum(p for key, p in law.items() if key[i] == '1') == Fraction(1, 2**k)
               for i, k in enumerate(GAPS))
    small = [q for q in range(35, 502) if is_prime(q)]
    for q in small:
        assert all(direct_original(k, q) == saturation(k, q) for k in GAPS)
        assert profile(q) in law
    witnesses = {3191: '11110', 1599326581: '10111'}
    for q, observed in witnesses.items():
        assert is_prime(q) and profile(q) == observed
    assert all(direct_original(k, 3191) == saturation(k, 3191) for k in GAPS)
    exceptional = sorted({p for n in ROWS.values() for p in range(35, n+1)
                          if n % p == 0 and is_prime(p)})
    assert all(profile(q) in law for q in exceptional)
    print(json.dumps({
        "identity": "five-gap same-prime comparator, q prime >=35, s=q-2k",
        "gap_order": GAPS,
        "joint_squareclass_rank": len(certificate),
        "support_primes": support,
        "four_prime_sign_extensions_generated_by": gauge,
        "independent_rows_private_prime_peel": certificate,
        "equalities_N": ["153=9*17", "297=9*33", "425=25*17", "697=17*41"],
        "profile_prime_densities": {key: str(p) for key, p in law.items()},
        "four_saturation_primes": witnesses,
        "trial_division_witness_bounds": {q: isqrt(q) for q in witnesses},
        "direct_original_map_regressions": 5*(len(small)+1),
        "direct_prime_ranges": ["35..501", "3191"],
        "ramified_primes_in_range_and_profile": {q: profile(q) for q in exceptional}
    }, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
