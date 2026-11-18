#!/usr/bin/env python3
"""Python standard-library, independently structured trie DP audit of selected key sets."""
import collections,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'EC49FJD_RELEASE_B11_COMPLETE_20261111'))
from EC49FGW_RADIUS5_SCREEN import all_words,pref,raw_key,PIN
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
SETS=json.load(open('SCAN_SETS_ALL.json'))
CPP={int(row.split()[0]):int(row.split()[1]) for row in open('SCAN_ALL_RESULT.txt')}
CAT=list(all_words());assert len(CAT)==178850

def dp_cover(rows, labels):
    L={lab:i for i,lab in enumerate(labels)}
    kids=[{}];terminal=[0]
    for lab,ps in rows:
        u=0
        for p in ps:
            if p not in kids[u]:
                kids[u][p]=len(kids);kids.append({});terminal.append(0)
            u=kids[u][p]
        terminal[u] |= 1<<L[lab]
    def solve(u):
        states={0:0}
        if terminal[u]:states[terminal[u]]=0
        for v in kids[u].values():
            child=solve(v)
            merged={}
            for a,ca in states.items():
                for b,cb in child.items():
                    mask=a|b
                    merged[mask]=min(merged.get(mask,10**9),ca+cb)
            states=merged
        if u!=0:
            states={mask:cost+int(mask!=0) for mask,cost in states.items()}
        return states
    exact=solve(0)
    cover=[10**9]*(1<<len(labels))
    for mask,cost in exact.items():cover[mask]=cost
    for i in range(len(labels)):
        for mask in range(len(cover)):
            if not ((mask>>i)&1):cover[mask]=min(cover[mask],cover[mask|1<<i])
    return cover,L

def verify(which):
    K={tuple(x) for x in SETS[which]['keyset']}
    roots=collections.defaultdict(list)
    for lab,w in CAT:
        if raw_key(w) in K:
            ps=pref(w)
            roots[ps[0]].append((lab,ps))
    data={}
    choices=collections.defaultdict(list)
    for root,rows in roots.items():
        labs=sorted({lab for lab,ps in rows})
        costs,index=dp_cover(rows,labs)
        data[root]=costs
        for label,bit in index.items():choices[label].append((root,bit))
    assert len(choices)==24
    acc={r:0 for r in data}
    minimum=10**9
    def dfs(j, labs):
        nonlocal minimum
        if j==24:
            minimum=min(minimum,sum(data[r][acc[r]] for r in data))
            return
        for root,bit in choices[labs[j]]:
            acc[root]|=1<<bit
            dfs(j+1,labs)
            acc[root]&=~(1<<bit)
    ordered=sorted(choices,key=lambda k:len(choices[k]))
    dfs(0,ordered)
    assert minimum==CPP[which]
    print('EC49FKY_INDEPENDENT_PASS',which,'minimum',minimum,'native_roots',','.join(x.hex() for x in sorted(roots)),flush=True)

if __name__=='__main__':
    ids=[0,119,180,107,182,192] if len(sys.argv)==1 else list(map(int,sys.argv[1:]))
    for i in ids:verify(i)
