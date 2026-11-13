#!/usr/bin/env python3
"""R655: exact finite check of composed Hall, receiver min-cost retarget and signed V27 gaps.
All arithmetic exact integers; standalone Python 3 standard library.
"""
import json
from functools import lru_cache
from itertools import product,combinations
INF=10**9

def shortest(K, nb):
    D=[[0 if a==b else INF for b in range(nb)] for a in range(nb)]
    for (a,b),w in K.items(): D[a][b]=min(D[a][b],w)
    for k in range(nb):
        for i in range(nb):
            for j in range(nb): D[i][j]=min(D[i][j],D[i][k]+D[k][j])
    return D

def effective(H,D,na,nb):
    W=[[INF]*nb for _ in range(na)]
    B=[[None]*nb for _ in range(na)]
    for a in range(na):
        for old in range(nb):
            for new in range(nb):
                if (a,new) in H and D[old][new]<W[a][old]:
                    W[a][old]=D[old][new];B[a][old]=new
    return W,B

def hall(s,t,W):
    best=0
    for mask in range(1<<len(s)):
        N={b for a in range(len(s)) if mask>>a&1
             for b in range(len(t)) if W[a][b]<INF}
        d=sum(s[a] for a in range(len(s)) if mask>>a&1)-sum(t[b] for b in N)
        best=max(best,d)
    return best

def brute(s,t,W):
    """Independent exhaustive DP over source->old-target assignments."""
    na,nb=len(s),len(t)
    @lru_cache(None)
    def rec(a,rem):
        if a==na:return 0 if not any(rem) else INF
        arr=[]
        def alloc(b,avail,used,cost):
            if b==nb:
                if avail==0: arr.append(cost+rec(a+1,tuple(rem[j]-used[j] for j in range(nb))))
                return
            for q in range(min(avail,rem[b])+1):
                if q and W[a][b]>=INF:continue
                alloc(b+1,avail-q,used+(q,),cost+q*W[a][b])
        alloc(0,s[a],(),0)
        return min(INF,min(arr,default=INF))
    return rec(0,tuple(t))

def mincost(s,t,W):
    na,nb=len(s),len(t);L=sum(s);n=na+nb+2;src=na+nb;dst=src+1
    G=[[] for _ in range(n)]
    def add(u,v,cap,c):
        G[u].append([v,len(G[v]),cap,c]);G[v].append([u,len(G[u])-1,0,-c])
        return len(G[u])-1
    for a,v in enumerate(s):add(src,a,v,0)
    chosen={}
    for a in range(na):
        for b in range(nb):
            if W[a][b]<INF: chosen[a,b]=(a,add(a,na+b,L,W[a][b]))
    for b,v in enumerate(t):add(na+b,dst,v,0)
    sent=total=0
    while sent<L:
        dist=[INF]*n;prev=[None]*n;dist[src]=0
        for _ in range(n-1):
            change=False
            for u in range(n):
                if dist[u]>=INF:continue
                for j,(v,rev,cap,cost) in enumerate(G[u]):
                    if cap>0 and dist[u]+cost<dist[v]:
                        dist[v]=dist[u]+cost;prev[v]=(u,j);change=True
            if not change:break
        if prev[dst] is None:break
        push=L-sent;cur=dst
        while cur!=src:
            u,j=prev[cur];push=min(push,G[u][j][2]);cur=u
        cur=dst
        while cur!=src:
            u,j=prev[cur];v,rev,_,cost=G[u][j]
            G[u][j][2]-=push;G[v][rev][2]+=push;cur=u
        sent+=push;total+=push*dist[dst]
    if sent<L:return INF,None
    X=[[0]*nb for _ in range(na)]
    for (a,b),(u,j) in chosen.items(): X[a][b]=G[na+b][G[u][j][1]][2]
    assert [sum(row) for row in X]==list(s)
    assert [sum(X[a][b] for a in range(na)) for b in range(nb)]==list(t)
    assert sum(X[a][b]*W[a][b] for a in range(na) for b in range(nb))==total
    return total,X

def check(s,t,H,K,stats):
    if sum(s)!=sum(t):return
    stats['balanced_tests']+=1
    D=shortest(K,len(t));W,B=effective(H,D,len(s),len(t))
    d=hall(s,t,W);opt,X=mincost(s,t,W);direct=brute(s,t,W)
    assert opt==direct,(s,t,H,K,W,opt,direct)
    assert (opt<INF)==(d==0),(s,t,H,K,W,opt,d)
    if opt>=INF:
        stats['infeasible_cases']+=1
        if d:stats['positive_hall_deficit_cases']+=1
        return
    stats['feasible_cases']+=1
    new=[0]*len(t);events=[]
    for a in range(len(s)):
        for old in range(len(t)):
            cnt=X[a][old]
            if cnt:
                dest=B[a][old]
                assert dest is not None and (a,dest) in H
                new[dest]+=cnt;events.extend([(a,old,dest)]*cnt)
    assert sum(new)==sum(s) and len(events)==sum(s)
    assert sum(D[old][dest] for _,old,dest in events)==opt
    stats['certified_integer_event_assignments']+=1

# Frozen V23 four-field matchings and signed V27 integer score.
MATCH=(((0,1),(2,3),(4,5)),((0,2),(1,4),(3,5)),
       ((0,3),(1,5),(2,4)),((0,4),(1,3),(2,5)))
TRIADS=tuple(combinations(range(6),3));P=range(4)
def field(m,s):
    z=set(s)
    if any((a in z)+(b in z)!=1 for a,b in m):return 0
    return 1 if sum(b in z for a,b in m)%2==0 else -1
