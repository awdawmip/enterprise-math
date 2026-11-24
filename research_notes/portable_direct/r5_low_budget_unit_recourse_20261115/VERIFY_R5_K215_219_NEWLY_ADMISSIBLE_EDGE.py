#!/usr/bin/env python3
"""Frozen R5: K=215..219 exact recourse lower-bound witnesses.
Run next to VERIFY_R5_LOW_BUDGET_UNIT_RECOURSE.py and VERIFY_R5_K220_221_FORCED_EDGE.py.
The max over sampled new paths is exploratory; min over every old optimum is exact.
"""
import json
import random
from VERIFY_R5_LOW_BUDGET_UNIT_RECOURSE import frozen, close, graph, paths_dp, INF
from VERIFY_R5_K220_221_FORCED_EDGE import select_path, nearest_old, cover_cost
PIN='435e77af0d180eac32bd1f9c4c464bc4010b7551'
SEED=202611150318
TRIALS=48
EXPECTED={3:[3,3,3,3,3],8:[6,6,5,5,5],9:[6,6,5,5,5],10:[4,4,4,4,4]}

def lex_old_best(oldgraph, S, K):
    """Independent direct lexicographic min-cost/max-shared-center DP."""
    inc,_,pref,tail=oldgraph
    present=set(S)
    state=[(pref[j],-int(j in present)) if pref[j]<INF else (INF,0)
           for j in range(len(pref))]
    for _ in range(1,K):
        nxt=[]
        for j in range(len(pref)):
            nxt.append(min(((state[i][0]+w,state[i][1]-int(j in present))
                            for i,w in inc[j] if state[i][0]<INF),default=(INF,0)))
        state=nxt
    opt=min((v+tail[j],neg) for j,(v,neg) in enumerate(state) if tail[j]<INF)
    return opt[0],-opt[1]

def main():
    x,cuts=frozen()
    og=graph(x);od=paths_dp(x,219)
    oe={(i,j) for j,row in enumerate(og[0]) for i,w in row}
    rows=[]
    for bit in (3,8,9,10):
        y=close(x,cuts,1<<bit)
        ng=graph(y);nd=paths_dp(y,219)
        inc,out,pref,tail=ng;_,C,D,J=nd
        extra=[(i,j,w) for j,row in enumerate(inc) for i,w in row if (i,j) not in oe]
        assert extra
        for K in range(215,220):
            assert J[K-1]==od[-1][K-1]==2134-5*K
            edges=[(layer,i,j) for i,j,w in extra for layer in range(1,K)
                   if C[layer-1][i]+w==C[layer][j] and
                      C[layer][j]+D[K-1-layer][j]==J[K-1]]
            assert edges
            hist={}; winner=(-1,None,None)
            for edge_idx,(layer,i,j) in enumerate(edges):
                for trial in range(TRIALS):
                    seed=SEED+1000000*bit+10000*K+500*edge_idx+trial
                    S=select_path(nd,inc,out,K,layer,i,j,random.Random(seed))
                    distance=nearest_old(S,og,od,K)
                    hist[str(distance)]=hist.get(str(distance),0)+1
                    if distance>winner[0]: winner=(distance,S,[layer,i,j])
            distance,S,edge=winner
            assert cover_cost(y,S)==(2,J[K-1])
            assert cover_cost(x,S)[0]>2
            cost,overlap=lex_old_best(og,S,K)
            assert cost==J[K-1] and K-overlap==distance
            rows.append({'K':K,'cut':bit,'new_optimum_cost':J[K-1],
                'newly_admissible_optimal_edge_states':len(edges),
                'samples_per_edge':TRIALS,'histogram':hist,
                'exact_nearest_old_swaps':distance,
                'nearest_old_maximum_overlap':overlap,
                'edge_layer_start_end':edge,'new_optimal_centers':S})
    assert all([r['exact_nearest_old_swaps'] for r in rows if r['cut']==bit]==vals
               for bit,vals in EXPECTED.items())
    print(json.dumps({'status':'PASS_R5_K215_219_FORCED_EDGE_LEX_VERIFIED',
          'science_pin':PIN,'scope':'K=215..219, singleton cuts 3,8,9,10, initial all-open',
          'max_over_all_new_optima_exhausted':False,'min_over_all_old_optima_exact':True,
          'seed':SEED,'trials_per_new_optimal_edge':TRIALS,'rows':rows,
          'independent_math_review':'NOT_REVIEWED'},sort_keys=True,indent=2))

if __name__=='__main__':main()
