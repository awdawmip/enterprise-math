"""Additive reciprocal-phase observer built on the multiplication lab UI.

No existing toolkit file is rewritten. The module patches a copy of the existing
HTML template at generation time and embeds an independently generated phase table.
"""
from __future__ import annotations
import argparse, hashlib, json, math, webbrowser
from pathlib import Path
from .core import demo_hex, fingerprint, integer
from .multiplication_lab import smallest_factors

VERSION='0.1.0'
SCHEMA='NOLLM_MULTIPLICATION_LAB_V1'
MAX_COUNT=65536


def modulus(bits:int)->int:
    integer(bits,'phase_bits',24)
    if bits < 6: raise ValueError('phase_bits must be in 6..24')
    return 1 << bits


def golden_tick(rank:int,M:int)->int:
    integer(rank,'rank',MAX_COUNT)
    if rank < 1: raise ValueError('rank starts at one')
    a=rank*M
    return ((3*a-math.isqrt(5*a*a)-1)//2)%M


def tables(spf:list[int],bits:int=16)->dict[str,dict[int,int]]:
    M=modulus(bits);primes=[p for p in range(2,len(spf)) if spf[p]==p]
    golden={p:golden_tick(i,M) for i,p in enumerate(primes,1)}
    rank={p:(i*M//len(primes))%M for i,p in enumerate(primes,1)}
    inverse={p:(M//8 if p==2 else pow(p,-1,M)) for p in primes}
    return {'golden':golden,'rank':rank,'inverse':inverse}


def phase_values(spf:list[int],table:dict[int,int],M:int)->list[int|None]:
    out=[None,0]+[0]*(len(spf)-2)
    for n in range(2,len(spf)):
        p=spf[n];out[n]=(out[n//p]+table[p])%M
    return out


def payload(count:int=MAX_COUNT,phase_bits:int=16)->dict:
    M=modulus(phase_bits);spf=smallest_factors(count);data=demo_hex(count);t=tables(spf,phase_bits)
    return {'schema':SCHEMA,'lab_version':'reciprocal-'+VERSION,'modulus':M,'phase_bits':phase_bits,
            'data':data,'data_sha256':fingerprint(data),'spf':spf,**t,
            'boundary':{'typed_observer':'A2_AND_DECLARED_POLAR_COMPARISON_NOT_X6',
                        'zero_phase':None,'native_geometry_changed':False,
                        'derived_polar_pixels_are_not_source_coordinates':True,
                        'candidate':'a2=M/8; odd ap=p^-1 mod M'}}


def patched_template()->str:
    from .multiplication_ui import TEMPLATE
    text=TEMPLATE
    edits=[
      ('LAB 0.1.0','LAB reciprocal 0.1.0'),
      ('<option value="golden">按质数顺序取黄金角（整数化）</option>',
       '<option value="inverse">模逆质数相位 + 2→45°（研究候选）</option><option value="golden">按质数顺序取黄金角（整数化）</option>'),
      ("!['golden','rank','zero'].includes(s.mode)","!['golden','rank','zero','inverse'].includes(s.mode)"),
      ("table[p]=S.mode==='zero'?0:(S.mode==='golden'?P.golden[p]:P.rank[p]);",
       "table[p]=S.mode==='zero'?0:(S.mode==='golden'?P.golden[p]:S.mode==='inverse'?P.inverse[p]:P.rank[p]);"),
      ("const opts={legacy:{layout:'legacy'},golden:{},zero:{mode:'zero'},layers:{stack:true,pitch:.85}};",
       "const opts={legacy:{layout:'legacy'},inverse:{mode:'inverse'},golden:{mode:'golden'},zero:{mode:'zero'},layers:{stack:true,pitch:.85}};"),
      ("else preset(location.hash.slice(1));", "else preset(location.hash.slice(1));$('tick').max=M-1;")
    ]
    for old,new in edits:
        if text.count(old)!=1: raise RuntimeError('base multiplication UI marker changed: '+old[:50])
        text=text.replace(old,new)
    return text


def build(out:str|Path,*,count:int=MAX_COUNT,phase_bits:int=16,preset:str='inverse')->Path:
    if preset not in ('inverse','golden','rank','zero','legacy','layers'):raise ValueError('unknown preset')
    data=payload(count,phase_bits)
    encoded=json.dumps(data,ensure_ascii=False,separators=(',',':'),allow_nan=False).replace('<','\\u003c')
    text=patched_template().replace('__LAB_PAYLOAD__',encoded)
    # Hash is handled by the existing template API; URL hash chooses the observer preset.
    out=Path(out);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(text,encoding='utf-8')
    return out


def build_site(out_dir:str|Path,*,count:int=MAX_COUNT,bits=(11,16))->Path:
    out=Path(out_dir);out.mkdir(parents=True,exist_ok=True);pages=[]
    for b in bits:
        name=f'reciprocal-{b}bit.html';build(out/name,count=count,phase_bits=b);pages.append((b,name))
    links=''.join(f'<a href="{name}#inverse" target="view">{b} bit / {1<<b:,} directions</a>' for b,name in pages)
    first=pages[0][1]
    html=f'''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Reciprocal phase laboratory</title><style>body{{margin:0;background:#101b28;color:#eef5fb;font:14px system-ui}}header{{padding:14px 20px}}nav{{padding:0 20px 12px;display:flex;gap:8px;flex-wrap:wrap}}a{{color:#5ce0bf;border:1px solid #345;padding:7px 10px;text-decoration:none;border-radius:5px}}iframe{{width:100%;height:calc(100vh - 105px);border:0;background:white}}</style><header><b>Reciprocal phase resolution comparison</b><div>same integer identities; only phase resolution changes</div></header><nav>{links}</nav><iframe name="view" src="{first}#inverse"></iframe></html>'''
    (out/'index.html').write_text(html,encoding='utf-8')
    manifest={'schema':'NOLLM_RECIPROCAL_PHASE_SITE_V1','version':VERSION,'records':count,
              'pages':[{'phase_bits':b,'modulus':1<<b,'href':name} for b,name in pages],
              'data_sha256':fingerprint(demo_hex(count))}
    (out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    return out/'index.html'


def main()->int:
    p=argparse.ArgumentParser(description='Reciprocal-prime phase resolution observer')
    g=p.add_mutually_exclusive_group(required=True);g.add_argument('--out',type=Path);g.add_argument('--site',type=Path)
    p.add_argument('--count',type=int,default=MAX_COUNT);p.add_argument('--phase-bits',type=int,default=16);p.add_argument('--preview',action='store_true')
    a=p.parse_args()
    try:
        page=build_site(a.site,count=a.count) if a.site else build(a.out,count=a.count,phase_bits=a.phase_bits)
        print(page)
        if a.preview:
            from .web import preview_server
            with preview_server(a.site if a.site else page) as server:
                print(server.url,flush=True);webbrowser.open(server.url)
                try:
                    import time
                    while True:time.sleep(.5)
                except KeyboardInterrupt:pass
        return 0
    except (ValueError,OSError,RuntimeError) as exc:p.exit(2,f'error: {exc}\n')

if __name__=='__main__':raise SystemExit(main())
