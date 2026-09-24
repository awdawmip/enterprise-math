#!/usr/bin/env python3
"""Regression only for the exact source-jet algebra in the companion note."""
from math import isqrt

def prime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n)+1):
        if n % d == 0:
            return False
    return True

checks = 0
for p in range(5, 5000):
    if not prime(p) or p % 24 not in (13, 19):
        continue
    p3 = p**3
    for alpha0, j0, eta in ((2,3,1),(5,7,2),(p-2,p-3,3)):
        alpha = alpha0 % (p*p)
        J = j0 % (p*p)
        c0 = pow((alpha0*j0) % p, -1, p)
        # independent p-adic lift of the exact companion scalar
        c = (c0 + p*((alpha0+j0+1) % p)) % (p*p)
        assert (c*alpha*J - 1) % p == 0
        A = (p*alpha) % p3
        B = (A + c*J) % p3
        P = (A*B) % p3
        assert (P-p) % (p*p) == 0
        traw = ((P-p)//(p*p)) % p
        L = ((c*alpha*J - 1)//p) % p
        assert traw == (alpha*alpha + L) % p

        # Forgetting the first lift of c is not faithful: c -> c+p*eta
        # preserves the first comparison but shifts the second product digit.
        c2 = (c + p*eta) % (p*p)
        assert (c2*alpha*J - 1) % p == 0
        B2 = (A + c2*J) % p3
        P2 = (A*B2) % p3
        traw2 = ((P2-p)//(p*p)) % p
        expected_shift = (eta*alpha*J) % p
        assert (traw2-traw) % p == expected_shift
        checks += 1

assert checks == 498
print('PASS', checks)
