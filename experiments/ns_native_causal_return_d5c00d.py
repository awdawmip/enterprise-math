#!/usr/bin/env python3
"""Exact finite causal-return checks for the unchanged X6 density-port law.

Candidate count dynamics only: no primitive-force, energy, viscosity or NS claim.
Uses the two published parent programs unchanged. Event vetoes are explicitly
marked counterfactual diagnostics; the main trajectories have no external input.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations
import json
from pathlib import Path
import ns_native_density_port_d5c00d as P

EVENT = 'NS-NATIVE-CAUSAL-RETURN-20260909-D5C00D-14'
SOURCE = 'd40aa672623d6fc82af4cbb60964e6a628267e62'
PARENTS = {
    'ns_native_density_port_d5c00d.py': '207bf471fea265bc5f9c6cb1c68c3e44ee9a515a0a91025ae638281f5f34d56e',
    'ns_native_ternary_coherence_d5c00d.py': '468b24f1299949ad634c34a87224f2e43df851a42fe48adce63fe1324306aa33',
}
ALL = frozenset(map(frozenset, combinations(range(6), 3)))
G9 = frozenset(frozenset(x-1 for x in t) for t in (
    (1,2,3),(1,2,4),(1,2,5),(1,2,6),(1,3,4),
    (1,3,5),(2,5,6),(3,4,6),(4,5,6)))

def e(i: int, s: int=1) -> P.Vec:
    return P.unit(i-1,s)

def ch(i: int, s: int=1) -> int:
    return 2*(i-1)+int(s==1)

def scale(n: int,v: P.Vec) -> P.Vec:
    return tuple(n*x for x in v)

def sub(a: P.Vec,b: P.Vec) -> P.Vec:
    return tuple(x-y for x,y in zip(a,b))

def put(field: dict, z: P.Vec, v: int) -> None:
    row=list(field.get(z,P.EMPTY));row[v]+=1;field[z]=tuple(row)

def seed(n: int=9) -> P.Field:
    if n not in (6,9): raise ValueError('The frozen witness uses six or nine packets')
    field={}
    for v in (ch(1),ch(2),ch(2,-1)): put(field,P.ZERO,v)
    for z,v in ((e(4,-1),ch(4)),(e(3,-1),ch(3)),(e(3),ch(3,-1))):
        put(field,z,v)
    if n==9:
        y=P.add(e(1),e(5))
        for v in (ch(6),ch(2),ch(2,-1)):
            put(field,sub(y,scale(2,P.DIRS[v])),v)
    return field

def step(field: P.Field, gamma=ALL, veto=frozenset()) -> tuple[P.Field,list]:
    """Preserve the parent gate; only the explicit incidence/veto can reject it."""
    mid,raw=P.collision(field,P.EMPTY)
    accepted=[]
    for z,event,scores in raw:
        j,s,l,m=event
        if frozenset((j,l,m)) in gamma and z not in veto:
            accepted.append((z,event,scores))
        else:
            old=field.get(z,P.EMPTY)
            if any(old):mid[z]=old
            else:mid.pop(z,None)
    out=P.stream(mid);P.validate(out,P.EMPTY)
    return out,accepted

def distance(a: P.Field,b: P.Field) -> int:
    return sum(sum(abs(x-y) for x,y in zip(a.get(z,P.EMPTY),b.get(z,P.EMPTY)))
               for z in a.keys()|b.keys())

def color_inventory(field: P.Field,t: int) -> tuple[int,int]:
    out=[0,0]
    for z,c in field.items():out[(sum(z)+t)%2]+=sum(c)
    return tuple(out)

def rows(field: P.Field) -> list:
    return [[list(z),list(c)] for z,c in sorted(field.items())]

def encode_event(x) -> dict:
    z,(j,s,l,m),scores=x
    return {'cell':list(z),'spectator_axis':j+1,'spectator_sign':s,
            'old_pair_axis':l+1,'new_pair_axis':m+1,'scores':list(scores)}

def run(field: P.Field, ticks: int, gamma=ALL, veto_tick: int | None=None):
    st=field;states=[st];events=[];invariant=P.invariants(st)
    inventory=color_inventory(st,0)
    for t in range(ticks):
        st,ev=step(st,gamma,frozenset({P.ZERO}) if t==veto_tick else frozenset())
        assert P.invariants(st)==invariant
        assert color_inventory(st,t+1)==inventory
        assert max((max(c) for c in st.values()),default=0)<=1
        states.append(st);events.append(ev)
    return states,events

def candidate_meeting(slots) -> Fraction | None:
    """Exact all-future three-line intersection, not a finite-time simulation."""
    z0,v0=slots[0];answer=None
    for z,v in slots[1:]:
        for a,b,c,d in zip(z0,P.DIRS[v0],z,P.DIRS[v]):
            denom=b-d;num=c-a
            if not denom:
                if num:return None
            else:
                t=Fraction(num,denom)
                if answer is None:answer=t
                elif answer!=t:return None
    if answer is None:raise AssertionError('Three identical lines require repeated slots')
    return answer

def no_future_meeting(field: P.Field) -> dict:
    slots=[(z,v) for z,c in sorted(field.items()) for v,n in enumerate(c) for _ in range(n)]
    possible=[];checked=0
    for triple in combinations(slots,3):
        t=candidate_meeting(triple);checked+=1
        if t is not None and t>=0 and t.denominator==1:
            possible.append({'after_ticks':int(t),'slots':triple})
    assert not possible, possible
    return {'triples_checked':checked,'future_integer_three_line_meetings':0,
            'scope':'All future ticks from this post-collision state; absence proves no later collision.'}

def link_connected(gamma,j):
    unseen=set(range(6))-{j};seen={min(unseen)}
    while True:
        nxt=seen|{b for a in seen for b in unseen if frozenset((j,a,b)) in gamma}
        if nxt==seen:return len(seen)==5
        seen=nxt

def feedback_checks() -> dict:
    out={}
    for count in (6,9):
        initial=seed(count);actual,ev=run(initial,8)
        ctl0,ec0=run(initial,8,veto_tick=0)
        ctl1,ec1=run(initial,8,veto_tick=1)
        expected=[(0,1,1,2),(3,1,2,0)]+([(5,1,1,4)] if count==9 else [])
        assert [x[1] for es in ev for x in es]==expected
        assert all(len(ev[t])==1 for t in range(len(expected)))
        assert all(not es for es in ev[len(expected):])
        assert actual[1][P.ZERO]==ctl0[1][P.ZERO] # middle core unchanged
        assert ev[1][0][1]==(3,1,2,0) and ec0[1][0][1]==(3,1,2,1)
        if count==9:
            y=P.add(e(1),e(5))
            assert actual[2][y]==ctl1[2][y] # final core unchanged by middle veto
            assert not ec1[2] and not ec0[2]
            assert [distance(actual[t],ctl0[t]) for t in range(4)]==[0,4,8,12]
            assert [distance(actual[t],ctl1[t]) for t in range(4)]==[0,0,4,8]
        out[str(count)]={
            'initial':rows(initial),'color_populations':list(color_inventory(initial,0)),
            'events':[[encode_event(x) for x in es] for es in ev],
            'first_veto_events':[[encode_event(x) for x in es] for es in ec0],
            'middle_veto_events':[[encode_event(x) for x in es] for es in ec1],
            'distance_first_veto':[distance(actual[t],ctl0[t]) for t in range(9)],
            'distance_middle_veto':[distance(actual[t],ctl1[t]) for t in range(9)],
            'post_last_state':rows(actual[len(expected)]),
            'all_future_no_collision':no_future_meeting(actual[len(expected)]),
        }
    # Transport an independently supplied relation rather than freeze a chart.
    initial=seed();reference,events=run(initial,3,G9)
    assert all(len(es)==1 for es in events)
    assert all(link_connected(G9,j) for j in range(6))
    return out

def symmetry_checks() -> dict:
    count=0;initial=seed();ref,refev=run(initial,3,G9)
    for perm in permutations(range(6)):
        gam=frozenset(frozenset(perm[i] for i in t) for t in G9)
        inp=P.transformed_field(perm,initial)
        states,events=run(inp,3,gam)
        for t in range(4):
            assert states[t]==P.transformed_field(perm,ref[t])
        for tick,es in enumerate(events):
            expected={(P.act_vec(perm,z),(perm[j],s,perm[l],perm[m]))
                      for z,(j,s,l,m),_ in refev[tick]}
            assert {(z,ev) for z,ev,_ in es}==expected
        count+=1
    for delta in ((5,-2,1,0,-4,3),(-2,0,1,4,0,-1)):
        inp={P.add(z,delta):v for z,v in initial.items()}
        st=inp
        for t in range(3):
            st,es=step(st,G9)
            assert st=={P.add(z,delta):v for z,v in ref[t+1].items()}
    rev={tuple(-x for x in z):tuple(c[v^1] for v in range(12)) for z,c in initial.items()}
    st=rev
    for t in range(3):
        st,es=step(st,G9)
        expected={tuple(-x for x in z):tuple(c[v^1] for v in range(12)) for z,c in ref[t+1].items()}
        assert st==expected
    return {'S6_full_three_tick_checks':count,'translations':2,'global_reversal':1}

def normalized_eight_checks(max_first=4,max_last=8,start_first=1) -> dict:
    """Regression of the analytic <=8 impossibility, NOT its unbounded proof.

    Only potential first 0->second k->third l alternating sequences are generated.
    Two extra same-color packets must meet one first-event descendant at the third
    collision; this fixes their initial positions. Ordinary proof covers all k,l.
    """
    cfgs=[(j,s,l,P.C(j,s,l)) for j in range(6) for l in range(6) if l!=j for s in (-1,1)]
    core=P.config_counts(P.C(0,1,1));cases=0;valid=0;first_dep=0;full_dep=0
    timings=[]
    for k in range(start_first,max_first+1):
        patterns=[]
        for j,s,l,vs in cfgs:
            ys={P.add(P.unit(2,eps),scale(k,P.DIRS[v])) for eps in (-1,1) for v in vs}
            for y in ys:
                pos=[sub(y,scale(k,P.DIRS[v])) for v in vs]
                scores=tuple(sum(z==P.unit(i) or z==P.unit(i,-1) for z in pos) for i in range(6))
                _,e0=P.local_collision(core,scores)
                if e0 and e0[3]==2:patterns.append((vs,y,pos))
        for last in range(k+1,max_last+1):
            here=0
            for vs,y,pos in patterns:
                for w in (ch(1),ch(3),ch(3,-1)):
                    meet=scale(last,P.DIRS[w])
                    for j3,s3,l3,third in cfgs:
                        if w not in third:continue
                        field={P.ZERO:core}
                        for z,v in zip(pos,vs):put(field,z,v)
                        for v in third:
                            if v!=w:put(field,sub(meet,scale(last,P.DIRS[v])),v)
                        cases+=1
                        # The fast runner still invokes the unchanged local gate.
                        def quick(st,veto=frozenset()):
                            totals={z:sum(c) for z,c in st.items()};mid=dict(st);es=[]
                            for z,c in st.items():
                                if sum(c)!=3:continue
                                scores=tuple(totals.get(P.add(z,P.unit(i)),0)+totals.get(P.add(z,P.unit(i,-1)),0) for i in range(6))
                                q,evt=P.local_collision(c,scores)
                                if evt is not None and z not in veto:mid[z]=q;es.append((z,evt,scores))
                            return P.stream(mid),es
                        st=field;hist=[];evs=[];good=True
                        for t in range(last+1):
                            hist.append(st);st,es=quick(st);evs.append(es)
                            if t in (0,k,last):
                                target=P.ZERO if t==0 else y if t==k else meet
                                if len(es)!=1 or es[0][0]!=target:good=False;break
                                if t==0 and es[0][1]!=(0,1,1,2):good=False;break
                            elif es:good=False;break
                        if not good:continue
                        valid+=1;here+=1
                        ca,_=quick(field,frozenset({P.ZERO}))
                        for t in range(1,k+1):ca,ea=quick(ca)
                        if [e[1] for e in ea if e[0]==y]==[evs[k][0][1]]:continue
                        first_dep+=1
                        cb,_=quick(hist[k],frozenset({y}))
                        for t in range(k+1,last+1):cb,eb=quick(cb)
                        if [e[1] for e in eb if e[0]==meet]!=[evs[last][0][1]]:
                            full_dep+=1;raise AssertionError((k,last,rows(field)))
            timings.append({'middle_tick':k,'last_tick':last,'three_event_trajectories':here})
    return {'first_tick':0,'max_middle_tick':max_first,'max_last_tick':max_last,
            'prepared_states_checked':cases,'actual_three_event_trajectories':valid,
            'first_link_changes_output':first_dep,'two_links_change_output':full_dep,
            'timing_records':timings,'scope':'Bounded regression only; unbounded impossibility is proved separately.'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=Path('results_14.json'))
    ap.add_argument('--full-eight-regression',action='store_true');args=ap.parse_args()
    for name,h in PARENTS.items():assert sha256((Path(__file__).parent/name).read_bytes()).hexdigest()==h
    result={'schema':'EM_NATIVE_CAUSAL_RETURN_RESULTS_V1','event_id':EVENT,'source_snapshot':SOURCE,
            'status':'ORDINARY_PROOFS_AND_EXACT_CHECKS_NOT_FORCE_OR_NS',
            'parent_sha256':PARENTS,'witnesses':feedback_checks(),'symmetry':symmetry_checks(),
            'g9':[sorted(i+1 for i in t) for t in sorted(G9,key=lambda t:tuple(sorted(t)))],
            'theorems':{'fewest_packets_for_two_events':6,
                        'fewest_for_first_three_alternating_causally_linked_events':9},
            'scope':['Fixed candidate law; all packets stream one signed unit step.',
                     'Event interventions are diagnostics, not inputs to actual trajectories.',
                     'No primitive force certification, viscosity, physical f=0 or NS conclusion.',
                     'Finite causal return is not perpetual feedback or unbounded growth.',
                     'No independent review, Lean build or historical-priority claim.']}
    if args.full_eight_regression:result['eight_regression']=normalized_eight_checks()
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'event_id':EVENT,'witness6_events':2,'witness9_events':3,
        'S6_checks':result['symmetry']['S6_full_three_tick_checks'],
        'eight_regression':{k:v for k,v in result.get('eight_regression',{}).items() if k!='timing_records'}},ensure_ascii=False))

if __name__=='__main__':main()
