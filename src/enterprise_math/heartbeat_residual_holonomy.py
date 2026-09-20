
"""Integer monodromy and residual-torsion diagnostics for Heartbeat World.

Research candidate / domain operator.  This module works on the raw signed X6
chart Z^6 and a declared periodic integer-linear heartbeat program.  It does
not turn residual/control state into extra spatial dimensions and does not
claim a fixed heartbeat program as a world axiom.

The finite residual group of an injective integer matrix M is coker(M)=Z^n/MZ^n.
Smith invariant factors are computed from determinantal divisors.  The current
implementation is intended for small n (especially n=6), not large-matrix SNF.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
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
        raise ValueError("nonnegative integer exponent required")
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


def _is_prime(p: int) -> bool:
    if type(p) is not int or p < 2:
        return False
    d = 2
    while d * d <= p:
        if p % d == 0:
            return False
        d += 1
    return True


def prime_valuation(value: int, prime: int) -> int:
    if type(value) is not int or value == 0:
        raise ValueError("nonzero integer value required")
    if not _is_prime(prime):
        raise ValueError("prime must be prime")
    n = abs(value)
    out = 0
    while n % prime == 0:
        n //= prime
        out += 1
    return out


def cyclic_weighted_heartbeat(factors) -> Matrix:
    """A_bvec(z)=(b6*z6,b1*z1,...,b5*z5) for positive integer factors."""
    factors = tuple(factors)
    if not factors or any(type(b) is not int or b < 1 for b in factors):
        raise ValueError("positive integer cyclic scale factors required")
    n = len(factors)
    a = [[0] * n for _ in range(n)]
    a[0][-1] = factors[-1]
    for i in range(1, n):
        a[i][i - 1] = factors[i - 1]
    return tuple(tuple(row) for row in a)


def cyclic_valuation_depths(factors, prime: int, beats: int) -> tuple[int, ...]:
    """Sorted p-adic Smith-depth profile for a cyclic weighted heartbeat power.

    If k=n*q+r, every axis gets q complete-cycle valuation V_p, plus the
    valuation sum in one cyclic window of r consecutive per-axis factors.
    """
    factors = tuple(factors)
    if not factors or any(type(b) is not int or b < 1 for b in factors):
        raise ValueError("positive integer cyclic scale factors required")
    if not _is_prime(prime):
        raise ValueError("prime must be prime")
    if type(beats) is not int or beats < 0:
        raise ValueError("nonnegative integer beat count required")
    n = len(factors)
    q, r = divmod(beats, n)
    vals = tuple(prime_valuation(b, prime) for b in factors)
    full = sum(vals)
    if not r:
        return (q * full,) * n
    depths = []
    for start in range(n):
        depths.append(q * full + sum(vals[(start + j) % n] for j in range(r)))
    return tuple(sorted(depths))


def monomial_action(matrix):
    """Return (permutation, column weights) for an integer monomial matrix."""
    a = _matrix(matrix)
    n = len(a)
    permutation = []
    weights = []
    used_rows = set()
    for j in range(n):
        rows = [i for i in range(n) if a[i][j] != 0]
        if len(rows) != 1:
            raise ValueError("monomial matrix requires exactly one nonzero per column")
        i = rows[0]
        if i in used_rows:
            raise ValueError("monomial matrix requires exactly one nonzero per row")
        used_rows.add(i)
        permutation.append(i)
        weights.append(a[i][j])
    if len(used_rows) != n:
        raise ValueError("monomial matrix requires every row to be used")
    return tuple(permutation), tuple(weights)


def monomial_cycles(matrix) -> tuple[tuple[int, ...], ...]:
    permutation, _weights = monomial_action(matrix)
    n = len(permutation)
    seen = set()
    cycles = []
    for start in range(n):
        if start in seen:
            continue
        cycle = []
        j = start
        while j not in seen:
            seen.add(j)
            cycle.append(j)
            j = permutation[j]
        if j != start:
            raise ArithmeticError("invalid permutation cycle decomposition")
        cycles.append(tuple(cycle))
    return tuple(cycles)


def monomial_cycle_valuation_data(matrix, prime: int):
    """Return (cycle, total p-valuation, length) for every permutation cycle."""
    if not _is_prime(prime):
        raise ValueError("prime must be prime")
    permutation, weights = monomial_action(matrix)
    cycles = monomial_cycles(matrix)
    return tuple(
        (cycle, sum(prime_valuation(weights[j], prime) for j in cycle), len(cycle))
        for cycle in cycles
    )


def monomial_valuation_depths(matrix, prime: int, beats: int) -> tuple[int, ...]:
    """Sorted p-adic Smith depths of a monomial matrix power."""
    if type(beats) is not int or beats < 0:
        raise ValueError("nonnegative integer beat count required")
    if not _is_prime(prime):
        raise ValueError("prime must be prime")
    permutation, weights = monomial_action(matrix)
    vals = tuple(prime_valuation(w, prime) for w in weights)
    depths = []
    for start in range(len(permutation)):
        j = start
        depth = 0
        for _ in range(beats):
            depth += vals[j]
            j = permutation[j]
        depths.append(depth)
    return tuple(sorted(depths))


def monomial_valuation_balance(matrix, prime: int) -> bool:
    """Whether all permutation cycles have the same mean p-adic growth."""
    data = monomial_cycle_valuation_data(matrix, prime)
    v0, l0 = data[0][1], data[0][2]
    return all(v * l0 == v0 * length for _cycle, v, length in data[1:])


def periodic_monomial_valuation_balance(steps, prime: int) -> bool:
    """Phase-invariant bounded-anisotropy criterion for periodic monomial beats."""
    steps = tuple(_matrix(step) for step in steps)
    if not steps:
        raise ValueError("nonempty heartbeat program required")
    for step in steps:
        monomial_action(step)
    verdicts = tuple(
        monomial_valuation_balance(monodromy(steps, start=t), prime)
        for t in range(len(steps))
    )
    if len(set(verdicts)) != 1:
        raise ArithmeticError("phase-shifted periodic monomial balance must agree")
    return verdicts[0]


def characteristic_coefficients(matrix) -> tuple[int, ...]:
    """Characteristic polynomial coefficients in ascending x-power order.

    Uses exact Faddeev-LeVerrier arithmetic and checks every integer division.
    For A, returns (c_0,...,c_(n-1),1) with det(xI-A)=sum c_i*x^i.
    """
    a = _matrix(matrix)
    n = len(a)
    b = identity(n)
    descending = [1]
    for k in range(1, n + 1):
        ab = matmul(a, b)
        trace = sum(ab[i][i] for i in range(n))
        if trace % k:
            raise ArithmeticError("nonexact Faddeev-LeVerrier division")
        c = -(trace // k)
        descending.append(c)
        b = tuple(tuple(ab[i][j] + (c if i == j else 0)
                        for j in range(n)) for i in range(n))
    return tuple(reversed(descending))


def newton_root_valuations(matrix, prime: int) -> tuple[Fraction, ...]:
    """p-adic root valuations of the characteristic polynomial.

    Values are the negatives of lower Newton-polygon slopes, repeated by
    horizontal length. A nonzero determinant is required so all root
    valuations are finite.
    """
    a = _matrix(matrix)
    if determinant(a) == 0:
        raise ValueError("nonsingular matrix required for finite carry slopes")
    if not _is_prime(prime):
        raise ValueError("prime must be prime")
    coeffs = characteristic_coefficients(a)
    points = tuple((i, Fraction(prime_valuation(c, prime), 1))
                   for i, c in enumerate(coeffs) if c)
    hull = []
    def slope(left, right):
        return Fraction(right[1] - left[1], right[0] - left[0])
    for point in points:
        while len(hull) >= 2 and slope(hull[-2], hull[-1]) >= slope(hull[-1], point):
            hull.pop()
        hull.append(point)
    values = []
    for left, right in zip(hull, hull[1:]):
        values.extend([-slope(left, right)] * (right[0] - left[0]))
    if len(values) != len(a):
        raise ArithmeticError("Newton polygon did not account for all roots")
    return tuple(sorted(values))


def carry_slope_spectrum(matrix, prime: int) -> tuple[Fraction, ...]:
    """Asymptotic p-primary Smith-depth slopes for powers of an integer matrix."""
    return newton_root_valuations(matrix, prime)


def carry_spread_rate(matrix, prime: int) -> Fraction:
    """Linear growth rate of max-minus-min p-primary Smith depth."""
    slopes = carry_slope_spectrum(matrix, prime)
    return slopes[-1] - slopes[0]


def carry_balanced(matrix, prime: int) -> bool:
    """Whether p-primary Smith-depth anisotropy is asymptotically bounded."""
    return carry_spread_rate(matrix, prime) == 0


def phase_carry_spectra(steps, prime: int) -> tuple[tuple[Fraction, ...], ...]:
    """Carry-slope spectrum at every phase cut of one periodic heartbeat."""
    steps = tuple(_matrix(step) for step in steps)
    if not steps:
        raise ValueError("nonempty heartbeat program required")
    spectra = tuple(carry_slope_spectrum(monodromy(steps, start=t), prime)
                    for t in range(len(steps)))
    if any(spectrum != spectra[0] for spectrum in spectra[1:]):
        raise ArithmeticError("rationally conjugate phase monodromies must share carry slopes")
    return spectra


def smith_p_depths(matrix, prime: int, power: int) -> tuple[int, ...]:
    """Finite p-primary Smith depths of matrix**power."""
    if type(power) is not int or power < 1:
        raise ValueError("positive integer power required")
    return tuple(prime_valuation(d, prime)
                 for d in smith_invariant_factors(matpow(matrix, power)))


def smith_factor_ratio(matrix, power: int, *, step=1) -> tuple[int, ...]:
    """Componentwise Smith-factor growth from power to power+step.

    This is a finite diagnostic only. Repeated ratios on a tested window do
    not by themselves certify eventual periodicity.
    """
    if type(power) is not int or power < 1:
        raise ValueError("positive integer power required")
    if type(step) is not int or step < 1:
        raise ValueError("positive integer step required")
    left = smith_invariant_factors(matpow(matrix, power))
    right = smith_invariant_factors(matpow(matrix, power + step))
    ratios = []
    for a, b in zip(left, right):
        if b % a:
            raise ArithmeticError("Smith invariant-factor divisibility failed")
        ratios.append(b // a)
    return tuple(ratios)


def smith_increment_trace(matrix, start: int, count: int, *, step=1) -> tuple[tuple[int, ...], ...]:
    """Finite trace of Smith growth ratios; a diagnostic, not an eventual-period proof."""
    if type(start) is not int or start < 1 or type(count) is not int or count < 0:
        raise ValueError("start>=1 and count>=0 integers required")
    return tuple(smith_factor_ratio(matrix, start + j * step, step=step)
                 for j in range(count))
