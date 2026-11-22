"""R5 m=1: exact cyclotomic lower witnesses for degree >=1 coefficient period.
Frozen scalar model: enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15.
No floating point, external packages, or web access.
"""
from math import isqrt, lcm

PRICES = range(214, 315)
EVENTS = (
    set((214, 215, 216, 217, 218)),
    set((214, 216, 217, 218, 219, 220, 221)),
    set((215, 216, 217, 218, 219, 220, 221)),
    set(range(223, 291)),
    set(range(296, 313)),
)
# Each row is (primitive order d, prime p, primitive root z, R_1(z) mod p).
CERT = (
    (32, 97, 28, 59),
    (54, 109, 36, 95),
    (25, 101, 16, 84),
    (49, 197, 16, 31),
    (11, 23, 4, 14),
    (13, 53, 16, 41),
    (17, 103, 64, 71),
    (19, 191, 69, 103),
    (23, 47, 4, 20),
    (29, 59, 4, 58),
    (62, 311, 264, 231),
    (37, 149, 16, 106),
    (41, 83, 4, 31),
    (43, 173, 16, 35),
    (47, 283, 64, 196),
    (59, 709, 551, 360),
    (61, 367, 64, 238),
    (73, 293, 16, 117),
)

def prime_divisors(n):
    found = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            found.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        found.append(n)
    return found

def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))

def block(support, p, z):
    value = 1
    for price in sorted(support):
        value = value * (1 - pow(z, price, p)) % p
    return value

def r1_inclusion_exclusion(p, z):
    total = 0
    for mask in range(1, 1 << len(EVENTS)):
        support = set().union(*(EVENTS[j] for j in range(len(EVENTS)) if mask & (1 << j)))
        value = block(support, p, z)
        total = (total + (1 if mask.bit_count() % 2 else -1) * value) % p
    return total

def r1_factored(p, z):
    a = 0
    for mask in range(1, 8):
        support = set().union(*(EVENTS[j] for j in range(3) if mask & (1 << j)))
        value = block(support, p, z)
        a = (a + (1 if mask.bit_count() % 2 else -1) * value) % p
    b, c = (block(EVENTS[j], p, z) for j in (3, 4))
    return (1 - (1 - a) * (1 - b) * (1 - c)) % p

def orders_with_poles_of_order_at_least(k):
    return [d for d in range(1, 315) if sum(price % d == 0 for price in PRICES) >= k]

lambda_1 = lcm(*orders_with_poles_of_order_at_least(2))
lambda_2 = lcm(*orders_with_poles_of_order_at_least(3))
assert lambda_1 == 814202665467037976682352800
assert lambda_2 == 229746052653717600
assert lambda_1 // lambda_2 == 3543924503
assert lambda_1 == lcm(*(row[0] for row in CERT))

print("order d | multiples | p | z | R1(z) mod p")
for d, p, z, expected in CERT:
    assert is_prime(p) and (p - 1) % d == 0
    assert pow(z, d, p) == 1
    assert all(pow(z, d // prime, p) != 1 for prime in prime_divisors(d))
    multiplicity = sum(price % d == 0 for price in PRICES)
    assert multiplicity >= 2
    observed = r1_inclusion_exclusion(p, z)
    assert observed == r1_factored(p, z) == expected != 0
    print(f"{d:7d} | {multiplicity:9d} | {p:3d} | {z:3d} | {observed:11d}")

print("PASS: 18/18 primitive nonzero finite-field witnesses, double independent event formulas")
print(f"Lambda_1 = {lambda_1}; Lambda_2 = {lambda_2}; ratio={lambda_1//lambda_2}")
