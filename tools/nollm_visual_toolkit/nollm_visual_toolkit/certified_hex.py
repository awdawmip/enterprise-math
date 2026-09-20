"""Certified A2 display-cell observer from exact integer polar sources.

No native-X6 interpretation is implied. Integers describe enclosing intervals,
NOT guessed values recovered from pixels. Every division/root evaluation uses
Enterprise Math's existing BRC facade. A finite precision budget can return
UNRESOLVED_BOUNDARY; this is never converted into an arbitrary cell.
"""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

MODULUS = 65536
TIE_RULE = 'HALF_TOWARD_POSITIVE_INFINITY_THEN_MAX_ERROR_Q_R_S'


def _phase_bits(modulus: int) -> int:
    """Validate an exact power-of-two phase carrier through uint32."""
    _positive(modulus, 'phase modulus')
    if modulus < 4 or modulus > (1 << 32) or modulus & (modulus - 1):
        raise ValueError('phase modulus must be a power of two in 4..2**32')
    return modulus.bit_length() - 1


def _integer(value: int, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f'{name} must be an exact integer')
    return value


def _positive(value: int, name: str) -> int:
    _integer(value, name)
    if value <= 0:
        raise ValueError(f'{name} must be positive')
    return value


def _brc():
    # Lazy: importing the standalone visualization toolkit needs no EM install.
    try:
        from enterprise_math import exact_arithmetic
    except ModuleNotFoundError as exc:
        if exc.name in ('enterprise_math', 'enterprise_math.exact_arithmetic'):
            raise RuntimeError('Certified cells require Enterprise Math BRC. No approximate fallback.') from exc
        raise
    return exact_arithmetic


def _quotient_remainder(n: int, d: int) -> tuple[int, int]:
    """Signed floor convention lifted from the nonnegative BRC trace."""
    brc = _brc()
    t = brc.brc_evaluate_division(brc.DivisionExpr(abs(n), d))
    if n >= 0:
        return t.quotient, t.remainder
    if t.remainder:
        return -t.quotient - 1, d - t.remainder
    return -t.quotient, 0


def _floor(n: int, d: int) -> int:
    return _quotient_remainder(n, d)[0]


def _ceil(n: int, d: int) -> int:
    return -_floor(-n, d)


def _root_index(n: int) -> int:
    brc = _brc()
    return brc.brc_evaluate_root(brc.RootExpr(n, 2)).root_index


@dataclass(frozen=True)
class DyadicInterval:
    """Closed interval [lo / 2**bits, hi / 2**bits]."""
    lo: int
    hi: int
    bits: int

    def __post_init__(self):
        _integer(self.lo, 'lower endpoint')
        _integer(self.hi, 'upper endpoint')
        _integer(self.bits, 'bits')
        if not 8 <= self.bits <= 512 or self.lo > self.hi:
            raise ValueError('ordered endpoints and bits in 8..512 required')

    @property
    def scale(self) -> int:
        return 1 << self.bits

    def _same(self, other):
        if not isinstance(other, DyadicInterval) or self.bits != other.bits:
            raise ValueError('interval scales must match')

    def __add__(self, other):
        self._same(other)
        return DyadicInterval(self.lo + other.lo, self.hi + other.hi, self.bits)

    def __neg__(self):
        return DyadicInterval(-self.hi, -self.lo, self.bits)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        self._same(other)
        products = (self.lo * other.lo, self.lo * other.hi,
                    self.hi * other.lo, self.hi * other.hi)
        return DyadicInterval(_floor(min(products), self.scale),
                              _ceil(max(products), self.scale), self.bits)

    def times_ratio(self, n: int, d: int):
        _integer(n, 'scale numerator')
        _positive(d, 'scale denominator')
        low, high = sorted((self.lo * n, self.hi * n))
        return DyadicInterval(_floor(low, d), _ceil(high, d), self.bits)

    def sqrt_nonnegative(self):
        if self.lo < 0:
            raise ValueError('square-root interval must be nonnegative')
        lo = _root_index(self.lo * self.scale)
        hi = _root_index(self.hi * self.scale)
        if hi * hi < self.hi * self.scale:
            hi += 1
        return DyadicInterval(lo, hi, self.bits)

    def intersect(self, lo: int, hi: int):
        # Callers may intersect only with separately established mathematical bounds.
        return DyadicInterval(max(lo, self.lo), min(hi, self.hi), self.bits)

    def as_record(self):
        return {'lower_numerator': str(self.lo), 'upper_numerator': str(self.hi),
                'denominator': str(self.scale), 'bits': str(self.bits)}


