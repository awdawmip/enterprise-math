#!/usr/bin/env python3
"""R681 exact integer state census: R680 V27/V29 PASS selector with V17 slot carry."""
from collections import Counter, defaultdict
from itertools import combinations, permutations
import json

TRIADS = tuple(combinations(range(6),3))
MATCH = (
    ((0,1),(2,3),(4,5)), ((0,2),(1,4),(3,5)),
    ((0,3),(1,5),(2,4)), ((0,4),(1,3),(2,5)),
)
PASS = ((0,1),(1,2),(2,0))
U0 = ((-4,-3,-2,10),(-3,-2,-4,10),(-2,-4,-3,10),
      (2,4,3,-10),(3,2,4,-10),(4,3,2,-10))
W = (-1,1,-2,-1)
K = 7
WORDS = ((),)+tuple((i,) for i in range(3))+tuple(permutations(range(3),2))+tuple(permutations(range(3),3))
assert len(WORDS)==16 and len(set(WORDS))==16

def v23(s,matching):
    if any((a in s)+(b in s)!=1 for a,b in matching):
        return 0
    return 1 if sum(b in s for a,b in matching)%2==0 else -1

C = {s:tuple(v23(s,m) for m in MATCH) for s in TRIADS}
N = {s:tuple(t for t in TRIADS if len(set(s)&set(t))==2) for s in TRIADS}
assert len(set(C.values()))==20 and all(len(N[s])==9 for s in TRIADS)

def prefix(u0,word):
    u=list(u0)
    M=[[0]*4 for _ in range(4)]
    yield tuple(u),tuple(tuple(x) for x in M)
    for e in word:
        a,b=PASS[e];M[a][b]+=1;u[a]+=1;u[b]-=1
        yield tuple(u),tuple(tuple(x) for x in M)

def phi(s,t,u,M):
    return (sum(u[i]*C[t][i] for i in range(4))
            +sum(C[s][i]*(M[i][j]-M[j][i])*C[t][j]
                 for i in range(4) for j in range(4)))

def next_triad(s,u,M):
    scores={t:K*phi(s,t,u,M)+sum(W[i]*C[t][i] for i in range(4))
            for t in N[s]}
    top=max(scores.values())
    candidates=[t for t in scores if scores[t]==top]
    assert len(candidates)==1
    return candidates[0]

def carry(frame,target):
    a=set(frame);b=set(target)
    assert len(a & b)==2
    outgoing=next(iter(a-b));incoming=next(iter(b-a))
    result=tuple(incoming if z==outgoing else z for z in frame)
    assert tuple(sorted(result))==target
    return result

def frame_at(u,word,s):
    frame=tuple(s)
    for up,M in list(prefix(u,word))[1:]:
        T=next_triad(tuple(sorted(frame)),up,M)
        frame=carry(frame,T)
    return frame

def label(s):return ''.join(map(str,s))
def label_word(w):return ''.join('ABC'[x] for x in w)

s_hist=Counter();f_hist=Counter();ts_hist=Counter();tf_hist=Counter()
s_total=f_total=changed_contexts=pair_count=0
critical=None
for u in U0:
    for s0 in TRIADS:
        fibers=defaultdict(list)
        for word in WORDS:
            f=frame_at(u,word,s0)
            fibers[tuple(sorted(word))].append((word,tuple(sorted(f)),f))
        assert len(fibers)==8
        ns=sum(len(set(x[1] for x in v)) for v in fibers.values())
        nf=sum(len(set(x[2] for x in v)) for v in fibers.values())
        s_hist[ns]+=1;f_hist[nf]+=1
        s_total+=ns;f_total+=nf
        final=fibers[(0,1,2)]
        ts_hist[len(set(x[1] for x in final))]+=1
        tf_hist[len(set(x[2] for x in final))]+=1
        changed=False
        for mask,group in fibers.items():
            for i,x in enumerate(group):
                for y in group[i+1:]:
                    if x[1]==y[1] and x[2]!=y[2]:
                        pair_count+=1
                        changed=True
                        assert mask==(0,1,2)
        if changed:
            changed_contexts+=1
            assert critical is None
            critical=(u,s0,final)

