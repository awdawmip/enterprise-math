#!/usr/bin/env python3
"""Exact paired-trajectory automaton for named positive-Q residual observations.
Shows two-read 5-bit recovery and finite unbounded 4-bit obstruction, p=5.
"""
import json,itertools,collections

def successors(p,x,h):
    return [x ^ sum(1 << i for i in ix)
            for j in range(h+1) for ix in itertools.combinations(range(p),j)]

def automaton(p=5,h=1):
    n=1<<p
    successor=[successors(p,x,h) for x in range(n)]
    trans=[sum(1<<(a*n+b) for a in successor[x] for b in successor[y])
           for x in range(n) for y in range(n)]
    diag=sum(1<<(x*n+x) for x in range(n))
    def equal_mask(q):return sum(1<<(x*n+y) for x in range(n) for y in range(n) if (x-y)%q==0)
    def post(bits,q):
        dest=0
        while bits:
            low=bits & -bits; i=low.bit_length()-1; bits-=low
            dest|=trans[i]
        return dest & equal_mask(q)
    # No known old bits: all pairs of initial current states possible.
    qs=list(range(3,16,2))
    seeds=[equal_mask(q) for q in qs]
    graph={}; state_order=[]; q=collections.deque()
    for state in seeds:
        if state not in graph:graph[state]=None;state_order.append(state);q.append(state)
    while q:
        state=q.popleft()
        nxt=tuple(post(state,m) for m in qs)
        graph[state]=nxt
        for t in nxt:
            if t not in graph:graph[t]=None;state_order.append(t);q.append(t)
    assert all(graph[state] is not None for state in graph)
    assert all(state & ~diag for state in graph), 'a 4-bit schedule unexpectedly recovers the terminal state'
    assert len(graph)==15, len(graph)
    assert set(v for outs in graph.values() for v in outs)<=set(graph)
    # Positional pair witnesses and forward transitions are checkable certificate.
    index={s:i for i,s in enumerate(state_order)}
    table=[]
    for s in state_order:
        witness=next((x,y) for x in range(n) for y in range(n) if x!=y and ((s>>(x*n+y))&1))
        table.append({'state':index[s], 'ambiguous_pair':list(witness),
                      'offdiagonal_pair_count':(s&~diag).bit_count(),
                      'successors':[index[t] for t in graph[s]]})
    # Positive construction: observe q=17 then q=31, one source flip or no-op.
    b=post(equal_mask(17),31)
    assert b & ~diag == 0
    assert (b & diag).bit_count()==n
    # A direct trajectory oracle, independent of bitset indexing, rechecks both windows.
    states=range(n)
    for a,bmod in [(17,31),(31,17)]:
        final={(u,v) for x in states for y in states if (x-y)%a==0
               for u in successor[x] for v in successor[y] if (u-v)%bmod==0}
        if (a,bmod)==(17,31):assert len(final)==n and all(u==v for u,v in final)
        else:assert any(u!=v for u,v in final)
    # All 4-bit schedules are in the full 15-node closure, and every node has an offdiagonal pair.
    return {
      'status':'ALL_EXACT_ASSERTIONS_PASSED',
      'domain':{'p':5,'J':'all 5 bits unknown','initial_missing_updates':0,
                'subsequent_flips_per_heartbeat':1,'raw_modulus':'odd fixed at each read; schedule may vary',
                '4_bit_candidates':qs,'constructive_5_bit_schedule':[17,31]},
      'exact_finite_certificate':{'reachable_pair_sets':len(graph),
                'initial_state_ids':[index[s] for s in seeds],
                'transition_moduli':qs,'states':table,
                'all_state_sets_have_distinct_endpoint_pair':True,
                'transition_closure_verified':True},
      'constructive_last_pair_count':n,
      'constructive_distinct_terminal_collisions':0,
      'minimum_max_per_sample_width_bits':5,
      'contrast':'reverse two-sample schedule (31,17) is not terminal-lossless; not a sliding-window claim',
      'proof_scope':'uniform terminal source recovery for an exact two-sample schedule; any-length 4-bit obstruction via exhaustive finite reachable set closure; auxiliary model only'
    }

if __name__=='__main__':
    print(json.dumps(automaton(),indent=2,ensure_ascii=False,sort_keys=True))
