"""Isolate the genuinely hard divisor-conductor tail in Euclidean Poisson space.

For the exact tent-smoothed channel C(n,d), conductor Möbius inversion gives

    C(n,d)=sum_(q|n) (q/n) P(q,d),

where P(q,d) is the native primitive-frequency block at conductor q.

Assume d<=k.  The q=1 block equals C(1,d) and its tent zero-frequency main is
k/d.  Since d/k<=1, the full nonzero-frequency error is at most d/(3k):

    C(1,d)=k/d+O(d/(3k)).

For every q>1 with q*d<=k the primitive block contains only nonzero frequencies,
and the same tent estimate gives

    |P(q,d)| <= q*d/(3k).

Therefore, writing

  L(n,d)=sum_(q|n, 1<q, q*d<=k) (q/n)P(q,d),
  H(n,d)=sum_(q|n, q*d>k)       (q/n)P(q,d),

one has

    |L(n,d)|
      <= d/(3kn) sum_(q|n,qd<=k) q^2
      <= sigma(n)/(3n),

and hence the hard-conductor isolation

    C(n,d)
      = k/(n*d)
        + O(d/(3kn) + sigma(n)/(3n))
        + H(n,d).

If n*d<=k then H(n,d)=0 automatically, recovering the deterministic low-region
closure.  When n*d>k, all unresolved primitive information comes only from
large divisors q|n with q>k/d.  These same q,d pairs lie in the P017
cross-orientation single-use product regime.

This is an analytic reduction theorem, not a bound for H(n,d) and not a proof of
Legendre's conjecture.
"""

from __future__ import annotations

from fractions import Fraction

from .p017_p018_euclidean_critical_hyperbola import low_hyperbola_poisson_bounds
from .p017_p018_poisson_conductor_mobius import (
    primitive_conductor_block,
    tent_smoothed_channel_count,
)


def _divisors(n: int) -> tuple[int, ...]:
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def _sigma(n: int) -> int:
    return sum(_divisors(n))


def low_primitive_block_ceiling(k: int, q: int, d: int) -> Fraction:
    """Return q*d/(3k), valid for q>1 and q*d<=k."""
    if q <= 1:
        raise ValueError("primitive low-block ceiling is declared for q>1")
    data = low_hyperbola_poisson_bounds(k, q, d)
    return data["nonzero_frequency_absolute_ceiling"]


def hard_conductor_isolation(center: int, k: int, n: int, d: int) -> dict[str, object]:
    """Compute exact low/hard Möbius blocks and return rigorous low ceilings."""
    from math import gcd

    if any(isinstance(v, bool) or not isinstance(v, int) or v < 1 for v in (center, k, n, d)):
        raise ValueError("center,k,n,d must be positive integers")
    if d > k:
        raise ValueError("hard-conductor isolation uses the critical divisor range d<=k")
    if gcd(center, n) != 1 or gcd(n, d) != 1:
        raise ValueError("isolation requires gcd(center,n)=gcd(n,d)=1")

    coarse = Fraction(1, n) * tent_smoothed_channel_count(center, k, 1, d)
    coarse_main = Fraction(k, n * d)
    coarse_error = coarse - coarse_main
    coarse_ceiling = Fraction(d, 3 * k * n)
    if abs(coarse_error) > coarse_ceiling:
        # This is the analytic tent bound; a failure is a source-level theorem bug.
        raise AssertionError("coarse q=1 tent error exceeded d/(3kn)")

    low = Fraction(0, 1)
    hard = Fraction(0, 1)
    low_rows: list[dict[str, object]] = []
    hard_rows: list[dict[str, object]] = []
    low_ceiling_sum = Fraction(0, 1)

    for q in _divisors(n):
        if q == 1:
            continue
        primitive = primitive_conductor_block(center, k, q, d)
        weighted = Fraction(q, n) * primitive
        if q * d <= k:
            ceiling = Fraction(q, n) * low_primitive_block_ceiling(k, q, d)
            if abs(weighted) > ceiling:
                raise AssertionError("low primitive block exceeded deterministic Poisson ceiling")
            low += weighted
            low_ceiling_sum += ceiling
            low_rows.append({"q": q, "primitive": primitive, "weighted": weighted, "ceiling": ceiling})
        else:
            hard += weighted
            hard_rows.append({"q": q, "primitive": primitive, "weighted": weighted})

    physical = tent_smoothed_channel_count(center, k, n, d)
    if coarse + low + hard != physical:
        raise AssertionError("coarse/low/hard conductor split failed exact reconstruction")

    sigma_ceiling = Fraction(_sigma(n), 3 * n)
    if low_ceiling_sum > sigma_ceiling:
        raise AssertionError("low conductor sum exceeded sigma(n)/(3n) ceiling")

    return {
        "center": center,
        "k": k,
        "n": n,
        "d": d,
        "physical_channel": physical,
        "coarse_q1_block": coarse,
        "coarse_main": coarse_main,
        "coarse_error": coarse_error,
        "coarse_error_ceiling": coarse_ceiling,
        "controlled_low_block": low,
        "controlled_low_rows": tuple(low_rows),
        "controlled_low_absolute_ceiling": low_ceiling_sum,
        "sigma_over_3n_ceiling": sigma_ceiling,
        "hard_conductor_block": hard,
        "hard_rows": tuple(hard_rows),
        "hard_conductors_absent": len(hard_rows) == 0,
        "hard_conductor_isolation_exact": True,
    }
