#!/usr/bin/env python3
"""Independent selected-instance Python trie/assignment solver.
The frozen companion files EC49FGW_RADIUS5_SCREEN.py, cases.json, plus the
expanded lossless certificate are in the complete reproduction archive.
This checker does not consume any C++ root-function array.
"""
from EC49FGW_RADIUS5_SCREEN import all_words,pref,raw_key,PIN
from pathlib import Path
import json,collections,sys
D=Path(__file__).resolve().parent
cases=json.loads((D/'cases.json').read_text())
assert cases['pin']==PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
cat=list(all_words()); assert len(cat)==178850
keys=sorted({raw_key(w) for _,w in cat})

def root_min(words,labels):
    local={x:j for j,x in enumerate(labels)}
    tree=[{}]; final=[0]
    for lab,word in words:
        node=0
        for p in pref(word):
            if p not in tree[node]:
                tree[node][p]=len(tree);tree.append({});final.append(0)
            node=tree[node][p]
        final[node]|=1<<local[lab]
    def recurse(node):
        dp={0:0}
        if final[node]:dp[final[node]]=0
        for child in tree[node].values():
            dp_child=recurse(child);nd={}
            for mask,score in dp.items():
                for m,s in dp_child.items():
                    combined=mask|m;value=score+s
                    if value<nd.get(combined,10**9):nd[combined]=value
            dp=nd
        return {m:v+(node!=0 and m!=0) for m,v in dp.items()}
    f=[10**9]*(1<<len(labels))
    for mask,score in recurse(0).items():f[mask]=score
    for j in range(len(labels)):
        for mask in range(1<<len(labels)):
            if not(mask>>j&1):f[mask]=min(f[mask],f[mask|(1<<j)])
    return f,local

def solve(i):
    allowed={keys[k] for k in cases['cases'][i]}
    grouped=collections.defaultdict(list)
    for label,word in cat:
        if raw_key(word) in allowed:grouped[pref(word)[0]].append((label,word))
    fs={};op=collections.defaultdict(list)
    for r,arr in grouped.items():
        labels=sorted({lab for lab,_ in arr});f,local=root_min(arr,labels)
        fs[r]=f
        for lab,j in local.items():op[lab].append((r,j))
    assert len(op)==24
    order=sorted(op,key=lambda lab:len(op[lab]));bits={r:0 for r in fs}
    best=10**9; second=10**9; ways=0
    def dfs(j):
        nonlocal best,second,ways
        if j==24:
            val=sum(fs[r][bits[r]] for r in fs)
            if val<best:second,best,ways=best,val,1
            elif val==best:ways+=1
            elif val<second:second=val
            return
        for r,idx in op[order[j]]:
            bits[r]|=1<<idx;dfs(j+1);bits[r]&=~(1<<idx)
    dfs(0)
    return best,ways,second

if __name__=='__main__':
    raw={int(s.split()[0]):tuple(map(int,s.split()[1:4])) for s in (D/'EXACT_NATIVE_32000_32999.txt').read_text().splitlines()}
    for i in map(int,sys.argv[1:] or (32281,32551,32970,32997)):
        got=solve(i);expected=raw[i];assert got==expected,(i,got,expected)
        print('INDEPENDENT_EXACT_PASS',i,'best',got[0],'ways',got[1],'second',got[2],flush=True)
