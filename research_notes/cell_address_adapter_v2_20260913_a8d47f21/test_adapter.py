"""Run with Python 3.11+: python test_adapter.py [--geometry PATH].
Uses the unchanged repository geometry backend; no network or pip required.
"""
from collections import Counter
from dataclasses import replace
from fractions import Fraction
from itertools import product
from pathlib import Path
import argparse, hashlib, importlib.util, json, platform
from cell_address_adapter import *

ap = argparse.ArgumentParser()
local_backend=Path(__file__).parent/'vendor'/'geometry.py'
repo_backend=Path(__file__).resolve().parents[2]/'src'/'enterprise_math'/'geometry.py'
ap.add_argument('--geometry', type=Path, default=local_backend if local_backend.exists() else repo_backend)
args = ap.parse_args()
b = args.geometry.read_bytes()
blob = hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
assert blob == 'a1a8dc4d1ca53fde2ca00d9b944c1b8aa346a152', 'native backend changed: audit before reuse'
spec=importlib.util.spec_from_file_location('native_geometry', args.geometry)
g=importlib.util.module_from_spec(spec); spec.loader.exec_module(g)
frames=(Frame('A'),Frame('B',(2,-1,0,3,-2,1),(2,5,0,4,1,3)),Frame('C',(-3,4,1,0,2,-1),(5,4,3,2,1,0)))
ad=Adapter('X6-fixed-native-chart', frames, g.l1_distance)
keys=[ad.key(x) for x in product((-1,0,1),repeat=6)]
k0=ad.key(ZERO); k1=ad.key((1,0,0,0,0,0)); k2=ad.key((2,0,0,0,0,0))
S=LayerScheme('fixture-S',(k0,k1)); R=LayerScheme('fixture-R',(ad.key((9,0,0,0,0,0)),))
T={}; N={}; exclusions=0

def rejects(f):
    global exclusions
    try: f()
    except (ValueError,TypeError,KeyError): exclusions+=1
    else: raise AssertionError('invalid/ambiguous input accepted')

# New tests target multi-frame identity, serialization and separately mutable views.
for k in keys:
    aa=[ad.encode(k,f.tag) for f in frames]
    assert len(set(aa))==3 and len({ad.decode(a) for a in aa})==1
    for a in aa:
        assert ad.load(ad.dump(a))==a
        assert ad.decode(a)==k
        assert ad.view(a,S).address==ad.view(a,R).address==a
        for f in frames:
            c=ad.reframe(a,f.tag)
            assert ad.same_cell(a,c) and ad.displacement(a,c)==ZERO
    for i in range(6):
        for sign in (-1,1):
            # Same native direction, differing frame axis order; output in another frame.
            out=ad.move(aa[1],i,sign,'C'); x=list(k.native); x[i]+=sign
            assert ad.decode(out)==ad.key(tuple(x))
            assert ad.decode(ad.move(out,i,-sign,'A'))==k
T['multi_frame_cell_keys']=len(keys)
T['distinct_address_aliases']=3*len(keys)
T['serialization_roundtrips']=3*len(keys)
T['cross_frame_same_cell_and_zero_displacement']=9*len(keys)
T['primitive_steps_with_permuted_input_output_frames']=12*len(keys)
T['separate_layer_view_pairs']=3*len(keys)
N['layer_change_same_address']={'old':ad.view(ad.encode(k0,'A'),S).layer,'new':ad.view(ad.encode(k0,'A'),R).layer}
assert N['layer_change_same_address']=={'old':1,'new':10}

# Mixed-chart finite graph: canonicalize actual Cell keys, not address spelling.
small=[ad.key(x) for x in product((0,1),repeat=6)]
native={k:{ad.key(tuple(1-t if i==j else t for i,t in enumerate(k.native))) for j in range(6)} for k in small}
lookup={k:ad.encode(k,frames[i%3].tag) for i,k in enumerate(small)}
encoded={lookup[k]:{lookup[q] for q in qs} for k,qs in native.items()}
for i,k in enumerate(small):
    for q in small:
        a=ad.encode(k,'B'); c=ad.encode(q,'C')
        assert ad.steps(a,c)==g.graph_distance(encoded,lookup[k],lookup[q])
        assert ad.distance_squared(a,c)==sum((x-y)**2 for x,y in zip(k.native,q.native))
T['mixed_frame_existing_graph_backend_pairs']=len(small)**2

# No operational input can be a display reference, layer view or raw code digits.
a=ad.encode(k0,'A'); a1=ad.encode(k1,'A')
rejects(lambda: ad.decode(DisplayReference()))
rejects(lambda: ad.decode(ad.view(a,S)))
rejects(lambda: ad.decode(a.digits))
rejects(lambda: g.l1_distance(a,a1)) # Addresses are not Sequence[int].
rejects(lambda: a+a1)
rejects(lambda: ad.move(a,0,1,''))
for axis,sign in [(True,1),(6,1),(0,True),(0,0),(0,2)]:
    rejects(lambda axis=axis,sign=sign:ad.move(a,axis,sign))
