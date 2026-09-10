"""Multiplicative Memory Field research observer.

Arithmetic identity is retained as the integer ``n`` and its prime valuation data.
Radius/angle are observer coordinates only; they never replace the arithmetic carrier.
"""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from typing import Iterable

from .core import MAX_POINTS, VERSION, integer

FIELD_SCHEMA = "NOLLM_MULTIPLICATIVE_FIELD_V1"
PHASE_MODULUS = 2**32
DEFAULT_SEED = 0x000C6C82


def _mix32(value: int) -> int:
    """Stable unsigned 32-bit avalanche mixer, mirrored by the browser workbench."""
    x = value & 0xFFFFFFFF
    x = (x + 0x9E3779B9) & 0xFFFFFFFF
    x ^= x >> 16
    x = (x * 0x85EBCA6B) & 0xFFFFFFFF
    x ^= x >> 13
    x = (x * 0xC2B2AE35) & 0xFFFFFFFF
    x ^= x >> 16
    return x & 0xFFFFFFFF


def prime_phase_code(prime: int, seed: int = DEFAULT_SEED) -> int:
    prime = integer(prime, "prime", MAX_POINTS)
    seed = integer(seed, "seed", 0xFFFFFFFF)
    if prime < 2:
        raise ValueError("prime must be >= 2")
    # Keep the native dyadic frame exact: the extra arithmetic phase of 2 is zero.
    return 0 if prime == 2 else _mix32(prime ^ seed)


