#!/usr/bin/env python3
"""EC49FBP: exact six-signature H8/H9 union cost via native signed-X6 prefix-tree DP.
Scientific input frozen at fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
import collections
import json
from itertools import count

ALPHABET='acdefg'
P={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIGNATURE=(0,0,4,1,16,32,8,2,0)
COLOR={1:0, 2:1, 4:2, 8:3, 16:4, 32:5}
REQUIRED=(1<<6)-1

class Node:
    __slots__=('children','labels')
    def __init__(self): self.children={}; self.labels=[]

def counts(h,x,y,z,cd=None):
    r={'a':z-1,'c':0,'d':0,'e':z,'f':h+1-y-2*z,'g':h+1-x}
    if cd is not None: r[cd]=x+y-h-1
    return r

def generate(cnt, wanted, cb):
    if min(cnt.values())<0: return
    path=[]
    def rec(state, left):
        if left==0:
            sig=SIGNATURE[state]
            if sig in wanted: cb(''.join(path),sig)
            return
        for c in ALPHABET:
            if cnt[c]==0: continue
            next_state=T[state][ALPHABET.index(c)]
            if next_state==8: continue
            cnt[c]-=1;path.append(c)
            rec(next_state,left-1)
            path.pop();cnt[c]+=1
    rec(0,sum(cnt.values()))

def one_key(x,y,z, include_words=False):
    root=Node(); terminal_words=[]; counts_per_sig=collections.Counter();
    n8=n9=0
    def add(word,sig,h):
        nonlocal n8,n9
        if h==8:n8+=1
        else:n9+=1
        node=root; raw=[]
        for op in word:
            for signed_axis in P[op]:
                raw.append(signed_axis)
                if signed_axis not in node.children:node.children[signed_axis]=Node()
                node=node.children[signed_axis]
        expected=18+2*z
        if len(raw)!=expected:raise AssertionError(('native length',word,raw,expected))
        terminal_id=len(terminal_words)
        terminal_words.append((word, sig, h))
        node.labels.append(terminal_id)
        counts_per_sig[sig]+=1
    for c in 'cd':
        generate(counts(8,x,y,z,c),{1,2,4,8},lambda w,s:add(w,s,8))
    generate(counts(9,x,y,z),{16,32},lambda w,s:add(w,s,9))
    if set(counts_per_sig)!={1,2,4,8,16,32}:raise AssertionError(('missing signatures',(x,y,z),counts_per_sig))
    visited_nodes=0
    def dp(node):
        nonlocal visited_nodes
        visited_nodes+=1
        states={0:(0,())}
        for tid in node.labels:
            mask=1<<COLOR[terminal_words[tid][1]]
            states[mask]=(0,(tid,))
        for ch in node.children.values():
            child=dp(ch)
            new=dict(states)
            for m1,(cost1,ids1) in states.items():
                for m2,(cost2,ids2) in child.items():
                    if not m2:continue
                    m=m1|m2;val=cost1+cost2+1
                    old=new.get(m)
                    if old is None or val<old[0] or (val==old[0] and (ids1+ids2)<old[1]):
                        new[m]=(val,ids1+ids2)
            states=new
        return states
    optimal_cost,selected=dp(root)[REQUIRED]
    selection=[terminal_words[i] for i in selected]
    chosen_paths=[tuple(step for op in w for step in P[op]) for w,_,_ in selection]
    edge_union={p[:i] for p in chosen_paths for i in range(1,len(p)+1)}
    assert len(edge_union)==optimal_cost
    assert {sig for _,sig,_ in selection} == set(COLOR)
    assert len(selection)==6, selection
    for p in chosen_paths:
        point=collections.Counter(p)
        assert point[1]-point[-1]==2
        assert point[2]-point[-2]==0
        assert point[3]-point[-3]==0
    res={'M':[x,y,z,0,0,0], 'primitive_length':18+2*z,
         'H8_accepted':n8,'H9_FG_accepted':n9,
         'per_signature':{str(s):counts_per_sig[s] for s in (1,2,4,8,16,32)},
         'trie_nodes':visited_nodes,'optimal_union_edges':optimal_cost,
         'optimal_words':[{'window':h,'signature':sig,'word':word} for word,sig,h in selection]}
    if include_words:res['candidate_words']=terminal_words
    return res

def main():
    records=[]
    for z in range(1,5):
        for x in range(2*z+1,10):
            y=10-x
            rec=one_key(x,y,z)
            records.append(rec)
            print(rec['M'][:3],rec['optimal_union_edges'],rec['H8_accepted'],rec['H9_FG_accepted'],rec['trie_nodes'], flush=True)
    result={'schema':'EC49FBP_H8_H9_SIX_SIGNATURE_EXACT_UNION_V1',
            'date':'2026-11-05','frozen_scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
            'status':'PASS','algorithm':'exact rooted signed-native prefix-trie set-cover DP over all 64 signature masks',
            'records':records}
    out='EXACT_REPORT_EC49FBP.regenerated.json'
    with open(out,'w') as f:json.dump(result,f,indent=2,ensure_ascii=False)
    print('written',out)
if __name__=='__main__':main()
