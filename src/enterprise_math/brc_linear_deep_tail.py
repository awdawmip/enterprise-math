"""Exact order-1 Pell/Padé BRC transport on the long multiplier tail.

For an exact source state

    m*N = J^2 + R,   0 <= R <= 2J,

and a short forward step h in {1,2}, the order-1 Pell/Padé lower ratio is

    (4m+3h)/(4m+h) = 1 + 2h/(4m+h).

Hence the predicted root increment is simply

    d = floor(2h*J/(4m+h)).

No sqrt-ratio table and no high-order Padé state are required.  The exact
Pell identity

    (m+h)(4m+h)^2 - m(4m+3h)^2 = h^3

gives a two-correction certificate.  A root-free sufficient condition is

    256*m^5 >= N*h^6.

For the odd-N mod-8 representative stream h is always 1 or 2, so the common
condition 4*m^5 >= N certifies every later step.  Thus beyond an O(N^(1/5))
prefix the long sparse multiplier stream is an exact linear-denominator BRC
transport with at most two ordinary odd-basin corrections per step.

This is a transport optimization.  Difference-of-squares factor search remains
classical and no factorization-complexity improvement is claimed.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isqrt
from typing import Protocol

from .core import integer_nth_root

ODD_N_REPRESENTATIVE_RESIDUES = frozenset((0, 1, 3, 5, 7))


class MultiplierStateLike(Protocol):
    n: int
    multiplier: int
    root: int
    remainder: int


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def odd_n_multiplier_is_representative(multiplier: int) -> bool:
    _require_positive("multiplier", multiplier)
    return multiplier % 8 in ODD_N_REPRESENTATIVE_RESIDUES


def next_odd_n_representative_multiplier(multiplier: int) -> int:
    """Return the next multiplier in the exact odd-N mod-8 representative set."""
    _require_positive("multiplier", multiplier)
    target = multiplier + 1
    while target % 8 not in ODD_N_REPRESENTATIVE_RESIDUES:
        target += 1
    return target


def order1_pell_pair(multiplier: int, step: int) -> tuple[int, int]:
    """Return the order-1 integer Pell/Padé pair ``(A,B)``.

    ``A/B=(4m+3h)/(4m+h)`` is a strict lower bound for
    ``sqrt((m+h)/m)`` and satisfies the exact Pell norm h^3.
    """
    _require_positive("multiplier", multiplier)
    _require_positive("step", step)
    if step not in (1, 2):
        raise ValueError("linear deep-tail transport supports step 1 or 2")
    a = 4 * multiplier + 3 * step
    b = 4 * multiplier + step
    if (multiplier + step) * b * b - multiplier * a * a != step**3:
        raise AssertionError("order-1 Pell identity failed")
    return a, b


def order1_two_correction_certificate(
    root: int,
    multiplier: int,
    step: int,
) -> bool:
    """Exact state-dependent certificate for at most two BRC corrections."""
    _require_nonnegative("root", root)
    a, b = order1_pell_pair(multiplier, step)
    return root * step**3 <= multiplier * a * b


def linear_tail_sufficient(n: int, multiplier: int, step: int) -> bool:
    """Root-free sufficient certificate ``256*m^5 >= N*h^6``."""
    _require_positive("n", n)
    _require_positive("multiplier", multiplier)
    _require_positive("step", step)
    if step not in (1, 2):
        return False
    return 256 * multiplier**5 >= n * step**6


def common_mod8_linear_tail_sufficient(n: int, multiplier: int) -> bool:
    """Sufficient condition for every later h=1,2 mod-8 sparse step.

    The h=2 condition dominates and reduces to ``4*m^5 >= N``.
    """
    _require_positive("n", n)
    _require_positive("multiplier", multiplier)
    return 4 * multiplier**5 >= n


def _ceil_fifth_root(value: int) -> int:
    _require_positive("value", value)
    root = integer_nth_root(value, 5)
    return root if root**5 == value else root + 1


def linear_tail_threshold(n: int, step: int) -> int:
    """Return the smallest m satisfying the root-free step-specific bound."""
    _require_positive("n", n)
    _require_positive("step", step)
    if step not in (1, 2):
        raise ValueError("linear deep-tail transport supports step 1 or 2")
    numerator = n * step**6
    target = (numerator + 255) // 256
    return _ceil_fifth_root(target)


def common_mod8_linear_tail_threshold(n: int) -> int:
    """Return the smallest integer m with ``4*m^5 >= N``."""
    _require_positive("n", n)
    return _ceil_fifth_root((n + 3) // 4)


@dataclass(frozen=True)
class LinearDeepTailState:
    n: int
    multiplier: int
    root: int
    remainder: int
    source_multiplier: int
    step_from_previous: int
    correction_steps: int

    def __post_init__(self) -> None:
        _require_positive("n", self.n)
        _require_positive("multiplier", self.multiplier)
        _require_positive("source_multiplier", self.source_multiplier)
        _require_nonnegative("root", self.root)
        _require_nonnegative("remainder", self.remainder)
        if self.remainder > 2 * self.root:
            raise ValueError("remainder escaped square-root BRC basin")
        if self.step_from_previous not in (0, 1, 2):
            raise ValueError("step_from_previous must be 0, 1, or 2")
        if not 0 <= self.correction_steps <= 2:
            raise ValueError("correction_steps must lie in 0..2")

    @property
    def target_value(self) -> int:
        return self.root * self.root + self.remainder

    @property
    def ceiling_completion_gap(self) -> int:
        if self.remainder == 0:
            return 0
        return 2 * self.root + 1 - self.remainder


def _transport_order1_core(
    source: MultiplierStateLike,
    target_multiplier: int,
) -> LinearDeepTailState:
    n = source.n
    m = source.multiplier
    j = source.root
    r = source.remainder
    h = target_multiplier - m

    # A/B = 1 + 2h/(4m+h), so floor(AJ/B)=J+floor(2hJ/(4m+h)).
    d = (2 * h * j) // (4 * m + h)
    candidate = j + d
    gap = r + h * n - d * (2 * j + d)
    if gap < 0:
        raise AssertionError("order-1 lower predictor overshot the target root")

    corrections = 0
    odd_width = 2 * candidate + 1
    while gap >= odd_width:
        gap -= odd_width
        candidate += 1
        corrections += 1
        if corrections > 2:
            raise AssertionError("linear deep-tail two-correction theorem failed")
        odd_width += 2

    state = LinearDeepTailState(
        n=n,
        multiplier=target_multiplier,
        root=candidate,
        remainder=gap,
        source_multiplier=m,
        step_from_previous=h,
        correction_steps=corrections,
    )
    if state.target_value != target_multiplier * n:
        raise AssertionError("linear deep-tail transport failed exact reconstruction")
    return state


def transport_order1_linear_tail(
    source: MultiplierStateLike,
    target_multiplier: int,
) -> LinearDeepTailState:
    """Transport one certified h=1 or h=2 step using the linear predictor.

    This general entrypoint checks the exact state-dependent order-1 Pell
    certificate.  Long streams should use :func:`odd_n_linear_deep_tail_states`,
    which checks the common monotone tail threshold only once.
    """
    _require_positive("target_multiplier", target_multiplier)
    n = source.n
    m = source.multiplier
    j = source.root
    r = source.remainder
    _require_positive("n", n)
    _require_positive("source multiplier", m)
    _require_nonnegative("root", j)
    _require_nonnegative("remainder", r)
    h = target_multiplier - m
    if h not in (1, 2):
        raise ValueError("linear deep-tail transport supports forward steps 1 or 2")
    if j * j + r != m * n:
        raise ValueError("source state does not reconstruct m*n")
    if not 0 <= r <= 2 * j:
        raise ValueError("source remainder escaped its BRC basin")
    if not order1_two_correction_certificate(j, m, h):
        raise ValueError("order-1 Pell certificate does not hold at this state")
    return _transport_order1_core(source, target_multiplier)


def odd_n_linear_deep_tail_states(
    n: int,
    start_multiplier: int,
    state_count: int,
) -> tuple[LinearDeepTailState, ...]:
    """Materialize an unbounded odd-N sparse tail with one initial square root.

    ``start_multiplier`` must be an odd-N mod-8 representative at or beyond the
    common threshold ``4*m^5>=N``.  The returned tuple includes the initial
    state, so ``state_count=1`` performs no transport.
    """
    _require_positive("n", n)
    _require_positive("start_multiplier", start_multiplier)
    _require_positive("state_count", state_count)
    if n % 2 == 0:
        raise ValueError("odd-N sparse tail requires odd n")
    if not odd_n_multiplier_is_representative(start_multiplier):
        raise ValueError("start_multiplier must lie in the odd-N mod-8 representative set")
    if not common_mod8_linear_tail_sufficient(n, start_multiplier):
        raise ValueError("start_multiplier is before the common linear deep tail")

    target = start_multiplier * n
    root = isqrt(target)
    current = LinearDeepTailState(
        n=n,
        multiplier=start_multiplier,
        root=root,
        remainder=target - root * root,
        source_multiplier=start_multiplier,
        step_from_previous=0,
        correction_steps=0,
    )
    states = [current]

    for _ in range(1, state_count):
        target_multiplier = next_odd_n_representative_multiplier(current.multiplier)
        # The common threshold is monotone in m; no per-step certificate is needed.
        current = _transport_order1_core(current, target_multiplier)
        states.append(current)
    return tuple(states)


__all__ = [
    "ODD_N_REPRESENTATIVE_RESIDUES",
    "LinearDeepTailState",
    "odd_n_multiplier_is_representative",
    "next_odd_n_representative_multiplier",
    "order1_pell_pair",
    "order1_two_correction_certificate",
    "linear_tail_sufficient",
    "common_mod8_linear_tail_sufficient",
    "linear_tail_threshold",
    "common_mod8_linear_tail_threshold",
    "transport_order1_linear_tail",
    "odd_n_linear_deep_tail_states",
]
