#!/usr/bin/env python3
"""Fixed-family phase rigidity and parallel 11-direction charts.
Research prototype: quotient identity is not scalar-label multiplication.
Run --output DIR. Requires numpy and the hash-pinned predecessor bundle in prior/.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, math, sys
from collections import Counter, deque
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
OPTIONS=[ROOT/'prior/nollm_two_inert_511/experiment.py',ROOT/'nollm_two_inert_511_20260909_c6c82.py']
PIN='db00742a81241d10883299253307fb1ee7831b7703bf710f88288606998f53b4'
pth=next((p for p in OPTIONS if p.exists()),None)
if pth is None: raise FileNotFoundError('two-inert predecessor required')
if hashlib.sha256(pth.read_bytes()).hexdigest()!=PIN:raise ValueError('predecessor hash mismatch')
sp=importlib.util.spec_from_file_location('phase_predecessor',pth)
g=importlib.util.module_from_spec(sp);sys.modules[sp.name]=g;sp.loader.exec_module(g)
EVENT='NOLLM-PHASE-RIGIDITY-CHARTS-20260909-C6C82'

def cycle(p):
    out=[];l=0
    while l not in out:
        out.append(l);l=g.act(g.ES[7],l,p,True)
    assert len(out)==p+1 and l==0
    return out

def label(x,line,p):
    q,r=map(int,x)
    return q%p if line==p else (r-line*q)%p

def labels(x,l,k):return label(x,l,5),label(x,k,11)

def ratio_sq(P):
    """Exact Voronoi outer-radius / inner-radius squared, not cloud axis ratio."""
    B=g.m.reduced(P)
    shortest=min(g.Q(B[:,0]),g.Q(B[:,1]))
    radius=max(g.m.qf(v) for v in g.m.vertices(P))
    return 4*radius/shortest,shortest,radius

def run(out):
    out.mkdir(parents=True,exist_ok=True)
    cyc5,cyc11=cycle(5),cycle(11)
    states=list(product(range(6),range(12)))
    shifts={p:(cyc5.index(g.act(g.ES[p],0,5,True)),cyc11.index(g.act(g.ES[p],0,11,True))) for p in (7,13,19)}
    assert shifts=={7:(1,1),13:(3,11),19:(2,9)}
    for i,j in states:
        for p,(a,b) in shifts.items():
            assert g.act(g.ES[p],cyc5[i],5,True)==cyc5[(i+a)%6]
            assert g.act(g.ES[p],cyc11[j],11,True)==cyc11[(j+b)%12]
    bad={(0,0),(cyc5.index(4),cyc11.index(10)),(cyc5.index(5),cyc11.index(11))}
    # Every start has an explicit nonnegative word leading to a unit-thin state.
    reach={}
    for ps in ((7,19),(7,13,19)):
        paths={v:[] for v in sorted(bad)};queue=deque(sorted(bad))
        while queue:
            x=queue.popleft()
            for p in ps:
                a,b=shifts[p];y=((x[0]-a)%6,(x[1]-b)%12)
                if y not in paths:paths[y]=[p]+paths[x];queue.append(y)
        assert len(paths)==72
        for start,path in paths.items():
            x=start
            for p in path:a,b=shifts[p];x=((x[0]+a)%6,(x[1]+b)%12)
            assert x in bad
        reach['_'.join(map(str,ps))]={'max_shortest_length':max(map(len,paths.values())),
            'distance_histogram':dict(sorted(Counter(map(len,paths.values())).items())),
            'witnesses':[{'start':s,'word':paths[s]} for s in states]}
    assert reach['7_13_19']['max_shortest_length']==5
    # Exact inherited prime-line invariant for every active atlas transition.
    inheritance=0
    for e,f,l,k in g.STATES:
        s=(e,f,l,k);P=g.H(*s)
        for p in (5,11,7,13,19):
            ns,E=g.trans(s,p);C=E@g.H(*ns)
            num=g.m.old.adj(P)@C;den=g.m.old.det(P)
            assert np.all(num%den==0)
            assert g.m.old.det(num//den)==p
            for q,active in ((5,e),(11,f)):
                if not active or p==q:continue
                def image_line(A):
                    vals={g.pline(A[:,j],q) for j in range(2) if np.any(A[:,j]%q)}
                    assert len(vals)==1
                    return next(iter(vals))
                assert image_line(C)==image_line(P);inheritance+=1
    # 72 exact cells; use the predecessor selector and geometry without changing them.
    costs={};sections={};lookup={};rows=[]
    for i,j in states:
        l,k=cyc5[i],cyc11[j];P=g.H(1,1,l,k)
        cost,sq,radius=ratio_sq(P);S=g.section(P,g.ANCHORS[(1,1,l,k)])
        by={labels(x,l,k):tuple(map(int,x)) for x in S}
        assert set(by)==set(product(range(5),range(11)))
        assert g.m.old.hull_metrics(S)['hull_total_lattice_sites']==55
        sections[i,j]=S;lookup[i,j]=by;costs[i,j]=cost
        rows.append({'state':[i,j],'lines':[l,k],'shortest_sq':sq,'outer_radius_sq':str(radius),
            'roundness_sq':str(cost),'roundness':math.sqrt(float(cost)),
            'cloud_axis_ratio':g.m.old.ratio(S.T@S),'basis':P.tolist()})
    # Fixed parallel charts differ ONLY in their initial line modulo 11.
    # Translation in j makes including offset 0 WLOG for these worst-state objectives.
    covers=[];selected={}
    for count in (1,2,3,4):
        best=None;ties=[];tested=0
        for rest in combinations(range(1,12),count-1):
            offsets=(0,)+rest;tested+=1
            worst=max(min(costs[i,(j+d)%12] for d in offsets) for i,j in states)
            if best is None or worst<best:best=worst;ties=[offsets]
            elif worst==best:ties.append(offsets)
        offsets=ties[0];selected[count]=offsets
        picks=[min(offsets,key=lambda d:(costs[i,(j+d)%12],d)) for i,j in states]
        covers.append({'charts':count,'tested_offset_sets':tested,'best_offsets':offsets,
            'tied_optima':ties,'worst_roundness_sq':str(best),'worst_roundness':math.sqrt(float(best)),
            'selected_offsets_by_state_order':picks})
    assert [v['worst_roundness_sq'] for v in covers]==['20593444/9075','172/25','13468/3025','364/121']
    # Natural ambient identity does NOT induce a map between incomparable quotients.
    # A concrete old 55-point section maps to just 27 target cosets.
    S0=sections[0,0];S1=sections[0,1];line1=cyc11[1]
    projected=Counter(labels(x,0,line1) for x in S0)
    assert len(projected)==27
    collision=((-2,5),(0,0),(2,-5))
    assert all(x in set(map(tuple,S0)) for x in collision)
    assert len({labels(x,0,line1) for x in collision})==1
    assert len({labels(x,0,0) for x in collision})==3
    # Explicit CRT-label transport is a different, bijective readout contract.
    # Encode once with source normal, decode with target normal. No global memory lookup.
    pair_checks=0;triple_checks=0
    for i in range(6):
        for j,k in product(range(12),repeat=2):
            T=[lookup[i,k][labels(x,cyc5[i],cyc11[j])] for x in sections[i,j]]
            assert len(set(T))==55 and set(T)==set(map(tuple,sections[i,k]));pair_checks+=55
            for h in range(12):
                for x,y in zip(sections[i,j],T):
                    direct=lookup[i,h][labels(x,cyc5[i],cyc11[j])]
                    via=lookup[i,h][labels(y,cyc5[i],cyc11[k])]
                    assert direct==via;triple_checks+=1
    repaired=[lookup[0,1][labels(x,0,0)] for x in S0]
    unchanged=sum(tuple(map(int,x))==y for x,y in zip(S0,repaired))
    moves=[g.Q((int(x[0])-y[0],int(x[1])-y[1])) for x,y in zip(S0,repaired)]
    # Genuine ambient lift: common refinement has 605 states, not 55.
    # L0 = Z x 55Z; L1 = {r=0 mod5, r=3q mod11}; intersection = 11Z x 55Z.
    J=np.array([[11,0],[0,55]],dtype=np.int64)
    for L in (g.H(1,1,0,0),g.H(1,1,0,line1)):
        assert np.all((g.m.old.adj(L)@J)%55==0)
    assert g.m.old.det(J)==605
    lift=[(q,r) for q in range(11) for r in range(55)]
    projected_pairs={(labels(x,0,0),labels(x,0,line1)) for x in lift}
    assert len(projected_pairs)==605
    source_fibers=Counter(a for a,b in projected_pairs)
    assert set(source_fibers.values())=={11} and len(source_fibers)==55
    # All 12 chart readouts can be reconstructed from full (q,r) mod11 plus r mod5.
    for x in lift:
        a=label(x,0,5);q,r=x[0]%11,x[1]%11
        for k in range(12):
            assert labels(x,0,k)==(a,q if k==11 else (r-k*q)%11)
    result={'schema':'NOLLM_PHASE_RIGIDITY_CHARTS_V1','event_id':EVENT,'status':'PASS_RESEARCH_NOT_PROMOTED',
        'source_sha256':PIN,'cycles':[cyc5,cyc11],'phase_shifts':shifts,'initial_line_pairs':72,
        'reachability':reach,'prime_line_invariance_cases':inheritance,
        'complete_sections':72,'section_point_appearances':3960,
        'charts':covers,'CRT_pair_transport_checks':pair_checks,'CRT_composition_checks':triple_checks,
        'direct_projection':{'source_points':55,'distinct_target_classes':27,
            'class_multiplicity_histogram':dict(sorted(Counter(projected.values()).items())),
            'collision':collision},
        'explicit_CRT_relabel':{'source_points':55,'distinct_target_points':55,'unchanged':unchanged,
            'moved':55-unchanged,'max_displacement_Q':max(moves)},
        'ambient_lift':{'index':605,'source_index':55,'fiber_size':11,'all_12_views_reconstructed':True},
        'limits':['no universal no-go outside the frozen split-generator/nested-family assumptions',
            'multi-chart roundness bound is for both 5 and 11 active and these fixed 12 parallel choices',
            'roundness is Voronoi outer/inner radius, not singular-value or cloud-axis ratio',
            'CRT relabeling is not natural ambient quotient identity and moves old positions',
            'the 605-state lower bound requires preserving all ambient cross-chart readouts; not a blanket memory lower bound',
            'no arbitrary scalar-label multiplication or Nollm runtime integration']}
    (out/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    (out/'shape_certificate.json').write_text(json.dumps(rows,indent=2)+'\n')
    np.savez_compressed(out/'sections.npz',**{f'i{i}j{j}':S for (i,j),S in sections.items()})
    np.savez_compressed(out/'transport_example.npz',old=S0,new=S1,transported=np.array(repaired,dtype=np.int64))
    print(json.dumps({k:result[k] for k in ('status','prime_line_invariance_cases','complete_sections','CRT_pair_transport_checks','CRT_composition_checks','direct_projection','explicit_CRT_relabel','ambient_lift')},indent=2))
    return result
if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,default=ROOT/'results')
    run(ap.parse_args().output)
