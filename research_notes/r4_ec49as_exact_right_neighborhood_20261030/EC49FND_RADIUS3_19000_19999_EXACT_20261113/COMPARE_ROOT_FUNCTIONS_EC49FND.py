#!/usr/bin/env python3
"""Recompute exact 8448 root-mask comparisons for EC49FND plateau.

Run next to cases.json and frozen original EC49FGW_RADIUS5_SCREEN.py.
Requires no floating arithmetic or endpoint projections.
"""
import collections, json
from pathlib import Path
from EC49FGW_RADIUS5_SCREEN import all_words, pref, raw_key, PIN
D = Path(__file__).resolve().parent
cases = json.loads((D/'cases.json').read_text())
assert cases['pin'] == PIN
catalog = list(all_words())
assert len(catalog) == 178850
keytypes = sorted({raw_key(w) for _,w in catalog})
pairs = [(19128,19553),(19291,19890),(19313,19947)]
expected = [
 [(2,4094,0),(326,3770,0),(21,235,0)],
 [(1,4095,0),(110,3986,0),(11,245,0)],
 [(0,4096,0),(0,4096,0),(0,256,0)]]

def exact_function(group, labels):
    label_pos = {lab:i for i,lab in enumerate(labels)}
    children=[{}]; terminals=[0]
    for lab,word in group:
        node=0
        for step in pref(word):
            nxt=children[node].get(step)
            if nxt is None:
                nxt=len(children)
                children[node][step]=nxt
                children.append({});terminals.append(0)
            node=nxt
        terminals[node] |= (1 << label_pos[lab])
    def solve(v):
        cost={0:0}
        if terminals[v]: cost[terminals[v]]=0
        for child in children[v].values():
            right=solve(child); merged={}
            for a,ca in cost.items():
                for b,cb in right.items():
                    mask=a|b; value=ca+cb
                    if value < merged.get(mask,10**9): merged[mask]=value
            cost=merged
        if v:
            return {mask:value+(mask!=0) for mask,value in cost.items()}
        return cost
    result=[10**9]*(1<<len(labels))
    for mask,value in solve(0).items(): result[mask]=value
    for bit in range(len(labels)):
        for mask in range(len(result)):
            if not mask>>bit&1:
                result[mask]=min(result[mask],result[mask|(1<<bit)])
    return result

functions={}
for idx in sorted(set(sum((list(x) for x in pairs),[]))):
    selected={keytypes[j] for j in cases['cases'][idx]}
    by_root=collections.defaultdict(list)
    for lab,word in catalog:
        if raw_key(word) in selected:
            by_root[pref(word)[0][0]].append((lab,word))
    for root,group in by_root.items():
        labels=tuple(sorted({lab for lab,_ in group}))
        functions[idx,root]=(labels,exact_function(group,labels))
        print('ROOT',idx,format(root,'02x'),len(labels),flush=True)
for i,(old,new) in enumerate(pairs):
    for j,root in enumerate([5,6,7]):
        labsA,fa=functions[old,root]
        labsB,fb=functions[new,root]
        assert labsA==labsB
        counts=(sum(a<b for a,b in zip(fa,fb)),
                sum(a==b for a,b in zip(fa,fb)),
                sum(a>b for a,b in zip(fa,fb)))
        assert counts==expected[i][j],(old,new,root,counts)
        print('COMPLETE_ROOT_MASK_COMPARISON_PASS',
              old,new,format(root,'02x'),counts)
print('PLATEAU_ROOT_DOMINANCE_PASS',sum(map(sum,expected[0]))+sum(map(sum,expected[1]))+sum(map(sum,expected[2])))
