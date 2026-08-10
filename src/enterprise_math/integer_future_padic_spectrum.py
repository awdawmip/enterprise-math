"""Recover p-primary Smith depth from the prime-power modular kernel curve.

For integer observation map O with hidden free rank h and nonzero Smith factors
``d_i``, write ``a_i=v_p(d_i)`` and

    kappa_e = log_p |ker(O mod p^e)|
            = e*h + sum_i min(e,a_i),

with ``kappa_0=0``.

The discrete slope is

    s_e = kappa_e-kappa_(e-1)
        = h + #{i : a_i >= e}.

Hence the slope sequence is nonincreasing, and

    s_e-s_(e+1) = #{i : a_i = e}.

The complete infinite precision-growth curve therefore determines the free
hidden rank and every positive p-adic Smith valuation multiplicity exactly.

A finite ladder through exponent E cannot in general distinguish a genuine free
hidden direction from finite torsion deeper than the observed precision.  It
recovers all valuation multiplicities below E and only the unresolved tail

    s_E = h + #{i : a_i >= E}.

Sharp indistinguishability: in dimension two, ``diag(1,0)`` has one free hidden
direction, while ``diag(1,p^K)`` has full rational rank and only finite torsion.
Their kernel exponents agree as ``kappa_e=e`` for every ``e<=K``.  The models
separate only at exponent K+1.

This is standard Smith/p-adic finite-difference arithmetic.  The project value
is the exact finite-precision identifiability boundary: unresolved deep finite
torsion can mimic a free hidden state direction until observation precision
passes its p-adic depth.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .integer_future_padic_precision import (
    p_adic_valuation,
    prime_power_precision_ladder,
)
from .integer_future_smith_precision import integer_smith_precision_profile


@dataclass(frozen=True)
class FinitePadicKernelSpectrum:
    prime: int
    observed_max_exponent: int
    kernel_exponents: tuple[int, ...]
    slopes: tuple[int, ...]
    recovered_exact_valuation_multiplicities: tuple[tuple[int, int], ...]
    unresolved_tail_slope: int

    @property
    def slopes_nonincreasing(self) -> bool:
        return all(
            left >= right
            for left, right in zip(self.slopes, self.slopes[1:])
        )


def padic_spectrum_from_kernel_exponents(
    prime: int,
    kernel_exponents: Sequence[int],
) -> FinitePadicKernelSpectrum:
    values = tuple(kernel_exponents)
    if not values:
        raise ValueError("kernel_exponents must contain at least exponent one")
    if isinstance(prime, bool) or not isinstance(prime, int) or prime < 2:
        raise ValueError("prime must be an integer at least two")
    # Reuse the exact primality validation through v_p(1).
    p_adic_valuation(1, prime)
    for value in values:
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("kernel exponents must be nonnegative integers")

    extended = (0,) + values
    slopes = tuple(
        extended[index] - extended[index - 1]
        for index in range(1, len(extended))
    )
    if any(slope < 0 for slope in slopes):
        raise ValueError("kernel exponent curve must be nondecreasing")
    if any(left < right for left, right in zip(slopes, slopes[1:])):
        raise ValueError("kernel exponent slopes must be nonincreasing")

    multiplicities = tuple(
        (depth, slopes[depth - 1] - slopes[depth])
        for depth in range(1, len(slopes))
        if slopes[depth - 1] != slopes[depth]
    )
    return FinitePadicKernelSpectrum(
        prime=prime,
        observed_max_exponent=len(values),
        kernel_exponents=values,
        slopes=slopes,
        recovered_exact_valuation_multiplicities=multiplicities,
        unresolved_tail_slope=slopes[-1],
    )


def padic_kernel_spectrum_from_matrix(
    observation_matrix: Sequence[Sequence[int]],
    prime: int,
    max_exponent: int,
) -> FinitePadicKernelSpectrum:
    ladder = prime_power_precision_ladder(
        observation_matrix,
        prime,
        max_exponent,
    )
    return padic_spectrum_from_kernel_exponents(
        prime,
        tuple(step.kernel_exponent for step in ladder),
    )


@dataclass(frozen=True)
class CompletePadicSmithSpectrum:
    prime: int
    hidden_free_rank: int
    positive_valuation_multiplicities: tuple[tuple[int, int], ...]
    sufficient_precision_exponent: int
    finite_reconstruction: FinitePadicKernelSpectrum


def complete_padic_smith_spectrum(
    observation_matrix: Sequence[Sequence[int]],
    prime: int,
) -> CompletePadicSmithSpectrum:
    profile = integer_smith_precision_profile(observation_matrix)
    valuations = tuple(
        p_adic_valuation(factor, prime)
        for factor in profile.smith_invariant_factors
    )
    positive = tuple(sorted(value for value in valuations if value > 0))
    max_valuation = max(positive, default=0)
    # One level beyond the deepest finite torsion reveals the eventual slope h.
    sufficient = max_valuation + 1 if max_valuation > 0 else 1
    reconstructed = padic_kernel_spectrum_from_matrix(
        observation_matrix,
        prime,
        sufficient,
    )
    multiplicities = tuple(
        (depth, positive.count(depth))
        for depth in sorted(set(positive))
    )
    if reconstructed.unresolved_tail_slope != profile.hidden_free_rank:
        raise AssertionError("p-adic ladder failed to recover hidden free rank")
    if reconstructed.recovered_exact_valuation_multiplicities != multiplicities:
        raise AssertionError("p-adic ladder failed to recover Smith valuation spectrum")
    return CompletePadicSmithSpectrum(
        prime=prime,
        hidden_free_rank=profile.hidden_free_rank,
        positive_valuation_multiplicities=multiplicities,
        sufficient_precision_exponent=sufficient,
        finite_reconstruction=reconstructed,
    )


def free_vs_deep_torsion_indistinguishable_through(
    prime: int,
    torsion_depth: int,
    observed_exponent: int,
) -> bool:
    if isinstance(torsion_depth, bool) or not isinstance(torsion_depth, int):
        raise TypeError("torsion_depth must be an integer")
    if isinstance(observed_exponent, bool) or not isinstance(observed_exponent, int):
        raise TypeError("observed_exponent must be an integer")
    if torsion_depth <= 0 or observed_exponent <= 0:
        raise ValueError("depths must be positive")
    # Matrix A: one visible unimodular coordinate + one free hidden direction.
    free_matrix = ((1, 0),)
    # Matrix B: full rank, second Smith factor p^K.
    p_adic_valuation(1, prime)
    torsion_matrix = (
        (1, 0),
        (0, prime ** torsion_depth),
    )
    free_curve = padic_kernel_spectrum_from_matrix(
        free_matrix,
        prime,
        observed_exponent,
    ).kernel_exponents
    torsion_curve = padic_kernel_spectrum_from_matrix(
        torsion_matrix,
        prime,
        observed_exponent,
    ).kernel_exponents
    expected_equal = observed_exponent <= torsion_depth
    if (free_curve == torsion_curve) != expected_equal:
        raise AssertionError("free/deep-torsion finite-precision boundary failed")
    return expected_equal
