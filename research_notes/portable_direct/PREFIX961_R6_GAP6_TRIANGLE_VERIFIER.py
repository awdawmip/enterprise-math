#!/usr/bin/env python3
"""Exact checks for p-bit adjacent odd-core named XOR endpoint m=6.
No historical pair certificate is used to generate input or outputs.
"""
import json
from collections import Counter
from pathlib import Path

PIN = 'f42f2906d77f24085c123f3ccfe9667d41caa96d'

def triangle_condition(p, a, b):
    H = 1 << (p-1)
    return ((a-H) - 3*(b-H)) >= H//2+2

def triangle_count(p):
    if p < 4: raise ValueError('p >= 4 required')
    R = 1 << (p-3)
    q = (R-3)//3
    return 0 if q < 0 else (q+1)*(R-2)-3*q*(q+1)//2

def original_named(p, k, a, b):
    x=k*a
    out=[]
    for j in range(p):
        y=x^(1<<j)
        for i in range(p):
            z=y-(1<<i)
            if z>0 and z%b==0:
                out.append((z//b,i,j))
    return out

def verify(p,full_domain=True):
    H=1<<(p-1)
    Q=range(H+1,2*H,2)
    c=Counter(); examples=[]; bad=[]
    eligible={(a,b) for b in Q for a in Q if triangle_condition(p,a,b)}
    assert len(eligible)==triangle_count(p),(p,len(eligible),triangle_count(p))
    for k in range(1,H-2,2):
        pairs=( ((a,b) for b in Q for a in Q) if full_domain else iter(sorted(eligible)))
        for a,b in pairs:
            if a==b: continue
            w1=original_named(p,k,a,b)
            if not w1: continue
            w2=original_named(p,k+2,a,b)
            if not w2: continue
            for t,i,j in w1:
                for T,I,J in w2:
                    if T-t!=6: continue
                    s=1-2*((k*a>>j)&1)
                    S=1-2*(( (k+2)*a>>J)&1)
                    cc=(1<<i)-s*(1<<j)
                    CC=(1<<I)-S*(1<<J)
                    assert CC-cc==2*a-6*b
                    assert (a,b) in eligible,(p,k,a,b)
                    assert cc >= H+9 and CC <= -8,(p,k,a,b,cc,CC)
                    assert s==-1 and max(i,j)==p-1,(p,k,a,b,i,j)
                    assert S==1 and J>I and J>=4,(p,k,a,b,I,J)
                    if cc !=2*H: assert J==p-1,(p,k,a,b,cc,CC,J)
                    if cc==2*H: assert i==j==p-1
                    c['named_endpoint6']+=1
                    c['c_top_both' if cc==2*H else 'other_c']+=1
                    c[f'core_{k}']+=1
                    if len(examples)<10:examples.append([p,k,a,b,t,T,i,j,I,J,cc,CC])
    return {'p':p,'H':H,'eligible_pair_count':len(eligible),
            'total_ordered_pair_count':(H//2)**2,
            'checked_domain':'full' if full_domain else 'triangle_only_theorem_reduction',
            'core_count':len(range(1,H-2,2)),
            'counts':dict(c), 'examples':examples}

if __name__=='__main__':
    results=[verify(p,full_domain=(p<=8)) for p in range(4,10)]
    p19={'p':19,'H':1<<18,'Q_size':1<<17,'eligible_pair_count_formula':triangle_count(19),
         'full_ordered_Q19_squared':(1<<17)**2,
         'eligible_fraction':triangle_count(19)/(1<<34)}
    assert results[0]['counts']=={} and results[1]['counts']=={}
    assert [r['counts'].get('named_endpoint6',0) for r in results[:5]]==[0,0,2,4,10]
    out={'scientific_input_pin':PIN,'model':'Auxiliary named XOR, adjacent positive odd k,k+2<H; Qp odd in (H,2H); t,T positive; off-diagonal.',
         'theorem':'If m=T-t=6, put u=b-H,v=a-H. Then v-3u>=H/2+2; s=-1, c>=H+9, max(i,j)=p-1; S=+1, J>I, J>=4, C<=-8; if c!=2H then J=p-1. No m6 for p<=5 (odd k,k+2<H).',
         'exact_triangle_count':'R=2^(p-3); q=floor((R-3)/3); max(0,(q+1)*(R-2)-3*q*(q+1)/2) for p>=4.',
         'exhaustive_results':results,'Q19_numeric_sieve':p19,
         'proof_scope':'Universal inequality, bit localization, p<=5 impossibility proved by arithmetic/case table; p<=8 brute original equation; p=9 restricted to theorem-necessary triangle.',
         'review':'AUTHOR_PROOF_PLUS_FINITE_CHECK;NOT_REVIEWED;NO_NATIVE_X6_BRC_TRANSFER'}
    dst=Path(__file__).with_name('PREFIX961_R6_EXACT_RESULTS.json')
    dst.write_text(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'p4_p9':[(r['p'],r['eligible_pair_count'],r['counts'].get('named_endpoint6',0),r['counts'].get('c_top_both',0),r['counts'].get('other_c',0)) for r in results], 'Q19':p19},ensure_ascii=False))
