#!/usr/bin/env python3
"""Exact incidence-filter diagnostics on X6. Not a native force or NS solver.

Extends the frozen density-port candidate by vetoing non-admitted triples,
never by reselecting a different score winner. Imports the two parent files
unchanged. All arithmetic is integer/set arithmetic, no continuity assumption.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from itertools import combinations, permutations
from pathlib import Path
import ns_native_density_port_d5c00d as P

Triple = frozenset[int]
Gamma = frozenset[Triple]
ALL: Gamma = frozenset(map(frozenset, combinations(range(P.D), 3)))
FCC: Gamma = frozenset(map(frozenset, ((0,2,5),(0,3,4),(1,2,4),(1,3,5))))
SECOND: Gamma = frozenset(map(frozenset, ((0,1,2),(0,3,5),(1,4,5),(2,3,4))))
EIGHT: Gamma = FCC | SECOND

def encoded(gamma: Gamma) -> list[list[int]]:
    return sorted(sorted(x+1 for x in t) for t in gamma)

def act(gamma: Gamma, p: tuple[int,...]) -> Gamma:
    return frozenset(frozenset(p[x] for x in t) for t in gamma)

def neighbors(gamma: Gamma, j: int, l: int) -> set[int]:
    return {next(iter(t-{j,l})) for t in gamma if {j,l} <= t}

def link_components(gamma: Gamma, j: int) -> tuple[frozenset[int],...]:
    unseen=set(range(P.D))-{j}; parts=[]
    while unseen:
        found={min(unseen)}
        while True:
            new=found|set().union(*(neighbors(gamma,j,l) for l in found))
            if new==found: break
            found=new
        parts.append(frozenset(found));unseen-=found
    return tuple(parts)

def background(j: int, l: int) -> P.Counts:
    return P.config_counts(P.C(j,1,l))

def seed(j: int) -> P.Field:
    pos=[0]*P.NCH;neg=[0]*P.NCH
    pos[2*j+1]=1;neg[2*j+1]=-1
    return {P.ZERO:tuple(pos),P.unit(j):tuple(neg)}

def step(field: P.Field, bg: P.Counts, gamma: Gamma) -> tuple[P.Field,list,list]:
    """Run the unchanged scoring/eligibility; veto only. Streaming unchanged."""
    out, raw = P.collision(field,bg)
    allowed=[]; denied=[]
    for z,event,scores in raw:
        j,sign,old,new=event
        if frozenset((j,old,new)) in gamma:
            allowed.append((z,event,scores))
        else:
            denied.append((z,event,scores))
            original=field.get(z,P.EMPTY)
            if any(original): out[z]=original
            else: out.pop(z,None)
    result=P.stream(out);P.validate(result,bg)
    return result,allowed,denied

def front(wake:P.Field,age:int,j:int,l:int,ports:set[int],bg:P.Counts)->int:
    n=0
    for m in ports:
        for eps in (-1,1):
            for sig in (-1,1):
                z=P.add(P.unit(m,eps),tuple(sig*age if q==l else 0 for q in range(P.D)))
                v=2*l+int(sig==1)
                assert P.actual(wake,z,bg)[v]==0
                n+=1
    for z,v in wake.items():
        assert z[j]==0 and abs(z[l])<=age
        assert v[2*j]==v[2*j+1]==0
        if abs(z[l])==age:
            channel=2*l+int(z[l]>0)
            assert v[channel]==-1
            assert all(x==0 for q,x in enumerate(v) if q!=channel)
    assert P.invariants(wake)==(0,P.ZERO)
    assert P.norm(wake)>=8*len(ports)
    return n

def run_case(gamma:Gamma,j:int,l:int,steps:int)->dict:
    bg=background(j,l);init=seed(j);ports=neighbors(gamma,j,l)
    first,yes,no=step(init,bg,gamma)
    assert len(yes)==2*len(ports)
    assert P.norm(first)==2+8*len(ports)
    wake={z:d for z,d in first.items() if z[j]==0}
    wakes=[];age_norms=[];hole_checks=0
    for a in range(1,steps+1):
        if a>1: wake,_,_=step(wake,bg,gamma)
        hole_checks+=front(wake,a,j,l,ports,bg)
        wakes.append(wake);age_norms.append(P.norm(wake))
    full=init;records=[]
    comp=next(c for c in link_components(gamma,j) if l in c)
    allowed_coordinates=set(comp)|{j}
    ever_channels=set();ever_axes=set()
    for t in range(1,steps+1):
        full,yes,no=step(full,bg,gamma)
        expected={}
        for a,w in enumerate(wakes[:t],1):
            shift=tuple(t-a if q==j else 0 for q in range(P.D))
            for z,d in w.items():
                target=P.add(z,shift);assert target not in expected
                expected[target]=d
        po=[0]*P.NCH;ho=[0]*P.NCH;po[2*j+1]=1;ho[2*j+1]=-1
        expected[tuple(t if q==j else 0 for q in range(P.D))]=tuple(po)
        expected[tuple(t+1 if q==j else 0 for q in range(P.D))]=tuple(ho)
        assert full==expected
        assert P.invariants(full)==(0,P.ZERO)
        assert P.norm(full)==2+sum(age_norms[:t])>=8*len(ports)*t+2
        for z,d in full.items():
            assert all(z[q]==0 for q in range(P.D) if q not in allowed_coordinates)
            for q,x in enumerate(d):
                if x:
                    assert q//2 in allowed_coordinates
                    ever_channels.add(q//2+1)
            ever_axes.update(q+1 for q,x in enumerate(z) if x)
            assert max(P.actual(full,z,bg))<=2
        records.append({'tick':t,'l1':P.norm(full),'active_events':len(yes),
                        'vetoed_events':len(no),'changed_cells':len(full),
                        'channel_axes_seen':sorted(ever_channels),
                        'spatial_axes_seen':sorted(ever_axes)})
    return {'gamma':encoded(gamma),'spectator_axis':j+1,'initial_pair_axis':l+1,
            'initial_ports':sorted(m+1 for m in ports),'port_degree':len(ports),
            'link_component':sorted(q+1 for q in comp),'wake_norms':age_norms,
            'frontier_hole_checks':hole_checks,'trajectory':records}

def main()->None:
    ap=argparse.ArgumentParser();ap.add_argument('--steps',type=int,default=5)
    ap.add_argument('--output',type=Path,default=Path('incidence_results.json'))
    args=ap.parse_args()
    if not 1<=args.steps<=8: ap.error('Use 1 <= steps <= 8 for the finite checker')
    here=Path(__file__).parent
    parent_hashes={
        'ns_native_density_port_d5c00d.py':'207bf471fea265bc5f9c6cb1c68c3e44ee9a515a0a91025ae638281f5f34d56e',
        'ns_native_ternary_coherence_d5c00d.py':'468b24f1299949ad634c34a87224f2e43df851a42fe48adce63fe1324306aa33'}
    for name,digest in parent_hashes.items():
        assert hashlib.sha256((here/name).read_bytes()).hexdigest()==digest
    orbit={act(FCC,p) for p in permutations(range(P.D))}
    assert len(orbit)==30 and SECOND in orbit and len(EIGHT)==8
    assert all(sorted(map(len,link_components(FCC,j)))==[1,2,2] for j in range(P.D))
    good=[g for g in orbit if len(FCC|g)==8 and all(len(link_components(FCC|g,j))==1 for j in range(P.D))]
    assert len(good)==8
    assert all(len(link_components(EIGHT,j))==1 for j in range(P.D))
    # Exhaust all 8-of-20 incidence sets. Equality in the edge lower bound
    # requires each vertex in exactly four triples; this is a sound pruning.
    triples=sorted(ALL,key=lambda t:tuple(sorted(t)))
    minimal=[]; degree_pruned=0
    for inds in combinations(range(20),8):
        counts=[0]*6
        for index in inds:
            for vertex in triples[index]: counts[vertex]+=1
        if counts!=[4]*6: continue
        degree_pruned+=1
        gamma=frozenset(triples[index] for index in inds)
        if all(len(link_components(gamma,j))==1 for j in range(6)):
            assert all(len(neighbors(gamma,j,l))<=2 for j in range(6) for l in range(6) if l!=j)
            minimal.append(gamma)
    unions={g|h for g in orbit for h in orbit if len(g|h)==8
            and all(len(link_components(g|h,j))==1 for j in range(6))}
    assert set(minimal)==unions and len(minimal)==120
    cases={
        'original_full':run_case(ALL,0,1,min(args.steps,5)),
        'fcc_original_seed':run_case(FCC,0,1,args.steps),
        'fcc_admissible_seed':run_case(FCC,0,2,args.steps),
        'eight_original_seed':run_case(EIGHT,0,1,args.steps),
        'eight_middle_seed':run_case(EIGHT,0,5,args.steps),
    }
    # Every rooted ordered pair of every atlas has the predicted first step.
    cases_checked=0
    for gamma in orbit|set(minimal)|{ALL,frozenset()}:
        for j in range(6):
            for l in range(6):
                if j==l:continue
                out,events,_=step(seed(j),background(j,l),gamma)
                d=len(neighbors(gamma,j,l))
                assert P.norm(out)==2+8*d and len(events)==2*d
                cases_checked+=1
    # Full S6 covariance must transform gamma, not freeze a chart label.
    symmetry=0
    ref,_,_=step(seed(0),background(0,1),EIGHT)
    for p in permutations(range(6)):
        lhs,_,_=step(P.transformed_field(p,seed(0)),P.transformed_counts(p,background(0,1)),act(EIGHT,p))
        assert lhs==P.transformed_field(p,ref);symmetry+=1
    translations=0
    for q in ((3,-2,5,0,-4,1),(-1,0,0,7,2,-3)):
        lhs,_,_=step({P.add(z,q):d for z,d in seed(0).items()},background(0,1),EIGHT)
        assert lhs=={P.add(z,q):d for z,d in ref.items()};translations+=1
    # Fixed-atlas filtering changes native count outcomes when only the atlas is changed.
    a,_,_=step(seed(0),background(0,1),FCC)
    b,_,_=step(seed(0),background(0,1),SECOND)
    assert P.norm(a)==2 and P.norm(b)==10
    data={'schema':'EM_NATIVE_INCIDENCE_FAMILY_RESULTS_V1',
          'event_id':'NS-NATIVE-INCIDENCE-FAMILY-20260909-D5C00D-12',
          'status':'EXACT_CHECKS_AND_ORDINARY_CONDITIONAL_PROOFS_NOT_FORCE_REALIZATION',
          'source_snapshot':'cf224163a9fe5ea4f3ac6d8dd5e13f1b771daf44',
          'parent_hashes':parent_hashes,
          'fcc_atlas_orbit':len(orbit),'compatible_second_atlases':len(good),
          'eight_subsets_total':125970,'eight_subsets_degree_four':degree_pruned,
          'eight_minimal_connected_families':len(minimal),
          'eight_minimal_all_pair_degrees_at_most_two':True,
          'eight_minimal_families_equal_two_atlas_unions':True,
          'minimum_triads_for_all_root_links_connected':8,
          'fcc':encoded(FCC),'second':encoded(SECOND),'eight':encoded(EIGHT),
          'ordered_root_pair_first_steps_checked':cases_checked,
          'S6_covariance_checks':symmetry,'translation_checks':translations,
          'same_native_state_changed_atlas_first_l1':[2,10],
          'cases':cases,
          'nonclaims':['Gamma is not certified as TRIADIC_CLOSURE_E',
                       'Link connectivity is possible-route connectivity, not same-trajectory reachability',
                       'FCC carrier atlas is not a physical constitutive law',
                       'No viscosity or NS theorem; no independent review; no historical novelty claim'],
          'execution_corrections':['First draft misused parent unit() for nonunit translations. Its input check rejected the call. Fixed only the wrapper to use integer displacement tuples.'],
          'exploratory_boundary':'Separate nine-triple probe was terminated at the 45-second tool limit; no universal nine-triple reachability conclusion is claimed.'}
    args.output.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:data[k] for k in ('fcc_atlas_orbit','compatible_second_atlases','ordered_root_pair_first_steps_checked')}))
    for name,case in cases.items(): print(name,case['wake_norms'],[(r['tick'],r['l1'],r['channel_axes_seen'],r['spatial_axes_seen']) for r in case['trajectory']])

if __name__=='__main__':main()
