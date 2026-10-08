#!/usr/bin/env python3
"""U12 exact finite BRC certificates, NOT a native force validation."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product,permutations
from dataclasses import replace
import json,gzip,hashlib
import synchronized_events as s
r,u,m,v=s.r,s.u,s.m,s.v
ROOT=Path(__file__).resolve().parent;EV=ROOT/'evidence';EV.mkdir(exist_ok=True)
checks=0

def ck(value,label):
    global checks
    checks+=1
    if not value:raise AssertionError((checks,label))

z=r.ZERO;e1=r.direction(0);e2=r.direction(2);e3=r.direction(4)
square=(z,e1,s.add(e1,e2),e2)
base=m.from_tree(square,((0,1),(1,2),(2,3)))
params=((Q(1,48),Q(0)),(Q(1,48),Q(1,48)),(Q(1,60),Q(1,120)))
kernels=[s.ClockKernel(*p) for p in params]
finite=[];paired=[]
for k in kernels:
    layers=k.full_layers(4)
    for n,layer in enumerate(layers):
        ck(r.total(layer.values())==k.series.depth(n),'full timed word mass/count/dominant')
        for pos,weight in layer.items():
            ck(k.endpoint(n,pos)==weight,'endpoint recurrence preserves exactly one endpoint')
            if not k.eta:ck(s.parity(pos)==n%2,'moving-only clock parity')
    for n in range(4):
        for disp in (z,e1,e2,s.add(e1,e2),s.add(e1,e1),s.add(s.add(e1,e2),e3)):
            translated={s.add(x,disp):w for x,w in layers[n].items()}
            join=s.pair_join(layers[n],translated)
            ck(join==k.endpoint(2*n,disp),'equal-time pair equals one midpoint split')
            paired.append({'lambda':k.lam,'eta':k.eta,'n':n,'r':disp,'join':join})
    finite.append({'lambda':k.lam,'eta':k.eta,'layers':layers})

# Enumerate timed words, retaining waits as events but not spatial directions.
timing=[]
k=kernels[1]
for n in range(4):
    total=s.ZERO
    for word in product((None,)+tuple(r.PORTS),repeat=n):
        sig=s.Signal('single','CANDIDATE',z,word)
        trace=s.signal_trace(sig);waits=word.count(None);pos=trace[-1]['cell']
        ck(s.parity(pos)==(n-waits)%2,'holding count participates in clock parity')
        weight=k.witness_weight((word,));total=r.merge(total,weight)
    ck(total==k.series.depth(n),'explicit timed grammar BRC census')
    timing.append({'ticks':n,'all_words':total})

# Joint shared-clock normalization: N one-step histories uniquely generate
# common meeting and all anchored source coordinates. This is not pairwise
# independently chosen clocks. All origins, including co-origin, are counted.
normalizers=[]
for N in (2,3):
    byconfig={};gated=s.ZERO;total=s.ZERO
    for pp in product((None,)+tuple(r.PORTS),repeat=N):
        dd=[z if p is None else r.direction(p) for p in pp]
        meeting=dd[0];origins=tuple(s.difference(meeting,d) for d in dd)
        weight=k.witness_weight(tuple((p,) for p in pp))
        for origin,d in zip(origins,dd):ck(s.add(origin,d)==meeting,'one common event Cell')
        ck(origins[0]==z,'only a relative-coordinate chart anchor')
        s.put(byconfig,origins,weight);total=r.merge(total,weight)
        if N==3 and all(p is not None for p in pp) and len({r.axis(p) for p in pp})==3:
            gated=r.merge(gated,weight)
    want=s.ONE
    for _ in range(N):want=r.serial(want,k.step)
    ck(total==want,'complete all-relative shared-time coefficient')
    if N==3:
        expected=r.total(m.Weights(k.lam).power(3) for _ in range(960))
        ck(gated==expected,'960 ordered signed DISTINCT-AXIS candidates, not native admissions')
    normalizers.append({'N':N,'total':total,'gated':gated,'by_configuration':byconfig})

# Exact all-clock comparison closures; these are positive population sums,
# not repeated firings of the same physical input occurrence.
shared_clock=[]
for kk in kernels[:2]:
    powers=s.ONE
    for N in range(1,5):
        powers=r.serial(powers,kk.step)
        if N<2:continue
        r.CALLS['one_state_recurrent_cwm']+=1
        closure=r.brc.one_state_recurrent_cwm([powers.total])
        ck(closure.total_mass_closure==1/(1-kk.s**N),'all-clock common-rendezvous normalization')
        entry={'eta':kk.eta,'N':N,'unexcluded_total':closure.total_mass_closure}
        if N==3:
            factor=r.total(m.Weights(kk.lam).power(3) for _ in range(960))
            upper=r.serial(factor,r.edge(closure.total_mass_closure))
            ck(upper.total==960*kk.lam**3/(1-kk.s**3),'all-clock fresh-three-axis total')
            entry['fresh_distinct_axis_total']=upper
        shared_clock.append(entry)

# The original square has both parity classes. No moving-only common-clock
# pair can cross this cut, and every tree must cross it.
nohold,lazy=kernels[:2]
original=u.Overlap()
ck(original.k(8,e1).total>0,'U8 static overlap of neighbors is positive')
ck(nohold.pair_interval(12,e1)==(Q(0),Q(0)),'all-time nearest neighbor synchronous zero')
for T in u.trees(4):
    ck(any(s.parity(square[i])!=s.parity(square[j]) for i,j in T),'every tree crosses source parity cut')
no_score=s.tree_score_interval(square,nohold,8)
ck(no_score['lower'].total==no_score['upper'].total==0,'zero is exact, not numerical truncation')
lazy_score=s.tree_score_interval(square,lazy,12)
ck(lazy_score['lower'].total>0,'explicit holdings remove this candidate parity obstruction')
links=[]
for disp in (z,e1,s.add(e1,e2),s.add(e1,e1)):
    bounds=[lazy.pair_interval(h,disp) for h in (6,8,10,12)]
    for (a,b),(aa,bb) in zip(bounds,bounds[1:]):
        ck(a<=aa<=bb<=b,'nested whole-infinite-clock pair intervals')
    links.append({'r':disp,'intervals':bounds})
ck(nohold.total_pair_mass()==Q(16,15),'moving-only all-space pair sum')
ck(lazy.total_pair_mass()==Q(2304,2135),'holding all-space pair sum')

# True triple coincidence and the stronger fresh-three-axis routing gate.
# Three square corners have mixed parity; without holding all common-clock
# joins vanish. With holding, co-location may precede a fresh-port meeting.
triple=[]
starts=(z,e1,e2)
for kernel in kernels[:2]:
    layers=[kernel.full_layers(3,x) for x in starts]
    for n in range(1,4):
        plain=s.triple_join([ll[n] for ll in layers])
        candidate,rows=s.port_gate([kernel.arrivals(ll[n-1]) for ll in layers])
        ck(candidate.total<=plain.total,'fresh different-axis gate only restricts the population')
        if kernel.eta==0:ck(plain.total==candidate.total==0,'all tested parity-mixed triple clocks blocked')
        if kernel.eta and n==1:ck(plain.total>0 and candidate.total==0,'co-location is not three fresh arrivals')
        if kernel.eta and n==2:ck(candidate.total>0,'a sourced waiting/route schedule creates candidates')
        triple.append({'lambda':kernel.lam,'eta':kernel.eta,'ticks':n,
                       'plain':plain,'routing_candidates':candidate,'port_rows':rows})

# Original-square leaf moves outward along E3. Resource delivery goes via E4;
# separate support arrives via E5. A complete source ledger is retained.
prep=s.prefix_preparation(base)
ck(prep['gate']['routing_ready'] and not prep['native_commit_performed'],'routing proof does not manufacture native event')
ck(prep['conditional_after'].state==m.material(base,0,4,True),'conditional data update is inherited U9 prefix')
ck(prep['candidate_history_weight'].total==Q(1,48**9),'five spatial moves plus four weighted holds')
ck(prep['support_after']['current_cell']==r.advance(z,4),'third source not reset to its old location')
ck(prep['support_after']['source']!=prep['support_after']['current_cell'],'source side effect is nontrivial')
for trace in prep['gate']['traces']:
    for aa,bb in zip(trace,trace[1:]):
        dd=sum(abs(x-y) for x,y in zip(aa['cell'],bb['cell']))
        ck(dd==(0 if bb['port'] is None else 1),'one allowed native hop or distinct hold event per tick')
ck(len({sig.identity for sig in prep['signals']})==3,'independent occurrence lineage')
for frame in prep['frames']:
    free,held,bound=map(set,(frame['record_free'],frame['record_held'],frame['record_bound']))
    ck(not(free&held or held&bound or bound&free),'record allocation disjoint in every delivery phase')
    ck(free|held|bound==set(range(prep['before'].B)),'all existing record identities conserved')
    ck(frame['support_reserved'] and not frame['native_event_fired'],'third source held rather than reset or fired')
ck(prep['frames'][-1]['prefix_head_unmatched'],'event-ready is not a falsely committed U11 state')
# Direct co-carry has two identical last axes and fails this canonical gate.
p,q,t=4,6,8;x=z;y=r.advance(x,p);c0=r.advance(y,t^1)
direct=(s.Signal('a','A',x,(p,)),s.Signal('r','R',x,(p,)),s.Signal('c','C',c0,(t,)))
bad=s.prepare_gate(direct)
ck(not bad['routing_ready'] and 'CANONICAL_DISTINCT_AXIS_PRECONDITION' in bad['reasons'],'co-carried tokens are not different-axis actions')
try:s.prepare_gate((direct[0],replace(direct[1],identity='a'),direct[2]))
except ValueError:ck(True,'same occurrence cannot provide two action roles')
else:ck(False,'duplicate occurrence accepted')
try:s.prepare_gate(direct[:2])
except ValueError:ck(True,'third source cannot be invented')
else:ck(False,'missing third source accepted')
ck(not s.prepare_gate((prep['signals'][0],prep['signals'][1],replace(prep['signals'][2],launch=1)))['routing_ready'],
   'source clock belongs to event qualification')

# Least spatial work: final port q != axis(p) implies a resource prefix from
# x to y-d(q) of L1 length2, followed by one last edge. Check all signed cases
# and all native words of length <=3 for a fixed outward step.
shortest=[]
for p in r.PORTS:
    for q in r.PORTS:
        if r.axis(p)==r.axis(q):continue
        yy=r.direction(p);pre=r.advance(yy,q^1)
        ck(sum(abs(a) for a in pre)==2,'different-axis final-edge prefix distance lower bound')
        word=(q^1,p,q)
        ck(m.endpoint(z,word)==yy,'three-move constructive detour')
        ck(all(m.endpoint(z,word[:j])!=yy for j in (1,2)),'chosen detour does not arrive early')
        shortest.append({'move_port':p,'arrival_port':q,'resource_word':word})
# All 12^n words for n<=3, gate by source end and last port. Count via BRC.
bylength={}
for n in range(1,4):
    val=s.ZERO
    for word in product(r.PORTS,repeat=n):
        if m.endpoint(z,word)==r.direction(4) and r.axis(word[-1])!=2:
            val=r.merge(val,m.Weights().power(n))
    bylength[n]=val
ck(bylength[1].count==bylength[2].count==0 and bylength[3].count>0,'no shorter resource redirection exists')
# Direct material + independent neighboring support cost at least one each.
ck(1+3+1==prep['spatial_moves'],'sharp five-hop minimum under the declared route readout')

# Epoch offsets remove the MUST-MOVE parity obstruction without changing space.
# Both sources now have fresh final arrivals at global tick2, distinct axes.
epoch=(s.Signal('source0','CANDIDATE',z,(2,0),launch=0),
       s.Signal('source1','CANDIDATE',e1,(2,),launch=1))
ea,eb=[s.signal_trace(a)[-1] for a in epoch]
ck(ea['tick']==eb['tick'] and ea['cell']==eb['cell'],'launch epoch difference restores pair meeting')
ck((s.parity(epoch[0].source_cell)-epoch[0].launch)%2==(s.parity(epoch[1].source_cell)-epoch[1].launch)%2,
   'corrected source-clock parity invariant')

summary={'schema':'CELL_U12_SYNCHRONOUS_ROUTING_RESULTS_V1',
 'event_id':'EM-20261008-CELL-U12-SYNCHRONOUS-ROUTING-93F4C2',
 'checks':checks,'BRC_calls':dict(r.CALLS),'source_kernel':'UNCHANGED_U11_U9_U8_U2_BRC',
 'new_results':['common_clock_parity_and_epoch_holding_invariant',
                'static_overlap_not_synchronous_coincidence',
                'positive_joint_rendezvous_normalizer_and_tail',
                'original_square_must_move_synchronous_tree_score_exact_zero',
                'holding_and_fresh_arrival_are_distinct_operations',
                'explicit_third_source_prefix_route_with_sharp_five_hop_three_tick_bound'],
 'pair_nohold_allspace':'16/15','pair_hold_allspace':'2304/2135',
 'shared_clock_totals':s.encode(shared_clock),'pair_link_intervals':s.encode(links),'original_square_hold_pair_tree_score':s.encode(lazy_score),
 'triple_counts':s.encode([{k:a[k] for k in ('eta','ticks','plain','routing_candidates')} for a in triple]),
 'prefix_route':{'ticks':prep['ticks'],'spatial_moves':prep['spatial_moves'],'holds':prep['waits'],
                 'weight':str(prep['candidate_history_weight'].total),'native_fired':False},
 'short_word_candidate_counts':{str(n):val.count for n,val in bylength.items()},
 'signed_detour_cases':len(shortest),'native_closure_certified':False,'force_to_motion_map':False,
 'physical_time_calibrated':False,'native_physics':False,'prime_claim':False,
 'registration':'PENDING_PRIOR_PLATFORM_BLOCK_PRESERVED_NO_RETRY',
 'independent_review':False,'finite_clock_horizon_is_dynamic_cutoff':False}
trace={'finite_layers':finite,'midpoint_checks':paired,'timed_word_census':timing,
       'one_clock_normalizers':normalizers,'shared_clock_totals':shared_clock,'pair_links':links,'square_nohold':no_score,
       'square_hold':lazy_score,'triples':triple,'prefix':prep,'direct_gate':bad,
       'minimal_routes':shortest,'epoch_witness':epoch}
raw=(json.dumps(s.encode(trace),sort_keys=True,separators=(',',':'))+'\n').encode()
packed=gzip.compress(raw,mtime=0)
(EV/'full_trace.json.gz').write_bytes(packed)
summary.update(trace_bytes=len(raw),trace_sha256=hashlib.sha256(raw).hexdigest(),
               trace_compressed_sha256=hashlib.sha256(packed).hexdigest())
(EV/'results.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k not in ('pair_link_intervals','original_square_hold_pair_tree_score')},indent=2))
