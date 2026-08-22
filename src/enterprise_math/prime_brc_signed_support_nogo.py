"""Prime-BRC signed-support compression boundary.

Owner-local L3 research support on ``research/prime-brc-stage-a``.

This module classifies a sharp no-go for trying to repair the classical parity
problem merely by replacing Boolean BRC with integer-valued coefficients while
still recoalescing branches only when their *current exact square-basin support*
is identical.

Two elementary facts drive the boundary.

1. For 1<=d<=k, the exact hit set

       I_k \cap d Z,  I_k={k^2+1,...,(k+1)^2-1},

   contains at least two consecutive multiples of d.  Hence the map

       d -> I_k \cap d Z

   is injective on [1,k].  Equal nonempty hit sets would have the same first-two
   gap, forcing equal moduli.

2. In the canonical P017 L020 large-prime-tail branch

       n = S_k(n) Q_k(n),  Q_k(n)>k,

   one has S_k(n)<=k.  Every squarefree sieve modulus built only from primes
   <=k and dividing n therefore divides rad(S_k(n))<=S_k(n)<=k.  Consequently
   every relevant current-support column lies in the injective range above.

Thus exact current-support recoalescence provides no branch merging at all in
this parity hard core.  Large-modulus singleton recoalescence (d>=2k) acts only
on the fully k-smooth sector and is identically absent from the large-prime-tail
sector.

This is a semantic/representation no-go, not a theorem about the impossibility
of future-signature compression or other non-static enrichments.
"""

from __future__ import annotations

from math import isqrt


def basin(k: int) -> range:
    if k < 1:
        raise ValueError("k must be positive")
    return range(k * k + 1, (k + 1) * (k + 1))


def hit_support(k: int, modulus: int) -> tuple[int, ...]:
    if modulus < 1:
        raise ValueError("modulus must be positive")
    return tuple(n for n in basin(k) if n % modulus == 0)


def support_injective_certificate(k: int, d1: int, d2: int) -> dict[str, object]:
    """Certify injectivity of exact basin support for 1<=d1,d2<=k."""
    if k < 1 or not (1 <= d1 <= k and 1 <= d2 <= k):
        raise ValueError("require 1<=d1,d2<=k")
    s1 = hit_support(k, d1)
    s2 = hit_support(k, d2)
    if len(s1) < 2 or len(s2) < 2:
        raise AssertionError("a modulus <=k must have at least two basin hits")
    if s1[1] - s1[0] != d1 or s2[1] - s2[0] != d2:
        raise AssertionError("first-two hit gap failed to recover modulus")
    if s1 == s2 and d1 != d2:
        raise AssertionError("distinct moduli <=k acquired equal exact support")
    return {
        "k": k,
        "d1": d1,
        "d2": d2,
        "support1": s1,
        "support2": s2,
        "supports_equal": s1 == s2,
        "equal_implies_same_modulus": True,
    }


def prime_factors(n: int) -> tuple[int, ...]:
    if n < 1:
        raise ValueError("n must be positive")
    out = []
    value = n
    p = 2
    while p * p <= value:
        if value % p == 0:
            out.append(p)
            while value % p == 0:
                value //= p
        p = 3 if p == 2 else p + 2
    if value > 1:
        out.append(value)
    return tuple(out)


def full_k_smooth_core(k: int, n: int) -> tuple[int, int]:
    """Return (S,Q) with all prime powers <=k moved into S."""
    if n not in basin(k):
        raise ValueError("n must lie in the open square basin")
    value = n
    core = 1
    for p in range(2, k + 1):
        # primality is not needed: repeatedly extracting composites here would
        # double-count factors.  Use a small exact primality filter.
        prime = p >= 2 and all(p % q for q in range(2, isqrt(p) + 1))
        if not prime:
            continue
        while value % p == 0:
            value //= p
            core *= p
    return core, value


def squarefree_divisors_from_primes(primes: tuple[int, ...]) -> tuple[int, ...]:
    values = [1]
    for p in primes:
        values += [d * p for d in list(values)]
    return tuple(sorted(values))


def tail_core_static_support_nogo(k: int, n: int) -> dict[str, object]:
    """Certify the static-support no-go for one L020 large-prime-tail state."""
    S, Q = full_k_smooth_core(k, n)
    if Q <= k:
        raise ValueError("state is not in the large-prime-tail branch Q>k")
    if S > k:
        raise AssertionError("L020 tail branch violated S<=k")
    small_primes = prime_factors(S)
    moduli = squarefree_divisors_from_primes(small_primes)
    if any(d > k for d in moduli):
        raise AssertionError("tail-core sieve modulus escaped d<=k")

    supports = {d: hit_support(k, d) for d in moduli}
    if len(set(supports.values())) != len(supports):
        raise AssertionError("tail-core current supports are not injective")
    large_moduli = tuple(d for d in moduli if d >= 2 * k)
    if large_moduli:
        raise AssertionError("large-modulus singleton BRC unexpectedly reached tail core")

    return {
        "k": k,
        "n": n,
        "smooth_core": S,
        "large_prime_tail": Q,
        "squarefree_small_moduli": moduli,
        "all_moduli_at_most_k": True,
        "current_supports_pairwise_distinct": True,
        "large_modulus_moduli": large_moduli,
        "verdict": "NO_STATIC_EXACT_SUPPORT_RECOALESCENCE_IN_LARGE_PRIME_TAIL_CORE",
    }


def large_modulus_signed_terms(k: int, n: int) -> tuple[tuple[int, int], ...]:
    """Return (d,mu(d)) for squarefree small-prime divisors d>=2k of n."""
    S, _Q = full_k_smooth_core(k, n)
    primes = prime_factors(S)
    terms = []
    for d in squarefree_divisors_from_primes(primes):
        if d < 2 * k:
            continue
        # d is squarefree by construction.
        omega = sum(1 for p in primes if d % p == 0)
        terms.append((d, -1 if omega % 2 else 1))
    return tuple(terms)


def signed_large_modulus_boundary_examples() -> dict[str, object]:
    """Return one smooth cancellation example and one tail-core zero example."""
    # k=10, 105=3*5*7 is fully k-smooth.  Distinct singleton-support moduli can
    # carry opposite signs; Boolean support recoalescence would lose them.
    smooth_terms = large_modulus_signed_terms(10, 105)
    support_21 = hit_support(10, 21)
    support_105 = hit_support(10, 105)
    if support_21 != (105,) or support_105 != (105,):
        raise AssertionError("smooth signed-recoalescence witness changed")
    signs = dict(smooth_terms)
    if signs.get(21) != 1 or signs.get(105) != -1:
        raise AssertionError("Möbius signs in smooth witness changed")

    # k=31, 985=5*197 has L020 core S=5 and tail Q=197>k; every small-prime
    # squarefree divisor is <=5, hence the d>=62 signed sector is empty.
    tail = tail_core_static_support_nogo(31, 985)
    if large_modulus_signed_terms(31, 985):
        raise AssertionError("tail-core large signed sector should be empty")

    return {
        "smooth_witness": {
            "k": 10,
            "n": 105,
            "support": (105,),
            "modulus_sign_pairs": ((21, 1), (105, -1)),
            "verdict": "BOOLEAN_SUPPORT_LOSES_SIGN",
        },
        "tail_witness": tail,
    }
