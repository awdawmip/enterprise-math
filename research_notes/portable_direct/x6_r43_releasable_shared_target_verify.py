#!/usr/bin/env python3
"""Exact finite validator for a *candidate* two-source, p-port, one shared-target release model.

Source/Port labels and release remain individually named. P000 triadic transport
admissibility is assumed as a typed candidate, not proven by this script.
"""
import json
from collections import Counter, defaultdict, deque


def model(p):
    assert p >= 1
    labels = tuple([f'A{i}' for i in range(p)] + [f'B{i}' for i in range(p)] + ['R'])
    start = (-1,-1,-1) # fired port A, fired port B, currently occupying source: -1,0(A),1(B)
    def step(s, lab):
        a,b,occ=s
        if lab == 'R':
            return (a,b,-1) if occ != -1 else None
        origin = lab[0]
        port = int(lab[1:])
        if origin=='A' and a == -1 and (port != 0 or occ == -1):
            return (port,b,0 if port == 0 else occ)
        if origin=='B' and b == -1 and (port != 0 or occ == -1):
            return (a,port,1 if port == 0 else occ)
        return None
    queue=deque([start]); reached={start}; transitions={}
    while queue:
        s=queue.popleft()
        edges={lab:step(s,lab) for lab in labels if step(s,lab) is not None}
        transitions[s]=edges
        for nxt in edges.values():
            if nxt not in reached:
                reached.add(nxt); queue.append(nxt)
    return labels,start,transitions


def count_prefixes(start,transitions):
    counts=Counter()
    words={}
    def visit(s,w):
        counts[len(w)]+=1
        words[w]=s
        for lab,t in transitions[s].items():
            visit(t,w+(lab,))
    visit(start,())
    return counts,words


def exact_language_classes(transitions):
    """Partition based on exact successful words of length <=h, refining to stability."""
    states=tuple(sorted(transitions))
    cls={s:0 for s in states}
    hist=[]
    # max path length <=4, but iterate until signature partition truly stabilizes
    for depth in range(1,8):
        sig={s:tuple(sorted((lab,cls[t]) for lab,t in transitions[s].items())) for s in states}
        ids={x:i for i,x in enumerate(sorted(set(sig.values()),key=repr))}
        new={s:ids[sig[s]] for s in states}
        old_partition={(s,t):cls[s]==cls[t] for s in states for t in states}
        new_partition={(s,t):new[s]==new[t] for s in states for t in states}
        hist.append(len(ids))
        cls=new
        if old_partition==new_partition:
            return cls,hist,depth
    raise AssertionError('Partition did not stabilize')


def witness(s,t,edges,max_depth=5):
    """Shortest event word whose existence differs at two states, by finite BFS."""
    if s==t:return None
    q=deque([(s,t,())]); seen={(s,t)}
    while q:
        x,y,word=q.popleft()
        for lab in sorted(set(edges[x])|set(edges[y])):
            a,b=edges[x].get(lab),edges[y].get(lab)
            if (a is None)!=(b is None):return word+(lab,)
            if a is not None and (a,b) not in seen:
                seen.add((a,b));q.append((a,b,word+(lab,)))
    return None


def verify(p):
    _,start,T=model(p)
    counts,words=count_prefixes(start,T)
    predicted=[1,2*p,2*p*p,6*p-4,2]
    assert [counts.get(i,0) for i in range(5)]==predicted
    assert not any(k>4 for k in counts)
    assert len(words)==sum(predicted)
    assert len(T)==(p+1)*(p+3)
    cls,hist,stability_depth=exact_language_classes(T)
    assert len(set(cls.values()))==7
    masks={s:tuple(sorted(T[s])) for s in T}
    mask_class_count=len(set(masks.values()))
    assert mask_class_count==(7 if p>=2 else 5)
    mask_congruent=all((masks[s]!=masks[t] or cls[s]==cls[t]) for s in T for t in T)
    assert mask_congruent==(p>=2)
    # Crucial p=1 counterexample: A0 and A0 R B0 share one-symbol license {R}
    if p==1:
        short=words[('A0',)]
        long=words[('A0','R','B0')]
        assert masks[short]==masks[long]==('R',)
        assert witness(short,long,T)==('R','B0')
    # Validate congruence of the *full* future language quotient
    for s in T:
        for t in T:
            if cls[s]==cls[t]:
                assert masks[s]==masks[t]
                for lab in T[s]:assert cls[T[s][lab]]==cls[T[t][lab]]
            else:
                assert witness(s,t,T) is not None
    return {
        'port_count_per_source':p,
        'reachable_decorated_states':len(T),
        'successful_prefixes_by_length':[counts.get(i,0) for i in range(5)],
        'successful_prefixes_total':sum(counts.values()),
        'future_language_classes':len(set(cls.values())),
        'one_step_enabled_masks':mask_class_count,
        'enabled_mask_is_future_congruence':mask_congruent,
        'partition_classes_by_refinement_depth':hist,
        'partition_stable_at_refinement':stability_depth,
        'all_pairs_checked':len(T)**2,
    }

if __name__=='__main__':
    cases=[verify(p) for p in range(1,7)]
    assert cases[2]['successful_prefixes_by_length']==[1,6,18,14,2]
    assert cases[2]['successful_prefixes_total']==41
    print(json.dumps({
        'schema':'X6_R43_TARGET_RELEASE_EXACT_CHECK_V1',
        'status':'PASS',
        'scope':'one-shot sources A/B, p named ports each, only port0 shares one target; R enabled iff occupied; clearing target restores the other source port0, never resets consumed sources',
        'p_range':[1,6],
        'cases':cases,
        'max_distinguishing_word_for_equal_one_step_masks_p1':['R','B0'],
        'closed_form':{
            'reachable_states':'(p+1)(p+3)',
            'word_counts_by_length':['1','2p','2p^2','6p-4','2'],
            'future_language_classes':'7 for all p>=1',
            'enabled_masks':'5 if p=1; 7 if p>=2'
        },
        'scientific_status':'CONDITIONAL_FINITE_MODEL_THEOREM_WITH_EXACT_CHECK_NOT_REVIEWED'
    },ensure_ascii=False,indent=2,sort_keys=True))
