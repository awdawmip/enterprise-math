"""R713 exact direct BRC triad membership-query certificate (Python standard library)."""
from itertools import combinations
from collections import Counter
from array import array
import json

V=range(6)
E=list(combinations(V,2))
T=list(combinations(V,3))
pair_index={p:i for i,p in enumerate(E)}
tri_pair=[sum(1<<pair_index[p] for p in combinations(t,2)) for t in T]
full=(1<<15)-1

def union_pairs(indices):
    out=0
    for i in indices: out|=tri_pair[i]
    return out

def classify(g):
    ts=[i for i,p in enumerate(tri_pair) if p&g==p]
    counts=[sum((p>>j)&1 for i in ts for p in [tri_pair[i]]) for j in range(15)]
    feasible=all(not(g>>j&1) or counts[j]>0 for j in range(15))
    forced=[i for i in ts if any(tri_pair[i]>>j&1 and counts[j]==1 for j in range(15))]
    optional=[i for i in ts if i not in forced]
    return feasible,forced,optional,ts

def inclusion_exclusion(g):
    active=[i for i in range(15) if g>>i&1]
    allowed=[p for p in tri_pair if p&g==p]
    ans=0
    for s in range(1<<len(active)):
        prohibited=sum(1<<active[j] for j in range(len(active)) if s>>j&1)
        surviving=sum(p&prohibited==0 for p in allowed)
        ans+=(-1 if s.bit_count()&1 else 1)*(1<<surviving)
    return ans

shadow=array('H',[0])*(1<<20)
fibers=[0]*(1<<15)
for h in range(1<<20):
    if h:
        lb=h&-h
        shadow[h]=shadow[h^lb]|tri_pair[lb.bit_length()-1]
    fibers[shadow[h]]+=1
assert sum(fibers)==1<<20
query_hist=Counter()
gap_hist=Counter()
for g,f in enumerate(fibers):
    feasible,forced,optional,ts=classify(g)
    assert feasible==(f>0)
    if not f:continue
    assert union_pairs(ts)==g
    for i in forced: assert union_pairs(j for j in ts if j!=i)!=g
    for i in optional: assert union_pairs(j for j in ts if j!=i)==g
    q=len(optional)
    bits=(f-1).bit_length()
    assert q>=bits
    query_hist[q]+=1
    gap_hist[q-bits]+=1

k6m1=full^(1<<pair_index[(0,1)])
assert sum(query_hist.values())==6115
assert fibers[full]==477965 and fibers[k6m1]==21450
assert inclusion_exclusion(full)==477965
assert inclusion_exclusion(k6m1)==21450
assert len(classify(full)[2])==20 and len(classify(k6m1)[2])==16
assert all(fibers[full^(1<<i)]==21450 for i in range(15))
assert all(fibers[g]<21450 for g in range(full) if g.bit_count()<14)
assert dict(gap_hist)=={0:3373,1:2137,2:585,3:20}
print('R713_BRC_TRIAD_QUERY_EXACT_PASS 6115 477965 21450 20 16')
print('Q_HIST',sorted(query_hist.items()))
print('GAP_HIST',sorted(gap_hist.items()))
output={
 'domain':{'axis_labels':6,'source_triads':20,'pair_labels':15,'states':1<<20,'pair_masks':1<<15},
 'theorem':'Q_direct(G)=|{t in T(G): each pair e in t has graph triangle codegree >=2}| for each feasible G',
 'feasible_shadows':6115,
 'K6':{'fiber':477965,'auxiliary_bits':19,'direct_membership_queries':20},
 'K6_minus_edge':{'fiber':21450,'auxiliary_bits':15,'direct_membership_queries':16,'labelled_cases':15},
 'second_max_fiber_exact':21450,
 'Q_histogram':dict(sorted(query_hist.items())),
 'direct_query_minus_aux_bit_gap':dict(sorted(gap_hist.items())),
 'verification':'2^20 exhaustive enumeration, 2^15 graph classification, independent inclusion-exclusion K6 and K6-e, optional/forced deletion witnesses'
}
with open('R713_BRC_TRIAD_QUERY_RESULTS.json','w') as out:
    json.dump(output,out,sort_keys=True,indent=2)
    out.write('\n')
