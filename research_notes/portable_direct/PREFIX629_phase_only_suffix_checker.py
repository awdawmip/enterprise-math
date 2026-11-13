#!/usr/bin/env python3
"""PREFIX-629: independently verify phase-only rolling labelled-suffix memory.
Native source semantics frozen at awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Exact Fraction arithmetic; 48 STAR phases, 96 ports and 576 typed actions.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json

STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):
    return tuple(-k if c>0 else k for k in STARS[a] if k != abs(c))
P=tuple((a,p,s*k) for a in range(4) for k in STARS[a] for s in (-1,1) for p in near(a,s*k))
IX={p:i for i,p in enumerate(P)}
def neighbors(i):
    a,p,c=P[i]; b=next(j for j in range(4) if j != a and abs(c) in STARS[j]); return tuple(IX[x] for x in ([(a,c,k) for k in near(a,c) if k!=p]+[(b,c,k) for k in near(b,c)]))
G=IX[(0,1,-3)]
WEIGHTS=(1,1,1,1,0,0)
ACTIONS=[]; BY_SRC=[[] for _ in range(96)]
for i in range(48):
    for j in neighbors(i):
        for u,v in product((0,1),repeat=2):
            gated=(j==G and u==v==1)
            w=Q(0) if gated else Q(WEIGHTS[abs(P[i][2])-1])
            a=(2*j+v,2*i+u,w,gated)
            ACTIONS.append(a)
            BY_SRC[a[0]].append(a)
assert len(P)==48 and len(ACTIONS)==576 and G==4
assert all(len(s)==6 for s in BY_SRC)

def embed(lam):
    r=[Q(0)]*96
    for i in (4,11,14,32):
        r[2*i]=lam
        if i==G:r[2*i+1]=lam
    return r

def step(r,g):
    out=[Q(0)]*96
    for s,d,w,gated in ACTIONS:
        if r[s] and (w or gated):out[d]+=r[s]*(g if gated else w)
    return out

def evolve(lam,gates):
    r=embed(lam)
    for g in gates:r=step(r,g)
    return r

def phase(r):
    return [r[2*i] if i==G else r[2*i]+r[2*i+1] for i in range(48)]

PURE=(2,28,38,16)
BASE={0:Q(1),1:Q(1),2:Q(1),3:Q(1,2)}
J0={0:2,1:1,2:0,3:3}
def phase_five(v,n):
    assert n>=5 and len(v)==48
    t=n-2
    lam=v[PURE[(t+2)%4]]/(4*2**t)
    assert lam>0
    w=(v[14],v[40]/2,v[26]/4,v[4]/4)
    prod={}
    for residue in range(4):
        wraps=sum(k%4==residue for k in range(3,n+1))
        j=(J0[residue]+t)%4
        prod[residue]=w[j]/(lam*BASE[residue]*4**wraps)
        assert prod[residue]>0
    return lam,prod

def true_products(gates):
    return {r:__import__('math').prod([g+3 for k,g in enumerate(gates,1) if k%4==r]) for r in range(4)}

def reconstruct_prefix(v,n,L,saved):
    t=n-L
    assert t>=4
    lam,prod=phase_five(v,n)
    if t==4:
        assert len(saved)==L
        known={k:g for k,g in zip(range(5,n+1),saved)}
    else:
        assert len(saved)==L+1
        known={k:g for k,g in zip(range(t,n+1),saved)}
    preprod={}
    for res in range(4):
        future=Q(1)
        for k in range(t+1,n+1):
            if k%4==res:future*=known[k]+3
        preprod[res]=prod[res]/future
    h=[Q(0)]*t
    if t>=5:h[t-1]=known[t]
    for res in range(4):
        candidates=[k for k in range(1,t+1) if k%4==res and k!=t]
        i=candidates[0] if candidates else t
        denom=Q(1)
        for k in range(1,t+1):
            if k%4==res and k!=i:denom*=h[k-1]+3
        h[i-1]=preprod[res]/denom-3
        assert h[i-1]>=0,(res,i,h[i-1],preprod[res])
    assert true_products(h)==preprod
    return evolve(lam,h),tuple(known[k] for k in range(t+1,n+1)),tuple(h),lam,prod

def suffix_paths(r_t,gates):
    """Sparse dictionary keyed by all ORIGINAL source/target port labels, no quotient."""
    paths={(i,):m for i,m in enumerate(r_t) if m}
    for gate in gates:
        nxt={}
        for path,m in paths.items():
            for s,d,w,gated in BY_SRC[path[-1]]:
                val=m*(gate if gated else w)
                if val:
                    q=path+(d,)
                    assert q not in nxt
                    nxt[q]=val
        paths=nxt
    return paths

def witness(n,L,lam,base,mods):
    alt=list(base)
    for k,v in mods.items():alt[k-1]=v
    # Preserve all four shifted products with exact early-position compensation.
    for i in range(1,5):
        res=i%4
        o=Q(1);p=Q(1)
        for k in range(1,n+1):
            if k%4==res and k!=i:
                o*=base[k-1]+3;p*=alt[k-1]+3
        alt[i-1]=(base[i-1]+3)*o/p-3
        assert alt[i-1]>0
    a=evolve(lam,base);b=evolve(lam,alt)
    assert phase(a)==phase(b)
    pa=suffix_paths(evolve(lam,base[:n-L]),base[n-L:])
    pb=suffix_paths(evolve(lam,alt[:n-L]),alt[n-L:])
    assert pa!=pb
    return {'n':n,'L':L,'base_gates':[str(x) for x in base], 'alt_gates':[str(x) for x in alt], 'phase_equal':True,'endpoint_port_equal':a==b,'suffix_differing_path_count':len(set(pa.items())^set(pb.items())),'examples':[{'path':list(k),'mass_a':str(pa.get(k,0)),'mass_b':str(pb.get(k,0))} for k in pa if pa[k]!=pb.get(k,0)][:3]}

trials=[];checks=0; coordinates=0
for n,L in ((5,1),(6,1),(7,1),(7,2),(8,2),(8,3),(9,3),(10,3),(11,4),(12,4)):
    for seed in range(4):
        lam=Q(2*seed+3,seed+2)
        g=tuple(Q((5*k+3*seed+4)%9,(k+seed)%4+1) for k in range(1,n+1))
        r=evolve(lam,g);v=phase(r)
        l2,p=phase_five(v,n)
        assert l2==lam and p==true_products(g)
        t=n-L
        saved=g[t-1:] if t>=5 else g[t:]
        rt,tail,h,_,_=reconstruct_prefix(v,n,L,saved)
        actual=evolve(lam,g[:t]);assert rt==actual
        pa=suffix_paths(actual,g[t:]);pb=suffix_paths(rt,tail)
        assert pa==pb
        coordinates+=len(pa)
        checks+=1
        trials.append({'n':n,'L':L,'t':t,'lambda':str(lam),'required_saved_scalars':len(saved),'paths':len(pa), 'all_equal':True,'synthetic_prefix':[str(x) for x in h]})

# A one-gate phase-only collision: five early gates and final gate with compensation.
examples=[]
for n,L,k,new in ((6,1,6,Q(4,3)),(5,1,5,Q(3,2)),(10,3,9,Q(4,3)),(10,3,10,Q(4,3))):
    examples.append(witness(n,L,Q(3,2),(Q(1),)*n,{k:new}))

result={
 'schema':'PREFIX629_PHASE_ONLY_NATIVE_SUFFIX_MEMORY_V1',
 'source':'awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'domain':'n>=L+4>=5; lambda>0, all g>=0; given ONLY full 48 native phase terminal vector, not ports; all original labelled L-suffix source paths; continuous real online registers',
 'theorem':'m=L for n=L+4, m=L+1 for n>=L+5',
 'source_phases':48,'source_ports':96,'actions':576,
 'exact_fraction_trial_count':checks,
 'nonzero_suffix_path_coordinate_comparisons':coordinates,
 'phase_equal_suffix_distinct_witnesses':examples,
 'trials':trials,
 'result':'ALL_ASSERTIONS_PASS',
 'review':'AUTHOR_SIDE_UNREVIEWED'
}
Path(__file__).with_name('PREFIX629_phase_only_suffix_results.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'status':result['result'],'trials':checks,'path_checks':coordinates,'witnesses':len(examples),'t4':sum(x['t']==4 for x in trials)},ensure_ascii=False))
