#!/usr/bin/env python3
"""Exact, dependency-free verification of the R189 source-only last-occurrence oracle.

Queries are nonempty sets U of <= b source names and return the most recently
occurring name in U or None. This is NOT a native X6 or BRC runtime test.
"""
from __future__ import annotations
from functools import lru_cache
from itertools import combinations, permutations
from hashlib import sha256
import json


def partial_orders(k):
    return [()] + [p for r in range(1, k+1) for p in permutations(range(k), r)]


def oracle(order, subset):
    chosen = set(subset)
    return next((x for x in reversed(order) if x in chosen), None)


def near_full_recover(order, k):
    assert k >= 3
    calls = 0
    primary = tuple(range(k-1))
    a = oracle(order, primary); calls += 1
    if a is None:
        x = oracle(order, (k-1,)); calls += 1
        return (() if x is None else (x,)), calls
    latest = oracle(order, (a,k-1)); calls += 1
    assert latest is not None
    remaining = set(range(k)) - {latest}
    descending = [latest]
    while remaining:
        v = oracle(order, remaining); calls += 1
        if v is None:
            break
        descending.append(v)
        remaining.remove(v)
    return tuple(reversed(descending)), calls


def exact_minimax(k, b):
    if b == 1 and k >= 2:
        return {"k":k,"aperture":b,"depth":None,
                "reason":"SINGLETON_ONLY_CANNOT_OBSERVE_ORDER"}
    universe = partial_orders(k)
    queries = [tuple(xs) for size in range(1,min(k,b)+1)
               for xs in combinations(range(k),size)]
    partitions = []
    for q in queries:
        partition = {}
        for i,s in enumerate(universe):
            v = oracle(s,q)
            partition[v] = partition.get(v,0) | (1<<i)
        partitions.append(partition)
    full = (1<<len(universe))-1
    attempts = []

    @lru_cache(None)
    def possible(belief,budget):
        if belief.bit_count()==1: return True
        if budget==0: return False
        options = []
        for q,parts in zip(queries,partitions):
            children=tuple(belief&v for v in parts.values() if belief&v)
            if len(children)<=1: continue
            if max(v.bit_count() for v in children)>(b+1)**(budget-1):
                continue
            options.append((max(v.bit_count() for v in children),q,children))
        for _,q,children in sorted(options,key=lambda x:(x[0],x[1])):
            if all(possible(ch,budget-1) for ch in children):
                return True
        return False

    optimum=None
    for budget in range(k if b>1 else 1,2*k+2):
        succeeds=possible(full,budget)
        attempts.append({"depth":budget,"feasible":succeeds})
        if succeeds:
            optimum=budget
            break
    assert optimum is not None

    def strategy(belief,budget):
        if belief.bit_count()==1:
            return ("leaf",belief.bit_length()-1)
        for q,parts in zip(queries,partitions):
            children=[(ans,belief&v) for ans,v in parts.items() if belief&v]
            if len(children)<=1: continue
            if all(possible(ch,budget-1) for _,ch in children):
                return ("query",q,{str(ans):strategy(ch,budget-1) for ans,ch in children})
        raise AssertionError("Feasible belief has no witness")

    tree=strategy(full,optimum)
    worst=0
    for i,order in enumerate(universe):
        node=tree; depth=0
        while node[0]=="query":
            node=node[2][str(oracle(order,node[1]))]
            depth+=1
        assert node==("leaf",i),(k,b,order,node,i)
        worst=max(worst,depth)
    assert worst==optimum

    def counts(node):
        if node[0]=="leaf": return (0,1)
        xs=[counts(ch) for ch in node[2].values()]
        return (1+sum(x[0] for x in xs),sum(x[1] for x in xs))
    nodes,leaves=counts(tree)
    digest=sha256(json.dumps(tree,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return {"k":k,"aperture":b,"states":len(universe),"query_types":len(queries),
            "depth":optimum,"attempts":attempts,"decision_nodes":nodes,
            "leaves":leaves,"all_states_decoded":True,"max_witness_depth":worst,
            "tree_sha256":digest,"memo_entries":possible.cache_info().currsize}


def main():
    matrix=[exact_minimax(k,b) for k in range(1,6) for b in range(1,k+1)]
    expected={
        (1,1):1,(2,1):None,(2,2):2,
        (3,1):None,(3,2):4,(3,3):3,
        (4,1):None,(4,2):6,(4,3):5,(4,4):4,
        (5,1):None,(5,2):8,(5,3):7,(5,4):6,(5,5):5
    }
    assert {(x["k"],x["aperture"]):x["depth"] for x in matrix}==expected
    scans=[]
    for k in range(3,9):
        count=0;worst=0
        for s in partial_orders(k):
            result,used=near_full_recover(s,k)
            assert result==s,(k,s,result)
            assert used<=k+1
            worst=max(worst,used);count+=1
        assert worst==k+1
        scans.append({"k":k,"aperture":k-1,"states":count,
                      "worst_queries":worst,"failures":0})
    report={
        "schema":"EM_R189_APERTURE_MINIMAX_EXACT_CHECK_V1",
        "scientific_input_pin":"43ec6098b1330ae86d0a7863be336c5d97f6ef34",
        "status":"PASS","arithmetics":"INTEGER_EXACT",
        "scope":"SOURCE_ONLY_LAST_OCCURRENCE_OBSERVER",
        "finite_minimax_k_le_5":matrix,
        "near_full_constructive_exhaustive_k_3_to_8":scans,
        "review":"NOT_REVIEWED","native_brc_integration":"NOT_EXECUTED",
        "claim_scope":"Finite minimax exact by full-belief DP; all-k theorem by symbolic argument"
    }
    print(json.dumps(report,ensure_ascii=False,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
