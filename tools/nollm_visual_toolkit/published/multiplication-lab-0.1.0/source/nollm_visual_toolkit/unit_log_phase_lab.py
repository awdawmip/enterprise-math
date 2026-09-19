"""Dyadic unit-log observer layered on the reciprocal-phase lab.

The arithmetic coordinate is computed directly from the odd residue modulo
2^(b+2), not by factorising the input. The browser table representation is only
an implementation adapter for the existing multiplication-lab UI.
"""
from __future__ import annotations
import argparse, json, webbrowser
from pathlib import Path
from .core import demo_hex, fingerprint, integer
from .multiplication_lab import smallest_factors
from . import reciprocal_phase_lab as reciprocal

VERSION='0.1.0'
MAX_COUNT=65536


def modulus(bits:int)->int:
    return reciprocal.modulus(bits)


def dlog_table(bits:int)->dict[int,int]:
    M=modulus(bits);Q=1<<(bits+2);out={};x=1
    for t in range(M):
        out[x]=t;x=x*5%Q
    if len(out)!=M or x!=1:raise RuntimeError('5 did not generate the expected 1 mod 4 subgroup')
    return out


def components(n:int,bits:int,table=None)->tuple[int,int,int]:
    integer(n,'n',2**53-1)
    if n<=0:raise ValueError('unit-log components require n>0')
    M=modulus(bits);Q=1<<(bits+2);tab=table or dlog_table(bits)
    v=(n&-n).bit_length()-1;u=(n>>v)%Q;eps=0 if u%4==1 else 1;a=u if eps==0 else (-u)%Q
    return v,eps,tab[a]


def direct_phase(n:int,bits:int,table=None)->int|None:
    if n==0:return None
    v,eps,t=components(n,bits,table);M=1<<bits
    return (t+eps*(M//2)+v*(M//8))%M


def prime_table(spf:list[int],bits:int)->dict[int,int]:
    tab=dlog_table(bits)
    return {p:direct_phase(p,bits,tab) for p in range(2,len(spf)) if spf[p]==p}


def phase_values_direct(count:int,bits:int)->list[int|None]:
    integer(count,'count',MAX_COUNT)
    if count<16:raise ValueError('count must be in 16..65536')
    tab=dlog_table(bits)
    return [None]+[direct_phase(n,bits,tab) for n in range(1,count)]


def payload(count:int=MAX_COUNT,phase_bits:int=11)->dict:
    data=reciprocal.payload(count,phase_bits);data['lab_version']='unit-log-'+VERSION
    data['unitlog']=prime_table(data['spf'],phase_bits)
    data['boundary']=dict(data['boundary'],candidate='n=2^v u; u=(-1)^eps 5^t mod 2^(b+2); unitlog phase=t+eps*M/2+v*M/8',
                          random_access='direct residue/unit-log path; no odd-part factorization required')
    return data


def patched_template()->str:
    text=reciprocal.patched_template()
    edits=[
      ('LAB reciprocal 0.1.0','LAB unit-log 0.1.0'),
      ('<option value="inverse">模逆质数相位 + 2→45°（研究候选）</option>',
       '<option value="unitlog">2-adic 单位对数（精确乘法坐标）</option><option value="inverse">模逆质数相位 + 2→45°（研究候选）</option>'),
      ("!['golden','rank','zero','inverse'].includes(s.mode)","!['golden','rank','zero','inverse','unitlog'].includes(s.mode)"),
      ("table[p]=S.mode==='zero'?0:(S.mode==='golden'?P.golden[p]:S.mode==='inverse'?P.inverse[p]:P.rank[p]);",
       "table[p]=S.mode==='zero'?0:(S.mode==='golden'?P.golden[p]:S.mode==='inverse'?P.inverse[p]:S.mode==='unitlog'?P.unitlog[p]:P.rank[p]);"),
      ("const opts={legacy:{layout:'legacy'},inverse:{mode:'inverse'},golden:{mode:'golden'},zero:{mode:'zero'},layers:{stack:true,pitch:.85}};",
       "const opts={legacy:{layout:'legacy'},unitlog:{mode:'unitlog'},inverse:{mode:'inverse'},golden:{mode:'golden'},zero:{mode:'zero'},layers:{stack:true,pitch:.85}};")]
    for old,new in edits:
        if text.count(old)!=1:raise RuntimeError('reciprocal UI marker changed: '+old[:55])
        text=text.replace(old,new)
    return text


def build(out:str|Path,*,count:int=MAX_COUNT,phase_bits:int=11)->Path:
    p=payload(count,phase_bits);encoded=json.dumps(p,ensure_ascii=False,separators=(',',':'),allow_nan=False).replace('<','\\u003c')
    out=Path(out);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(patched_template().replace('__LAB_PAYLOAD__',encoded),encoding='utf-8');return out


def build_site(out_dir:str|Path,*,count:int=MAX_COUNT,bits=(11,16))->Path:
    out=Path(out_dir);out.mkdir(parents=True,exist_ok=True);pages=[]
    for b in bits:
        name=f'unit-log-{b}bit.html';build(out/name,count=count,phase_bits=b);pages.append((b,name))
    links=''.join(f'<a href="{name}#unitlog" target="view">unit-log {b} bit</a><a href="{name}#inverse" target="view">reciprocal {b} bit</a>' for b,name in pages)
    first=pages[0][1]
    page=f'''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Dyadic unit-log field</title><style>body{{margin:0;background:#101b28;color:#eef5fb;font:14px system-ui}}header{{padding:14px 20px}}nav{{padding:0 20px 12px;display:flex;gap:8px;flex-wrap:wrap}}a{{color:#5ce0bf;border:1px solid #345;padding:7px 10px;text-decoration:none;border-radius:5px}}iframe{{width:100%;height:calc(100vh - 105px);border:0;background:white}}</style><header><b>Dyadic unit-log multiplicative field</b><div>same integer identities; compare exact arithmetic observers and phase resolution</div></header><nav>{links}</nav><iframe name="view" src="{first}#unitlog"></iframe></html>'''
    (out/'index.html').write_text(page,encoding='utf-8')
    manifest={'schema':'NOLLM_UNIT_LOG_PHASE_SITE_V1','version':VERSION,'records':count,'pages':[{'phase_bits':b,'modulus':1<<b,'href':name} for b,name in pages],'data_sha256':fingerprint(demo_hex(count))}
    (out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');return out/'index.html'


def main()->int:
    p=argparse.ArgumentParser(description='Dyadic unit-log multiplication observer');g=p.add_mutually_exclusive_group(required=True);g.add_argument('--out',type=Path);g.add_argument('--site',type=Path)
    p.add_argument('--count',type=int,default=MAX_COUNT);p.add_argument('--phase-bits',type=int,default=11);p.add_argument('--preview',action='store_true');a=p.parse_args()
    try:
        page=build_site(a.site,count=a.count) if a.site else build(a.out,count=a.count,phase_bits=a.phase_bits);print(page)
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