C={s:tuple(field(m,s) for m in MATCH) for s in TRIADS}
N={s:tuple(t for t in TRIADS if len(set(s)&set(t))==2) for s in TRIADS}
assert len(set(C.values()))==20
def scores(S,u,O):
    return sorted(((sum(u[i]*C[t][i] for i in P)+
                    sum(C[S][i]*O[i][j]*C[t][j] for i in P for j in P),t)
                   for t in N[S]),reverse=True)
def gapcheck(S,u,O,moves):
    old=scores(S,u,O);T=old[0][1]
    if old[0][0]==old[1][0]:return None
    du=[0]*4;cost=0
    for origin,dest,w in moves:du[origin]-=1;du[dest]+=1;cost+=w
    new=scores(S,[u[i]+du[i] for i in P],O)
    for v,t in new:
        if t==T:continue
        oldgap=old[0][0]-next(o for o,t0 in old if t0==t)
        newgap=next(x for x,z in new if z==T)-v
        d=[C[T][i]-C[t][i] for i in P]
        assert newgap==oldgap+sum(du[i]*d[i] for i in P)
        change=sum(du[i]*d[i] for i in P)
        assert abs(change)<=sum(abs(d[dest]-d[origin]) for origin,dest,w in moves)
        assert abs(change)<=4*cost
    return old,new

def main():
    stats=dict(graph_cost_models=0,balanced_tests=0,infeasible_cases=0,
        positive_hall_deficit_cases=0,feasible_cases=0,certified_integer_event_assignments=0)
    A2=list(product(range(2),repeat=2))
    for maskH in range(1,1<<4):
        H={e for i,e in enumerate(A2) if maskH>>i&1}
        for maskK in range(4):
            for c01,c10 in product((1,2),repeat=2):
                K={(0,0):0,(1,1):0}
                if maskK&1:K[0,1]=c01
                if maskK&2:K[1,0]=c10
                stats['graph_cost_models']+=1
                for s in product(range(4),repeat=2):
                    for t in product(range(4),repeat=2):check(s,t,H,K,stats)
    H3=[{(0,0),(1,1),(2,2)},{(0,1),(1,0),(1,2),(2,1)},
        {(0,0),(0,1),(1,1),(1,2),(2,2)},
        {(0,0),(1,0),(1,2),(2,1)},set(product(range(3),repeat=2))]
    K3=[{(i,i):0 for i in range(3)}|{(0,1):1,(1,2):2},
        {(i,i):0 for i in range(3)}|{(0,1):2,(1,0):1,(1,2):1,(2,1):2}]
    for H in H3:
        for K in K3:
            stats['graph_cost_models']+=1
            for s in product(range(3),repeat=3):
                for t in product(range(3),repeat=3):check(s,t,H,K,stats)
    # 4 native X6 Cells: one actual c0->c1 TRANSFER; old receiver c3.
    H={(0,1)};K={(i,i):0 for i in range(4)}|{(3,2):1,(2,1):1}
    W,B=effective(H,shortest(K,4),1,4);s=(1,);t=(0,0,0,1)
    fourcost,X=mincost(s,t,W)
    assert fourcost==2 and X==[[0,0,0,1]] and B[0][3]==1
    assert hall(s,t,W)==0
    K1={(i,i):0 for i in range(4)}|{(3,2):1}
    W1,_=effective(H,shortest(K1,4),1,4)
    assert hall(s,t,W1)==1 and mincost(s,t,W1)[0]==INF
    # Nonnegative primitive PASS seed: old port1 -> new port3 retarget.
    M=[[0]*4 for _ in P]
    for a,b in ((0,1),(2,0),(2,3),(3,0)):M[a][b]+=1
    O=[[M[i][j]-M[j][i] for j in P] for i in P]
    u0=[sum(M[i])-sum(M[j][i] for j in P) for i in P];u0[1]+=1
    S=(0,1,4)
    old,new=gapcheck(S,u0,O,[(1,3,1)])
    assert old[0]==(3,(1,2,4)) and new[0]==(3,(0,3,4))
    assert old[0][0]-old[1][0]==1 and new[0][0]-new[1][0]==1
    assert [u0[i]+int(i==3)-int(i==1) for i in P]==[-1,-1,2,1]
    tested=0
    for m in range(4):
        M=[[0]*4 for _ in P]
        for a,b in ((0,1),(2,0),(2,3),(3,0)):M[a][b]+=m
        Om=[[M[i][j]-M[j][i] for j in P] for i in P]
        base=[sum(M[i])-sum(M[j][i] for j in P) for i in P]
        for op in P:
            for np in P:
                if op==np:continue
                u=list(base);u[op]+=1
                for triad in TRIADS:
                    if gapcheck(triad,u,Om,[(op,np,1)]) is not None:tested+=1
    print(json.dumps(dict(marker='R655_CONSTRAINED_TARGET_MINCOST_BRC_GAP_EXACT_PASS',
        scope='Composed Hall graph and directed weighted receiver relocation; exact integers',
        stats=stats,score_checks=tested,
        native_four_cell_example=dict(Hall_unrestricted=1,one_step_Hall=1,
          one_step_feasible=False,two_step_min_cost=2,
          actual_transfer='c0/port0 -> c1/port0'),
        signed_winner_change=dict(seed_PASS=[(0,1),(2,0),(2,3),(3,0)],
           old_receiver_port=1,new_receiver_port=3,active_triad=(0,1,4),
           old_winner=(1,2,4),new_winner=(0,3,4),old_gap=1,new_gap=1,
           signed_delta_u=(0,-1,0,1))),ensure_ascii=False,indent=2))
if __name__=='__main__':main()