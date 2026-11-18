#!/usr/bin/env python3
"""EC49FBQ: exact fixed H2/H3 root-aware six-signature H8/H9 union costs.
Source: EC49FBP at c7e366fd4c9158e7d05f49231b858c7ff522ead0
Frozen scientific input fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
import json
from collections import Counter
from pathlib import Path

ALPHABET = 'acdefg'
P = {'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
T = ((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIGNATURE = (0,0,4,1,16,32,8,2,0)
COLOR = {1:0,2:1,4:2,8:3,16:4,32:5}
ROOT_WORDS = {2:['fe','ge'],3:['feg','gef']}

def primitive(w):
    return tuple(a for c in w for a in P[c])

ROOT_EDGES = {p[:j] for words in ROOT_WORDS.values() for w in words for p in [primitive(w)] for j in range(1,len(p)+1)}
assert len(ROOT_EDGES)==16, len(ROOT_EDGES)

class Node:
    __slots__='children','labels','prefix'
    def __init__(self,prefix=()):
        self.children={}
        self.labels=[]
        self.prefix=prefix

def counts(h,x,y,z,cd=None):
    ct={'a':z-1,'c':0,'d':0,'e':z,'f':h+1-y-2*z,'g':h+1-x}
    if cd:ct[cd]=x+y-h-1
    return ct

def generate(cnt, accepted, accept):
    if min(cnt.values())<0:return
    out=[]
    def walk(state, rem):
        if not rem:
            sig=SIGNATURE[state]
            if sig in accepted:accept(''.join(out),sig)
            return
        for i,c in enumerate(ALPHABET):
            if not cnt[c] or T[state][i]==8:continue
            cnt[c]-=1;out.append(c)
            walk(T[state][i],rem-1)
            out.pop();cnt[c]+=1
    walk(0,sum(cnt.values()))

def optimize(x,y,z):
    root=Node();terminals=[];by_sig=Counter()
    def add(w,s,h):
        node=root
        p=[]
        for op in w:
            for step in P[op]:
                p.append(step)
                if step not in node.children:node.children[step]=Node(tuple(p))
                node=node.children[step]
        assert len(p)==18+2*z
        node.labels.append(len(terminals))
        terminals.append((h,s,w));by_sig[s]+=1
    for cd in 'cd':
        generate(counts(8,x,y,z,cd),{1,2,4,8},lambda w,s:add(w,s,8))
    generate(counts(9,x,y,z),{16,32},lambda w,s:add(w,s,9))
    assert set(by_sig)==set(COLOR)
    explored=0
    def dp(node):
        nonlocal explored
        explored+=1
        states={0:(0,())}
        for tid in node.labels:
            mask=1<<COLOR[terminals[tid][1]]
            if mask not in states:states[mask]=(0,(tid,))
        for nxt in node.children.values():
            cm=dp(nxt)
            new=dict(states)
            cost_edge=int(nxt.prefix not in ROOT_EDGES)
            for m1,(v1,s1) in states.items():
                for m2,(v2,s2) in cm.items():
                    if not m2:continue
                    m=m1|m2
                    cost=v1+v2+cost_edge
                    old=new.get(m)
                    if old is None or cost<old[0] or (cost==old[0] and s1+s2<old[1]):
                        new[m]=(cost,s1+s2)
            states=new
        return states
    extra,ids=dp(root)[63]
    selected=[terminals[i] for i in ids]
    paths=[primitive(w) for h,s,w in selected]
    union=ROOT_EDGES | {p[:j] for p in paths for j in range(1,len(p)+1)}
    assert len(union)==16+extra
    assert len(ids)==6 and {s for h,s,w in selected}==set(COLOR)
    for p in paths:
        endpoint=[p.count(i)-p.count(-i) for i in range(1,7)]
        assert endpoint==[2,0,0,0,0,0],(p,endpoint)
    return {'M':[x,y,z,0,0,0],'root_edges':16,'extra_edges':extra,
      'joint_union_edges':len(union),'trie_nodes':explored,
      'per_signature':{str(s):by_sig[s] for s in COLOR},
      'optimal_words':[{'window':h,'signature':s,'word':w} for h,s,w in selected]}

def main():
    rec=[]
    for z in range(1,5):
        for x in range(2*z+1,10):
            y=10-x
            r=optimize(x,y,z);rec.append(r)
            print((x,y,z),r['joint_union_edges'],r['extra_edges'],r['trie_nodes'],flush=True)
    result={'schema':'EC49FBQ_FIXED_ROOT_H89_UNION_V1',
      'frozen_scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
      'root_words':ROOT_WORDS,'root_native_edges':16,
      'method':'exact rooted trie mask DP, zero incremental cost for fixed H2/H3 native prefix edges',
      'records':rec}
    with open(Path(__file__).with_name('EXACT_REPORT_EC49FBQ.regenerated.json'),'w') as f:
        json.dump(result,f,indent=2)
if __name__=='__main__':main()