def root_ratio_bound(n: int, d: int, bits: int) -> tuple[DyadicInterval, dict]:
    """Enclose sqrt(n/d), retaining n*S*S = d*k*k + R, not a root tail."""
    _integer(n, 'radicand numerator')
    _positive(d, 'radicand denominator')
    if n < 0:
        raise ValueError('radicand must be nonnegative')
    DyadicInterval(0, 0, bits)
    scale = 1 << bits
    k = _root_index(_floor(n * scale * scale, d))
    residual = n * scale * scale - d * k * k
    if not 0 <= residual < d * (2 * k + 1):
        raise AssertionError('root-ratio certificate failed')
    result = DyadicInterval(k, k + (1 if residual else 0), bits)
    certificate = {'kind': 'ROOT_RATIO_POLYNOMIAL_RESIDUAL',
                   'radicand_numerator': str(n), 'radicand_denominator': str(d),
                   'scale': str(scale), 'root_index': str(k),
                   'polynomial_residual': str(residual)}
    return result, certificate


@lru_cache(maxsize=64, typed=True)
def _rotation_powers(bits: int, phase_bits: int = 16):
    """Positive binary half-angle roots down to one phase tick, reversed.

    Starting at cos(pi/2)=0, sin(pi/2)=1 avoids approximating pi entirely.
    For a 2**k carrier this constructs k-2 roots, ending at pi/2**(k-1).
    The scale is fixed; each operation rounds OUTWARD, not to nearest.
    """
    _integer(phase_bits, 'phase bits')
    if not 2 <= phase_bits <= 32:
        raise ValueError('phase bits must be in 2..32')
    scale = 1 << bits
    one = DyadicInterval(scale, scale, bits)
    cosine = DyadicInterval(0, 0, bits)
    result = []
    for _ in range(phase_bits - 2):
        next_cos = (one + cosine).times_ratio(1, 2).sqrt_nonnegative()
        next_sin = (one - cosine).intersect(0, 2 * scale).times_ratio(1, 2).sqrt_nonnegative()
        cosine = next_cos.intersect(0, scale)
        result.append((cosine, next_sin.intersect(0, scale)))
    return tuple(reversed(result))


@lru_cache(maxsize=16384, typed=True)
def phase_bounds(tick: int, bits: int = 64, phase_modulus: int = MODULUS) -> tuple[DyadicInterval, DyadicInterval]:
    """cos/sin enclosures for an integer tick on an exact 2**k carrier."""
    _integer(tick, 'phase tick')
    DyadicInterval(0, 0, bits)
    phase_bits = _phase_bits(phase_modulus)
    if not 0 <= tick < phase_modulus:
        raise ValueError(f'phase tick must be in 0..{phase_modulus - 1}')
    quadrant_size = _floor(phase_modulus, 4)
    quadrant, rest = _quotient_remainder(tick, quadrant_size)
    scale = 1 << bits
    cosine = DyadicInterval(scale, scale, bits)
    sine = DyadicInterval(0, 0, bits)
    for index, (c, s) in enumerate(_rotation_powers(bits, phase_bits) if rest else ()):
        if rest & (1 << index):
            cosine, sine = cosine * c - sine * s, sine * c + cosine * s
    cosine, sine = cosine.intersect(0, scale), sine.intersect(0, scale)
    return ((cosine, sine), (-sine, cosine), (-cosine, -sine), (sine, -cosine))[quadrant]


