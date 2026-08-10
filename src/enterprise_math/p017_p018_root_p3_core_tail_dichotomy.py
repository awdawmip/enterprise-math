"""P017/P018 Generation 3: root-P3 core/tail dichotomy.

At the exact P3 product cutoff

    U = k^2+2k,
    z3 = floor(U^(1/4)),

every z3-rough square-shell state has Omega<=3.

The factor geometry then has an exact P017-style core/tail split:

* a rough semiprime p*q, p<=q, must satisfy

      z3 < p <= k < q;

  so it has exactly one large prime tail above k;

* a rough triple-prime state a*b*c, a<=b<=c, satisfies

      a*b >= (z3+1)^2 > sqrt(U),

  hence

      c < sqrt(U) < k+1,

  and therefore every prime factor is <=k.  It is fully k-smooth.

Conversely, a z3-rough fully-k-smooth state in the shell cannot be prime and
cannot be semiprime (two factors <=k have product <=k^2).  Since Omega<=3, it
must be exactly a triple-prime state.

Thus

    {root-P3 triple contaminants}
      = {z3-rough survivors} intersect {fully k-smooth states}.

This identifies the P3-only contaminant with the existing P017 complete-core
semantic layer.  It is an exact classification, not an upper bound and not a
P2 theorem.
"""

from __future__ import annotations

from math import isqrt

from .legendre import is_prime, primes_up_to
from .p017_p018_buchstab_cutoff_ladder import (
    almost_prime_cutoff,
    rough_survivor_offsets,
    square_interval_upper,
)


def _factor_multiset(value: int) -> tuple[int, ...]:
    remaining = value
    factors: list[int] = []
    for p in primes_up_to(isqrt(value) + 1):
        while remaining % p == 0:
            factors.append(p)
            remaining //= p
        if remaining == 1:
            break
        if p * p > remaining:
            break
    if remaining > 1:
        factors.append(remaining)
    return tuple(sorted(factors))


def root_p3_core_tail_partition(k: int) -> dict[str, object]:
    """Partition root-P3 rough states into prime, P2-tail and smooth P3 core."""
    if isinstance(k, bool) or not isinstance(k, int) or k < 4:
        raise ValueError("k must be an integer >=4")

    upper = square_interval_upper(k)
    z3 = int(almost_prime_cutoff(k, 3)["cutoff"])
    offsets = rough_survivor_offsets(k, z3)

    prime_rows: list[tuple[int, int]] = []
    semiprime_tail_rows: list[tuple[int, int, int, int]] = []
    smooth_triple_rows: list[tuple[int, int, int, int, int]] = []

    for r in offsets:
        value = k * k + r
        factors = _factor_multiset(value)
        if any(p <= z3 for p in factors):
            raise AssertionError("root-P3 rough state recovered a factor at or below z3")
        if len(factors) > 3:
            raise AssertionError("root-P3 cutoff failed Omega<=3")

        if len(factors) == 1:
            p = factors[0]
            if p != value or not is_prime(p) or p <= k:
                raise AssertionError("prime branch lost its unique large factor")
            prime_rows.append((value, r))
            continue

        if len(factors) == 2:
            p, q = factors
            if not (z3 < p <= k < q):
                raise AssertionError("rough semiprime failed one-low-one-high tail split")
            semiprime_tail_rows.append((p, q, value, r))
            continue

        if len(factors) == 3:
            a, b, c = factors
            if not (z3 < a <= b <= c <= k):
                raise AssertionError("rough triple failed fully k-smooth core classification")
            if not a * b > k:
                raise AssertionError("first two root-P3 factors should already exceed k")
            smooth_triple_rows.append((a, b, c, value, r))
            continue

        raise AssertionError("square-shell rough state had impossible Omega=0")

    if len(offsets) != len(prime_rows) + len(semiprime_tail_rows) + len(smooth_triple_rows):
        raise AssertionError("root-P3 core/tail partition failed")

    # Converse check: every rough fully-k-smooth row is exactly a triple.
    for r in offsets:
        value = k * k + r
        factors = _factor_multiset(value)
        fully_k_smooth = max(factors) <= k
        triple = len(factors) == 3
        if fully_k_smooth != triple:
            raise AssertionError("root-rough fully-smooth iff triple equivalence failed")

    return {
        "k": k,
        "upper": upper,
        "p3_cutoff": z3,
        "rough_offsets": offsets,
        "rough_count": len(offsets),
        "prime_rows": tuple(prime_rows),
        "prime_count": len(prime_rows),
        "semiprime_tail_rows": tuple(semiprime_tail_rows),
        "semiprime_tail_count": len(semiprime_tail_rows),
        "fully_smooth_triple_rows": tuple(smooth_triple_rows),
        "fully_smooth_triple_count": len(smooth_triple_rows),
        "p3_only_equals_root_rough_intersect_k_smooth": True,
        "status": "ROOT_P3_CORE_TAIL_DICHOTOMY",
    }
