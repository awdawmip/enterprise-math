"""Primitive cyclotomic phase clocks as an exact finite-memory alternative.

The 2D exact integer linear oscillator has only short elliptic orders.  A second
way to buy finer exact phase resolution, without adding numeric projection, is
to increase the internal integer state dimension.

For one **primitive n-th cyclotomic mode**, the minimal polynomial contains the
cyclotomic polynomial ``Phi_n`` and therefore needs at least ``phi(n)`` rational/
integer dimensions.  The integer companion matrix of ``Phi_n`` attains exactly
that dimension and has matrix order n.

This statement is deliberately about one primitive cyclotomic mode.  A general
integer matrix of exact composite order n may assemble several lower-order blocks
whose least common multiple is n, and can have a different dimension tradeoff.

For a finite-order integer matrix M, the orbit-sum quadratic coordinate

    Q(v) = sum_{k=0}^{n-1} ||M^k v||^2

is a positive integer invariant and proves bounded exact periodicity without any
real-valued angle.

Cyclotomic polynomials and companion matrices are established algebra; this E001
module is an architecture comparator for material internal-state cost, not a
novelty claim.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def euler_totient(n: int) -> int:
    _positive("n", n)
    result = n
    value = n
    prime = 2
    while prime * prime <= value:
        if value % prime == 0:
            while value % prime == 0:
                value //= prime
            result -= result // prime
        prime += 1
    if value > 1:
        result -= result // value
    return result


def _trim(poly: list[int] | tuple[int, ...]) -> tuple[int, ...]:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def _exact_monic_polynomial_division(
    dividend: tuple[int, ...],
    divisor: tuple[int, ...],
) -> tuple[int, ...]:
    if not divisor or divisor[-1] != 1:
        raise ValueError("divisor must be a nonempty monic integer polynomial")
    work = list(dividend)
    quotient = [0] * max(1, len(dividend) - len(divisor) + 1)
    while len(work) >= len(divisor):
        factor = work[-1]
        shift = len(work) - len(divisor)
        quotient[shift] = factor
        for index, coefficient in enumerate(divisor):
            work[index + shift] -= factor * coefficient
        while work and work[-1] == 0:
            work.pop()
    if any(work):
        raise AssertionError("cyclotomic polynomial division produced a remainder")
    return _trim(quotient)


def _proper_divisors(n: int) -> tuple[int, ...]:
    return tuple(d for d in range(1, n) if n % d == 0)


@lru_cache(maxsize=None)
def cyclotomic_polynomial(n: int) -> tuple[int, ...]:
    """Return Phi_n with coefficients in ascending powers."""
    _positive("n", n)
    if n == 1:
        return (-1, 1)
    poly = tuple([-1] + [0] * (n - 1) + [1])
    for divisor in _proper_divisors(n):
        poly = _exact_monic_polynomial_division(poly, cyclotomic_polynomial(divisor))
    if len(poly) - 1 != euler_totient(n):
        raise AssertionError("cyclotomic degree disagrees with Euler totient")
    return poly


Matrix = tuple[tuple[int, ...], ...]
Vector = tuple[int, ...]


def cyclotomic_companion_matrix(n: int) -> Matrix:
    poly = cyclotomic_polynomial(n)
    degree = len(poly) - 1
    if degree <= 0 or poly[-1] != 1:
        raise AssertionError("cyclotomic polynomial must be monic of positive degree")
    rows = [[0] * degree for _ in range(degree)]
    for row in range(1, degree):
        rows[row][row - 1] = 1
    for row in range(degree):
        rows[row][-1] = -poly[row]
    return tuple(tuple(row) for row in rows)


def identity_matrix(dimension: int) -> Matrix:
    _positive("dimension", dimension)
    return tuple(
        tuple(1 if i == j else 0 for j in range(dimension))
        for i in range(dimension)
    )


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right or len(left[0]) != len(right):
        raise ValueError("matrix dimensions do not compose")
    if any(len(row) != len(left[0]) for row in left) or any(len(row) != len(right[0]) for row in right):
        raise ValueError("matrices must be rectangular")
    columns = len(right[0])
    return tuple(
        tuple(
            sum(left[i][k] * right[k][j] for k in range(len(right)))
            for j in range(columns)
        )
        for i in range(len(left))
    )


def matrix_power(matrix: Matrix, exponent: int) -> Matrix:
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 0:
        raise ValueError("exponent must be a non-negative integer")
    if not matrix or any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be nonempty and square")
    result = identity_matrix(len(matrix))
    base = matrix
    power = exponent
    while power:
        if power & 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        power >>= 1
    return result


def matrix_vector(matrix: Matrix, vector: Vector) -> Vector:
    if not matrix or len(matrix[0]) != len(vector):
        raise ValueError("matrix and vector dimensions do not match")
    return tuple(sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix)


def _prime_divisors(n: int) -> tuple[int, ...]:
    value = n
    primes: list[int] = []
    p = 2
    while p * p <= value:
        if value % p == 0:
            primes.append(p)
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        primes.append(value)
    return tuple(primes)


@dataclass(frozen=True)
class PrimitiveCyclotomicClock:
    order: int
    dimension: int
    polynomial: tuple[int, ...]
    companion_matrix: Matrix
    exact_order_verified: bool


def primitive_cyclotomic_clock(order: int) -> PrimitiveCyclotomicClock:
    _positive("order", order)
    matrix = cyclotomic_companion_matrix(order)
    identity = identity_matrix(len(matrix))
    exact = matrix_power(matrix, order) == identity
    for prime in _prime_divisors(order):
        if matrix_power(matrix, order // prime) == identity:
            exact = False
    if not exact:
        raise AssertionError("cyclotomic companion failed its primitive-order certificate")
    return PrimitiveCyclotomicClock(
        order=order,
        dimension=euler_totient(order),
        polynomial=cyclotomic_polynomial(order),
        companion_matrix=matrix,
        exact_order_verified=True,
    )


def cyclotomic_step(clock: PrimitiveCyclotomicClock, state: Vector) -> Vector:
    if len(state) != clock.dimension:
        raise ValueError("state dimension does not match cyclotomic clock")
    return matrix_vector(clock.companion_matrix, state)


def cyclotomic_orbit_invariant(clock: PrimitiveCyclotomicClock, state: Vector) -> int:
    """Return sum ||M^k state||^2 over one exact period."""
    if len(state) != clock.dimension:
        raise ValueError("state dimension does not match cyclotomic clock")
    current = state
    total = 0
    for _ in range(clock.order):
        total += sum(value * value for value in current)
        current = cyclotomic_step(clock, current)
    if current != state:
        raise AssertionError("cyclotomic orbit failed exact closure")
    return total
