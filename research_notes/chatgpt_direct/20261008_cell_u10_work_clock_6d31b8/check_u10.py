#!/usr/bin/env python3
"""New U10 finite certificates, not independent review or native mechanics."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib
import local_work_clock as c
m,r,u=c.m,c.r,c.u
ROOT=Path(__file__).resolve().parent;EV=ROOT/'evidence';EV.mkdir(exist_ok=True)
checks=0

def ck(v,label):
    global checks
    checks+=1
    if not v:raise AssertionError((checks,label))

records=[]
for radius in range(17):
    p,q,h=c.distant_pair(radius);b=p.cells[1]
    ck(c.header(p)==c.header(q),'same whole coarse header')
    ck(c.local_view(p,b,radius)==c.local_view(q,b,radius),'same uncached radius view')
    sp,sq=c.slots(p),c.slots(q)
    changed=[key for key in sp if sp[key]!=sq[key]]
    min_changed=min(min(c.distance(sp[key][0],b),c.distance(sq[key][0],b)) for key in changed)
    ck(min_changed==h and h>radius,'all disagreement outside observation cone')
    ck(m.slide(p,0,1,2) is not None and m.slide(q,0,1,2) is None,'different actual U9 slide eligibility')
    for s,expected in ((p,True),(q,False)):
        result=c.compare_trails(s)
        ck(result['equal']==expected,'local traversal agrees with exact immutable eligibility')
        ck(result['ticks']==2*result['matched_edges']+1,'explicit outward/acknowledgement clock')
        ck(result['positive_trace_weight'].total==1,'comparison does not delete response mass')
        for row in result['trace']:
            if row[0] in ('READ_HOP','RETURN'):
                ck(c.distance(row[1],row[2])==1,'each actual communication hop is native')
        if expected:ck(result['matched_edges']==2*h+2,'complete equal-word verification')
        else:ck(result['matched_edges']==h,'remote first mismatch')
        records.append({'radius':radius,'equal_input':expected,'header':c.header(s),'min_changed_distance':min_changed,
                        'comparison':result})

# The locality inputs above are explicitly prepared admissible records;
# their creation/communication costs are not assumed to be zero.
z=r.ZERO;e1=r.direction(0);e2=r.direction(2)
cells=(z,e1,tuple(x+y for x,y in zip(e1,e2)),e2)
T=((0,1),(1,2),(2,3));base=m.from_tree(cells,T)
# The full locality inputs were prepared explicitly above; their representation
# lower bound only needs admissibility, not a zero-work physical preparation.

# A real U9 one-edge inverse pair; restrict proposals to this pair as a TEST.
s0=base;s1=m.material(s0,0,4,True)
ck(s1 is not None and m.material(s1,0,5,False)==s0,'actual U9 move and exact inverse')
ck((s0.length(),s1.length())==(3,4),'work example uses actual path lengths')
ck(c.distance(s0.cells[0],s1.cells[0])==1,'work example has different material positions')
cost=(2*s0.length()+1,2*s1.length()+1)
clock_rows=[];fullkernels=[]
for lam in (Q(1,48),Q(1,36),Q(1,60),Q(1,24)):
    w=m.Weights(lam);weights=(w.weight(s0),w.weight(s1))
    original=c.normalized(weights)
    for corrected in (False,True):
        if corrected:
            a01,b01=c.corrected_decision(w,1,*cost)
            a10,b10=c.corrected_decision(w,-1,*reversed(cost))
            target=(r.serial(weights[0],r.edge(Q(1,cost[0]))),
                    r.serial(weights[1],r.edge(Q(1,cost[1]))))
        else:
            a01,b01=w.decision(1);a10,b10=w.decision(-1);target=weights
        K=({0:b01,1:a01},{0:a10,1:b10})
        pi=c.normalized(target)
        for j in range(2):
            incoming=r.total(r.serial(pi[i],K[i][j]) for i in range(2)).total
            ck(incoming==pi[j].total,'embedded stationary total readout')
        ck(r.serial(pi[0],a01).total==r.serial(pi[1],a10).total,'embedded detailed balance')
        lift=c.clock_lift(K,cost);nu=c.phase_invariant(target,cost)
        ck(len(lift)==16,'all16 phase states present')
        nxt=c.push(lift,nu)
        for key in lift:
            ck(r.total(lift[key].values()).total==1,'all phase transition rows normalized')
            ck(nxt[key].total==nu[key].total,'exact invariant total at every phase')
        grouped=c.group_phases(nu)
        ck(r.total(grouped.values()).total==1,'time-sampled readout normalized')
        expected=lam*cost[1]/(cost[0]+lam*cost[1]) if not corrected else lam/(1+lam)
        ck(grouped[1].total==expected,'duration bias or exact compensation')
        ck(grouped[1].total==original[1].total if corrected else grouped[1].total!=original[1].total,
           'target restoration requires an actual different kernel')
        law={(0,0):r.edge(1)};prefix=[]
        for tick in range(41):
            ck(r.total(law.values()).total==1,'finite BRC clock propagation mass')
            prefix.append({'tick':tick,'law':law})
            law=c.push(lift,law)
        clock_rows.append({'lambda':lam,'corrected':corrected,'cost':cost,'completed_distribution':pi,
                           'work_distribution':grouped,'forward_accept':a01,'reverse_accept':a10,
                           'clock_stationary':nu})
        fullkernels.append({'lambda':lam,'corrected':corrected,'kernel':lift,'evolution':prefix})
main=clock_rows[0];fixed=clock_rows[1]
ck(main['completed_distribution'][1].total==Q(1,49),'main completion fraction')
ck(main['work_distribution'][1].total==Q(3,115),'main actual work-tick fraction')
ck(main['work_distribution'][1].total-main['completed_distribution'][1].total==Q(32,5635),'exact clock TV contrast')
ck(fixed['forward_accept'].total==Q(7,439),'corrected forward acceptance')
ck(fixed['work_distribution'][1].total==Q(1,49),'corrected work observation restored')

# General phase-lift invariant on a nontrivial three-state reversible chain.
# Positive masses/flows and the residual wait branch are explicit test inputs.
ms=tuple(r.edge(q) for q in (Q(1),Q(2),Q(3)))
K=[]
for i in range(3):
    row={j:r.edge(Q(1,12)/ms[i].total) for j in range(3) if j!=i}
    row[i]=r.edge(1-r.total(row.values()).total);K.append(row)
for work in ((1,2,5),(3,3,3),(2,7,11)):
    lifted=c.clock_lift(K,work);nu=c.phase_invariant(ms,work);nxt=c.push(lifted,nu)
    for key in nu:ck(nu[key].total==nxt[key].total,'general multistate work invariant')

bounds=[c.tail_bounds(B) for B in (16,32,48,64,80)]
ck(bounds[3]['completion_tail_upper']<Q(1,10**12),'64-edge whole-state completion tail certificate')
ck(bounds[3]['work_tail_upper']<Q(1,10**12),'64-edge whole-state linear-clock tail certificate')
for a,b in zip(bounds,bounds[1:]):
    ck(b['completion_tail_upper']<=a['completion_tail_upper'],'completion tail monotone bound')
    ck(b['work_tail_upper']<=a['work_tail_upper'],'work tail monotone bound')

# Lift the work-clock correction to the FULL U9 stationary shape law.
# A marker on one edge records L*lambda^L without numerical differentiation.
o=u.Overlap()
shapes={'square_221':cells,
        'four_chain':tuple(tuple(j*v for v in e1) for j in range(4)),
        'four_star':(z,e1,e2,r.direction(4))}
score_rows={name:c.work_score(xx,o,20) for name,xx in shapes.items()}
for name,row in score_rows.items():
    lo,hi=row['conditional_work_interval']
    ck(7<=lo<=hi,'every four-member relation needs at least three edges')
    ck(hi-lo<Q(1,10**4),'certified conditional-work interval')
    ordinary=u.Candidate(o,20).score(shapes[name])
    ck(row['lower'][0]==ordinary['lower'],'new marked observer preserves original ordinary weight')
# A non-fibre-constant mean workload changes relative stationary shape odds.
ck(score_rows['square_221']['conditional_work_interval'][1]<score_rows['four_chain']['conditional_work_interval'][0],
   'full target work-clock changes square/chain relative odds')
# Direct marker product law on explicit small positive families.
for aa,bb in ((1,2),(2,3),(0,4)):
    wa,wb=m.Weights().power(aa),m.Weights().power(bb)
    ja=r.total(wa for _ in range(aa));jb=r.total(wb for _ in range(bb))
    ww,jj=c.jet_product((wa,ja),(wb,jb))
    ck(jj==r.total(ww for _ in range(aa+bb)),'marked-edge Leibniz identity in full CWM')

# No uniform acknowledgement time exists: exact prefix construction for all R
# is proved in NOTE.md; finite R0..16 are implementation checks only.
summary={'schema':'CELL_U10_WORK_CLOCK_RESULTS_V1','event_id':'EM-20261008-CELL-U10-WORK-CLOCK-6D31B8',
 'status':'CONDITIONAL_CAUSAL_ENCODING_AND_WORK_CLOCK_THEOREMS',
 'checks':checks,'BRC_calls':dict(r.CALLS),'locality_radii_checked':[0,16],
 'locality_inputs':34,'phase_states_per_clock_example':16,'clock_examples':len(clock_rows),
 'clock_ticks_executed_per_example':41,'example_lengths':[3,4],'example_costs':cost,
 'original_completion_fraction':'1/49','uncorrected_work_fraction':'3/115',
 'exact_clock_TV':'32/5635','corrected_acceptance':'7/439','corrected_work_fraction':'1/49',
 'full_shape_work_intervals':{name:list(map(str,row['conditional_work_interval'])) for name,row in score_rows.items()},
 'tail_certificates':c.encode(bounds),'native_force':False,'native_triad_certificate':False,
 'physical_time_calibrated':False,'full_distributed_U9_compiler':False,
 'all_U9_dynamics_revalidated':False,'primality_claim':False,'independent_review':False,
 'research_registration':'CURRENT_PLATFORM_BLOCKED_NO_RETRY_NO_NEW_RA'}
trace={'locality':records,'clock_examples':clock_rows,'phase_kernels_and_evolutions':fullkernels,
       'example_states':[s0,s1],'tail_bounds':bounds,'full_shape_work_scores':score_rows}
raw=(json.dumps(c.encode(trace),sort_keys=True,separators=(',',':'))+'\n').encode()
pack=gzip.compress(raw,mtime=0)
(EV/'full_trace.json.gz').write_bytes(pack)
summary.update(trace_bytes=len(raw),trace_sha256=hashlib.sha256(raw).hexdigest(),
               trace_compressed_sha256=hashlib.sha256(pack).hexdigest())
(EV/'results.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