def round_axial(q_n: int, r_n: int, denominator: int) -> dict:
    """Exact version of existing cube-round half-up and q/r/s error tie policy."""
    _integer(q_n, 'q numerator')
    _integer(r_n, 'r numerator')
    _positive(denominator, 'denominator')
    source = (q_n, r_n, -q_n - r_n)
    rounded = [_floor(2 * n + denominator, 2 * denominator) for n in source]
    errors = [abs(a * denominator - n) for a, n in zip(rounded, source)]
    if errors[0] >= errors[1] and errors[0] >= errors[2]:
        corrected = 0
    elif errors[1] >= errors[2]:
        corrected = 1
    else:
        corrected = 2
    rounded[corrected] = -sum(rounded[i] for i in range(3) if i != corrected)
    residuals = [n - a * denominator for n, a in zip(source, rounded)]
    boundary = any(abs(residuals[i] - residuals[j]) == denominator
                   for i, j in ((0, 1), (0, 2), (1, 2)))
    if any(abs(residuals[i] - residuals[j]) > denominator
           for i, j in ((0, 1), (0, 2), (1, 2))):
        raise AssertionError('rounded point escaped nearest-cell region')
    return {'kind': 'RATIONAL_AXIAL_CELL_CERTIFICATE', 'source_numerators': [str(n) for n in source],
            'denominator': str(denominator), 'cube_cell': [str(a) for a in rounded],
            'signed_residual_numerators': [str(r) for r in residuals],
            'corrected_axis': ('q', 'r', 's')[corrected],
            'boundary': boundary, 'tie_rule': TIE_RULE}


def certify_box(q: DyadicInterval, r: DyadicInterval, s: DyadicInterval) -> dict:
    """Conditional certificate for a cube-plane point enclosed in the given box.

    q+r+s=0 is a source obligation. A box must at least intersect this plane.
    A strict pairwise Voronoi test implies the same cell for all its plane points.
    Point boxes apply the explicit legacy tie policy rather than guessing a side.
    """
    q._same(r)
    q._same(s)
    coords = (q, r, s)
    if sum(x.lo for x in coords) > 0 or sum(x.hi for x in coords) < 0:
        raise ValueError('box does not meet the cube plane')
    exact = all(x.lo == x.hi for x in coords)
    if exact:
        cert = round_axial(q.lo, r.lo, q.scale)
        return {'status': 'CERTIFIED_TIE' if cert['boundary'] else 'CERTIFIED_INTERIOR',
                'cell': cert['cube_cell'][:2], 'rounding_certificate': cert,
                'margin_numerators': None}
    proposed = round_axial(q.lo + q.hi, r.lo + r.hi, 2 * q.scale)
    cell = [int(v) for v in proposed['cube_cell']]
    margins = []
    for i, j in ((0, 1), (0, 2), (1, 2)):
        shift = (cell[i] - cell[j]) * q.scale
        low = coords[i].lo - coords[j].hi - shift
        high = coords[i].hi - coords[j].lo - shift
        margins.append(q.scale - max(abs(low), abs(high)))
    if min(margins) > 0:
        return {'status': 'CERTIFIED_INTERIOR', 'cell': [str(v) for v in cell[:2]],
                'margin_numerators': [str(v) for v in margins], 'rounding_certificate': None}
    return {'status': 'UNRESOLVED_BOUNDARY', 'cell': None,
            'margin_numerators': [str(v) for v in margins], 'rounding_certificate': None}


def _linear_root_sign(a: int, b: int, n: int, d: int) -> int:
    """Sign of a*sqrt(n/d)+b by integer comparisons; n>=0 and d>0.

    Kept private to this observer: the shared radical is a retained dependency,
    not independent interval noise. Squaring is used only after sign separation.
    """
    def sign(value):
        return (value > 0) - (value < 0)
    if not a or not n:
        return sign(b)
    if not b:
        return sign(a)
    if sign(a) == sign(b):
        return sign(a)
    return sign(a) * sign(a * a * n - b * b * d)


