"""Small-number divisor-layer lift probe.

This module explores a local multiplicative lift attached to the divisor-count
function tau.  It is intentionally a research probe: exact for the integers it
examines, but not advertised as a large-integer factoring algorithm.

For target T define the lift set

    L_T(n) = {a >= 1 : tau(a*n) = T}.

If gcd(a,n)=1, multiplicativity gives tau(a*n)=tau(a)tau(n).  Hence whenever
T is not divisible by tau(n), every lift multiplier must overlap n.

For squarefree n with k prime factors and target

    T = 2^(k-1) * r,   r an odd prime,

the exponent pattern is forced: exactly one source prime exponent becomes
r-1 and the other k-1 source exponents remain 1.  Therefore the minimal lift is

    lambda_T(n) = p_min^(r-2).

The local-neighborhood routines deliberately preserve every composite-neighbor
tau layer instead of collapsing immediately to a mode.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from math import isqrt


def factorization_small(n: int) -> tuple[tuple[int, int], ...]:
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    x = n
    out: list[tuple[int, int]] = []
    p = 2
    while p * p <= x:
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            out.append((p, e))
        p = 3 if p == 2 else p + 2
    if x > 1:
        out.append((x, 1))
    return tuple(out)


def divisor_count_small(n: int) -> int:
    total = 1
    for _, exponent in factorization_small(n):
        total *= exponent + 1
    return total


def is_prime_small(n: int) -> bool:
    if n < 2:
        return False
    return factorization_small(n) == ((n, 1),)


def is_squarefree_semiprime_small(n: int) -> bool:
    factors = factorization_small(n)
    return len(factors) == 2 and all(exponent == 1 for _, exponent in factors)


def local_composite_divisor_layers(n: int, radius: int = 2) -> tuple[tuple[int, int], ...]:
    if n <= 1 or radius <= 0:
        raise ValueError("n must exceed 1 and radius must be positive")
    out = []
    for value in range(max(2, n - radius), n + radius + 1):
        if value == n or is_prime_small(value):
            continue
        out.append((value, divisor_count_small(value)))
    return tuple(out)


def modal_local_divisor_layer(n: int, radius: int = 2) -> int | None:
    layers = [layer for _, layer in local_composite_divisor_layers(n, radius)]
    if not layers:
        return None
    counts = Counter(layers)
    best = max(counts.values())
    return min(layer for layer, count in counts.items() if count == best)


def factor_forcing_target(source_tau: int, target_tau: int) -> bool:
    if source_tau <= 0 or target_tau <= 0:
        raise ValueError("tau values must be positive")
    return target_tau % source_tau != 0


def _odd_prime(value: int) -> bool:
    return value >= 3 and value % 2 == 1 and is_prime_small(value)


def squarefree_prime_layer_encoder(k: int, target_tau: int) -> int | None:
    """Return odd prime r when target is 2^(k-1)*r, otherwise None."""
    if k <= 0 or target_tau <= 0:
        raise ValueError("k/target_tau must be positive")
    base = 1 << (k - 1)
    if target_tau % base:
        return None
    r = target_tau // base
    return r if _odd_prime(r) else None


def predicted_minimal_encoder_lift(source_factors: tuple[int, ...], target_tau: int) -> int | None:
    if not source_factors or any(p < 2 or not is_prime_small(p) for p in source_factors):
        raise ValueError("source_factors must be nonempty primes")
    if len(set(source_factors)) != len(source_factors):
        raise ValueError("encoder theorem requires a squarefree source")
    r = squarefree_prime_layer_encoder(len(source_factors), target_tau)
    if r is None:
        return None
    return min(source_factors) ** (r - 2)


def minimal_divisor_layer_lift_small(n: int, target_tau: int, max_multiplier: int) -> int | None:
    if n <= 0 or target_tau <= 0 or max_multiplier <= 0:
        raise ValueError("inputs must be positive")
    for multiplier in range(1, max_multiplier + 1):
        if divisor_count_small(multiplier * n) == target_tau:
            return multiplier
    return None


@dataclass(frozen=True, slots=True)
class DivisorLayerNeighborhoodProfile:
    n: int
    radius: int
    source_tau: int
    layers: tuple[tuple[int, int], ...]
    factor_forcing_layers: tuple[int, ...]
    strong_encoder_layers: tuple[int, ...]
    modal_layer: int | None


def neighborhood_profile(n: int, radius: int = 2) -> DivisorLayerNeighborhoodProfile:
    source_tau = divisor_count_small(n)
    layers = local_composite_divisor_layers(n, radius)
    factor_forcing = tuple(sorted({t for _, t in layers if factor_forcing_target(source_tau, t)}))
    k = len(factorization_small(n)) if all(e == 1 for _, e in factorization_small(n)) else 0
    strong: list[int] = []
    if k:
        for _, target in layers:
            if squarefree_prime_layer_encoder(k, target) is not None:
                strong.append(target)
    return DivisorLayerNeighborhoodProfile(
        n=n,
        radius=radius,
        source_tau=source_tau,
        layers=layers,
        factor_forcing_layers=factor_forcing,
        strong_encoder_layers=tuple(sorted(set(strong))),
        modal_layer=modal_local_divisor_layer(n, radius),
    )


__all__ = [
    "DivisorLayerNeighborhoodProfile",
    "factorization_small",
    "divisor_count_small",
    "is_prime_small",
    "is_squarefree_semiprime_small",
    "local_composite_divisor_layers",
    "modal_local_divisor_layer",
    "factor_forcing_target",
    "squarefree_prime_layer_encoder",
    "predicted_minimal_encoder_lift",
    "minimal_divisor_layer_lift_small",
    "neighborhood_profile",
]
