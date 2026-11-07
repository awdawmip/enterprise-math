#!/usr/bin/env python3
"""EC49FDR author-side 19-label native signed-X6 Trie exact relaxation.

Frozen science: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
The PRIM/DFA/cache-key language block below is the actual unmodified
scientific source from EC49FDQ_REPLAY.py at immutable predecessor commit
9eb422ab5476e11583f4dbafd65c6d423b3b1a21.
Only the exact 19-label relaxation's bookkeeping is added here.
Run: python EC49FDR_RELAXATION_DP.py
No third-party dependencies or numerical approximation.
"""
import json,sys,time
from functools import lru_cache

PIN='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
PRIM={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
LETTERS='acdefg'
TRANS=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
       (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
       (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0);CLAUSES=(18,20,33,40)
SEED={2:['de','ed','ce','ec'],3:['feg','gef']}
FAMILIES={
 '1512':((3,1,1),(4,2,1),(4,3,1),(4,4,1),(5,5,1)),
 '1513':((3,1,1),(4,2,1),(5,2,1),(6,2,1),(7,3,1)),
 '2200':((3,1,1),(3,2,1),(4,3,1),(4,4,1),(5,5,1)),
 '2203':((3,1,1),(4,1,1),(5,2,1),(6,2,1),(7,3,1))}
QUOTAS={'1512':(4,2,2,2,4,2),'1513':(4,2,2,2,4,2),
        '2200':(2,4,2,2,4,2),'2203':(2,4,2,2,4,2)}
def steps(w):return tuple(v for c in w for v in PRIM[c])
def prefix(w):
 s=steps(w);return set(s[:n] for n in range(1,len(s)+1))
def key(w):return tuple(steps(w).count(i) for i in (1,2,3))
@lru_cache(None)
def language(h,k):
 x,y,z=k;r=x+y-h-1;cnt=[z-1,0,r,z,h+1-y-2*z,h+1-x]
 out=[]
 if min(cnt)<0:return ()
 def rec(q,state,w):
  if q==h:
   if SIG[state] in (1,2,4,8,16,32):out.append((SIG[state],w))
   return
  for j,x in enumerate(cnt):
   if x and TRANS[state][j]!=8:
    cnt[j]-=1;rec(q+1,TRANS[state][j],w+LETTERS[j]);cnt[j]+=1
 for n in range(r+1):
  cnt[1]=n;cnt[2]=r-n;rec(0,0,'')
 return tuple(out)


def solve(fid,k):
    start=time.monotonic()
    keys=FAMILIES[fid]
    old_h7=keys[-2]
    paid=set().union(*(prefix(w) for ws in SEED.values() for w in ws))
    assert len(paid)==42
    assert old_h7[0]+old_h7[1]==8
    old_keys=keys[1:4]
    small_h=5 if fid in ('1512','1513') else 4
    big_h=4 if small_h==5 else 5
    clauses=(18,20,33,40)
    req={7:(16,32),8:(1,2,4,8),9:(16,32),
         6:(16,32),small_h:(16,32)}
    data=[]
    for h in (4,5,6,7,8,9):
        kh=(tuple(old_keys)+(k,) if h<=6
            else (old_h7,k) if h==7 else (k,))
        for kk in kh:
            for sig,w in language(h,kk):
                if h<=6 or sig in req[h]:
                    data.append((h,kk,sig,w))
    # Bits: H7 0..1; H8 2..5; H9 6..7;
    # retained-key use 8..10; H6 11..12;
    # earlier two-slot rank 13..14; earlier four-slot rank 15..18.
    label={(h,sig):1<<(i+(0 if h==7 else 2 if h==8 else 6))
           for h in (7,8,9) for i,sig in enumerate(req[h])}
    nodes=[{}]
    term=[0]
    cost=[0]
    path=[()]
    for h,kk,sig,w in data:
        cur=0
        for t in steps(w):
            nxt=nodes[cur].get(t)
            if nxt is None:
                nxt=len(nodes)
                nodes[cur][t]=nxt
                nodes.append({})
                term.append(0)
                path.append(path[cur]+(t,))
                cost.append(int(path[-1] not in paid))
            cur=nxt
        early_key_bit=(1<<(8+old_keys.index(kk)) if kk in old_keys else 0)
        pair_bits=(1<<({6:11,small_h:13}[h]+(16,32).index(sig)
                   if h in (6,small_h) and sig in (16,32) else 0)
        rank_bits=(sum(1<<(15+i) for i,mask in enumerate(clauses)
                       if sig&mask) if h==big_h else 0)
        # Retained-key occurrence can be witnessed in H7, not only H4-H6.
        # Keep key-use labels independent of the horizon/signature switch.
        term[cur]|=(early_key_bit|
                    (pair_bits|rank_bits if h<=6 else label[h,sig]))
    # Each terminal's 19-label mask is an optional selected complete word.
    # Subtrees combine by OR-convolution with min-plus cost.
    dp=[None]*len(nodes)
    visited=0
    max_masks=0
    for u in range(len(nodes)-1,-1,-1):
        z={0:0}
        if term[u]:
            z[term[u]]=0
        for v in nodes[u].values():
            d=dp[v]
            n={}
            for m,c in z.items():
                for mm,cc in d.items():
                    nm=m|mm
                    cv=c+cc
                    if nm not in n or cv<n[nm]:
                        n[nm]=cv
            z=n
        if u>0:
            delta=cost[u]
            z={m:(v+delta if m else 0) for m,v in z.items()}
        dp[u]=z
        visited+=len(z)
        max_masks=max(max_masks,len(z))
    wanted=(1<<19)-1
    exact=dp[0].get(wanted)
    assert exact is not None, (fid,k)
    return {'family':fid,
            'new_key':k,
            'old_h7_key':old_h7,
            'seed_prefixes':len(paid),
            'target_93':93,
            'required_labels':19,
            'mandatory_early_keys':old_keys,
            'new_edges_min':exact,
            'rigorous_full_lower_bound':42+exact,
            'candidate_words':len(data),
            'trie_edges':len(nodes)-1,
            'subtree_mask_state_entries':visited,
            'max_subtree_masks':max_masks,
            'elapsed_seconds':round(time.monotonic()-start,3),
            'science_pin':PIN}

if __name__=='__main__':
    cases=(sys.argv[1].split(',') if len(sys.argv)>1
           else list(FAMILIES))
    newkeys=([tuple(map(int,t.split(','))) for t in sys.argv[2:]]
             if len(sys.argv)>2 else [(6,4,2),(7,3,2),(8,2,2),(8,2,3)])
    for fid in cases:
        for k in newkeys:
            print(json.dumps(solve(fid,k),ensure_ascii=False),flush=True)
