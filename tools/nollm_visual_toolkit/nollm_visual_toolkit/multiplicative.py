"""Multiplicative-field lab: exact integer phases, approximate display observers.

An additive extension to Visual Toolkit 0.3.0. No runtime/native geometry changes.
Run: python -m nollm_visual_toolkit.multiplicative --out multiplication.html
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

LAB_VERSION = '0.1.0'
PHASE_MODULUS = 65536
GOLDEN_STEP = 25033  # nearest integer to 65536*(3-sqrt(5))/2; declared finite schedule
MAX_COUNT = 65536
CONFIG_SCHEMA = 'NOLLM_MULTIPLICATIVE_CONFIG_V1'
REPORT_SCHEMA = 'NOLLM_MULTIPLICATIVE_REPORT_V1'


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


def build_field(settings: dict | None = None) -> dict:
    cfg = checked_config(settings) if settings is not None else config()
    count, scheme, scale = cfg['count'], cfg['scheme'], cfg['scale']
    spf, primes = sieve(count)
    prime_phase = {p: cfg['overrides'].get(str(p), mixed_phase(p) if scheme == 'mixed' else ((i+1)*GOLDEN_STEP) % PHASE_MODULUS)
                   for i, p in enumerate(primes)}
    phase, omega = [0]*count, [0]*count
    rows = [{'id': '0', 'n': 0, 'phase': None, 'omega': None, 'prime': False,
             'ideal': [0.0, 0.0], 'coord': [0, 0]}]
    for n in range(1, count):
        if n > 1:
            p = spf[n]
            omega[n] = omega[n//p]+1
            if scheme in ('valuation', 'mixed'): phase[n] = (phase[n//p]+prime_phase[p]) % PHASE_MODULUS
            elif scheme == 'spiral': phase[n] = n*GOLDEN_STEP % PHASE_MODULUS
        if n == 1 and scheme == 'spiral': phase[n] = GOLDEN_STEP
        theta = math.tau*phase[n]/PHASE_MODULUS
        radius = scale*math.sqrt(n)
        x, y = radius*math.cos(theta), radius*math.sin(theta)
        rows.append({'id': str(n), 'n': n, 'phase': phase[n], 'omega': omega[n],
                     'prime': n > 1 and spf[n] == n, 'ideal': [x, y],
                     'coord': list(lattice_point(x, y))})
    return {'config': cfg, 'spf': spf, 'prime_phase': prime_phase, 'records': rows}


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
        q, s = r['coord']; return complex(q+s/2, math.sqrt(3)*s/2)
    return {'a': a, 'b': b, 'product': n, 'in_range': True,
            'phase_defect': (rn['phase']-ra['phase']-rb['phase']) % PHASE_MODULUS if n else None,
            'omega_defect': rn['omega']-ra['omega']-rb['omega'] if n else None,
            'ideal_relative_error': abs(za*zb/scale-zn)/(scale*math.sqrt(n)) if n else 0,
            'rounded_relative_error': abs(hx(ra)*hx(rb)/scale-hx(rn))/(scale*math.sqrt(n)) if n else 0,
            'zero_phase': 'undefined; multiplication by zero is handled separately' if not n else None}


def statistics(field: dict, rings: int = 8, sectors: int = 32) -> dict:
    rows = field['records']; count = len(rows); positive = count-1
    grid = [[0]*sectors for _ in range(rings)]; cells = {}
    for row in rows:
        cells.setdefault(tuple(row['coord']), []).append(row['id'])
        if row['n']:
            band = (row['n']-1)*rings//positive
            sector = row['phase']*sectors//PHASE_MODULUS
            grid[band][sector] += 1
    def cv(values):
        total = sum(values)
        return math.sqrt(max(0, len(values)*sum(v*v for v in values)/total**2-1))
    angular = [sum(b[j] for b in grid) for j in range(sectors)]
    return {'population': count, 'positive_population': positive, 'prime_count':len(field['prime_phase']),
            'rings': rings, 'sectors': sectors, 'grid': grid,
            'distinct_phases':len({r['phase'] for r in rows[1:]}), 'angular_cv': cv(angular), 'area_sector_cv': cv([v for b in grid for v in b]),
            'iid_cv_scale': math.sqrt((rings*sectors-1)/positive),
            'iid_boundary': 'reference sqrt(E(CV^2)); not significance or a randomness test',
            'occupied_hex_centers':len(cells), 'collision_groups':sum(len(ids)>1 for ids in cells.values()),
            'extra_identities_at_shared_centers': count-len(cells), 'largest_fiber':max(map(len,cells.values())),
            'max_display_quantization_error': max(math.hypot(r['ideal'][0]-r['coord'][0]-r['coord'][1]/2,
                                     r['ideal'][1]-math.sqrt(3)*r['coord'][1]/2) for r in rows)}


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
    """V2 adapter: all IDs retained even where observer centers coincide."""
    return {'schema':'NOLLM_VISUAL_DATA_V2', 'kind':'hex',
            'title':'Multiplicative field / rounded hex observer',
            'metadata':{'typing':'A2_ROUNDED_OBSERVER_NOT_NATIVE_X6', 'config':field['config'],
                        'phase_modulus':PHASE_MODULUS, 'lab_version':LAB_VERSION,
                        'layer_semantics':'Omega(n), with zero on display layer 0; NOT Nollm physical layer',
                        'rounding':'floating nearest hex center; raw n and phase retained; no identity quotient'},
            'records':[{'id':r['id'],'n':r['n'],'coord':r['coord'],'layer':r['omega'] or 0,
                        'fields':{'phase':r['phase'],'omega':r['omega'],'prime':r['prime'],
                                  'ideal_x':r['ideal'][0],'ideal_y':r['ideal'][1]}} for r in field['records']],
            'relations':[]}


def render(path: str | Path, settings: dict | None = None) -> Path:
    cfg = checked_config(settings) if settings is not None else config()
    template = Path(__file__).with_name('multiplicative_lab.html').read_text(encoding='utf-8')
    payload = json.dumps({'config':cfg}, ensure_ascii=False, separators=(',',':')).replace('<','\\u003c')
    if template.count('__LAB_SEED__') != 1: raise ValueError('template seed marker mismatch')
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(template.replace('__LAB_SEED__', payload), encoding='utf-8')
    return path


def main() -> int:
    p = argparse.ArgumentParser(description='Multiplicative Field Lab 0.1.0 / Toolkit 0.3.0 extension')
    p.add_argument('--count', type=int, default=MAX_COUNT)
    p.add_argument('--scheme', choices=['valuation','mixed','spiral','radial'], default='valuation')
    p.add_argument('--scale', type=float, default=1)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--report', type=Path); p.add_argument('--hex-data',type=Path)
    p.add_argument('--preview',action='store_true'); p.add_argument('--no-open',action='store_true')
    a = p.parse_args()
    try:
        cfg = config(a.count,a.scheme,a.scale); print(render(a.out,cfg))
        if a.report or a.hex_data:
            field = build_field(cfg)
            if a.report:
                report = {'schema':REPORT_SCHEMA,'lab_version':LAB_VERSION,'config':cfg,
                          'statistics':statistics(field),'all_pairs':all_pair_audit(field)}
                a.report.parent.mkdir(parents=True,exist_ok=True)
                a.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
            if a.hex_data:
                from .core import write_data
                write_data(hex_data(field),a.hex_data)
        if a.preview:
            from .web import serve_preview
            serve_preview(a.out,open_browser=not a.no_open)
        return 0
    except (ValueError,OSError,TypeError) as exc: p.exit(2,f'error: {exc}\n')

if __name__ == '__main__':
    raise SystemExit(main())
