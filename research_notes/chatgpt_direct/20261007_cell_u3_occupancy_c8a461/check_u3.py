#!/usr/bin/env python3
"""Finite same-author U3 certificate. Run with pinned packet_router + BRC."""
from fractions import Fraction as Q
from itertools import combinations,product
from dataclasses import asdict
from pathlib import Path
import json,gzip,hashlib
import occupancy as o
r=o.r
checks=0

def check(test,name):
    global checks
    checks+=1
    if not test: raise AssertionError(name)

root=Path(__file__).resolve().parent; ev=root/'evidence';ev.mkdir(exist_ok=True)
def conv(x):
    if isinstance(x,o.Demand):return {k:conv(v) for k,v in asdict(x).items()}
    if isinstance(x,r.brc.CWMState):return r.to_json(x)
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {str(k):conv(v) for k,v in x.items()}
    if isinstance(x,(tuple,list,set,frozenset)):return [conv(v) for v in x]
    return x

def verify_branches(cells,demands,bs):
    keys={t.key for t in demands}
    check(len(keys)==len(demands),'unique indivisible request IDs')
    check(r.total(b['measure'] for b in bs).total==1,'full finite trial measure retained')
    for b in bs:
        check(len(b['cells'])==len(set(b['cells'])),'successor exclusion')
        used={t.key for t in b['used']};held={t.key for t in b['held']}
        check(used.isdisjoint(held) and used|held==keys,'request partition')
        check(r.total(t.response for t in b['used']+b['held'])==r.total(t.response for t in demands),
              'full response CWM not erased by selection')
        check(len(b['interaction_log'])==len(used),'every accepted move logged')
        for a in range(len(cells)):
            delta=tuple(y-x for x,y in zip(cells[a],b['cells'][a]))
            check(sum(abs(x) for x in delta)==(1 if a in b['accepted'] else 0),
                  'one primitive step per accepted indivisible request')
        for a,bidx in combinations(b['accepted'],2):
            check(not(b['cells'][a]==cells[bidx] and b['cells'][bidx]==cells[a]),'no head-on exchange')
        # General decomposition: paths end at vacancies; cycles have even length >= 4.
        links={cells[a]:b['cells'][a] for a in b['accepted']}
        for start in links:
            p=start;seen=[]
            while p in links and p not in seen:
                seen.append(p);p=links[p]
            if p in seen:
                cycle=seen[seen.index(p):]
                check(len(cycle)>=4 and len(cycle)%2==0,'native bipartite cycle bound')
            else:
                check(p not in cells,'moving path ends at initial vacancy')
    return o.summarize(bs,cells)

z=r.ZERO;es=[r.direction(2*j) for j in range(6)]
def plus(*vs):return tuple(sum(v[j] for v in vs) for j in range(6))
layouts={
 'adjacent_pair':((z,es[0]),1),
 'one_vacancy_pair':((z,plus(es[0],es[0])),2),
 'square_221':((z,es[0],plus(es[0],es[1]),es[1]),1),
 'chain4':(tuple(tuple(k*x for x in es[0]) for k in range(4)),1),
 'star4':((z,es[0],es[1],es[2]),1),
 'square_plus_pendant5':((z,es[0],plus(es[0],es[1]),es[1],es[2]),1),
 'six_cycle':((z,es[0],plus(es[0],es[1]),plus(es[0],es[1],es[2]),plus(es[1],es[2]),es[2]),1)}
results={};full={};branchsets={}
for name,(cells,depth) in layouts.items():
    pulse=o.marked_pulse(cells,depth)
    check(r.total(pulse['layers'][-1].values()).total==len(cells)*pulse['rho']**depth,'active exact pulse mass')
    check(r.total(list(pulse['inactive'].values())+list(pulse['layers'][-1].values())).total==len(cells),
          'retired response sector included; not energy conservation')
    check(r.total([t.response for t in pulse['demands']]+list(pulse['nonacting'].values()))==
          r.total(pulse['layers'][-1].values()),'source/self/vacant fields kept')
    for t in pulse['demands']:
        check(t.response.total==Q(1,48)**depth,'exact first/second cross-source term on these inputs')
    bs=o.successor_branches(cells,pulse['demands'])
    summary=verify_branches(cells,pulse['demands'],bs)
    results[name]=summary;full[name]={'pulse':pulse,'branches':bs};branchsets[name]=bs

for name in ('adjacent_pair','chain4','star4'):
    check(results[name]['moving_measure']=='0','tree first-neighbor pulse jam')
check(results['square_221']['moving_measure']=='2/81','square circulation measure')
check(results['square_plus_pendant5']['moving_measure']=='1/54','five units also permit circulation')
check(results['six_cycle']['moving_measure']=='2/729','nonsquare six-cycle circulation')
check(results['one_vacancy_pair']['moving_measure']=='97/2401','vacancy resolution without postselection')
check(results['one_vacancy_pair']['resolved_branches']==5,'two-request clash expands into two resolutions')

# Exact occupancy correlations of the separated pair.
bs=branchsets['one_vacancy_pair'];middle=es[0]
ma=r.total(b['measure'] for b in bs if b['cells'][0]==middle)
mb=r.total(b['measure'] for b in bs if b['cells'][1]==middle)
joint=r.total(b['measure'] for b in bs if b['cells'][0]==middle and b['cells'][1]==middle)
check(ma.total==mb.total==Q(97,4802),'mirror weights identical')
check(joint.total==0 and r.serial(ma,mb).total>0,'independent occupancy marginals produce false collision')

