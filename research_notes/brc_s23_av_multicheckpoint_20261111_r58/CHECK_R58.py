#!/usr/bin/env python3
"""R58 exact multi-checkpoint grouped phase-state oracle; auxiliary rational-circle model."""
from bisect import bisect_right
from math import gcd
from random import Random
import json

PIN='43ec6098b1330ae86d0a7863be336c5d97f6ef34'

def farey_bracket(p,q,K):
    a,i,c,j=0,1,1,1
    while i+j<=K:
        if (a+c)*q < (i+j)*p: a,i=a+c,i+j
        else: c,j=c+a,j+i
    return i,j

def cut_prefix(p,q,m,H,kmax):
    K=m+H-1
    i,j=farey_bracket(p,q,K)
    s=j
    out=[]
    for _ in range(kmax):
        out.append(s)
        s=s-i if s>i else (s+j if s+j<=K else s+j-i)
    return i,j,out

def latest(owners,m):
    v=[None]*m
    for r,z in enumerate(owners,1):
        if v[z] is None: v[z]=r
    return v

def phase_oracle(p,q,m,H,x):
    boundaries=sorted((2*((z*p)%q),z) for z in range(m))
    vals=[v for v,z in boundaries]
    labels=[z for v,z in boundaries]
    return [labels[bisect_right(vals,(x-2*r*p)%(2*q))-1] for r in range(1,H+1)]

def run(p,q,m,H,queries,verify=True):
    K=m+H-1
    assert 0<p<q and q//gcd(p,q)>K
    assert all(isinstance(k,int) and 0<=k<=K for k in queries)
    kmax=max(queries,default=0)
    i,j,cuts=cut_prefix(p,q,m,H,kmax)
    assert len(set(cuts))==kmax
    if verify: assert all(((cuts[t]*p)%q)>((cuts[t+1]*p)%q) for t in range(kmax-1))
    # R57 initial observer phase is strictly above the largest positive cut.
    first=((j*p)%q)
    x0=q+first
    boundary=sorted((((z*p)%q),z) for z in range(m))
    B=[z for ph,z in boundary]
    rank={z:n for n,z in enumerate(B)}
    pred={z:B[(n-1)%m] for n,z in enumerate(B)}
    initial=phase_oracle(p,q,m,H,x0)
    # Bucket by cut rank, allowing arbitrary query order and duplicate checkpoints.
    buckets=[[] for _ in range(kmax+1)]
    for query_index,k in enumerate(queries): buckets[k].append(query_index)
    answer=[None]*len(queries)
    diff=[0]*(H+2)
    moves=0
    def report(k):
        c=0; ownership=[]
        for r in range(1,H+1):
            c+=diff[r]
            ownership.append(B[(rank[initial[r-1]]-c)%m])
        youngest=latest(ownership,m)
        if verify:
            if k==0: x=x0
            elif k==K: x=((cuts[-1]*p)%q)
            else: x=((cuts[k-1]*p)%q)+((cut_prefix(p,q,m,H,k+1)[2][-1]*p)%q)
            expected=phase_oracle(p,q,m,H,x)
            assert ownership==expected, (p,q,m,H,k,'owners')
            assert youngest==latest(expected,m)
        return (ownership,youngest)
    for k in range(kmax+1):
        if k:
            s=cuts[k-1]
            lo=max(1,s-m+1); hi=min(H,s)
            assert lo<=hi
            diff[lo]+=1;diff[hi+1]-=1
            moves+=hi-lo+1
        if buckets[k]:
            result=report(k)
            for idx in buckets[k]:answer[idx]=result
    if verify:
        # Independent event-by-event replay of every original label, not just endpoint values.
        live=initial[:]
        for t,s in enumerate(cuts,1):
            for r in range(max(1,s-m+1),min(H,s)+1):
                z=s-r
                assert live[r-1]==z,(m,H,t,r,z,live[r-1])
                live[r-1]=pred[z]
            if buckets[t]:assert live==answer[buckets[t][0]][0]
        if buckets[0]:assert initial==answer[buckets[0][0]][0]
    return {'m':m,'H':H,'K':K,'k_max':kmax,'Q':len(queries),
            'Farey_lower_denominator':i,'Farey_upper_denominator':j,
            'delta_endpoint_updates':2*kmax,
            'source_owner_outputs':len(queries)*H,
            'youngest_label_outputs':len(queries)*m,
            'individual_events_avoided':moves,
            'full_tour_events':m*H,'answers':answer}

def main():
    rng=Random(580011)
    case_count=0; total_individual=0; total_endpoints=0; total_queries=0
    for m in range(1,13):
        for H in range(1,16):
            K=m+H-1
            for rep in range(8):
                p=rng.randrange(1,1009)
                # Nonchronological order, duplicates, initial/final, and 3 interior cuts.
                qs=[K,0,(rep*59+m*13+H*7)% (K+1), K//2, 1, K]
                rng.shuffle(qs)
                z=run(p,1009,m,H,qs)
                case_count+=1;total_individual+=z['individual_events_avoided'];total_endpoints+=z['delta_endpoint_updates'];total_queries+=z['Q']
    assert case_count==1440
    D=10**24; lo=262204504569236716045286
    frozen=[]
    for p in (lo,lo+1):
        qs=[352,0,1,4,32,88,176,264,352,176,351,225,61,126,127,163,164]
        rng.shuffle(qs)
        z=run(p,D,128,225,qs)
        assert z['Farey_lower_denominator']==164 and z['Farey_upper_denominator']==225
        assert z['individual_events_avoided']==28800
        assert z['delta_endpoint_updates']==704
        assert z['answers'][qs.index(0)]==z['answers'][qs.index(352)]
        for k in (0,176,352):
            if k==0: x=D+((225*p)%D)
            elif k==352:
                cs=cut_prefix(p,D,128,225,352)[2];x=(cs[-1]*p)%D
            else:
                cs=cut_prefix(p,D,128,225,177)[2]
                x=(cs[175]*p)%D+(cs[176]*p)%D
            for j_phys in (-10**18,10**12+128,10**18):
                phys=(x-2*j_phys*p)%(2*D)
                for r in range(1,226):
                    assert (phys+2*(j_phys-r)*p)%(2*D)==(x-2*r*p)%(2*D)
        frozen.append({k:v for k,v in z.items() if k!='answers'})
    # R56 newest source state is insufficient for arbitrary deletion.
    A={1,2};B={2}; old_A=max(A);old_B=max(B)
    assert old_A==old_B==2
    A.remove(2);B.remove(2)
    assert max(A)==1 and len(B)==0
    result={'science_pin':PIN,'claim':'author exact finite verification, no independent review',
            'small_cases':case_count,'small_checkpoint_queries':total_queries,
            'small_replayed_events':total_individual,'small_delta_endpoints':total_endpoints,
            'frozen_cases':frozen,
            'deletion_witness':{'A_before':[1,2],'B_before':[2],'latest_before':2,'delete':2,'A_latest_after':1,'B_latest_after':None}}
    with open('/mnt/data/em_r58/CERTIFICATE.json','w',encoding='utf-8') as f:json.dump(result,f,indent=2,ensure_ascii=False)
    print('PASS_R58',case_count,'checkpoint_queries',total_queries,'microevents',total_individual,'delta_updates',total_endpoints,'S23',frozen,'deletion_witness_ok')
if __name__=='__main__':main()
