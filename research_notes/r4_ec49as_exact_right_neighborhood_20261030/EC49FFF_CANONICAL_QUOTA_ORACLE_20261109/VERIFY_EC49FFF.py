#!/usr/bin/env python3
"""EC49FFF exact complete-key observer-quota oracle, Python standard library."""
from collections import Counter
from functools import lru_cache
from itertools import combinations
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
O=(0,0,4,1,16,32,8,2,0)
@lru_cache(None)
def states(c):
    if not any(c): return 1
    b=0
    for j,n in enumerate(c):
        if n:
            q=list(c);q[j]-=1
            old=states(tuple(q))
            for s in range(9):
                if old>>s&1: b|=1<<T[s][j]
    return b
def support(h,k):
    x,y,z=k;t=x+y-h-1;f=h+1-y-2*z;g=h+1-x
    if min(z-1,t,f,g)<0:return 0
    out=0
    for c in range(t+1):
        ss=states((z-1,c,t-c,z,f,g))
        for s,lab in enumerate(O):
            if ss>>s&1:out|=lab
    return out
def canonical(H):
    f=(H-1)//2;g=H-1-f
    return 2+f,g,1
def bits(h,v):
    low=(1<<(h-2)) if v&15 else 0
    if h==2:
        return low|(1<<15 if v&16 else 0)|(1<<16 if v&32 else 0)
    return low|((1<<(h+5)) if v&48 else 0)
def kmask(k):
    ans=0
    for h in range(2,10):ans|=bits(h,support(h,k))
    return ans
def minimum(keys):
    n=len(keys);N=1<<17
    masks=[kmask(k) for k in keys]
    union=[0]*(1<<n);cost=[100]*N;witness=[0]*N
    cost[0]=0
    for s in range(1,1<<n):
        bit=s&-s;j=bit.bit_length()-1
        m=union[s^bit]|masks[j];union[s]=m
        if s.bit_count()<cost[m]:cost[m]=s.bit_count();witness[m]=s
    for j in range(17):
        bit=1<<j
        for q in range(N):
            if not q&bit and cost[q|bit]<cost[q]:
                cost[q]=cost[q|bit];witness[q]=witness[q|bit]
    return cost,witness,masks
def requirement(high):
    high=set(high);m=0
    for h in range(2,10):m|=bits(h,48 if h in high else 15)
    return m
def main():
    keys=[(3,0,1),(2,1,1)]+[canonical(H) for H in range(3,18)]
    count=0
    for h in range(2,10):
        for z in range(1,(h+1)//2+1):
            n=h+1-2*z
            for t in range(n+1):
                for f in range(n-t+1):
                    g=n-t-f;k=(t+2*z+f,t+g,z)
                    v=support(h,k);count+=1
                    assert v==(15 if t else (16 if f else 0)|(32 if g else 0))
                    H=k[0]+k[1]-1
                    rep=(3,0,1) if H==2 and f else (2,1,1) if H==2 else canonical(H)
                    assert not (v&~support(h,rep))
    assert count==294 and len(keys)==17
    d0,w0,km=minimum(keys)
    dp,wp,_=minimum(keys[1:])
    assert len(d0)==131072
    assert Counter(d0)=={0:1,1:76,2:1146,3:6748,4:20109,5:34152,
                          6:35192,7:22576,8:8896,9:1984,10:192}
    assert Counter(dp)=={0:1,1:75,2:1071,3:5677,4:14432,5:19720,
                          6:15472,7:7104,8:1792,9:192,100:65536}
    f22=Counter(d0[requirement((3,)+late)] for late in combinations(range(4,10),4))
    f24=Counter(d0[requirement(late)] for late in combinations(range(4,10),4))
    assert f22=={5:10,6:5} and f24=={5:9,6:6}
    want=requirement((6,7,8,9));chosen=w0[want]
    got=0
    for j in range(len(keys)):
        if chosen>>j&1: got|=km[j]
    assert d0[want]==6 and (want&got)==want
    print("EXACT_PASS: 294 original DFA checks; 131072 requirement minima")
    print("22 patterns",dict(f22),"24 patterns",dict(f24))
    print("all-count keys",dict(sorted(Counter(d0).items())))
    print("strict-positive keys",dict(sorted(Counter(dp).items())))
    print("H3-low/H6-9-high six-key witness",
          [keys[j] for j in range(len(keys)) if chosen>>j&1])
if __name__=="__main__":main()
