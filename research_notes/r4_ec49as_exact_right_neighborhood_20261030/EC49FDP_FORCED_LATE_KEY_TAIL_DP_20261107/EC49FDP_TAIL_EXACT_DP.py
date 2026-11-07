#!/usr/bin/env python3
"""EC49FDP exact H8/H9 six-signature tail relaxation.
Frozen science: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab
Usage: python EC49FDP_TAIL_EXACT_DP.py > tail_results.json
No third-party dependencies. Every witness is independently recounted.
The reported bound is for the specified early seed and late windows,
not a solution to the full H2..H9 minimization.
"""
from collections import defaultdict
from functools import lru_cache
import json

PIN="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
TRANS=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
       (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
       (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
LETTERS="acdefg"
PRIM={"a":(-1,-1),"c":(1,2,-1,-2),"d":(2,1,-2,-1),
      "e":(3,1,1,-3),"f":(1,-1),"g":(2,-2)}
SEED={2:["de","ed","ce","ec"],3:["feg","gef"]}
KEYS=[(3,7,1),(4,6,1),(5,5,1),(5,5,2),(6,4,1),(6,4,2),
      (7,3,1),(7,3,2),(7,3,3),(8,2,1),(8,2,2),(8,2,3),
      (9,1,1),(9,1,2),(9,1,3),(9,1,4)]

def native(word):
    return tuple(step for letter in word for step in PRIM[letter])

def prefix_set(word):
    seq=native(word)
    return {seq[:i] for i in range(1,len(seq)+1)}

PAID=set().union(*(prefix_set(w) for a in SEED.values() for w in a))
assert len(PAID)==42

@lru_cache(None)
def language(h,k):
    x,y,z=k
    r=x+y-h-1
    a=z-1; e=z; f=h+1-y-2*z; g=h+1-x
    if min(r,a,e,f,g)<0: return ()
    result=[]
    def visit(counts,state,word):
        if sum(counts)==0:
            if SIG[state]:result.append((SIG[state],word))
            return
        for i,amount in enumerate(counts):
            nxt=TRANS[state][i]
            if amount and nxt!=8:
                new=list(counts);new[i]-=1
                visit(tuple(new),nxt,word+LETTERS[i])
    for c in range(r+1):
        visit((a,c,r-c,e,f,g),0,"")
    return tuple(result)

def solve(k):
    entries=[(sig,word,native(word))
             for h in (8,9) for sig,word in language(h,k)
             if (h==8 and sig in (1,2,4,8))
             or (h==9 and sig in (16,32))]
    counts={str(s):sum(x[0]==s for x in entries)
            for s in (1,2,4,8,16,32)}
    if not all(counts.values()):
        return {"key":list(k),"feasible":False,"counts":counts}
    nodes=[()];children=[{}];terminal=[0];term_word=[{}]
    for sig,w,steps in entries:
        p=0
        for v in steps:
            q=children[p].get(v)
            if q is None:
                q=len(nodes)
                children[p][v]=q
                nodes.append(nodes[p]+(v,))
                children.append({});terminal.append(0);term_word.append({})
            p=q
        terminal[p]|=sig
        term_word[p][sig]=w
    dp=[None]*len(nodes);inf=10**9
    for p in range(len(nodes)-1,-1,-1):
        state={0:0}
        if terminal[p]:state[terminal[p]]=0
        for q in children[p].values():
            next_state=state.copy()
            for a,ca in state.items():
                for b,cb in dp[q].items():
                    if b==0:continue
                    mask=a|b;cost=ca+cb
                    if cost<next_state.get(mask,inf):next_state[mask]=cost
            state=next_state
        if p:
            extra=int(nodes[p] not in PAID)
            for mask in state:
                if mask:state[mask]+=extra
        dp[p]=state
    assert 63 in dp[0]

    def witness(p,mask):
        if mask==0:return []
        trace={0:(0,[])}
        if terminal[p]:trace[terminal[p]]=(0,[])
        for q in children[p].values():
            nxt=trace.copy()
            for a,(ca,choices) in trace.items():
                for b,cb in dp[q].items():
                    if not b:continue
                    m=a|b;v=ca+cb
                    if v<nxt.get(m,(inf,None))[0]:
                        nxt[m]=(v,choices+[(q,b)])
            trace=nxt
        extra=0 if p==0 or nodes[p] in PAID else 1
        assert trace[mask][0]+extra==dp[p][mask]
        if terminal[p]:
            assert mask==terminal[p]
            return [(mask,term_word[p][mask])]
        out=[]
        for q,b in trace[mask][1]:out.extend(witness(q,b))
        return out

    chosen=witness(0,63)
    assert sorted(x for x,w in chosen)==[1,2,4,8,16,32]
    new=set().union(*(prefix_set(w) for sig,w in chosen))-PAID
    assert len(new)==dp[0][63]
    for sig,w in chosen:
        seq=native(w)
        assert len(w)==(8 if sig<=8 else 9)
        assert tuple(seq.count(j) for j in (1,2,3))==k
        assert tuple(seq.count(j)-seq.count(-j) for j in (1,2,3))==(2,0,0)
        assert len(seq)==18+2*k[2]
    return {"key":list(k),"feasible":True,"signed_tail_extra":dp[0][63],
            "seed_plus_tail_lower_bound":42+dp[0][63],
            "candidate_words":len(entries),"trie_edges":len(nodes)-1,
            "native_length":len(entries[0][2]),
            "words_by_signature":counts,
            "witness":{str(sig):w for sig,w in chosen},
            "direct_recount":len(new)}

def main():
    data={"schema":"EC49FDP_TAIL_H8H9_EXACT_RELAXATION_V1",
          "science_pin":PIN,"seed_paths":SEED,"seed_edges":42,
          "required_signatures":{"H8":[1,2,4,8],"H9":[16,32]},
          "results":[solve(k) for k in KEYS]}
    assert all(r["feasible"] for r in data["results"])
    assert sorted(r["key"] for r in data["results"])==sorted(map(list,KEYS))
    return data

if __name__=="__main__":
    print(json.dumps(main(),indent=2,ensure_ascii=False))
