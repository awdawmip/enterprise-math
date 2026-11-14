#!/usr/bin/env python3
"""EC49FFI: fully standalone exact integer verifier. No solver or floats.
Frozen native-X6/BRC science: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
import itertools
import json
from collections import Counter

ORDER="acdefg"
OPS={"a":(-1,-1),"c":(1,2,-1,-2),"d":(2,1,-2,-1),
     "e":(3,1,1,-3),"f":(1,-1),"g":(2,-2)}
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
LOWS=(1,2,4,8)

def minkeys(A,U):
    return (((U+A-2)//(A-1))-1).bit_length()

def formula(A,U):
    assert 2<=A<=U
    k=minkeys(A,U)
    H=[1+(U+(1<<j)-1)//(1<<j) for j in range(k-1,-1,-1)]
    assert H[0]>=A+1 and H[0]<=2*A-1 and H[-1]==U+1
    assert all(H[i]<H[i+1]<=2*H[i]-1 for i in range(k-1))
    assert all(any(h+1<=z<=2*h-1 for z in H) for h in range(A,U+1))
    n=U-1; q=n>>k
    length=4*(n-q)+6*k-2*(n.bit_count()-q.bit_count())
    assert length==sum(2*(z+1) for z in H)
    return k,length,H

def independent_cover_dp(A,U):
    states={0:(0,0)}
    for H in range(A+1,2*U):
        mask=sum(1<<(h-A) for h in range(A,U+1) if h+1<=H<=2*h-1)
        if not mask:continue
        nxt=dict(states)
        for old,cost in states.items():
            dest=old|mask
            val=(cost[0]+1,cost[1]+2*(H+1))
            if val<nxt.get(dest,(10**9,10**9)):nxt[dest]=val
        states=nxt
    return states[(1<<(U-A+1))-1]

def candidates(h,K):
    x,y,z=K
    a=z-1; cd=x+y-h-1; f=h+1-y-2*z; g=h+1-x
    if min(a,cd,f,g)<0:return
    for c in range(cd+1):
        count=[a,c,cd-c,z,f,g]
        def rec(word,state):
            if not any(count):
                yield word,SIG[state]
                return
            for i,num in enumerate(count):
                if num:
                    count[i]-=1
                    yield from rec(word+ORDER[i],T[state][i])
                    count[i]+=1
        yield from rec("",0)

def allkeys(h):
    for z in range(1,(h+1)//2+1):
        for x in range(2*z,h+2):
            for y in range(h+2-2*z):
                if x+y>=h+2:yield (x,y,z)

def prefix_opt(h,K):
    groups={s:[] for s in LOWS}
    for word,s in candidates(h,K):
        if s not in groups:continue
        n=tuple(t for op in word for t in OPS[op])
        assert len(n)==2*(sum(K)-1)
        assert s==SIG[_end_state(word)]
        cnt=Counter(n)
        assert tuple(cnt[i]-cnt[-i] for i in range(1,7))==(2,0,0,0,0,0)
        assert tuple(cnt[i] for i in (1,2,3))==K
        groups[s].append((word,tuple(n[:i] for i in range(1,len(n)+1))))
    assert all(groups.values())
    prefixes=set(itertools.chain.from_iterable(ps for g in groups.values() for _,ps in g))
    pmap={p:i for i,p in enumerate(prefixes)}
    masked={}
    for s in LOWS:
        masked[s]=[(w,sum(1<<pmap[p] for p in ps)) for w,ps in groups[s]]
    left=[(a|b,w1,w2) for w1,a in masked[1] for w2,b in masked[2]]
    right=[(c|d,w3,w4) for w3,c in masked[4] for w4,d in masked[8]]
    best=10**9; witness=None
    for l,w1,w2 in left:
        for r,w3,w4 in right:
            v=(l|r).bit_count()
            if v<best:best=v;witness=(w1,w2,w3,w4)
    return {"h":h,"key":K,"four_signature_counts":[len(groups[s]) for s in LOWS],
            "four_word_selections":len(left)*len(right),
            "minimum_prefix_union":best,"words":dict(zip(LOWS,witness))}

def _end_state(word):
    q=0
    for op in word:q=T[q][ORDER.index(op)]
    return q

def main():
    count=0
    for U in range(2,17):
        for A in range(2,U+1):
            k,L,_=formula(A,U)
            assert independent_cover_dp(A,U)==(k,L)
            count+=1
    assert count==120
    jump=0
    for A in range(2,19):
        for U in range(A,101):
            k,L,_=formula(A,U)
            k2,L2,_=formula(A,U+1)
            if k2==k:
                v=(U&-U).bit_length()-1
                assert L2-L==2*(1+min(k-1,v))
            else:
                assert k2==k+1 and U==(1<<k)*(A-1)
                assert L2-L==2*(A+k+2)
            jump+=1
    assert jump==1547
    prefix=[prefix_opt(h,K) for h in range(2,6) for K in allkeys(h)]
    assert len(prefix)==24
    totals={h:min(x["minimum_prefix_union"] for x in prefix if x["h"]==h) for h in range(2,6)}
    assert totals=={2:28,3:34,4:32,5:36}
    assert sum(x["four_word_selections"] for x in prefix)==3389185
    print(json.dumps({"status":"EXACT_INTEGER_PASS","interval_DP_cases":count,
                      "jump_checks":jump,"prefix_configs":len(prefix),
                      "prefix_selection_combinations":3389185,"prefix_optima":totals,
                      "examples":{str((a,u)):formula(a,u) for a,u in [(3,9),(5,9),(5,16),(5,17)]}},
                     ensure_ascii=False,indent=2))
if __name__=="__main__":main()