def _cardinal_decision(source) -> dict | None:
    """Preserve the common radical at exact quarter-turn phases.

    Coordinates have integer coefficients times one positive radical. This
    makes irrational symmetry ties decidable without losing q=s correlation.
    Other phases remain under the rigorous interval/refinement contract.
    """
    quarter = _floor(source.phase_modulus, 4)
    directions = {None: (0, 0, 0), 0: (1, 0, -1), quarter: (-1, 2, -1),
                  2 * quarter: (-1, 0, 1), 3 * quarter: (1, -2, 1)}
    if source.tick not in directions:
        return None
    coefficients = directions[source.tick]
    n = source.n * source.scale_numerator * source.scale_numerator
    d = source.scale_denominator * source.scale_denominator
    if source.tick in (quarter, 3 * quarter):
        d *= 3
    rounded = []
    for k in coefficients:
        whole = _root_index(_floor(k * k * n, d))
        half = _linear_root_sign(2 * abs(k), -(2 * whole + 1), n, d)
        # Positive and negative half cases both round toward positive infinity.
        rounded.append(whole + (1 if half >= 0 else 0) if k >= 0
                       else -whole - (1 if half > 0 else 0))
    errors = []
    for k, a in zip(coefficients, rounded):
        orientation = _linear_root_sign(-k, a, n, d)
        errors.append((-k * orientation, a * orientation))
    def compare_error(i, j):
        return _linear_root_sign(errors[i][0] - errors[j][0],
                                 errors[i][1] - errors[j][1], n, d)
    if compare_error(0, 1) >= 0 and compare_error(0, 2) >= 0:
        corrected = 0
    elif compare_error(1, 2) >= 0:
        corrected = 1
    else:
        corrected = 2
    rounded[corrected] = -sum(rounded[i] for i in range(3) if i != corrected)
    boundary = False
    for i, j in ((0, 1), (0, 2), (1, 2)):
        a, b = coefficients[i] - coefficients[j], rounded[j] - rounded[i]
        upper = _linear_root_sign(a, b - 1, n, d)
        lower = _linear_root_sign(a, b + 1, n, d)
        if upper > 0 or lower < 0:
            raise AssertionError('radical rounded point escaped nearest-cell region')
        boundary = boundary or upper == 0 or lower == 0
    certificate = {
        'kind': 'SHARED_RADICAL_AXIAL_CELL_CERTIFICATE',
        'radicand_numerator': str(n), 'radicand_denominator': str(d),
        'source_coefficients': [str(k) for k in coefficients],
        'cube_cell': [str(a) for a in rounded],
        'signed_residuals': [{'radical_coefficient': str(k), 'integer_part': str(-a)}
                             for k, a in zip(coefficients, rounded)],
        'corrected_axis': ('q', 'r', 's')[corrected],
        'boundary': boundary, 'tie_rule': TIE_RULE,
        'comparison': 'SIGN_SEPARATED_INTEGER_SQUARE_COMPARISON'}
    return {'status': 'CERTIFIED_TIE' if boundary else 'CERTIFIED_INTERIOR',
            'cell': certificate['cube_cell'][:2], 'rounding_certificate': certificate,
            'margin_numerators': None}


