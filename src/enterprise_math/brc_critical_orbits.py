"""Exact critical-word and primitive-orbit arithmetic for Enterprise BRC."""
from __future__ import annotations
from dataclasses import dataclass
from math import comb
from typing import Sequence
from .brc_critical_degeneracy import criticality_polynomial

IntMatrix = tuple[tuple[int, ...], ...]


def _matrix(matrix: Sequence[Sequence[int]]) -> IntMatrix:
    rows = tuple(tuple(row) for row in matrix)
    n = len(rows)
    if n == 0 or any(len(row) != n for row in rows):
        raise ValueError("matrix must be nonempty and square")
    for row in rows:
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError("matrix entries must be integers")
            if value < 0:
                raise ValueError("matrix entries must be non-negative")
    return rows


def _upto(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("upto must be a positive integer")
    return value


def _mul(a: IntMatrix, b: IntMatrix) -> IntMatrix:
    n = len(a)
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)) for i in range(n))


def _divisors(n: int) -> tuple[int, ...]:
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def _mobius(n: int) -> int:
    if n == 1:
        return 1
    primes = 0
    p = 2
    value = n
    while p * p <= value:
        if value % p == 0:
            value //= p
            primes += 1
            if value % p == 0:
                return 0
        p += 1
    if value > 1:
        primes += 1
    return -1 if primes % 2 else 1


def critical_word_counts(matrix: Sequence[Sequence[int]], upto: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Return total and based-closed word counts indexed by lengths 0..upto."""
    k = _matrix(matrix)
    upto = _upto(upto)
    n = len(k)
    power: IntMatrix = tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))
    total = [n]
    closed = [n]
    for _ in range(upto):
        power = _mul(power, k)
        total.append(sum(sum(row) for row in power))
        closed.append(sum(power[i][i] for i in range(n)))
    return tuple(total), tuple(closed)


def critical_primitive_orbit_counts(matrix: Sequence[Sequence[int]], upto: int) -> tuple[int, ...]:
    """Return P_n primitive periodic-orbit counts indexed by 0..upto."""
    k = _matrix(matrix)
    upto = _upto(upto)
    _, closed = critical_word_counts(k, upto)
    out = [0]
    for n in range(1, upto + 1):
        numerator = sum(_mobius(d) * closed[n // d] for d in _divisors(n))
        if numerator % n:
            raise AssertionError("Möbius primitive-orbit numerator lost divisibility")
        value = numerator // n
        if value < 0:
            raise AssertionError("primitive-orbit count became negative")
        out.append(value)
    return tuple(out)


def critical_zeta_coefficients(matrix: Sequence[Sequence[int]], upto: int) -> tuple[int, ...]:
    """Return coefficients of 1/det(I-zK) through order upto."""
    k = _matrix(matrix)
    upto = _upto(upto)
    poly = criticality_polynomial(k)
    out = [1] + [0] * upto
    for n in range(1, upto + 1):
        out[n] = -sum(poly[j] * out[n-j] for j in range(1, min(n, len(poly)-1) + 1))
    return tuple(out)


def critical_euler_coefficients(matrix: Sequence[Sequence[int]], upto: int) -> tuple[int, ...]:
    """Return and verify the truncated primitive-orbit Euler product."""
    k = _matrix(matrix)
    upto = _upto(upto)
    primitive = critical_primitive_orbit_counts(k, upto)
    series = [1] + [0] * upto
    for length in range(1, upto + 1):
        exponent = primitive[length]
        if not exponent:
            continue
        factor = [0] * (upto + 1)
        for copies in range(upto // length + 1):
            factor[copies * length] = comb(exponent + copies - 1, copies)
        new = [0] * (upto + 1)
        for i, a in enumerate(series):
            for j, b in enumerate(factor):
                if i + j <= upto:
                    new[i+j] += a * b
        series = new
    result = tuple(series)
    if result != critical_zeta_coefficients(k, upto):
        raise AssertionError("Euler prefix disagrees with determinant zeta")
    return result


@dataclass(frozen=True)
class CriticalOrbitPrefix:
    critical_matrix: IntMatrix
    total_word_counts: tuple[int, ...]
    closed_word_counts: tuple[int, ...]
    primitive_orbit_counts: tuple[int, ...]
    zeta_coefficients: tuple[int, ...]

    @property
    def upto(self) -> int:
        return len(self.primitive_orbit_counts) - 1

    def verify(self) -> bool:
        for n in range(1, self.upto + 1):
            if self.closed_word_counts[n] != sum(d * self.primitive_orbit_counts[d] for d in _divisors(n)):
                return False
        return self.zeta_coefficients == critical_zeta_coefficients(self.critical_matrix, self.upto)


def critical_orbit_prefix(matrix: Sequence[Sequence[int]], upto: int) -> CriticalOrbitPrefix:
    """Return a verified finite prefix of T43/T44 integer observables."""
    k = _matrix(matrix)
    total, closed = critical_word_counts(k, upto)
    primitive = critical_primitive_orbit_counts(k, upto)
    zeta = critical_euler_coefficients(k, upto)
    prefix = CriticalOrbitPrefix(k, total, closed, primitive, zeta)
    if not prefix.verify():
        raise AssertionError("critical orbit prefix verification failed")
    return prefix
