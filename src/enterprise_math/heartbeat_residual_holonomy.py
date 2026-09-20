
"""Integer monodromy and residual-torsion diagnostics for Heartbeat World.

Research candidate / domain operator.  This module works on the raw signed X6
chart Z^6 and a declared periodic integer-linear heartbeat program.  It does
not turn residual/control state into extra spatial dimensions and does not
claim a fixed heartbeat program as a world axiom.

The finite residual group of an injective integer matrix M is coker(M)=Z^n/MZ^n.
Smith invariant factors are computed from determinantal divisors.  The current
implementation is intended for small nn (especially n=6), not large-matrix SNF.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import combinations
from math import gcd, prod

Matrix = tuple[tuple[int, ...], ...]


def _matrix(rows) -> Matrix:
    rows = tuple(tuple(row) for row in rows)
    if not rows or any(len(row) != len(rows) for row in rows):
        raise ValueError("nonempty square matrix required")
    if any(type(v) is not int for row in rows for v in row):
        raise TypeError("integer matrix required")
    return rows


def identity(n: int) -> Matrix:
    if type(n) is not int or n < 1:
        raise ValueError("positive integer dimension required")
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def matmul(left, right) -> Matrix:
    a, b = _matrix(left), _matrix(right)
    if len(a) != len(b):
        raise ValueError("equal square dimensions required")
    n = len(a)
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n))
                     for i in range(n))


def matpow(matrix, exponent: int) -> Matrix:
    a = _matrix(matrix)
    if type(exponent) is not int or exponent < 0:
        raise ValueEError("nonnegative integer exponent required")
    out = identity(len(a))
    while exponent:
        if exponent & 1:
            out = matmul(out, a)
        exponent >>= 1
        if exponent:
            a = matmul(a, a)
    return out


def determinant(matrix) -> int:
    """Fraction-free Bareiss determinant."""
    a = [list(row) for row in _matrix(matrix)]
    n = len(a)
    if n == 1:
        return a[0][0]
    sign = 1
    prev = 1
    for k in range(n - 1):
        pivot = next((r for r in range(k, n) if a[r][k] != 0), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        p = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * p - a[i][k] * a[k][j]
                if num % prev:
                    raise ArithmeticError("Bareiss exact division failed")
                a[i][j] = num // prev
        prev = p
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[n - 1][n - 1]


def _minor(matrix: Matrix, rows, cols) -> Matrix:
    return tuple(tuple(matrix[i][j] for j in cols) for i in rows)


def smith_invariant_factors(matrix, *, dimension_limit=6) -> tuple[int, ...]:
    """Return positive Smith factors using gcds of minors.

    Complexity is combinatorial; this is intentionally bounded to small native
    X6-style matrices rather than advertised as a general large-SNF engine.
    """
    a = _matrix(matrix)
    n = len(a)
    if n > dimension_limit:
        raise ValueError("matrix exceeds declared small-dimension SNF limit")
    det = determinant(a)
    if det == 0:
        raise ValueError("finite residual group requires nonzero determinant")
    previous = 1
    factors = []
    indices = tuple(range(n))
    for k in range(1, n + 1):
        delta = 0
        for rs in combinations(indices, k):
            for cs in combinations(indices, k):
                delta = gcd(delta, abs(determinant(_minor(a, rs, cs))))
        if delta == 0 or delta % previous:
            raise ArithmeticError("invalid determinantal-divisor chain")
        factors.append(delta // previous)
        previous = delta
    if prod(factors) != abs(det):
        raise ArithmeticError("Smith factors do not match determinant")
    if any(factors[i + 1] % factors[i] for i in range(n - 1)):
        raise ArithmeticError("Smith divisibility chain failed")
    return tuple(factors)


@dataclass(frozen=True)
class ResidualProfile:
    determinant: int
    cardinality: int
    invariant_factors: tuple[int, ...]
    exponent: int

    @classmethod
    def from_matrix(cls, matrix):
        a = _matrix(matrix)
        d = determinant(a)
        if not d:
            raise ValueError("injective finite-index integer map required")
        factors = smith_invariant_factors(a)
        return cls(d, abs(d), factors, factors[-1])


def monodromy(steps, *, start=0, period=None) -> Matrix:
    """Linear monodromy A_(t+p-1)...A_t of a cyclic integer heartbeat list."""
    steps = tuple(_matrix(s) for s in steps)
    if not steps:
        raise ValueError("nonempty heartbeat program required")
    n = len(steps[0])
    if any(len(s) != n for s in steps):
        raise ValueError("heartbeat dimensions disagree")
    if type(start) is not int:
        raise TypeError("start must be integer")
    p = len(steps) if period is None else period
    if type(p) is not int or p < 1:
        raise ValueError("positive period required")
    out = identity(n)
    for j in range(p):
        out = matmul(steps[(start + j) % len(steps)], out)
    return out


def phase_residual_profiles(steps) -> tuple[ResidualProfile, ...]:
    steps = tuple(_matrix(s) for s in steps)
    return tuple(ResidualProfile.from_matrix(monodromy(steps, start=t))
                 for t in range(len(steps)))


def cyclic_radix_heartbeat(base: int, *, axes=6) -> Matrix:
    """A_b(z1,...,zn)=(b*z_n,z1,...,z_(n-1))."""
    if type(base) is not int or base < 2 or type(axes) is not int or axes < 1:
        raise ValueError("base>=2 and positive integer axes required")
    a = [[0] * axes for _ in range(axes)]
    a[0][-1] = base
    for i in range(1, axes):
        a[i][i - 1] = 1
    return tuple(tuple(row) for row in a)


def radix_staircase_factors(base: int, beats: int, *, axes=6) -> tuple[int, ...]:
    """Closed-form Smith factors of A_b^beats for the cyclic radix heartbeat."""
    if type(base) is not int or base < 2 or type(axes) is not int or axes < 1:
        raise ValueError("base>=2 and positive integer axes required")
    if type(beats) is not int or beats < 0:
        raise ValueError("nonnegative integer beat count required")
    q, r = divmod(beats, axes)
    return (base**q,) * (axes - r) + (base**(q + 1),) * r


def residual_branch_count(matrix) -> int:
    """Number of fine alternatives after forgetting the exact finite residual."""
    return ResidualProfile.from_matrix(matrix).cardinality


def torsion_killed_count(invariant_factors, multiplier: int) -> int:
    """Number of residual classes r with multiplier*r=0 in the finite cokernel.

    For a Smith decomposition direct sum Z/d_i, the kernel size of multiply-by-m
    is product gcd(|m|,d_i).  This is an observer of residual group structure,
    not merely its cardinality.
    """
    factors = tuple(invariant_factors)
    if not factors or any(type(d) is not int or d < 1 for d in factors):
        raise ValueError("positive invariant factors required")
    if type(multiplier) is not int:
        raise TypeError("integer multiplier required")
    return prod(gcd(abs(multiplier), d) for d in factors)
