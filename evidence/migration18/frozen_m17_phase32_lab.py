"""Integer phase carrier and optional offline multiplicative-field observer.

An additive experiment module for Nollm Visual Toolkit >= 0.3.0.  No native
coordinates or Nollm runtime are redefined. Geometry is explicitly a readout.
"""
from __future__ import annotations
import argparse
import hashlib
import html
import json
import math
from pathlib import Path

VERSION = "0.1.0"
SCHEMA = "NOLLM_PHASE32_LAB_V1"
DEN = 1 << 32
GOLDEN = 2654435761  # declared finite phase schedule, not an irrational identity
DEFAULT = dict(count=65536, mode="golden", seed=0, overrides={}, pitch=1.0,
               view="plane", field="phase", sectors=64, rings=8,
               yaw=0.0, tilt=0.65, zoom=1.0, a=5, b=7)


def validate_config(config: dict) -> dict:
    if not isinstance(config, dict) or set(config) - set(DEFAULT):
        raise ValueError("Unknown configuration field")
    c = dict(DEFAULT, **config)
    def integer(k, lo, hi):
        v = c[k]
        if isinstance(v, bool) or not isinstance(v, int) or not lo <= v <= hi:
            raise ValueError(f"{k} must be an integer in {lo}..{hi}")
    integer("count", 2, 65536); integer("seed", 0, DEN-1)
    integer("sectors", 6, 128); integer("rings", 1, 32)
    integer("a", 0, c['count']-1); integer("b", 0, c['count']-1)
    for k, lo, hi in [("pitch", .25, 8), ("yaw", -100, 100), ("tilt", 0, 1.55), ("zoom", .1, 20)]:
        if isinstance(c[k], bool) or not isinstance(c[k], (int, float)) or not math.isfinite(c[k]) or not lo <= c[k] <= hi:
            raise ValueError(f"Invalid {k}")
    if c['mode'] not in ('golden', 'hash', 'spiral') or c['view'] not in ('plane', 'hex', 'layers') or c['field'] not in ('phase', 'prime', 'mod3', 'omega'):
        raise ValueError("Invalid model/view/field")
    if not isinstance(c['overrides'], dict) or len(c['overrides']) > 128:
        raise ValueError("At most 128 prime overrides")
    for p, v in c['overrides'].items():
        if not isinstance(p, str) or not p.isascii() or not p.isdecimal() or str(int(p)) != p or not 2 <= int(p) < c['count'] or any(int(p)%d == 0 for d in range(2, math.isqrt(int(p))+1)):
            raise ValueError("Overrides require canonical prime keys within the population")
        if isinstance(v, bool) or not isinstance(v, int) or not 0 <= v < DEN:
            raise ValueError("Override phase must be uint32")
    c['overrides'] = dict(c['overrides'])
    return c


def phase_hash(p: int, seed: int) -> int:
    x = (p ^ seed) & (DEN-1)
    x = ((x ^ (x >> 16)) * 0x7FEB352D) & (DEN-1)
    x = ((x ^ (x >> 15)) * 0x846CA68B) & (DEN-1)
    return (x ^ (x >> 16)) & (DEN-1)


def _cell_pitch(value: tuple[int, int]) -> tuple[int, int]:
    """Explicit unreduced A2 pitch source; never inferred from config.pitch."""
    if not isinstance(value, tuple) or len(value) != 2:
        raise ValueError('cell_pitch must be an explicit (integer numerator, integer denominator) tuple')
    numerator, denominator = value
    if any(isinstance(v, bool) or not isinstance(v, int) or v <= 0 for v in value):
        raise ValueError('cell_pitch numerator and denominator must be positive exact integers')
    return numerator, denominator


