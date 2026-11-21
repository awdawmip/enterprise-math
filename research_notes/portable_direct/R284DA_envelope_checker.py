#!/usr/bin/env python3
"""Exact event envelope of the frozen Port farthest-arc observer (R284DA)."""
from R284CO_spectral_witness_checker import P,FROZEN_SHA,words,arcs,dist
from collections import Counter,defaultdict
from itertools import combinations
from bisect import bisect_right
from pathlib import Path
import hashlib,json

def envelope(A):
    events=defaultdict(list); segs=0
    for a,w in A:
        assert 0<w<P//2
        for k in (-1,0):
            b=a+w+k*P; e=a+(k+1)*P; mid=(b+e)//2
            for lo,hi,s,c in ((b,mid+1,1,-b),(mid+1,e+1,-1,e)):
                lo=max(0,lo); hi=min(P,hi)
                if lo<hi:
                    events[lo].append(((s,c),1))
                    events[hi].append(((s,c),-1))
                    segs+=1
    events[0];events[P];times=sorted(events);active=Counter();plus=[];minus=[]
    for t in times[:-1]:
        for key,delta in events[t]:
            active[key]+=delta
            assert active[key]>=0
            if active[key]==0:del active[key]
        pos=[c for (s,c) in active if s==1]
        neg=[c for (s,c) in active if s==-1]
        plus.append(max(pos) if pos else None)
        minus.append(max(neg) if neg else None)
    return times,plus,minus,segs

def farthest(x,times,plus,minus):
    i=bisect_right(times,x)-1
    return max(0,x+plus[i] if plus[i] is not None else 0,
               minus[i]-x if minus[i] is not None else 0)

def main():
    X=words(); A=arcs(); T,up,dn,segments=envelope(A)
    F=[farthest(x,T,up,dn) for x in X]
    assert F==[max(dist(x,a) for a in A) for x in X]
    count=Counter(); equal=[]; edges=0
    for i,v in enumerate(F):
        upper,lower=divmod(i,4096)
        for p in range(12):
            j=upper*4096+(lower^(1<<(11-p)))
            if j>i:
                edges+=1
                if v==F[j]:
                    equal.append(('flip',str(p),i,j,v));count[f'flip:{p}']+=1
        for p,q in combinations(range(12),2):
            if ((lower>>(11-p))&1)==((lower>>(11-q))&1):continue
            j=upper*4096+(lower^(1<<(11-p))^(1<<(11-q)))
            if j>i:
                edges+=1
                if v==F[j]:
                    equal.append(('swap',f'{p},{q}',i,j,v))
                    count[f'swap:{p},{q}']+=1
    assert edges==1474560 and len(equal)==307
    assert count==Counter({'flip:0':3,'flip:1':14,'flip:2':228,
                          'flip:4':16,'flip:6':45,'swap:0,1':1})
    selected={i for _,_,i,j,_ in equal}|{j for _,_,i,j,_ in equal}
    winners={}
    for i in selected:
        ds=[dist(X[i],a) for a in A]
        ids=[j for j,d in enumerate(ds) if d==F[i]]
        assert len(ids)==1
        winners[i]=ids[0]
    serialized=[(kind,mutation,i,j,v,winners[i],winners[j])
                for kind,mutation,i,j,v in equal]
    edge_sha=hashlib.sha256(json.dumps(serialized,separators=(',',':'),ensure_ascii=False)
                            .encode('utf8')).hexdigest()
    assert edge_sha=='251a3ca8d2d72cf6f7ca19869f174eb9e370f330533e484faf13dcb2a68dab8b'
    coefficient_runs=1+sum((up[i],dn[i])!=(up[i-1],dn[i-1])
                            for i in range(1,len(up)))
    cert={'schema':'R284DA_EXACT_FARTHEST_ENVELOPE_V1',
          'status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
          'P':P,'frozen_codeword_sha256':FROZEN_SHA,
          'codewords':len(X),'arcs':len(A),
          'branch_segments':segments,'event_positions':len(T),
          'event_slabs':len(up),'coefficient_runs':coefficient_runs,
          'selected_equal_edge_endpoints':len(selected),
          'arc_distance_calls_to_recover_equal_edge_winners':64*len(selected),
          'independent_full_distance_baseline_verified':True,
          'graph_edges':edges,'equal_graph_edges':len(equal),
          'equal_by_mutation':dict(sorted(count.items())),
          'canonical_307_edge_sha256':edge_sha,
          'scope':'Frozen auxiliary Port observer and one-flip/unequal-swap source graph'}
    Path(__file__).with_name('R284DA_envelope_certificate.json').write_text(
        json.dumps(cert,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps(cert,ensure_ascii=False))

if __name__=='__main__': main()