# Permutation/reflection covariance and memory distinguishability.
square=branchsets['square_221'];moves=[b for b in square if b['accepted']]
check(len(moves)==2,'two labelled circulation branches')
check(set(moves[0]['cells'])==set(moves[1]['cells'])==set(layouts['square_221'][0]),'same occupied cells')
check(moves[0]['cells']!=moves[1]['cells'],'material identity/readout retained')
for b in moves:
    check(len(b['used'])==4 and len(b['held'])==4,'four whole tokens used/four held')
    check(r.total(t.response for t in b['held']).total==Q(1,12),'pending response not zero')
    check(all(sum(dst[j]-src[j] for src,dst in zip(layouts['square_221'][0],b['cells']))==0
              for j in range(6)),'net displacement hides actual steps')
# A moving material cannot reuse a stored old arrival port as a fresh local edge.
rebasing=[]
for b in moves:
    for t in b['held']:
        current=b['cells'][t.actor]
        historical=t.destination
        naive=r.advance(current,t.port)
        check(sum(abs(x-y) for x,y in zip(current,historical))==2,'stored square demand now needs two native edges')
        check(naive!=historical,'blind port reuse changes the actual target Cell')
        try:
            o.compatible(b['cells'],{t.actor:t})
        except ValueError:
            pass
        else:
            raise AssertionError('stale anchored request accepted')
        check(True,'stale request rejected by interface')
        steps=[p for p in r.PORTS if sum(abs(x-y) for x,y in zip(r.advance(current,p),historical))==1]
        pathstates=[];paths=[]
        for p in steps:
            mid=r.advance(current,p)
            for q in r.PORTS:
                if r.advance(mid,q)==historical:
                    pathstates.append(r.serial(r.edge(1),r.edge(1)))
                    paths.append((current,mid,historical))
        family=r.total(pathstates)
        check(len(paths)==2 and family.count==2 and family.total==2,'two ordered shortest repair paths, not one diagonal primitive')
        rebasing.append({'actor':t.actor,'source':t.source,'old_anchor':t.born_at,
                         'new_cell':current,'old_target':historical,'naive_target':naive,
                         'candidate_repair_paths':paths,'path_CWM':family,
                         'execution_or_collision_clearance_claimed':False})
# Adjacent pair no movement, but idle versus attempted conflict are distinct records.
adj=branchsets['adjacent_pair']
check(len(adj)==4 and all(b['cells']==layouts['adjacent_pair'][0] for b in adj),'same pair positions')
check(any(b['rejected'] for b in adj) and any(not b['rejected'] for b in adj),'rejection log distinguishable')

# Actual nontrivial signed-axis permutation + translation + material relabelling.
# This is a graph symmetry check, not a claimed full native rotation group.
perm=(3,5,1,4,0,2); signs=(1,-1,1,-1,1,-1); shift=(7,5,3,2,1,4)
def transform(v):
    out=list(shift)
    for i,x in enumerate(v):out[perm[i]]+=signs[i]*x
    return tuple(out)
for name in ('one_vacancy_pair','square_221','star4'):
    cells,depth=layouts[name];n=len(cells)
    tcells=tuple(transform(cells[n-1-i]) for i in range(n))
    tp=o.marked_pulse(tcells,depth);tb=o.successor_branches(tcells,tp['demands'])
    original_out={};new_out={}
    for b in branchsets[name]:
        key=tuple(transform(b['cells'][n-1-i]) for i in range(n))
        original_out[key]=r.merge(original_out.get(key,r.brc.CWM_ZERO),b['measure'])
    for b in tb:
        key=b['cells'];new_out[key]=r.merge(new_out.get(key,r.brc.CWM_ZERO),b['measure'])
    check(original_out==new_out,'actual graph/label covariance of complete outcome law')
# Reuse a derived BRC emission column for complete <=4-unit cube preparations.
mat,bulk=r.transport_tables()
one_step={p:r.brc.CWM_ZERO for p in r.PORTS}
seed=r.edge(Q(1,12))
for p in r.PORTS:
    for q,v in mat[p]:one_step[q]=r.merge(one_step[q],r.serial(seed,v))
check(all(v.total==Q(1,48) for v in one_step.values()),'default row sums; no new incidence')
cube=tuple(tuple(bits)+(0,0,0) for bits in product((0,1),repeat=3))
cube_cases=0;cube_proposals=0;cube_resolved=0;cube_moves=0
for n in range(1,5):
    for cells in combinations(cube,n):
        ds=[]
        for a,cell in enumerate(cells):
            for p in r.PORTS:
                target=r.advance(cell,p)
                if target in cells:
                    b=cells.index(target)
                    ds.append(o.Demand((1,b,a,p),b,a,cell,p,one_step[p^1]))
        bs=o.successor_branches(cells,ds)
        summary=verify_branches(cells,ds,bs)
        cube_cases+=1;cube_proposals+=summary['proposals'];cube_resolved+=len(bs)
        cube_moves+=summary['moving_branches']
check(cube_cases==162,'all cube subsets of size1..4 covered')

output={'status':'CONDITIONAL_ONE_TRANSACTION_CERTIFICATE_NOT_NATIVE_FORCE',
 'checks':checks,'source_kernel_blob':r.BLOB,
 'u2_router_blob':'7465f5aa16cbb8fba61ba4be80f8a6884b879c53',
 'actual_brc_calls':dict(r.CALLS),'wait_budget':'1/48','rho':'1/4',
 'sample_results':results,'gap_pair_center_marginal':str(ma.total),
 'false_independent_double_occupation':str(r.serial(ma,mb).total),
 'stale_request_witnesses':len(rebasing),'cube_cases':cube_cases,'cube_proposals':cube_proposals,'cube_resolved_branches':cube_resolved,
 'cube_moving_branches':cube_moves,'native_force_lift':False,'native_triads_admitted':False,
 'primitive_quantum_realization':False,'physical_time':False,'prime_claim':False},indent=2))