def _lexicographic_cells(phase: list[int], pitch_n: int, pitch_d: int,
                         *, initial_bits: int, max_bits: int) -> dict:
    """Certified uint32 A2 cells, adapting only true ties to this caller's rule."""
    from .certified_hex import certified_population
    from .multiplicative import _lexicographic_tie_cell
    base = certified_population([None, *phase[1:]], pitch_d, pitch_n,
                                initial_bits=initial_bits, max_bits=max_bits,
                                include_certificates=True, phase_modulus=DEN)
    cells = {}; unresolved = []; ties = []; certificates = []
    for identity, proof in enumerate(base['certificates']):
        cell = _lexicographic_tie_cell(proof) if proof['status'] == 'CERTIFIED_TIE' else proof['cell']
        wrapped = {'schema':'NOLLM_PHASE32_CELL_CERTIFICATE_V1',
                   'status':proof['status'], 'cell':cell,
                   'tie_rule':'MINIMUM_EUCLIDEAN_DISTANCE_THEN_AXIAL_LEXICOGRAPHIC',
                   'base_certifier_tie_rule':proof.get('tie_rule'),
                   'base_certificate':proof}
        certificates.append(wrapped)
        if identity == 0:
            continue
        if cell is None:
            unresolved.append(str(identity)); continue
        key = tuple(cell); cells[key] = cells.get(key, 0) + 1
        if proof['status'] == 'CERTIFIED_TIE': ties.append(str(identity))
    complete = not unresolved; occupied = len(cells); positive = len(phase) - 1
    return {'schema':'NOLLM_PHASE32_CERTIFIED_A2_POPULATION_V1',
            'status':'CERTIFIED_ALL' if complete else 'UNRESOLVED_BOUNDARY',
            'population':str(len(phase)), 'positive_population':str(positive),
            'certified_positive_identities':str(positive-len(unresolved)),
            'phase_modulus':str(DEN), 'phase_source_sha256':base['phase_source_sha256'],
            'phase_source_encoding':base['phase_source_encoding'],
            'unresolved_identities':unresolved, 'tie_identities':ties,
            'occupied_cells':str(occupied) if complete else None,
            'occupied_cells_bounds':[str(occupied),str(occupied+len(unresolved))],
            'collision_excess':str(positive-occupied) if complete else None,
            'max_cell_multiplicity':str(max(cells.values(), default=0)) if complete else None,
            'pitch':{'numerator':str(pitch_n),'denominator':str(pitch_d),'unreduced':True},
            'certifier_scale':base['scale'], 'precision_counts':base['precision_counts'],
            'tie_rule':'MINIMUM_EUCLIDEAN_DISTANCE_THEN_AXIAL_LEXICOGRAPHIC',
            'base_certifier_tie_rule':base['tie_rule'], 'certificates':certificates,
            'scope':'CERTIFIED_A2_OBSERVER_ONLY; POSITIVE_METRICS_EXCLUDE_ZERO; NO_NATIVE_IDENTITY_COLLAPSE'}