assert s_total==1141 and f_total==1143
assert dict(sorted(s_hist.items()))=={8:59,9:14,10:10,11:10,12:21,13:3,14:3}
assert dict(sorted(f_hist.items()))=={8:59,9:14,10:10,11:10,12:21,13:2,14:3,15:1}
assert dict(sorted(ts_hist.items()))=={1:59,2:29,3:27,4:5}
assert dict(sorted(tf_hist.items()))=={1:59,2:29,3:26,4:5,5:1}
assert (changed_contexts,pair_count)==(1,3)
u,s0,final=critical
assert u==(3,2,4,-10) and s0==(1,4,5)
witness={label_word(word):{'triad':label(s),'frame':label(f)} for word,s,f in final}
assert witness=={
 'ABC':{'triad':'124','frame':'124'},
 'ACB':{'triad':'015','frame':'105'},
 'BAC':{'triad':'345','frame':'345'},
 'BCA':{'triad':'015','frame':'015'},
 'CAB':{'triad':'345','frame':'543'},
 'CBA':{'triad':'345','frame':'543'},
}
assert carry((1,0,5),(0,1,2))==(1,0,2)
assert carry((0,1,5),(0,1,2))==(0,1,2)
triad_mass=Counter(v['triad'] for v in witness.values())
frame_mass=Counter(v['frame'] for v in witness.values())
assert dict(triad_mass)=={'124':1,'015':2,'345':3}
assert dict(frame_mass)=={'124':1,'105':1,'345':1,'015':1,'543':2}

evidence={
 'schema':'R681_V17_FRAME_OBSERVER_RESIDUAL_V1',
 'status':'AUTHOR_SIDE_EXACT_FINITE_CERTIFICATE',
 'frozen_science':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
 'predecessor':'R680@151d820a1c776fe4b1401ab0a23b1d0867c13883',
 'six_baseline_u':[list(u) for u in U0],
 'primitive_PASS':['A:0>1','B:1>2','C:2>0'],
 'score':{'K':K,'w':list(W)},
 'contexts':120,'legal_event_words_per_context':16,'raw_histories':1920,
 'summed_minimal_ledger_unordered_triad_states':s_total,
 'summed_minimal_ledger_ordered_frame_states':f_total,
 'context_histogram_unordered':dict(sorted(s_hist.items())),
 'context_histogram_ordered':dict(sorted(f_hist.items())),
 'terminal_context_histogram_unordered':dict(sorted(ts_hist.items())),
 'terminal_context_histogram_ordered':dict(sorted(tf_hist.items())),
 'contexts_with_same_M_S_but_different_F':changed_contexts,
 'same_M_S_different_F_word_pairs':pair_count,
 'witness':{'initial_u':list(u),'initial_S':label(s0),'terminal_by_PASS_order':witness,
            'triad_positive_mass':dict(sorted(triad_mass.items())),
            'frame_positive_mass':dict(sorted(frame_mass.items())),
            'common_next_triad':'012','ACB_next_frame':'102','BCA_next_frame':'012'},
 'limitations':'Finite fixed R680 scores, six R679 biases, at most one A/B/C PASS each; no autonomous X6 scheduler, V39 j or independent Driver acceptance.'
}
with open('R681_EVIDENCE.json','w',encoding='utf-8') as f:
    json.dump(evidence,f,ensure_ascii=False,sort_keys=True,indent=2)
    f.write('\n')
print(json.dumps({k:evidence[k] for k in ('raw_histories','summed_minimal_ledger_unordered_triad_states','summed_minimal_ledger_ordered_frame_states','same_M_S_different_F_word_pairs','witness')},ensure_ascii=False,indent=2))
print('R681_V17_ORDERED_FRAME_BRC_FIBER_EXACT_PASS')
