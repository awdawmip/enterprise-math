#!/usr/bin/env python3
"""Exact finite U11 tests. python check_u11.py
All new scientific aggregation uses source-pinned BRC; proofs are in NOTE.md.
No native force, conserved physical energy, independent review or prime claim.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction as Q
from collections import Counter,deque
import hashlib,json,gzip
import resource_lift as v
m,r,u=v.m,v.r,v.u
ROOT=Path(__file__).resolve().parent;EV=ROOT/'evidence';EV.mkdir(exist_ok=True)
checks=0

def ck(b,label):
    global checks
    checks+=1
    if not b:raise AssertionError((checks,label))

def add(a,b):return tuple(x+y for x,y in zip(a,b))

def disp(w):return m.endpoint(r.ZERO,w)

z=r.ZERO;e1=r.direction(0);e2=r.direction(2);e3=r.direction(4)
cells=(z,e1,add(e1,e2),e2)
base=m.from_tree(cells,((0,1),(1,2),(2,3)))
other=m.material(base,0,4,True)
ck((base.length(),other.length())==(3,4),'actual U9 inverse pair')

protocol_records=[];linear_readouts=[]
# All possible actor/port requests on the original four-actor path witness.
# Plus star centers of each incidence degree1..5 with sufficient free records.
inputs=[(base,a,p) for a in range(4) for p in r.PORTS]
for d in range(1,6):
    cc=tuple(tuple(j*x for x in e1) for j in range(d+1))
    st=m.from_tree(cc,tuple((0,j) for j in range(1,d+1)))
    inputs.append((st,0,4))
for st,a,p in inputs:
    d=len(v.incident_slots(st,a));L=st.length();s=v.prepared(st,L+d+2,3,reservoir_cell=st.cells[a])
    chosen=tuple(t for t,c in s.free)[:d]
    out,trace=v.transaction(s,a,p,True,chosen)
    raw=m.material(st,a,p,True)
    ck((out is None)==(raw is None),'inventory does not override collision')
    if out is None:
        ck(trace==[],'collision makes no resource transaction');continue
    ck(out.state==raw,'same successful U9 geometry')
    ck(out.state.length()==L+d and len(out.free)==len(s.free)-d,'resource budget delta')
    ck(len(trace)==2*d+1,'specified finite protocol duration')
    before_meet=[m.endpoint(st.cells[i],wa) for i,j,wa,wb in st.links for _ in (0,1)]
    for frame in trace:
        bound=set(frame['bound']);free={i for i,c in frame['free']};held=set(frame['held'])
        ck(not(bound&free or bound&held or free&held),'exclusive resource ownership')
        ck(bound|free|held==set(range(s.B)),'no record resource lost or created')
        ck(len(bound)+len(free)+len(held)==s.B,'integer resource conservation')
        ck(frame['trace_weight'].total==1,'unit trace weight is not physical energy')
        for head,word,target in zip(frame['heads'],frame['words'],before_meet):
            ck(m.endpoint(head,word)==target,'actual old meetings persist in partial phases')
        if frame['hop']:
            aa,bb=frame['hop'];ck(sum(abs(x-y) for x,y in zip(aa,bb))==1,'one native carry edge')
            ck(len(frame['unattached_slots'])==d,'in-flight endpoint mismatch retained')
    back,reverse=v.transaction(out,a,p^1,False,chosen)
    ck(back==s,'reverse restores token IDs, free phases and every original path')
    ck(len(reverse)==2*d+1,'reverse cost and sources retained')
    # Nonzero free phase cannot be silently erased to force a move.
    blocked=v.Inventory(st,s.tokens,tuple((i,1) for i,c in s.free),s.B,s.q,s.reservoir_cell)
    fail,log=v.transaction(blocked,a,p,True,chosen)
    ck(fail is None and not log,'free count alone does not certify binding phase')
    # A reservoir at a remote Cell is not silently moved to the actor.
    remote=v.Inventory(st,s.tokens,s.free,s.B,s.q,r.advance(s.reservoir_cell,10))
    no_remote,_=v.transaction(remote,a,p,True,chosen)
    ck(no_remote is None,'remote resource requires unimplemented explicit delivery')
    # An attempted reused token is not a new resource.
    if d>1:
        try:v.transaction(s,a,p,True,(chosen[0],)*d)
        except ValueError:ck(True,'duplicate allocation rejected')
        else:ck(False,'duplicate allocation was accepted')
    dd=tuple(sum(disp(w)[j] for w in v.paths(out.state))-sum(disp(w)[j] for w in v.paths(st)) for j in range(6))
    hop=r.direction(p)
    ck(dd==tuple(-d*x for x in hop),'path-displacement contrast scales with incidence degree')
    linear_readouts.append({'degree':d,'material_shift':hop,'path_shift':dd})
    protocol_records.append({'before':s,'after':out,'forward':trace,'reverse':reverse})
ck({a['degree'] for a in linear_readouts}=={1,2,3,4,5},'all requested incidence degrees covered')

# Complete finite resource fibres and their ACTUAL microscopic reversible kernel.
# No Barker factor is added. There are exactly B(q+2) labels per state.
fibre_records=[];total_states=0;total_labels=0
for B,q in ((4,2),(5,3),(6,2)):
    states=v.pair_universe(base,other,B,q);index={s:i for i,s in enumerate(states)}
    ck(len(index)==len(states),'every resource assignment uniquely represented')
    counts=Counter(s.state.length() for s in states)
    for L,n in counts.items():
        family=v.multiplicity(B,L,q)
        ck(family.count==n and family.total==n and family.dominant==1,'complete multiplicity identity')
    nq=B*(q+2);edge=r.edge(Q(1,nq));mass=r.edge(Q(1,len(states)))
    columns={};graph={i:set() for i in range(len(states))};rows=[]
    for i,s in enumerate(states):
        row={}
        labels=[(kind,t,0) for kind in ('grow','shrink') for t in range(B)]
        labels += [('phase',t,k) for t in range(B) for k in range(q)]
        for kind,t,k in labels:
            y=v.pair_step(s,base,other,kind,t,k)
            inv=('shrink' if kind=='grow' else 'grow') if kind!='phase' else 'phase'
            back=v.pair_step(y,base,other,inv,t,(-k)%q)
            # Invalid grow/shrink labels are self-loops but their formal inverse
            # may be valid at that same state: do not claim those labels pair.
            if y!=s:ck(back==s,'every nontrivial label has an equal-weight reverse')
            j=index[y]
            row[j]=r.merge(row.get(j,v.ZERO),edge)
            graph[i].add(j)
            total_labels+=1
        ck(r.total(row.values()).total==1,'all microscopic alternatives retained')
        for j,w in row.items():columns[j]=r.merge(columns.get(j,v.ZERO),r.serial(mass,w))
        rows.append(row)
    for j in index.values():ck(columns[j].total==mass.total,'full uniform stationary balance')
    # Original three bound identities are conserved: explicitly disclose sectors.
    seen=set();component_sizes=[]
    while len(seen)<len(states):
        start=next(i for i in range(len(states)) if i not in seen)
        reach={start};queue=deque([start])
        while queue:
            for j in graph[queue.popleft()]-reach:reach.add(j);queue.append(j)
        seen|=reach;component_sizes.append(len(reach))
    sector_count=B*(B-1)*(B-2)
    ck(len(component_sizes)==sector_count,'old bound resource identities label invariant sectors')
    ck(len(set(component_sizes))==1,'same finite test law in each sector')
    n0,n1=counts[3],counts[4]
    pi1=Q(n1,n0+n1)
    ck(pi1==Q(B-3,q+B-3),'exact finite resource positional marginal')
    fibre_records.append({'B':B,'q':q,'states':states,'rows':rows,'counts':dict(counts),
                          'invariant_sectors':len(component_sizes),'component_size':component_sizes[0],
                          'position1_stationary':pi1})
    total_states+=len(states)

# Same geometric state, same token IDs and same free amount, different local phase.
s=v.prepared(base,5,3);t=s.free[0][0]
a,tr=v.transaction(s,0,4,True,(t,))
s2=v.phase_shift(s,t,1);b,tr2=v.transaction(s2,0,4,True,(t,))
ck(a is not None and b is None,'phase-sensitive resource eligibility witness')
ck(s.state==s2.state and s.tokens==s2.tokens and len(s.free)==len(s2.free),'same coarse resource count')
ck(v.phase_shift(s2,t,2)==s,'witness preparation is reversible and explicit')
phase_laws=[]
for item in (s,s2):
    outlaw={};qw=r.edge(Q(1,item.B*(item.q+2)))
    labels=[(kind,tok,0) for kind in ('grow','shrink') for tok in range(item.B)]
    labels += [('phase',tok,k) for tok in range(item.B) for k in range(item.q)]
    for kind,tok,k in labels:
        yy=v.pair_step(item,base,other,kind,tok,k)
        outlaw[yy.state]=r.merge(outlaw.get(yy.state,v.ZERO),qw)
    phase_laws.append(outlaw)
ck(phase_laws[0][other].total==Q(2,25) and phase_laws[1][other].total==Q(1,25),
   'complete same-observer query distinguishes available local resource phases')
phase_TV=sum(abs(phase_laws[0].get(k,v.ZERO).total-phase_laws[1].get(k,v.ZERO).total)
             for k in phase_laws[0].keys()|phase_laws[1].keys())/2
ck(phase_TV==Q(1,25),'exact resource-phase position TV')

# Main B=64 comparison. q=48B is an EXPLICIT choice to compare against lambda=1/48.
main=[]
for B in (4,8,16,64,256):
    q=48*B
    f0=v.multiplicity(B,3,q);f1=v.multiplicity(B,4,q)
    norm=r.edge(1/r.merge(f0,f1).total)
    pi1=r.serial(f1,norm).total
    ck(pi1==Q(B-3,49*B-3),'without-replacement correction computed by BRC counting')
    contrast=Q(1,49)-pi1
    ck(contrast==Q(144,49*(49*B-3)),'exact two-state contrast')
    main.append({'B':B,'q':q,'state1':pi1,'ideal_state1':Q(1,49),'TV':contrast})
ck(main[3]['state1']==Q(61,3133) and main[3]['TV']==Q(144,153517),'main64 certificate')

# Depletion identity, monotone convergence and a global second-moment TV bound.
for B in range(1,33):
    for L in range(0,40):
        d=v.depletion(B,L).total
        ck(0<=d<=1,'positive finite-inventory density multiplier')
        ck(1-d<=Q(L*(L-1),2*B),'birthday-collision union bound including L>B')
        ck(v.depletion(B+1,L).total>=d,'fixed-length depletion approaches one monotonically')

# Stronger source-derived positive denominator: ALL shortest relative four-actor
# states, not just the single fixed square. Tree increments determine positions.
w=m.Weights();short_link=r.merge(w.power(1),w.power(1))  # two split labels
short_tree=r.serial(short_link,r.serial(short_link,short_link))
Zlower=v.ZERO;short_rows=[]
for T in u.trees(4):
    valid=0;subtotal=v.ZERO
    for pp in product(r.PORTS,repeat=3):
        todo=list(zip(T,pp));pos={0:z}
        while todo:
            for k,(e,p) in enumerate(todo):
                i,j=e
                if i in pos and j not in pos:pos[j]=add(pos[i],r.direction(p));todo.pop(k);break
                if j in pos and i not in pos:pos[i]=add(pos[j],r.direction(p^1));todo.pop(k);break
            else:raise AssertionError('tree traversal error')
        if len(set(pos.values()))==4:
            subtotal=r.merge(subtotal,short_tree);valid+=1
    degrees=Counter(a for edge0 in T for a in edge0)
    expected=1320 if max(degrees.values())==3 else 1452
    ck(valid==expected,'all one-edge tree embeddings with exclusion')
    Zlower=r.merge(Zlower,subtotal)
    short_rows.append({'tree':T,'valid_increment_assignments':valid,'CWM':subtotal})
ck(Zlower.count==181632,'complete shortest augmented relative population')
ck(Zlower.total==Q(473,288),'exact improved whole-space lower denominator')
# Unrestricted six-leg ordered-second-marker mass: 16*6*7*rho^2/(1-rho)^8.
rho=Q(1,4);r.CALLS['one_state_recurrent_cwm']+=1
geom=r.brc.one_state_recurrent_cwm([w.lam]*12)
num=r.serial(r.edge(rho),r.edge(rho))
for _ in range(8):num=r.serial(num,r.edge(geom.total_mass_closure))
num=r.total(num for _ in range(16*6*7))
moment_bound=r.serial(num,r.edge(1/Zlower.total)).total
ck(moment_bound>0,'finite full-state ordered second-marker upper bound')
TVmillion=min(Q(1),moment_bound/Q(2*10**6))
# This is a static COMPLETE augmented-state bound for this new density, not a
# trajectory/mixing estimate or proof that any reservoir is a physical heat bath.

summary={'schema':'CELL_U11_FINITE_RESOURCE_RESULTS_V1','event_id':'EM-20261008-CELL-U11-RESOURCE-REACTION-C7E4A1',
 'checks':checks,'BRC_calls':dict(r.CALLS),'protocol_cases':len(protocol_records),
 'complete_fibre_states':total_states,'microscopic_labels_executed':total_labels,
 'fibre_tests':[{'B':a['B'],'q':a['q'],'states':len(a['states']),'counts':a['counts'],
                 'sectors':a['invariant_sectors'],'state1':str(a['position1_stationary'])} for a in fibre_records],
 'finite_inventory_comparisons':[{k:str(x) if isinstance(x,Q) else x for k,x in a.items()} for a in main],
 'resource_phase_position_TV':str(phase_TV),
 'shortest_relative_population':Zlower.count,'whole_space_Z_lower':str(Zlower.total),
 'full_target_factorial_second_moment_upper':str(moment_bound),'static_TV_bound_B_one_million':str(TVmillion),
 'new_results':['identified_inventory_multiplicity_(B)_L_q^(B-L)',
                'isolated_local_prefix_transfer_preserves_all_resource_identities',
                'phase_eligibility_residual_not_determined_by_free_total',
                'resource_weighted_law_differs_before_capacity_is_reached',
                'depletion_to_ideal_static_TV_bound_via_factorial_second_moment',
                'uniform_material_and_path_displacement_readout_cannot_encode_nontrivial_reaction'],
 'native_force':False,'native_triad_certificate':False,'physical_energy_conservation':False,
 'physical_clock':False,'complete_distributed_U9_resource_model':False,'prime_claim':False,
 'independent_review':False,'registration':'CURRENT_PLATFORM_BLOCKED_NO_RETRY_NO_NEW_ID',
 'microscopic_pair_kernel_is_full_U9':False,'two_state_test_has_multiple_invariant_resource_sectors':True}
trace={'protocols':protocol_records,'reaction_readouts':linear_readouts,'complete_fibre_kernels':fibre_records,
       'resource_phase_witness':[s,s2],'resource_phase_position_laws':phase_laws,'shortest_relative_tree_counts':short_rows,'comparisons':main}
raw=(json.dumps(v.encode(trace),sort_keys=True,separators=(',',':'))+'\n').encode()
packed=gzip.compress(raw,mtime=0)
(EV/'full_trace.json.gz').write_bytes(packed)
summary.update(trace_bytes=len(raw),trace_sha256=hashlib.sha256(raw).hexdigest(),
               trace_compressed_sha256=hashlib.sha256(packed).hexdigest())
(EV/'results.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
