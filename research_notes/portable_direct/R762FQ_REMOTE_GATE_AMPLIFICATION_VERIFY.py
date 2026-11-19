#!/usr/bin/env python3
"""Exact, dependency-free verifier for R762FQ candidate triad matching gates.
Python 3.10+, no floating point. Run: python R762FQ_REMOTE_GATE_AMPLIFICATION_VERIFY.py
"""
from collections import Counter
from itertools import product
from pathlib import Path
import json

def model(m):
    k = 2*m+1
    allowed = {1: ((1,1),)}
    edges = []
    for r in range(1,m+1):
        a,b=2*r,2*r+1
        allowed[a]=((a,a),(a,b),(b,b))
        allowed[b]=((b,b),(b,a),(a,a))
        edges.append((a,b))
    return k, allowed, edges

def enumerate_legal(k, allowed):
    # Direct matching DFS, not a hardcoded enumeration of 3^m states.
    states=[]
    def visit(row,used_b,used_c,partial):
        if row>k:
            states.append(tuple(partial))
            return
        for j,l in allowed[row]:
            if j in used_b or l in used_c:
                continue
            partial.append((j,l))
            visit(row+1, used_b|{j}, used_c|{l}, partial)
            partial.pop()
    visit(1,set(),set(),[])
    return states

def swap(state,edge):
    a,b=edge
    z=list(state)
    z[a-1],z[b-1]=z[b-1],z[a-1]
    return tuple(z)

def signatures(states,edges,h):
    present=set(states)
    E={s:s[0] for s in states}
    for _ in range(h):
        F={}
        for s in states:
            F[s]=(s[0], tuple(E[t] if t in present else 'BLOCK'
                                 for t in (swap(s,e) for e in edges)))
        E=F
    return E

def word_signature(state, edges, present, h):
    out=[]
    for depth in range(h+1):
        for word in product(range(len(edges)), repeat=depth):
            z=state
            blocked=False
            for edge_no in word:
                z=swap(z,edges[edge_no])
                if z not in present:
                    blocked=True
                    break
            out.append('BLOCK' if blocked else z[0])
    return tuple(out)

def check(m):
    k, allowed, edges = model(m)
    states=enumerate_legal(k,allowed)
    present=set(states)
    assert len(states)==len(present)==3**m
    assert all(s[0]==(1,1) for s in states)
    gate={s:tuple(int(swap(s,e) not in present) for e in edges) for s in states}
    counts=Counter(gate.values())
    assert len(counts)==2**m
    for bits in product((0,1), repeat=m):
        assert counts[bits]==2**(m-sum(bits))
    levels=[signatures(states,edges,h) for h in range(4)]
    assert len(set(levels[0].values()))==1
    for level in levels[1:]:
        fibers={}
        for s in states:
            fibers.setdefault(gate[s],set()).add(level[s])
        assert len(fibers)==2**m
        assert all(len(value)==1 for value in fibers.values())
        assert len({next(iter(value)) for value in fibers.values()})==2**m
    pair_checks=0
    if m<=3:
        independent={s:word_signature(s,edges,present,3) for s in states}
        assert len(set(independent.values()))==2**m
        for x in states:
            for y in states:
                assert (independent[x]==independent[y])==(gate[x]==gate[y])
                pair_checks+=1
    return {
        "m":m,"k":k,"legal_histories":len(states),
        "current_classes":1,"one_step_classes":len(counts),
        "horizon_2_classes":len(set(levels[2].values())),
        "horizon_3_classes":len(set(levels[3].values())),
        "fiber_by_blocked_count": {
            str(z):{"number_of_classes":sum(sum(bits)==z for bits in counts),
                    "fiber_size":2**(m-z)}
            for z in range(m+1)
        },
        "minimal_one_step_bits":m,
        "full_provenance_bits":(3**m-1).bit_length(),
        "independent_word_pair_checks":pair_checks
    }

if __name__=="__main__":
    results=[check(m) for m in range(1,7)]
    evidence={
        "schema":"R762FQ_REMOTE_GATE_AMPLIFICATION_V1",
        "status":"PASS",
        "arithmetic":"exact integer and combinatorial checks only",
        "coverage":"all tensor-legal states, m=1..6; recurrence h=0..3; independent known words m=1..3, h<=3",
        "results":results,
        "general_theorem":"AUTHOR_PROVED_FOR_ALL_M>=1_AND_ALL_FINITE_H>=1",
        "independent_review":"NOT_REVIEWED"
    }
    filename=Path(__file__).with_name("R762FQ_REMOTE_GATE_AMPLIFICATION_EVIDENCE.json")
    filename.write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(evidence,ensure_ascii=False,indent=2))