raw=json.loads(ad.dump(a))
mutations=[]
for key,val in [('version',True),('version',1),('space','other'),('digits',[0]*6),('digits',[True]*6),('digits',[1]*5),('digits',[1.0]*6),('unexpected',0)]:
    x=dict(raw);x[key]=val;mutations.append(x)
x=json.loads(ad.dump(a));x['frame']['offset'][0]=1;mutations.append(x)
x=json.loads(ad.dump(a));x['frame']['order']=[0]*6;mutations.append(x)
x=json.loads(ad.dump(a));x['frame']['tag']='unknown';mutations.append(x)
for x in mutations: rejects(lambda x=x:ad.load(json.dumps(x)))
rejects(lambda:ad.load('{"version":2,"version":2}'))
rejects(lambda:Adapter(ad.space,(frames[0],frames[0]),g.l1_distance))
rejects(lambda:LayerScheme('empty',()))
rejects(lambda:CellKey(ad.space,(True,)*6))

# Preserve authoritative branch identities; duplicate chart declarations are NOT new branches.
records=[]
for f in frames:
    records.extend([EdgeRecord('physical-e01',ad.encode(k0,f.tag),ad.encode(k1,f.tag),0,1,Fraction(1,2)),
                    EdgeRecord('physical-e12',ad.encode(k1,f.tag),ad.encode(k2,f.tag),0,1,Fraction(1,3))])
edges=canonical_edges(ad,records)
assert len(edges)==2

def hist(edge_values):
    mass={k0:Counter({Fraction(1):1})}
    for _ in range(2):
        nxt={}
        for s,t,axis,sign,w in edge_values:
            for old,n in mass.get(s,{}).items():
                nxt.setdefault(t,Counter())[old*w]+=n
        mass=nxt
    return mass.get(k2,Counter())

naive=[(ad.decode(r.source),ad.decode(r.target),r.axis,r.sign,r.weight) for r in records]
assert hist(naive)==Counter({Fraction(1,6):9})
assert hist(edges.values())==Counter({Fraction(1,6):1})
# Synthetic pre-existing parallel branch: retain distinct physical ID even at same endpoints.
parallel=EdgeRecord('physical-parallel',ad.encode(k0,'B'),ad.encode(k1,'C'),0,1,Fraction(3,4))
with_parallel=canonical_edges(ad,records+[parallel])
assert hist(with_parallel.values())==Counter({Fraction(1,6):1,Fraction(1,4):1})
rejects(lambda:canonical_edges(ad,records+[replace(records[0],weight=Fraction(2,3))]))
rejects(lambda:canonical_edges(ad,[replace(records[0],target=ad.encode(k2,'B'))]))
rejects(lambda:canonical_edges(ad,[replace(records[0],weight=0.5)]))
T['duplicate_edge_records']=len(records)
T['canonical_physical_edges']=len(edges)
N['alias_branch_inflation']={'naive_two_step_paths':9,'correct':1,'genuine_parallel_paths':2}

# Time-varying address frame: E_{t+1} F_t D_t, not E_t F_t D_t at every epoch.
for k in keys:
    current=ad.encode(k,'A'); expected=list(k.native)
    for t in range(12):
        tag=frames[(t+1)%3].tag
        if t%2:
            current=ad.move(current,t%6,1,tag);expected[t%6]+=1
        else:
            current=ad.reframe(current,tag)
        assert ad.decode(current)==ad.key(tuple(expected))
T['time_dependent_frame_updates']=len(keys)*12
wrong=Address(a.space,frames[1],a.digits)
assert ad.decode(wrong)!=k0
N['copy_digits_into_new_frame_moves_stationary_cell']=list(ad.decode(wrong).native)

# Finite domains are transported as sets; do not reuse numeric code range bounds.
old=[ad.key((i,0,0,0,0,0)) for i in range(3)]
correct={ad.encode(k,'A') for k in old}
wrong_range={Address(a.space,frames[0],(i,1,1,1,1,1)) for i in range(1,4)}
assert {ad.decode(x) for x in correct}==set(old)
assert {ad.decode(x) for x in wrong_range}!=set(old)
N['old_domain_vs_naive_code_range']={'correct':[0,1,2],'naive':[-1,0,1]}
T['strict_invalid_input_rejections']=exclusions
T['backend_blob_sha1']=blob
out={'status':'PASS','python':platform.python_version(),'tests':T,'negative_controls':N,
     'scope':'new experimental adapter and pinned native backend, not production migration, full repo, or Lean'}
print(json.dumps(out,ensure_ascii=False,indent=2))
(Path(__file__).parent/'results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
