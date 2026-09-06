"""Prioritized direct-jump BRC multiplier scan for odd N.

This module extends the exact multiplier root/remainder transport with exact
2-adic scan reductions plus one explicitly heuristic structural ordering:

1. if odd N and m == 2 (mod 4), then mN cannot be a difference of two integer
   squares;
2. if odd N and m == 4 (mod 8) yields an immediate ceiling-square witness, the
   same witness divides by 2 to give an immediate witness already at m/4, with
   the same gcd factor. Such multipliers are feasible but scan-redundant;
3. among the remaining irredundant multipliers, the number of same-parity
   multiplier factor pairs is a natural N-independent structural priority score.

Thus a scan-complete odd-N representative set uses multiplier residues
{0,1,3,5,7} modulo 8. After materializing the m=1 BRC state once, each
prioritized candidate m<=100 is reached directly from that state by a dyadic
sqrt(m)-1 predictor plus at most 11 exact odd-width BRC corrections. No
intermediate multiplier roots are required.

The factor-pair priority rule is a heuristic ordering, not a theorem of
optimality. The mod-4 obstruction, mod-8 redundancy reduction, and jump
transport are exact.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from math import isqrt

from .brc_multiplier_transition import initial_multiplier_root_state
from .brc_multiplier_transition_table import MAX_MULTIPLIER, fraction_bits_for_n_bits


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def factor_pair_count(value: int) -> int:
    """Number of unordered positive factor pairs a*b=value with a<=b."""
    _require_positive("value", value)
    return sum(1 for a in range(1, isqrt(value) + 1) if value % a == 0)


def admissible_same_parity_factor_pair_count(multiplier: int) -> int:
    """Same-parity multiplier splits relevant to odd-N difference of squares.

    For odd m, every factor split u*v=m has u,v odd. For m divisible by 4,
    same-parity requires u=2a, v=2b and therefore a*b=m/4. For m == 2 mod 4
    no same-parity split exists.
    """
    _require_positive("multiplier", multiplier)
    if multiplier % 2:
        return factor_pair_count(multiplier)
    if multiplier % 4 == 0:
        return factor_pair_count(multiplier // 4)
    return 0


def odd_n_multiplier_is_difference_square_feasible(multiplier: int) -> bool:
    """Safe mod-4 feasibility test for odd N.

    This answers whether the multiplier can occur in a difference-of-squares
    representation at all. It intentionally returns True on m == 4 (mod 8):
    those multipliers are feasible, but :func:`odd_n_multiplier_is_scan_irredundant`
    identifies them as unnecessary in a factor-finding scan.
    """
    _require_positive("multiplier", multiplier)
    return multiplier % 4 != 2


def odd_n_multiplier_is_scan_irredundant(multiplier: int) -> bool:
    """Exact scan-complete mod-8 representative test for odd N.

    Multipliers 2 or 6 modulo 8 are impossible difference-of-squares targets.
    A multiplier 4 modulo 8 is feasible but redundant: writing m=4*l with l
    odd, every immediate ceiling witness x^2-y^2=m*N has even x,y and divides
    to an immediate ceiling witness at l*N with the same gcd factor.

    Therefore residues {0,1,3,5,7} modulo 8 form a scan-complete set.
    """
    _require_positive("multiplier", multiplier)
    return multiplier % 8 in (0, 1, 3, 5, 7)


def odd_n_multiplier_scan_representative(multiplier: int) -> int | None:
    """Return the exact odd-N scan representative, or None if impossible.

    - m == 2 or 6 (mod 8): impossible -> None;
    - m == 4 (mod 8): every successful witness reduces to m/4 -> m//4;
    - other residues: already irredundant -> m.
    """
    _require_positive("multiplier", multiplier)
    residue = multiplier % 8
    if residue in (2, 6):
        return None
    if residue == 4:
        return multiplier // 4
    return multiplier


def prioritized_odd_multiplier_order(
    max_multiplier: int = MAX_MULTIPLIER,
) -> tuple[int, ...]:
    """Return scan-complete structural order with m=1 fixed first.

    Exact 2-adic reduction keeps only residues {0,1,3,5,7} modulo 8. Remaining
    multipliers are sorted by decreasing count of same-parity multiplier factor
    pairs, then increasing m. The candidate set reduction is exact; only the
    ordering within that set is heuristic.
    """
    _require_positive("max_multiplier", max_multiplier)
    candidates = [
        m for m in range(1, max_multiplier + 1)
        if odd_n_multiplier_is_scan_irredundant(m)
    ]
    rest = [m for m in candidates if m != 1]
    rest.sort(key=lambda m: (-admissible_same_parity_factor_pair_count(m), m))
    return (1, *rest)


@lru_cache(maxsize=None)
def _direct_jump_constants(n_bits: int, max_multiplier: int) -> tuple[int, dict[int, int]]:
    B = fraction_bits_for_n_bits(n_bits)
    scale = 1 << B
    constants = {
        m: isqrt(m << (2 * B)) - scale
        for m in range(2, max_multiplier + 1)
    }
    return B, constants


@dataclass(frozen=True)
class DirectMultiplierJumpState:
    n: int
    multiplier: int
    root: int
    remainder: int
    correction_steps: int

    @property
    def ceiling_completion_gap(self) -> int:
        if self.remainder == 0:
            return 0
        return 2 * self.root + 1 - self.remainder


def direct_multiplier_jump_from_one(
    n: int,
    target_multiplier: int,
    *,
    max_multiplier: int = MAX_MULTIPLIER,
) -> DirectMultiplierJumpState:
    """Reach target multiplier directly from the exact m=1 BRC state.

    For target m<=100, beta=sqrt(m)<=10. With B chosen by the existing
    transition precision rule, the lower predictor error plus the unresolved
    source-root fractional part places the true target root fewer than 12
    integers above the candidate. Hence at most 11 odd-width corrections occur.
    """
    _require_positive("n", n)
    _require_positive("target_multiplier", target_multiplier)
    if target_multiplier > max_multiplier:
        raise ValueError("target_multiplier exceeds declared max_multiplier")
    if max_multiplier > MAX_MULTIPLIER:
        raise ValueError(f"max_multiplier must be <= {MAX_MULTIPLIER}")

    base = initial_multiplier_root_state(n)
    if target_multiplier == 1:
        return DirectMultiplierJumpState(n, 1, base.root, base.remainder, 0)

    B, constants = _direct_jump_constants(n.bit_length(), max_multiplier)
    gamma_constant = constants[target_multiplier]
    j = base.root
    r = base.remainder
    d0 = (gamma_constant * j) >> B
    candidate = j + d0
    gap = r + (target_multiplier - 1) * n - d0 * (2 * j + d0)
    if gap < 0:
        raise AssertionError("direct-jump lower predictor overshot target root")

    corrections = 0
    odd_width = 2 * candidate + 1
    while gap >= odd_width:
        gap -= odd_width
        candidate += 1
        corrections += 1
        if corrections > 11:
            raise AssertionError("direct-jump 11-correction theorem failed")
        odd_width += 2

    if candidate * candidate + gap != target_multiplier * n:
        raise AssertionError("direct-jump reconstruction failed")
    if not 0 <= gap <= 2 * candidate:
        raise AssertionError("direct-jump remainder escaped BRC basin")

    return DirectMultiplierJumpState(
        n=n,
        multiplier=target_multiplier,
        root=candidate,
        remainder=gap,
        correction_steps=corrections,
    )


def prioritized_odd_multiplier_states(
    n: int,
    max_multiplier: int = MAX_MULTIPLIER,
) -> tuple[DirectMultiplierJumpState, ...]:
    """Exact prioritized candidate states for odd n.

    Multipliers 2 or 6 mod 8 are impossible; multipliers 4 mod 8 are omitted by
    the exact m -> m/4 witness reduction. Every retained state is independently
    jumped from m=1.
    """
    _require_positive("n", n)
    if n % 2 == 0:
        raise ValueError("prioritized odd multiplier scan requires odd n")
    return tuple(
        direct_multiplier_jump_from_one(n, m, max_multiplier=max_multiplier)
        for m in prioritized_odd_multiplier_order(max_multiplier)
    )


__all__ = [
    "DirectMultiplierJumpState",
    "factor_pair_count",
    "admissible_same_parity_factor_pair_count",
    "odd_n_multiplier_is_difference_square_feasible",
    "odd_n_multiplier_is_scan_irredundant",
    "odd_n_multiplier_scan_representative",
    "prioritized_odd_multiplier_order",
    "direct_multiplier_jump_from_one",
    "prioritized_odd_multiplier_states",
]
