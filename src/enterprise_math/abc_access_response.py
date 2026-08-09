"""Eventual affine-periodic structure of two-variable certificate access.

For coprime positive A,B define

    kappa(N) = min_{A*u+B*v=N} max(|u|,|v|).

The exact modular two-candidate solver shows that kappa need not be monotone at
small targets.  After a finite coefficient-scale boundary, however, the
minimum is given by a residue-periodic non-negative balanced solution and
satisfies ``kappa(N+A+B)=kappa(N)+1`` exactly.

This is elementary Diophantine optimization used as a finite-precision
calibration.  No historical novelty is claimed for eventual quasipolynomial /
periodic behavior of parametric integer optimization.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .abc_diophantine_modular import minimum_linf_two_variable_modular


@dataclass(frozen=True)
class StableAccessResponse:
    A: int
    B: int
    target: int
    period: int
    residue_difference: int
    periodic_penalty: int
    radius: int


def _extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        if a >= 0:
            return a, 1, 0
        return -a, -1, 0
    g, x1, y1 = _extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def stable_access_formula(A: int, B: int, N: int) -> StableAccessResponse:
    """Return the explicit stable formula for ``N >= max(A,B)^2``.

    Let ``S=A+B`` and ``r in {0,...,S-1}`` solve ``A*r=N mod S``.  In the
    stable non-negative region the better of the two nearest congruence
    representatives has penalty

        delta(r) = min(B*r, A*(S-r)).

    Hence

        kappa(N) = (N + delta(r)) / S.
    """
    for name, value in (("A", A), ("B", B)):
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer")
    if isinstance(N, bool) or not isinstance(N, int) or N < 0:
        raise ValueError("N must be a non-negative integer")
    if gcd(A, B) != 1:
        raise ValueError("A and B must be coprime")
    M = max(A, B)
    if N < M * M:
        raise ValueError("stable formula requires N >= max(A,B)^2")

    S = A + B
    g, inverse, _ = _extended_gcd(A, S)
    if g != 1:
        raise AssertionError("coprime coefficients imply A invertible mod A+B")
    r = (inverse * N) % S
    positive_penalty = B * r
    negative_penalty = A * (S - r) if r else 0
    if r == 0 or positive_penalty <= negative_penalty:
        difference = r
        penalty = positive_penalty
    else:
        difference = r - S
        penalty = negative_penalty

    numerator = N + penalty
    if numerator % S:
        raise AssertionError("stable residue penalty must make numerator divisible by period")
    radius = numerator // S

    exact = minimum_linf_two_variable_modular(A, B, N)
    if exact.radius != radius:
        raise AssertionError("stable closed formula disagrees with exact modular optimum")

    return StableAccessResponse(
        A=A,
        B=B,
        target=N,
        period=S,
        residue_difference=difference,
        periodic_penalty=penalty,
        radius=radius,
    )


def access_period_shift_holds(A: int, B: int, N: int) -> bool:
    """Verify ``kappa(N+A+B)=kappa(N)+1`` in the stable region."""
    current = stable_access_formula(A, B, N)
    future = stable_access_formula(A, B, N + A + B)
    if future.residue_difference != current.residue_difference:
        raise AssertionError("period shift changed residue class")
    if future.periodic_penalty != current.periodic_penalty:
        raise AssertionError("period shift changed periodic penalty")
    if future.radius != current.radius + 1:
        raise AssertionError("stable access recurrence failed")
    return True


def local_access_nonmonotonicity_example() -> dict[str, int]:
    """Return the exact ``(A,B)=(5,2)`` small-target inversion."""
    first = minimum_linf_two_variable_modular(5, 2, 1)
    second = minimum_linf_two_variable_modular(5, 2, 2)
    if not first.radius > second.radius:
        raise AssertionError("access nonmonotonicity example changed")
    return {
        "A": 5,
        "B": 2,
        "kappa_1": first.radius,
        "kappa_2": second.radius,
    }


def one_period_lipschitz(A: int, B: int, N: int) -> bool:
    """Verify the global bound ``|kappa(N+S)-kappa(N)|<=1`` exactly.

    Adding ``(1,1)`` to any solution raises the target by ``S=A+B`` and changes
    L-infinity norm by at most one.  Subtracting ``(1,1)`` gives the reverse
    inequality.
    """
    if gcd(A, B) != 1:
        raise ValueError("A and B must be coprime")
    if N < 0:
        raise ValueError("N must be non-negative")
    left = minimum_linf_two_variable_modular(A, B, N).radius
    right = minimum_linf_two_variable_modular(A, B, N + A + B).radius
    if abs(right - left) > 1:
        raise AssertionError("one-period access Lipschitz bound failed")
    return True
