#!/usr/bin/env python3
"""R656: exact integer optimal repair score-gap envelopes, stdlib only."""
import json
from functools import lru_cache
from itertools import combinations,product
INF=10**12
MATCH=(((0,1),(2,3),(4,5)),((0,2),(1,4),(3,5)),((0,3),(1,5),(2,4)),((0,4),(1,3),(2,5)))
P=range(4);TRIADS=tuple(combinations(range(6),3))
def code(s):
    z=set(s);out=[]
    for m in MATCH:
        if any((a in z)+(b in z)!=1 for a,b in m):out.append(0)
        else:out.append(1 if sum(b in z for a,b in m)%2==0 else -1)
    return tuple(out)
C={s:code(s) for s in TRIADS}
assert len(set(C.values()))==20
NEI={s:tuple(t for t in TRIADS if len(set(s)&set(t))==2) for s in TRIADS}
def shortest(K,n):
    D=[[0 if i==j else INF for j in range(n)] for i in range(n)]
    for (i,j),w in K.items():D[i][j]=min(D[i][j],w)
    for k in range(n):
        for i in range(n):
            for j in range(n):D[i][j]=min(D[i][j],D[i][k]+D[k][j])
    return D
def mincost(s,t,W):
    L=sum(s);na,nb=len(s),len(t);source=na+nb;sink=source+1;n=sink+1
    G=[[] for _ in range(n)]
    def edge(u,v,cap,c):
        G[u].append([v,len(G[v]),cap,c]);G[v].append([u,len(G[u])-1,0,-c])
    for a,cap in enumerate(s):edge(source,a,cap,0)
    for a in range(na):
        for i in range(nb):
            if W[a][i] is not None:edge(a,na+i,L,W[a][i])
    for i,cap in enumerate(t):edge(na+i,sink,cap,0)
    sent=cost=0
    while sent<L:
        dist=[INF]*n;pre=[None]*n;dist[source]=0
        for _ in range(n-1):
            changed=False
            for u in range(n):
                if dist[u]==INF:continue
                for j,(v,rev,cap,w) in enumerate(G[u]):
                    if cap>0 and dist[u]+w<dist[v]:
                        dist[v]=dist[u]+w;pre[v]=(u,j);changed=True
            if not changed:break
        if pre[sink] is None:return None
        pushed=L-sent;cur=sink
        while cur!=source:
            u,j=pre[cur];pushed=min(pushed,G[u][j][2]);cur=u
        cur=sink
        while cur!=source:
            u,j=pre[cur];v,rev,_,w=G[u][j]
            G[u][j][2]-=pushed;G[v][rev][2]+=pushed;cur=u
        sent+=pushed;cost+=pushed*dist[sink]
    return cost
def brute(s,t,W,lo,hi):
    na,nb=len(s),len(t)
    @lru_cache(None)
    def rec(a,rem):
        if a==na:return (0,0,0) if all(v==0 for v in rem) else None
        best=None
        def alloc(i,available,vec):
            nonlocal best
            if i==nb:
                if available:return
                trail=rec(a+1,tuple(rem[k]-vec[k] for k in range(nb)))
                if trail is None:return
                weight=trail[0]+sum(vec[k]*W[a][k] for k in range(nb) if vec[k])
                low=trail[1]+sum(vec[k]*lo[a][k] for k in range(nb))
                high=trail[2]+sum(vec[k]*hi[a][k] for k in range(nb))
                if best is None or weight<best[0]:best=(weight,low,high)
                elif weight==best[0]:best=(weight,min(best[1],low),max(best[2],high))
                return
            for q in range(min(available,rem[i])+1):
                if q and W[a][i] is None:continue
                alloc(i+1,available-q,vec+(q,))
        alloc(0,s[a],())
        return best
    return rec(0,tuple(t))
