"""Run with Python 3.11+; vendored source is pinned, not a production install.
Optional --nollm-src is packages/nollm-core/src in an actual Nollm checkout.
Optional --em-src is src in an Enterprise Math checkout.
"""
from __future__ import annotations
import argparse
from dataclasses import asdict
from fractions import Fraction as F
from hashlib import sha1
import json
from pathlib import Path
import random
import sys
from types import ModuleType, SimpleNamespace as NS

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument('--nollm-src', type=Path, default=ROOT/'vendor')
parser.add_argument('--em-src', type=Path, default=ROOT/'vendor')
parser.add_argument('--output', type=Path, default=ROOT/'verification_results.json')
args = parser.parse_args()
# Load a sparse exact dependency closure, not the packages' eager __init__ files.
for name, base in [('nollm_core', args.nollm_src), ('enterprise_math', args.em_src)]:
    module = ModuleType(name); module.__path__ = [str(base/name)]
    sys.modules[name] = module

from nollm_core.recall import (CoreRecallRequest, RecallBudget, resolve_recall, _targets)
from nollm_core.bridge import BridgeSpec, GeometryAnchor
from nollm_core.atom import MemoryAtom
from nollm_core.handle import AtomHandle
from nollm_core.geometry import GeometryAddress
from nollm_core.fixed_point import normalize_q16_weights
from enterprise_math.brc_transport import Affine, EffectHistogram, MomentState
from enterprise_math.predictive_quotient import predictive_block_profile, stable_predictive_partition
from brc_resource_recall import Label, RoundedWord, coalesce, bounded_recall, Q16

EXPECTED = {
 'nollm_core/recall.py': '02c148caad1929a0f72055100b75f806f55a956d',
 'nollm_core/atom.py': '2e62a248cca48b459b4b21304a4e3c8e1c9f07b2',
 'nollm_core/bridge.py': 'c9d0bda25d2d019cff31f31f3bb7724ba963e438',
 'nollm_core/fixed_point.py': '9ea00e3c84a82f480c692a6ca0ca717a579dab60',
 'nollm_core/geometry.py': '6f3778a24ce58d05a53d052b5dbb080b6bc5bd86',
 'nollm_core/handle.py': 'caaa2c318d9e4d3e62e9661a0f810996c49f95bf',
 'nollm_core/ports.py': 'e2b450b0ef440eb80c995b8903629478e28addd4',
 'nollm_core/profiles.py': '9aec8183997b884ff3b936ca01a52a3ceab07446',
 'nollm_core/validation.py': '1b68755f92d5ee870a828e285c4695d54420c5c9',
 'enterprise_math/brc_transport.py': 'be1debe367263931bd5e93fd750be3ed54624fe1',
 'enterprise_math/brc_histogram.py': '9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1',
 'enterprise_math/predictive_quotient.py': 'f27d9ddf908f5b07051acfaf0c69f359d499b98b',
}
results = {}
for path, expected in EXPECTED.items():
    base = args.nollm_src if path.startswith('nollm_core') else args.em_src
    raw = (base/path).read_bytes()
    actual = sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    assert actual == expected, (path, actual, expected)
results['01_source_identity'] = {'full_exact_files': len(EXPECTED), 'git_blobs': EXPECTED,
 'dependency_slices': ['three coverage-template functions', 'prime-valuation dependency excerpt'],
 'not_loaded': ['Nollm complete runtime/state/storage', 'entire compiled template artifact']}


def cell(q, r):
    return GeometryAddress('default_dream_v1', 'default', 0, q, r)


class LateralRegistryFixture:
    """Exact canonical phase-0 lateral data, not a replacement coverage kernel.

    Official compiler.py _physical_entries('lateral', phase) uses these six
    offsets and normalize_q16_weights(6); physical_geometry axial_transform_q32
    returns identity for lateral. Runtime expand_template executes unchanged.
    """
    fanout_limit = 7
    def coverage_template(self, profile_id, direction, layer):
        assert direction == 'lateral' and profile_id == 'default_dream_v1' and layer == 0
        offsets = ((-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0))
        weights = normalize_q16_weights([1]*6)
        return NS(profile_id=profile_id, transform_q32=(1<<32,0,0,1<<32),
                  entries=tuple(NS(layer_delta=0,dq=q,dr=r,weight_q16=w)
                                for (q,r),w in zip(offsets, weights)))


class RuntimeFixture:
    def __init__(self, bridges, target):
        self.kernel_registry = LateralRegistryFixture()
        self.bridges = bridges
        self.target = target
        self.traces = []
    def _emit_trace(self, event): self.traces.append(event)
    def _bridges_locked(self): return self.bridges
    def _atoms_at_locked(self, address):
        return ((AtomHandle(self.target,'target'),MemoryAtom('target','synthetic target')),) if address == self.target else ()


