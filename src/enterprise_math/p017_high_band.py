"""High least-factor consequences for P017 rough cofactor windows.

This module adds no new sieve machinery.  It combines the already-proved exact
P017 cofactor window with the high-band contraction p^2 >= 2k.  In that band a
second least-prime-factor branch is a single binary quotient-response event, and
distinct p-rough cofactor survivors are pairwise coprime.

It also verifies that the newer cofactor-window representation is exactly the
positive least-factor form of the older P017 square-basin hit-count machinery:
raw window length is H_p(k), and a second-factor branch is H_{p*ell}(k).
"""

from __future__ import annotations

from math import gcd, isqrt

from .factor_precision import smallest_prime_factor
from .legendre import interior_hit_count, is_prime, primes_up_to
from .p017_cofactor_window import centered_cofactor_window, cofactor_window_survivors
from .p017_rough_recursion import high_least_factor_band


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _integer_power_capacity(base: int, limit: int) -> int:
    """Return max t>=0 with base**t <= limit using integer arithmetic only."""
    _require_positive("base", base)
    _require_positive("limit", limit)
    exponent = 0
    power = 1
    while power <= limit // base:
        power *= base
        exponent += 1
    return exponent


def _unique_large_modulus_hit(k: int, modulus: int) -> int | None:
    """Return the unique square-basin multiple when modulus>=2k, if it exists."""
    _require_positive("k", k)
    _require_positive("modulus", modulus)
    if modulus < 2 * k:
        raise ValueError("unique-hit helper requires modulus >= 2k")
    center = k * (k + 1)
    residue = center % modulus
    if residue < k:
        return center - residue
    if residue >= modulus - k:
        return center + (modulus - residue)
    return None


def _high_band_triple_primes(k: int) -> list[int]:
    """Return least primes that can support a high-band three-prime state."""
    _require_positive("k", k)
    upper = (k + 1) * (k + 1) - 1
    return [
        p
        for p in primes_up_to(k)
        if p * p >= 2 * k and p**3 <= upper
    ]


def cofactor_window_hit_identity(k: int, prime: int) -> dict[str, int]:
    """Identify W_p(k) with the quotient image of p-multiples in the square basin."""
    _require_positive("k", k)
    _require_positive("prime", prime)
    if prime not in primes_up_to(k):
        raise ValueError("prime must be a prime <= k")

    data = centered_cofactor_window(k, prime)
    direct_A = (k * k) // prime + 1
    direct_B = (((k + 1) * (k + 1)) - 1) // prime
    direct_N = interior_hit_count(k, prime, 2)

    if int(data["q_min"]) != direct_A or int(data["q_max"]) != direct_B:
        raise AssertionError("centered cofactor window disagrees with direct quotient endpoints")
    if int(data["raw_count"]) != direct_N:
        raise AssertionError("cofactor window length disagrees with square-basin hit count H_p(k)")

    return {
        "prime": prime,
        "A": direct_A,
        "B": direct_B,
        "N": direct_N,
    }


