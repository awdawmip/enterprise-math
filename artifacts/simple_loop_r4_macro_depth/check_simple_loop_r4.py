#!/usr/bin/env python3
"""Exact bounded certificate for RS-SIMPLE-LOOP-R4-MACRO-DEPTH-CLASSIFICATION.

The symbolic theorem used before enumeration is:
  locked + blocker-rank R => cyclic run count = 2R+3,
from Theta = n_plus - n_minus = 3 and runs=n_plus+n_minus.
The finite scan is therefore used only to classify the first R=4 locus, not to
infer the all-holonomy structural theorem.
"""
from collections import Counter, deque

STEP = {1:(1,0), 2:(0,1), 3:(-1,-1)}  # chi-coordinates on derived displacement carrier
CYC = {(1,2),(2,3),(3,1)}
EXPECTED_R4 = {
    "111111222322122333133233",
    "111111223221222331332333",
    "111111223221222333133233",
}
H6 = tuple(map(int, "111112222233133233"))
PACKET_PATH = [
    (1,3,3,2),
    (3,1,3,2),
    (3,3,1,2),
    (3,3,2,1),
    (3,2,3,1),
    (2,3,3,1),
]

def omega(a,b):
    if a == b: return 0
    return 1 if (a,b) in CYC else -1

def vertices(w):
    x=y=0; out=[(0,0)]
    for g in w:
        dx,dy=STEP[g]; x+=dx; y+=dy; out.append((x,y))
    return out

def simple(w):
    v=vertices(w)
    return v[-1] == v[0] and len(set(v[:-1])) == len(v)-1

def theta(w):
    n=len(w)
    return sum(omega(w[i],w[(i+1)%n]) for i in range(n))

def area2(w):
    pref=[0,0,0,0]; A=0
    for b in w:
        for a in (1,2,3): A += pref[a]*omega(a,b)
        pref[b]+=1
    return A

def runs(w):
    return sum(w[i] != w[i-1] for i in range(len(w)))

def reflexes(w):
    n=len(w)
    return [i for i in range(n) if omega(w[i],w[(i+1)%n]) == -1]

def blocker(w,i):
    v=vertices(w); n=len(w); b=w[(i+1)%n]
    dx,dy=STEP[b]; q=(v[i][0]+dx,v[i][1]+dy)
    occ=[j for j,p in enumerate(v[:-1]) if p == q]
    return q, occ

def blocked(w,i):
    return bool(blocker(w,i)[1])

def locked(w):
    rr=reflexes(w)
    return bool(rr) and all(blocked(w,i) for i in rr)

def blocker_level(w,i):
    n=len(w); _,occ=blocker(w,i); assert len(occ)==1
    j=occ[0]; counts=[0,0,0,0]; t=i
    while t != j:
        counts[w[t]] += 1; t=(t+1)%n
    b=w[(i+1)%n]
    ks=[counts[g] - (1 if g==b else 0) for g in (1,2,3)]
    assert ks[0] == ks[1] == ks[2] and ks[0] >= 1
    return ks[0], tuple(counts[g] for g in (1,2,3))

def canon(w):
    w=tuple(w); n=len(w); cand=[]
    for sh in range(3):
        r=tuple(((g-1+sh)%3)+1 for g in w)
        for k in range(n): cand.append(r[k:]+r[:k])
    return min(cand)

def cyclic_replace(w,i,src,tgt):
    w=tuple(w); n=len(w); L=len(src)
    r=w[i:]+w[:i]
    if r[:L] != tuple(src): return None
    rr=tuple(tgt)+r[L:]
    k=(n-i)%n
    return rr[k:]+rr[:k]

def macro_depth(w,maxd=5):
    """Cyclic/C3-invariant adjacent-transposition depth to a higher-area simple loop.

    C3 need not be seeded separately: applying the same global C3 relabeling to
    source and target preserves distance, simplicity and A2.
    """
    w=tuple(w); n=len(w); A0=area2(w)
    starts=list(dict.fromkeys(w[k:]+w[:k] for k in range(n)))
    seen=set(starts); cur=set(starts)
    stats=[]
    for d in range(1,maxd+1):
        nxt=set()
        for s in cur:
            for i in range(n-1):
                if s[i] == s[i+1]: continue
                t=list(s); t[i],t[i+1]=t[i+1],t[i]; t=tuple(t)
                if t not in seen: seen.add(t); nxt.add(t)
        higher=[t for t in nxt if simple(t) and theta(t)==3 and area2(t)>A0]
        stats.append((d,len(nxt),len(higher)))
        if higher: return d, min(higher), stats
        cur=nxt
    return None,None,stats

