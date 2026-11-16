#!/usr/bin/env python3
"""Independent standard-library k=6 two-Set coherent 11-state lower core.
Frozen source pin: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
"""
import json
k=6;N=1<<k;T=1<<(k-2);J=(0,1)
CORE=(3,5,6,9,10,11,12,13,14,15)
q=lambda x:sum(((x>>i)&1)*((x>>((i+1)%k))&1) for i in range(k))
qs=[q(x) for x in range(N)]
def good(r,u):return (u&~r)==0 and 0<=qs[r]-qs[u]<=2
masks=[[sum(1<<t for t in range(T) if good(r,(t<<2)|a)) for r in range(N)] for a in range(4)]
costs={}
for S_mask in range(4):
    S=[i for i in J if S_mask>>i&1];choices=[]
    for p in range(1<<len(S)):
        alphas=[a for a in range(4) if sum(((a>>i)&1)<<j for j,i in enumerate(S))==p]
        ms=set()
        for r in range(N):
            v=(1<<T)-1
            for a in alphas:v &= masks[a][r]
            if v:ms.add(v)
        choices.append(ms)
    eligible={(1<<T)-1}
    for cs in choices:eligible={a&b for a in eligible for b in cs if a&b}
    for mask in eligible:costs[mask]=min(costs.get(mask,100),1<<len(S))
assert len(costs)==41

def cover_min(rows):
    compressed={}
    for mask,c in costs.items():
        m=sum(1<<j for j,t in enumerate(rows) if mask>>t&1)
        if m:compressed[m]=min(c,compressed.get(m,100))
    full=(1<<len(rows))-1;dp=[100]*(full+1);dp[0]=0
    for m in range(full+1):
        for c,w in compressed.items():
            if dp[m|c]>dp[m]+w:dp[m|c]=dp[m]+w
    return dp[full],compressed
value,compressed=cover_min(CORE)
expected=[(1,1),(2,1),(4,1),(5,4),(7,4),(8,2),(16,1),(32,2),(33,2),
          (57,4),(64,1),(128,2),(192,2),(202,4),(256,1),(320,2),
          (324,4),(340,4),(512,2),(768,4),(928,4)]
assert sorted(compressed.items())==expected
assert value==11
leave_one_out={str(t):cover_min(tuple(x for x in CORE if x!=t))[0] for t in CORE}
assert max(leave_one_out.values())<=10
print(json.dumps({'status':'PASS_R5_K6_TEN_TAIL_EXACT_CORE','core_rows':CORE,
                  'all_16_tail_candidates':len(costs),'core_candidates':len(compressed),
                  'core_weighted_masks':expected,'minimum_states':value,
                  'drop_one_minima':leave_one_out},indent=2,sort_keys=True))
