"""Bounded multiplication-field observer; additive extension to toolkit 0.3.0.

Exact identity, factorization and phase ticks precede floating display/quantization.
This is a declared experiment, not Nollm production geometry or native X6.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
from .core import demo_hex, canonical_bytes, fingerprint, integer

LAB_VERSION = '0.1.0'
SCHEMA = 'NOLLM_MULTIPLICATION_LAB_V1'
MODULUS = 65536
MAX_COUNT = 65536


def smallest_factors(count: int) -> list[int]:
    integer(count, 'count', MAX_COUNT)
    if count < 16:
        raise ValueError('count must be in 16..65536')
    spf = list(range(count)); spf[0] = spf[1] = 0
    for p in range(2, math.isqrt(count - 1) + 1):
        if spf[p] == p:
            for n in range(p*p, count, p):
                if spf[n] == n:
                    spf[n] = p
    return spf


def golden_tick(rank: int) -> int:
    """floor(rank*M*(3-sqrt(5))/2) mod M, using only exact integers."""
    integer(rank, 'rank', MAX_COUNT)
    if rank < 1:
        raise ValueError('rank starts at one')
    a = rank * MODULUS
    return ((3*a - math.isqrt(5*a*a) - 1) // 2) % MODULUS


def prime_phases(spf: list[int], mode: str = 'golden', overrides=None) -> dict[int, int]:
    if mode not in ('golden', 'rank', 'zero'):
        raise ValueError('Unknown phase mode')
    primes = [p for p in range(2, len(spf)) if spf[p] == p]
    table = {p: (golden_tick(i) if mode == 'golden' else (i*MODULUS//len(primes))%MODULUS if mode == 'rank' else 0)
             for i, p in enumerate(primes, 1)}
    for p, tick in (overrides or {}).items():
        integer(p, 'override prime', len(spf)-1)
        if p not in table:
            raise ValueError('Override key must be a prime within the population')
        integer(tick, 'phase tick', MODULUS-1)
        if tick < 0:
            raise ValueError('phase tick must be nonnegative')
        table[p] = tick
    return table


def phases(spf: list[int], table: dict[int, int]) -> list[int | None]:
    result = [None, 0] + [0] * (len(spf)-2)
    for n in range(2, len(spf)):
        p = spf[n]
        result[n] = (result[n//p] + table[p]) % MODULUS
    return result


def factors(n: int, spf: list[int]) -> list[list[int]] | None:
    integer(n, 'n', len(spf)-1)
    if n < 0:
        raise ValueError('n must be nonnegative')
    if n == 0:
        return None
    result = []
    while n > 1:
        p = spf[n]; power = 0
        while n % p == 0:
            n //= p; power += 1
        result.append([p, power])
    return result


def phase_audit(phi, multiplier: int) -> dict:
    integer(multiplier, 'multiplier', len(phi)-1)
    if multiplier < 2:
        raise ValueError('multiplier must be at least two')
    pairs = (len(phi)-1)//multiplier
    failures = sum(phi[multiplier*n] != (phi[multiplier]+phi[n])%MODULUS for n in range(1,pairs+1))
    return {'pairs': pairs, 'phase_failures': failures,
            'radius_sq_failures': 0, 'radius_sq_scope': 'R(n)^2=n; multiplication is exact by definition',
            'claim': 'finite check of declared multiplicative phase model, not a discovered law'}


def hex_product(a, b):
    q,r = a; u,v = b
    return q*u-r*v, q*v+r*u+r*v


def legacy_audit(rows, multiplier: int) -> dict:
    integer(multiplier, 'multiplier', len(rows)-1)
    if multiplier < 2:
        raise ValueError('multiplier must be at least two')
    pairs = (len(rows)-1)//multiplier; failures = 0; witness = None
    for n in range(1,pairs+1):
        prediction = hex_product(rows[n]['coord'], rows[multiplier]['coord'])
        actual = tuple(rows[n*multiplier]['coord'])
        if prediction != actual:
            failures += 1
            if witness is None:
                witness = {'n':n,'k':multiplier,'predicted':prediction,'actual':actual}
    return {'pairs':pairs,'coordinate_failures':failures,'first_witness':witness}


def rounded_hex(x: float, y: float) -> tuple[int, int]:
    """Float display quantizer. JS-compatible half-up and deterministic axis ties."""
    q = x-y/math.sqrt(3); r = 2*y/math.sqrt(3); s = -q-r
    a,b,c = (math.floor(v+0.5) for v in (q,r,s))
    da,db,dc = abs(a-q),abs(b-r),abs(c-s)
    if da >= db and da >= dc: a = -b-c
    elif db >= dc: b = -a-c
    return a,b


def diagnostics(phi, scale: float = 1.0, bins: int = 64) -> dict:
    if isinstance(scale,bool) or not isinstance(scale,(int,float)) or not math.isfinite(scale) or not 0.5 <= scale <= 3:
        raise ValueError('display scale must be in 0.5..3')
    integer(bins,'bins',256)
    if bins < 2: raise ValueError('at least two bins')
    counts=[0]*bins; cells={}; max_load=0
    for n,tick in enumerate(phi):
        if n:
            counts[tick*bins//MODULUS]+=1
            angle=2*math.pi*tick/MODULUS
            radius=scale*math.sqrt(n)
            cell=rounded_hex(radius*math.cos(angle),radius*math.sin(angle))
        else: cell=(0,0)
        cells[cell]=cells.get(cell,0)+1; max_load=max(max_load,cells[cell])
    mean=(len(phi)-1)/bins
    cv=math.sqrt(sum((c-mean)**2 for c in counts)/bins)/mean
    return {'population':len(phi),'angular_population':len(phi)-1,'angular_bins':bins,
            'angular_counts':counts,'angular_cv':cv,'occupied_cells':len(cells),
            'collision_groups':sum(c>1 for c in cells.values()),
            'excess_identities_if_collapsed':len(phi)-len(cells),'max_cell_load':max_load,
            'scale':scale,'quantizer':'float display observer; not a native/proven cell quantizer'}


def make_payload(count: int = MAX_COUNT) -> dict:
    spf=smallest_factors(count)
    data=demo_hex(count)
    return {'schema':SCHEMA,'lab_version':LAB_VERSION,'modulus':MODULUS,
            'data':data,'data_sha256':fingerprint(data),'spf':spf,
            'golden':prime_phases(spf),'rank':prime_phases(spf,'rank'),
            'boundary':{'typed_observer':'A2_AND_DECLARED_POLAR_COMPARISON_NOT_X6',
                        'zero_phase':None,'native_geometry_changed':False,
                        'derived_polar_pixels_are_not_source_coordinates':True}}


def build_lab(out: str | Path, *, count: int = MAX_COUNT) -> Path:
    from .multiplication_ui import TEMPLATE
    payload=make_payload(count)
    encoded=json.dumps(payload,ensure_ascii=False,separators=(',',':'),allow_nan=False).replace('<','\\u003c')
    text=TEMPLATE.replace('__LAB_PAYLOAD__',encoded)
    out=Path(out); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(text,encoding='utf-8')
    return out


def build_lab_site(out_dir: str | Path, *, count: int = MAX_COUNT) -> Path:
    """A one-page experiment gallery; four presets reuse the same complete data."""
    out=Path(out_dir); out.mkdir(parents=True,exist_ok=True)
    build_lab(out/'multiplication.html',count=count)
    page="""<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>数场研究预览 · Nollm</title><style>
