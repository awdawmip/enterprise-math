#!/usr/bin/env python3
"""Frozen R5 all 28 individual gap 3->2 closures: exact low-budget cost spectrum.
Standard library only. Integer event boundaries reconstructed from frozen 15 atoms.
"""
from collections import Counter
from fractions import Fraction
from json import dump

W=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)

def original_blocks():
    pools={3:set(),12:set(),15:set()}
    mask=n=k=0
    for step in range(1,1<<15):
        bit=step&-step
        i=bit.bit_length()-1
        mask^=bit
        sign=1 if mask&bit else -1
        n+=sign*W[i]; k+=sign*K0[i]
        assert mask==(step^(step>>1))
        if n>=3 and k%36==0 and k//36 in pools:
            pools[k//36].add(n)
    assert [len(pools[t]) for t in (3,12,15)]==[538,298,229]
    events=Counter(Fraction(p,q) for q,ps in pools.items() for p in ps)
    assert len(events)==953 and Counter(events.values())=={1:869,2:56,3:28}
    x=[0]
    for threshold in sorted(events):x.append(x[-1]+events[threshold])
    assert len(x)==954 and x[-1]==1065
    B=[];start=0
    for t in range(1,len(x)):
        if x[t]-x[t-1]>2:
            assert x[t]-x[t-1]==3
            B.append(tuple(x[start:t]));start=t
    B.append(tuple(x[start:]))
    assert len(B)==29
    return x,B

def cost_frontier(x):
    n=len(x)
    incoming=[[] for _ in x]
    for p in range(n):
        for q in range(p+1,min(n,p+6)):
            vals=[min(x[b]-x[p],x[q]-x[b]) for b in range(p+1,q)]
            if all(v<=2 for v in vals):incoming[q].append((p,sum(vals)))
    row=[None]*n
    for p in range(n):
        if x[p]-x[0]<=2:row[p]=sum(x[p]-x[b] for b in range(p))
    result={}
    for budget in range(1,n+1):
        vals=[cost+sum(x[b]-x[p] for b in range(p+1,n)) for p,cost in enumerate(row) if cost is not None and x[-1]-x[p]<=2]
        if vals:result[budget]=min(vals)
        if budget==n:break
        nxt=[None]*n
        for q,edges in enumerate(incoming):
            vals=[row[p]+w for p,w in edges if row[p] is not None]
            if vals:nxt[q]=min(vals)
        row=nxt
    assert result[len(x)]==0
    return result

def convolution(frontiers,limit=315):
    min_counts=[min(z) for z in frontiers]
    nmin=sum(min_counts)
    assert nmin<=limit
    extra_max=limit-nmin
    dp=[10**9]*(extra_max+1);dp[0]=0
    for front,m in zip(frontiers,min_counts):
        options=[front[m+t] for t in range(min(max(front)-m,extra_max)+1)]
        ndp=[10**9]*(extra_max+1)
        for used,old_cost in enumerate(dp):
            if old_cost>=10**9:continue
            for t,cost in enumerate(options[:extra_max-used+1]):
                v=old_cost+cost
                if v<ndp[used+t]:ndp[used+t]=v
        dp=ndp
    return {nmin+t:cost for t,cost in enumerate(dp) if cost<10**9}

def main():
    x,B=original_blocks()
    F=[cost_frontier(block) for block in B]
    old=convolution(F)
    assert min(old)==213
    assert [old[k] for k in range(213,218)]==[1070,1064,1059,1054,1049]
    changed=[]; min_hist=Counter(); any_changed=Counter(); total_comparisons=0
    for cut in range(28):
        left,right=B[cut],B[cut+1]
        assert right[0]-left[-1]==3
        joined=left+tuple(t-1 for t in right)
        merged=cost_frontier(joined)
        f_new=F[:cut]+[merged]+F[cut+2:]
        cur=convolution(f_new)
        min_hist[min(cur)]+=1
        if min(cur)<min(old):assert min(cur)==212
        decreases={str(k):old[k]-cur[k] for k in range(213,315) if old[k]!=cur[k]}
        assert all(v>0 for v in decreases.values())
        for k in range(213,315):
            assert cur[k]<=old[k]
            total_comparisons+=1
        for k in map(int,decreases):any_changed[k]+=1
        changed.append({'zero_based_cut':cut,'minimum_centers':min(cur),'cost_at_212':cur.get(212),'low_budget_cost_changes':decreases})
    result={'status':'PASS_EXACT_28_GAP_CLOSURES','scientific_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551','original_event_boundaries':len(x),'original_activation_events':x[-1], 'original_blocks':len(B),'original_Kmin':min(old),'single_cut_cases':28,'new_minimum_histogram':dict(sorted(min_hist.items())),'low_budget_comparisons':total_comparisons,'changed_budget_frequency':dict(sorted(any_changed.items())),'per_cut':changed}
    with open('R5_28_CUT_OUTPUT.json','w') as f:dump(result,f,indent=2)
    print('RESULT', {k:v for k,v in result.items() if k!='per_cut'})
    for item in changed:
        if item['cost_at_212'] is not None or item['low_budget_cost_changes']:
            print('CUT',item)
if __name__=='__main__':main()
