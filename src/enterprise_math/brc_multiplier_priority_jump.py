"""Prioritized direct-jump BRC multiplier scan for odd N.

This module extends exact multiplier root/remainder transport with exact 2-adic
scan reductions plus one explicitly heuristic structural ordering:

1. if odd N and m == 2 (mod 4), then mN cannot be a difference of two integer
   squares;
2. if odd N and m == 4 (mod 8) yields an immediate ceiling-square witness, the
   same witness divides by 2 to give an immediate witness already at m/4, with
   the same gcd factor. Such multipliers are feasible but scan-redundant;
3. more generally, once a BRC state is known, every successful witness with
   4|m and even ceiling root reduces exactly to m/4. Repeating this gives an
   N-visible, zero-loss gap-test representative before squarehood testing;
4. among the remaining irredundant multipliers, the number of same-parity
   multiplier factor pairs is a natural N-independent structural priority score.

Thus a static scan-complete odd-N representative set uses multiplier residues
{0,1,3,5,7} modulo 8. The dynamic ceiling-root reduction may remove additional
gap tests inside the retained 0 mod 8 class, but it does not delete that class
uniformly. After materializing the m=1 BRC state once, each prioritized
candidate m<=100 is reached directly from that state by a dyadic sqrt(m)-1
predictor plus at most 11 exact odd-width BRC corrections.

The factor-pair priority rule is a heuristic ordering, not a theorem of
optimality. The 2-adic reductions and jump transport are exact.
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
    """Same-parity multiplier splits relevant to odd-N difference of squares."""
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
    identifies them as unnecessary in a complete factor-finding scan.
    """
    _require_positive("multiplier", multiplier)
    return multiplier % 4 != 2


def odd_n_multiplier_is_scan_irredundant(multiplier: int) -> bool:
    """Exact static scan-complete mod-8 representative test for odd N."""
    _require_positive("multiplier", multiplier)
    return multiplier % 8 in (0, 1, 3, 5, 7)


def odd_n_multiplier_scan_representative(multiplier: int) -> int | None:
    """Return the exact static odd-N scan representative, or None if impossible.

    - m == 2 or 6 (mod 8): impossible -> None;
    - m == 4 (mod 8): every successful witness reduces to m/4 -> m//4;
    - other residues: statically irredundant -> m.
    """
    _require_positive("multiplier", multiplier)
    residue = multiplier % 8
    if residue in (2, 6):
        return None
    if residue == 4:
        return multiplier // 4
    return multiplier


def odd_n_ceiling_state_scan_representative(
    multiplier: int,
    ceiling_root: int,
) -> int | None:
    """Exact N-visible 2-adic representative conditional on a BRC ceiling root.

    Assume N is odd and ``ceiling_root = ceil(sqrt(multiplier*N))`` is already
    known. If a square completion gap exists and both ``4|multiplier`` and the
    ceiling root is even, then the square root of the gap is also even. Dividing
    the complete difference-of-squares witness by 4 yields the same immediate
    ceiling witness at ``multiplier/4`` and preserves the gcd factor with odd N.

    The reduction is repeated using the correspondingly halved ceiling root.
    If it lands in a 2 mod 4 target, or in a 4 mod 8 target with odd ceiling
    root, square-gap success is impossible and ``None`` is returned.

    Returning a smaller multiplier means any success at the supplied state is
    scan-redundant with that smaller representative. Returning the original
    multiplier means the state cannot be eliminated by this exact 2-adic rule.
    """
    _require_positive("multiplier", multiplier)
    _require_positive("ceiling_root", ceiling_root)

    representative = multiplier
    root = ceiling_root
    while representative % 4 == 0 and root % 2 == 0:
        representative //= 4
        root //= 2

    if representative % 4 == 2:
        return None
    if representative % 8 == 4:
        # v2(target)=2 but the reduced ceiling root is odd. A square gap would
        # make both roots odd, whose square difference is divisible by 8, a
        # contradiction.
        return None
    return representative


def prioritized_odd_multiplier_order(
    max_multiplier: int = MAX_MULTIPLIER,
) -> tuple[int, ...]:
    """Return scan-complete structural order with m=1 fixed first.

    Exact static 2-adic reduction keeps residues {0,1,3,5,7} modulo 8.
    Remaining multipliers are sorted by decreasing count of same-parity factor
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
    def ceiling_root(self) -> int:
        return self.root if self.remainder == 0 else self.root + 1

    @property
    def ceiling_completion_gap(self) -> int:
        if self.remainder == 0:
            return 0
        return 2 * self.root + 1 - self.remainder

    @property
    def scan_representative(self) -> int | None:
        """Exact state-dependent odd-N representative for square-gap testing."""
        if self.n % 2 == 0:
            raise ValueError("scan_representative requires odd n")
        return odd_n_ceiling_state_scan_representative(
            self.multiplier,
            self.ceiling_root,
        )

    @property
    def gap_test_is_irredundant(self) -> bool:
        return self.scan_representative == self.multiplier


def direct_multiplier_jump_from_one(
    n: int,
    target_multiplier: int,
    *,
    max_multiplier: int = MAX_MULTIPLIER,
) -> DirectMultiplierJumpState:
    """Reach target multiplier directly from the exact m=1 BRC state."""
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

    Static multipliers 2/6 mod 8 are impossible and 4 mod 8 are omitted by the
    exact m -> m/4 reduction. Retained 0 mod 8 states may still be dynamically
    gap-test redundant when their N-specific ceiling root is even; callers may
    inspect ``state.gap_test_is_irredundant`` without changing scan coverage.
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
    "odd_n_ceiling_state_scan_representative",
    "prioritized_odd_multiplier_order",
    "direct_multiplier_jump_from_one",
    "prioritized_odd_multiplier_states",
]
