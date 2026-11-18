#!/usr/bin/env python3
"""Independent pure-Python finite model and signed-prefix OR-mask optimization for EC49FBC."""
from itertools import product, combinations
import json
from pathlib import Path
OPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
L='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
S=(0,0,4,1,16,32,8,2,0)
BASE=('de','ec','fe','feg','gef')
END=(2,0,0,0,0,0)
K9=(6,4,1,0,0,0)
def expand(w):return tuple(n for c in w for n in OPS[c])
def status(w):
    state=0
    for c in w:state=T[state][L.index(c)]
    return S[state]
def key_and_delta(w):
    key=[0]*6;delta=[0]*6
    for n in expand(w):
        k=abs(n)-1
        if n>0:key[k]+=1;delta[k]+=1
        else:delta[k]-=1
    return tuple(key),tuple(delta)
def edges(w):
    p=expand(w)
    return {p[:i] for i in range(1,len(p)+1)}
def rank(m):return all(m & v for v in (18,20,33,40))
W={h:[(w,key_and_delta(w)[0],status(w),expand(w)) for letters in product(L,repeat=h) if (w:=''.join(letters)) and key_and_delta(w)[1]==END and status(w)] for h in (4,5)}
PRE=set().union(*(edges(w) for w in BASE))
OLD=set(key_and_delta(w)[0] for w in BASE)
OTHER=sorted(set(x[1] for v in W.values() for x in v)-OLD)
assert len(PRE)==31 and len(OLD)==2 and len(W[4])==206 and len(W[5])==1062 and len(OTHER)==27
assert [k for k in OTHER if k[0]+k[1]>=10]==[K9]
def min_cost(allowed):
    root=[{},[]]
    for h in (4,5):
        for word,key,obs,prim in W[h]:
            if key not in allowed:continue
            node=root
            for signed_step in prim:
                node=node[0].setdefault(signed_step,[{},[]])
            node[1].append(obs << (0 if h==4 else 6))
    def fold(node,position=()):
        best={0:0}
        for sig in node[1]:best[sig]=0
        for n,child in node[0].items():
            child_dp=fold(child,position+(n,))
            nxt={}
            for m1,c1 in best.items():
                for m2,c2 in child_dp.items():
                    m=m1|m2; cost=c1+c2
                    if cost<nxt.get(m,10**8):nxt[m]=cost
            best=nxt
        if position not in PRE and position:
            for mask in best:
                if mask:best[mask]+=1
        return best
    states=fold(root)
    feasible=[v+31 for k,v in states.items() if rank(k&63) and rank((k>>6)&63)]
    return min(feasible,default=None)
C1={k:min_cost(OLD|{k}) for k in OTHER}
C2={tuple(pair):min_cost(OLD|set(pair)) for pair in combinations([k for k in OTHER if k!=K9],2)}
C3={pair:min_cost(OLD|set(pair)|{K9}) for pair in C2}
assert min(v for v in C1.values() if v is not None)==53
assert min(v for v in C2.values() if v is not None)==39
assert min(v for v in C3.values() if v is not None)==39
out={'source':'independent Python prefix-trie OR-mask implementation','H4_legal_words':len(W[4]),'H5_legal_words':len(W[5]),'key_classes':len(OTHER),'base_edges':len(PRE),'base_keys':[list(k) for k in sorted(OLD)],'one_added_key':{'tested':len(C1),'feasible':sum(v is not None for v in C1.values()),'minimum':min(v for v in C1.values() if v is not None)},'two_early_additional_reserving_H9':{'tested':len(C2),'feasible':sum(v is not None for v in C2.values()),'minimum':min(v for v in C2.values() if v is not None)},'two_additional_plus_early_H9':{'tested':len(C3),'feasible':sum(v is not None for v in C3.values()),'minimum':min(v for v in C3.values() if v is not None)}}
original=json.loads(Path(__file__).with_name('EXACT_REPORT_EC49FBC.json').read_text())
for row in original['single_new']['rows']:
    key=tuple(map(int,row['extra_key'].split(',')))
    assert C1[key]==(row['best'] or {}).get('cost')
for row in original['two_new_reserved_h9']['rows']:
    key=tuple(tuple(map(int,x.split(','))) for x in row['additional_keys'])
    assert C2[key]==(row['best'] or {}).get('cost')
for row in original['two_new_plus_early_h9']['rows']:
    key=tuple(tuple(map(int,x.split(','))) for x in row['additional_keys'][:2])
    assert C3[key]==(row['best'] or {}).get('cost')
Hs={2:('de','ec','fe'),3:('feg','gef'),4:('fegg','gefg'),5:('feggg','gefgg'),6:('fegccc','fegddd','gefccc','gefddd'),7:('fegccfg','fegddgf','gefccfg','gefddgf'),8:('feggfgfc','feggfgfd','gefgfgfc','gefgfgfd'),9:('feggfgfgf','gefgfgfgf')}
used=set();ks=set();cumulative={}
for h,ws in Hs.items():
    m=0
    for w in ws:
        k,d=key_and_delta(w); assert d==END and status(w)>0
        m|=status(w);ks.add(k);used.update(edges(w))
    assert rank(m)
    cumulative[str(h)]=len(used)
assert len(used)==131 and len(ks)==5
out['131_edge_full_witness']={'cumulative_native_signed_edges':cumulative,'total_edges':len(used),'distinct_keys':len(ks),'horizons_H2_H9':len(Hs)}
Path(__file__).with_name('CROSSCHECK_REPORT_EC49FBC.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(out,indent=2))
