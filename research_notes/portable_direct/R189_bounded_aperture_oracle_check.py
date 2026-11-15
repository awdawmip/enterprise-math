#!/usr/bin/env python3
"""R189: exhaustive partial-history and exact minimax small-k checks.
Integer-only reference model for latest-present source oracle q_U.
"""
from itertools import combinations, permutations
from functools import lru_cache
import json, math

def partial_orders(k):
    return [p for r in range(k+1) for p in permutations(range(k),r)]

def q(history, block):
    B=set(block)
    return next((i for i in reversed(history) if i in B),None)

def tournament_recover(history,k,b):
    """b-ary winner tree over derived total order, capture all raw oracle answers.
    Then recover absent-prefix boundary without any new nonsingleton query.
    """
    assert 2<=b<=k
    raw=[]
    calls=0
    tie=list(range(k))
    rank={x:i for i,x in enumerate(history)}
    def greater(x,y):
        return (x in rank,rank.get(x,x if x not in rank else 0)) > (y in rank,rank.get(y,y if y not in rank else 0))
    # Derived order: absents ordered by id, present ordered by position.
    def query_max(candidates):
        nonlocal calls
        if not candidates: return None
        if len(candidates)==1: return candidates[0]
        ans=q(history,candidates)
        raw.append((frozenset(candidates),ans))
        calls+=1
        return max(candidates) if ans is None else ans
    # recursively build b-ary group partitions: each internal vertex at most b children
    nodes=[]
    def build(a):
        if len(a)==1:
            u=len(nodes); nodes.append({'kids':[], 'winner':a[0], 'parent':None});return u
        # contiguous partition into max b nonempty blocks, balanced for logarithmic depth
        group_count=min(b,len(a))
        blocks=[]
        z=len(a)//group_count; rem=len(a)%group_count
        pos=0
        for j in range(group_count):
            sz=z+(j<rem);blocks.append(a[pos:pos+sz]);pos+=sz
        ch=[build(block) for block in blocks]
        u=len(nodes)
        nodes.append({'kids':ch, 'winner':query_max([nodes[v]['winner'] for v in ch]), 'parent':None})
        for v in ch:nodes[v]['parent']=u
        return u
    root=build(list(range(k)))
    output=[]
    while nodes[root]['winner'] is not None:
        best=nodes[root]['winner'];output.append(best)
        node=next(i for i,x in enumerate(nodes) if not x['kids'] and x['winner']==best)
        nodes[node]['winner']=None
        while nodes[node]['parent'] is not None:
            node=nodes[node]['parent']
            kids=nodes[node]['kids'];cand=[nodes[u]['winner'] for u in kids if nodes[u]['winner'] is not None]
            nodes[node]['winner']=query_max(cand)
    output.reverse()
    assert output==sorted(range(k), key=lambda x:(x in rank,rank[x] if x in rank else x)),(k,b,history,output)
    # Witness lemma: for each consecutive pair, one queried subset includes both and has no larger element in *derived* order.
    order={v:i for i,v in enumerate(output)}
    raw_witness=[]
    for i,(x,y) in enumerate(zip(output,output[1:])):
        choices=[(block,ans) for block,ans in raw if x in block and y in block and max(order[z] for z in block)==i+1]
        assert choices,(k,b,history,x,y)
        raw_witness.append(choices[0])
    first_present=q(history,[output[0]]) is not None
    if first_present:
        m=0
    else:
        m=1
        while m<k and raw_witness[m-1][1] is None:
            m+=1
    recovered=tuple(output[m:])
    assert recovered==history,(k,b,history,recovered)
    return calls, len(raw_witness)

def finite_exact_minimax(k,b,unknown=False):
    states=partial_orders(k) if unknown else list(permutations(range(k)))
    queries=[tuple(q) for size in range(1 if unknown else 2,min(k,b)+1) for q in combinations(range(k),size)]
    # Each subset of states is represented by bitmask, queries partition by oracle answers.
    masks=[]
    for query in queries:
        out={}
        for idx,state in enumerate(states):
            key=q(state,query)
            out[key]=out.get(key,0)|(1<<idx)
        masks.append(tuple(out.values()))
    full=(1<<len(states))-1
    calls=0
    @lru_cache(maxsize=None)
    def dp(belief):
        nonlocal calls
        calls+=1
        if belief & (belief-1)==0: return 0
        best=len(states)
        for pm in masks:
            parts=[belief & group for group in pm]
            parts=[v for v in parts if v]
            if len(parts)<=1: continue
            # best possible under this query
            cost=1
            for group in sorted(parts,key=int.bit_count,reverse=True):
                child=dp(group)
                cost=max(cost,child+1)
                if cost>=best: break
            if cost<best:best=cost
        assert best<len(states)
        return best
    answer=dp(full)
    return {'k':k,'b':b,'known_support':not unknown,'exact_minimax':answer,'state_count':len(states),'beliefs_visited':calls}

def verify():
    rows=[]
    for k in range(2,8):
        states=partial_orders(k)
        for b in range(2,k+1):
            maximum=0;witness_count=0
            for s in states:
                n,w=tournament_recover(s,k,b)
                maximum=max(maximum,n);witness_count+=w
            rows.append({'k':k,'b':b,'partial_histories_checked':len(states),'max_tournament_subset_queries':maximum,'adjacent_witnesses':witness_count,'singleton_calls_each':1})
    minimax=[]
    for k in range(1,5):
        for b in range(2,k+1):
            known=finite_exact_minimax(k,b)
            unknown=finite_exact_minimax(k,b,True)
            assert unknown['exact_minimax']==known['exact_minimax']+1,(k,b,known,unknown)
            minimax.extend([known,unknown])
    return {'schema':'EM_R189_CHECK_V1','result':'PASS',
        'theorem':'Q_b(k) = C_b(k)+1 for integers k>=1, b>=2 (query sizes truncated to k)',
        'total_partial_history_checks':sum(x['partial_histories_checked'] for x in rows),
        'total_witness_checks':sum(x['adjacent_witnesses'] for x in rows),
        'tournament_rows':rows,'exact_decision_tree_rows':minimax,
        'arithmetic':'integers-only, exhaustive finite histories for k<=7, exact decision trees k<=4',
        'review':'NOT_REVIEWED'}

if __name__=='__main__':
    print(json.dumps(verify(),ensure_ascii=False,indent=2))
