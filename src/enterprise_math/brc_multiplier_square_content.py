"""Exact square-content reduction for BRC multiplier square-gap states.

Let m=a^2*d be the canonical squarefree decomposition and let
x=ceil(sqrt(m*n)) be an already-known BRC ceiling root.  When gcd(m,n)=1,
any common factor g=gcd(a,x) is forced into the square root of a successful
completion gap as well.  Dividing x,y by g and m by g^2 preserves the exact
immediate-ceiling witness and the gcd factor with n.

This is a state-dependent scan reduction, not a new factorization principle.
It generalizes the earlier dynamic m->m/4 rule from p=2 to every prime square
in the multiplier.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .brc_multiplier_basin import squarefree_decomposition
from .brc_multiplier_priority_jump import (
    DirectMultiplierJumpState,
    odd_n_ceiling_state_scan_representative,
)


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


@dataclass(frozen=True)
class SquareContentReduction:
    """Exact square-content normalization of one odd-N ceiling-root state."""

    n: int
    multiplier: int
    ceiling_root: int
    square_content_root: int
    common_scale: int
    reduced_multiplier: int
    reduced_ceiling_root: int
    scan_representative: int | None

    @property
    def impossible(self) -> bool:
        return self.scan_representative is None

    @property
    def reduced(self) -> bool:
        return self.common_scale > 1

    @property
    def gap_test_is_irredundant(self) -> bool:
        return self.scan_representative == self.multiplier

    @property
    def status(self) -> str:
        if self.impossible:
            return "IMPOSSIBLE"
        if self.reduced:
            return "REDUCED"
        return "IRREDUNDANT"


def odd_n_square_content_scan_reduction(
    n: int,
    multiplier: int,
    ceiling_root: int,
) -> SquareContentReduction:
    """Strip every square multiplier factor already visible in the ceiling root.

    Preconditions:
    - n is odd;
    - gcd(n,multiplier)=1.  A caller should test this gcd first; a nontrivial
      gcd is itself already a factor witness and lies outside this reduction's
      same-gcd transport contract.

    Write ``multiplier=a^2*d`` with d squarefree and set
    ``g=gcd(a,ceiling_root)``.  If a completion gap is a square ``y^2``, then
    ``g^2`` divides both ``ceiling_root^2`` and ``multiplier*n``, hence g|y.
    Therefore the witness divides exactly to multiplier/g^2.

    The ceiling property is preserved because
    ``g*X=ceil(g*sqrt(z))`` implies ``X=ceil(sqrt(z))``.  Since gcd(g,n)=1,
    the gcd factor with n is unchanged.

    After square-content stripping, the existing exact odd-N 2-adic state
    reduction is applied to diagnose an impossible residual class if present.
    """
    _require_positive("n", n)
    _require_positive("multiplier", multiplier)
    _require_positive("ceiling_root", ceiling_root)
    if n % 2 == 0:
        raise ValueError("square-content scan reduction currently requires odd n")
    if gcd(n, multiplier) != 1:
        raise ValueError("check gcd(n,multiplier) first; reduction requires coprimality")

    square_part, _ = squarefree_decomposition(multiplier)
    common = gcd(square_part, ceiling_root)
    reduced_multiplier = multiplier // (common * common)
    reduced_root = ceiling_root // common

    representative = odd_n_ceiling_state_scan_representative(
        reduced_multiplier,
        reduced_root,
    )
    return SquareContentReduction(
        n=n,
        multiplier=multiplier,
        ceiling_root=ceiling_root,
        square_content_root=square_part,
        common_scale=common,
        reduced_multiplier=reduced_multiplier,
        reduced_ceiling_root=reduced_root,
        scan_representative=representative,
    )


def jump_state_square_content_reduction(
    state: DirectMultiplierJumpState,
) -> SquareContentReduction:
    """Apply square-content normalization to an existing direct-jump BRC state."""
    return odd_n_square_content_scan_reduction(
        state.n,
        state.multiplier,
        state.ceiling_root,
    )


__all__ = [
    "SquareContentReduction",
    "odd_n_square_content_scan_reduction",
    "jump_state_square_content_reduction",
]
