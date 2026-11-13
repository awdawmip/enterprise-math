#!/usr/bin/env python3
"""PREFIX-626 native X6-BRC four-probe tagged-history recovery.
Frozen original science: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Python stdlib Fraction only, original 48 STAR phases, 96 ports, 576
source-labelled BRC actions. Rebuilds input and checks full original evolution.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):
    return tuple(-k if c>0 else k for k in STARS[a] if k!=abs(c))
P=tuple((a,p,s*k) for a in range(4) for k in STARS[a]
        for s in (-1,1) for p in near(a,s*k))
IX={p:i for i,p in enumerate(P)}
def neighbors(i):
    a,p,c=P[i]
    b=next(j for j in range(4) if j!=a and abs(c) in STARS[j])
    return tuple(IX[x] for x in ([(a,c,k) for k in near(a,c) if k!=p]
                                 + [(b,c,k) for k in near(b,c)]))
N=tuple(neighbors(i) for i in range(48))
G=IX[(0,1,-3)]
AXIS=tuple(abs(c)-1 for a,p,c in P)
WEIGHTS=(1,1,1,1,0,0)
ACTIONS=[]
for i in range(48):
    for j in N[i]:
        for u,v in product((0,1),repeat=2):
            gated=(j==G and u==v==1)
            w=0 if gated else WEIGHTS[AXIS[i]]
            ACTIONS.append((2*i+u,2*j+v,w,gated,(i,j,u,v)))
assert len(P)==48 and len(ACTIONS)==576 and G==4
assert {(dest,src) for dest,src,w,g,lab in ACTIONS if g}=={(7,9),(29,9),(31,9)}
BY_ARC={}
for d,s,w,g,l in ACTIONS:
    BY_ARC.setdefault((s,d),[]).append((w,g,l))
def edge_weight(src,dst,z):
    candidates=BY_ARC.get((src,dst),[])
    assert len(candidates)==1,(src,dst,candidates)
    w,g,lab=candidates[0]
    return F(z) if g else F(w)
def embed_d(lam):
    r=[F(0)]*96
    for i in (4,11,14,32):
        r[2*i]=F(lam)
        if i==G:r[2*i+1]=F(lam)
    return r
def step(r,z):
    out=[F(0)]*96
    for d,s,w,g,lab in ACTIONS:
        if g:out[d]+=F(z)*r[s]
        elif w:out[d]+=w*r[s]
    return out
def phase(r):
    return [r[2*i] if i==G else r[2*i]+r[2*i+1] for i in range(48)]

PREFIX={0:(9,),1:(22,9),2:(64,52,9),3:(28,80,52,9)}
CYCLE_PRE=(9,28,80,52,9)
CYCLE_POST=(29,80,52,8,29)
assert all(edge_weight(a,b,0)==1 for p in PREFIX.values() for a,b in zip(p,p[1:]))
assert all(edge_weight(a,b,0)==1 for cyc in (CYCLE_PRE,CYCLE_POST) for a,b in zip(cyc,cyc[1:]))
assert edge_weight(9,29,1)==1 and edge_weight(9,29,0)==0

HC=((2,3,15),(5,28,29),(27,38,39),(16,17,41))
HB=({3:1,14:1,15:1},{17:2,40:2,41:2},
    {26:4,27:4,39:4},{4:4,5:8,29:8})
PURE=(2,28,38,16)
BASE={0:F(1),1:F(1),2:F(1),3:F(1,2)}
J0={0:2,1:1,2:0,3:3}
def phase_and_port_coarse(r,n):
    assert n>=2
    t=n-2
    v=phase(r)
    lam=v[PURE[(t+2)%4]]/(4*2**t)
    assert lam>0
    w=(v[14],v[40]/2,v[26]/4,v[4]/4)
    c=[F(0)]*4
    c[(t+2)%4]+=4*2**t*lam
    c[(t+3)%4]+=4*2**t*lam
    rebuilt=[F(0)]*48
    for j,p in enumerate(HC):
        for i in p:rebuilt[i]+=c[j]
    for j,rows in enumerate(HB):
        for i,b in rows.items():rebuilt[i]+=F(b)*w[j]
    assert rebuilt==v
    products={}
    for residue in range(4):
        wraps=sum(k%4==residue for k in range(3,n+1))
        j=(J0[residue]+t)%4
        products[residue]=w[j]/(lam*BASE[residue]*4**wraps)
    ell=v[3]+v[14]+v[15]-2*v[2]
    delta=r[29]-r[28]
    assert ell>0 and ell-3*delta>0
    last=(ell+9*delta)/(ell-3*delta)
    assert last>=0
    for i in range(48):
        if i==G:
            assert r[2*i]==r[2*i+1]==v[i]
        else:
            e=delta if i in (3,14,15) else 0
            assert r[2*i]==(v[i]-e)/2 and r[2*i+1]==(v[i]+e)/2
    return lam,products,last

def special_path(n,k):
    assert n>=k>=1
    m=k-1;rem=m%4
    path=list(PREFIX[rem])
    for _ in range((m-rem)//4):path.extend(CYCLE_PRE[1:])
    assert len(path)==k and path[-1]==9
    path.append(29)
    for j in range(n-k):path.append(CYCLE_POST[(j+1)%4])
    assert len(path)==n+1
    return tuple(path)

def path_mass(path,gates,lam):
    assert len(path)==len(gates)+1
    assert path[0] in (8,9,22,28,64)
    mass=F(lam)
    for a,b,z in zip(path,path[1:],gates):mass*=edge_weight(a,b,z)
    return mass

def recover(gates,lam):
    n=len(gates);assert n>=5
    r=embed_d(lam)
    for z in gates:r=step(r,z)
    l2,prod,last=phase_and_port_coarse(r,n)
    assert l2==lam and last==gates[-1]
    for rr in range(4):
        pp=F(1)
        for k in range(1,n+1):
            if k%4==rr:pp*=gates[k-1]+3
        assert prod[rr]==pp
    obs={}
    for k in range(5,n):
        p=special_path(n,k)
        mass=path_mass(p,gates,lam)
        assert mass==lam*gates[k-1]
        obs[k]=mass
    known={k:obs[k]/l2 for k in obs}
    known[n]=last
    for k in range(1,5):
        rr=k%4;den=F(1)
        for s in range(5,n+1):
            if s%4==rr:den*=known[s]+3
        known[k]=prod[rr]/den-3
    result=tuple(known[k] for k in range(1,n+1))
    assert result==tuple(gates)
    return {'n':n,'supplementary_path_coordinates':len(obs),
            'lambda':str(lam),'last_gate':str(last),
            'actual_path_masses':{str(k):str(v) for k,v in obs.items()},
            'mod4_products':{str(k):str(v) for k,v in prod.items()},
            'reconstruction_exact':True}

for n in range(1,65):
    gates=tuple(F((7*k+3)%11,(k%4)+1) for k in range(1,n+1))
    for k in range(1,n+1):
        p=special_path(n,k)
        assert path_mass(p,gates,F(7,5))==F(7,5)*gates[k-1]
        zeros=list(gates);zeros[k-1]=F(0)
        assert path_mass(p,zeros,F(7,5))==0
    ref=[28]
    for j in range(n):ref.append(CYCLE_POST[(j+1)%4] if j else 80)
    assert len(ref)==n+1
    assert path_mass(ref,gates,F(7,5))==F(7,5)

trials=[]
for n in (5,6,7,8,9,12,16,24,32):
    for seed in (0,1,2):
        gates=tuple(F((7*k+3*seed+2)%11,(k+seed)%4+1) for k in range(1,n+1))
        lam=F(2*seed+3,seed+2)
        trials.append(recover(gates,lam))
assert len(trials)==27
result={
 'schema':'PREFIX626_NATIVE_X6_SHARP_TAGGED_GATE_HISTORY_RECOVERY_V1',
 'date':'2026-11-09',
 'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
 'probe_phases':[4,11,14,32],
 'original_phases':48,'original_ports':96,'original_one_step_actions':576,
 'domain':'n>=5; lambda>0; every nonnegative real gate vector; full terminal 96 ports; specified labelled path-coordinate queries',
 'claim':'exactly n-5 supplementary labelled path-coordinate readings reconstruct all n gates and lambda; continuous dimension lower bound n-5',
 'special_gate_arc':[9,29],
 'four_fixed_prefix_paths':{str(k):list(v) for k,v in PREFIX.items()},
 'fixed_cycle_pre':list(CYCLE_PRE),'fixed_cycle_post':list(CYCLE_POST),
 'path_mass_identity':'J_n[W_(n,k)] = lambda*g_k for 1<=k<=n',
 'reference_gate_free_path_mass':'lambda for every n>=1',
 'endpoint_parameter_summary':'lambda, four mod4 products of (g_k+3), final g_n',
 'endpoint_dimension_bound':6,
 'minimal_extra_path_coordinates_for_n_ge_5':'n-5',
 'path_witness_tests_n_1_to_64':sum(range(1,65)),
 'zero_gate_witness_tests_n_1_to_64':sum(range(1,65)),
 'endpoint_recovery_tests':len(trials),
 'tested_horizons':sorted(set(x['n'] for x in trials)),
 'exact_trials':trials,
 'arithmetic':'native source-labelled BRC actions with Python Fraction; no classical propagation',
 'review':'AUTHOR_SIDE_UNREVIEWED',
 'status':'ALL_ASSERTIONS_PASS'}
path=Path(__file__).with_name('PREFIX626_native_history_recovery_results.json')
path.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'status':result['status'],'witnesses':result['path_witness_tests_n_1_to_64'],'trials':len(trials),'horizons':result['tested_horizons']},ensure_ascii=False))