def build(config: dict | None = None, *, cell_pitch: tuple[int, int] | None = None,
          cell_bits: int = 64, cell_max_bits: int = 192) -> dict:
    c = validate_config(config or {})
    N = c['count']; spf = [0]*N; phase = [0]*N; omega = [0]*N; primes=[]
    for p in range(2, N):
        if spf[p] == 0:
            primes.append(p)
            for k in range(p, N, p):
                if not spf[k]: spf[k] = p
    schedules = {p: ((i+1)*GOLDEN + c['seed']) % DEN if c['mode'] == 'golden' else phase_hash(p,c['seed']) for i,p in enumerate(primes)}
    schedules.update({int(k):v for k,v in c['overrides'].items()})
    for n in range(2,N):
        p=spf[n]; omega[n]=omega[n//p]+1
        phase[n]=(phase[n//p]+schedules[p])%DEN
    if c['mode']=='spiral':
        for n in range(1,N): phase[n]=((n-1)*GOLDEN)%DEN
    # 0 has no prime-valuation/angle interpretation; it is an external absorbing point.
    result = dict(config=c, phase=phase, spf=spf, omega=omega, primes=primes)
    if cell_pitch is None:
        if (cell_bits, cell_max_bits) != (64, 192):
            raise ValueError('cell precision budgets require explicit cell_pitch')
        return result
    pitch_n, pitch_d = _cell_pitch(cell_pitch)
    exact = _lexicographic_cells(phase, pitch_n, pitch_d,
                                 initial_bits=cell_bits, max_bits=cell_max_bits)
    result.update(cell_engine='CERTIFIED_INTEGER_RESIDUAL',
                  cell_pitch_source={'numerator':str(pitch_n),'denominator':str(pitch_d),'unreduced':True},
                  cell_precision={'initial_bits':cell_bits,'max_bits':cell_max_bits},
                  cell_membership_exact=exact)
    return result


def factors(model: dict, n: int) -> list[list[int]] | None:
    if isinstance(n,bool) or not isinstance(n,int) or not 0<=n<model['config']['count']:
        raise ValueError('Input outside population')
    if n == 0: return None
    result=[]
    while n>1:
        p=model['spf'][n]; e=0
        while n%p==0: n//=p; e+=1
        result.append([p,e])
    return result


def position(model: dict, n: int) -> complex:
    factors(model,n)
    if n==0:return 0j
    a=math.tau*model['phase'][n]/DEN
    return math.sqrt(n)*complex(math.cos(a),math.sin(a))


def quantize(z: complex, pitch: float=1) -> tuple[int,int]:
    q=z.real/pitch-z.imag/(math.sqrt(3)*pitch); r=2*z.imag/(math.sqrt(3)*pitch)
    # Explicit nearest-point search; lexicographic tie-break, no cell-ID merging.
    a=math.floor(q); b=math.floor(r)
    return min(((i,j) for i in range(a-1,a+3) for j in range(b-1,b+3)),
               key=lambda t: ((q-t[0])**2+(q-t[0])*(r-t[1])+(r-t[1])**2,t[0],t[1]))


def metrics(model: dict, *, readout_scale: int | None = 10**6) -> dict:
    c=model['config']; N=c['count']; S=c['sectors']; R=c['rings']
    exact = model.get('cell_engine') == 'CERTIFIED_INTEGER_RESIDUAL'
    if not exact and readout_scale != 10**6:
        raise ValueError('readout_scale is available only for certified Phase32 metrics')
    angular=[0]*S; bins=[0]*(S*R); rings=[0]*R
    if exact:
        from .angular_dispersion import AngularDispersion
        from .certified_hex import _floor
        for n in range(1,N):
            sector=_floor(model['phase'][n]*S,DEN)
            ring=min(R-1,_floor(n*R,N-1))
            angular[sector]+=1; rings[ring]+=1; bins[ring*S+sector]+=1
        pop=model['cell_membership_exact']
        def value(key):
            return None if pop[key] is None else int(pop[key])
        return dict(positive_population=N-1, angular_cv=None, equal_area_cv=None,
                    approximate_metrics_role='OMITTED_FROM_EXACT_OBSERVER',
                    angular_cv_squared_exact=AngularDispersion.from_counts(angular).as_record(scale=readout_scale),
                    equal_area_cv_squared_exact=AngularDispersion.from_counts(bins).as_record(scale=readout_scale),
                    angular_counts=angular, annular_counts=rings, equal_area_counts=bins,
                    empty_equal_area_bins=bins.count(0), occupied_cells=value('occupied_cells'),
                    occupied_cells_bounds=[int(x) for x in pop['occupied_cells_bounds']],
                    collision_excess=value('collision_excess'), max_cell_multiplicity=value('max_cell_multiplicity'),
                    unresolved_cell_identities=pop['unresolved_identities'][:],
                    empty_bins_not_missing_ids=True)
    cells={}
    for n in range(1,N):
        sector=model['phase'][n]*S//DEN
        ring=min(R-1,n*R//(N-1))  # radius^2 / max-radius^2: actual equal-area annuli
        angular[sector]+=1; rings[ring]+=1; bins[ring*S+sector]+=1
        qr=quantize(position(model,n),c['pitch']);cells[qr]=cells.get(qr,0)+1
    def cv(v):
        mu=sum(v)/len(v)
        return math.sqrt(sum((x-mu)**2 for x in v)/len(v))/mu
    return dict(positive_population=N-1, angular_cv=cv(angular), equal_area_cv=cv(bins),
                angular_counts=angular, annular_counts=rings, equal_area_counts=bins,
                empty_equal_area_bins=bins.count(0), occupied_cells=len(cells),
                collision_excess=(N-1)-len(cells), max_cell_multiplicity=max(cells.values()),
                empty_bins_not_missing_ids=True)


def multiplication(model: dict, a: int, b: int) -> dict:
    factors(model,a); factors(model,b); product=a*b
    if product>=model['config']['count']:
        return dict(a=a,b=b,product=product,in_domain=False)
    delta=(model['phase'][product]-model['phase'][a]-model['phase'][b])%DEN if product else None
    if model.get('cell_engine') == 'CERTIFIED_INTEGER_RESIDUAL':
        return dict(a=a,b=b,product=product,in_domain=True,phase_defect_uint32=delta,
                    omega_defect=(model['omega'][product]-model['omega'][a]-model['omega'][b]) if product else None,
                    continuous_relative_error=None,rounded_relative_error=None,
                    approximate_metrics_role='OMITTED_FROM_EXACT_OBSERVER',
                    zero_rule='absorbing; valuation/phase undefined' if product==0 else None)
    z=position(model,a)*position(model,b); target=position(model,product)
    coords=[quantize(position(model,n),model['config']['pitch']) for n in (a,b,product)]
    def cell(c):return model['config']['pitch']*complex(c[0]+c[1]/2,math.sqrt(3)*c[1]/2)
    rounded=cell(coords[0])*cell(coords[1]); norm=math.sqrt(product) if product else 1
    return dict(a=a,b=b,product=product,in_domain=True,phase_defect_uint32=delta,
        continuous_relative_error=abs(z-target)/norm,
        rounded_relative_error=abs(rounded-cell(coords[2]))/norm,
        zero_rule='absorbing; valuation/phase undefined' if product==0 else None)


def render(path: str | Path, config: dict | None = None) -> Path:
    c=validate_config(config or {})
    template=Path(__file__).with_name('phase32_lab.html').read_text(encoding='utf-8')
    payload=json.dumps(c,ensure_ascii=False,sort_keys=True,separators=(',',':')).replace('<','\\u003c')
    out=Path(path);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(template.replace('__CONFIG__',payload),encoding='utf-8')
    return out



def build_site(out_dir: str | Path, count: int = 65536) -> Path:
    """Three self-contained experiment pages; no V2 data-type coercion."""
    root=Path(out_dir);root.mkdir(parents=True,exist_ok=True)
    pages=[]
    for mode,label in [('hash','质数散列 · 乘法模型'),('golden','质数序号 · 乘法模型'),('spiral','逐数黄金角 · 非乘法对照')]:
        c=validate_config(dict(count=count,mode=mode,a=min(5,count-1),b=min(7,count-1)))
        name=mode+'.html';render(root/name,c)
        pages.append(dict(label=label,href=name,config=c,sha256=hashlib.sha256((root/name).read_bytes()).hexdigest()))
    manifest=dict(schema='NOLLM_PHASE32_SITE_V1',experiment_version=VERSION,pages=pages)
    (root/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    links=''.join('<a target="lab" href="'+p['href']+'">'+html.escape(p['label'])+'</a>' for p in pages)
    landing='<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>乘法记忆场对照站</title><style>body{margin:0;background:#101923;color:#edf3f7;font:14px system-ui}header{padding:15px}h1{font-size:20px;margin:0 0 12px}a{display:inline-block;color:#80dab7;border:1px solid #314253;border-radius:6px;margin:4px;padding:9px;text-decoration:none}iframe{display:block;width:100%;height:calc(100vh - 115px);min-height:600px;border:0}p{font-size:12px;color:#a9bac9}</style><header><h1>乘法记忆场 / 三种方案，同一总体</h1>'+links+'<p>离线观察页；点击切换，不合并身份。页面分别含完整整数总体。</p></header><iframe name="lab" title="乘法场实验页面" src="hash.html"></iframe></html>'
    (root/'index.html').write_text(landing,encoding='utf-8')
    return root/'index.html'


def hex_data(model: dict) -> dict:
    """V2 bridge; certified mode never guesses unresolved cells or pixel fields."""
    exact = model.get('cell_engine') == 'CERTIFIED_INTEGER_RESIDUAL'
    rows=[]
    if exact:
        pop=model['cell_membership_exact']
        if pop['unresolved_identities']:
            raise ValueError('unresolved certified Phase32 cells cannot be exported as complete V2 coordinates')
        for n,cert in enumerate(pop['certificates']):
            q,r=map(int,cert['cell'])
            rows.append(dict(id=str(n),n=n,coord=[q,r],layer=model['omega'][n],fields=dict(
                phase_numerator=model['phase'][n] if n else None,phase_denominator=DEN,
                omega=model['omega'][n] if n else None,prime=model['spf'][n]==n if n>1 else False,
                factors=factors(model,n))))
        config=model['config']
        source_config={'count':config['count'],'mode':config['mode'],'seed':config['seed'],
                       'overrides':dict(config['overrides']),'phase_modulus':str(DEN)}
        return dict(schema='NOLLM_VISUAL_DATA_V2',kind='hex',title='Phase32 / certified hex observer',
            metadata=dict(typing='A2_CERTIFIED_INTEGER_RESIDUAL_OBSERVER_NOT_NATIVE_X6',phase_source=source_config,
                layer_semantics='Omega(n) observer layer; zero displayed on layer 0; NOT Nollm physical layer',
                cell_engine=model['cell_engine'],cell_pitch_source=model['cell_pitch_source'],
                cell_precision=dict(model['cell_precision']),
                cell_membership_exact={k:v for k,v in pop.items() if k!='certificates'},
                identity='n retained despite center collisions',pixel_fields='ABSENT_IN_EXACT_MODE',
                legacy_display_config='OMITTED_FROM_EXACT_EXPORT'),records=rows,relations=[])
    for n in range(model['config']['count']):
        z=position(model,n);q,r=quantize(z,model['config']['pitch'])
        rows.append(dict(id=str(n),n=n,coord=[q,r],layer=model['omega'][n],fields=dict(
            phase_numerator=model['phase'][n] if n else None,phase_denominator=DEN,
            omega=model['omega'][n] if n else None,prime=model['spf'][n]==n if n>1 else False,
            factors=factors(model,n),ideal_x=z.real,ideal_y=z.imag)))
    return dict(schema='NOLLM_VISUAL_DATA_V2',kind='hex',title='Phase32 / rounded hex observer',
        metadata=dict(typing='A2_FLOATING_OBSERVER_NOT_NATIVE_X6',config=model['config'],
            layer_semantics='Omega(n) observer layer; zero displayed on layer 0; NOT Nollm physical layer',
            pitch=model['config']['pitch'],identity='n retained despite center collisions'),records=rows,relations=[])


def main() -> int:
    p=argparse.ArgumentParser(description='Nollm multiplicative-field experiment; additive toolkit module')
    p.add_argument('--out',type=Path,default=Path('multiplicative-field.html'))
    p.add_argument('--count',type=int,default=65536);p.add_argument('--mode',choices=['golden','hash','spiral'],default='golden')
    p.add_argument('--config',type=Path);p.add_argument('--preview',action='store_true');p.add_argument('--site',action='store_true',help='out becomes the three-page site directory')
    p.add_argument('--report',type=Path);p.add_argument('--hex-data',type=Path)
    a=p.parse_args()
    try:
        c=json.loads(a.config.read_text(encoding='utf-8')) if a.config else dict(count=a.count,mode=a.mode,a=min(5,a.count-1),b=min(7,a.count-1))
        if isinstance(c,dict) and c.get('schema')==SCHEMA:
            if c.get('version')!=VERSION:raise ValueError('configuration version mismatch')
            c=c['config']
        if a.site and (a.config or a.hex_data or a.report):raise ValueError('--site does not accept single-model config/data/report options')
        out=build_site(a.out,a.count) if a.site else render(a.out,c);print(out)
        if a.report:
            m=build(c);report=dict(schema=SCHEMA,config=m['config'],metrics=metrics(m),multiplication=multiplication(m,m['config']['a'],m['config']['b']))
            a.report.parent.mkdir(parents=True,exist_ok=True);a.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
        if a.hex_data:
            a.hex_data.parent.mkdir(parents=True,exist_ok=True)
            a.hex_data.write_text(json.dumps(hex_data(build(c)),ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
        if a.preview:
            from .web import serve_preview
            serve_preview(a.out if a.site else out)  # Reuses 0.3.0 loopback preview, not a new web server.
        return 0
    except (OSError,ValueError,TypeError,KeyError) as e:p.exit(2,f'error: {e}\n')

if __name__=='__main__':raise SystemExit(main())
