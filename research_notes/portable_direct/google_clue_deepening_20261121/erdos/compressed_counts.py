"""Exact Erdős #1063 singleton counts from finite base-p digit arithmetic.

New author-side exploratory derivation, 2026-11-21; not independently reviewed.
Original population, period, CRT product, and reflection are due to the source
EM-DIRECT-3DCA45 at enterprise-math commit
ab4699ad2a80b0e040c5a5f287cd34a537d75e6f.  This file does not replace that source.
The new steps are the closed local counts z_p and a_{p,i}; see THEOREM.md.
No local residue period is enumerated here.  All arithmetic is exact integer.
"""

from math import isqrt


def primes(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p:n + 1:p] = b"\x00" * ((n - p * p) // p + 1)
    return [p for p in range(2, n + 1) if sieve[p]]


def floor_log(n, p):
    answer = 0
    while n >= p:
        n //= p
        answer += 1
    return answer


def factorial_valuation(n, p):
    answer = 0
    while n:
        n //= p
        answer += n
    return answer


def local_counts(k, p, modulus=None):
    """Return (z_p, [a_{p,0},...,a_{p,k-1}], auxiliary exact integers).

    p must be prime and <= k.  With a modulus, count values are reduced but
    exponents and factorial valuations remain their ordinary exact integers.
    """
    assert k >= 2 and 2 <= p <= k
    h = floor_log(k, p)
    m = floor_log(k // 2, p)
    e = h + m
    tail = k
    digit_factor = tail % p
    tail //= p
    for _ in range(1, h):
        digit_factor *= 1 + tail % p
        tail //= p
    power = (lambda x: p ** x) if modulus is None else (lambda x: pow(p, x, modulus))
    z = power(m) * digit_factor
    if modulus is not None:
        z %= modulus
    valuations = [factorial_valuation(i, p) for i in range(k)]
    ak = factorial_valuation(k, p)
    singleton = []
    exponents = []
    deficits = []
    for i in range(k):
        b = floor_log(max(i, k - 1 - i), p)
        d = ak - valuations[i] - valuations[k - 1 - i]
        deficits.append(d)
        if d == 0:
            singleton.append(0)
            exponents.append(None)
        else:
            exponent = e - b - d
            assert d > 0 and exponent >= 0
            singleton.append(power(exponent))
            exponents.append(exponent)
    return z, singleton, {"h": h, "m": m, "e": e,
                           "digit_factor": digit_factor,
                           "deficits": deficits,
                           "singleton_exponents": exponents}


def count_positions(k, modulus=None):
    """Exact N_i, or their residues modulo modulus, over the named period P_k."""
    assert k >= 2 and (modulus is None or modulus >= 1)
    columns = [1] * k
    empty = 1
    for p in primes(k):
        z, a, _ = local_counts(k, p, modulus)
        columns = [value * (z + single) for value, single in zip(columns, a)]
        empty *= z
        if modulus is not None:
            columns = [value % modulus for value in columns]
            empty %= modulus
    # empty=0 for k>=2, because any p|k has z_p=0.  Keep the general CRT
    # subtraction visible to document exactly which joint event is counted.
    result = [value - empty for value in columns]
    return result if modulus is None else [value % modulus for value in result]


if __name__ == "__main__":
    import argparse
    import json
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("k", type=int)
    parser.add_argument("--modulus", type=int)
    args = parser.parse_args()
    columns = count_positions(args.k, args.modulus)
    total = sum(columns)
    if args.modulus is not None:
        total %= args.modulus
    print(json.dumps({"k": args.k, "modulus": args.modulus,
                      "H": total, "N": columns}, indent=2))