def high_band_second_factor_candidate(k: int, prime: int, second_prime: int) -> dict[str, object]:
    """Return the unique possible second-factor branch in the high band.

    For parent cofactor interval [A,B] of length N<=p and prime ell>=p, the
    multiple count is

        floor(N/ell) + carry_ell((A-1) mod ell, N mod ell) in {0,1}.

    If it is one, the unique raw multiple is q=A+d with d=(-A) mod ell.  It
    gives a genuine three-prime P017 state exactly when q/ell is a prime >=ell.

    The same bit is exactly the older P017 square-basin hit count H_{p*ell}(k),
    because q divisible by ell is equivalent to n=p*q divisible by p*ell.
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

    old_hit_count = interior_hit_count(k, prime * second_prime, 2)
    if old_hit_count != multiple_count:
        raise AssertionError("second-factor branch disagrees with legacy H_{p*ell}(k) hit count")

    candidate_q = A + step if residue_hit else None
    candidate_tail = None
    candidate_state = None
    triple_state = None
    if candidate_q is not None:
        if candidate_q % second_prime != 0 or not (A <= candidate_q <= B):
            raise AssertionError("binary branch candidate left the parent interval")
        candidate_state = prime * candidate_q
        if candidate_state % (prime * second_prime) != 0:
            raise AssertionError("candidate state lost the p*ell modulus hit")
        candidate_tail = candidate_q // second_prime
        if candidate_tail >= second_prime and is_prime(candidate_tail):
            triple_state = candidate_state

    # Recover the same unique large-modulus hit directly from the common square
    # center M=k(k+1).  In the high band p*ell>=2k, the 2k-state basin can contain
    # at most one multiple of the modulus.
    modulus = prime * second_prime
    center_hit = _unique_large_modulus_hit(k, modulus)
    residue = k * (k + 1) % modulus
    if (center_hit is not None) != (multiple_count == 1):
        raise AssertionError("common-center unique-hit criterion disagrees with branch bit")
    if center_hit is not None and center_hit != candidate_state:
        raise AssertionError("cofactor-window candidate and common-center unique hit differ")

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
        "legacy_hit_count": old_hit_count,
        "residue_step": step,
        "candidate_q": candidate_q,
        "candidate_state": candidate_state,
        "candidate_tail": candidate_tail,
        "center_residue": residue,
        "center_hit": center_hit,
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


def high_band_multiplicative_resource_bound(k: int, prime: int) -> dict[str, object]:
    """Bound high-band three-prime branches by multiplicative resource capacity.

    Let W_p(k)=[A,B], let K=floor(U/p^2), and let P be the product of all
    primes in [p,K].  Distinct three-prime cofactors q_i are pairwise coprime,
    so their prime supports do not reuse resources.  Every non-square q_i uses
    each resource prime once.  At most one square cofactor r^2 can occur; when
    it does, its prime root r is the only resource that needs one extra copy.

    With xi=r for that unique prime square and xi=1 otherwise,

        product(q_i) divides xi*P.

    Since every q_i lies in [A,B], A^T <= product(q_i), where T is the number of
    three-prime states.  Therefore T is at most the largest integer t with
    A^t <= xi*P.  This is computed without logarithms.
    """
    parent = high_least_factor_band(k, prime)
    additive = high_band_triple_resource_bound(k, prime)
    A = int(parent["q_min"])
    B = int(parent["q_max"])
    K = int(additive["K"])
    resources = list(additive["resource_primes"])

    resource_product = 1
    for resource in resources:
        resource_product *= resource

    square_roots = [
        resource
        for resource in resources
        if resource <= isqrt(B) and A <= resource * resource <= B
    ]
    if len(square_roots) > 1:
        raise AssertionError("high-band cofactor window contains multiple prime squares")
    square_allowance = square_roots[0] if square_roots else 1
    resource_limit = square_allowance * resource_product

    triples = list(additive["triple_states"])
    triple_cofactor_product = 1
    for n in triples:
        triple_cofactor_product *= n // prime

    if resource_limit % triple_cofactor_product != 0:
        raise AssertionError("three-prime cofactor product exceeds multiplicative resources")

    T = len(triples)
    if A**T > triple_cofactor_product:
        raise AssertionError("cofactor lower-endpoint product bound failed")
    if triple_cofactor_product > resource_limit:
        raise AssertionError("cofactor product exceeded multiplicative resource limit")

    multiplicative_capacity = _integer_power_capacity(A, resource_limit)
    if T > multiplicative_capacity:
        raise AssertionError("multiplicative resource capacity bound failed")

    additive_bound = int(additive["triple_bound"])
    combined_bound = min(additive_bound, multiplicative_capacity)
    if T > combined_bound:
        raise AssertionError("combined high-band resource bound failed")

    return {
        "prime": prime,
        "A": A,
        "B": B,
        "K": K,
        "resource_primes": resources,
        "resource_product": resource_product,
        "square_allowance": square_allowance,
        "resource_limit": resource_limit,
        "triple_states": triples,
        "triple_cofactor_product": triple_cofactor_product,
        "multiplicative_capacity": multiplicative_capacity,
        "additive_bound": additive_bound,
        "combined_bound": combined_bound,
    }


def high_band_global_hit_union_bound(k: int) -> dict[str, object]:
    """Bound all high-band three-prime states by cross-shell hit unions.

    A triple state n=p*ell*s has cofactor-prime support {ell,s}.  Summed over all
    high-band triple states, the support incidence count is 2T-E, where E counts
    square cofactors ell=s.

    Fix a possible cofactor resource prime r.  If an actual triple state with
    least prime p uses r, then p<=r, p^2*r<=U, and p*r divides that state.  Since
    p*r>=p^2>=2k, the modulus p*r has at most one square-basin hit.  Therefore
    all actual states using r lie inside the union of these exact unique hits as
    eligible p varies.  Calling that union X_r gives

        2T-E <= sum_r |X_r|.

    The square term E is itself exact from the cofactor windows: r^2 in W_p(k)
    with r>=p is automatically p-rough and hence forces the triple state p*r^2.
    """
    _require_positive("k", k)
    upper = (k + 1) * (k + 1) - 1
    least_primes = _high_band_triple_primes(k)
    if not least_primes:
        return {
            "least_primes": [],
            "resource_hit_states": {},
            "resource_capacities": {},
            "support_capacity": 0,
            "square_branches": [],
            "square_branch_count": 0,
            "global_triple_bound": 0,
        }

    max_resource = max(upper // (p * p) for p in least_primes)
    all_resources = primes_up_to(max_resource)
    resource_hit_states: dict[int, tuple[int, ...]] = {}
    resource_capacities: dict[int, int] = {}

    for resource in all_resources:
        hit_states: set[int] = set()
        for prime in least_primes:
            if prime > resource or prime * prime * resource > upper:
                continue
            modulus = prime * resource
            if modulus < 2 * k:
                raise AssertionError("eligible global resource modulus left the high band")
            hit = _unique_large_modulus_hit(k, modulus)
            expected_count = interior_hit_count(k, modulus, 2)
            if expected_count not in (0, 1):
                raise AssertionError("large-modulus global hit count is not binary")
            if (hit is not None) != (expected_count == 1):
                raise AssertionError("global unique-hit state disagrees with H_(p*r)(k)")
            if hit is not None:
                hit_states.add(hit)
        if hit_states:
            ordered = tuple(sorted(hit_states))
            resource_hit_states[resource] = ordered
            resource_capacities[resource] = len(ordered)

    square_branches: list[tuple[int, int, int]] = []
    for prime in least_primes:
        A = (k * k) // prime + 1
        B = upper // prime
        K = upper // (prime * prime)
        roots = [
            resource
            for resource in all_resources
            if prime <= resource <= K and A <= resource * resource <= B
        ]
        if len(roots) > 1:
            raise AssertionError("one high-band cofactor window contains multiple prime squares")
        if roots:
            resource = roots[0]
            state = prime * resource * resource
            if not (k * k < state <= upper):
                raise AssertionError("forced square branch left the square basin")
            square_branches.append((prime, resource, state))

    support_capacity = sum(resource_capacities.values())
    square_branch_count = len(square_branches)
    global_triple_bound = (support_capacity + square_branch_count) // 2

    return {
        "least_primes": least_primes,
        "resource_hit_states": resource_hit_states,
        "resource_capacities": resource_capacities,
        "support_capacity": support_capacity,
        "square_branches": square_branches,
        "square_branch_count": square_branch_count,
        "global_triple_bound": global_triple_bound,
    }