def exhaustive(entry, targets, depth, bridge_budget):
    frontier = [(entry,Q16,0,())]; best={}; generated=0; widths=[]
    for t in range(depth+1):
        widths.append(len(frontier))
        for x,s,b,p in frontier:
            old = best.get(x)
            if old is None or s>old[0] or (s==old[0] and p<old[1]): best[x]=(s,p)
        if t==depth: break
        following=[]
        for x,s,b,p in frontier:
            for y,w,b2,k in targets(x,b):
                if b2<=bridge_budget:
                    following.append((y,s*w//Q16,b2,p+(k,)))
        generated += len(following); frontier=following
    return best,widths,generated

S,A,C,T = cell(0,0),cell(10,0),cell(0,2),cell(20,0)
def mkbridge(name,source,target):
    return BridgeSpec(name,GeometryAnchor(name+'f',(source,)),GeometryAnchor(name+'t',(target,)),Q16,'normal',3,1)
bridges=(mkbridge('sa',S,A),mkbridge('ac',A,C),mkbridge('ct',C,T))
request=CoreRecallRequest('brc-resource-witness',(S,),('bridge','lateral'),RecallBudget(3,4096,0,1,2,8))
runtime=RuntimeFixture(bridges,T)
original=resolve_recall(runtime,request)
def actual_targets(x,b):
    return tuple(e for e in _targets(runtime,x,request,b)
                 if abs(e[0].layer-S.layer)<=request.budget.max_layer_delta)
oracle,widths,generated=exhaustive(S,actual_targets,3,2)
repaired=bounded_recall(S,actual_targets,max_steps=3,max_bridges=2,mode='paths')
score_repaired=bounded_recall(S,actual_targets,max_steps=3,max_bridges=2,mode='scores')
assert original.items==()
assert oracle[T] == (1820,('lateral','lateral','bridge'))
assert repaired.best==oracle
assert {k:v[0] for k,v in score_repaired.best.items()}=={k:v[0] for k,v in oracle.items()}
assert max(widths)<request.budget.beam  # stronger than just checking retained frontiers
results['02_actual_recall_counterexample']={
 'profile':'default_dream_v1', 'entry':S.to_mapping(),
 'A':A.to_mapping(), 'C':C.to_mapping(), 'T':T.to_mapping(),
 'bridge_weight_q16':Q16,'bridge_per_spec_cap':3,'request_budget':asdict(request.budget),
 'original_items':len(original.items),'oracle_target_score':oracle[T][0],'oracle_target_path':oracle[T][1],
 'merge_pair':[[65536,2,['bridge','bridge']],[1820,0,['lateral','lateral']]],
 'exhaustive_widths':widths,'exhaustive_generated':generated,
 'original_frontier_widths':[e.fields['cell_count'] for e in runtime.traces if e.name=='core.recall.frontier'],
 'repaired_widths':repaired.frontier_widths,'score_only_widths':score_repaired.frontier_widths,
 'repaired_all_reached_cell_results_match_exhaustive':True,'beam_truncation':False,
 'scope':'unaltered resolve_recall/_targets with canonical lateral-data and legal synthetic BridgeSpec/atom fixture, not installed-user runtime'}
# Negative/control experiment: larger Bridge allowance restores the three-bridge route.
control_req=CoreRecallRequest('brc-resource-control',(S,),('bridge','lateral'),RecallBudget(3,4096,0,1,3,8))
control=resolve_recall(RuntimeFixture(bridges,T),control_req)
assert control.items[0].score_q16==Q16 and control.items[0].path==('bridge',)*3
results['03_budget_control']={'max_bridge_steps':3,'target_score':control.items[0].score_q16}

# The previously extracted tool is executed, rather than a second moment implementation.
a=Affine.identity(6)
p=EffectHistogram.from_terms(6,[(F(3,4),a,1),(F(1,4),a,1)])
q=EffectHistogram.from_terms(6,[(F(1,2),a,2)])
m=MomentState.from_point((0,)*6)
assert m.then(p)==m.then(q)
assert p.forget_effects().count==q.forget_effects().count==2
assert p.forget_effects().dominant_mass!=q.forget_effects().dominant_mass
results['04_moment_max_observer_boundary']={'same_28_entry_moment':True,'same_count':2,
 'dominant_weights':['3/4','1/2'],'interpretation':'not a failure of the affine-moment theorem; max is another observer'}

# Exact Q16 scalar multiplication is NOT associative.
a,b,c=65535,65535,32768
mul=lambda x,y:x*y//Q16
left=mul(mul(a,b),c);right=mul(a,mul(b,c))
assert (left,right)==(32767,32766)
u,v,w=RoundedWord((a,)),RoundedWord((b,)),RoundedWord((c,))
assert u.then(v).then(w)==u.then(v.then(w))
assert u.then(v).then(w).apply(Q16)==left
assert all(RoundedWord((b,c)).apply(s)<=RoundedWord((b,c)).apply(s+1) for s in range(Q16))
results['05_rounded_action_composition']={'scalar_left':left,'scalar_right':right,
 'action_composition':'associative','monotonicity_cases':Q16,'absent_and_zero_distinct':RoundedWord((1,)).apply(None) is None and RoundedWord((1,)).apply(0)==0}

# High score can become tied later: lexicographic provenance must not be erased.
low=Label('C',2,1,2,('bridge','lateral'))
high=Label('C',3,1,2,('lateral','bridge'))
assert len(coalesce([low,high],mode='scores'))==1
assert len(coalesce([low,high],mode='paths'))==2
assert RoundedWord((16384,)).apply(low.score)==RoundedWord((16384,)).apply(high.score)==0
assert low.path+('lateral',)<high.path+('lateral',)
results['06_rounding_tie_provenance']={'before_scores':[2,3],'after_scores':[0,0],
 'score_only_labels':1,'path_safe_labels':2,'lower_score_path_wins_after_rounding':True}

# T6 directly gives the minimal remaining-resource partition for a declared language.
B=5
states=tuple(range(-1,B+1))  # -1 = failed, r>=0 = r remaining Bridge operations
profile=predictive_block_profile(states,{'bridge':lambda r:max(-1,r-1)},lambda r:r>=0, B+1)
stable=stable_predictive_partition(states,{'bridge':lambda r:max(-1,r-1)},lambda r:r>=0)
assert profile==(2,3,4,5,6,7,7) and stable.block_count==7
results['07_T6_resource_minimality']={'bridge_budget':B,'profile':profile,
 'alive_resource_classes':B+1,'failure_class':1,'scope':'universal bridge-continuation language; a specific graph may need fewer classes'}

# Independent finite random systems; no semantic simulation or geometry claim.
rng=random.Random(20260919)
case_count=180; total_expansions=0
for case in range(case_count):
    n=6; B=rng.randrange(1,4); depth=rng.randrange(2,6)
    edges={x:[] for x in range(n)}
    for x in range(n):
        for _ in range(rng.randrange(1,5)):
            cost=rng.randrange(2)
            edges[x].append((rng.randrange(n),rng.choice((1,16384,32768,65534,65535,65536)),cost,'bridge' if cost else 'lateral',rng.randrange(1,4)))
    def targets(x,used):
        return tuple((y,w,used+cost,k) for y,w,cost,k,cap in edges[x]
                     if not cost or (used<B and used<cap))
    oracle,_,count=exhaustive(0,targets,depth,B);total_expansions+=count
    kept=bounded_recall(0,targets,max_steps=depth,max_bridges=B,mode='paths')
    scores=bounded_recall(0,targets,max_steps=depth,max_bridges=B,mode='scores')
    assert kept.best==oracle,(case,kept.best,oracle)
    assert {x:v[0] for x,v in scores.best.items()}=={x:v[0] for x,v in oracle.items()},case
results['08_finite_graph_regression']={'graphs':case_count,'explicit_generated_path_labels':total_expansions,
 'both_score_and_path_observers':'PASS','independent_oracle':'unpruned bounded path enumeration'}

# Idempotence and input-order independence at fixed depth, including score zero.
checks=0
for _ in range(100):
    paths=[tuple(rng.choice(('bridge','lateral')) for _ in range(3)) for i in range(20)]
    labels=[Label(0,rng.randrange(8),path.count('bridge'),3,path) for path in paths]
    for mode in ('scores','paths'):
        frozen=set(coalesce(labels,mode=mode))
        assert set(coalesce(frozen,mode=mode))==frozen
        for j in range(4):
            rng.shuffle(labels)
            got=coalesce(labels,mode=mode)
            if mode=='paths': assert set(got)==frozen
            else: assert {(x.bridges,x.score) for x in got}=={(x.bridges,x.score) for x in frozen}
            checks+=1
results['09_antichain_regression']={'order_checks':checks,'idempotence':True,
 'score_mode_does_not_preserve_tie_path':True}

rejected=0
for fn in (lambda:RoundedWord((0,)),lambda:RoundedWord((1.0,)),lambda:RoundedWord((1,),True),
           lambda:RoundedWord().apply(-1),lambda:Label(0,1,2,1,('bridge',)),
           lambda:coalesce([],mode='bad')):
    try:fn()
    except (TypeError,ValueError):rejected+=1
assert rejected==6
results['10_input_boundaries']={'rejected':rejected}
report={'status':'PASS','check_groups':len(results),'nollm_source':'88d63b32329fbbcd18028de1ac83b2db3c988e33',
 'em_source':'c62b1472db2e6ad90e988247f9590e2cf62957e1','results':results,
 'limits':['No production state change','No semantic recall benchmark','No default dynamic inter-layer coverage execution',
           'No proof that finite beam is exact','No polynomial/constant-bit memory claim','No Foundation promotion or independent reviewer']}
args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
