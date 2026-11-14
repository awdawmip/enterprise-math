#!/usr/bin/env python3
"""Exact R5 all-pattern center-cover cost-spectrum classifier.

Scope: frozen derived 1D integer-event, radius-2 observer.
Scientific input pin: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Standard-library-only exact integer and rational calculation.
"""
from collections import Counter
from fractions import Fraction
import json
import random

W = (336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0 = (-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
SCIENCE_PIN='435e77af0d180eac32bd1f9c4c464bc4010b7551'
Q=6
INF=10**9

def frozen():
    pools={3:set(),12:set(),15:set()};n=k=mask=0
    for t in range(1,1<<15):
        bit=t&-t;i=bit.bit_length()-1;mask^=bit
        sign=1 if mask&bit else -1
        n+=sign*W[i];k+=sign*K0[i]
        if n>=3 and k%36==0 and k//36 in pools:
            pools[k//36].add(n)
    assert [len(pools[q]) for q in (3,12,15)]==[538,298,229]
    events=Counter(Fraction(p,q) for q,values in pools.items() for p in values)
    x=[0]
    for value in sorted(events):x.append(x[-1]+events[value])
    cuts=[i for i in range(len(x)-1) if x[i+1]-x[i]>2]
    assert len(x)==954 and x[-1]==1065 and len(cuts)==28
    assert all(x[i+1]-x[i]==3 for i in cuts)
    return x,cuts

def closed_points(x,cuts,closed_mask):
    positions={cuts[i] for i in range(28) if (closed_mask>>i)&1}
    out=[];shift=0
    for i,v in enumerate(x):
        out.append(v-shift)
        if i in positions:shift+=1
    return out

def cluster_profile(x):
    """Independent of the selected-center edge recurrence below."""
    n=len(x); candidates=[[] for _ in range(n+1)]
    for b in range(1,n+1):
        for a in range(b-1,-1,-1):
            if x[b-1]-x[a]>4:break
            best=INF
            for j in range(a,b):
                if max(x[j]-x[a],x[b-1]-x[j])<=2:
                    best=min(best,sum(abs(x[t]-x[j]) for t in range(a,b)))
            if best<INF:candidates[b].append((a,best))
    prev=[INF]*(n+1);prev[0]=0;d=None;costs=[]
    for centers in range(1,n+1):
        nxt=[INF]*(n+1)
        for b in range(centers,n+1):
            nxt[b]=min((prev[a]+c for a,c in candidates[b]),default=INF)
        prev=nxt
        if prev[n]<INF:
            if d is None:d=centers
            costs.append(prev[n])
            if len(costs)==Q+1:break
    assert d is not None
    return d,tuple(costs+[INF]*(Q+1-len(costs)))

def product(p,q):
    dp,a=p;dq,b=q
    return dp+dq,tuple(min(a[i]+b[e-i] for i in range(e+1)) for e in range(Q+1))

def center_path_spectrum(x,max_centers=213):
    """Independent chosen-center path DP for full-size witness checking."""
    n=len(x);gap=max(x[j+1]-x[j] for j in range(n-1))
    incoming=[[] for _ in range(n)]
    for j in range(n):
        for i in range(j-1,-1,-1):
            if x[j]-x[i]>4+gap:break
            cost=0
            for t in range(i+1,j):
                d=min(x[t]-x[i],x[j]-x[t])
                if d>2:break
                cost+=d
            else:incoming[j].append((i,cost))
    prev=[INF]*n
    for j in range(n):
        if x[j]-x[0]<=2:
            prev[j]=sum(x[j]-x[t] for t in range(j))
    result={}
    for k in range(1,max_centers+1):
        if k>1:
            nxt=[INF]*n
            for j in range(n):
                nxt[j]=min((prev[i]+c for i,c in incoming[j]),default=INF)
            prev=nxt
        cost=min((prev[i]+sum(x[t]-x[i] for t in range(i+1,n))
            for i in range(n-1,-1,-1) if x[-1]-x[i]<=2),default=INF)
        if cost<INF:result[k]=cost
    return result

def compute():
    x,cuts=frozen()
    starts=[0]+[c+1 for c in cuts]
    ends=[c+1 for c in cuts]+[len(x)]
    # Every contiguous block interval is a fully closed local run.
    P={}
    for a in range(29):
        for b in range(a,29):
            coords=[];shift=0;ci=a
            for t in range(starts[a],ends[b]):
                coords.append(x[t]-shift)
                if ci<b and t==cuts[ci]:shift+=1;ci+=1
            P[a,b]=cluster_profile(coords)
    assert len(P)==435
    assert sum(P[i,i][0] for i in range(29))==213
    assert P[0,28][0]==207
    assert P[0,28][1][0]==1116 and P[0,28][1][6]==1069

    # A local factorization valid across every surrounding run is a
    # sufficient (and here exactly matched) all-pattern cost-inert certificate.
    inert=[];factorization_checks=0
    for i in range(28):
        failures=0
        for a in range(i+1):
            for b in range(i+1,29):
                factorization_checks+=1
                if P[a,b]!=product(P[a,i],P[i+1,b]):failures+=1
        if not failures:inert.append(i)
    assert factorization_checks==4060
    assert inert==[0,1,7,14,15,17,18,19,20,21,22,23,24]

    # Count partitions of 29 blocks; each partition is one unique
    # 28-bit closure pattern. Keep a canonical representative per state.
    states=[{} for _ in range(30)]
    states[0][(0,(0,)+(INF,)*Q)]=(1,0)
    sizes=[]
    for j in range(1,30):
        table={}
        for i in range(j):
            run=P[i,j-1]
            closed_bits=((1<<(j-i-1))-1)<<i
            for old,(number,mask) in states[i].items():
                key=product(old,run);candidate=mask|closed_bits
                if key in table:
                    n,representative=table[key]
                    table[key]=(n+number,min(representative,candidate))
                else:table[key]=(number,candidate)
        states[j]=table;sizes.append(len(table))
        assert sum(v[0] for v in table.values())==1<<(j-1)
    assert len(states[29])==32
    assert sum(v[0] for v in states[29].values())==1<<28

    classes=[]
    for (d,costs),(count,mask) in sorted(states[29].items()):
        classes.append(dict(D=d,J_D_to_J_D_plus_6=list(costs),count=count,
            representative_closed_gaps=[i for i in range(28) if mask>>i&1]))
    hist={}
    for K in range(207,214):
        counts=Counter()
        for row in classes:
            if row['D']>K:counts['INFEASIBLE']+=row['count']
            else:counts[str(row['J_D_to_J_D_plus_6'][K-row['D']])]+=row['count']
        assert sum(counts.values())==1<<28
        hist[str(K)]=dict(sorted(counts.items()))

    # Independent full-size nearest-center recurrence: all 32 classes.
    for row in classes:
        mask=sum(1<<i for i in row['representative_closed_gaps'])
        actual=center_path_spectrum(closed_points(x,cuts,mask))
        assert min(actual)==row['D']
        for K in range(row['D'],214):
            assert actual[K]==row['J_D_to_J_D_plus_6'][K-row['D']]
    rng=random.Random(20261114)
    for _ in range(12):
        mask=rng.randrange(1<<28)
        actual=center_path_spectrum(closed_points(x,cuts,mask))
        current=(0,(0,)+(INF,)*Q);start=0
        for i in range(28):
            if not (mask>>i)&1:
                current=product(current,P[start,i]);start=i+1
        current=product(current,P[start,28])
        d,c=current
        assert min(actual)==d
        for K in range(d,214):assert actual[K]==c[K-d]
    assert hist['207']=={'1116':229376,'INFEASIBLE':268206080}
    assert hist['213']=={'1069':201326592,'1070':67108864}
    assert hist['212']=={'1075':201326592,'1076':33554432,
                         '1077':28508160,'1084':630784,'INFEASIBLE':4415488}
    return dict(status='PASS_EXACT_R5_LOW_BUDGET_FULL_PATTERN_SPECTRUM',
        science_pin=SCIENCE_PIN,scope='derived one-dimensional radius-2 cover observer',
        event_count=len(x),cut_count=len(cuts),patterns=1<<28,
        interval_profiles=len(P),factorization_checks=factorization_checks,
        globally_cost_inert_cuts=inert,effective_cut_count=28-len(inert),
        full_spectrum_classes=len(classes),
        state_counts_after_each_block=sizes,
        exact_K_207_to_213_histograms=hist,
        classes=classes,independent_fullsize_class_witnesses=32,
        independent_seeded_extra_closures=12,
        independent_review='NOT_REVIEWED')

if __name__=='__main__':
    result=compute()
    print(json.dumps(result,ensure_ascii=False,indent=2))