@dataclass(frozen=True)
class PolarSource:
    n: int
    tick: int | None
    scale_numerator: int = 1
    scale_denominator: int = 1
    phase_modulus: int = MODULUS

    def __post_init__(self):
        _integer(self.n, 'n')
        _positive(self.scale_numerator, 'scale numerator')
        _positive(self.scale_denominator, 'scale denominator')
        _phase_bits(self.phase_modulus)
        if self.n < 0:
            raise ValueError('n must be nonnegative')
        if self.n == 0:
            if self.tick is not None:
                raise ValueError('zero has no phase; use None')
        else:
            _integer(self.tick, 'phase tick')
            if not 0 <= self.tick < self.phase_modulus:
                raise ValueError(f'phase tick must be in 0..{self.phase_modulus - 1}')

    def as_record(self):
        return {'n': str(self.n), 'phase_tick': None if self.tick is None else str(self.tick),
                'phase_modulus': str(self.phase_modulus), 'scale_numerator': str(self.scale_numerator),
                'scale_denominator': str(self.scale_denominator),
                'observer': 'DECLARED_POLAR_A2_NOT_NATIVE_X6'}

    def coordinates(self, bits: int):
        radius, radius_trace = root_ratio_bound(self.n, 1, bits)
        radial_third, third_trace = root_ratio_bound(self.n, 3, bits)
        cosine, sine = phase_bounds(0 if self.tick is None else self.tick, bits, self.phase_modulus)
        a = (radius * cosine).times_ratio(self.scale_numerator, self.scale_denominator)
        b = (radial_third * sine).times_ratio(self.scale_numerator, self.scale_denominator)
        return (a - b, b.times_ratio(2, 1), -a - b), (radius_trace, third_trace)

    def locate(self, *, initial_bits: int = 64, max_bits: int = 192) -> dict:
        DyadicInterval(0, 0, initial_bits)
        DyadicInterval(0, 0, max_bits)
        if initial_bits > max_bits:
            raise ValueError('initial_bits must not exceed max_bits')
        bits = initial_bits
        history = []
        while True:
            coords, roots = self.coordinates(bits)
            decision = _cardinal_decision(self) or certify_box(*coords)
            history.append(str(bits))
            if decision['cell'] is not None or bits == max_bits:
                return {'schema': 'NOLLM_CERTIFIED_POLAR_CELL_V1', 'source': self.as_record(),
                        **decision, 'coordinate_bounds': [v.as_record() for v in coords],
                        'root_certificates': list(roots), 'refinement_bits': history,
                        'tie_rule': TIE_RULE}
            bits = min(2 * bits, max_bits)


def certified_population(phi, scale_numerator: int, scale_denominator: int,
                         *, initial_bits: int = 64, max_bits: int = 192,
                         include_certificates: bool = False, phase_modulus: int = MODULUS) -> dict:
    """Compute only certified cell counts, with explicit unresolved identities."""
    if not isinstance(include_certificates, bool):
        raise ValueError('include_certificates must be boolean')
    if not isinstance(phi, (list, tuple)) or len(phi) < 2 or phi[0] is not None:
        raise ValueError('phase population must start with the unphased zero and include one')
    _phase_bits(phase_modulus)
    sources = tuple(PolarSource(n, tick, scale_numerator, scale_denominator, phase_modulus)
                    for n, tick in enumerate(phi))
    # Complete validation before materialization or partial output.
    DyadicInterval(0, 0, initial_bits)
    DyadicInterval(0, 0, max_bits)
    if initial_bits > max_bits:
        raise ValueError('invalid precision budget')
    cells = {}
    unresolved = []
    ties = []
    certificates = []
    precision_counts = {}
    for source in sources:
        result = source.locate(initial_bits=initial_bits, max_bits=max_bits)
        precision = result['refinement_bits'][-1]
        precision_counts[precision] = precision_counts.get(precision, 0) + 1
        if result['cell'] is None:
            unresolved.append(str(source.n))
        else:
            cell = tuple(result['cell'])
            cells[cell] = cells.get(cell, 0) + 1
            if result['status'] == 'CERTIFIED_TIE':
                ties.append(str(source.n))
        if include_certificates:
            certificates.append(result)
    import hashlib
    import json
    phase_bytes = json.dumps([None if v is None else str(v) for v in phi],
                             separators=(',', ':')).encode('utf-8')
    complete = not unresolved
    occupied = len(cells)
    return {'schema': 'NOLLM_CERTIFIED_POLAR_POPULATION_V1',
            'status': 'CERTIFIED_ALL' if complete else 'UNRESOLVED_BOUNDARY',
            'population': str(len(sources)), 'certified_identities': str(len(sources) - len(unresolved)),
            'phase_modulus': str(phase_modulus),
            'phase_source_sha256': hashlib.sha256(phase_bytes).hexdigest(),
            'phase_source_encoding': 'COMPACT_UTF8_JSON_ARRAY_NULL_OR_DECIMAL_STRINGS',
            'unresolved_identities': unresolved, 'tie_identities': ties,
            'occupied_cells': str(occupied) if complete else None,
            'occupied_cells_bounds': [str(occupied), str(occupied + len(unresolved))],
            'collision_groups': str(sum(v > 1 for v in cells.values())) if complete else None,
            'excess_identities_if_collapsed': str(len(sources) - occupied) if complete else None,
            'max_cell_load': str(max(cells.values(), default=0)) if complete else None,
            'scale': {'numerator': str(scale_numerator), 'denominator': str(scale_denominator)},
            'precision_counts': {k: str(v) for k, v in precision_counts.items()},
            'tie_rule': TIE_RULE, 'certificates': certificates if include_certificates else None,
            'scope': 'CERTIFIED_A2_OBSERVER_ONLY; NO_NATIVE_IDENTITY_COLLAPSE'}