def r4_classes(H):
    """Exact self-avoiding bounded atlas, first letter fixed to 1.

    Fixing first=1 is complete modulo cyclic/C3 because every closed H-word has
    H occurrences of each label. Only the structurally forced 11-run locus is
    admitted to the R=4 classifier.
    """
    N=3*H; cnt={1:H-1,2:H,3:H}; word=[1]
    x,y=STEP[1]; vis={(0,0),(x,y)}; out=set(); based=0
    def dfs(x,y,d):
        nonlocal based
        if d == N:
            if (x,y) != (0,0): return
            w=tuple(word)
            if theta(w)!=3 or runs(w)!=11: return
            if len(reflexes(w))!=4 or not locked(w): return
            # run theorem replay at the accepted candidates
            assert runs(w) == 2*len(reflexes(w))+3
            based += 1; out.add(canon(w)); return
        for g in (1,2,3):
            if cnt[g] == 0: continue
            dx,dy=STEP[g]; q=(x+dx,y+dy); final=(d==N-1)
            if q == (0,0):
                if not final: continue
            elif q in vis: continue
            cnt[g]-=1; word.append(g); add=q!=(0,0)
            if add: vis.add(q)
            dfs(q[0],q[1],d+1)
            if add: vis.remove(q)
            word.pop(); cnt[g]+=1
    dfs(x,y,1)
    return based,out

def packet_unlock(w):
    n=len(w)
    for i in range(n):
        t=cyclic_replace(w,i,(1,3,3,2),(2,3,3,1))
        if t is not None and simple(t) and area2(t)>area2(w):
            # verify the specified five-swap unrestricted realization globally
            r=w[i:]+w[:i]; states=[]
            for p in PACKET_PATH:
                q=p+r[4:]
                states.append((simple(q),area2(q)))
            return i,t,states
    return None

def main():
    # H=6 regression
    assert simple(H6) and theta(H6)==3 and area2(H6)==22 and runs(H6)==7
    rr=reflexes(H6); assert rr == [12,14] and locked(H6)
    v=vertices(H6)
    q0,o0=blocker(H6,12); q1,o1=blocker(H6,14)
    assert v[12]==(3,3) and q0==(2,2) and o0==[16]
    assert v[14]==(3,2) and q1==(3,3) and o1==[12]
    assert blocker_level(H6,12)==(1,(1,1,2))
    assert blocker_level(H6,14)==(5,(5,6,5))
    h6u=cyclic_replace(H6,12,(1,3,3,2),(2,3,3,1))
    assert h6u and simple(h6u) and area2(h6u)-area2(H6)==6 and theta(h6u)==3
    d6,_,stats6=macro_depth(H6,5); assert d6==5

    # First R=4 locus
    census={}
    for H in range(4,9):
        based,cls=r4_classes(H); census[H]=(based,{''.join(map(str,x)) for x in cls})
    assert all(census[H][0]==0 for H in range(4,8))
    assert census[8][0]==72 and census[8][1]==EXPECTED_R4

    rows=[]
    for s in sorted(EXPECTED_R4):
        w=tuple(map(int,s)); R=len(reflexes(w))
        assert simple(w) and locked(w) and R==4 and runs(w)==11 and theta(w)==3
        assert area2(w)==30
        lev=[blocker_level(w,i)[0] for i in reflexes(w)]
        assert lev == [1,7,1,7]
        # edge equation n_arc = e_b + k(1,1,1)
        for i in reflexes(w): blocker_level(w,i)
        u=packet_unlock(w); assert u is not None
        i,t,states=u
        assert area2(t)-area2(w)==6 and theta(t)-theta(w)==0
        assert states == [(True,30),(False,32),(False,34),(False,32),(False,34),(True,36)]
        d,tgt,stats=macro_depth(w,5); assert d==5
        assert all(h==0 for _,_,h in stats[:4])
        rows.append((s,i,''.join(map(str,t)),stats))

    print("PASS SIMPLE_LOOP_R4_BLOCKING_MOTIF_AND_MACRO_DEPTH_EXACTLY_REFUTED")
    print("H6: R=2, runs=7, A2=22, d=5, packet 1332->2331")
    print("R4 census:", {H:(c,len(k)) for H,(c,k) in census.items()})
    for row in rows: print("R4",row)

if __name__ == '__main__': main()
