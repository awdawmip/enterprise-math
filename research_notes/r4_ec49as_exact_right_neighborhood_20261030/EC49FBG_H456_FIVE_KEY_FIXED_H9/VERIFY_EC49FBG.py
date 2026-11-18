#!/usr/bin/env python3
"""Independent standard-library multiset enumerator + exact min-plus prefix-tree DP.
Fixed native signed-X6 BRC finite subproblem EC49FBG.
"""
import json
from collections import defaultdict, Counter
from functools import lru_cache
OP = {'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
ALPH = 'acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
CLAUSES=(18,20,33,40)
EARLY = ['fe','ge','feg','gef']
HIGH=(6,4,1)

def native(w): return tuple(n for c in w for n in OP[c])
def evalword(w):
    delta=[0]*6;pos=[0]*6; state=0
    for c in w:
        state=T[state][ALPH.index(c)]
        for s in OP[c]:
            i=abs(s)-1;delta[i]+=1 if s>0 else -1
            if s>0:pos[i]+=1
    return tuple(pos),tuple(delta),SIG[state]
def rank(mask):return all(mask & k for k in CLAUSES)
def cmask(sig):return sum(1<<i for i,k in enumerate(CLAUSES) if sig&k)
@lru_cache(None)
def cand(key,h):
    x,y,z=key
    a=z-1; e=z;r=x+y-h-1;f=h+1-y-2*z;g=h+1-x
    if min(a,e,r,f,g)<0:return ()
    result=[]
    def each(counts,w,state):
        if len(w)==h:
            sig=SIG[state]
            if sig:
                pos,delta,actual=evalword(w)
                assert pos[:3]==key and pos[3:]==(0,0,0) and delta==(2,0,0,0,0,0) and actual==sig
                result.append((w,sig))
            return
        for i,c in enumerate(ALPH):
            if counts[i]:
                counts[i]-=1
                each(counts,w+c,T[state][i])
                counts[i]+=1
    for nc in range(r+1):
        each([a,nc,r-nc,e,f,g],'',0)
    return tuple(result)

def edge_union(words):
    result=set()
    for w in words:
        steps=native(w)
        for j in range(1,len(steps)+1):result.add(steps[:j])
    return result
FREE=edge_union(EARLY)
assert len(FREE)==16

def do(key):
    data={4:cand(key,4),5:cand(key,5)+cand(HIGH,5),6:cand(key,6)+cand(HIGH,6)}
    root={}
    nodes=[{'ch':{},'term':0,'prefix':()}]
    def insert(w,mask):
        current=0;prefix=()
        for step in native(w):
            prefix+=(step,)
            children=nodes[current]['ch']
            if step not in children:
                children[step]=len(nodes)
                nodes.append({'ch':{},'term':0,'prefix':prefix})
            current=children[step]
        nodes[current]['term'] |= mask
    for w in EARLY:insert(w,0)
    for h,entries in data.items():
        for w,sig in entries:insert(w,cmask(sig) << (4*(h-4)))
    dps=[None]*len(nodes)
    joins=0
    for i in range(len(nodes)-1,-1,-1):
        t=nodes[i]
        states={0:0}
        if t['term']:states[t['term']]=0
        for child in t['ch'].values():
            d={}
            for ma,ca in states.items():
                for mb,cb in dps[child].items():
                    joins+=1
                    m=ma|mb;v=ca+cb
                    if v<d.get(m,1000000):d[m]=v
            states=d
        if i and t['prefix'] not in FREE:
            for m in list(states):
                if m:states[m]+=1
        dps[i]=states
    return dict(low_key=key, min_edges=(16+dps[0][4095] if 4095 in dps[0] else None),
                candidates_by_horizon={str(h):len(v) for h,v in data.items()}, trie_nodes=len(nodes), joins=joins)

all_h4=defaultdict(int)
for x in range(0,9):
    for y in range(0,9):
        for z in range(1,5):
            key=(x,y,z)
            sig=0
            for _,s in cand(key,4):sig |=s
            if rank(sig):all_h4[key]=sig
assert len(all_h4)==9
results=[do(key) for key in sorted(all_h4)]
assert [r['min_edges'] for r in results]==[106,96,106,70,82,96,120,82,102]
best=min(r['min_edges'] for r in results if r['min_edges'] is not None)
assert best==70
witness={2:['fe','ge'],3:['feg','gef'],4:['fegc','fegd','gefc','gefd'],5:['fegfg','geffg'],6:['fegccc','fegddd','gefccc','gefddd']}
acc=[];seen=set();allkeys=set()
for h,words in witness.items():
    s=0
    for w in words:
        key,delta,sig=evalword(w)
        assert delta==(2,0,0,0,0,0) and sig
        allkeys.add(key);s|=sig
    assert rank(s)
    seen |=edge_union(words);acc.append((h,len(seen)))
assert len(seen)==70 and len(allkeys)==5
print(json.dumps({'schema':'EC49FBG_PYTHON_INDEPENDENT_CROSSCHECK','h4_rank_keys':list(all_h4),
                  'results':results,'minimum':best,'witness_cumulative':acc,'witness_total_keys':len(allkeys),'status':'PASS'},indent=2))
