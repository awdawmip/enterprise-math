"""Exact support-band verification for the pinned R5 min-plus/count suffix DP.
The quantitative resource experiment is in VERIFY_R5_SUPPORT_BANDS.py (companion).
"""
from bisect import bisect_left, bisect_right
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
W=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
HEX56='d500a95a516544511a50596555556a5a441665a66a9195956669611456565551aa5669aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa6a00'
INF=10**30

def fixture():
    pairs={3:set(),12:set(),15:set()}
    for mask in range(1,1<<15):
        n=-sum(W[i] for i in range(15) if mask>>i&1)
        k=-sum(K0[i] for i in range(15) if mask>>i&1)
        if n>=3 and k%36==0 and k//36 in pairs:pairs[k//36].add(n)
    assert [len(pairs[q]) for q in (3,12,15)]==[538,298,229]
    hist=Counter((1-Fraction(36*q,n))/23 for q in pairs for n in pairs[q])
    assert len(hist)==953 and Counter(hist.values())=={1:869,2:56,3:28}
    x=[0]
    for threshold in sorted(hist):x.append(x[-1]+hist[threshold])
    raw=bytes.fromhex(HEX56)
    assert len(raw)==56 and sha256(raw).hexdigest()=='bf4f377e8a3b9823d589d0f5c5b0b5973f374a09aa986d5b729bc695c5de0326'
    bits=int.from_bytes(raw[2:],'little');center=[bits&3];bits>>=2
    for _ in range(212):
        center.append(center[-1]+3+(bits&3));bits>>=2
    assert bits==0 and center[0]==1 and center[-1]==952
    return x,center

def graph(x,r):
    n=len(x)
    u=[bisect_right(x,x[p]+r)-1 for p in range(n)]
    v=[bisect_left(x,x[p]-r) for p in range(n)]
    adj=[[] for _ in x]
    for p in range(n):
        for q in range(p+1,min(n,p+2*r+2)):
            if v[q]<=u[p]+1:
                adj[p].append((q,sum(min(x[b]-x[p],x[q]-x[b]) for b in range(p+1,q+1))))
    start=[p for p in range(n) if x[p]-x[0]<=r]
    end=[p for p in range(n) if x[-1]-x[p]<=r]
    head={p:sum(x[p]-x[b] for b in range(p)) for p in start}
    tail={p:sum(x[b]-x[p] for b in range(p+1,n)) for p in end}
    return start,end,adj,head,tail

def rows(x,r,k,pruned):
    start,end,adj,head,tail=graph(x,r)
    n=len(x)
    row={p:(tail[p],1) for p in end}
    out=[None,row]
    for t in range(2,k+1):
        nxt={}
        candidates=(range(max(0,min(row)-(2*r+1)),max(row)) if pruned and row
                    else range(n))
        for p in candidates:
            cost=INF;count=0
            for q,w in adj[p]:
                old,nways=row.get(q,(INF,0))
                if not nways:continue
                value=w+old
                if value<cost:cost,count=value,nways
                elif value==cost:count+=nways
            if count:nxt[p]=(cost,count)
        row=nxt;out.append(row)
    return out,(start,end,adj,head,tail)

def rank_of(center,rr,g):
    start,end,adj,head,tail=g; k=len(center)
    z=rr[k]; best=min(head[p]+z[p][0] for p in start if p in z)
    ans=sum(z[p][1] for p in start if p<center[0] and p in z and head[p]+z[p][0]==best)
    for t,(p,q) in enumerate(zip(center,center[1:])):
        parent=rr[k-t][p];child=rr[k-t-1]
        assert any(v==q and v in child and w+child[v][0]==parent[0] for v,w in adj[p])
        ans+=sum(child[v][1] for v,w in adj[p] if v<q and v in child and w+child[v][0]==parent[0])
    return ans

def check():
    x,center=fixture();assert len(x)==954 and x[-1]==1065
    full,g=rows(x,2,213,False)
    thin,_=rows(x,2,213,True)
    assert full==thin, 'all 213 row maps (including counts and ties) must match'
    start,end,adj,head,tail=g
    assert sum(map(len,adj))==4383
    opt=min(head[p]+thin[213][p][0] for p in start if p in thin[213])
    count=sum(thin[213][p][1] for p in start if p in thin[213] and head[p]+thin[213][p][0]==opt)
    rank=rank_of(center,thin,g)
    assert (opt,count,rank)==(1070,1338767625695954932334592000,417027933051277583800994379)
    assert all(set(row)==set(range(min(row),max(row)+1)) for row in thin[1:])
    assert sum(map(len,thin[1:]))==83813
    cases=0
    for n in range(1,5):
        for increments in product((1,2,3),repeat=n):
            v=[0]
            for d in increments:v.append(v[-1]+d)
            for radius in range(4):
                for k in range(1,len(v)+1):
                    a,gr=rows(v,radius,k,False)
                    b,_=rows(v,radius,k,True)
                    assert a==b
                    direct=[]
                    for subset in combinations(range(len(v)),k):
                        dd=[min(abs(v[p]-v[s]) for s in subset) for p in range(len(v))]
                        if max(dd)<=radius:direct.append(sum(dd))
                    starts,ends,adj,head,tail=gr
                    got=[(head[p]+b[k][p][0],b[k][p][1]) for p in starts if p in b[k]]
                    if not direct:assert not got
                    else:
                        best=min(direct)
                        assert min(c for c,_ in got)==best
                        assert sum(w for c,w in got if c==best)==direct.count(best)
                    cases+=1
    print({'PASS':True,'finite_cases':cases,'dp_rows':213,'row_cells_dense':954*213,'row_cells_reachable':83813,
           'saved_cell_fraction':round(1-83813/(954*213),6),'J':opt,'Topt':str(count),'rank':str(rank)})
if __name__=='__main__':check()
