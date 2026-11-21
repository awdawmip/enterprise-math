"""Independent actual-residual crosscheck of PREFIX-986 (exact integers)."""
from collections import deque
from itertools import product
import json

def sources(p):
    d={}
    for i in range(p):
        for j in range(1,p):
            for s in (-1,1):
                c=(1<<i)-s*(1<<j)
                if c:d.setdefault(c,[]).append((i,j,s))
    return d

def legal_successors(x,c,d):
    for i,j,s in d[c]:
        if ((x>>j)&1)==(1-s)//2:
            yield x^(1<<j)

def period(x,word,d):
    todo={x}
    for c in word:
        todo={z for y in todo for z in legal_successors(y,c,d)}
    return todo

def census(p):
    d=sources(p)
    keys=sorted(d)
    n=1<<(p-1)
    cycles=0
    without_four=0
    mismatch_eight=0
    words=0
    for word in product(keys,repeat=4):
        words+=1
        ad=[set() for _ in range(n)]
        indeg=[0]*n
        four=False
        eight=False
        for x in range(n):
            nxt={(z-1)//2 for z in period(2*x+1,word,d)}
            ad[x]=nxt
            for z in nxt:indeg[z]+=1
            if x in nxt:four=True
        for x in range(n):
            if any(x in ad[z] for z in ad[x]):
                eight=True
                break
        qu=deque(i for i,v in enumerate(indeg) if v==0)
        done=0
        while qu:
            u=qu.popleft()
            done+=1
            for v in ad[u]:
                indeg[v]-=1
                if indeg[v]==0:qu.append(v)
        cyc=done<n
        cycles+=cyc
        without_four+=cyc and not four
        mismatch_eight+=cyc!=eight
    return dict(p=p,residuals=len(keys),words=words,cyclic=cycles,
                cyclic_without_four=without_four,cycle_eight_mismatches=mismatch_eight)

def sharp():
    p=6;d=sources(p);w=(6,24,8,40)
    seen=set();cache={}
    def dp(phase,x):
        key=(phase,x)
        if key in seen:raise AssertionError("Unexpected cycle in witness")
        if key in cache:return cache[key]
        seen.add(key)
        candidates=[]
        for y in legal_successors(x,w[phase],d):
            length,trail=dp((phase+1)%4,y)
            candidates.append((length+1,[(phase,x,y)]+trail))
        seen.remove(key)
        cache[key]=max(candidates,default=(0,[]),key=lambda v:v[0])
        return cache[key]
    all_states=[(q,x) for q in range(4) for x in range(1,1<<p,2)]
    longest=max(dp(*state)[0] for state in all_states)
    length,trail=dp(0,63)
    assert length==longest==18
    return dict(word=w,start=63,longest=longest,
                ports=[(x^y).bit_length()-1 for _,x,y in trail],
                states=[63]+[y for _,x,y in trail])

if __name__=="__main__":
    a=census(3);b=census(4);wit=sharp()
    assert (a["words"],a["cyclic"],a["cycle_eight_mismatches"])==(6561,960,0)
    assert (b["words"],b["cyclic"],b["cycle_eight_mismatches"])==(65536,9957,0)
    print(json.dumps(dict(actual_residual_crosscheck=[a,b],sharp_witness=wit)))
