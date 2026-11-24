#!/usr/bin/env python3
"""Exact 2-control coherent-cube cover, k=3..6, no nonstandard packages.
Science pin 435e77af0d180eac32bd1f9c4c464bc4010b7551.
"""
import json
PIN='435e77af0d180eac32bd1f9c4c464bc4010b7551'
def run(k):
    n=1<<k; tails=1<<(k-2); full=(1<<tails)-1
    q=lambda z:sum(((z>>i)&1)*((z>>((i+1)%k))&1) for i in range(k))
    qq=list(map(q,range(n)))
    def raw(t,a):return (t<<2)|a
    def good(r,u):return (u&~r)==0 and 0<=qq[r]-qq[u]<=2
    patterns=[[sum((1<<t) for t in range(tails) if good(r,raw(t,a))) for r in range(n)] for a in range(4)]
    costs={};labels={};counts={}
    for S_mask in range(4):
        S=tuple(i for i in (0,1) if (S_mask>>i)&1)
        options=[]
        for p in range(1<<len(S)):
            a_set=[a for a in range(4) if sum(((a>>i)&1)<<j for j,i in enumerate(S))==p]
            table={}
            for r in range(n):
                m=full
                for a in a_set:m &=patterns[a][r]
                if m:table.setdefault(m,r)
            options.append(table)
        states={full:()}
        for option in options:
            nxt={}
            for m,rs in states.items():
                for c,r in option.items():
                    if m&c:nxt.setdefault(m&c,rs+(r,))
            states=nxt
        counts[str(S_mask)]=len(states)
        for m,rs in states.items():
            cost=1<<len(S)
            if cost<costs.get(m,100):costs[m]=cost;labels[m]=(S,rs)
    dp=[100]*(full+1);parent=[None]*(full+1);dp[0]=0
    for m in range(full+1):
        if dp[m]>=100:continue
        for c,w in costs.items():
            v=m|c
            if dp[v]>dp[m]+w:dp[v]=dp[m]+w;parent[v]=(m,c)
    value=dp[full];cur=full;components=[]
    while cur:
        previous,mask=parent[cur]; S,centers=labels[mask]
        components.append({'observable_control_indices':S,'source_centers':centers,
                           'tail_bitset':mask,'states':costs[mask]});cur=previous
    assert sum(c['states'] for c in components)==value
    assert all(any(c['tail_bitset']>>t&1 for c in components) for t in range(tails))
    for c in components:
        for t in range(tails):
            if c['tail_bitset']>>t&1:
                for a in range(4):
                    p=sum(((a>>i)&1)<<j for j,i in enumerate(c['observable_control_indices']))
                    assert good(c['source_centers'][p],raw(t,a))
    return {'k':k,'tails':tails,'unique_candidate_bitsets':len(costs),
            'pattern_class_counts':counts,'exact_minimum':value,'witness':components}
if __name__=='__main__':
    out={'status':'PASS_EXACT_R5_TWO_CONTROL_CUBE','science_pin':PIN,
         'scope':'internally cross-commuting and same-coordinate reset-absorbing controllers',
         'method':'complete enumeration of canonical source-center tables and exact subset DP',
         'results':[run(k) for k in range(3,7)]}
    assert [x['exact_minimum'] for x in out['results']]==[3,4,7,11]
    print(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2))
