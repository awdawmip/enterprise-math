#!/usr/bin/env python3
"""Exact finite adversarial online path-coupling upper certificates for frozen R5.
The old player sees each new center before selecting its rank-matched center.
This stronger-online game's value bounds the offline set-recourse from above.
All computed quantities use Python unbounded integers. No native X6 identification.
"""
import json
from VERIFY_R5_LOW_BUDGET_UNIT_RECOURSE import frozen,close,graph,paths_dp
PIN='435e77af0d180eac32bd1f9c4c464bc4010b7551'
BITS=(3,8,9,10,27)
ANCHORS=(6,11,16,536,541,546)

def opt_dp(z,max_k=221):
    inc,out,pref,tail=graph(z)
    out2,C,D,J=paths_dp(z,max_k)
    assert out==out2
    return inc,out,pref,tail,C,D,J

def language(dp,K):
    inc,out,pref,tail,C,D,J=dp;best=J[K-1]
    levels=[{j for j in range(len(pref)) if C[t][j]+D[K-1-t][j]==best}
            for t in range(K)]
    assert levels[0] and levels[-1]
    nexts=[]
    for t in range(K-1):
        nex={i:tuple(j for j,w in out[i] if j in levels[t+1]
                            and C[t][i]+w==C[t+1][j]) for i in levels[t]}
        assert all(nex.values())
        nexts.append(nex)
    return levels,nexts

def online_rank_bound(old,new,K):
    # Max (new choices), min (old choices after seeing each new move).
    # Rank mismatch is >= set difference, hence this value is an upper bound.
    O,OE=language(old,K);N,NE=language(new,K)
    V={(a,b):int(a!=b) for a in N[-1] for b in O[-1]}
    for t in range(K-2,-1,-1):
        V={(a,b):int(a!=b)+max(min(V[aa,bb] for bb in OE[t][b])
                                  for aa in NE[t][a])
           for a in N[t] for b in O[t]}
    return max(min(V[a,b] for b in O[0]) for a in N[0])

def main():
    x,cuts=frozen()
    dp={}
    for mask in range(32):
        mask28=sum(1<<bit for k,bit in enumerate(BITS) if mask>>k&1)
        dp[mask]=opt_dp(close(x,cuts,mask28))
    rows=[];anchor_checks=0;checks=0
    for K in range(214,222):
        ref={6:1,11:2,16:3,536:K-85,541:K-84,546:K-83}
        for mask in range(32):
            M=dp[mask]
            for j,rank in ref.items():
                # Membership on a global optimum path in the exact layer.
                assert M[4][rank][j]+M[5][K-1-rank][j]==M[6][K-1]
                assert sum(M[4][rank][q]+M[5][K-1-rank][q]==M[6][K-1]
                           for q in range(len(x)))==1
                assert all(M[4][r][j]+M[5][K-1-r][j]!=M[6][K-1]
                           for r in range(K) if r!=rank)
                anchor_checks+=1
        for bit in (3,10):
            p=BITS.index(bit);vals=[]
            for newmask in range(32):
                if not newmask>>p&1:continue
                oldmask=newmask^(1<<p)
                assert dp[oldmask][6][K-1]==dp[newmask][6][K-1]
                U=online_rank_bound(dp[oldmask],dp[newmask],K)
                vals.append({'new_five_bit_mask':newmask,'old_five_bit_mask':oldmask,
                             'online_rank_mismatch_upper':U})
                checks+=1
            bound=max(v['online_rank_mismatch_upper'] for v in vals)
            assert bound==(3 if bit==3 else 4),(K,bit,bound)
            rows.append({'K':K,'cut':bit,'max_upper_all_backgrounds':bound,
                         'min_upper_all_backgrounds':min(v['online_rank_mismatch_upper'] for v in vals),
                         'backgrounds':vals})
    print(json.dumps({'status':'PASS_R5_ALL_BACKGROUND_ONLINE_COUPLING',
                      'scientific_input_commit':PIN,
                      'observer':'derived 954-event integer radius-two indexed-center',
                      'effective_bits':BITS,
                      'coverage':'all 32 five-bit closure masks; K214-221; changed cuts 3 and 10',
                      'anchor_event_indices':ANCHORS,
                      'universal_anchor_layer_formula':{'6':'1','11':'2','16':'3',
                                                        '536':'K-85','541':'K-84','546':'K-83'},
                      'anchor_membership_and_unique_layer_checks':anchor_checks,
                      'online_rank_coupling_checks':checks,
                      'rows':rows,'independent_math_review':'NOT_REVIEWED'},
                     sort_keys=True,indent=2))
if __name__=='__main__':main()