def exact_diagnostics(phi, scale_numerator: int, scale_denominator: int,
                      *, bins: int = 64, readout_scale: int | None = None,
                      initial_bits: int = 64, max_bits: int = 192,
                      include_certificates: bool = False, phase_modulus: int = MODULUS) -> dict:
    """Exact branch of the existing diagnostics API; no legacy float execution."""
    from .angular_dispersion import AngularDispersion
    _integer(bins, 'bins')
    if not 2 <= bins <= 256:
        raise ValueError('bins must be in 2..256')
    if readout_scale is not None:
        _positive(readout_scale, 'readout scale')
    _positive(scale_numerator, 'scale numerator')
    _positive(scale_denominator, 'scale denominator')
    if 2 * scale_numerator < scale_denominator or scale_numerator > 3 * scale_denominator:
        raise ValueError('declared layout scale must be in one-half..three')
    if not isinstance(phi, (list, tuple)) or not 2 <= len(phi) <= 65536:
        raise ValueError('bounded phase population must contain 2..65536 entries')
    _phase_bits(phase_modulus)
    cells = certified_population(phi, scale_numerator, scale_denominator,
                                 initial_bits=initial_bits, max_bits=max_bits,
                                 include_certificates=include_certificates,
                                 phase_modulus=phase_modulus)
    counts = [0] * bins
    for tick in phi[1:]:
        counts[_floor(tick * bins, phase_modulus)] += 1
    statistic = AngularDispersion.from_counts(counts).as_record(scale=readout_scale)
    def count_or_none(key):
        return None if cells[key] is None else int(cells[key])
    return {'population': len(phi), 'angular_population': len(phi) - 1,
            'angular_bins': bins, 'angular_counts': counts,
            'angular_cv': None, 'angular_cv_role': 'OMITTED_IN_EXACT_MODE',
            'angular_cv_squared_exact': statistic,
            'occupied_cells': count_or_none('occupied_cells'),
            'collision_groups': count_or_none('collision_groups'),
            'excess_identities_if_collapsed': count_or_none('excess_identities_if_collapsed'),
            'max_cell_load': count_or_none('max_cell_load'),
            'scale': cells['scale'], 'cell_membership_exact': cells,
            'quantizer': 'CERTIFIED_DYADIC_POLAR_A2_NOT_NATIVE_X6'}


def verify_cell_record(record: dict) -> bool:
    """Replay the exact source, bounds, rule and precision schedule; reject tampering.

    The record is not a cryptographic signature. Replay verifies this observer's
    calculation, not external origin, native identity or phase-generation claims.
    """
    import json
    def decimal(value):
        if not isinstance(value, str):
            raise ValueError('integer fields require decimal strings')
        result = int(value)
        if str(result) != value:
            raise ValueError('noncanonical integer encoding')
        return result
    try:
        if not isinstance(record, dict):
            return False
        source = record['source']
        n = decimal(source['n'])
        tick = None if source['phase_tick'] is None else decimal(source['phase_tick'])
        instance = PolarSource(n, tick, decimal(source['scale_numerator']),
                               decimal(source['scale_denominator']), decimal(source['phase_modulus']))
        schedule = record['refinement_bits']
        if not isinstance(schedule, list) or not schedule:
            return False
        actual = instance.locate(initial_bits=decimal(schedule[0]), max_bits=decimal(schedule[-1]))
        return json.dumps(actual, sort_keys=True, allow_nan=False) == json.dumps(record, sort_keys=True, allow_nan=False)
    except (KeyError, TypeError, ValueError, OverflowError):
        return False
