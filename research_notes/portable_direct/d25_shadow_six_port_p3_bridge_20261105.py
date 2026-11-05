#!/usr/bin/env python3
"""D25 signed 216 integer-shadow six-port exact regression. Python 3 stdlib."""
from math import comb, factorial, isqrt

def primes_1mod6(limit):
    for p in range(7, limit + 1, 6):
        if all(p % q for q in range(2, isqrt(p) + 1)):
            yield p

def direct_W(p):
    modulus = p ** 3
    term, total = 1, 0
    for k in range(p):
        total = (total + (6 * k + 1) * term) % modulus
        if k < p - 1:
            term = (term * (2*k+1) * (3*k+1) * (3*k+2)
                    * pow(36 * (k+1)**3, -1, modulus)) % modulus
    return total

def six_ports(p):
    n = (p - 1) // 6
    modulus = p ** 3
    mod2 = p ** 2
    ports = [0] * 6
    mvals = (3*n, 2*n, 4*n)
    harmonic = [0, 0, 0]
    harmonic2 = [0, 0, 0]
    inv2 = pow(2, -1, mod2)
    inv3 = pow(3, -1, mod2)
    slopes = [inv2, inv3, 2 * inv3 % mod2]

    for k in range(2*n + 1):
        if k:
            for j, m in enumerate(mvals):
                inverse = pow(m-k+1, -1, mod2)
                harmonic[j] = (harmonic[j] - inverse) % mod2
                harmonic2[j] = (harmonic2[j] + inverse * inverse) % mod2
        linear = sum(slopes[j] * harmonic[j] for j in range(3)) % mod2
        squared = sum(slopes[j]**2 * harmonic2[j] for j in range(3)) % p
        base = ((-1)**k * comb(3*n, k) * comb(2*n, k)
                * comb(4*n, k) * pow(2, -k, modulus)) % modulus
        weight = 6*k+1
        ports[0] = (ports[0] + weight * base) % modulus
        ports[1] = (ports[1] + weight * base * linear) % mod2
        ports[3] = (ports[3] + weight * base * (
            linear**2 - squared) * pow(2, -1, p)) % p

    for k in range(2*n+1, 3*n+1):
        mid = (comb(3*n, k) * comb(4*n, k)
               * factorial(2*n) * factorial(k-2*n-1))
        mid = mid * pow(3 * 2**k * factorial(k), -1, mod2) % mod2
        hzero = (sum(pow(j,-1,p) for j in range(1,k-2*n))
                 - sum(pow(j,-1,p) for j in range(1,2*n+1))) % p
        h3 = sum(pow(j,-1,p) for j in range(3*n-k+1,3*n+1)) % p
        h4 = sum(pow(j,-1,p) for j in range(4*n-k+1,4*n+1)) % p
        shift = ((hzero * pow(3,-1,p) - h3 * pow(2,-1,p)
                  - h4 * 2 * pow(3,-1,p))) % p
        weight = 6*k+1
        ports[2] = (ports[2] + weight * mid) % mod2
        ports[4] = (ports[4] + weight * (mid % p) * shift) % p

    for k in range(3*n+1, 4*n+1):
        top = ((-1)**(3*n+k) * factorial(2*n) * factorial(3*n)
               * factorial(k-2*n-1) * factorial(k-3*n-1)
               * comb(4*n, k))
        top = (top * pow(6 * 2**k * factorial(k)**2, -1, p)) % p
        ports[5] = (ports[5] + (6*k+1) * top) % p

    S,A,B,C,D,E = ports
    reconstructed = (S + p*(A+B) + p*p*(C+D+E)) % modulus
    return reconstructed, ports

def check(limit=1200):
    count = 0
    for p in primes_1mod6(limit):
        independent = direct_W(p)
        reconstructed, ports = six_ports(p)
        assert independent == reconstructed, (p, independent, reconstructed)
        S,A,B,C,D,E = ports
        Z = (S + p*(A+B) - p) % (p**3)
        if p in (7,13,19,37,61,373):
            print("p",p, "W",independent, "ports",ports,
                  "Zmodp2",Z%(p*p),
                  "Z_over_p2", Z//(p*p) if Z%(p*p)==0 else None,
                  "CDE", (C+D+E)%p)
        count += 1
    print("PASS", count, "primes 7<=p<=", limit, "p=1 mod6")

if __name__ == "__main__":
    check()
