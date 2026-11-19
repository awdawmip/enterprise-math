"""Exact signed matching counts for prime-power labels; standard Python."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial, gcd
import json


def valuation(t, p):
    assert t
    h = 0
    while t % p == 0:
        t //= p
        h += 1
    return h


def signed_buckets(u, v, q):
    states = {0: [1] + [0] * (q - 1)}
    for x in u:
        new = {}
        for mask, row in states.items():
            for j, y in enumerate(v):
                if mask >> j & 1:
                    continue
                sign = (-1) ** ((mask >> (j + 1)).bit_count())
                output = new.setdefault(mask | 1 << j, [0] * q)
                shift = x * y % q
                for z, c in enumerate(row):
                    output[(shift + z) % q] += sign * c
        states = new
    return next(iter(states.values()))


def permutation_counts(u, v, q):
    even = [0] * q
    odd = [0] * q
    for perm in permutations(range(len(u))):
        parity = sum(a > b for a, b in combinations(perm, 2)) % 2
        index = sum(x * v[i] for x, i in zip(u, perm)) % q
        (even, odd)[parity][index] += 1
    return [a - b for a, b in zip(even, odd)]


def occupancy(v, d):
    row = [0] * d
    for a in v:
        row[a % d] += 1
    return row


def unbalanced(v, p, k):
    for j in range(1, k + 1):
        d = p ** j
        c = occupancy(v, d)
        if max(c) - min(c) > 1:
            return d
    return 0


def killing_set(n, q, d):
    rows, tail = divmod(n, d)
    return sorted([s + h * (q // d) for s in range(rows) for h in range(d)]
                  + [rows + h * (q // d) for h in range(tail)])


def interior_data(u, v, p, k):
    n, q, phi = len(u), p ** k, (p - 1) * p ** (k - 1)
    weight, leading = 0, 1
    for a, b in combinations(u, 2):
        jump = p ** valuation(b - a, p)
        weight += jump
        leading *= (b - a) // jump
    level = max(0, (weight - q // p) // phi)
    degree = weight - level * phi
    schur = Fraction(1)
    for i, j in combinations(range(n), 2):
        schur *= Fraction(v[j] - v[i], j - i)
    assert schur.denominator == 1 and schur.numerator % p
    leading *= (-1) ** level * schur.numerator
    return weight, level, degree, leading % p


def verify(table, u, v, p, k):
    weight, level, degree, lead = interior_data(u, v, p, k)
    assert valuation(gcd(*table), p) == level
    reduced = [z // p ** level % p for z in table]
    jet = [sum(c * comb(i, j) for i, c in enumerate(reduced) if i >= j) % p
           for j in range(degree + 1)]
    assert jet == [0] * degree + [lead]
    return dict(weight=weight, content_exponent=level, first_degree=degree, first_coefficient=lead)


def reverse_digits(x, p, k):
    y = 0
    for _ in range(k):
        x, digit = divmod(x, p)
        y = y * p + digit
    return y


def maximum(n, p, k):
    q = p ** k
    ans = comb(n, 2)
    for j in range(1, k):
        d = p ** j
        cap = q // d
        full, last = divmod(n, cap)
        ans += (d - d // p) * (full * comb(cap, 2) + comb(last, 2))
    return ans


def main():
    exhaustive = []
    for p, k in [(2, 2), (2, 3), (3, 2)]:
        q = p ** k
        cases, kills, direct = 0, 0, 0
        for n in range(2, q + 1):
            subsets = list(combinations(range(q), n))
            # The all-pairs checks use a common translation of each table.
            # It only induces an additive permutation (unit shift) of buckets.
            origins = [s for s in subsets if s[0] == 0]
            assert max(sum(p ** valuation(b-a,p) for a,b in combinations(s,2))
                       for s in subsets) == maximum(n,p,k)
            for v in origins:
                d = unbalanced(v, p, k)
                if d:
                    u = killing_set(n, q, d)
                    assert not any(signed_buckets(u, v, q))
                    kills += 1
                    continue
                for u in origins:
                    row = signed_buckets(u, v, q)
                    verify(row, u, v, p, k)
                    if n <= 4:
                        assert row == permutation_counts(u, v, q)
                        direct += 1
                    cases += 1
        exhaustive.append(dict(q=q, balanced_pairs=cases, zero_witnesses=kills,
                               direct_permutation_comparisons=direct))
    examples = []
    for p,k,n in [(2,4,6), (2,4,8), (3,3,8), (5,2,7), (2,5,9)]:
        q = p**k
        u = sorted(reverse_digits(j,p,k) for j in range(n))
        v = list(range(n))
        assert maximum(n,p,k) == interior_data(u,v,p,k)[0]
        row = signed_buckets(u,v,q)
        examples.append(dict(q=q,n=n,u=u,v=v,**verify(row,u,v,p,k),gcd=gcd(*row)))
    # Nonbalanced is not a pairwise obstruction. The same distinct V at modulus
    # eight survives one distinct table but fails against the crafted adversary.
    v = [0,2,4]
    regular, blind = [0,1,2], killing_set(3,8,2)
    rows = [permutation_counts(u,v,8) for u in [regular,blind]]
    assert any(rows[0]) and not any(rows[1])
    return dict(exhaustive=exhaustive, maximum_examples=examples,
                fixed_v_example=dict(v=v,live_u=regular,dead_u=blind,signed=rows))


if __name__ == '__main__':
    print(json.dumps(main(), ensure_ascii=False, indent=2))
