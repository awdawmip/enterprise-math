"""Multiplicative-field lab: exact integer phases and optional certified A2 cells.

An additive extension to Visual Toolkit 0.3.0. No runtime/native geometry changes.
Run: python -m nollm_visual_toolkit.multiplicative --out multiplication.html
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import re
import sys
from pathlib import Path
from typing import Any

LAB_VERSION = '0.1.0'
PHASE_MODULUS = 65536
GOLDEN_STEP = 25033  # nearest integer to 65536*(3-sqrt(5))/2; declared finite schedule
MAX_COUNT = 65536
CONFIG_SCHEMA = 'NOLLM_MULTIPLICATIVE_CONFIG_V1'
REPORT_SCHEMA = 'NOLLM_MULTIPLICATIVE_REPORT_V1'
EXACT_REPORT_SCHEMA = 'NOLLM_MULTIPLICATIVE_REPORT_V2'
STARTUP_SCHEMA = 'NOLLM_MULTIPLICATIVE_STARTUP_V1'
_CELL_SCALE_TEXT_RE = re.compile(r'(?:(?P<int>[1-9][0-9]*)|(?P<num>[1-9][0-9]*)/(?P<den>[1-9][0-9]*)|(?P<whole>0|[1-9][0-9]*)\.(?P<frac>[0-9]+))')


def config(count: int = MAX_COUNT, scheme: str = 'valuation', scale: float = 1,
           overrides: dict[str, int] | None = None) -> dict[str, Any]:
    """Reject coercions. Prime phases are exact residues, not floating angles."""
    if isinstance(count, bool) or not isinstance(count, int) or not 16 <= count <= MAX_COUNT:
        raise ValueError('count must be an integer in 16..65536')
    if scheme not in ('valuation', 'mixed', 'spiral', 'radial'):
        raise ValueError('unknown phase scheme')
    if isinstance(scale, bool) or not isinstance(scale, (int, float)) or not math.isfinite(scale) or not .25 <= scale <= 4:
        raise ValueError('scale must be finite and in 0.25..4')
    overrides = {} if overrides is None else overrides
    if not isinstance(overrides, dict) or len(overrides) > 100:
        raise ValueError('overrides must be an object with at most 100 prime entries')
    clean = {}
    for key, value in overrides.items():
        if not isinstance(key, str) or not key.isascii() or not key.isdigit() or str(int(key)) != key:
            raise ValueError('phase keys must be canonical positive decimal prime strings')
        p = int(key)
        if not 2 <= p < count or any(p % d == 0 for d in range(2, math.isqrt(p)+1)):
            raise ValueError('phase key must be a prime below count')
        if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value < PHASE_MODULUS:
            raise ValueError('phase residue must be an integer in 0..65535')
        clean[key] = value
    return {'schema': CONFIG_SCHEMA, 'count': count, 'scheme': scheme,
            'scale': float(scale), 'overrides': clean}


def checked_config(value: dict) -> dict:
    if not isinstance(value, dict) or value.get('schema') != CONFIG_SCHEMA:
        raise ValueError('invalid configuration schema')
    if set(value) != {'schema', 'count', 'scheme', 'scale', 'overrides'}:
        raise ValueError('unexpected or missing configuration keys')
    return config(value['count'], value['scheme'], value['scale'], value['overrides'])


def sieve(count: int) -> tuple[list[int], list[int]]:
    spf = list(range(count)); spf[0] = 0; spf[1] = 1
    for p in range(2, math.isqrt(count-1)+1):
        if spf[p] == p:
            for j in range(p*p, count, p):
                if spf[j] == j: spf[j] = p
    return spf, [p for p in range(2, count) if spf[p] == p]


def lattice_point(x: float, y: float) -> tuple[int, int]:
    """Nearest hex center in double display arithmetic, lexicographic ties.

    This is a floating observer, not an exact-arithmetic Voronoi certificate.
    """
    rf = 2*y/math.sqrt(3); qf = x-rf/2
    iq, ir = math.floor(qf), math.floor(rf)
    return min(((a, b) for a in range(iq-1, iq+3) for b in range(ir-1, ir+3)),
               key=lambda c: ((c[0]+c[1]/2-x)**2+(math.sqrt(3)*c[1]/2-y)**2, c))


def mixed_phase(p: int) -> int:
    """Fixed uint32 mixer, not randomness or a security hash."""
    h = ((p ^ 0x9e3779b9) * 0x85ebca6b) & 0xffffffff
    h ^= h >> 13
    h = (h * 0xc2b2ae35) & 0xffffffff
    h ^= h >> 16
    return h % PHASE_MODULUS


def _cell_scale(value: tuple[int, int]) -> tuple[int, int]:
    """Validate an explicit, unreduced exact cell scale; never infer from float."""
    if not isinstance(value, tuple) or len(value) != 2:
        raise ValueError('cell_scale must be an explicit (integer numerator, integer denominator) tuple')
    numerator, denominator = value
    if any(isinstance(v, bool) or not isinstance(v, int) or v <= 0 for v in value):
        raise ValueError('cell_scale numerator and denominator must be positive exact integers')
    return numerator, denominator


def _cell_precision(initial_bits: int, max_bits: int) -> tuple[int, int]:
    if any(isinstance(v, bool) or not isinstance(v, int) for v in (initial_bits, max_bits)):
        raise ValueError('cell precision budgets must be exact integers')
    if not 8 <= initial_bits <= max_bits <= 512:
        raise ValueError('cell precision requires 8 <= initial_bits <= max_bits <= 512')
    return initial_bits, max_bits


def parse_cell_scale_text(value: str) -> tuple[tuple[int, int], dict[str, object]]:
    """Parse exact CLI scale syntax without ever constructing a float.

    Decimal spelling is provenance: ``0.50`` becomes 50/100 rather than 1/2.
    Fractions and integers must be canonical positive decimal text.
    """
    if not isinstance(value, str) or not value or len(value) > 256:
        raise ValueError('cell scale text must be a nonempty string of at most 256 characters')
    match = _CELL_SCALE_TEXT_RE.fullmatch(value)
    if match is None:
        raise ValueError('cell scale must be positive exact text: integer, fraction n/d, or decimal')
    if match.group('int') is not None:
        numerator, denominator, syntax = int(match.group('int')), 1, 'INTEGER'
    elif match.group('num') is not None:
        numerator, denominator, syntax = int(match.group('num')), int(match.group('den')), 'FRACTION'
    else:
        whole, frac = match.group('whole'), match.group('frac')
        denominator = 10 ** len(frac)
        numerator = int(whole) * denominator + int(frac)
        syntax = 'DECIMAL'
    if numerator <= 0:
        raise ValueError('cell scale must be positive')
    pair = _cell_scale((numerator, denominator))
    return pair, {'text': value, 'syntax': syntax, 'numerator': str(numerator),
                  'denominator': str(denominator), 'unreduced': True}


def cell_membership_summary(field: dict) -> dict | None:
    exact = field.get('cell_membership_exact')
    if exact is None:
        return None
    return {key: exact[key] for key in (
        'schema', 'status', 'population', 'certified_identities', 'phase_modulus',
        'phase_source_sha256', 'phase_source_encoding', 'unresolved_identities',
        'tie_identities', 'occupied_cells', 'occupied_cells_bounds',
        'collision_groups', 'excess_identities_if_collapsed', 'max_cell_load',
        'scale', 'precision_counts', 'tie_rule', 'base_certifier_schema',
        'base_certifier_tie_rule', 'scope')}


LEXICOGRAPHIC_CELL_TIE_RULE = 'MINIMUM_EUCLIDEAN_DISTANCE_THEN_AXIAL_LEXICOGRAPHIC'


def _lexicographic_tie_cell(base: dict) -> list[str]:
    """Select the old module's declared tie using the base exact certificate.

    The certified kernel remains the geometric certificate. This adapter only
    changes which of several *equal nearest* A2 cells is named by this legacy
    module. No interval midpoint or floating comparison participates.
    """
    if base.get('status') != 'CERTIFIED_TIE' or base.get('cell') is None:
        return base.get('cell')
    proof = base.get('rounding_certificate') or {}
    q0, r0 = map(int, base['cell'])
    candidates = sorted({(q0+dq, r0+dr) for dq, dr in
                         ((0,0),(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1))})
    kind = proof.get('kind')
    if kind == 'RATIONAL_AXIAL_CELL_CERTIFICATE':
        qn, rn, _ = map(int, proof['source_numerators']); den = int(proof['denominator'])
        def distance(cell):
            q, r = cell; dq, dr = qn-q*den, rn-r*den
            return dq*dq+dq*dr+dr*dr
        best = min(candidates, key=lambda c:(distance(c),c))
    elif kind == 'SHARED_RADICAL_AXIAL_CELL_CERTIFICATE':
        from .certified_hex import _linear_root_sign
        n = int(proof['radicand_numerator']); d = int(proof['radicand_denominator'])
        cq, cr, _ = map(int, proof['source_coefficients'])
        def bc(cell):
            q, r = cell
            return (-2*cq*q-cq*r-cr*q-2*cr*r, q*q+q*r+r*r)
        def compare(left, right):
            bl, cl = bc(left); br, cr0 = bc(right)
            return _linear_root_sign(bl-br, cl-cr0, n, d)
        best = candidates[0]
        for candidate in candidates[1:]:
            order = compare(candidate, best)
            if order < 0 or (order == 0 and candidate < best):
                best = candidate
    else:
        raise AssertionError('unsupported exact tie certificate for lexicographic adapter')
    return [str(best[0]), str(best[1])]


def _certified_lexicographic_population(phi, numerator: int, denominator: int,
                                         *, initial_bits: int, max_bits: int) -> dict:
    """Reuse certified cells, adapting only certified ties to legacy semantics."""
    from .certified_hex import certified_population
    base = certified_population(phi, numerator, denominator,
                                initial_bits=initial_bits, max_bits=max_bits,
                                include_certificates=True)
    cells = {}; unresolved = []; ties = []; certificates = []
    for identity, proof in enumerate(base['certificates']):
        cell = _lexicographic_tie_cell(proof) if proof['status'] == 'CERTIFIED_TIE' else proof['cell']
        wrapped = {'schema':'NOLLM_MULTIPLICATIVE_CELL_CERTIFICATE_V1',
                   'status':proof['status'], 'cell':cell,
                   'tie_rule':LEXICOGRAPHIC_CELL_TIE_RULE,
                   'base_certifier_tie_rule':proof.get('tie_rule'),
                   'base_certificate':proof}
        certificates.append(wrapped)
        if cell is None:
            unresolved.append(str(identity)); continue
        key = tuple(cell); cells[key] = cells.get(key,0)+1
        if proof['status'] == 'CERTIFIED_TIE': ties.append(str(identity))
    complete = not unresolved; occupied = len(cells)
    return {'schema':'NOLLM_MULTIPLICATIVE_CERTIFIED_A2_POPULATION_V1',
            'status':'CERTIFIED_ALL' if complete else 'UNRESOLVED_BOUNDARY',
            'population':base['population'], 'certified_identities':base['certified_identities'],
            'phase_modulus':base['phase_modulus'], 'phase_source_sha256':base['phase_source_sha256'],
            'phase_source_encoding':base['phase_source_encoding'],
            'unresolved_identities':unresolved, 'tie_identities':ties,
            'occupied_cells':str(occupied) if complete else None,
            'occupied_cells_bounds':[str(occupied),str(occupied+len(unresolved))],
            'collision_groups':str(sum(v>1 for v in cells.values())) if complete else None,
            'excess_identities_if_collapsed':str(len(certificates)-occupied) if complete else None,
            'max_cell_load':str(max(cells.values(),default=0)) if complete else None,
            'scale':base['scale'], 'precision_counts':base['precision_counts'],
            'tie_rule':LEXICOGRAPHIC_CELL_TIE_RULE,
            'base_certifier_schema':base['schema'], 'base_certifier_tie_rule':base['tie_rule'],
            'certificates':certificates,
            'scope':'CERTIFIED_A2_OBSERVER_ONLY; LEGACY_AXIAL_LEXICOGRAPHIC_TIE; NO_NATIVE_IDENTITY_COLLAPSE'}


def _phase_state(cfg: dict) -> tuple[list[int], dict[int, int], list[int], list[int]]:
    count, scheme = cfg['count'], cfg['scheme']
    spf, primes = sieve(count)
    prime_phase = {p: cfg['overrides'].get(str(p), mixed_phase(p) if scheme == 'mixed' else ((i+1)*GOLDEN_STEP) % PHASE_MODULUS)
                   for i, p in enumerate(primes)}
    phase, omega = [0]*count, [0]*count
    for n in range(1, count):
        if n > 1:
            p = spf[n]
            omega[n] = omega[n//p]+1
            if scheme in ('valuation', 'mixed'):
                phase[n] = (phase[n//p]+prime_phase[p]) % PHASE_MODULUS
            elif scheme == 'spiral':
                phase[n] = n*GOLDEN_STEP % PHASE_MODULUS
        if n == 1 and scheme == 'spiral':
            phase[n] = GOLDEN_STEP
    return spf, prime_phase, phase, omega


def build_field(settings: dict | None = None, *, cell_scale: tuple[int, int] | None = None,
                cell_bits: int = 64, cell_max_bits: int = 192) -> dict:
    """Build the field; exact cells require an explicit integer-ratio source.

    ``config.scale`` remains the historical floating display scale. Passing
    ``cell_scale=(n,d)`` selects the existing certified A2 observer for cell
    membership without deriving n/d from that float. Approximate ``ideal``
    pixels remain display-only and may use a different declared scale.
    """
    cfg = checked_config(settings) if settings is not None else config()
    _cell_precision(cell_bits, cell_max_bits)
    count, scale = cfg['count'], cfg['scale']
    spf, prime_phase, phase, omega = _phase_state(cfg)
    exact = None
    certificates = None
    source = None
    if cell_scale is not None:
        numerator, denominator = _cell_scale(cell_scale)
        exact = _certified_lexicographic_population([None, *phase[1:]], numerator, denominator,
                                                    initial_bits=cell_bits, max_bits=cell_max_bits)
        certificates = exact['certificates']
        source = {'numerator': str(numerator), 'denominator': str(denominator),
                  'unreduced': True}
    rows = []
    for n in range(count):
        if n == 0:
            x = y = 0.0
            shown_phase = shown_omega = None
        else:
            theta = math.tau*phase[n]/PHASE_MODULUS
            radius = scale*math.sqrt(n)
            x, y = radius*math.cos(theta), radius*math.sin(theta)
            shown_phase, shown_omega = phase[n], omega[n]
        if certificates is None:
            coord = [0, 0] if n == 0 else list(lattice_point(x, y))
            row = {'id': str(n), 'n': n, 'phase': shown_phase, 'omega': shown_omega,
                   'prime': n > 1 and spf[n] == n, 'ideal': [x, y], 'coord': coord}
        else:
            cert = certificates[n]
            coord = None if cert['cell'] is None else [int(v) for v in cert['cell']]
            row = {'id': str(n), 'n': n, 'phase': shown_phase, 'omega': shown_omega,
                   'prime': n > 1 and spf[n] == n, 'ideal': [x, y],
                   'coord': coord, 'cell_status': cert['status']}
        rows.append(row)
    result = {'config': cfg, 'spf': spf, 'prime_phase': prime_phase, 'records': rows}
    if exact is not None:
        result.update({'cell_engine': 'CERTIFIED_INTEGER_RESIDUAL',
                       'cell_scale_source': source, 'cell_membership_exact': exact})
    return result


def factors(n: int, field: dict) -> list[list[int]]:
    if isinstance(n, bool) or not isinstance(n, int) or not 1 <= n < field['config']['count']:
        raise ValueError('factorization requires a positive in-range label')
    result = []
    while n > 1:
        p = field['spf'][n]; e = 0
        while n % p == 0: n //= p; e += 1
        result.append([p, e])
    return result


def multiplication(field: dict, a: int, b: int) -> dict:
    count = field['config']['count']
    if any(isinstance(x, bool) or not isinstance(x, int) or not 0 <= x < count for x in (a, b)):
        raise ValueError('factors must be in-range integer labels')
    n = a*b
    if n >= count: return {'a': a, 'b': b, 'product': n, 'in_range': False}
    ra, rb, rn = (field['records'][x] for x in (a,b,n)); scale = field['config']['scale']
    za, zb, zn = (complex(*r['ideal']) for r in (ra,rb,rn))
    def hx(r):
        if r['coord'] is None:
            return None
        q, s = r['coord']; return complex(q+s/2, math.sqrt(3)*s/2)
    result = {'a': a, 'b': b, 'product': n, 'in_range': True,
              'phase_defect': (rn['phase']-ra['phase']-rb['phase']) % PHASE_MODULUS if n else None,
              'omega_defect': rn['omega']-ra['omega']-rb['omega'] if n else None,
              'ideal_relative_error': abs(za*zb/scale-zn)/(scale*math.sqrt(n)) if n else 0,
              'zero_phase': 'undefined; multiplication by zero is handled separately' if not n else None}
    if field.get('cell_engine') == 'CERTIFIED_INTEGER_RESIDUAL':
        result.update({'rounded_relative_error': 0 if not n else None,
                       'rounded_relative_error_role': 'OMITTED_EXACT_CELL_SCALE_IS_SEPARATE_FROM_DISPLAY_SCALE'})
    else:
        result['rounded_relative_error'] = abs(hx(ra)*hx(rb)/scale-hx(rn))/(scale*math.sqrt(n)) if n else 0
    return result


def statistics(field: dict, rings: int = 8, sectors: int = 32) -> dict:
    rows = field['records']; count = len(rows); positive = count-1
    grid = [[0]*sectors for _ in range(rings)]; cells = {}; unresolved = []
    for row in rows:
        if row['coord'] is None:
            unresolved.append(row['id'])
        else:
            cells.setdefault(tuple(row['coord']), []).append(row['id'])
        if row['n']:
            band = (row['n']-1)*rings//positive
            sector = row['phase']*sectors//PHASE_MODULUS
            grid[band][sector] += 1
    def cv(values):
        total = sum(values)
        return math.sqrt(max(0, len(values)*sum(v*v for v in values)/total**2-1))
    angular = [sum(b[j] for b in grid) for j in range(sectors)]
    area = [v for b in grid for v in b]
    legacy = field.get('cell_engine') != 'CERTIFIED_INTEGER_RESIDUAL'
    if legacy:
        return {'population': count, 'positive_population': positive, 'prime_count':len(field['prime_phase']),
                'rings': rings, 'sectors': sectors, 'grid': grid,
                'distinct_phases':len({r['phase'] for r in rows[1:]}), 'angular_cv': cv(angular), 'area_sector_cv': cv(area),
                'iid_cv_scale': math.sqrt((rings*sectors-1)/positive),
                'iid_boundary': 'reference sqrt(E(CV^2)); not significance or a randomness test',
                'occupied_hex_centers':len(cells), 'collision_groups':sum(len(ids)>1 for ids in cells.values()),
                'extra_identities_at_shared_centers': count-len(cells), 'largest_fiber':max(map(len,cells.values())),
                'max_display_quantization_error': max(math.hypot(r['ideal'][0]-r['coord'][0]-r['coord'][1]/2,
                                         r['ideal'][1]-math.sqrt(3)*r['coord'][1]/2) for r in rows)}
    from .angular_dispersion import AngularDispersion
    angular_exact = AngularDispersion.from_counts(angular).as_record()
    area_exact = AngularDispersion.from_counts(area).as_record()
    complete = not unresolved
    return {'population': count, 'positive_population': positive, 'prime_count':len(field['prime_phase']),
            'rings': rings, 'sectors': sectors, 'grid': grid,
            'distinct_phases':len({r['phase'] for r in rows[1:]}),
            'angular_cv': cv(angular), 'angular_cv_role':'LEGACY_FLOAT_DISPLAY_NOT_EXACT_EVIDENCE',
            'angular_cv_squared_exact': angular_exact,
            'area_sector_cv': cv(area), 'area_sector_cv_role':'LEGACY_FLOAT_DISPLAY_NOT_EXACT_EVIDENCE',
            'area_sector_cv_squared_exact': area_exact,
            'iid_cv_scale': math.sqrt((rings*sectors-1)/positive),
            'iid_boundary': 'reference sqrt(E(CV^2)); not significance or a randomness test',
            'occupied_hex_centers':len(cells) if complete else None,
            'occupied_hex_centers_bounds':[len(cells),len(cells)+len(unresolved)],
            'collision_groups':sum(len(ids)>1 for ids in cells.values()) if complete else None,
            'extra_identities_at_shared_centers': count-len(cells) if complete else None,
            'largest_fiber':max(map(len,cells.values()),default=0) if complete else None,
            'unresolved_cell_identities':unresolved,
            'max_display_quantization_error':None,
            'max_display_quantization_error_role':'OMITTED_EXACT_CELL_SCALE_IS_SEPARATE_FROM_DISPLAY_SCALE'}


def all_pair_audit(field: dict) -> dict:
    """All ORDERED positive pairs ab<count; integer-phase/omega audit only."""
    rows = field['records']; limit = len(rows)-1
    pairs = phase_failures = omega_failures = 0
    for a in range(1,limit+1):
        for b in range(1,limit//a+1):
            pairs += 1
            phase_failures += (rows[a*b]['phase']-rows[a]['phase']-rows[b]['phase']) % PHASE_MODULUS != 0
            omega_failures += rows[a*b]['omega'] != rows[a]['omega']+rows[b]['omega']
    return {'ordered_positive_pairs':pairs,'phase_failures':phase_failures,'omega_failures':omega_failures,
            'scope':'all a,b>=1 with a*b<count; excludes zero; not an asymptotic claim'}


def hex_data(field: dict) -> dict:
    """V2 adapter: all IDs retained; unresolved exact cells are never guessed."""
    if any(r['coord'] is None for r in field['records']):
        raise ValueError('hex_data requires resolved cells; increase exact precision rather than guessing')
    exact = field.get('cell_engine') == 'CERTIFIED_INTEGER_RESIDUAL'
    metadata = {'typing':'A2_ROUNDED_OBSERVER_NOT_NATIVE_X6', 'config':field['config'],
                'phase_modulus':PHASE_MODULUS, 'lab_version':LAB_VERSION,
                'layer_semantics':'Omega(n), with zero on display layer 0; NOT Nollm physical layer',
                'rounding':'floating nearest hex center; raw n and phase retained; no identity quotient'}
    if exact:
        metadata.update({'cell_engine':'CERTIFIED_INTEGER_RESIDUAL',
                         'cell_scale_source':field['cell_scale_source'],
                         'rounding':'certified integer-residual A2 cell; approximate ideal pixels are separate'})
    return {'schema':'NOLLM_VISUAL_DATA_V2', 'kind':'hex',
            'title':'Multiplicative field / rounded hex observer', 'metadata':metadata,
            'records':[{'id':r['id'],'n':r['n'],'coord':r['coord'],'layer':r['omega'] or 0,
                        'fields':{'phase':r['phase'],'omega':r['omega'],'prime':r['prime'],
                                  'ideal_x':r['ideal'][0],'ideal_y':r['ideal'][1]}} for r in field['records']],
            'relations':[]}


def browser_startup(settings: dict | None = None, *, cell_scale_text: str | None = None,
                    cell_bits: int = 64, cell_max_bits: int = 192) -> dict:
    """One source packet for CLI/render and browser initial cell computation.

    The browser supports [1/4, 4]. Larger mathematical domains stay available
    through machine-only output; they are never clamped or changed to floats.
    """
    cfg = checked_config(settings) if settings is not None else config()
    if cell_scale_text is None:
        if (cell_bits, cell_max_bits) != (64, 192):
            raise ValueError('browser precision budgets require an exact cell scale')
        return {'config': cfg}  # Historical seed shape is preserved.
    (numerator, denominator), _ = parse_cell_scale_text(cell_scale_text)
    _cell_precision(cell_bits, cell_max_bits)
    if 4 * numerator < denominator or numerator > 4 * denominator:
        raise ValueError('browser exact scale must be in 1/4..4; use --machine-only with --report/--hex-data for a broader source')
    return {'schema': STARTUP_SCHEMA, 'config': cfg,
            'cell_options': {'engine': 'certified', 'scale': cell_scale_text,
                             'initialBits': cell_bits, 'maxBits': cell_max_bits}}


def render(path: str | Path, settings: dict | None = None, *,
           cell_scale_text: str | None = None, cell_bits: int = 64,
           cell_max_bits: int = 192) -> Path:
    seed = browser_startup(settings, cell_scale_text=cell_scale_text,
                           cell_bits=cell_bits, cell_max_bits=cell_max_bits)
    template = Path(__file__).with_name('multiplicative_lab.html').read_text(encoding='utf-8')
    from .multiplicative_browser import prepare_template
    template = prepare_template(template)
    payload = json.dumps(seed, ensure_ascii=False, separators=(',',':'), allow_nan=False).replace('<','\\u003c')
    if template.count('__LAB_SEED__') != 1: raise ValueError('template seed marker mismatch')
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(template.replace('__LAB_SEED__', payload), encoding='utf-8')
    return path


def _distinct_output_paths(*paths: Path | None) -> None:
    """Reject output aliases before writing, not a multi-file I/O transaction."""
    resolved = [path.resolve() for path in paths if path is not None]
    if len(resolved) != len(set(resolved)):
        raise ValueError('HTML, report and hex-data must use distinct output paths')


def main() -> int:
    p = argparse.ArgumentParser(description='Multiplicative Field Lab 0.1.0 / Toolkit 0.3.0 extension')
    p.add_argument('--count', type=int, default=MAX_COUNT)
    p.add_argument('--scheme', choices=['valuation','mixed','spiral','radial'], default='valuation')
    p.add_argument('--scale', type=float, default=1, help='legacy/display scale only; never an exact cell source')
    p.add_argument('--cell-scale', help='exact scale for generated page and machine outputs: integer, n/d, or decimal such as 0.50')
    p.add_argument('--cell-bits', type=int, default=64, help='initial dyadic precision for --cell-scale')
    p.add_argument('--cell-max-bits', type=int, default=192, help='maximum dyadic precision for --cell-scale')
    p.add_argument('--out', type=Path, help='generated HTML; required unless --machine-only')
    p.add_argument('--machine-only', action='store_true', help='exact report/hex-data without HTML; permits the broader positive scale domain')
    p.add_argument('--report', type=Path); p.add_argument('--hex-data',type=Path)
    p.add_argument('--preview',action='store_true'); p.add_argument('--no-open',action='store_true')
    a = p.parse_args()
    try:
        cfg = config(a.count,a.scheme,a.scale)
        if a.machine_only:
            if a.out is not None or a.preview:
                raise ValueError('--machine-only cannot be combined with --out or --preview')
            if a.cell_scale is None or not (a.report or a.hex_data):
                raise ValueError('--machine-only requires --cell-scale and --report/--hex-data')
        elif a.out is None:
            raise ValueError('--out is required unless --machine-only is selected')
        _distinct_output_paths(a.out, a.report, a.hex_data)
        cell_pair = None; cell_source = None; startup = None
        if a.cell_scale is not None:
            if a.preview:
                raise ValueError('certified --preview awaits native-browser acceptance; generate --out without preview')
            cell_pair, cell_source = parse_cell_scale_text(a.cell_scale)
            _cell_precision(a.cell_bits, a.cell_max_bits)
            if not a.machine_only:
                startup = browser_startup(cfg, cell_scale_text=a.cell_scale,
                                          cell_bits=a.cell_bits, cell_max_bits=a.cell_max_bits)
        elif a.cell_bits != 64 or a.cell_max_bits != 192:
            raise ValueError('--cell-bits/--cell-max-bits require --cell-scale')
        field = None; prepared_hex = None
        # Semantic preflight precedes output writes. No filesystem rollback is claimed.
        if cell_pair is not None and (a.report or a.hex_data):
            field = build_field(cfg, cell_scale=cell_pair, cell_bits=a.cell_bits, cell_max_bits=a.cell_max_bits)
            field['cell_scale_source'] = cell_source
            if a.hex_data:
                prepared_hex = hex_data(field)
        if a.out is not None:
            if cell_pair is None:
                print(render(a.out,cfg))
            else:
                print(render(a.out,cfg,cell_scale_text=a.cell_scale,
                             cell_bits=a.cell_bits,cell_max_bits=a.cell_max_bits))
        if a.report or a.hex_data:
            if field is None:
                field = build_field(cfg)
            if a.report:
                report = {'schema':EXACT_REPORT_SCHEMA if cell_pair is not None else REPORT_SCHEMA,
                          'lab_version':LAB_VERSION,'config':cfg,
                          'statistics':statistics(field),'all_pairs':all_pair_audit(field)}
                if cell_pair is not None:
                    report.update({'cell_engine':field['cell_engine'],
                                   'cell_scale_source':field['cell_scale_source'],
                                   'cell_membership_exact':cell_membership_summary(field),
                                   'browser_startup':startup,
                                   'html_observer_boundary':('NOT_GENERATED_MACHINE_ONLY' if a.machine_only
                                                             else 'GENERATED_WITH_CERTIFIED_STARTUP_NOT_BROWSER_EXECUTION_RECEIPT')})
                a.report.parent.mkdir(parents=True,exist_ok=True)
                a.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
            if a.hex_data:
                from .core import write_data
                write_data(prepared_hex if prepared_hex is not None else hex_data(field),a.hex_data)
        if a.preview:
            from .web import serve_preview
            serve_preview(a.out,open_browser=not a.no_open)
        return 0
    except (ValueError,OSError,TypeError) as exc: p.exit(2,f'error: {exc}\n')

if __name__ == '__main__':
    raise SystemExit(main())
