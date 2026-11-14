"""R762AN exact single-trajectory diagnostics on the AK4 eight-state model."""
import json
from itertools import product
E=(0,1,2); C=(1,2,0); T=(1,0,2)
def mul(p,q):return tuple(p[i] for i in q)
frame={E}; pending=[E]
for h in pending:
    for p in (C,T):
        g=mul(p,h)
        if g not in frame:frame.add(g);pending.append(g)
X=sorted({(s,E) for s in range(3)}|{(0,h) for h in frame},key=str)
FAIL=('UNDEFINED',);X.append(FAIL)
def step(x,a):
    if x==FAIL:return FAIL
    s,h=x
    if a=='S' and h==E:return ((s+1)%3,h)
    if a=='C' and s==0:return(s,mul(C,h))
    if a=='T' and s==0:return(s,mul(T,h))
    return FAIL
def obs(x):
    if x==FAIL:return 'U'
    s,h=x
    return ('E' if s==0 else 'C')+('E' if h==E else 'C' if h in (C,mul(C,C)) else 'T')
def trajectory(x,w):
    out=[obs(x)]
    for a in w:
        x=step(x,a);out.append(obs(x))
    return tuple(out)
def policy(x):
    initial=obs(x)
    if initial in ('EE','U'):w=''
    elif initial=='EC':w='C'
    elif initial=='CE':w='S'
    elif initial=='ET':
        t=step(x,'T')
        w='TC' if obs(t)=='EC' else 'T'
    else:raise AssertionError(initial)
    # The feedback is read DURING this same trajectory, not from a fresh copy.
    return w,trajectory(x,w)
assert len(X)==9 and len({(w,tr) for x in X for w,tr in [policy(x)]})==9
assert max(len(policy(x)[0]) for x in X)==2
assert sum(len(policy(x)[0]) for x in X[:-1])==9
# Any static word destroys at least one initially indistinguishable pair
# on its very first action. This proves impossibility for ALL word lengths.
ce=[x for x in X if obs(x)=='CE']; ec=[x for x in X if obs(x)=='EC']
assert len(ce)==len(ec)==2
for a in 'SCT':
    assert (len({step(x,a) for x in ce})==1 or len({step(x,a) for x in ec})==1)
# Exhaustive small-horizon corroboration, not the basis for the universal claim.
fixed_counts={}
for k in range(6):
    fixed_counts[str(k)]=sum(len({trajectory(x,''.join(w)) for x in X})==len(X)
           for w in product('SCT',repeat=k))
assert not any(fixed_counts.values())
et=[x for x in X if obs(x)=='ET'];assert len(et)==3
assert max(len({obs(step(x,a)) for x in et}) for a in 'SCT')==2
print(json.dumps({'schema':'R762AN_SINGLE_TRAJECTORY_EXACT_V1','states':len(X),
 'live_states':len(X)-1,'adaptive_worst_case_events':2,
 'uniform_live_expected_events':'9/8','fixed_word_all_lengths_impossible':True,
 'fixed_word_length_0_to_5_complete_counts':fixed_counts,
 'ET_one_event_max_outputs':2,'policy_by_baseline':{'EE':'','U':'','EC':'C',
 'CE':'S','ET':'T then C if intermediate output EC'},
 'all_nine_policy_traces_unique':True,'checks_passed':True},sort_keys=True,indent=2))
