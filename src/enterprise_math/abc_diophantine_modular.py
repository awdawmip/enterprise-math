"""Closed modular solver for positive two-variable L-infinity Diophantine access.

For coprime positive ``A,B`` and non-negative target ``N``, write

    S = A+B,  s = u-v.

Then ``A*u+B*v=N`` is equivalent to

    A*s == N (mod S),
    u = (N+B*s)/S,
    v = (N-A*s)/S.

The real L-infinity objective is strictly increasing away from ``s=0`` on each
side, so among the congruence class only the nearest non-negative and nearest
negative representatives can minimize the norm.  Thus one modular inverse and
two candidates solve the exact integer problem.

This is elementary Diophantine optimization used as a P025 calibration tool.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd


@dataclass(frozen=True)
class ModularLinfSolution:
    A: int
    B: int
    N: int
    residue: int
    candidate_differences: tuple[int, ...]
    u: int
    v: int
    difference: int
    radius: int


def _extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        if a >= 0:
            return a, 1, 0
        return -a, -1, 0
    g, x1, y1 = _extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def _solution_from_difference(A: int, B: int, N: int, difference: int) -> tuple[int, int]:
    S = A + B
    u_num = N + B * difference
    v_num = N - A * difference
    if u_num % S or v_num % S:
        raise ValueError("difference does not lie in the required congruence class")
    return u_num // S, v_num // S


def minimum_linf_two_variable_modular(A: int, B: int, N: int) -> ModularLinfSolution:
    """Solve ``A*u+B*v=N`` exactly for coprime positive ``A,B`` and ``N>=0``."""
    for name, value in (("A", A), ("B", B)):
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer")
    if isinstance(N, bool) or not isinstance(N, int) or N < 0:
        raise ValueError("N must be a non-negative integer")
    if gcd(A, B) != 1:
        raise ValueError("A and B must be coprime; reduce the equation first")

    S = A + B
    if N == 0:
        return ModularLinfSolution(A, B, N, 0, (0,), 0, 0, 0, 0)

    g, inverse, _ = _extended_gcd(A, S)
    if g != 1:
        raise AssertionError("gcd(A,A+B)=gcd(A,B)=1")
    residue = (inverse * N) % S

    if residue == 0:
        differences = (0,)
    else:
        differences = (residue, residue - S)

    candidates: list[tuple[int, int, int, int]] = []
    for difference in differences:
        u, v = _solution_from_difference(A, B, N, difference)
        radius = max(abs(u), abs(v))
        candidates.append((radius, abs(difference), difference, u))

    _radius, _abs_difference, best_difference, _u_tiebreak = min(candidates)
    u, v = _solution_from_difference(A, B, N, best_difference)
    radius = max(abs(u), abs(v))
    if A * u + B * v != N:
        raise AssertionError("modular solver escaped the Diophantine equation")

    return ModularLinfSolution(
        A=A,
        B=B,
        N=N,
        residue=residue,
        candidate_differences=differences,
        u=u,
        v=v,
        difference=best_difference,
        radius=radius,
    )


def reduced_minimum_linf_two_variable_modular(A: int, B: int, N: int) -> ModularLinfSolution:
    """Reduce a solvable positive equation by gcd and use the closed solver.

    The returned coefficients/target are the reduced equation.  Solutions in
    ``u,v`` are unchanged by common-factor cancellation.
    """
    for name, value in (("A", A), ("B", B)):
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer")
    if isinstance(N, bool) or not isinstance(N, int) or N < 0:
        raise ValueError("N must be a non-negative integer")
    d = gcd(A, B)
    if N % d:
        raise ValueError("Diophantine equation has no integer solution")
    return minimum_linf_two_variable_modular(A // d, B // d, N // d)