def check(s,t,H,K,d,stats):
    stats['balanced_cases']+=1;n=len(t);D=shortest(K,n)
    W=[[None]*n for _ in s];lo=[[0]*n for _ in s];hi=[[0]*n for _ in s]
    for a in range(len(s)):
        for old in range(n):
            choices=[(D[old][j],d[j]-d[old]) for j in range(n)
                     if (a,j) in H and D[old][j]<INF]
            if not choices:continue
            v=min(w for w,q in choices);W[a][old]=v
            lo[a][old]=min(q for w,q in choices if w==v)
            hi[a][old]=max(q for w,q in choices if w==v)
    pure=mincost(s,t,W);ref=brute(s,t,W,lo,hi)
    assert (pure is None)==(ref is None)
    if ref is None:stats['infeasible_cases']+=1;return
    R,mn,mx=ref;stats['feasible_cases']+=1;assert pure==R
    B=8*sum(s)+1
    Vm=[[None if W[a][i] is None else B*W[a][i]+lo[a][i] for i in range(n)] for a in range(len(s))]
    Vp=[[None if W[a][i] is None else B*W[a][i]-hi[a][i] for i in range(n)] for a in range(len(s))]
    assert mincost(s,t,Vm)==B*R+mn
    assert mincost(s,t,Vp)==B*R-mx
    stats['lexicographic_minmax_verified']+=1
    if mn<mx:stats['nontrivial_envelopes']+=1
def scores(S,u,O):
    return sorted((sum(u[i]*C[t][i] for i in P)+sum(C[S][i]*O[i][j]*C[t][j] for i in P for j in P),t) for t in NEI[S])
def main():
    stats={k:0 for k in ('graph_cost_models','balanced_cases','feasible_cases','infeasible_cases','lexicographic_minmax_verified','nontrivial_envelopes')}
    contrasts=[tuple(C[a][i]-C[b][i] for i in P) for a,b in (
        ((1,2,4),(0,3,4)),((0,1,5),(1,2,4)),((1,2,3),(0,2,4)))]
    pair=list(product(range(2),repeat=2))
    for mask in range(1,16):
        H={e for i,e in enumerate(pair) if mask>>i&1}
        for kmask in range(4):
            for w01,w10 in product((1,2),repeat=2):
                K={(0,0):0,(1,1):0}
                if kmask&1:K[0,1]=w01
                if kmask&2:K[1,0]=w10
                stats['graph_cost_models']+=1
                for s in product(range(3),repeat=2):
                    for t in product(range(3),repeat=2):
                        if sum(s)==sum(t):
                            for d in contrasts:check(s,t,H,K,d,stats)
    H3=[{(0,1),(0,2)}, {(0,0),(0,1),(1,1),(1,2),(2,2)},
        {(0,1),(0,2),(1,0),(1,2),(2,1)},
        {(0,0),(1,0),(1,1),(2,1),(2,2)},set(product(range(3),repeat=2))]
    id3={(i,i):0 for i in range(3)}
    K3=[id3|{(0,1):1,(0,2):1},id3|{(0,1):1,(0,2):1,(1,2):2},
        id3|{(0,1):1,(0,2):1,(1,0):1,(2,0):1},
        id3|{(2,1):1,(2,0):1},id3|{(0,1):2,(0,2):2,(1,2):1,(2,1):1}]
    for H in H3:
        for K in K3:
            stats['graph_cost_models']+=1
            for s in product(range(3),repeat=3):
                for t in product(range(3),repeat=3):
                    if sum(s)==sum(t):
                        for d in contrasts:check(s,t,H,K,d,stats)
    M=[[0]*4 for _ in P]
    for (a,b),cnt in zip(((0,1),(2,0),(2,3),(3,0)),(2,1,2,2)):M[a][b]+=cnt
    O=[[M[i][j]-M[j][i] for j in P] for i in P]
    u=[sum(M[i])-sum(M[j][i] for j in P) for i in P];S=(0,1,4)
    def top(r):
        v=u.copy();v[r]+=1;z=scores(S,v,O);assert z[-1][0]>z[-2][0]
        return z[-1],z[-1][0]-z[-2][0]
    original=top(0);p1=top(1);p3=top(3)
    assert original==((4,(0,1,5)),1) and p1==((4,(1,2,4)),1) and p3==((4,(0,3,4)),1)
    H={(0,1),(0,3)};K={(i,i):0 for i in range(4)}|{(0,1):1,(0,3):1}
    assert min(shortest(K,4)[0][j] for a,j in H)==1
    print(json.dumps(dict(marker='R656_OPTIMAL_REPAIR_BRC_GAP_ENVELOPE_EXACT_PASS',
      model='H actual V29 transfer; K directed weighted target editing; frozen V23/V27 score',
      stats=stats,witness=dict(pass_counts=(2,1,2,2),triad=S,original_receiver=0,
      original_winner=original[0][1],original_gap=original[1],
      equal_cost_receiver_choices=(1,3),cost=1,winner_for_port1=p1[0][1],
      winner_for_port3=p3[0][1],each_new_gap=1),
      arithmetic='exact integers only'),indent=2))
if __name__=='__main__':main()