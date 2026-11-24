#!/usr/bin/env python3
"""Independent exact integer audit of rank-labeled radius-2 optimizer-DAG frontiers.

Frozen R5 science pin 435e77af0d180eac32bd1f9c4c464bc4010b7551;
uses the finite generator in the neighboring geometric-support verifier.
For each of 32 effective masks and K=214..221, compute optimal DAG
from first principles, then count all crossing vertex-rank pairs and their
spatial tail supports at every integer event-index threshold.
"""
from VERIFY_R5_FRONTIER_SPATIAL_SUPPORT import frozen,close,BITS,band
from collections import Counter,defaultdict
import json
INF=10**14

def costs(z,maxK=221):
    n=len(z)
    outgoing=[[] for _ in range(n)]; incoming=[[] for _ in range(n)]
    pref=[INF]*n;tail=[INF]*n
    for j in range(n):
        if z[j]-z[0]<=2:pref[j]=sum(z[j]-z[t] for t in range(j))
        if z[-1]-z[j]<=2:tail[j]=sum(z[t]-z[j] for t in range(j+1,n))
        for i in range(j-1,-1,-1):
            if z[j]-z[i]>7:break
            mid=[min(z[t]-z[i],z[j]-z[t]) for t in range(i+1,j)]
            if max(mid,default=0)<=2:
                w=sum(mid)
                outgoing[i].append((j,w));incoming[j].append((i,w))
    C=[pref]
    for k in range(1,maxK):
        last=C[-1]
        C.append([min((last[i]+w for i,w in incoming[j]),default=INF) for j in range(n)])
    D=[tail]
    for k in range(1,maxK):
        last=D[-1]
        D.append([min((last[j]+w for j,w in outgoing[i]),default=INF) for i in range(n)])
    J=[min(C[k-1][j]+tail[j] for j in range(n)) for k in range(1,maxK+1)]
    return outgoing,C,D,J

def frontier_stats(z,dp,K):
    out,C,D,J=dp;n=len(z);target=J[K-1]
    L=[{i for i in range(n) if C[r][i]+D[K-1-r][i]==target} for r in range(K)]
    entering=[[] for _ in range(n+1)];leaving=[[] for _ in range(n+1)]
    vcount=0;ecount=0
    for r in range(K-1):
        for i in L[r]:
            good=[q for q,w in out[i] if q in L[r+1] and C[r][i]+w==C[r+1][q]]
            if good:
                last=max(good)
                entering[i].append(i)
                leaving[last].append(i)
                vcount+=1;ecount+=len(good)
    active=Counter();width=0;support=0;rankmax=0;worst=None
    for j in range(n):
        for i in leaving[j]:
            active[i]-=1
            if active[i]==0:del active[i]
        for i in entering[j]:active[i]+=1
        if len(active)>5:raise AssertionError(('five',K,j,z,active))
        if not set(active)<=band(z,j):raise AssertionError(('band',K,j,z,active))
        w=sum(active.values())
        if w>width:width=w;worst=j
        support=max(support,len(active))
        rankmax=max(rankmax,max(active.values(),default=0))
    return {'K':K,'cost':target,'optimal_arc_tails':vcount,'optimal_edges':ecount,
            'max_frontier_width':width,'max_distinct_spatial_tails':support,
            'max_rank_multiplicity_per_tail':rankmax,'max_width_at_event_index':worst}

def main():
    x,cuts=frozen();rows=[]
    for mask in range(32):
        z=close(x,cuts,[bit for idx,bit in enumerate(BITS) if mask>>idx&1]);dp=costs(z)
        for K in range(214,222):
            row=frontier_stats(z,dp,K);row['effective_mask']=mask
            rows.append(row)
    assert len(rows)==256
    print(json.dumps({'status':'PASS_R5_OPTIMAL_FRONTIER_RANK_AUDIT',
                      'scientific_input_commit':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
                      'masks':32,'budgets':[214,221],
                      'max_global_frontier_width':max(x['max_frontier_width'] for x in rows),
                      'max_global_distinct_tails':max(x['max_distinct_spatial_tails'] for x in rows),
                      'max_rank_multiplicity_per_tail':max(x['max_rank_multiplicity_per_tail'] for x in rows),
                      'observations':rows},sort_keys=True,indent=2))
if __name__=='__main__':main()
