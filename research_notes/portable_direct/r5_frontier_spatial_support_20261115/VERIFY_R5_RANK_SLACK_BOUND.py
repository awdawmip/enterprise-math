#!/usr/bin/env python3
"""Feasible anchored-budget slack bound on optimizer frontier rank multiplicity.
Uses frozen R5 radius2 observer; checks all effective masks and K214..221.
"""
import json
from VERIFY_R5_FRONTIER_SPATIAL_SUPPORT import frozen,close,BITS
from VERIFY_R5_OPTIMAL_FRONTIER_RANK_AUDIT import costs
INF=10**14

def minima(z,out):
    n=len(z);a=[INF]*n;b=[INF]*n
    for i in range(n):
        if z[i]-z[0]<=2:a[i]=0
        for j,w in out[i]:
            if a[i]<INF:a[j]=min(a[j],a[i]+1)
    for i in range(n-1,-1,-1):
        if z[-1]-z[i]<=2:b[i]=0
        for j,w in out[i]:
            if b[j]<INF:b[i]=min(b[i],b[j]+1)
    return a,b

def inspect(z,dp,K,a,b):
    out,C,D,J=dp;n=len(z);obj=J[K-1]
    L=[{i for i in range(n) if C[r][i]+D[K-1-r][i]==obj} for r in range(K)]
    tails={}
    for r in range(K-1):
        for i in L[r]:
            if any(q in L[r+1] and C[r][i]+w==C[r+1][q] for q,w in out[i]):
                tails.setdefault(i,set()).add(r)
    assert tails
    violations=[];best_slack=-1;best_rankdiv=0;min_deficit=None
    for i,rs in tails.items():
        assert a[i]<INF and b[i]<INF,(i,K)
        slack=K-1-a[i]-b[i]
        if not all(a[i]<=r<=K-1-b[i] for r in rs):
            violations.append((i,sorted(rs),a[i],b[i]))
        assert len(rs)<=slack+1
        best_slack=max(best_slack,slack)
        best_rankdiv=max(best_rankdiv,len(rs))
        diff=(slack+1)-len(rs)
        min_deficit=diff if min_deficit is None else min(min_deficit,diff)
    assert not violations,violations
    return dict(K=K,max_slack=best_slack,max_rank_diversity=best_rankdiv,
                most_rank_diverse_tail_count=sum(len(rs)==best_rankdiv for rs in tails.values()),
                max_slack_rank_bound=best_slack+1,
                tail_indices=len(tails),smallest_rank_gap_from_feasible_budget_bound=min_deficit)

def main():
    x,cuts=frozen();rows=[]
    for mask in range(32):
        z=close(x,cuts,[bit for j,bit in enumerate(BITS) if mask>>j&1]);dp=costs(z)
        a,b=minima(z,dp[0])
        for K in range(214,222):
            row=inspect(z,dp,K,a,b);row['mask']=mask
            rows.append(row)
    print(json.dumps(dict(status='PASS_R5_FEASIBLE_RANK_SLACK_BOUND',
             frozen_scientific_input='435e77af0d180eac32bd1f9c4c464bc4010b7551',
             budgets=[214,221],masks=32,instances=len(rows),
             largest_feasible_budget_slack=max(r['max_slack'] for r in rows),
             largest_observed_optimizer_rank_diversity=max(r['max_rank_diversity'] for r in rows),
             rows=rows),indent=2,sort_keys=True))
if __name__=='__main__':main()
