#!/usr/bin/env python3
"""Exact nearest-old-optimizer forced-coordinate certificate for the frozen R5 K=214 witnesses.
Computes lexicographic (cost, negative overlap) path DP in both directions and counts
all globally nearest old optimum paths. Standard library only, no floating point.
"""
import json
import sys
from collections import Counter
from fractions import Fraction

W=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
K=214
INF=10**10

def frozen():
    p={3:set(),12:set(),15:set()};n=k=mask=0
    for t in range(1,1<<15):
        bit=t&-t;i=bit.bit_length()-1;mask^=bit;sgn=1 if mask&bit else -1
        n+=sgn*W[i];k+=sgn*K0[i]
        if n>=3 and k%36==0 and k//36 in p:p[k//36].add(n)
    e=Counter(Fraction(v,q) for q,vals in p.items() for v in vals)
    x=[0]
    for v in sorted(e): x.append(x[-1]+e[v])
    cuts=[i for i in range(len(x)-1) if x[i+1]-x[i]==3]
    assert len(x)==954 and len(cuts)==28 and x[-1]==1065
    return x,cuts

def graph(z):
    n=len(z);incoming=[[] for _ in z]; outgoing=[[] for _ in z];pref=[INF]*n;tail=[INF]*n
    for j in range(n):
        if z[j]-z[0]<=2: pref[j]=sum(z[j]-z[t] for t in range(j))
        if z[-1]-z[j]<=2: tail[j]=sum(z[t]-z[j] for t in range(j+1,n))
        for i in range(j-1,-1,-1):
            if z[j]-z[i]>7: break
            mids=[min(z[t]-z[i],z[j]-z[t]) for t in range(i+1,j)]
            if max(mids,default=0)<=2:
                w=sum(mids)
                incoming[j].append((i,w));outgoing[i].append((j,w))
    return incoming,outgoing,pref,tail

def lexadd(v,w,bonus=0):
    return v[0]+w,v[1]-bonus

def analyze(S,G,expected_cost=1064):
    incoming,outgoing,pref,tail=G
    n=len(pref);pres=set(S);bon=[int(j in pres) for j in range(n)]
    # F[t][j], A[t][j]: best prefix with t centers, and count of optimal such prefixes
    F=[];A=[]
    for t in range(K):
        f=[None]*n;a=[0]*n
        if t==0:
            for j in range(n):
                if pref[j]<INF: f[j]=(pref[j],-bon[j]);a[j]=1
        else:
            old=F[-1];old_a=A[-1]
            for j in range(n):
                if not incoming[j]:continue
                m=None;c=0
                for i,w in incoming[j]:
                    if old[i] is None:continue
                    v=lexadd(old[i],w,bon[j]);cnt=old_a[i]
                    if m is None or v<m:m=v;c=cnt
                    elif v==m:c+=cnt
                f[j]=m;a[j]=c
        F.append(f);A.append(a)
    # H[m][j], B[m][j]: best suffix from j, with m centers INCLUDING j but its bonus excluded
    # This suffix includes tail and all centers after j; no prefix cost.
    H=[];B=[]
    for mindex in range(K):
        h=[None]*n;b=[0]*n
        if mindex==0:
            for j in range(n):
                if tail[j]<INF:h[j]=(tail[j],0);b[j]=1
        else:
            old=H[-1];old_b=B[-1]
            for i in range(n):
                choice=None;c=0
                for j,w in outgoing[i]:
                    if old[j] is None:continue
                    v=lexadd(old[j],w,bon[j]);cnt=old_b[j]
                    if choice is None or v<choice:choice=v;c=cnt
                    elif v==choice:c+=cnt
                h[i]=choice;b[i]=c
        H.append(h);B.append(b)
    best=None;tot=0
    for j in range(n):
        if F[K-1][j] is None or H[0][j] is None:continue
        v=(F[K-1][j][0]+tail[j],F[K-1][j][1]);cnt=A[K-1][j]
        if best is None or v<best: best=v;tot=cnt
        elif best==v:tot+=cnt
    assert best is not None and best[0]==expected_cost
    # exhaustive edge tie-count through each node: F[t,j] and H[K-t,j] represent disjoint portions.
    marg=[0]*n;states=0
    for t in range(K):
        frow=F[t];hrow=H[K-1-t]
        arow=A[t];brow=B[K-1-t]
        for j in range(n):
            if frow[j] is None or hrow[j] is None:continue
            if (frow[j][0]+hrow[j][0], frow[j][1]+hrow[j][1])==best:
                marg[j]+=arow[j]*brow[j];states+=1
    assert sum(marg)==K*tot,(sum(marg),K*tot)
    assert all(0<=v<=tot for v in marg)
    return {'closest_swaps':K+best[1], 'max_overlap':-best[1], 'nearest_count':tot,
           'forced_removed':sorted(j for j in S if marg[j]==0),
           'common_retained':sorted(j for j in S if marg[j]==tot),
           'optional_retained':sorted(j for j in S if 0<marg[j]<tot),
           'forced_additions':sorted(j for j in range(n) if j not in pres and marg[j]==tot),
           'optional_additions':sorted(j for j in range(n) if j not in pres and 0<marg[j]<tot),
           'states_on_nearest_opt_paths':states,
           'marginals_for_near_original_witness':{str(j):str(marg[j]) for j in S if 0<marg[j]<tot}}

def main():
    witness_path=sys.argv[1] if len(sys.argv)>1 else 'EXACT_R5_K214_NONLOCAL_RECOURSE.json'
    data=json.load(open(witness_path,encoding='utf-8'))
    x,cuts=frozen();G=graph(x)
    result=[]
    for row in data['witnesses']:
        S=row['new_optimal_centers'];r=analyze(S,G)
        assert r['closest_swaps']==row['exact_min_swaps'],(row['cut'],r['closest_swaps'])
        result.append({'cut':row['cut'],'cut_event_index':cuts[row['cut']],
                       'witness_old_nearest_out':row['replace_out'],
                       'witness_old_nearest_in':row['replace_in'],
                       **r})
    print(json.dumps({'status':'PASS_EXACT_R5_FORCED_COORDINATE_CLASSIFICATION',
        'science_input':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
        'witness_source_sha256':'53072d874619a1eb6bede5e43d647d7d5c228f83371ea76b05eba03b5a81da82',
        'K':K,'rows':result,'math_review':'NOT_REVIEWED'},indent=2,sort_keys=True))

if __name__=='__main__':main()
