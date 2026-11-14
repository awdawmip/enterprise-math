#!/usr/bin/env python3
"""Independent exact Python enumeration of nine BRC cache-exchange pairs and eleven cases.
Usage: python VERIFY_EC49FOJ_INDEPENDENT.py master_and_radius3_cases.txt FOJ_EDGES_84.csv
Builds its own signed-prefix trie and integer cover DP; does not consume the C++ DP.
"""
from pathlib import Path
from itertools import product
from collections import defaultdict
import csv
import hashlib
import sys

INF = 10**9
ROOTS = (3, 5, 6, 7)
PAIRS = (
    (32315,32324), (32315,32279), (32315,32296),
    (32315,32264), (32318,32264), (32315,32292),
    (32315,32293), (32315,32294), (32275,32288),
)
EXPECTED = (-1,156,157,-1,164,165,171,174,-1)

def trie_cover(words, keys, root):
    terms=[(l,code) for k in keys for l,r,code in words[k] if r==root]
    labels=sorted(set(l for l,_ in terms))
    ix={l:i for i,l in enumerate(labels)}
    kids=[{}]
    terminal=[0]
    for l,word in terms:
        u=0
        for letter in word:
            if letter not in kids[u]:
                kids[u][letter]=len(kids)
                kids.append({})
                terminal.append(0)
            u=kids[u][letter]
        terminal[u]|=1<<ix[l]
    def dp_node(u):
        ways={0:0}
        if terminal[u]:
            ways[terminal[u]]=0
        for v in kids[u].values():
            child=dp_node(v)
            next_ways={}
            for m,cm in ways.items():
                for n,cn in child.items():
                    mask=m|n
                    cost=cm+cn
                    if cost<next_ways.get(mask,INF):
                        next_ways[mask]=cost
            ways=next_ways
        return {m:c+int(m!=0) for m,c in ways.items()}
    exact=dp_node(0)
    f=[INF]*(1<<len(labels))
    for m,c in exact.items():
        f[m]=c
    for j in range(len(labels)):
        for mask in range(len(f)):
            if not ((mask>>j)&1):
                f[mask]=min(f[mask],f[mask|(1<<j)])
    return ix,f

def parse(master, ids):
    assert hashlib.sha256(master.read_bytes()).hexdigest()==(
        "cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"
    )
    ts=iter(master.read_text().split())
    assert tuple(int(next(ts)) for _ in range(3))==(94,178850,38169)
    words=[]
    for key in range(94):
        n=int(next(ts))
        terms=[]
        for _ in range(n):
            l=int(next(ts))
            code=next(ts)
            terms.append((l,int(code[:2],16),tuple(bytes.fromhex(code[2:]))))
        words.append(terms)
    cases={}
    for i in range(38169):
        keys=tuple(int(next(ts)) for _ in range(7))
        if i in ids:
            cases[i]=keys
    assert len(cases)==len(ids)
    try:
        next(ts)
        raise AssertionError("Unexpected trailing source tokens")
    except StopIteration:
        pass
    return words,cases

def full_cost_map(words,keys,profile_cache):
    profiles={}
    for root in ROOTS:
        selected=tuple(k for k in keys if any(r==root for _,r,_ in words[k]))
        key=(root,selected)
        if key not in profile_cache:
            profile_cache[key]=trie_cover(words,selected,root)
        profiles[root]=profile_cache[key]
    opts={l:tuple(root for root in ROOTS if l in profiles[root][0]) for l in range(24)}
    assert all(opts.values())
    result={}
    for assignment in product(*(opts[l] for l in range(24))):
        by_root={r:0 for r in ROOTS}
        local={r:0 for r in ROOTS}
        for label,root in enumerate(assignment):
            by_root[root]|=1<<label
            local[root]|=1<<profiles[root][0][label]
        key=tuple(by_root[r] for r in ROOTS)
        val=sum(profiles[r][1][local[r]] for r in ROOTS)
        assert val<INF
        result[key]=val
    assert len(result)==__import__("math").prod(len(opts[l]) for l in range(24))
    return result

def first_separator(A,B):
    inf=10**9
    return min((min(A.get(k,inf),B.get(k,inf))
        for k in A.keys()|B.keys()
        if A.get(k,inf)!=B.get(k,inf)),default=-1)

def main(master,edgecsv):
    ids={i for pair in PAIRS for i in pair}
    words,cases=parse(master,ids)
    cache={}
    result={}
    for i in sorted(ids):
        result[i]=full_cost_map(words,cases[i],cache)
        print("INDEPENDENT_CASE",i,"full_assignments",len(result[i]),flush=True)
    rows={(int(x["src"]),int(x["dst"])):x for x in csv.DictReader(edgecsv.open())}
    for (a,b),expected in zip(PAIRS,EXPECTED):
        actual=first_separator(result[a],result[b])
        assert actual==expected
        assert actual==int(rows[a,b]["first_separation_threshold"])
        print("INDEPENDENT_EDGE_PASS",a,b,"first_separation",actual,flush=True)
    print("EC49FOJ_INDEPENDENT_PASS nine edges eleven cases all six finite separation levels and permanent equalities")

if __name__=="__main__":
    if len(sys.argv)!=3:
        raise SystemExit("Usage: python VERIFY_EC49FOJ_INDEPENDENT.py master.txt edges.csv")
    main(Path(sys.argv[1]),Path(sys.argv[2]))
