# Regression-only checker for the exact twist identity.
from math import isqrt

def prime(n):
    if n < 2: return False
    for d in range(2, isqrt(n)+1):
        if n % d == 0: return False
    return True

count = 0
for p in range(5, 5000):
    if not prime(p) or p % 24 not in (13, 19):
        continue
    D = 2 ** ((p-1)//2)
    assert (D + 1) % p == 0
    tau = ((D + 1)//p) % p
    assert D % (p*p) == (-1 + p*tau) % (p*p)
    for K in (0, 1, p-1, p//2):
        C = (-p + p*p*K) % (p**3)
        lhs = (C * pow(D, -1, p**3)) % (p**3)
        rhs = (p + p*p*((tau-K) % p)) % (p**3)
        assert lhs == rhs
        count += 1
assert count == 664
print('PASS', count)
