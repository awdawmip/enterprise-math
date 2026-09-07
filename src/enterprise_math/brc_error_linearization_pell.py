"""Exact error linearization and table-free Pell/Padé BRC tail transport.

This module records three compatible exact structures behind the multiplier
square-root error surface:

1. after a Taylor truncation has been differentiated away, derivative ratios
   are affine in derivative order;
2. repeated BRC basin correction has a quadratic gap orbit, hence linear first
   differences and constant second differences;
3. diagonal Padé approximants of sqrt(1+x) admit an integer Pell identity that
   gives a table-free lower multiplier-root predictor with an exact error
   certificate.

The rational approximation is classical Padé/Pell structure composed with the
retained BRC root/remainder state.  It is not a new factoring theorem.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Protocol


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


def post_truncation_derivative_ratio(
    truncation_degree: int,
    derivative_order: int,
) -> Fraction:
    """Return the exact affine derivative ratio ``1/2-n``.

    For E_K(x)=sqrt(1+x)-1-P_K(x), once n>K the polynomial truncation has
    vanished and

        (1+x) E_K^(n+1)(x) / E_K^n(x) = 1/2-n.
    """
    _require_nonnegative("truncation_degree", truncation_degree)
    _require_positive("derivative_order", derivative_order)
    if derivative_order <= truncation_degree:
        raise ValueError("derivative_order must exceed truncation_degree")
    return Fraction(1, 2) - derivative_order


def brc_gap_after_crossings(
    candidate_root: int,
    initial_gap: int,
    crossings: int,
) -> int:
    """Exact gap after ``crossings`` ordinary odd-width BRC basin steps.

    If a is the initial candidate root and G_0 the initial gap, then

        G_q = G_0 - q(2a+q).

    Consequently Delta G_q is linear, Delta^2 G_q=-2, and Delta^3 G_q=0.
    """
    _require_nonnegative("candidate_root", candidate_root)
    _require_nonnegative("initial_gap", initial_gap)
    _require_nonnegative("crossings", crossings)
    q = crossings
    return initial_gap - q * (2 * candidate_root + q)


def _quadratic_pair_power(multiplier: int, step: int, order: int) -> tuple[int, int]:
    """Return the quadratic-unit power pair used by the Pell predictor.

    The matrix

        [[2m+h, 2(m+h)], [2m, 2m+h]]

    is represented by u+v*sqrt(m(m+h)).  Binary powering therefore needs only
    the pair multiplication law and no square-root evaluation.
    """
    _require_positive("multiplier", multiplier)
    _require_positive("step", step)
    _require_positive("order", order)
    d = multiplier * (multiplier + step)
    result_u, result_v = 1, 0
    base_u, base_v = 2 * multiplier + step, 2
    exponent = order
    while exponent:
        if exponent & 1:
            result_u, result_v = (
                result_u * base_u + d * result_v * base_v,
                result_u * base_v + result_v * base_u,
            )
        base_u, base_v = (
            base_u * base_u + d * base_v * base_v,
            2 * base_u * base_v,
        )
        exponent >>= 1
    return result_u, result_v


def pell_pade_pair(multiplier: int, step: int, order: int) -> tuple[int, int]:
    """Return integer ``(A_n,B_n)`` with ``A_n/B_n < sqrt((m+h)/m)``.

    They satisfy the exact identity

        (m+h) B_n^2 - m A_n^2 = h^(2n+1).

    Equivalently, for x=h/m these are the diagonal Padé/Pell polynomials from

        (1+sqrt(1+x))^(2n+1) = P_n(x)+sqrt(1+x) Q_n(x),

    homogenized by ``m^n``.
    """
    _require_positive("multiplier", multiplier)
    _require_positive("step", step)
    _require_positive("order", order)
    u, v = _quadratic_pair_power(multiplier, step, order)
    a = u + (multiplier + step) * v
    b = u + multiplier * v
    if (multiplier + step) * b * b - multiplier * a * a != pow(
        step, 2 * order + 1
    ):
        raise AssertionError("Pell/Padé identity failed")
    if a < b:
        raise AssertionError("Pell/Padé lower ratio escaped sqrt-ratio >= 1")
    return a, b


def pell_linear_recurrence_next(
    previous: int,
    current: int,
    multiplier: int,
    step: int,
) -> int:
    """One step of the exact second-order linear recurrence in Padé order.

        X_(n+2) = (4m+2h) X_(n+1) - h^2 X_n.

    Both A_n and B_n obey this same recurrence.
    """
    _require_nonnegative("previous", previous)
    _require_nonnegative("current", current)
    _require_positive("multiplier", multiplier)
    _require_positive("step", step)
    return (4 * multiplier + 2 * step) * current - step * step * previous


def pell_two_correction_certificate(
    root: int,
    multiplier: int,
    step: int,
    order: int,
) -> bool:
    """Exact sufficient certificate for at most two BRC root corrections.

    Let A/B be the Pell/Padé lower ratio.  From the Pell norm,

        beta-A/B < h^(2n+1)/(2mAB), beta=sqrt((m+h)/m).

    For h in {1,2}, m>=h gives beta<=sqrt(2).  Therefore

        J*h^(2n+1) <= m*A*B

    implies J(beta-A/B)<1/2 and the target integer root is at most two BRC
    basins above floor(AJ/B).
    """
    _require_nonnegative("root", root)
    _require_positive("multiplier", multiplier)
    _require_positive("step", step)
    _require_positive("order", order)
    if step not in (1, 2) or multiplier < step:
        return False
    a, b = pell_pade_pair(multiplier, step, order)
    return root * pow(step, 2 * order + 1) <= multiplier * a * b


@dataclass(frozen=True)
class PellTailState:
    n: int
    multiplier: int
    root: int
    remainder: int
    source_multiplier: int
    pade_order: int
    correction_steps: int

    @property
    def target_value(self) -> int:
        return self.root * self.root + self.remainder


def transport_pell_tail(
    source: MultiplierStateLike,
    target_multiplier: int,
    *,
    order: int,
) -> PellTailState:
    """Certified table-free short-step transport using the Pell/Padé predictor."""
    _require_positive("target_multiplier", target_multiplier)
    _require_positive("order", order)
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
        raise ValueError("Pell tail transport currently supports forward steps 1 or 2")
    if m < h:
        raise ValueError("two-correction certificate requires step/multiplier <= 1")
    if j * j + r != m * n:
        raise ValueError("source state does not reconstruct m*n")
    if not 0 <= r <= 2 * j:
        raise ValueError("source remainder escaped its BRC basin")

    a_scale, b_scale = pell_pade_pair(m, h, order)
    if j * pow(h, 2 * order + 1) > m * a_scale * b_scale:
        raise ValueError("declared Padé order does not certify <=2 corrections")

    candidate = (a_scale * j) // b_scale
    d = candidate - j
    gap = r + h * n - d * (2 * j + d)
    if gap < 0:
        raise AssertionError("Pell/Padé lower predictor overshot target root")

    corrections = 0
    odd_width = 2 * candidate + 1
    while gap >= odd_width:
        gap -= odd_width
        candidate += 1
        corrections += 1
        if corrections > 2:
            raise AssertionError("Pell two-correction certificate failed")
        odd_width += 2

    state = PellTailState(
        n=n,
        multiplier=target_multiplier,
        root=candidate,
        remainder=gap,
        source_multiplier=m,
        pade_order=order,
        correction_steps=corrections,
    )
    if state.target_value != target_multiplier * n:
        raise AssertionError("Pell tail transport failed exact reconstruction")
    return state


__all__ = [
    "PellTailState",
    "post_truncation_derivative_ratio",
    "brc_gap_after_crossings",
    "pell_pade_pair",
    "pell_linear_recurrence_next",
    "pell_two_correction_certificate",
    "transport_pell_tail",
]
