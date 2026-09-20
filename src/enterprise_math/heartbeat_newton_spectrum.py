"""Exact Newton-slope diagnostics for periodic integer Heartbeat World maps.

Extension of the existing residual-holonomy/T5/T9/BRC tools; not Foundation.
A fixed nonsingular integer monodromy M has local Smith depths a_i(M**n)
with a_i=n*lambda_i+O_M,p(1), where lambda_i are the Newton slopes of char(M).
This module extracts slopes and a constructive all-n bound in the one-slope
case. It does not replace finite residual groups by slopes, preserve arbitrary
BRC effects, identify Smith channels with physical native axes, or assert
real-metric stability. No floating-point or p-adic root approximation is used.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from .heartbeat_residual_holonomy import (
    _matrix, _is_prime, determinant, identity, matmul, matpow, monodromy,
    prime_valuation, smith_invariant_factors,
)
from .brc_transport import eye, mm, mpow, inv, matrix as qmatrix, sm


def _prime(p: int) -> int:
    if not _is_prime(p):
        raise ValueError('prime must be a prime integer')
    return p


def _integer_map(rows):
    a = _matrix(rows)
    if len(a) > 6 or determinant(a) == 0:
        raise ValueError('nonsingular integer matrix of dimension 1..6 required')
    return a


def valuation(value: int | F, prime: int) -> int | None:
    """Exact valuation; None denotes +infinity (zero), never a missing value."""
    _prime(prime)
    if isinstance(value, bool) or not isinstance(value, (int, F)):
        raise TypeError('int/Fraction required')
    q = F(value)
    if not q:
        return None
    return prime_valuation(q.numerator, prime)-prime_valuation(q.denominator, prime)


def characteristic_coefficients(rows) -> tuple[F, ...]:
    """Descending monic coefficients, using exact Newton trace identities."""
    a = qmatrix(rows)
    n = len(a)
    if len(a[0]) != n or n > 6:
        raise ValueError('square rational matrix of dimension 1..6 required')
    power = eye(n)
    traces = [F(n)]
    for _ in range(n):
        power = mm(power, a)
        traces.append(sum((power[i][i] for i in range(n)), F(0)))
    coefficients = [F(1)]
    for k in range(1, n+1):
        coefficients.append(-sum((coefficients[k-j]*traces[j]
                                 for j in range(1, k+1)), F(0))/k)
    return tuple(coefficients)


def newton_polygon(coefficients, prime: int):
    """Lower hull of (j,v_p(c_j)) for x^d+c1*x^(d-1)+...+cd.

    With this descending-coefficient convention slopes, NOT their negatives,
    are root valuations. Collinear interior points are removed.
    """
    _prime(prime)
    c = tuple(coefficients)
    if len(c) < 2 or c[0] != 1 or c[-1] == 0:
        raise ValueError('monic positive-degree polynomial with nonzero constant required')
    hull = []
    for j, value in enumerate(c):
        v = valuation(value, prime)
        if v is None:
            continue
        point = (j, v)
        while len(hull) >= 2:
            a, b = hull[-2:]
            cross = (b[0]-a[0])*(v-b[1])-(b[1]-a[1])*(j-b[0])
            if cross > 0:
                break
            hull.pop()
        hull.append(point)
    return tuple(hull)


@dataclass(frozen=True)
class NewtonSpectrum:
    prime: int
    coefficients: tuple[F, ...]
    vertices: tuple[tuple[int, int], ...]
    slopes: tuple[F, ...]

    @classmethod
    def from_matrix(cls, rows, prime: int):
        a = _integer_map(rows)
        c = characteristic_coefficients(a)
        hull = newton_polygon(c, prime)
        slopes = []
        for (x0, y0), (x1, y1) in zip(hull, hull[1:]):
            slopes.extend([F(y1-y0, x1-x0)]*(x1-x0))
        return cls(prime, c, hull, tuple(slopes))

    @property
    def balanced(self) -> bool:
        return self.slopes[0] == self.slopes[-1]

    @property
    def spread_rate(self) -> F:
        return self.slopes[-1]-self.slopes[0]

    @property
    def determinant_depth(self) -> int:
        result = sum(self.slopes, F(0))
        if result.denominator != 1:
            raise ArithmeticError('integer determinant depth expected')
        return int(result)

    def coefficient_obstruction(self):
        """First exact violation of d*v(c_j)>=j*v(det), or None."""
        d, s = len(self.slopes), self.determinant_depth
        for j, c in enumerate(self.coefficients[1:], 1):
            v = valuation(c, self.prime)
            if v is not None and d*v < j*s:
                return j, v, F(j*s, d)
        return None


def _matrix_valuation(a, p):
    vals = [valuation(v, p) for row in a for v in row if v]
    if not vals:
        raise ValueError('nonzero matrix required')
    return min(vals)


@dataclass(frozen=True)
class BalanceCertificate:
    source_digest: str
    prime: int
    dimension: int
    slope: F
    normalized_coefficients: tuple[F, ...]
    lower_offsets: tuple[F, ...]
    upper_offsets: tuple[F, ...]

    def interval(self, repetitions: int) -> tuple[F, F]:
        if type(repetitions) is not int or repetitions < 0:
            raise ValueError('nonnegative integer repetition count required')
        r = repetitions % self.dimension
        center = repetitions*self.slope
        return center-self.lower_offsets[r], center+self.upper_offsets[r]

    @property
    def spread_bound(self) -> F:
        return max(a+b for a, b in zip(self.lower_offsets, self.upper_offsets))

    def recheck(self, rows):
        if certify_balanced_powers(rows, self.prime) != self:
            raise ValueError('matrix/certificate mismatch')
        return True


def certify_balanced_powers(rows, prime: int) -> BalanceCertificate:
    """Construct a uniform all-n Smith-depth interval, not a simulation guess.

    Set d=dimension, s=v(det M), B=M^d/p^s. One Newton slope implies both
    char(B) and char(B^-1) are p-integral, with unit constant coefficient.
    Cayley-Hamilton bounds all B^q and B^-q by their first d powers. Combine
    with the d finite prefixes M^r. Fractional entries are diagnostic only;
    they do not authorize fractional primitive Cell moves.
    """
    a = _integer_map(rows)
    spectrum = NewtonSpectrum.from_matrix(a, prime)
    if not spectrum.balanced:
        raise ValueError(f'multiple slopes: coefficient obstruction {spectrum.coefficient_obstruction()}')
    d, s = len(a), spectrum.determinant_depth
    b = sm(F(1, prime**s), qmatrix(matpow(a, d)))
    bi = inv(b)
    cb, cbi = characteristic_coefficients(b), characteristic_coefficients(bi)
    for c in (cb, cbi):
        if valuation(c[-1], prime) != 0 or any(
            v is not None and v < 0 for v in (valuation(x, prime) for x in c)
        ):
            raise ArithmeticError('normalized integral-unit characteristic certificate failed')
    bp, bm = eye(d), eye(d)
    kp = km = 0
    for _ in range(d):
        kp = max(kp, -_matrix_valuation(bp, prime))
        km = max(km, -_matrix_valuation(bm, prime))
        bp, bm = mm(bp, b), mm(bm, bi)
    aq, ai = qmatrix(a), inv(qmatrix(a))
    rp, ri = eye(d), eye(d)
    lower, upper = [], []
    alpha = F(s, d)
    for r in range(d):
        lower.append(r*alpha+kp-_matrix_valuation(rp, prime))
        upper.append(km-_matrix_valuation(ri, prime)-r*alpha)
        rp, ri = mm(rp, aq), mm(ri, ai)
    digest = sha256(repr(a).encode('utf-8')).hexdigest()
    return BalanceCertificate(digest, prime, d, alpha, cb, tuple(lower), tuple(upper))


def local_smith_depths(rows, prime: int, repetitions=1):
    a = _integer_map(rows)
    _prime(prime)
    factors = smith_invariant_factors(matpow(a, repetitions))
    return tuple(prime_valuation(x, prime) for x in factors)


def periodic_newton_spectra(steps, prime: int):
    steps = tuple(_integer_map(step) for step in steps)
    if not steps:
        raise ValueError('nonempty periodic program required')
    spectra = tuple(NewtonSpectrum.from_matrix(monodromy(steps, start=t), prime)
                    for t in range(len(steps)))
    if any(s.coefficients != spectra[0].coefficients for s in spectra[1:]):
        raise ArithmeticError('phase characteristic polynomials disagree')
    return spectra


def torsion_capacity_rate(spectrum: NewtonSpectrum, depth_rate: int | F) -> F:
    """Limit (1/n) log_p |G_n[p^floor(tau*n)]| = sum min(tau,lambda_i).

    An asymptotic count observer, not an exact finite-time replacement for G_n.
    """
    if not isinstance(spectrum, NewtonSpectrum):
        raise TypeError('NewtonSpectrum required')
    if isinstance(depth_rate, bool) or not isinstance(depth_rate, (int, F)) or depth_rate < 0:
        raise ValueError('nonnegative int/Fraction depth rate required')
    return sum((min(F(depth_rate), slope) for slope in spectrum.slopes), F(0))


@dataclass(frozen=True)
class SmithRhythmCertificate:
    source_digest: str
    prime: int
    period: int
    depth_increment: int
    unit_matrix: tuple[tuple[int, ...], ...]

    def recheck(self, rows):
        a = _integer_map(rows)
        if sha256(repr(a).encode('utf-8')).hexdigest() != self.source_digest:
            raise ValueError('matrix/certificate mismatch')
        if type(self.period) is not int or self.period < 1:
            raise ValueError('positive period required')
        if type(self.depth_increment) is not int or self.depth_increment < 0:
            raise ValueError('nonnegative depth increment required')
        _prime(self.prime)
        u = _integer_map(self.unit_matrix)
        if len(u) != len(a) or prime_valuation(determinant(u), self.prime) != 0:
            raise ValueError('local unit matrix required')
        scale = self.prime**self.depth_increment
        if matpow(a, self.period) != tuple(tuple(scale*v for v in row) for row in u):
            raise ValueError('claimed exact power identity failed')
        return True


def find_smith_rhythm(rows, prime: int, *, max_trials=256) -> SmithRhythmCertificate | None:
    """Find a finite exact local Smith rhythm; None is only search-limit exhaustion.

    Single slope alpha=a/b implies C=M^b/p^a has bounded positive/negative
    powers. Some positive C^T is a p-local unit in the original lattice.
    The returned exact identity proves a_i(n+b*T)=a_i(n)+a*T for EVERY n.
    The resulting period is not promised minimal or cheap to find.
    """
    a = _integer_map(rows)
    if type(max_trials) is not int or max_trials < 1:
        raise ValueError('positive integer max_trials required')
    spectrum = NewtonSpectrum.from_matrix(a, prime)
    if not spectrum.balanced:
        raise ValueError('no common affine Smith rhythm with multiple slopes')
    alpha = spectrum.slopes[0]
    q, s = alpha.denominator, alpha.numerator
    c = sm(F(1, prime**s), qmatrix(matpow(a, q)))
    power = eye(len(a))
    for t in range(1, max_trials+1):
        power = mm(power, c)
        if _matrix_valuation(power, prime) >= 0:
            if any(v.denominator != 1 for row in power for v in row):
                raise ArithmeticError('normalization uses only powers of the selected prime')
            unit = tuple(tuple(int(v) for v in row) for row in power)
            cert = SmithRhythmCertificate(sha256(repr(a).encode('utf-8')).hexdigest(),
                                          prime, q*t, s*t, unit)
            cert.recheck(a)
            return cert
    return None
