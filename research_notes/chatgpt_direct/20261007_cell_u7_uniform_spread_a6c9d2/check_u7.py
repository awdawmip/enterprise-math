#!/usr/bin/env python3
"""Same-author U7 finite certificates. python check_u7.py
No native force / physical time / prime claim. Infinite conclusions are proved
in NOTE.md, not inferred from these samples. All propagation uses pinned BRC.
"""
from fractions import Fraction as Q
from pathlib import Path
from itertools import product
from collections import defaultdict
import json, gzip, hashlib
import uniform_spread as m
u,c,r=m.u,m.c,m.r
ROOT=Path(__file__).resolve().parent;EV=ROOT/'evidence';EV.mkdir(exist_ok=True)
checks=0

def ck(test,label):
    global checks
    checks+=1
    if not test:raise AssertionError(label)

def v(f,key):return f.get(key,r.brc.CWM_ZERO).total

def pair(a,b,comp):
    return sum((comp.mu[s]*state.total*v(b,(s,z,p)) for (s,z,p),state in a.items()),Q(0))

# Every spatial axis, port and sector, both adjoint comparison graphs.
# These paths connect two input slots in a variance estimate; not material moves.
paths=[];maxlen=0
for adj in (False,True):
    for s,p,j in product((m.A,m.D),r.PORTS,range(6)):
        path=m.reference_path(s,p,j,adj);L=len(path)-1
        ck(path[0]==(s,r.ZERO,p),'comparison start')
        ck(path[-1]==(s,r.direction(2*j),p),'comparison target')
        ck(L<=8,'universal path-length bound')
        types=[]
        for aa,bb in zip(path,path[1:]):
            types.append(m.edge_type(aa,bb,adj));ck(True,'uniform Jensen edge')
        maxlen=max(maxlen,L);paths.append({'adjoint':adj,'sector':s,'port':p,'axis':j,'path':path,'types':types})
ck(len(paths)==288,'complete template coverage')

z=r.ZERO;e=r.direction(0);q=r.direction(2)
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
inputs=[
 {(m.A,z,0):r.edge(1)},
 {(m.D,z,11):r.edge(1)},
 {(m.A,z,0):r.edge(Q(1,3)),(m.D,e,5):r.edge(Q(2,7)),(m.A,q,8):r.edge(Q(4,9)),(m.D,add(e,q),1):r.edge(Q(1,5))}
]
layouts=[(),(z,e,add(e,q),q)]
parameters=[(Q(1,4),Q(1,8)),(Q(1,5),Q(1,3)),(Q(3,4),Q(2,3))]
energy_records=[];constants=[]
for rho,eps in parameters:
    comp=m.Comparison(rho,eps)
    ck(comp.cv>0 and comp.ce>0,'strict parameter interval')
    ck(comp.h==(1-rho)/eps,'common invariant fibre ratio')
    # Default K must have BOTH unit row and column sums. Not automatic from conservation.
    for occupied in (False,True):
        cells={z} if occupied else set()
        K={p:{out:m.scaled(w,1/rho) for out,w in comp.column(z,p,cells).items()} for p in r.PORTS}
        for p in r.PORTS:
            ck(r.total(K[p].values()).total==1,'K column conservation')
            ck(r.total(K[old].get(p,r.brc.CWM_ZERO) for old in r.PORTS).total==1,'K row conservation')
            for out in r.PORTS:
                w=K[p].get(out,r.brc.CWM_ZERO)
                if out!=p^1:ck(w.total>=Q(1,15),'uniform allowed scattering share')
    # Exact translated-edge congestion, while theorem uses a deliberately coarser universal bound.
    actual=[]
    for adj in (False,True):
        loads=defaultdict(lambda:r.brc.CWM_ZERO)
        for row in paths:
            if row['adjoint']!=adj:continue
            L=len(row['path'])-1
            weight=r.serial(r.edge(comp.mu[row['sector']]),r.edge(L))
            for t in row['types']:loads[t]=r.merge(loads[t],weight)
        measured=max(w.total/(comp.cv if t[0]=='vertical' else comp.ce) for t,w in loads.items())
        ck(measured<=comp.comparison_constant,'all-translation congestion bound')
        actual.append(measured)
    constants.append({'rho':rho,'epsilon':eps,'mu':comp.mu,'cv':comp.cv,'ce':comp.ce,
                      'actual_comparison_loads':actual,'C_comparison':comp.comparison_constant,
                      'C_Nash':comp.nash_constant,'a':comp.a,'C_kernel':comp.kernel_constant})
    for f,cells,adj in product(inputs,layouts,(False,True)):
        ff=comp.apply(f,cells,adj)
        M=comp.norm(f);U=comp.norm(f,2);Un=comp.norm(ff,2)
        ck(comp.norm(ff)==M,'positive density mass preserved')
        ck(Un<=U,'weighted L2 contraction')
        exact,terms=comp.jensen_identity(f,cells,adj)
        ck(exact==U-Un,'exact positive Jensen-pair identity')
        graph=comp.graph_energy(f,adj)
        energy=comp.reference_energy(f)
        ck(graph<=exact,'uniform graph is a lower dissipation bound')
        ck(energy<=comp.comparison_constant*graph,'canonical path comparison')
        ck(U**4<=comp.nash_constant**3*M**2*energy**3,'root-free Nash check')
        ck((U-Un)**3*M**2>=comp.a**3*U**4,'root-free smoothing recursion')
        ck(max(state.total for state in ff.values())<=max(state.total for state in f.values()),'density sup contraction')
        # Positive adjoint duality for a different nontrivial probe input.
        g=inputs[2];left=pair(comp.apply(f,cells,False),g,comp)
        right=pair(f,comp.apply(g,cells,True),comp)
        ck(left==right,'weighted adjoint identity with pinned forward circuit')
        energy_records.append({'rho':rho,'epsilon':eps,'layout':cells,'adjoint':adj,'input':f,
                               'output':ff,'mass':M,'U':U,'Unext':Un,'Jensen':exact,
                               'graph':graph,'reference_energy':energy,'positive_pair_terms':terms})

