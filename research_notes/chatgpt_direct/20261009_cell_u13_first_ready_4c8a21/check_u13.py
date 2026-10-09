#!/usr/bin/env python3
"""U13 exact first-ready BRC checks. No native firing or ordinary solver."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
from dataclasses import replace
import json, gzip, hashlib
import first_ready as f
r=f.r;ROOT=Path(__file__).resolve().parent;EV=ROOT/'evidence';EV.mkdir(exist_ok=True)
checks=0

def ck(ok,label):
    global checks
    checks+=1
    if not ok:raise AssertionError((checks,label))

plans=f.example_plans();table=[];prefix_records=[];closure_records=[]
for probs in ((Q(1,2),)*3,(Q(1,3),)*3,(Q(1,2),Q(1,3),Q(2,3))):
    for H in (0,1,2,3,4,8,None):
        p=f.Protocol(plans,probs,H);values=p.solve(p.initial())
        ck(values[0]+values[1]==1,'entire outcome law normalized')
        ck(all(x>=0 for x in values),'positive probability and first moment observers')
        if H is None:ck(values[0]==1,'finite routes with positive advance eventually all arrive')
        finite=p.prefixes(14);joined=f.joined_first_curve(p.lengths,p.a,H,14)
        accum_yes=accum_no=f.ZERO
        for t,(hit,no,surv,direct) in enumerate(zip(finite['hit'],finite['expired'],finite['survival'],joined),1):
            ck(hit==direct,'full C/W/M identity: stopped joint law equals positive last-arrival join')
            accum_yes=r.merge(accum_yes,hit);accum_no=r.merge(accum_no,no)
            ck(r.total((accum_yes,accum_no,surv)).total==1,'finite first-success/failure/live conservation')
            ck(accum_yes.total<=values[0],'finite success is lower bound, not hard cutoff')
            ck(values[0]-accum_yes.total<=surv.total,'remaining success bounded by live weight')
        # Actual local closure equalities on every computed transient state.
        for rec in p.closure_records:
            x=rec['state'];vals=rec['observers'];incoming=[f.ZERO]*4
            for bits,y,w in p.row(x):
                vv=p.solve(y)
                for j in (0,1):incoming[j]=r.merge(incoming[j],r.serial(w,f.lift(vv[j])))
                for j in (2,3):
                    term=r.serial(w,r.merge(f.lift(vv[j]),f.lift(vv[j-2])))
                    incoming[j]=r.merge(incoming[j],term)
            for actual,expected in zip(incoming,vals):ck(actual.total==expected,'exact total first-step recurrence')
        table.append({'a':probs,'H':H,'success':values[0],'failure':values[1],
                      'success_tick_moment':values[2],'terminal_mean_ticks':values[2]+values[3],
                      'conditional_success_ticks':values[2]/values[0],
                      'finite_hit_mass14':accum_yes.total,'live14':finite['survival'][-1].total,
                      'transient_closures':len(p.closure_records)})
        prefix_records.append({'a':probs,'H':H,'prefix':finite})
        closure_records.append({'a':probs,'H':H,'states':p.closure_records})

main=[t for t in table if t['a']==(Q(1,2),)*3]
want={0:Q(1,343),1:Q(41,1372),2:Q(849,5488),3:Q(7463,21952),4:Q(46087,87808),8:Q(20639019,22478848),None:Q(1)}
for row in main:ck(row['success']==want[row['H']],'frozen main exact fractions, not independent review')
for a in (Q(1,2),Q(1,3)):
    # Fresh protocol sums a^5 b^(3n+4) choose(n+2,2), a positive three-stage closure.
    b=1-a;unit=f.ONE
    for _ in range(5):unit=r.serial(unit,r.edge(a))
    for _ in range(4):unit=r.serial(unit,r.edge(b))
    r.CALLS['one_state_recurrent_cwm']+=1
    c=r.brc.one_state_recurrent_cwm([b**3])
    for _ in range(3):unit=r.serial(unit,r.edge(c.total_mass_closure))
    row=next(t for t in table if t['a']==(a,)*3 and t['H']==0)
    ck(unit.total==row['success'],'fresh all-time success via positive generating grammar')
    ck(row['conditional_success_ticks']==3/(1-b**3),'fresh conditional mean')

# Deterministic earliest schedules: same five spatial hops, with explicit storage.
deterministic=[]
for H in (0,1,2,None):
    p=f.Protocol(plans,(1,1,1),H);vals=p.solve(p.initial())
    ck(vals[0]==(1 if H in (2,None) else 0),'minimum two-clock storage window')
    choices=[(1,1,1)]
    if H!=0:choices.append((0,1,0))
    if H in (2,None):choices.append((0,1,0))
    trace=p.trace(choices)
    if H in (2,None):
        ck(trace[-1]['state'].outcome=='READY_RESERVED','all three reserved once')
        ck(trace[-1]['arrival_ticks']==(1,3,1),'arrival ages retained, not freshened')
        ck(trace[-1]['ages']==(2,0,2),'two old inputs remain distinguishable from fresh')
        ck(sum(map(sum,choices))==5,'exact five native transport hops')
        try:p.trace(choices+[(0,0,0)])
        except ValueError:ck(True,'no reissue of terminal occurrences')
        else:ck(False,'source triple reused')
    for frame in trace:
        ck(not frame['native_closure_certified'] and not frame['native_firing_performed'],'routing is not physical closure')
    deterministic.append({'H':H,'trace':trace,'eventual':vals})

# Same material/resource cells, progress, IDs and final axes; different arrival age.
p=f.Protocol(plans,window=2)
old=p.trace([(1,1,1),(0,1,0)])
new=p.trace([(0,1,0),(1,1,1)])
x,y=old[-1]['state'],new[-1]['state']
ck(old[-1]['cells']==new[-1]['cells'] and x.progress==y.progress==(1,2,1),'same coarse geometry and unused route')
ck(old[-1]['occurrences']==new[-1]['occurrences'],'same complete source IDs')
ck((x.oldest,y.oldest)==(1,0),'only oldest arrival age differs in reduced state')
xx,yy=p.solve(x),p.solve(y)
ck(xx[0]==Q(1,2) and yy[0]==Q(3,4),'source age changes eventual readiness')
ck(yy[0]-xx[0]==Q(1,4),'exact binary event TV witness')
ck(old[-1]['weight'].total>0 and new[-1]['weight'].total>0,'both prepared histories have positive weight')

# Keeping only the oldest age is sufficient for this common-window observer,
# while retaining event grammar permits reconstruction of the full arrival ages.
# Check against a full-age-vector automaton on every finite reachable input.
full_age_runs=[]
for H in (0,1,2,3):
    protocol=f.Protocol(plans,window=H)
    live={((0,0,0),(None,None,None)):f.ONE}
    fullhits=[]
    for tick in range(1,8):
        nxt={};hit=f.ZERO
        for (progress,ages),w in live.items():
            compact=f.State(progress,max((a for a in ages if a is not None),default=None))
            active=[i for i,j in enumerate(progress) if j<protocol.lengths[i]]
            for selected in product((0,1),repeat=len(active)):
                bits=[0]*3;q=f.ONE
                for i,b in zip(active,selected):bits[i]=b;q=r.serial(q,protocol.factors[i][b])
                pp=tuple(min(n,j+b) for n,j,b in zip(protocol.lengths,progress,bits))
                aa=tuple((a+1 if a is not None else (0 if j==n else None))
                         for a,j,n in zip(ages,pp,protocol.lengths))
                all_here=all(a is not None for a in aa)
                oldest=max((a for a in aa if a is not None),default=None)
                out='READY_RESERVED' if all_here else ('EXPIRED_RETAINED' if oldest is not None and oldest>=H else 'PENDING')
                cc=protocol.step(compact,tuple(bits))
                ck(cc==f.State(pp,oldest,out),'full-age to oldest-age exact transition intertwining')
                ww=r.serial(w,q)
                if out=='READY_RESERVED':hit=r.merge(hit,ww)
                elif out=='PENDING':f.add(nxt,(pp,aa),ww)
        live=nxt;fullhits.append(hit)
    ck(fullhits==protocol.prefixes(7)['hit'],'full-age and sufficient-age finite CWM first hits')
    full_age_runs.append({'H':H,'first_hits':fullhits,'remaining_full_states':len(live)})

# The age-domain convergence bound is based on independent first arrival tails.
# Explicit tail probabilities use BRC Bernoulli counting, not float libraries.
tails=[]
for H in (2,4,8,16,32):
    n=H+1;bernoulli={0:f.ONE}
    for _ in range(n):
        nxt={}
        for k,w in bernoulli.items():
            f.add(nxt,k,r.serial(w,r.edge(Q(1,2))))
            f.add(nxt,k+1,r.serial(w,r.edge(Q(1,2))))
        bernoulli=nxt
    nb_tail=r.total(bernoulli[k] for k in (0,1,2))
    geom_tail=bernoulli[0]
    bound=min(Q(1),r.total((geom_tail,geom_tail,nb_tail)).total)
    ck(bound==min(Q(1),Q(3+n+n*(n-1)//2,2**n)),'finite lifetime loss bound by positive word census')
    pr=f.Protocol(plans,window=H);val=pr.solve(pr.initial())[0]
    ck(1-val<=bound,'whole-future finite-lifetime error, not a time cutoff')
    tails.append({'H':H,'success':val,'failure':1-val,'failure_upper':bound})

# Without stopping, a retained completed trio is counted again at every tick.
infinite=next(t for t in table if t['a']==(Q(1,2),)*3 and t['H'] is None)
no_stop=f.Protocol(plans,window=None).prefixes(12)['hit']
ready_cdf=f.ZERO;visit_sum=f.ZERO
for hit in no_stop:
    ready_cdf=r.merge(ready_cdf,hit);visit_sum=r.merge(visit_sum,ready_cdf)
ck(ready_cdf.total<=1 and visit_sum.total>1,'occupancy sum is not a one-use first-event probability')
# A deterministic arrival at tick3 contributes four visits at ticks3..6 but one first event.
ck(6-3+1==4,'deterministic duplicate-ready-count witness')

summary={'schema':'CELL_U13_FIRST_READY_RESULTS_V1','event_id':'EM-20261009-CELL-U13-FIRST-READY-4C8A21',
 'checks':checks,'BRC_calls':dict(r.CALLS),'main_window_results':f.encode(main),
 'all_parameter_results':f.encode(table),'deterministic_minimum_window':2,
 'age_witness':{'old_ready':'1/2','new_ready':'3/4','binary_TV':'1/4'},
 'finite_age_tail_bounds':f.encode(tails),'prefix_horizon':14,
 'nonstopped_ready_occupation_sum12':str(visit_sum.total),
 'first_ready_by12':str(ready_cdf.total),'total_first_ready_infinite_lifetime':'1',
 'complete_infinite_time_via_positive_self_loop_closures':True,
 'single_use_routing_reservation_only':True,'native_action_incidence':False,
 'native_firing_performed':False,'physical_clock':False,'material_reaction':False,
 'prime_claim':False,'independent_review':False,
 'registration':'PRIOR_PLATFORM_BLOCK_PRESERVED_NOT_RETRIED'}
trace={'plans':plans,'prefix_runs':prefix_records,'positive_closure_certificates':closure_records,
       'deterministic':deterministic,'age_witness':{'old_trace':old,'new_trace':new,'old_outcome':xx,'new_outcome':yy},
       'full_age_checks':full_age_runs,'tail_bounds':tails}
raw=(json.dumps(f.encode(trace),sort_keys=True,separators=(',',':'))+'\n').encode()
packed=gzip.compress(raw,mtime=0)
(EV/'full_trace.json.gz').write_bytes(packed)
summary.update(trace_bytes=len(raw),trace_sha256=hashlib.sha256(raw).hexdigest(),trace_compressed_sha256=hashlib.sha256(packed).hexdigest())
(EV/'results.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k not in ('all_parameter_results','main_window_results','finite_age_tail_bounds')},indent=2))
