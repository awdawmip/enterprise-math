#!/usr/bin/env python3
"""R5 K=220,221: deterministic changed-edge witnesses, exact old-optimal recourse.
Place alongside prior VERIFY_R5_LOW_BUDGET_UNIT_RECOURSE.py; Python stdlib only.
"""
import json
import random
from VERIFY_R5_LOW_BUDGET_UNIT_RECOURSE import frozen,close,graph,paths_dp,INF

FROZEN='435e77af0d180eac32bd1f9c4c464bc4010b7551'


def select_path(dp, inc, out, K, layer, before, after, rng):
    C,D,J=dp[1:]
    seq=[after];j=before
    for r in range(layer-1,-1,-1):
        seq.append(j)
        if r:
            prior=[i for i,w in inc[j] if C[r-1][i]+w==C[r][j]]
            assert prior
            j=rng.choice(prior)
    j=after
    for remain in range(K-1-layer,0,-1):
        nxt=[q for q,w in out[j] if w+D[remain-1][q]==D[remain][j]]
        assert nxt
        j=rng.choice(nxt)
        seq.append(j)
    seq.sort()
    assert len(seq)==K and len(set(seq))==K
    return seq


def nearest_old(S, oldgraph, olddp, K):
    inc,out,pref,tail=oldgraph
    _,C,D,J=olddp
    best=J[K-1]; chosen=set(S);n=len(C[0]); M=[-1]*n
    for j in range(n):
        if pref[j]<INF and pref[j]+D[K-1][j]==best:
            M[j]=int(j in chosen)
    for t in range(1,K):
        new=[-1]*n
        for j in range(n):
            if C[t][j]+D[K-1-t][j]!=best:continue
            score=max((M[i] for i,w in inc[j] if M[i]>=0 and C[t-1][i]+w==C[t][j]),default=-1)
            if score>=0:new[j]=score+int(j in chosen)
        M=new
    return K-max(M[j] for j in range(n) if M[j]>=0 and C[K-1][j]+tail[j]==best)


def cover_cost(z,S):
    d=[min(abs(z[t]-z[j]) for j in S) for t in range(len(z))]
    return max(d),sum(d)


def main():
    x,cuts=frozen()
    og=graph(x);od=paths_dp(x,221)
    old_edges={(i,j) for j,rr in enumerate(og[0]) for i,w in rr}
    rows=[]
    for bit in (3,8,9,10):
        y=close(x,cuts,1<<bit);ng=graph(y);nd=paths_dp(y,221)
        inc,out,pref,tail=ng;_,C,D,J=nd
        added=[(i,j,w) for j,row in enumerate(inc) for i,w in row if (i,j) not in old_edges]
        for K in (220,221):
            assert J[K-1]==od[-1][K-1]
            edges=[(layer,i,j) for i,j,w in added for layer in range(1,K)
                   if C[layer-1][i]+w==C[layer][j] and C[layer][j]+D[K-1-layer][j]==J[K-1]]
            assert edges
            chosen=None
            for idx,(layer,i,j) in enumerate(edges[:8]):
                S=select_path(nd,inc,out,K,layer,i,j,random.Random(20261115+idx))
                r=nearest_old(S,og,od,K)
                if chosen is None or r>chosen[0]:chosen=(r,S,(layer,i,j),idx)
            r,S,edge,idx=chosen
            assert cover_cost(y,S)==(2,J[K-1])
            assert cover_cost(x,S)[0]>2
            rows.append({'K':K,'cut':bit,'cut_event_index':cuts[bit],'J':J[K-1],
              'new_optimal_old_infeasible_edge_count':len(edges),
              'exact_min_swaps_for_constructed_S':r,'chosen_edge_layer_i_j':edge,
              'edge_iteration_index':idx,'new_optimal_center_indices':S})
    print(json.dumps({'status':'PASS_EXACT_R5_FORBIDDEN_EDGE_K220_221',
      'scientific_input_commit':FROZEN,'result_kind':'exact witness-specific min old, lower bound max-new-min-old',
      'rows':rows,'math_review':'NOT_REVIEWED'},indent=2,sort_keys=True))


if __name__=='__main__':main()
