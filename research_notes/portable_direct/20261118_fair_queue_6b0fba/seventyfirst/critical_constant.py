"""Enclose the critical Euler coefficient with interval arithmetic."""
from math import isqrt
from mpmath import iv

iv.dps = 70
P = 50000

def primes_to(limit):
    sieve = bytearray([1]) * (limit + 1)
    sieve[:2] = bytes(2)
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p*p::p] = bytes((limit - p*p)//p + 1)
    return [i for i, bit in enumerate(sieve) if bit]

def zeta_half_integer(twice_s, terms=100):
    # Euler transform of eta; the transformed differences lie in (0,1)
    # by the positive Laplace integral of n^{-s}. Omitted total <= 2^{-terms}.
    s = iv.mpf(twice_s) / 2
    differences = [iv.mpf(n)**(-s) for n in range(1, terms + 1)]
    eta = iv.mpf(0)
    for k in range(terms):
        eta += differences[0] / 2**(k+1)
        differences = [a-b for a,b in zip(differences,differences[1:])]
    eta += iv.mpf([0,1]) / 2**terms
    return eta / (1-iv.mpf(2)**(1-s))

def critical_coefficient():
    c = zeta_half_integer(5)**2 / (12*zeta_half_integer(3)**2*zeta_half_integer(4))
    for p in primes_to(P):
        t = 1/iv.sqrt(p)
        d = (1-t**3)**2 * (1-t**4)
        # f(t)/G(t)-1 = t^6(t-1)^3(t+1)(2t^5+3t^4+4t^3+4t^2+4t+1)/d
        n = t**6*(t-1)**3*(t+1)*(2*t**5+3*t**4+4*t**3+4*t**2+4*t+1)
        c *= 1 + n/d
    # For t<=1/2, -11t^6 <= n/d <= 0. Thus the tail log is in [-11/P^2,0]
    # by -log(1-x)<=2x and sum_{n>P} n^-3 <= 1/(2 P^2).
    return c * iv.exp(iv.mpf([-11,0])/P**2)

if __name__ == "__main__":
    c = critical_coefficient()
    print("A*",iv.nstr(c,18))
    print("critical dyadic coefficient",iv.nstr(c/3,18))