*{box-sizing:border-box}body{margin:0;background:#101b28;color:#ecf3f9;font:14px/1.6 system-ui}header{padding:16px 22px;border-bottom:1px solid #31465a}h1{margin:0;font-size:21px}p{margin:3px 0;color:#a6b8c8;font-size:12px}nav{display:flex;gap:8px;padding:12px 20px;flex-wrap:wrap}a{color:#5ce0bf;padding:6px 13px;border:1px solid #31465a;border-radius:5px;text-decoration:none}iframe{display:block;width:100%;height:calc(100vh - 145px);min-height:650px;border:0}a:hover{background:#245b55}</style></head><body><header><h1>数场研究 · 四个对照预览</h1><p>同一批完整整数；切换的是观察参数，不是原数据。网页在本地执行，不上传资料。</p></header><nav>
<a href="multiplication.html#golden" target="lab">候选乘法布局</a><a href="multiplication.html#legacy" target="lab">原六角编码</a><a href="multiplication.html#zero" target="lab">全零相位反例</a><a href="multiplication.html#layers" target="lab">立体分层</a><a href="multiplication.html" target="_blank" rel="noopener">独立打开工作台</a></nav><iframe name="lab" title="数场交互工作台" ></iframe><script id="embedded" type="application/json">__EMBEDDED_LAB__</script><script>
const frame=document.querySelector('iframe');let selected='golden';const code=JSON.parse(document.getElementById('embedded').textContent);frame.addEventListener('load',()=>{if(frame.contentWindow.NumberFieldLab)frame.contentWindow.NumberFieldLab.preset(selected)});frame.srcdoc=code;for(const a of document.querySelectorAll('a[target="lab"]'))a.addEventListener('click',e=>{e.preventDefault();selected=a.getAttribute('href').split('#')[1];if(frame.contentWindow.NumberFieldLab)frame.contentWindow.NumberFieldLab.preset(selected)});
</script></body></html>"""
    embedded=json.dumps((out/'multiplication.html').read_text(encoding='utf-8'),ensure_ascii=False).replace('<','\\u003c')
    page=page.replace('__EMBEDDED_LAB__',embedded)
    (out/'index.html').write_text(page,encoding='utf-8')
    manifest={'schema':'NOLLM_MULTIPLICATION_SITE_V1','lab_version':LAB_VERSION,'records':count,
        'page':'multiplication.html','presets':['golden','legacy','zero','layers'],
        'html_sha256':hashlib.sha256((out/'multiplication.html').read_bytes()).hexdigest(),
        'data_sha256':fingerprint(demo_hex(count))}
    (out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    return out/'index.html'


def main() -> int:
    parser=argparse.ArgumentParser(description='Exact identity / phase / rendered-cell multiplication laboratory')
    output=parser.add_mutually_exclusive_group(required=True)
    output.add_argument('--out',type=Path)
    output.add_argument('--site',type=Path)
    parser.add_argument('--count',type=int,default=MAX_COUNT)
    parser.add_argument('--preview',action='store_true')
    args=parser.parse_args()
    try:
        page=build_lab_site(args.site,count=args.count) if args.site else build_lab(args.out,count=args.count)
        print(page)
        if args.preview:
            from .web import preview_server
            import webbrowser
            with preview_server(args.site if args.site else page) as server:
                print(server.url,flush=True); webbrowser.open(server.url)
                try:
                    import time
                    while True: time.sleep(0.5)
                except KeyboardInterrupt: pass
        return 0
    except (ValueError,OSError) as exc:
        parser.exit(2,f'error: {exc}\n')


if __name__ == '__main__':
    raise SystemExit(main())
