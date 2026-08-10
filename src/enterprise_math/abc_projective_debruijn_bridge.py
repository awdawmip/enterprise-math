"""Exact pair-radical consequences used by the P025/de Bruijn prior-art bridge.

Supplement 61 shows that a non-unit PCC_eta failure forces two distinct
components x,y with

    m(x)m(y) >= c^(1+eta)/2.

Since primitive abc components are pairwise coprime,

    rad(xy) = x*y / (m(x)m(y)).

On a dyadic interval X/2<c<=X this yields

    rad(xy) <= const_eta * X^(1-eta).

A classical de Bruijn radical-counting theorem can then be applied to the
single pair-product state xy.  The asymptotic counting theorem is external
prior art and is *not* implemented/proved here; this module stores only the
exact arithmetic reduction and exponent comparisons.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_projective_paired_square_tail import (
    projective_failure_paired_residual_witness,
)
from .abc_projective_sparse_failure import projective_failure_large_residual_witness
from .abc_support import radical


@dataclass(frozen=True)
class PairRadicalFailureState:
    abc: tuple[int, int, int]
    component_indices: tuple[int, int]
    component_values: tuple[int, int]
    component_product: int
    residual_product: int
    radical_product: int


def nonunit_pcc_failure_pair_radical_state(
    a: int,
    b: int,
    c: int,
    numerator: int,
    denominator: int,
) -> PairRadicalFailureState | None:
    """Return the pair-product radical state forced by a non-unit PCC failure."""
    witness = projective_failure_paired_residual_witness(
        a, b, c, numerator, denominator
    )
    if witness is None:
        return None
    x, y = witness.component_values
    product = x * y
    radical_product = radical(x) * radical(y)
    if radical_product * witness.residual_product != product:
        raise AssertionError("primitive pair radical/residual factorization failed")
    return PairRadicalFailureState(
        abc=(a, b, c),
        component_indices=witness.component_indices,
        component_values=witness.component_values,
        component_product=product,
        residual_product=witness.residual_product,
        radical_product=radical_product,
    )


def unit_pcc_failure_small_radical_component(
    a: int,
    b: int,
    c: int,
    numerator: int,
    denominator: int,
) -> tuple[int, int] | None:
    """Return ``(n,rad(n))`` for the Stage-50 unit failure component.

    For a unit triple, Stage 50 already gives m(n)>=c^eta.  Hence on a dyadic
    range that component itself is a one-variable small-radical state.  This
    helper keeps only the exact finite reduction; de Bruijn counting is prior
    art outside the executable layer.
    """
    if not (a == 1 or b == 1):
        raise ValueError("require a unit additive triple")
    witness = projective_failure_large_residual_witness(
        a, b, c, numerator, denominator
    )
    if witness is None:
        return None
    n = witness.component_value
    return n, radical(n)


def pcc_debruijn_failure_power(numerator: int, denominator: int) -> Fraction:
    """Return the pair-product de Bruijn power ``1-eta``.

    This is the exponent before an arbitrary ``+epsilon`` loss in the external
    radical-count/divisor-bound argument.
    """
    if not 0 < numerator < denominator:
        raise ValueError("require 0 < numerator < denominator")
    return Fraction(denominator - numerator, denominator)


def oesterle_via_pcc_debruijn_limit_power(M_numerator: int, M_denominator: int) -> Fraction:
    """Return the limiting P025-via-PCC exceptional power ``1/M``.

    Stage 60 needs eta<1-1/M.  Combining Stage 62 with eta approaching that
    boundary gives X^(1/M+epsilon).  This is an internal route benchmark, not
    the strongest known bound.
    """
    if M_denominator <= 0 or M_numerator <= M_denominator:
        raise ValueError("require rational M>1")
    return Fraction(M_denominator, M_numerator)


def classical_debruijn_abc_limit_power(M_numerator: int, M_denominator: int) -> Fraction:
    """Return the classical radical-selector power ``2/(3M)``.

    This number is recorded only for comparison with the external de Bruijn
    estimate used in current abc exceptional-set literature.
    """
    if M_denominator <= 0 or M_numerator <= M_denominator:
        raise ValueError("require rational M>1")
    return Fraction(2 * M_denominator, 3 * M_numerator)


def classical_selector_strictly_beats_pcc_route(
    M_numerator: int, M_denominator: int
) -> bool:
    """Verify ``2/(3M) < 1/M`` for every rational M>1."""
    return classical_debruijn_abc_limit_power(
        M_numerator, M_denominator
    ) < oesterle_via_pcc_debruijn_limit_power(M_numerator, M_denominator)
