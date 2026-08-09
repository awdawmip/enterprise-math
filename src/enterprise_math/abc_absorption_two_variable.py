"""Exact two-variable L-infinity Bezout solver for P025 structured families.

The helper solves ``A*u+B*v=N`` in integers while minimizing
``max(|u|,|v|)``.  This is a one-dimensional affine-lattice problem with an
exact interval-feasibility characterization.  P025 uses it to specialize the
absorption-access radius for triples ``1+q*r=p^m``.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .abc_absorption_formula import one_plus_squarefree_to_prime_power_absorption
from .abc_support import prime_factorization


@dataclass(frozen=True)
class TwoVariableLinfSolution:
    coefficient_a: int
    coefficient_b: int
    target: int
    u: int
    v: int
    parameter: int
    homogeneous_direction: tuple[int, int]
    radius: int
    triangle_lower_bound: int


def _extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        if a >= 0:
            return a, 1, 0
        return -a, -1, 0
    g, x1, y1 = _extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def _ceil_div(numerator: int, positive_denominator: int) -> int:
    if positive_denominator <= 0:
        raise ValueError("denominator must be positive")
    return -((-numerator) // positive_denominator)


def _parameter_interval(
    particular: tuple[int, int],
    direction: tuple[int, int],
    radius: int,
) -> tuple[int, int] | None:
    lower: int | None = None
    upper: int | None = None
    for x0, step in zip(particular, direction, strict=True):
        if step == 0:
            if abs(x0) > radius:
                return None
            continue
        if step > 0:
            lo = _ceil_div(-radius - x0, step)
            hi = (radius - x0) // step
        else:
            magnitude = -step
            lo = _ceil_div(x0 - radius, magnitude)
            hi = (x0 + radius) // magnitude
        lower = lo if lower is None else max(lower, lo)
        upper = hi if upper is None else min(upper, hi)
        if lower > upper:
            return None
    if lower is None or upper is None:
        raise AssertionError("nontrivial Diophantine equation lost homogeneous direction")
    return lower, upper


def minimum_linf_diophantine_solution(A: int, B: int, N: int) -> TwoVariableLinfSolution:
    """Solve ``A*u+B*v=N`` with exact minimum ``max(|u|,|v|)``.

    Coefficients may have either sign but must not both vanish.  A solution must
    exist.  The continuous triangle inequality gives the exact universal lower
    bound ``ceil(|N|/(|A|+|B|))``; interval feasibility decides whether and when
    that lower bound is attained.
    """
    for name, value in (("A", A), ("B", B), ("N", N)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    if A == 0 and B == 0:
        raise ValueError("A and B cannot both be zero")
    divisor = gcd(abs(A), abs(B))
    if N % divisor != 0:
        raise ValueError("Diophantine equation has no integer solution")

    g, x, y = _extended_gcd(A, B)
    scale = N // g
    particular = (x * scale, y * scale)
    direction = (B // g, -A // g)
    upper = max(abs(particular[0]), abs(particular[1]))
    lower_bound = _ceil_div(abs(N), abs(A) + abs(B))

    lo = lower_bound
    hi = upper
    while lo < hi:
        mid = (lo + hi) // 2
        if _parameter_interval(particular, direction, mid) is None:
            lo = mid + 1
        else:
            hi = mid
    radius = lo
    interval = _parameter_interval(particular, direction, radius)
    if interval is None:
        raise AssertionError("minimum radius must be feasible")
    candidates = {interval[0], interval[1]}
    parameter = min(
        candidates,
        key=lambda k: (
            max(abs(particular[0] + k * direction[0]), abs(particular[1] + k * direction[1])),
            abs(k),
            k,
        ),
    )
    u = particular[0] + parameter * direction[0]
    v = particular[1] + parameter * direction[1]
    if A * u + B * v != N:
        raise AssertionError("minimum solution escaped Diophantine equation")
    if max(abs(u), abs(v)) != radius:
        raise AssertionError("minimum radius not realized")

    return TwoVariableLinfSolution(
        coefficient_a=A,
        coefficient_b=B,
        target=N,
        u=u,
        v=v,
        parameter=parameter,
        homogeneous_direction=direction,
        radius=radius,
        triangle_lower_bound=lower_bound,
    )


def one_plus_two_primes_prime_power_access(
    q: int,
    r: int,
    p: int,
    exponent: int,
) -> dict[str, int | bool | tuple[int, int, int]]:
    """Specialize ``nu`` for an actual relation ``1+q*r=p^exponent``.

    Here ``q,r,p`` are pairwise distinct primes.  In coordinates ``(q,r,p)``
    the additive and raw Wronskian equations at the absorption floor reduce to

        r*x_q + q*x_r = exponent*p^(exponent-1),
        x_p = 1.

    Therefore ``nu=max(1, min max(|x_q|,|x_r|))`` for that two-variable
    Diophantine equation.  Supplement 05 gives ``eta_min=exponent``.
    """
    for name, prime in (("q", q), ("r", r), ("p", p)):
        if isinstance(prime, bool) or not isinstance(prime, int) or prime <= 1:
            raise ValueError(f"{name} must be a prime integer > 1")
        if prime_factorization(prime) != ((prime, 1),):
            raise ValueError(f"{name} must be prime")
    if len({q, r, p}) != 3:
        raise ValueError("q,r,p must be pairwise distinct")
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 1:
        raise ValueError("exponent must be a positive integer")
    b = q * r
    c = p**exponent
    if 1 + b != c:
        raise ValueError("require the actual relation 1+q*r=p^exponent")

    eta = one_plus_squarefree_to_prime_power_absorption(b, p, exponent)
    target = exponent * p ** (exponent - 1)
    solution = minimum_linf_diophantine_solution(r, q, target)
    nu = max(1, solution.radius)
    lower_bound = max(1, solution.triangle_lower_bound)
    witness = (solution.u, solution.v, 1)
    return {
        "eta_min": eta,
        "nu": nu,
        "triangle_lower_bound": lower_bound,
        "lower_bound_is_sharp": nu == lower_bound,
        "witness_q_r_p": witness,
        "target": target,
    }
