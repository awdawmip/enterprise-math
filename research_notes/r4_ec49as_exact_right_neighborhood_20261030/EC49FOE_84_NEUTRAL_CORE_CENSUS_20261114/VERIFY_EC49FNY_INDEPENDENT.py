#!/usr/bin/env python3
"""Exact signed ordered-prefix rooted cover reference, reused from EC49FNY.

This file contains the table(words,keys,root) function of the earlier
VERIFY_EC49FNY_INDEPENDENT.py. No approximation, rounding or reordered words.
"""
INF=10**9

def table(words,keys,root):
    terms=[]
    for key in keys:
        terms.extend((label,code) for label,r,code in words[key] if r==root)
    labels=sorted({l for l,c in terms})
    idx={l:i for i,l in enumerate(labels)}
    children=[{}]
    terminal=[0]
    for l,code in terms:
        node=0
        for symbol in code:
            if symbol not in children[node]:
                children[node][symbol]=len(children)
                children.append({})
                terminal.append(0)
            node=children[node][symbol]
        terminal[node]|=1<<idx[l]
    def visit(node):
        partial={0:0}
        if terminal[node]:
            partial[terminal[node]]=0
        for child in children[node].values():
            d=visit(child);merged={}
            for m,cm in partial.items():
                for n,cn in d.items():
                    k=m|n;v=cm+cn
                    if v<merged.get(k,INF):merged[k]=v
            partial=merged
        return {m:c+(m!=0) for m,c in partial.items()}
    exact=visit(0)
    size=1<<len(labels)
    f=[INF]*size
    for m,c in exact.items():f[m]=c
    for j in range(len(labels)):
        for m in range(size):
            if not (m>>j)&1:
                f[m]=min(f[m],f[m|(1<<j)])
    return labels,idx,f,len(children)
