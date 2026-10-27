#!/usr/bin/env python3
"""D25 author-side exact finite falsifier, NOT a native H0/B0 experiment.

Carrier: original weighted {}_3F_2 p-adic scalar W_p, via integer binomials.
Scope: every prime p < 30000 with p % 24 in (13, 19).
Arithmetic: exact Python integer modular inverses (no floating point).
This is finite evidence, NOT a uniform supercongruence proof or accepted Result.
"""

from hashlib import sha256
from math import comb, isqrt

BOUND = 30000


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def original_binomial_coefficient(k: int, modulus: int) -> int:
    """A_k = binom(2k,k)^2 binom(3k,k)/216^k mod p^3."""
    return (comb(2*k, k)**2 * comb(3*k, k)
            * pow(pow(216, k, modulus), -1, modulus)) % modulus


def weighted_sum_via_recurrence(p: int, crosscheck: bool = False) -> int:
    """Exact W_p mod p^3; step ratios have unit denominator for k<p-1."""
    assert is_prime(p) and p > 3
    modulus = p**3
    coeff, value = 1, 0
    samples = set()
    if crosscheck:
        samples = {0, 1, (p-1)//6, (p-1)//3, (p-1)//2,
                   2*(p-1)//3, p-1}
    for k in range(p):
        if k in samples:
            assert coeff == original_binomial_coefficient(k, modulus), (p, k)
        value = (value + (6*k+1)*coeff) % modulus
        if k + 1 < p:
            numerator = (2*k+1)*(3*k+1)*(3*k+2)
            denominator = 36*(k+1)**3
            # p does not divide 36*(k+1)^3: 0<=k<p-1 and p>=5.
            coeff = (coeff * numerator * pow(denominator, -1, modulus)) % modulus
    return value


def independent_full_binomial_sum(p: int) -> int:
    """Second arithmetic path; used for selected small p only."""
    modulus = p**3
    return sum((6*k+1)*original_binomial_coefficient(k, modulus)
               for k in range(p)) % modulus


def run() -> None:
    targets = [p for p in range(5, BOUND) if p % 24 in (13, 19) and is_prime(p)]
    assert targets[0] == 13 and targets[-1] == 29989
    h = sha256()
    trace = []
    independent_primes = {13, 19, 373, 10069, 29989}
    for p in targets:
        observed = weighted_sum_via_recurrence(p, crosscheck=p in independent_primes)
        if p in (13, 19, 373):
            assert independent_full_binomial_sum(p) == observed
        triple = f"{p}:{observed}:{p**3}\n".encode('ascii')
        h.update(triple)
        if p in independent_primes:
            trace.append((p, observed, p**3))
        if observed != p:
            raise AssertionError(f"COUNTEREXAMPLE p={p}: W_p={observed} mod {p**3}, expected {p}")
    assert len(targets) == 815, len(targets)
    print('RESULT=FINITE_EXHAUSTIVE_PASS_NOT_UNIFORM_THEOREM')
    print(f'BOUND_EXCLUSIVE={BOUND}')
    print(f'TARGET_PRIME_COUNT={len(targets)}')
    print(f'FIRST_LAST_TARGET={targets[0]},{targets[-1]}')
    print(f'RECORD_SHA256={h.hexdigest()}')
    for p, observed, modulus in trace:
        print(f'EXACT_SAMPLE p={p} W_mod_p3={observed} modulus={modulus}')
    print('NATIVE_H0B0=NOT_EXECUTED')
    print('SOURCE_NATIVE_CLAIM_OR_RESULT=NONE_FROM_THIS_SCRIPT')


if __name__ == '__main__':
    run()
