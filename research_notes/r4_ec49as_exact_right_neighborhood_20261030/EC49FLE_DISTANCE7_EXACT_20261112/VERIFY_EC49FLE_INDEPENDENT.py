#!/usr/bin/env python3
"""Independent Python standard-library signed-native trie DP for EC49FLE.
Selection is a fixed subset of the full 810-case C++ optimization.
"""
import collections,sys
import REPRO_EC49FLE as source
from EC49FGW_RADIUS5_SCREEN import pref,raw_key
CAT=source.cat
CASES=source.d7
COSTS=list(source.costbytes)

def exact_root(rows,labs):
    labelid={v:i for i,v in enumerate(labs)}
    child=[{}];terminals=[0]
    for lab,word in rows:
        node=0
        for signed_prefix in pref(word):
            if signed_prefix not in child[node]:
                child[node][signed_prefix]=len(child)
                child.append({});terminals.append(0)
            node=child[node][signed_prefix]
        terminals[node]|=1<<labelid[lab]
    def traverse(node):
        states={0:0}
        if terminals[node]:states[terminals[node]]=0
        for nxt in child[node].values():
            branch=traverse(nxt);merged={}
            for a,ca in states.items():
                for b,cb in branch.items():
                    m=a|b;merged[m]=min(merged.get(m,10**9),ca+cb)
            states=merged
        return {m:c+(node!=0 and m!=0) for m,c in states.items()}
    exact=traverse(0)
    f=[10**9]*(1<<len(labs))
    for m,c in exact.items():f[m]=c
    for j in range(len(labs)):
        for m in range(len(f)):
            if (m>>j)&1==0:f[m]=min(f[m],f[m|1<<j])
    return f,labelid

def verify(caseidx):
    keys=set(CASES[caseidx][3]);roots=collections.defaultdict(list)
    for lab,word in CAT:
        if raw_key(word) in keys:roots[pref(word)[0]].append((lab,word))
    rootcost={};choices=collections.defaultdict(list)
    for root,rows in roots.items():
        f,lid=exact_root(rows,sorted({lab for lab,w in rows}));rootcost[root]=f
        for lab,bit in lid.items():choices[lab].append((root,bit))
    assert len(choices)==24
    picked={r:0 for r in rootcost};minimum=10**9
    labels=sorted(choices,key=lambda k:len(choices[k]))
    def visit(j):
        nonlocal minimum
        if j==24:
            minimum=min(minimum,sum(rootcost[r][picked[r]] for r in rootcost));return
        for r,bit in choices[labels[j]]:
            picked[r]|=1<<bit;visit(j+1);picked[r]&=~(1<<bit)
    visit(0)
    assert minimum==COSTS[caseidx],(caseidx,minimum,COSTS[caseidx])
    print('EC49FLE_PYTHON_INDEPENDENT_PASS',caseidx,minimum,flush=True)

if __name__=='__main__':
    for caseidx in map(int,sys.argv[1:] or [0,186,328,549,675,809]):verify(caseidx)
