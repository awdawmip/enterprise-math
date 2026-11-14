"""R762AM -- exact adaptive vs fixed diagnostic protocols on the AK4 partial model.
Python 3 standard library; deterministic complete finite enumerations, integer arithmetic.
"""
import json
from collections import deque
from functools import lru_cache
from itertools import combinations

E=(0,1,2); C=(1,2,0); T=(1,0,2)
def mul(p,q): return tuple(p[i] for i in q)
frame={E}; agenda=[E]
for h in agenda:
    for g in (C,T):
        v=mul(g,h)
        if v not in frame:
            frame.add(v); agenda.append(v)
assert len(frame)==6
states=sorted({(s,E) for s in range(3)} | {(0,h) for h in frame}, key=str)
FAIL=('UNDEFINED',)
states.append(FAIL); n=len(states); idx={x:i for i,x in enumerate(states)}
def step(x,a):
    if x==FAIL: return FAIL
    s,h=x
    if a=='S' and h==E: return ((s+1)%3,h)
    if a=='C' and s==0: return (s,mul(C,h))
    if a=='T' and s==0: return (s,mul(T,h))
    return FAIL
def obs(x):
    if x==FAIL: return 'U'
    s,h=x
    f='E' if h==E else ('C' if h in (C,mul(C,C)) else 'T')
    return ('E' if s==0 else 'C')+f

def word_obs(x,w):
    for a in w:x=step(x,a)
    return obs(x)

# Full generated transformation monoid, not a truncated word search.
ident=tuple(range(n)); transforms={ident:''}; q=deque([ident])
while q:
    f=q.popleft()
    for a in 'SCT':
        g=tuple(idx[step(states[i],a)] for i in f)
        if g not in transforms:
            transforms[g]=transforms[f]+a; q.append(g)
assert len(transforms)==75
# Retain each distinct output vector with its shortest/lexicographically first word.
vectors={}
for f,w in transforms.items():
    v=tuple(obs(states[i]) for i in f)
    if v not in vectors or (len(w),w)<(len(vectors[v]),vectors[v]):
        vectors[v]=w
assert len(vectors)==43

def partitions_for_count(count):
    out={}
    for v,w in vectors.items():
        grouping={}
        for i in range(count):grouping[v[i]]=grouping.get(v[i],0)|(1<<i)
        p=tuple(sorted(grouping.values()))
        if p not in out or (len(w),w)<(len(out[p]),out[p]):out[p]=w
    return out

def adaptive_minimax(count):
    parts=partitions_for_count(count)
    @lru_cache(None)
    def solve(mask):
        if mask.bit_count()<2:return (0,0,'',())
        candidates=[]
        for part,w in parts.items():
            children=tuple(sorted({mask & b for b in part}-{0}))
            if len(children)<2:continue
            sub=[solve(child) for child in children]
            depth=1+max(v[0] for v in sub)
            events=len(w)+max(v[1] for v in sub)
            candidates.append((depth,events,len(w),w,children))
        if not candidates:raise AssertionError('nonseparable states')
        return min(candidates)
    m=(1<<count)-1
    optimum=solve(m)
    return {'count':count,'candidate_partitions':len(parts),
            'minimum_adaptive_probes_including_empty_if_chosen':optimum[0],
            'worst_total_event_letters_at_minimum_depth':optimum[1]}

def fixed_minimum_after_free_baseline(count):
    pairs=list(combinations(range(count),2))
    full=(1<<len(pairs))-1
    candidate={}
    for v,w in vectors.items():
        mask=sum(1<<i for i,(a,b) in enumerate(pairs) if v[a]!=v[b])
        if mask not in candidate or (len(w),w)<(len(candidate[mask]),candidate[mask]):candidate[mask]=w
    baseline=next(m for m,w in candidate.items() if w=='')
    masks=list(candidate)
    for k in range(5):
        for choice in combinations(masks,k):
            union=baseline
            for x in choice:union|=x
            if union==full:
                return {'count':count,'pair_masks':len(masks),
                        'minimum_nonempty_fixed_words_after_baseline':k,
                        'witness':[candidate[m] for m in choice]}
    raise AssertionError('not covered')

def policy(x):
    baseline=word_obs(x,'')
    if baseline in ('EE','U'): return [baseline],0,0
    if baseline=='EC':w=['C']
    elif baseline=='CE':w=['S']
    elif baseline=='ET':
        first=word_obs(x,'T')
        w=['T','CT'] if first=='EC' else ['T']
    else:raise AssertionError(baseline)
    return [baseline]+[word_obs(x,z) for z in w],len(w),sum(map(len,w))

# Full identification with a *reset copy of the original state* for each word.
# Include the chosen event word in the signature, as branches may use different probes.
def policy_signature(x):
    o=word_obs(x,'')
    if o in ('EE','U'):return (o,)
    if o=='EC':return (o,'C',word_obs(x,'C'))
    if o=='CE':return (o,'S',word_obs(x,'S'))
    if o=='ET':
        p=word_obs(x,'T')
        return (o,'T',p,'CT',word_obs(x,'CT')) if p=='EC' else (o,'T',p)
    raise AssertionError(o)
assert len({policy_signature(x) for x in states})==n
assert max(policy(x)[1] for x in states)==2
assert max(policy(x)[2] for x in states)==3
# The ET baseline fiber is three states; every word has at most two outputs there.
et=[x for x in states if obs(x)=='ET']
assert len(et)==3
assert max(len({word_obs(x,w) for x in et}) for w in vectors.values())==2
assert {w for w in ('S','C','T') if len({word_obs(x,w) for x in et})>1}=={'T'}
# Exact expected costs on the uniform distribution on the eight live states.
assert sum(policy(x)[1] for x in states[:-1])==9
assert sum(policy(x)[2] for x in states[:-1])==11
adaptive=[adaptive_minimax(count) for count in (8,9)]
fixed=[fixed_minimum_after_free_baseline(count) for count in (8,9)]
assert [v['minimum_adaptive_probes_including_empty_if_chosen'] for v in adaptive]==[3,3]
assert [v['minimum_nonempty_fixed_words_after_baseline'] for v in fixed]==[4,4]
assert [v['worst_total_event_letters_at_minimum_depth'] for v in adaptive]==[3,3]
result={
 'schema':'R762AM_ADAPTIVE_DIAGNOSTICS_EXACT_V1',
 'scope':'AK4 eight reachable partial source/frame states; optional absorbing undefined',
 'total_states':n,'live_states':n-1,'generated_transformation_monoid':len(transforms),
 'distinct_observation_vectors':len(vectors),
 'adaptive_global_minimax':adaptive,
 'nonadaptive_after_free_initial_observation':fixed,
 'free_initial_observation_policy':{'EE':'stop','U':'stop','EC':'C','CE':'S',
    'ET':'T; if output EC then CT on another reset copy else stop',
    'maximum_additional_probe_count':2,'maximum_event_letters':3,
    'uniform_live_expected_additional_probes':'9/8',
    'uniform_live_expected_event_letters':'11/8'},
 'ET_baseline_fiber_size':len(et),
 'max_output_categories_from_one_any_length_probe_on_ET':2,
 'informative_single_letter_tests_on_ET':['T'],
 'validation':'Complete finite transformation monoid closure; exact partition/subset search; explicit adaptive-policy signatures on 9 states; integer costs',
 'checks_passed':True}
print(json.dumps(result,sort_keys=True,indent=2))
