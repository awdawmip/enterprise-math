#!/usr/bin/env python3
"""R671 exact S3 graph/scheduler quotient checker; Python standard library."""
from collections import Counter, defaultdict, deque
import json
LETTERS='ABC'
E=(0,1,2)
G={'A':(0,2,1),'B':(2,1,0),'C':(1,0,2)}
def mul(p,q): return tuple(p[q[i]] for i in range(3))
def rows(mask):
    return {a:''.join(b for j,b in enumerate(LETTERS) if mask & (1<<(3*i+j)))
            for i,a in enumerate(LETTERS)}
def next_states(st,H):
    h,last=st
    permitted=LETTERS if last=='_' else H[last]
    return {x:(mul(h,G[x]),x) for x in permitted}
def reachable(H):
    root=(E,'_')
    words={root:''}
    queue=deque([root])
    while queue:
        st=queue.popleft()
        for x,nxt in next_states(st,H).items():
            if nxt not in words:
                words[nxt]=words[st]+x
                queue.append(nxt)
    return words
def row_quotient(states,H):
    return len({(h,LETTERS if last=='_' else H[last]) for h,last in states})
def moore(states,H):
    states=tuple(states)
    def recolor(features):
        d={}
        return {s:d.setdefault(features[s],len(d)) for s in states}
    cls=recolor({s:s[0] for s in states})
    while True:
        signatures={}
        for s in states:
            go=next_states(s,H)
            signatures[s]=(s[0],tuple((x,cls[go[x]]) if x in go else (x,None)
                                      for x in LETTERS))
        nxt=recolor(signatures)
        if all((cls[a]==cls[b])==(nxt[a]==nxt[b])
               for a in states for b in states):
            return len(set(nxt.values()))
        cls=nxt
def run():
    histogram=Counter()
    by_edges=defaultdict(Counter)
    witnesses=[]
    for mask in range(512):
        H=rows(mask)
        R=reachable(H)
        n=row_quotient(R,H)
        assert n==moore(R,H),mask
        histogram[n]+=1
        by_edges[mask.bit_count()][n]+=1
        if mask.bit_count()==3 and n==19:
            witnesses.append((mask,H))
    assert sum(histogram.values())==512
    assert histogram[19]==74
    assert len(witnesses)==8
    assert max(n for e,d in by_edges.items() if e<=2 for n in d)==14
    samples={'empty':0,'complete':511,'no_repeat':238,'cycle':98,'path':170}
    expect={'empty':4,'complete':6,'no_repeat':19,'cycle':19,'path':13}
    for label,mask in samples.items():
        assert row_quotient(reachable(rows(mask)),rows(mask))==expect[label]
    W=reachable(rows(98))
    assert len(W)==19 and max(map(len,W.values()))==6
    result={
        'schema':'R671_EXACT_512_SCHEDULER_GRAPHS',
        'matrices_checked':512,
        'histogram':dict(sorted(histogram.items())),
        'edge_histogram':{str(k):dict(sorted(v.items())) for k,v in sorted(by_edges.items())},
        'max_at_most_two_edges':14,
        'three_edge_nineteen_masks':[m for m,H in witnesses],
        'n_nineteen':74,
        'samples':{k:{'mask':m,'minimal_states':expect[k],
                      'reachable_pairs':len(reachable(rows(m)))}
                   for k,m in samples.items()},
        'directed_cycle_shortest_words':[
            {'h':list(h),'last':l,'word':w}
            for (h,l),w in sorted(W.items(),key=lambda z:(z[0][1],z[0][0]))],
        'independent_moore_agreement':True,
        'pass':True,
    }
    print(json.dumps(result,indent=2,ensure_ascii=False,sort_keys=True))
if __name__=='__main__':
    run()