# Actual positive cube averaging, a proof interface on the same six-axis chart.
comp=m.Comparison();f=inputs[2];M=comp.norm(f);U=comp.norm(f,2);E=comp.reference_energy(f)
cube_records=[]
for side in (2,3):
    avg={};weight=r.edge(Q(1,side**6))
    for shift in product(range(side),repeat=6):
        for (s,x,p),w in f.items():m.put(avg,(s,add(x,shift),p),r.serial(w,weight))
    avgU=comp.norm(avg,2)
    diff=sum((comp.mu[s]*(v(f,k)-v(avg,k))**2 for k in f.keys()|avg.keys() for s in (k[0],)),Q(0))
    ck(comp.norm(avg)==M,'cube average preserves total comparison mass')
    ck(avgU<=M*M/(comp.mu_min*side**6),'positive cube convolution L1-L2 bound')
    ck(diff<=36*side*side*E,'ordered coordinate-telescope bound')
    ck(U<=2*diff+2*avgU,'two-term quadratic comparison')
    ck(U<=72*side*side*E+2*M*M/(comp.mu_min*side**6),'displayed six-axis cube inequality')
    cube_records.append({'side':side,'average':avg,'difference_square':diff,'average_square':avgU})

# Full physical-direction circuit remains U5. This externally declared layout
# translates; it is NOT claimed to be the selector's chosen material history.
seed=r.edge(Q(1,12));initial=(z,add(e,e));active={(b,x,p):seed for b,x in enumerate(initial) for p in r.PORTS};dormant={}
steps=[];offset=z
for n in range(5):
    cells=tuple(add(x,offset) for x in initial)
    flat={}
    for (b,x,p),w in active.items():m.put(flat,(m.A,x,p),w)
    for (b,x,p),w in dormant.items():m.put(flat,(m.D,x,p),m.scaled(w,1/comp.h))
    mass=c.total_readout(active)+c.total_readout(dormant)
    ck(mass==2,'moving-layout full response conserved')
    sup=max(w.total for w in flat.values())
    ck(sup<=comp.kernel_constant*mass/Q((1+n)**3),'uniform density bound finite illustration')
    local=r.total(w for (b,x,p),w in active.items() if x in cells).total
    steps.append({'stage':n,'layout':cells,'density_sup':sup,'local_active':local,
                  'active':active,'dormant':dormant,'global_mass':mass})
    if n<4:
        active,dormant,parts=u.local_release_step(active,dormant,cells,n+1,comp.transport,comp.epsilon)
        offset=r.advance(offset,2*n)

# Bounded analytic error/movement tail uses a convergent n^-3 sum, no simulation
# of all histories. Comparison constants are evaluated via positive BRC products.
C=comp.kernel_constant
motion_constant=r.serial(r.serial(r.edge(12*2*2),r.edge(C)),r.edge(Q(48))).total
ck(motion_constant==12*2*2*C/Q(1,48),'two-material motion-envelope constant')
# sum_(n>h)(n+1)^-3 <= 1/[2(h+1)^2] by an elementary monotone integral bound.
tails={str(h):str(min(Q(1),motion_constant/Q(2*(h+1)**2))) for h in (0,10,100)}

trace={'templates':paths,'energy_records':energy_records,'cube_records':cube_records,'moving_layout':steps}
raw=(json.dumps(c.encode(trace),ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode()
packed=gzip.compress(raw,mtime=0)
(EV/'full_trace.json.gz').write_bytes(packed)
summary={'status':'CONDITIONAL_UNIFORM_DELOCALIZATION_NOT_NATIVE_FORCE',
 'event_id':'EM-20261007-CELL-U7-UNIFORM-SPREAD-A6C9D2',
 'checks':checks,'actual_BRC_calls':dict(r.CALLS),'comparison_templates':len(paths),
 'max_template_length':maxlen,'Jensen_cases':len(energy_records),
 'parameter_certificates':c.encode(constants),'cube_sides':[2,3],
 'moving_layout_stages':5,'moving_layout_was_controlled_not_selector_sample':True,
 'uniform_density_rate':'C*M/(n+1)^3 for every layout schedule',
 'finite_size_unbounded_comoving_localization':'EXCLUDED_IN_FIXED_U5_CIRCUIT',
 'infinite_selector_motion':'TRIAL_MEASURE_ZERO_FOR_FINITE_N_M_FIXED_POSITIVE_KAPPA',
 'all_future_augmented_difference_TV':'min(1,18*N*C*delta/kappa)',
 'coarse_two_material_tail_examples':tails,'constants_not_sharp_or_physical_times':True,
 'native_force':False,'primitive_triad_lift':False,'physical_time':False,'prime_claim':False,
 'trace_uncompressed_bytes':len(raw),'trace_sha256':hashlib.sha256(raw).hexdigest(),
 'trace_compressed_sha256':hashlib.sha256(packed).hexdigest(),'independent_review':False}
(EV/'results.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
