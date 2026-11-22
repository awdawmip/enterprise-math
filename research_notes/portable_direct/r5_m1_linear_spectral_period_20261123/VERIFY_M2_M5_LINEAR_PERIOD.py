"""Exact m=2..5 extension of the R5 scalar linear-coefficient period theorem.
Run beside VERIFY_M1_LINEAR_PERIOD.py. Python 3 standard library only.
"""
from itertools import product
import VERIFY_M1_LINEAR_PERIOD as base

EXPECTED = {
    2: (5,105,73,187,9,35,15,124,22,7,75,138,74,140,127,507,351,231),
    3: (93,29,96,28,5,12,13,25,4,5,171,127,47,62,244,240,324,26),
    4: (53,66,93,25,15,9,12,149,20,11,117,38,52,128,202,594,10,104),
    5: (79,92,90,80,12,44,95,3,8,40,57,121,1,90,136,350,115,206),
}

def overlap_numerator(m, p, z):
    """Union of E0,E1,E2; enumerate each genuine simultaneous load constraint."""
    answer = 0
    for mask in range(1, 8):
        chosen = [j for j in range(3) if mask & (1 << j)]
        support = sorted(set().union(*(base.EVENTS[j] for j in chosen)))
        powers = [tuple(pow(z, price * count, p) for count in range(m)) for price in support]
        load_indices = [[i for i, price in enumerate(support) if price in base.EVENTS[j]] for j in chosen]
        restricted = 0
        for counts in product(range(m), repeat=len(support)):
            if any(sum(counts[i] for i in indices) >= m for indices in load_indices):
                continue
            monomial = 1
            for i, count in enumerate(counts):
                monomial = monomial * powers[i][count] % p
            restricted = (restricted + monomial) % p
        answer = (answer + (1 if len(chosen) % 2 else -1) * restricted * base.block(support, p, z)) % p
    return answer

def complete_h_prefix(m, support, p, z):
    """Sum of complete homogeneous h_j, j<m, with unlimited item multiplicity."""
    h = [1] + [0] * (m - 1)
    for price in sorted(support):
        x = pow(z, price, p)
        for j in range(1, m):
            h[j] = (h[j] + x * h[j - 1]) % p
    return sum(h) % p

def disjoint_block_numerator(m, index, p, z):
    support = base.EVENTS[index]
    return base.block(support, p, z) * complete_h_prefix(m, support, p, z) % p

for m, expected_values in EXPECTED.items():
    values = []
    for d, p, z, previous in base.CERT:
        a = overlap_numerator(m, p, z)
        b = disjoint_block_numerator(m, 3, p, z)
        c = disjoint_block_numerator(m, 4, p, z)
        value = (1 - (1 - a) * (1 - b) * (1 - c)) % p
        values.append(value)
        assert value != 0, (m, d)
    assert tuple(values) == expected_values, (m, values)
    print(f"m={m}: all 18 exact primitive-root witnesses nonzero, values={tuple(values)}")
print("PASS: m=1..5 attain Lambda_1=814202665467037976682352800")
