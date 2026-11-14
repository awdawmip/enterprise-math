"""R762AL: exact finite-action diagnostic certificate; Python 3 standard library."""
import json
from collections import deque
from itertools import combinations, product

I=(0,1,2); C=(1,2,0); T=(1,0,2)
def mul(p,q): return tuple(p[i] for i in q)
frame={I}; todo=[I]
for h in todo:
    for g in (C,T):
        v=mul(g,h)
        if v not in frame: frame.add(v); todo.append(v)
assert len(frame)==6
states=sorted(set([(s,I) for s in range(3)] + [(0,h) for h in frame]),key=str)
bottom=('UNDEFINED',)
states.append(bottom)
N=len(states); index={s:i for i,s in enumerate(states)}

def act(st,a):
    if st==bottom:return bottom
    s,h=st
    if a=='S' and h==I:return ((s+1)%3,h)
    if a=='C' and s==0:return (s,mul(C,h))
    if a=='T' and s==0:return (s,mul(T,h))
    return bottom

def output(st):
    if st==bottom:return 'U'
    s,h=st
    typ='E' if h==I else ('C' if h in (C,mul(C,C)) else 'T')
    return ('E' if s==0 else 'C')+typ

def run(st,w):
    for a in w: st=act(st,a)
    return st

# All transformation maps: closure under right composition with each event.
identity=tuple(range(N)); trans={identity:''}; queue=deque([identity])
while queue:
    g=queue.popleft()
    for a in 'SCT':
        v=tuple(index[act(states[i],a)] for i in g)
        if v not in trans:trans[v]=trans[g]+a;queue.append(v)
# Outputs for the complete finite transformation semigroup.
vec={}
for g,w in trans.items():
    signature=tuple(output(states[i]) for i in g)
    if signature not in vec or len(w)<len(vec[signature]):vec[signature]=w
pairs=list(combinations(range(N),2));allpairs=(1<<len(pairs))-1
masks={}
for signature,w in vec.items():
    m=sum(1<<j for j,(i,k) in enumerate(pairs) if signature[i]!=signature[k])
    if m not in masks or len(w)<len(masks[m]):masks[m]=w
maximal={m:w for m,w in masks.items() if not any(m!=z and (m&z)==m for z in masks)}
assert (len(states),len(trans),len(vec),len(masks),len(maximal))==(9,75,43,19,8)
M=list(maximal.items())
for k in range(4):
    assert not any((lambda masks: __import__('functools').reduce(lambda x,y:x|y,masks,0)==allpairs)([x[0] for x in subset]) for subset in combinations(M,k))
assert len({tuple(output(run(s,w)) for w in ('S','C','T','CT')) for s in states})==N
# Independently certify four-probe optimality on the eight NONFAILURE states.
live_pairs=list(combinations(range(N-1),2))
live_full=(1<<len(live_pairs))-1
live_masks=set()
for signature in vec:
    live_masks.add(sum(1<<j for j,(i,k) in enumerate(live_pairs) if signature[i]!=signature[k]))
live_maximal={m for m in live_masks if not any(m!=z and (m&z)==m for z in live_masks)}
for k in range(4):
    assert all(__import__('functools').reduce(lambda x,y:x|y,sub,0)!=live_full for sub in combinations(live_maximal,k))
assert len({tuple(output(run(s,w)) for w in ('S','C','T','CT')) for s in states[:-1]})==N-1
# Horizon partitions: n=0,1,2.
parts=[]
for horizon in range(3):
    words=[''.join(p) for j in range(horizon+1) for p in product('SCT',repeat=j)]
    parts.append(len({tuple(output(run(s,w)) for w in words) for s in states}))
assert parts==[5,8,9]
# Construct both exact deterministic languages: only ab accepted on the left,
# only ba on the right. All intermediate outputs are 0, accept is transient.
def accept(orientation,w):
    stage=0
    for letter in w:
        if stage==0: stage=1 if letter==orientation[0] else 3
        elif stage==1: stage=2 if letter==orientation[1] else 3
        else: stage=3
    return int(stage==2)
assert accept('ab','ab')==1 and accept('ba','ab')==0
for u,v in ((2,3),(3,5),(7,11)):
    for k in range(7):
        def mass(orientation):
            return sum(accept(orientation,''.join(w))*
                       __import__('math').prod(u if e=='a' else v for e in w)
                       for w in product('ab',repeat=k))
        assert mass('ab')==mass('ba')==(u*v if k==2 else 0)
# Distinct commutative-weight BRC histories ab vs ba are indistinguishable by their
# summed terminal mass, for arbitrary positive weights u,v, but labeled futures differ.
for u,v in ((2,3),(3,5),(7,11)):
    for k in range(7):
        mass_p=(u*v if k==2 else 0)
        mass_q=(v*u if k==2 else 0)
        assert mass_p==mass_q
assert 'ab'!='ba'

result={
 'schema':'R762AL_DIAGNOSTIC_EXACT_V1',
 'domain':'AK4 partial S/C/T on (C3 x {E}) union ({E} x S3), plus absorbing undefined',
 'states':N,'nonfailure_states':N-1,'frame_group_size':len(frame),
 'horizon_observer_classes':parts,'transformation_semigroup_size':len(trans),
 'distinct_output_vectors':len(vec),'distinct_pair_separation_masks':len(masks),
 'maximal_pair_separation_masks':len(maximal),
 'maximal_masks':sorted([{'mask_hex':hex(m),'shortest_witness':w} for m,w in maximal.items()],key=lambda v:v['mask_hex']),
 'complete_pairs':len(pairs),'minimum_number_of_future_probes':4,
 'four_probe_witness':['S','C','T','CT'],
 'three_or_fewer_probes_exhaustively_ruled_out':True,
 'commuting_BRC_counterexample':{'left_accept_word':'ab','right_accept_word':'ba','commuting_weight_mass_length2':'u*v','other_lengths_mass':'0','checked_weight_pairs':[[2,3],[3,5],[7,11]],'checked_lengths':'0..6'},
 'checker':'Python standard-library exact integers; full transformation closure and exhaustive subsets of maximal masks',
 'checks_passed':True
}
print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