def smallest_prime_factors(limit: int) -> list[int]:
    limit = integer(limit, "limit", MAX_POINTS)
    if limit < 1:
        raise ValueError("limit must be positive")
    spf = list(range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    for p in range(2, math.isqrt(limit) + 1):
        if spf[p] == p:
            for multiple in range(p * p, limit + 1, p):
                if spf[multiple] == multiple:
                    spf[multiple] = p
    return spf


def factorization(n: int, spf: list[int] | None = None) -> tuple[tuple[int, int], ...]:
    n = integer(n, "n", MAX_POINTS)
    if n < 1:
        raise ValueError("factorization is defined here for positive integers")
    if n == 1:
        return ()
    if spf is None:
        spf = smallest_prime_factors(n)
    if len(spf) <= n:
        raise ValueError("spf table is too short")
    out: list[tuple[int, int]] = []
    value = n
    while value > 1:
        p = spf[value]
        e = 0
        while value % p == 0:
            value //= p
            e += 1
        out.append((p, e))
    return tuple(out)


def phase_accumulator(n: int, seed: int = DEFAULT_SEED, spf: list[int] | None = None) -> int:
    """Unwrapped integer prime-phase accumulator; serial multiplication adds exactly."""
    if n < 1:
        raise ValueError("phase accumulator is defined here for positive integers")
    return sum(e * prime_phase_code(p, seed) for p, e in factorization(n, spf))


def multiplicative_config(
    *,
    count: int = 65536,
    seed: int = DEFAULT_SEED,
    radial_exponent: float = 0.5,
    frame_strength: float = 1.0,
    phase_strength: float = 1.0,
    sectors: int = 64,
    block_size: int = 1024,
) -> dict[str, object]:
    count = integer(count, "count", MAX_POINTS)
    seed = integer(seed, "seed", 0xFFFFFFFF)
    if seed < 0:
        raise ValueError("seed must be an unsigned 32-bit integer")
    sectors = integer(sectors, "sectors", 512)
    block_size = integer(block_size, "block_size", MAX_POINTS)
    if block_size > count:
        block_size = count
    if count < 2:
        raise ValueError("count must include at least 0 and 1")
    if not (0.05 <= radial_exponent <= 2.0):
        raise ValueError("radial_exponent must be in 0.05..2.0")
    if not all(math.isfinite(x) and -8.0 <= x <= 8.0 for x in (frame_strength, phase_strength)):
        raise ValueError("phase strengths must be finite and in -8..8")
    if not 4 <= sectors <= 512:
        raise ValueError("sectors must be in 4..512")
    if not 16 <= block_size <= count:
        raise ValueError("block_size must be in 16..count")
    return {
        "schema": FIELD_SCHEMA,
        "toolkit_version": VERSION,
        "population": {"first": 0, "last": count - 1, "count": count},
        "carrier": {
            "identity": "integer n; positive n retain sparse prime valuations v_p(n)",
            "zero": "special absorbing state, excluded from logarithmic/phase identities",
            "phase_code_modulus": PHASE_MODULUS,
            "prime_2_intrinsic_phase_code": 0,
        },
        "observer": {
            "radius": "r(n)=n^alpha for n>0",
            "alpha": radial_exponent,
            "angle": "theta(n)=frame_strength*(pi/4)*log2(n)+phase_strength*2*pi*A(n)/2^32",
            "frame_strength": frame_strength,
            "phase_strength": phase_strength,
            "phase_seed": seed,
            "native_frame_spokes": 16,
            "native_frame_step_degrees": 22.5,
        },
        "diagnostics": {"sectors": sectors, "block_size": block_size},
        "claim_boundary": {
            "finite_visualization_not_asymptotic_theorem": True,
            "observer_coordinates_do_not_replace_carrier": True,
            "deterministic_prime_phase_is_research_choice_not_canonical_number_theory": True,
        },
    }


def config_fingerprint(config: dict[str, object]) -> str:
    raw = json.dumps(config, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def carrier_certificate(count: int = 4096, seed: int = DEFAULT_SEED) -> dict[str, object]:
    """Finite exact certificate for the retained arithmetic phase carrier."""
    count = integer(count, "count", MAX_POINTS)
    if count < 4:
        raise ValueError("count must be >= 4")
    spf = smallest_prime_factors(count - 1)
    checked = 0
    failures = []
    # Deterministic bounded grid of products; no random sampling.
    bound = min(128, count - 1)
    for a in range(1, bound + 1):
        for b in range(1, bound + 1):
            product = a * b
            if product >= count:
                continue
            checked += 1
            lhs = phase_accumulator(product, seed, spf)
            rhs = phase_accumulator(a, seed, spf) + phase_accumulator(b, seed, spf)
            if lhs != rhs:
                failures.append([a, b, product, lhs, rhs])
                if len(failures) >= 10:
                    break
        if failures:
            break
    return {
        "schema": "NOLLM_MULTIPLICATIVE_CARRIER_CERTIFICATE_V1",
        "count": count,
        "seed": seed,
        "pairs_checked": checked,
        "phase_accumulator_failures": failures,
        "phase_accumulator_additive_on_checked_products": not failures,
        "prime_2_phase_code": prime_phase_code(2, seed),
        "status": "FINITE_EXACT_CHECK_NOT_ASYMPTOTIC_THEOREM",
    }


def _html_template(config: dict[str, object]) -> str:
    payload = json.dumps(config, ensure_ascii=False, sort_keys=True, separators=(",", ":")).replace("<", "\\u003c")
    fingerprint = config_fingerprint(config)
    return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Multiplicative Memory Field Lab · Nollm Visual Toolkit {VERSION}</title>
<style>
:root{{--ink:#172532;--muted:#5c6e7b;--line:#d5dee5;--paper:#f3f5f7;--panel:#fff;--accent:#285b7b}}*{{box-sizing:border-box}}body{{margin:0;font:14px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--ink);background:var(--paper)}}header{{padding:13px 18px;background:#172a39;color:white;display:flex;justify-content:space-between;gap:10px;align-items:center}}h1{{margin:0;font-size:18px}}header small{{opacity:.72}}main{{display:grid;grid-template-columns:290px minmax(0,1fr) 300px;height:calc(100vh - 56px);min-height:620px}}aside{{background:var(--panel);padding:13px;overflow:auto;border-right:1px solid var(--line)}}aside.right{{border-left:1px solid var(--line);border-right:0}}#stage{{position:relative;background:#fff;overflow:hidden}}canvas{{display:block;width:100%;height:100%;touch-action:none}}h2{{font-size:13px;margin:14px 0 6px}}h2:first-child{{margin-top:0}}label{{font-size:11px;color:var(--muted);display:block;margin:7px 0}}input,select,button{{font:inherit;border:1px solid var(--line);border-radius:5px;padding:6px;background:#fff;color:var(--ink)}}input[type=number],select{{width:100%}}input[type=range]{{width:100%;padding:0}}button{{cursor:pointer}}button:hover{{border-color:var(--accent);background:#eef3f7}}.row{{display:flex;gap:6px;margin:6px 0}}.row>*{{flex:1;min-width:0}}.hint{{font-size:11px;color:var(--muted)}}.metric{{font-size:20px;font-weight:650;font-variant-numeric:tabular-nums}}.card{{padding:8px 0;border-bottom:1px solid var(--line)}}pre{{white-space:pre-wrap;overflow-wrap:anywhere;font-size:10px;background:#f6f8fa;padding:8px;max-height:250px;overflow:auto}}#hud{{position:absolute;top:10px;left:10px;right:10px;display:flex;justify-content:space-between;pointer-events:none}}#hud span{{background:rgba(255,255,255,.9);padding:4px 7px;border:1px solid var(--line);border-radius:4px;font-size:11px}}#notice{{position:absolute;bottom:8px;left:10px;right:10px;background:rgba(255,255,255,.9);border:1px solid var(--line);padding:5px 8px;font-size:10px;pointer-events:none}}@media(max-width:1000px){{main{{grid-template-columns:240px 1fr}}aside.right{{display:none}}}}@media(max-width:650px){{main{{display:flex;flex-direction:column;height:auto;min-height:0}}aside{{max-height:330px;border-right:0;border-bottom:1px solid var(--line)}}#stage{{height:60vh;min-height:420px}}aside.right{{display:block;max-height:none}}header small{{display:none}}}}
</style></head><body>
<header><h1>Multiplicative Memory Field Lab <small>{VERSION}</small></h1><small>BRC: arithmetic carrier first · geometry is an observer</small></header>
<main><aside>
<h2>01 / Population</h2><label>整数数量（0..N-1）<input id="count" type="number" min="128" max="200000" value="{config['population']['count']}"></label><label>质数相位 seed（uint32）<input id="seed" type="number" min="0" max="4294967295" value="{config['observer']['phase_seed']}"></label><button id="rebuild">重建算术 carrier</button>
<h2>02 / Multiplicative observer</h2><label>径向指数 α <span id="alphaText"></span><input id="alpha" type="range" min="0.1" max="1.0" step="0.01" value="{config['observer']['alpha']}"></label><label>原生 frame 强度 <span id="frameText"></span><input id="frame" type="range" min="-2" max="2" step="0.05" value="{config['observer']['frame_strength']}"></label><label>质数相位强度 <span id="phaseText"></span><input id="phase" type="range" min="-2" max="2" step="0.05" value="{config['observer']['phase_strength']}"></label><div class="row"><button id="frameOnly">Frame only</button><button id="phaseOnly">Prime phase</button><button id="hybrid">Hybrid</button></div><label><input id="spokes" type="checkbox" checked>显示 16 条 22.5° Nollm frame 辐条</label><label>着色<select id="color"><option value="prime">素数 / 合数</option><option value="mod">n mod k</option><option value="omega">Ω(n)</option><option value="v2">v₂(n)</option><option value="phase">prime phase</option></select></label><label>模数 k<input id="modulus" type="number" min="2" max="97" value="6"></label>
<div class="row"><button id="fit">全图</button><button id="resetObserver">观察归零</button></div>
<h2>03 / Multiplication trace</h2><label>起始 n<input id="query" type="number" min="0" value="3"></label><label>乘数 m<input id="multiplier" type="number" min="1" value="5"></label><div class="row"><button id="locate">定位</button><button id="trace">显示 n,mn,m²n…</button></div>
<h2>04 / Density diagnostics</h2><label>角扇区数<input id="sectors" type="number" min="8" max="256" value="{config['diagnostics']['sectors']}"></label><label>径向 block 大小<input id="block" type="number" min="64" max="8192" value="{config['diagnostics']['block_size']}"></label><button id="measure">重新测量</button>
<div class="row"><button id="png">PNG</button><button id="config">配置 JSON</button></div>
<p class="hint">α=1/2 是二维等面积密度候选。调参改变 observer，不改整数、质因数分解或相位 carrier。</p>
</aside><section id="stage"><canvas id="canvas"></canvas><div id="hud"><span id="title"></span><span id="drawn"></span></div><div id="notice">0 是特殊吸收态；1 是乘法单位。显示坐标不是 Nollm Cell 身份。</div></section>
<aside class="right"><h2>观察指标</h2><div class="card"><div class="hint">平均角向 sector CV</div><div class="metric" id="angular">—</div></div><div class="card"><div class="hint">角向 CV / iid 占位基准</div><div class="metric" id="angularRatio">—</div></div><div class="card"><div class="hint">等面积环计数 CV</div><div class="metric" id="radial">—</div></div><div class="card"><div class="hint">当前配置</div><pre id="params"></pre></div><h2>点选 / 反查</h2><pre id="detail">点击一个点或输入 n</pre><h2>Carrier 边界</h2><pre id="contract"></pre><p class="hint">A(n)=Σ vₚ(n)h(p) 使用整数累加；A(ab)=A(a)+A(b) 是 carrier 关系。角度、半径、CV、屏幕距离均为 observer。</p><div class="hint">config sha256: <span id="sha">{fingerprint[:16]}…</span></div></aside></main>
<script id="configData" type="application/json">{payload}</script>
<script>
'use strict';
const CFG=JSON.parse(document.getElementById('configData').textContent), TAU=2*Math.PI, MOD=4294967296;
const $=id=>document.getElementById(id), cv=$('canvas'), ctx=cv.getContext('2d');
let N=CFG.population.count,seed=CFG.observer.phase_seed>>>0,alpha=CFG.observer.alpha,frameStrength=CFG.observer.frame_strength,phaseStrength=CFG.observer.phase_strength;
let spf=[],prime=[],omega=[],v2=[],acc=[],points=[],screen=[],selected=3,traceIds=[],zoom=1,pan=[0,0],observerYaw=0,drag=null,W=800,H=600;
function mix32(value){{let x=value>>>0;x=(x+0x9e3779b9)>>>0;x^=x>>>16;x=Math.imul(x,0x85ebca6b)>>>0;x^=x>>>13;x=Math.imul(x,0xc2b2ae35)>>>0;x^=x>>>16;return x>>>0}}
function phaseCode(p){{return p===2?0:mix32((p^seed)>>>0)}}
function buildCarrier(){{
 N=Math.max(128,Math.min(200000,Number($('count').value)||65536));seed=(Number($('seed').value)||0)>>>0;$('count').value=N;$('seed').value=seed;
 spf=new Int32Array(N);prime=new Uint8Array(N);omega=new Uint8Array(N);v2=new Int8Array(N);acc=new Float64Array(N);for(let i=0;i<N;i++)spf[i]=i;if(N>1)spf[1]=1;
 for(let p=2;p*p<N;p++)if(spf[p]===p)for(let m=p*p;m<N;m+=p)if(spf[m]===m)spf[m]=p;
 for(let n=2;n<N;n++)prime[n]=spf[n]===n?1:0;v2[0]=-1;for(let n=1;n<N;n++){{let x=n,o=0,a=0;while(x>1){{const p=spf[x];let e=0;while(x%p===0){{x=Math.trunc(x/p);e++}}o+=e;a+=e*phaseCode(p)}}omega[n]=o;acc[n]=a;let t=n,c=0;while((t&1)===0){{c++;t=Math.trunc(t/2)}}v2[n]=c}}
 computePoints();fit();measure();show(selected);render();
}}
function computePoints(){{alpha=Number($('alpha').value);frameStrength=Number($('frame').value);phaseStrength=Number($('phase').value);points=new Array(N);points[0]=[0,0,0,0];for(let n=1;n<N;n++){{const radius=Math.pow(n,alpha),theta=frameStrength*Math.PI/4*Math.log2(n)+phaseStrength*TAU*acc[n]/MOD;points[n]=[radius*Math.cos(theta),radius*Math.sin(theta),radius,theta]}}updateText()}}
function updateText(){{$('alphaText').textContent=alpha.toFixed(2);$('frameText').textContent=frameStrength.toFixed(2);$('phaseText').textContent=phaseStrength.toFixed(2);$('params').textContent=JSON.stringify({{N,seed,alpha,frameStrength,phaseStrength,sectors:Number($('sectors').value),block:Number($('block').value)}},null,2);$('contract').textContent=JSON.stringify(CFG.claim_boundary,null,2)}}
function resize(){{const d=devicePixelRatio||1,W0=cv.clientWidth||800,H0=cv.clientHeight||600;W=W0;H=H0;if(cv.width!==Math.floor(W0*d)||cv.height!==Math.floor(H0*d)){{cv.width=Math.floor(W0*d);cv.height=Math.floor(H0*d);ctx.setTransform(d,0,0,d,0,0)}}}}
function fit(){{let max=1;for(const p of points)max=Math.max(max,Math.abs(p[0]),Math.abs(p[1]));zoom=.46*Math.min(cv.clientWidth||800,cv.clientHeight||600)/max;pan=[0,0]}}
function worldToScreen(x,y){{const c=Math.cos(observerYaw),s=Math.sin(observerYaw),X=x*c-y*s,Y=x*s+y*c;return [W/2+pan[0]+zoom*X,H/2+pan[1]-zoom*Y]}}
function valueColor(n){{const mode=$('color').value;if(n===0)return '#a64848';if(mode==='prime')return prime[n]?'#d28a18':'#315f7a';if(mode==='mod'){{const k=Math.max(2,Number($('modulus').value)||6);return `hsl(${{(n%k)*360/k}} 58% 47%)`}}if(mode==='omega')return `hsl(${{(omega[n]*47)%360}} 62% 46%)`;if(mode==='v2')return `hsl(${{((v2[n]+1)*53)%360}} 58% 46%)`;return `hsl(${{((acc[n]%MOD)/MOD)*360}} 62% 46%)`}}
function render(){{resize();ctx.clearRect(0,0,W,H);ctx.fillStyle='#fff';ctx.fillRect(0,0,W,H);if($('spokes').checked){{ctx.save();ctx.translate(W/2+pan[0],H/2+pan[1]);ctx.rotate(observerYaw);ctx.strokeStyle='#dbe3e8';ctx.lineWidth=1;const L=Math.max(W,H);for(let i=0;i<16;i++){{const a=i*Math.PI/8;ctx.beginPath();ctx.moveTo(0,0);ctx.lineTo(L*Math.cos(a),-L*Math.sin(a));ctx.stroke()}}ctx.restore()}}
 screen=new Array(N);const base=N>80000?.8:N>20000?1.05:1.45;for(let n=0;n<N;n++){{const p=points[n],s=worldToScreen(p[0],p[1]);screen[n]=s;if(s[0]<-3||s[0]>W+3||s[1]<-3||s[1]>H+3)continue;ctx.fillStyle=valueColor(n);ctx.beginPath();ctx.arc(s[0],s[1],traceIds.includes(n)?3.4:(n===selected?3.2:base),0,TAU);ctx.fill()}}
 if(traceIds.length>1){{ctx.strokeStyle='#111';ctx.lineWidth=1.5;ctx.beginPath();traceIds.forEach((n,i)=>{{const s=screen[n];if(i)ctx.lineTo(s[0],s[1]);else ctx.moveTo(s[0],s[1])}});ctx.stroke()}}$('title').textContent=`0..${{N-1}} · α=${{alpha.toFixed(2)}} · seed=${{seed}}`;$('drawn').textContent=`${{N.toLocaleString()}} identities`}}
function factors(n){{if(n<1)return n===0?'special zero':'1';let x=n,out=[];while(x>1){{const p=spf[x];let e=0;while(x%p===0){{x=Math.trunc(x/p);e++}}out.push(e===1?`${{p}}`:`${{p}}^${{e}}`)}}return out.join(' × ')}}
function show(n){{n=Math.max(0,Math.min(N-1,Number(n)||0));selected=n;$('query').value=n;const p=points[n];$('detail').textContent=JSON.stringify({{n,factorization:factors(n),prime:!!prime[n],omega:omega[n],v2:n===0?null:v2[n],prime_phase_accumulator:n===0?null:acc[n],radius:n===0?0:p[2],angle_radians:n===0?null:p[3]}},null,2);render()}}
function doTrace(){{const m=Math.max(1,Math.trunc(Number($('multiplier').value)||1));let n=Math.max(0,Math.trunc(Number($('query').value)||0));traceIds=[];const seen=new Set();for(let i=0;i<64&&n<N&&!seen.has(n);i++){{traceIds.push(n);seen.add(n);const next=n*m;if(next===n)break;n=next}}render()}}
function cvOf(a){{if(!a.length)return 0;const mean=a.reduce((x,y)=>x+y,0)/a.length;if(!mean)return 0;const v=a.reduce((x,y)=>x+(y-mean)*(y-mean),0)/a.length;return Math.sqrt(v)/mean}}
function measure(){{const sectors=Math.max(8,Math.min(256,Math.trunc(Number($('sectors').value)||64))),block=Math.max(64,Math.min(8192,Math.trunc(Number($('block').value)||1024)));let cvs=[];for(let start=1;start<N;start+=block){{const bins=new Array(sectors).fill(0),end=Math.min(N,start+block);for(let n=start;n<end;n++){{let a=points[n][3]%TAU;if(a<0)a+=TAU;bins[Math.min(sectors-1,Math.floor(a/TAU*sectors))]++}}cvs.push(cvOf(bins))}}const meanAngular=cvs.reduce((a,b)=>a+b,0)/Math.max(1,cvs.length),iid=Math.sqrt((sectors-1)/block);$('angular').textContent=meanAngular.toFixed(4);$('angularRatio').textContent=(meanAngular/iid).toFixed(3);
 const rings=32,bins=new Array(rings).fill(0),maxR2=Math.pow(N-1,2*alpha);for(let n=1;n<N;n++){{const t=Math.pow(n,2*alpha)/maxR2;bins[Math.min(rings-1,Math.floor(t*rings))]++}}$('radial').textContent=cvOf(bins).toFixed(4);updateText()}}
function download(name,text,type){{const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([text],{{type}}));a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000)}}
for(const id of ['alpha','frame','phase'])$(id).addEventListener('input',()=>{{computePoints();measure();render()}});for(const id of ['color','modulus','spokes'])$(id).addEventListener('change',render);function preset(f,p){{$('frame').value=f;$('phase').value=p;computePoints();measure();render()}}$('frameOnly').onclick=()=>preset(1,0);$('phaseOnly').onclick=()=>preset(0,1);$('hybrid').onclick=()=>preset(1,1);$('rebuild').onclick=buildCarrier;$('fit').onclick=()=>{{fit();render()}};$('resetObserver').onclick=()=>{{observerYaw=0;pan=[0,0];fit();render()}};$('locate').onclick=()=>show($('query').value);$('trace').onclick=doTrace;$('measure').onclick=measure;$('png').onclick=()=>{{const a=document.createElement('a');a.download='multiplicative-field.png';a.href=cv.toDataURL('image/png');a.click()}};$('config').onclick=()=>download('multiplicative-field-config.json',JSON.stringify({{...CFG,runtime:{{N,seed,alpha,frameStrength,phaseStrength}}}},null,2),'application/json');
cv.addEventListener('wheel',e=>{{e.preventDefault();zoom*=Math.exp(-e.deltaY*.001);render()}},{{passive:false}});cv.addEventListener('pointerdown',e=>{{drag=[e.clientX,e.clientY,e.shiftKey]}});cv.addEventListener('pointermove',e=>{{if(!drag)return;const dx=e.clientX-drag[0],dy=e.clientY-drag[1];if(drag[2])observerYaw+=dx*.006;else{{pan[0]+=dx;pan[1]+=dy}}drag=[e.clientX,e.clientY,e.shiftKey];render()}});window.addEventListener('pointerup',()=>drag=null);cv.addEventListener('click',e=>{{if(drag)return;const box=cv.getBoundingClientRect(),mx=e.clientX-box.left,my=e.clientY-box.top;let best=-1,d=64;for(let n=0;n<N;n++){{const s=screen[n],dd=(s[0]-mx)*(s[0]-mx)+(s[1]-my)*(s[1]-my);if(dd<d){{d=dd;best=n}}}}if(best>=0)show(best)}});window.addEventListener('resize',render);
window.NollmMultiplicativeLab={{status:()=>({{N,seed,alpha,frameStrength,phaseStrength,selected,trace:traceIds.slice(),angularCV:$('angular').textContent,angularToIid:$('angularRatio').textContent,radialCV:$('radial').textContent}}),phaseCode,mix32,phaseAccumulator:n=>n>0?acc[n]:null,factors:n=>factors(n)}};
buildCarrier();
</script></body></html>'''


def multiplicative_html(
    path: str | Path,
    *,
    count: int = 65536,
    seed: int = DEFAULT_SEED,
    radial_exponent: float = 0.5,
    frame_strength: float = 1.0,
    phase_strength: float = 1.0,
    sectors: int = 64,
    block_size: int = 1024,
) -> Path:
    config = multiplicative_config(
        count=count,
        seed=seed,
        radial_exponent=radial_exponent,
        frame_strength=frame_strength,
        phase_strength=phase_strength,
        sectors=sectors,
        block_size=block_size,
    )
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(_html_template(config), encoding="utf-8")
    return path
