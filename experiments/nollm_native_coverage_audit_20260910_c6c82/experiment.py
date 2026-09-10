#!/usr/bin/env python3
"""Native Nollm coverage / recall audit, isolated hash-pinned source execution.

Run: python experiment.py --output results
The four source snapshots are unmodified. Only relative imports are supplied
by explicit test fixtures. This is NOT a Core/provider or semantic benchmark.
Research variants below are NOT installed into Nollm.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
import sys
import types
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path

import kernel_harness as h

ONE = 65536
ORIGIN = h.cell()
DIRS = ('coverage_down', 'coverage_up')
EVENT = 'NOLLM-NATIVE-COVERAGE-AUDIT-20260910-C6C82'


def xyz(c):
    return [c.layer, c.q, c.r]


def dump(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')


def field_radius(c):
    return max(abs(c.q), abs(c.r), abs(c.q+c.r))


def load_variant(ledger=False):
    """Only move beam slicing after dominance filtering; optionally record loss."""
    raw = (h.SOURCE_DIR/'recall.py').read_text()
    old = 'in sorted(merged.items(), key=lambda item: (-item[1][0], item[1][2], item[0].stable_key()))[: request.budget.beam]'
    new = 'in sorted(merged.items(), key=lambda item: (-item[1][0], item[1][2], item[0].stable_key()))'
    assert raw.count(old) == 1
    raw = raw.replace(old, new)
    ending = 'if cell not in best or score > best[cell][0] or (score == best[cell][0] and path < best[cell][1])\n        ]'
    assert raw.count(ending) == 1
    if not ledger:
        raw = raw.replace(ending, ending + '[: request.budget.beam]')
    else:
        raw = raw.replace(ending, ending + '''
        removed = max(0, len(frontier) - request.budget.beam)
        if removed:
            truncated_by_budget = True
        runtime._emit_trace(CoreTraceEvent("research.recall.pruning", {
            "step": step, "live_candidates": len(frontier),
            "beam_discarded": removed}, "internal"))
        frontier = frontier[: request.budget.beam]''')
    tree = ast.parse(raw)
    tree.body = [n for n in tree.body
                 if not (isinstance(n, ast.ImportFrom) and n.level)]
    name = 'research_filter_first_ledger' if ledger else 'research_filter_first'
    module = types.ModuleType(name)
    module.__dict__.update(vars(h.recall))
    sys.modules[name] = module
    exec(compile(tree, '<'+name+'>', 'exec'), module.__dict__)
    return module.resolve_recall, raw


def signature(result):
    return [(i.handle.geometry_address.stable_key(), i.score_q16, i.path)
            for i in result.items]


def scan_native(radius=18):
    fanout = Counter()
    edges = asymmetric = samples = 0
    errors = []
    earliest = None
    for q, r in product(range(-radius, radius+1), repeat=2):
        s = h.cell(q, r)
        if field_radius(s) > radius:
            continue
        samples += 1
        for direction, reverse in [('coverage_up','coverage_down'),
                                   ('coverage_down','coverage_up')]:
            e = h.coverage.expand_approximate_coverage(s, direction)
            assert sum(m.hit_count for m in e.members) == 96
            assert sum(m.weight_q16 for m in e.members) == ONE
            assert all(m.hit_count >= 1 and m.weight_q16 > 0 for m in e.members)
            assert e.fanout == len(e.members) <= 8
            fanout[f'{direction}:{e.fanout}'] += 1
            for member in e.members:
                edges += 1
                back = h.coverage.expand_approximate_coverage(member.target, reverse)
                # Do not crop the reverse expansion to the scan disk.
                if s not in dict(back.targets()):
                    asymmetric += 1
                    row = dict(source=xyz(s), target=xyz(member.target), direction=direction,
                               hits=member.hit_count, weight=member.weight_q16,
                               reverse_targets=[dict(cell=xyz(c),weight=w) for c,w in back.targets()])
                    errors.append(row)
                    if earliest is None or (field_radius(s),s.stable_key(),direction) < earliest[0]:
                        earliest = ((field_radius(s),s.stable_key(),direction),row)
    return dict(radius=radius, source_cells=samples, expansions=2*samples,
                fanout_histogram=dict(fanout), positive_relations=edges,
                relations_without_direct_reverse=asymmetric,
                minimum_witness_radius=earliest[0][0], minimum_witness=earliest[1]), errors


def two_step():
    result=[]
    for directions in [('coverage_down','coverage_up'),('coverage_up','coverage_down')]:
        count=Counter();mass=Counter();maximum={}
        for s,w in h.coverage.expand_approximate_coverage(ORIGIN,directions[0]).targets():
            for t,v in h.coverage.expand_approximate_coverage(s,directions[1]).targets():
                count[t]+=1
                mass[t]+=Fraction(w*v,ONE*ONE)
                maximum[t]=max(maximum.get(t,0),w*v//ONE)
        assert sum(mass.values())==1
        result.append(dict(directions=directions, paths=sum(count.values()),
                           endpoint_support=len(count), root_paths=count[ORIGIN],
                           root_sum_of_weight_products=str(mass[ORIGIN]),
                           root_best_two_step_q16=maximum[ORIGIN],
                           endpoints=[dict(cell=xyz(t),paths=count[t],mass=str(mass[t]),
                                           best_two_step_q16=maximum[t])
                                      for t in sorted(count,key=lambda c:c.stable_key())]))
    # A shared positive output demonstrates a weight-only reversible decoder obstruction.
    a,b = ORIGIN,h.cell(1,0)
    out_a=dict(h.coverage.expand_approximate_coverage(a,'coverage_up').targets())
    out_b=dict(h.coverage.expand_approximate_coverage(b,'coverage_up').targets())
    common=sorted(set(out_a)&set(out_b),key=lambda c:c.stable_key())
    assert common
    return result,dict(source_a=xyz(a),source_b=xyz(b),
                       shared_outputs=[dict(cell=xyz(t),weight_a=out_a[t],weight_b=out_b[t]) for t in common],
                       scope='Only scalar positive-mass encoding; not deletion of stored atoms or provenance.')


def beam_audit(outdir):
    repaired,source=load_variant(False)
    ledger,_=load_variant(True)
    # Keep the candidate as a reviewable diff, never modify the frozen source.
    import difflib
    original=(h.SOURCE_DIR/'recall.py').read_text()
    (outdir/'research_only_filter_order.diff').write_text(''.join(difflib.unified_diff(
        original.splitlines(True),source.splitlines(True),
        fromfile='pinned_nollm/recall.py',tofile='research_only/recall_filter_first.py')))
    bound_ball=h.support_ball(8,2)
    rows=[];counts=0
    samples={}
    for beam in (1,2,4,8,16,32,64,128,512,4096):
        rt,a=h.run_recall(8,beam,fn=h.recall.resolve_recall)
        rt2,b=h.run_recall(8,beam,fn=repaired)
        rt3,c=h.run_recall(8,beam,fn=ledger)
        assert signature(b)==signature(c)
        for runtime in (rt,rt2,rt3):
            assert set(runtime.visited)<=set(bound_ball)
            assert len(set(runtime.visited))<=1+8*beam
        discarded=sum(e.data['beam_discarded'] for e in rt3.trace
                      if e.name=='research.recall.pruning')
        rows.append(dict(beam=beam,depth=8,layer_delta=2,reachable_support=len(bound_ball),
                         native_visited=len(set(rt.visited)),
                         filter_first_visited=len(set(rt2.visited)),
                         native_budget_exhausted=a.budget_exhausted,
                         filter_first_budget_exhausted=b.budget_exhausted,
                         ledger_budget_exhausted=c.budget_exhausted,
                         ledger_discarded_live_occurrences=discarded))
        counts+=3
        if beam in (1,8,32,512):
            samples[str(beam)]=dict(native=[xyz(x) for x in rt.visited],
                                   filter_first=[xyz(x) for x in rt2.visited],
                                   native_frontiers=[e.data for e in rt.trace if e.name=='core.recall.frontier'])
        if beam>=512:
            assert set(rt.visited)==set(bound_ball)==set(rt2.visited)
            assert signature(a)==signature(b)
    assert rows[0]['native_visited']==3
    assert rows[0]['native_budget_exhausted'] is False
    assert rows[0]['filter_first_visited']==9
    # Independent origin/depth/budget combinations; do not assume monotone benefit.
    grid=[]
    for origin,depth,beam in product([h.cell(),h.cell(-4,2),h.cell(6,-1),h.cell(3,5)],
                                     (2,4,6),(1,8,64)):
        support=h.support_ball(depth,2,origin)
        rt,a=h.run_recall(depth,beam,2,origin,fn=h.recall.resolve_recall)
        rt2,b=h.run_recall(depth,beam,2,origin,fn=repaired)
        assert set(rt.visited)<=set(support) and set(rt2.visited)<=set(support)
        assert len(set(rt2.visited))<=1+depth*beam
        grid.append(dict(origin=xyz(origin),depth=depth,beam=beam,support=len(support),
                         native=len(set(rt.visited)),filter_first=len(set(rt2.visited)),
                         native_flag=a.budget_exhausted,filter_first_flag=b.budget_exhausted))
        counts+=2
    dump(outdir/'beam_visits.json',samples)
    dump(outdir/'beam_grid.json',grid)
    dump(outdir/'coverage_support_depth8.json',[
        dict(cell=xyz(c),distance=d) for c,d in sorted(bound_ball.items(),key=lambda t:t[0].stable_key())])
    return rows,dict(recall_executions=counts,additional_grid_cases=len(grid),
                     grid_native_underreports_exhaustion=sum(not r['native_flag'] and r['native']<r['support'] for r in grid),
                     grid_filter_first_fewer_than_native=sum(r['filter_first']<r['native'] for r in grid))


def bridge_budget_witness():
    """Synthetic graph using actual Recall targets/selection, not native Coverage."""
    E,A,X,Y=h.cell(),h.cell(0,0,1),h.cell(1,0),h.cell(2,0)
    class FixtureRegistry:
        def expand_coverage(self,c,d):
            if c==E and d=='coverage_down':return ((A,ONE//2),)
            if c==A and d=='coverage_up':return ((X,ONE),)
            return ()
    def bridge(src,dst,name):
        return types.SimpleNamespace(bridge_id=name,from_anchor=types.SimpleNamespace(cells=(src,)),
            to_anchor=types.SimpleNamespace(cells=(dst,)),weight_q16=ONE,max_steps=1,max_fanout=1)
    bridges=(bridge(E,X,'entry-shortcut'),bridge(X,Y,'target-bridge'))
    class FixtureRuntime(h.Runtime):
        def _bridges_locked(self):return bridges
    request=h.recall.CoreRecallRequest('resource-witness',(E,),('bridge',*DIRS),
                  h.recall.RecallBudget(3,100,2,0,1,100))
    rt=FixtureRuntime(FixtureRegistry());res=h.recall.resolve_recall(rt,request)
    assert Y not in set(rt.visited)
    # Exhaustive path reference, retaining remaining bridge budget and step depth.
    frontier=[(E,ONE,0,())];records=[]
    for step in range(4):
        nxt=[]
        for c,s,b,path in frontier:
            records.append((c,s,b,path))
            if step<3:
                for target,w,nb,kernel in h.recall._targets(rt,c,request,b):
                    if abs(target.layer)<=2:nxt.append((target,s*w//ONE,nb,(*path,kernel)))
        frontier=nxt
    ys=[row for row in records if row[0]==Y]
    assert len(ys)==1 and ys[0][1]==ONE//2
    assert ys[0][3]==('coverage_down','coverage_up','bridge')
    # The filtered-beam patch alone cannot repair hidden-resource dominance.
    repaired,_=load_variant(False)
    rt2=FixtureRuntime(FixtureRegistry());res2=repaired(rt2,request)
    assert Y not in set(rt2.visited)
    return dict(scope='synthetic four-node legal-operation fixture; NOT measured native geometry',
                nodes=dict(entry=xyz(E),via=xyz(A),junction=xyz(X),target=xyz(Y)),
                native_visited=[xyz(c) for c in rt.visited],
                native_budget_exhausted=res.budget_exhausted,
                filter_first_still_misses_target=True,
                feasible_reference_path=ys[0][3],feasible_reference_score_q16=ys[0][1],
                native_total_steps=3,beam=100,max_bridge_steps=1,
                reference_path_state_appearances=len(records),
                explanation='Higher score at X has used its one bridge; lower score at X retains a usable bridge.')



def native_bridge_witness():
    """Real sampled Coverage plus two explicitly declared test Bridges.
    The anchors are test input, not evidence-backed production Bridge creation.
    """
    E,X,Y=h.cell(),h.cell(1,0),h.cell(100,0)
    def bridge(a,b):
        return types.SimpleNamespace(from_anchor=types.SimpleNamespace(cells=(a,)),
             to_anchor=types.SimpleNamespace(cells=(b,)),max_steps=1,
             max_fanout=1,weight_q16=ONE)
    class HybridRuntime(h.Runtime):
        def _bridges_locked(self):return (bridge(E,X),bridge(X,Y))
    rt=HybridRuntime()
    rq=h.recall.CoreRecallRequest('native-hybrid',(E,),('bridge',*DIRS),
               h.recall.RecallBudget(3,4096,2,0,1,1000000))
    observed=h.recall.resolve_recall(rt,rq)
    assert Y not in set(rt.visited)
    # Enumerate all feasible paths without collapsing bridge-budget state.
    frontier=[(E,ONE,0,())];target_paths=[];appearances=0
    for step in range(4):
        nxt=[]
        for c,score,used,path in frontier:
            appearances+=1
            if c==Y:target_paths.append((score,used,path))
            if step<3:
                for target,w,b,k in h.recall._targets(rt,c,rq,used):
                    if abs(target.layer)<=2:
                        nxt.append((target,score*w//ONE,b,(*path,k)))
        frontier=nxt
    assert len(target_paths)==3 and max(x[0] for x in target_paths)==2730
    # Resource-aware DP: merge only within an exact depth and bridge-used count.
    # This preserves reachability and maximal numerical score, not every history
    # or the globally smallest lexicographic witness after Q16 floor ties.
    frontier={(E,0):ONE};seen=set();score_at_target=None;dp_states=0
    for step in range(4):
        nxt={}
        for (c,used),score in frontier.items():
            dp_states+=1;seen.add(c)
            if c==Y:score_at_target=max(score_at_target or 0,score)
            if step<3:
                for target,w,b,k in h.recall._targets(rt,c,rq,used):
                    if abs(target.layer)>2:continue
                    key=(target,b);new_score=score*w//ONE
                    if key not in nxt or nxt[key]<new_score:nxt[key]=new_score
        frontier=nxt
    assert Y in seen and score_at_target==2730
    return dict(scope='native sampled Coverage; two explicit test Bridge anchors; isolated runtime fixture',
                entry=xyz(E),junction=xyz(X),target=xyz(Y),max_steps=3,beam=4096,max_bridge_steps=1,
                native_visited=len(set(rt.visited)),native_target_found=False,
                native_budget_exhausted=observed.budget_exhausted,
                exhaustive_path_appearances=appearances,
                feasible_target_paths=[dict(score_q16=s,bridge_steps=b,path=path) for s,b,path in target_paths],
                resource_aware_dp_state_appearances=dp_states,
                resource_aware_target_found=True,resource_aware_target_score_q16=score_at_target,
                reference_contract='Reachability and maximum score, not all provenance or global lexicographic tie minimization')

def run(outdir):
    outdir.mkdir(parents=True,exist_ok=True)
    sources={name:dict(git_blob_sha1=pin,sha256=hashlib.sha256((h.SOURCE_DIR/name).read_bytes()).hexdigest())
             for name,pin in h.PINS.items()}
    scan,nonreciprocal=scan_native()
    dump(outdir/'nonreciprocal_relations.json',nonreciprocal)
    assert (scan['source_cells'],scan['positive_relations'],scan['relations_without_direct_reverse'])==(1027,7946,66)
    pair,loss=two_step()
    assert pair[0]['paths']==25 and pair[0]['root_paths']==7
    rows,checks=beam_audit(outdir)
    # BFS visibility is independent of scoring and beam; unique support, not paths.
    balls=[]
    for depth in (2,4,6,8,10,12,16,20):
        seen=h.support_ball(depth)
        balls.append(dict(depth=depth,unique_cells=len(seen),
                          same_layer_cells=sum(c.layer==0 for c in seen),
                          maximum_axial_radius=max(map(field_radius,seen))))
    bridge=bridge_budget_witness()
    native_bridge=native_bridge_witness()
    result=dict(schema='NOLLM_NATIVE_COVERAGE_AUDIT_V1',event_id=EVENT,
        status='ISOLATED_PINNED_SOURCE_CHECKED_NOT_PROMOTED',
        nollm_source='91bd14ab394e87931b45baaaa87671f30fcfd706',source_hashes=sources,
        scan=scan,two_step_observers=pair,weight_only_decoder_witness=loss,
        beam_comparison=rows,beam_checks=checks,support_balls=balls,
        bridge_resource_witness=bridge,native_coverage_bridge_witness=native_bridge,
        limits=['Isolated function execution with declared fixtures, not installed Core/provider validation.',
                'Native geometric experiments use coverage_up/down only, no lateral or persistent bridges.',
                'Bridge-resource case is an explicitly synthetic graph.',
                'No real memory corpus, semantic quality, concurrency capacity or wire timing measured.',
                'The local filter-order variant is not a complete recall fix or production patch.',
                'Ideal branch multiplicity, rational weight sums, max-path scores and stored identity are different observers.',
                'No Nollm source mutation, P000 change, theorem promotion or ordinary integer multiplication embedding.'])
    dump(outdir/'results.json',result)
    print(json.dumps(dict(status=result['status'],scan={k:v for k,v in scan.items() if k!='minimum_witness'},
                         beam=rows,checks=checks,support=balls,bridge=bridge),indent=2))
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('results'))
    run(parser.parse_args().output)
