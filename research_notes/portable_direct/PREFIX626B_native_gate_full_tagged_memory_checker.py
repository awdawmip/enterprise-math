#!/usr/bin/env python3
"""PREFIX-626B native X6 BRC fully tagged gate-memory exact witness checker.
Frozen science: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Reconstructs original STAR typed 576 actions, verifies two unit four-cycles,
gate edge, all-gate tagged paths, and sharp residual memory upper construction.
"""
from collections import defaultdict
from fractions import Fraction
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
    return tuple(IX[x] for x in
       ([(a,c,k) for k in near(a,c) if k!=p]
       +[(b,c,k) for k in near(b,c)]))
N=tuple(neighbors(i) for i in range(48))
AXIS=tuple(abs(c)-1 for a,p,c in P)
G=IX[(0,1,-3)]
WEIGHTS=(1,1,1,1,0,0)
assert len(P)==48 and G==4 and sum(map(len,N))==144
ACTIONS=[]
for i in range(48):
    for j in N[i]:
        for u,v in product((0,1),repeat=2):
            label=(i,j,u,v)
            w='GATE' if j==G and u==v==1 else WEIGHTS[AXIS[i]]
            ACTIONS.append((2*i+u,2*j+v,w,label))
assert len(ACTIONS)==576
edge=defaultdict(list)
for dst,src,weight,label in ACTIONS:
    edge[(src,dst)].append((weight,label))

IN_CYCLE=(9,28,80,52)
OUT_CYCLE=(29,80,52,8)
for cycle in (IN_CYCLE,OUT_CYCLE):
    for k,src in enumerate(cycle):
        dst=cycle[(k+1)%4]
        assert any(w==1 for w,l in edge[(src,dst)]),(src,dst)
assert any(w=='GATE' for w,l in edge[(9,29)])

# Exact future-operation BRC labelled path: for every index j one path has
# variable weight exactly g_j and every other action weight exactly one.
def coordinate_path(n,j):
    assert 1<=j<=n
    k=j-1
    a=(-k)%4
    ports=[IN_CYCLE[(a+i)%4] for i in range(k+1)]
    assert ports[-1]==9
    ports.append(29)
    ports.extend(OUT_CYCLE[i%4] for i in range(1,n-j+1))
    assert len(ports)==n+1
    labels=[]
    kinds=[]
    for pos,(src,dst) in enumerate(zip(ports,ports[1:]),start=1):
        w,l=next(((w,l) for w,l in edge[(src,dst)]
                 if w==('GATE' if pos==j else 1)),(None,None))
        assert w is not None,(n,j,pos,src,dst)
        labels.append(l)
        kinds.append(w)
    assert kinds.count('GATE')==1 and kinds[j-1]=='GATE'
    return ports,labels,kinds

# Exact gate-product sufficient statistic plus explicit sharp recovery.
def products(gates):
    n=len(gates)
    out={r:Fraction(1) for r in range(4)}
    group={r:[] for r in range(4)}
    for j in range(2,n):
        r=j%4
        out[r]*=(1+gates[j-1]/3)
        group[r].append(j)
    return out,group

def encode_and_recover(gates):
    n=len(gates)
    ps,group=products(gates)
    omitted={r:group[r][-1] for r in range(4) if group[r]}
    extras={j:gates[j-1] for r in range(4) for j in group[r][:-1]}
    known={1:gates[0],n:gates[-1],**extras}
    recovered=dict(known)
    for r,missing in omitted.items():
        den=Fraction(1)
        for j in group[r][:-1]:den*=1+known[j]/3
        recovered[missing]=3*(ps[r]/den-1)
    assert sorted(recovered)==list(range(1,n+1))
    assert [recovered[j] for j in range(1,n+1)]==gates
    assert len(extras)==max(n-6,0)
    return extras,ps,omitted

runs=[]
for n in (2,3,4,5,6,7,8,9,10,13,17,32,64):
    g=[Fraction((7*i+3)%19,5) for i in range(n)]
    extras,ps,omitted=encode_and_recover(g)
    for j in range(1,n+1):
        ports,labels,kinds=coordinate_path(n,j)
        w=Fraction(1)
        for pos,kind in enumerate(kinds,1):
            w*=g[pos-1] if kind=='GATE' else kind
        assert w==g[j-1]
    runs.append({'n':n,'gate_positions_verified':n,'minimal_extra_continuous_scalars':len(extras),
                 'active_residue_groups':len(omitted),'all_tagged_gate_path_coordinates_exact':True,
                 'exact_gate_vector_recovered':True})

alpha=[Fraction(x) for x in (0,1,0,0,0,2,0,0,0,0)]
beta=[Fraction(x) for x in (0,2,0,0,0,1,0,0,0,0)]
pa,_=products(alpha)
pb,_=products(beta)
assert pa==pb and pa[2]==Fraction(20,9)
_,_,ka=coordinate_path(10,2)
assert ka[1]=='GATE' and all(x==1 for i,x in enumerate(ka) if i!=1)
assert alpha[1]==1 and beta[1]==2
result={'schema':'PREFIX626B_ORIGINAL_NATIVE_X6_TAGGED_GATE_MEMORY_V1',
'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
'native_actions':len(ACTIONS),'native_ports':96,'native_phases':48,
'incoming_unit_cycle_to_gate_source_9':list(IN_CYCLE)+[IN_CYCLE[0]],
'outgoing_unit_cycle_from_gate_target_29':list(OUT_CYCLE)+[OUT_CYCLE[0]],
'gate_edge_source_target':[9,29],
'full_tagged_path_operator_injective_in_entire_n_gate_sequence':True,
'baseline_observer':'n known; boundary gates g1,gn plus all interior four residue products P_r',
'minimal_additional_real_scalars_under_continuous_representations':'max(0,n-6)',
'lower_bound':'relative interior product fibers have dimension n-2-number_of_nonempty_residues; full labelled path admits path-coordinate readout g_j for every j; continuity and invariance of domain',
'upper_bound':'retain all but one interior gate in each nonempty residue class and solve missing gate exactly using positive P_r',
'exact_checks':runs,
'checked_n':[r['n'] for r in runs],
'checked_all_gate_position_count':sum(r['n'] for r in runs),
'equal_endpoint_operator_tagged_path_contrast':{'n':10,'P_r_equal':True,'tagged_path_mass_alpha':'1','tagged_path_mass_beta':'2'},
'status':'ALL_ASSERTIONS_PASS','review':'AUTHOR_SIDE_UNREVIEWED'}
Path(__file__).with_name('PREFIX626B_native_gate_full_tagged_memory_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'ALL_ASSERTIONS_PASS','n_checked':len(runs),
'gate_positions_checked':sum(r['n'] for r in runs),
'memory_formula':'max(0,n-6)','cycles':2},ensure_ascii=False))
