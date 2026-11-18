#!/usr/bin/env python3
"""Separate exact 4-colour native-prefix trie solver and BRC witness audit."""
import json, math, collections, sys
from pathlib import Path
here=Path(__file__).resolve().parent
sys.path.insert(0,str(here.parent/'EC49FFJ_NATIVE_PREFIX_TRIE_20261109'))
from BRC_ORIGINAL_MODEL_EC49FFJ import OPS, ORDER, observed, native, candidates
SIG=(1,2,4,8); ALL=15; INF=10**12

def check(key):
    child=[{}]; terminals=[0]; counts=collections.Counter()
    for word,sig in candidates(9,key):
        if sig not in SIG: continue
        assert observed(word)==sig
        counts[sig]+=1
        p=0
        for op in word:
            for step in OPS[op]:
                q=child[p].get(step)
                if q is None:
                    q=len(child);child[p][step]=q;child.append({});terminals.append(0)
                p=q
        terminals[p]|=1<<SIG.index(sig)
    F=[None]*len(child)
    for p in range(len(child)-1,-1,-1):
        current=[INF]*16
        s=terminals[p]
        while True:
            current[s]=0
            if s==0:break
            s=(s-1)&terminals[p]
        for v in child[p].values():
            out=current[:]
            branch=F[v]
            for mask,base in enumerate(current):
                if base==INF:continue
                remain=ALL^mask
                sub=remain
                while sub:
                    if branch[sub]!=INF:
                        cost=base+branch[sub]+1
                        if cost<out[mask|sub]:out[mask|sub]=cost
                    sub=(sub-1)&remain
            current=out
        F[p]=current
    return F[0][ALL], counts, len(child)

def main():
    data=json.loads((here/'EXACT_REPORT_EC49FFK.json').read_text())
    expected={(x,y,int(z)):v for z,rows in data['rows_by_z'].items() for x,y,v in rows}
    assert len(expected)==70
    seen=total_nodes=total_words=0
    for key,score in expected.items():
        best,counts,nodes=check(key)
        assert best==score,(key,best,score)
        assert all(counts[s]>0 for s in SIG)
        a=key[2]-1;cd=key[0]+key[1]-10;f=10-key[1]-2*key[2];g=10-key[0]
        all_count=sum(math.factorial(9)//math.prod(math.factorial(v) for v in (a,c,cd-c,key[2],f,g)) for c in range(cd+1))
        actual_count=sum(1 for _ in candidates(9,key))
        assert actual_count==all_count
        total_nodes+=nodes;total_words+=sum(counts.values());seen+=1
    assert (seen,total_words,total_nodes)==(70,625050,5320558)
    assert sorted(k for k,v in expected.items() if v==52)==[(x,11-x,1) for x in range(4,10)]
    print('SECONDARY_EXACT_PASS H9: 70 keys, 625050 nonzero words, 5320558 signed-prefix trie nodes, min52 at 6 keys')
if __name__=='__main__':main()
