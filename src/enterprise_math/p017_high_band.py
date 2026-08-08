"""High least-factor consequences for P017 rough cofactor windows.

This module adds no new sieve machinery.  It combines the already-proved exact
P017 cofactor window with the high-band contraction p^2 >= 2k.  In that band a
second least-prime-factor branch is a single binary quotient-response event, and
distinct p-rough cofactor survivors are pairwise coprime.
"""

from __future__ import annotations

from math import gcd, isqrt

from .factor_precision import smallest_prime_factor
from .legendre import is_prime, primes_up_to
from .p017_cofactor_window import cofactor_window_survivors
from .p017_rough_recursion import high_least_factor_band


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def high_band_second_factor_candidate(k: int, prime: int, second_prime: int) -> dict[str, object]:
    """Return the unique possible second-factor branch in the high band.

    For parent cofactor interval [A,B] of length N<=p and prime ell>=p, the
    multiple count is

        floor(N/ell) + carry_ell((A-1) mod ell, N mod ell) in {0,1}.

    If it is one, the unique raw multiple is q=A+d with d=(-A) mod ell.  It
    gives a genuine three-prime P017 state exactly when q/ell is a prime >=ell.
    """
    _require_positive("k", k)
    _require_positive("prime", prime)
    _require_positive("second_prime", second_prime)
    data = high_least_factor_band(k, prime)
    A = int(data["q_min"])
    B = int(data["q_max"])
    N = int(data["parent_length"])

    if second_prime < prime or second_prime not in primes_up_to(isqrt(B)):
        raise ValueError("second_prime must be a prime in [p, floor(sqrt(q_max))]")
    if N > prime or prime > second_prime:
        raise AssertionError("high-band ordering invariant failed")

    bulk = N // second_prime
    carry = (((A - 1) % second_prime) + (N % second_prime)) // second_prime
    multiple_count = bulk + carry
    if multiple_count not in (0, 1):
        raise AssertionError("high-band branch is not binary")

    step = (-A) % second_prime
    residue_hit = step < N
    if residue_hit != (multiple_count == 1):
        raise AssertionError("residue-hit and quotient-response branch tests disagree")

    candidate_q = A + step if residue_hit else None
    candidate_tail = None
    triple_state = None
    if candidate_q is not None:
        if candidate_q % second_prime != 0 or not (A <= candidate_q <= B):
            raise AssertionError("binary branch candidate left the parent interval")
        candidate_tail = candidate_q // second_prime
        if candidate_tail >= second_prime and is_prime(candidate_tail):
            triple_state = prime * candidate_q

    canonical_triples = set(data["triple_prime_states"])
    if triple_state is not None and triple_state not in canonical_triples:
        raise AssertionError("binary candidate produced a noncanonical triple state")
    if triple_state is None:
        # If this ell really occurs as the second least prime of a canonical
        # triple state, the candidate test must have found it.
        for n in canonical_triples:
            q = n // prime
            if smallest_prime_factor(q) == second_prime:
                raise AssertionError("binary candidate missed a canonical triple state")

    return {
        "prime": prime,
        "second_prime": second_prime,
        "A": A,
        "B": B,
        "N": N,
        "bulk": bulk,
        "carry": carry,
        "multiple_count": multiple_count,
        "residue_step": step,
        "candidate_q": candidate_q,
        "candidate_tail": candidate_tail,
        "triple_state": triple_state,
    }


def high_band_pairwise_coprime(k: int, prime: int) -> dict[str, object]:
    """Verify distinct p-rough cofactor survivors are pairwise coprime.

    The high-band parent window has length N<=p.  A common prime divisor of two
    distinct p-rough values would be >=p and divide their nonzero difference,
    whose absolute value is <p; impossible.
    """
    data = high_least_factor_band(k, prime)
    survivors = cofactor_window_survivors(k, prime)
    if int(data["parent_length"]) > prime:
        raise AssertionError("pairwise-coprime theorem used outside N<=p band")

    for i, left in enumerate(survivors):
        for right in survivors[i + 1 :]:
            if gcd(left, right) != 1:
                raise AssertionError("distinct high-band p-rough cofactors share a prime factor")
            if gcd(prime * left, prime * right) != prime:
                raise AssertionError("high-band shell states share more than the common factor p")

    return {
        "prime": prime,
        "survivors": survivors,
        "pairwise_coprime": True,
    }


def high_band_triple_resource_bound(k: int, prime: int) -> dict[str, object]:
    """Bound all three-prime branches by a finite prime-resource interval.

    For n=p*ell*s in the band p^2>=2k, ell and s are primes with
    p<=ell<=s<=K=floor(U/p^2).  Different cofactor survivors are pairwise
    coprime, so their prime supports are disjoint.  A square cofactor ell^2 can
    occur at most once because the parent interval has length <=p while gaps
    between distinct squares with roots >=p exceed p.

    Hence if R counts primes in [p,K] and T is the number of three-prime shell
    states, 2T-E<=R with E in {0,1}; in particular T<=floor((R+1)/2).
    """
    data = high_least_factor_band(k, prime)
    high_band_pairwise_coprime(k, prime)
    upper = (k + 1) * (k + 1) - 1
    K = upper // (prime * prime)
    resources = [q for q in primes_up_to(K) if q >= prime]
    resource_set = set(resources)

    triples = list(data["triple_prime_states"])
    used_support: set[int] = set()
    square_branches = 0
    detailed: list[tuple[int, int, int]] = []

    for n in triples:
        q = n // prime
        ell = smallest_prime_factor(q)
        tail = q // ell
        if not (prime <= ell <= tail <= K):
            raise AssertionError("three-prime factors left the finite resource interval")
        if not is_prime(ell) or not is_prime(tail):
            raise AssertionError("three-prime resource factor is not prime")
        support = {ell, tail}
        if used_support.intersection(support):
            raise AssertionError("distinct high-band triple states reuse a cofactor prime resource")
        used_support.update(support)
        if ell == tail:
            square_branches += 1
        detailed.append((n, ell, tail))

    if square_branches > 1:
        raise AssertionError("a length<=p high-band window contains multiple square cofactors")
    if not used_support.issubset(resource_set):
        raise AssertionError("used triple-prime support exceeds available resource primes")

    T = len(triples)
    used_count = len(used_support)
    if used_count != 2 * T - square_branches:
        raise AssertionError("triple-prime resource accounting failed")
    R = len(resources)
    if used_count > R:
        raise AssertionError("triple states consume more distinct primes than available")
    bound = (R + 1) // 2
    if T > bound:
        raise AssertionError("triple-prime resource bound failed")

    return {
        "prime": prime,
        "K": K,
        "resource_primes": resources,
        "resource_count": R,
        "triple_states": triples,
        "triple_details": detailed,
        "square_branches": square_branches,
        "used_resource_count": used_count,
        "triple_bound": bound,
    }
