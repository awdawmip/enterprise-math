"""Exact cyclotomic divisor-lattice carrier for equal-exponent P025 atoms.

For distinct odd primes p>q and exponent n>=2,

    p^n-q^n = product_{d|n} Phi_d(p,q),
    p^n+q^n = product_{d|2n, d not| n} Phi_d(p,q).

The cyclotomic layer values need not be pairwise coprime.  Nevertheless the
multiplicity residual has the exact decomposition

    m(active) = Delta * product_d m(Phi_d(p,q)),

where

    Delta = product_d rad(Phi_d(p,q)) / rad(active)
          = product_r r^(t_r-1)

and t_r is the number of selected cyclotomic layers containing r.  Delta is the
precise overlap correction, so no false coprimality assumption is needed.

For a chosen set U of layers, the carrier outside U is

    Delta * product_{d notin U} m(Phi_d).

If an activated state has outside carrier below the threshold denominator, then
at least one layer in U must be nonsquarefree.  This exact criterion unifies the
odd-prime top-factor forcing of Stage 79 with the exponent-four counterexample
of Stage 82 and exposes the odd-composite depth boundary.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import prod

from .abc_support import multiplicity_residual, prime_factorization, radical
from .legendre import is_prime


@dataclass(frozen=True)
class CyclotomicCarrierLayer:
    index: int
    value: int
    radical: int
    residual: int
    support: tuple[int, ...]
    squarefree: bool


@dataclass(frozen=True)
class CyclotomicDivisorCarrierState:
    q: int
    p: int
    exponent: int
    mode: str
    index_set: tuple[int, ...]
    layers: tuple[CyclotomicCarrierLayer, ...]
    active_component: int
    active_residual: int
    overlap_factor: int
    overlap_support_counts: tuple[tuple[int, int], ...]
    projective_denominator: int
    projective_ratio: Fraction


@dataclass(frozen=True)
class CyclotomicSelectedCarrier:
    selected_indices: tuple[int, ...]
    outside_indices: tuple[int, ...]
    overlap_factor: int
    outside_carrier: int
    selected_residual_product: int
    active_residual: int
    threshold: Fraction
    active_at_threshold: bool
    selected_repetition_forced_by_margin: bool
    selected_actually_repeated: bool


def _divisors(n: int) -> tuple[int, ...]:
    result: list[int] = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            result.append(d)
            if d * d != n:
                result.append(n // d)
        d += 1
    return tuple(sorted(result))


def cyclotomic_index_set(exponent: int, mode: str) -> tuple[int, ...]:
    """Return the exact homogeneous cyclotomic indices for p^n +/- q^n."""
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 2:
        raise ValueError("exponent must be an integer >=2")
    if mode == "difference":
        return _divisors(exponent)
    if mode == "sum":
        divisors_n = set(_divisors(exponent))
        return tuple(d for d in _divisors(2 * exponent) if d not in divisors_n)
    raise ValueError("mode must be 'sum' or 'difference'")


def homogeneous_cyclotomic_value(p: int, q: int, index: int) -> int:
    """Evaluate homogeneous Phi_index(p,q) by exact divisor recursion."""
    if index < 1:
        raise ValueError("index must be positive")

    @lru_cache(maxsize=None)
    def phi(d: int) -> int:
        numerator = p**d - q**d
        proper = prod(phi(e) for e in _divisors(d) if e < d)
        if numerator % proper:
            raise AssertionError("homogeneous cyclotomic recursion lost integrality")
        value = numerator // proper
        if value <= 0:
            raise AssertionError("homogeneous cyclotomic value must be positive")
        return value

    return phi(index)


def cyclotomic_divisor_carrier_state(
    q: int, p: int, exponent: int, mode: str
) -> CyclotomicDivisorCarrierState:
    """Compile the full exact cyclotomic carrier for one equal-exponent atom."""
    if any(isinstance(value, bool) or not isinstance(value, int) for value in (q, p)):
        raise ValueError("q and p must be integers")
    if not (3 <= q < p and is_prime(q) and is_prime(p)):
        raise ValueError("require distinct odd primes 3 <= q < p")
    indices = cyclotomic_index_set(exponent, mode)
    layers: list[CyclotomicCarrierLayer] = []
    support_counts: dict[int, int] = {}
    for d in indices:
        value = homogeneous_cyclotomic_value(p, q, d)
        factors = prime_factorization(value)
        support = tuple(prime for prime, _e in factors)
        for prime in support:
            support_counts[prime] = support_counts.get(prime, 0) + 1
        layers.append(
            CyclotomicCarrierLayer(
                index=d,
                value=value,
                radical=radical(value),
                residual=multiplicity_residual(value),
                support=support,
                squarefree=all(e == 1 for _prime, e in factors),
            )
        )

    active = p**exponent - q**exponent if mode == "difference" else p**exponent + q**exponent
    product_layers = prod(layer.value for layer in layers)
    if product_layers != active:
        raise AssertionError("sign-specific cyclotomic index set failed factorization")

    overlap = prod(
        prime ** (count - 1)
        for prime, count in support_counts.items()
        if count >= 2
    )
    overlap_alt_numerator = prod(layer.radical for layer in layers)
    if overlap_alt_numerator != overlap * radical(active):
        raise AssertionError("cyclotomic overlap factor lost radical identity")

    active_residual = multiplicity_residual(active)
    recomposed = overlap * prod(layer.residual for layer in layers)
    if active_residual != recomposed:
        raise AssertionError("cyclotomic residual carrier decomposition failed")

    denominator = exponent * (p + q)
    return CyclotomicDivisorCarrierState(
        q=q,
        p=p,
        exponent=exponent,
        mode=mode,
        index_set=indices,
        layers=tuple(layers),
        active_component=active,
        active_residual=active_residual,
        overlap_factor=overlap,
        overlap_support_counts=tuple(sorted(support_counts.items())),
        projective_denominator=denominator,
        projective_ratio=Fraction(active_residual, denominator),
    )


def selected_cyclotomic_carrier(
    state: CyclotomicDivisorCarrierState,
    selected_indices: tuple[int, ...],
    threshold: Fraction = Fraction(1, 1),
) -> CyclotomicSelectedCarrier:
    """Test whether a selected layer set is forced to contain repetition.

    The criterion is pointwise exact and makes no pairwise-coprimality claim.
    """
    if threshold <= 0:
        raise ValueError("threshold must be positive")
    selected = tuple(sorted(set(selected_indices)))
    if not selected or any(index not in state.index_set for index in selected):
        raise ValueError("selected_indices must be a nonempty subset of the carrier index set")
    layer_by_index = {layer.index: layer for layer in state.layers}
    outside = tuple(index for index in state.index_set if index not in selected)
    outside_carrier = state.overlap_factor * prod(
        layer_by_index[index].residual for index in outside
    )
    selected_product = prod(layer_by_index[index].residual for index in selected)
    if outside_carrier * selected_product != state.active_residual:
        raise AssertionError("selected/outside carrier split failed")

    active = state.projective_ratio >= threshold
    margin_forces = active and Fraction(outside_carrier, state.projective_denominator) < threshold
    actually_repeated = selected_product > 1
    if margin_forces and not actually_repeated:
        raise AssertionError("carrier margin claimed repetition without selected residual")

    return CyclotomicSelectedCarrier(
        selected_indices=selected,
        outside_indices=outside,
        overlap_factor=state.overlap_factor,
        outside_carrier=outside_carrier,
        selected_residual_product=selected_product,
        active_residual=state.active_residual,
        threshold=threshold,
        active_at_threshold=active,
        selected_repetition_forced_by_margin=margin_forces,
        selected_actually_repeated=actually_repeated,
    )


def top_cyclotomic_carrier(
    state: CyclotomicDivisorCarrierState,
    threshold: Fraction = Fraction(1, 1),
) -> CyclotomicSelectedCarrier:
    """Specialize the exact carrier split to the maximal cyclotomic index."""
    return selected_cyclotomic_carrier(state, (max(state.index_set),), threshold)
