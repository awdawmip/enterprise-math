#!/usr/bin/env python3
"""Exact source-race and causal one-body tests; conditional, same-author."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from dataclasses import replace
import json,gzip,hashlib
import direction_race as d
f,r,m,v,u=d.f,d.r,d.m,d.v,d.u
ROOT=Path(__file__).resolve().parent
checks=0

def ck(x,label):
    global checks
    checks+=1
    if not x:raise AssertionError((checks,label))

def joined_prefix(race,h):
    """A second positive construction from independent stopped channel curves."""
    aa,bb=(c.prefixes(h) for c in race.channels)
    expired=[d.ZERO,d.ZERO];ans=[]
    for t in range(h):
        ea,eb=aa['expired'][t],bb['expired'][t]
        no=r.total((r.serial(ea,expired[1]),r.serial(eb,expired[0]),r.serial(ea,eb)))
        expired[0]=r.merge(expired[0],ea);expired[1]=r.merge(expired[1],eb)
        a=r.serial(aa['hit'][t],r.merge(expired[1],bb['survival'][t]))
        b=r.serial(bb['hit'][t],r.merge(expired[0],aa['survival'][t]))
        tie=r.serial(aa['hit'][t],bb['hit'][t])
        ans.append((a,b,tie,no))
    return ans

runs=[];certificates=[]
# Whole-future result by finite monotone-state positive self-loop closure.
for long,W in ((1,None),(1,0),(1,2),(3,None),(3,0),(3,1),(3,2),(3,4)):
    race=d.standard_race(long,W)
    raw=race.solve(race.initial);law=race.law()
    ck(sum(law)==1 and all(q>=0 for q in law),'all outcomes including no move retained')
    singles=[c.solve(c.initial())[0] for c in race.channels]
    no=r.serial(f.lift(1-singles[0]),f.lift(1-singles[1])).total
    ck(raw[3]==no,'two invalid cohorts cause no move, not renormalized away')
    for state,loop,values in tuple(race.records):
        got=[d.ZERO]*4
        for bits,y,q in race.row(state):
            for i,z in enumerate(race.solve(y)):got[i]=r.merge(got[i],r.serial(q,f.lift(z)))
        ck(tuple(x.total for x in got)==values,'all-time first-step equation')
    prefix=race.prefixes(6);direct=joined_prefix(race,6)
    ck(prefix['hits']==direct,'exact finite count,total,dominant first-choice decomposition')
    cumulative=[d.ZERO]*4
    for hits in prefix['hits']:
        for i,w in enumerate(hits):cumulative[i]=r.merge(cumulative[i],w)
    live=r.total(prefix['live'].values()).total
    ck(sum(w.total for w in cumulative)+live==1,'first-choice/live conservation')
    for i,z in enumerate(raw):ck(cumulative[i].total<=z<=cumulative[i].total+live,'certified finite remainder')
    if long==1:ck(law[0]==law[1]==(1-no)/2,'mirror-equal preparation gives equal directions')
    row={'support_length_minus':long,'effective_window':W,'protocol_window_H':None if W is None else W+8,
         'source_successes':tuple(map(str,singles)),'strict_plus_minus_tie_none':tuple(map(str,raw)),
         'position_law_plus_minus_wait':tuple(map(str,law)),'mean_signed_step':str(law[0]-law[1]),
         'transient_state_count':len(race.records),'prefix_horizon':6,'prefix_remaining_weight':str(live)}
    runs.append(row)
    certificates.append({'input':row,'all_time_states':race.records,'prefix':prefix,'joined':direct})

byW={a['effective_window']:a for a in runs if a['support_length_minus']==3}
P=lambda W:tuple(Q(a) for a in byW[W]['position_law_plus_minus_wait'])
ck(P(None)[0]>P(None)[1],'unlimited storage favors shorter supporting route')
ck(P(0)[0]<P(0)[1] and P(1)[0]<P(1)[1],'tight deadline reverses direction')
for W,winning in ((None,0),(0,1),(1,1),(2,0),(4,0)):
    strict=tuple(Q(x) for x in byW[W]['strict_plus_minus_tie_none'])
    ck(strict[winning]>strict[1-winning]+strict[2],'bias sign survives ANY tie allocation')
ck(P(2)[0]>P(2)[1] and P(4)[0]>P(4)[1],'larger finite window restores shorter-side bias')
ck(byW[0]['source_successes']==('1/343','97/16807'),'exact isolated fresh-ready comparison')
ck(P(0)==(Q(5943876335,2042434405494),Q(11764092079,2042434405494),Q(5714820,5764801)),
   'frozen exact full competition result')

# Positive all-time short/long fresh formulas. z=(1/2)^3; no differentiation.
a=Q(1,2);z=Q(1,8)
r.CALLS['one_state_recurrent_cwm']+=1
geom=r.edge(r.brc.one_state_recurrent_cwm([z]).total_mass_closure)
poly=r.total((d.ONE,r.total(r.edge(z) for _ in range(4)),r.serial(r.edge(z),r.edge(z))))
weight=r.edge(Q(1,512))
for _ in range(5):weight=r.serial(weight,geom)
longfresh=r.serial(weight,poly)
ck(longfresh.total==Q(97,16807),'squared binomial positive rational series')

# Same model with directions interchanged and asymmetric advancement rates.
for W in (0,None):
    base=d.standard_race(3,W)
    a,b=base.channels
    reverse=d.Race(b.plans,a.plans,W)
    x=base.law();y=reverse.law()
    ck(y==(x[1],x[0],x[2]),'channel renaming covariance')
probs=(Q(1,2),Q(2,3),Q(1,3),Q(2,3),Q(1,2),Q(2,3))
p=d.standard_race(3,0,probs);vals=p.law()
ck(sum(vals)==1,'heterogeneous positive source rates')
try:d.Race(p.channels[0].plans,p.channels[0].plans)
except ValueError:ck(True,'duplicated channel sources rejected')
else:ck(False,'source occurrence duplicated')

# Execute both fair tie branches and strict/failed candidate cases.
examples=[]
for arrival_pair,H in ((((1,3,1),(3,3,3)),8),(((1,3,1),(3,3,3)),10),
                       (((1,3,1),(1,3,3)),8),(((2,3,1),(4,5,4)),None),
                       (((3,4,3),(1,3,3)),10)):
    for tie in (0,1):
        tr=d.material_trace(arrival_pair,H,tie);examples.append(tr)
        ck(tr['body_move_count'] in (0,1),'one original material occurrence only')
        n=tr['body_before'].length();allids=set(tr['resource_ids'])
        ck(len(allids)==n+2,'one shared old field plus TWO distinct record resources')
        for frame in tr['frames']:
            free,held,bound=map(set,(frame['free'],frame['held'],frame['bound']))
            ck(not(free&held or free&bound or held&bound) and free|held|bound==allids,'global ownership partition')
            ck(set(frame['record_locations'])==allids,'every identified record has an actual location')
            ck(len(set(frame['body_cells']))==4,'no material collisions')
            ck(frame['body_cells'][1:]==tr['body_before'].cells[1:],'other material identities fixed')
            ck(not frame['native_firing'],'calculated protocol is not a native-force certificate')
        win=tr['winner']
        if win is not None:
            rt=tr['return_ticks'][win]
            for frame in tr['frames']:
                before=frame['tick']<rt+2
                ck((frame['body_cells'][0]==tr['body_before'].cells[0])==before,'material waits for local receipt then moves')
            for aa,bb in zip(tr['frames'],tr['frames'][1:]):
                for identity,pos in aa['record_locations'].items():ck(sum(abs(a-b) for a,b in zip(pos,bb['record_locations'][identity]))<=1,'all bound/free record motion is local')
                for old,new in zip(aa['packet_cells'],bb['packet_cells']):
                    for x,y in zip(old,new):ck(sum(abs(a-b) for a,b in zip(x,y))<=1,'each resource/signal uses one native edge or waits')
            inv=tr['winner_inventory_before'];after=tr['winner_inventory_after']
            late=u.Ticket('late',0,inv.state.cells[0],r.advance(inv.state.cells[0],5 if win==0 else 4),
                          tuple(pl.identity for pl in tr['plans'][1-win]),True)
            unchanged,steps,used,status=d.one_body_apply(True,late,inv,5 if win==0 else 4,n)
            ck(unchanged==inv and not steps and used and status=='LATE_RETAINED','consumed occurrence blocks late ticket even after geometry is restored')
            ck(len(tr['winner_local_inverse'])==3,'actual source-pinned three-stage reverse')
            ck(v.validate(after)is None,'valid inherited material/path state')
        else:ck(tr['body_after']==tr['body_before'],'all-ineligible inputs wait')
# Same preparation/clock, two choices occur only at a local tie.
a=d.material_trace(((3,3,3),(3,3,3)),8,0)
b=d.material_trace(((3,3,3),(3,3,3)),8,1)
ck(a['trial_weight']==b['trial_weight'],'symmetric tie retains equal joint weights')
ck(a['body_after'].cells[0]==r.direction(4) and b['body_after'].cells[0]==r.direction(5),'two actual opposite integer successors')
ck(a['frames'][:8]==b['frames'][:8],'no future tie choice in pre-receipt state')

# Whole native signed-axis covariance on generators; no 90-degree embedding.
transforms=[]
base=u.standard_body()
def transform(body,perm,flips):
    def port(p):return 2*perm[p//2]+((p%2)^flips[p//2])
    def cell(x):
        y=[0]*6
        for i,a in enumerate(x):y[perm[i]]=a*(-1 if flips[i] else 1)
        return tuple(y)
    return m.State(tuple(cell(x) for x in body.cells),tuple((i,j,tuple(map(port,a)),tuple(map(port,b))) for i,j,a,b in body.links)),port,cell
for i in range(6):
    flips=[0]*6;flips[i]=1;transforms.append((tuple(range(6)),tuple(flips)))
for i in range(5):
    perm=list(range(6));perm[i],perm[i+1]=perm[i+1],perm[i];transforms.append((tuple(perm),(0,)*6))
for perm,flips in transforms:
    bb,port,cell=transform(base,perm,flips)
    tr=d.material_trace(((3,3,3),(3,3,3)),8,0,bb,(port(4),port(5)),(1,3),port(6),port(8))
    ck(tr['body_after'].cells==tuple(cell(x) for x in a['body_after'].cells),'signed-axis transformed successor')
    ck(tr['trial_weight']==a['trial_weight'],'signed-axis transformation preserves BRC trial weight')

summary={'schema':'CELL_U17_DIRECTION_RACE_RESULTS_V1',
         'event_id':'EM-20261009-CELL-U17-DIRECTION-RACE-6F2B91',
         'checks':checks,'BRC_calls':dict(r.CALLS),'main_runs':runs,
         'executed_source_transcripts':len(examples)+2+len(transforms),
         'signed_axis_generators_checked':len(transforms),'exact_first_choice_prefix_horizon':6,
         'native_force':False,'native_triad_certificate':False,'mechanical_reaction':False,
         'physical_time':False,'prime_claim':False,'independent_review':False,
         'previous_checker_republished':False,'registration':'PRIOR_DENIAL_UNRESOLVED_NOT_RETRIED',
         'model':'two disjoint three-source cohorts (six sources total); first returned valid ticket; one body latch; fair tie',
         'main_new_result':'directional preference reverses between effective lifetime W=0,1 and W=2,infinity',
         'scope':'one externally prepared comparison with state-dependent local selection, not autonomous repeated material'}
trace={'all_time_certificates':certificates,'source_transcripts':examples,'tie_branches':[a,b]}
raw=(json.dumps(d.encode(trace),sort_keys=True,separators=(',',':'))+'\n').encode()
payload=gzip.compress(raw,mtime=0)
ev=ROOT/'evidence';ev.mkdir(exist_ok=True)
(ev/'full_trace.json.gz').write_bytes(payload)
summary.update(trace_bytes=len(raw),trace_sha256=hashlib.sha256(raw).hexdigest(),
               trace_compressed_sha256=hashlib.sha256(payload).hexdigest())
(ev/'results.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
