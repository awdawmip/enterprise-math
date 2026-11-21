#!/usr/bin/env python3
"""R284DD: exact farthest-arc label propagation and 307-edge digest without direct distances."""
from R284CO_spectral_witness_checker import P,FROZEN_SHA,words,arcs,dist
from itertools import combinations
from collections import Counter,defaultdict
from bisect import bisect_right
from pathlib import Path
import json,hashlib

EXPECTED='251a3ca8d2d72cf6f7ca19869f174eb9e370f330533e484faf13dcb2a68dab8b'

def attributed_envelope(A):
    events=defaultdict(list)
    for arc_id,(a,w) in enumerate(A):
        assert 0<w<P
        for k in (-1,0):
            b=a+w+k*P; e=a+(k+1)*P; mid=(b+e)//2
            for lo,hi,s,c in ((b,mid+1,1,-b),(mid+1,e+1,-1,e)):
                lo=max(lo,0);hi=min(hi,P)
                if lo<hi:
                    key=(s,c,arc_id)
                    events[lo].append((key,1));events[hi].append((key,-1))
    events[0];events[P]
    times=sorted(events);active=Counter(); profiles=[]
    for t in times[:-1]:
        for key,d in events[t]:
            active[key]+=d
            assert active[key]>=0
            if not active[key]:del active[key]
        classes=[]
        for s in (1,-1):
            candidates=[(c,label) for (ss,c,label) in active if ss==s]
            if not candidates:
                classes.append((None,()))
            else:
                max_c=max(c for c,_ in candidates)
                classes.append((max_c,tuple(sorted(label for c,label in candidates if c==max_c))))
        profiles.append(tuple(classes))
    return times,profiles

def labeled_farthest(x,T,profiles,number_arcs):
    p,n=profiles[bisect_right(T,x)-1]
    terms=[(0,None)]
    if p[0] is not None:terms.extend((x+p[0],label) for label in p[1])
    if n[0] is not None:terms.extend((n[0]-x,label) for label in n[1])
    m=max(v for v,_ in terms)
    ids=tuple(sorted({label for v,label in terms if v==m and label is not None}))
    if m==0:ids=tuple(range(number_arcs))
    return (m,ids)

def main():
    X=words();A=arcs();T,profiles=attributed_envelope(A)
    parsed=[labeled_farthest(x,T,profiles,len(A)) for x in X]
    assert all(len(ids)==1 for _,ids in parsed)
    # Independent exact baseline validates values AND arc labels; only this test uses direct dist.
    baseline=[]
    for x in X:
        ds=[dist(x,a) for a in A]
        v=max(ds);baseline.append((v,tuple(j for j,d in enumerate(ds) if d==v)))
    assert parsed==baseline
    buckets=defaultdict(list)
    for i,(v,_) in enumerate(parsed):buckets[v].append(i)
    hist=Counter(map(len,buckets.values()))
    assert hist==Counter({1:64760,2:366,3:8,4:5})
    pairs=sum(n*(n-1)//2 for n in map(len,buckets.values()))
    assert pairs==420
    edges=[];rejected=0
    for v,ids in buckets.items():
        for i,j in combinations(ids,2):
            if i//4096!=j//4096:
                rejected+=1;continue
            lo=i%4096;mask=lo^(j%4096)
            p,q=-1,-1
            if mask.bit_count()==1:
                p=11-(mask.bit_length()-1)
                kind,mutation='flip',str(p)
            elif mask.bit_count()==2 and (lo&mask).bit_count()==1:
                p,q=[t for t in range(12) if mask&(1<<(11-t))]
                kind,mutation='swap',f'{p},{q}'
            else:
                rejected+=1;continue
            edges.append((kind,mutation,i,j,v,p,q))
    assert (len(edges),rejected)==(307,113)
    edges.sort(key=lambda e:(e[2],0 if e[0]=='flip' else 1,e[5],e[6]))
    canonical=[[kind,mutation,i,j,v,parsed[i][1][0],parsed[j][1][0]]
               for kind,mutation,i,j,v,_,_ in edges]
    sha=hashlib.sha256(json.dumps(canonical,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
    assert sha==EXPECTED
    cert={
      'schema':'R284DD_FULLY_ATTRIBUTED_EXACT_TWO_SLOPE_ENVELOPE_V1',
      'status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
      'frozen_codeword_sha256':FROZEN_SHA,'codewords':len(X),'arcs':len(A),
      'event_positions':len(T),'event_slabs':len(profiles),
      'unique_maximizing_arc_sites':len(parsed),
      'distance_or_label_direct_arc_calls_in_new_algorithm':0,
      'independent_validation_arc_distance_calls':len(X)*len(A),
      'all_max_values_and_argmax_labels_match_direct_baseline':True,
      'distinct_farthest_values':len(buckets),'within_bucket_pairs':pairs,
      'equal_source_graph_edges':len(edges),'canonical_307_edge_sha256':sha,
      'requires_full_65k_farthest_profile':True,
      'scope':'Exact integer circular arcs generally; numeric census only frozen Port observer'
    }
    Path(__file__).with_name('R284DD_attributed_envelope_certificate.json').write_text(
        json.dumps(cert,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print(json.dumps(cert,ensure_ascii=False))

if __name__=='__main__':main()
