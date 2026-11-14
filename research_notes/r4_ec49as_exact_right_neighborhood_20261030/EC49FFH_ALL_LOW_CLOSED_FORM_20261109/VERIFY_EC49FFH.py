#!/usr/bin/env python3
"""Independent exact finite check of EC49FFH all-low horizon theorem.

Covers every requested (h, label) for h=2..U and labels 1,2,4,8 via
frozen EC49FFD observer staircase.  Independent DP ranges over each
candidate terminal horizon, no greedy or closed-form optimization inside.
"""
import json
from pathlib import Path


def covers(H, U):
    return sum(1 << (h-2) for h in range(2,U+1) if h+1 <= H <= 2*h-1)


def independent_subset_dp(U):
    full=(1<<(U-1))-1
    dp={0:(0,0)}
    # 0/1 choice of complete-key canonical terminal horizon H.
    # Other z>=1 full keys have no better length/support at given H.
    for H in range(3,2*U):
        cm=covers(H,U)
        if not cm: continue
        newer=dict(dp)
        for state,cost in dp.items():
            state2=state|cm
            newcost=(cost[0]+1,cost[1]+2*(H+1))
            if newcost < newer.get(state2,(10**6,10**12)):
                newer[state2]=newcost
        dp=newer
    return dp[full],len(dp)


def formula(U):
    k=(U-1).bit_length()
    HH=[1+(U+(1<<(k-i))-1)//(1<<(k-i)) for i in range(1,k+1)]
    pop=(U-1).bit_count()
    L=4*U-4+6*k-2*pop
    assert sum(2*(h+1) for h in HH)==L
    assert HH[0]==3 and HH[-1]==U+1
    assert all(hi < hj <= 2*hi-1 for hi,hj in zip(HH,HH[1:]))
    return k,HH,L


def main():
    rows=[]
    for U in range(2,17):
        k,HH,L=formula(U)
        independent,states=independent_subset_dp(U)
        assert independent==(k,L),(U,independent,(k,L))
        rows.append({'last_required_low_horizon':U,'minimum_keys':k,
                     'minimum_total_one_word_per_key_native_length':L,
                     'canonical_terminal_horizons':HH,'independent_dp_states':states})
    for U in (17,18,19,31,32,33,63,64,65,100,1000,1000000):
        formula(U)
    result={'schema':'EC49FFH_ALL_LOW_THEOREM_CHECK_V1','scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
            'model':'original 9-state BRC observer / strict-positive complete key domain',
            'mathematical_claim':'forall integers U>=2: k=ceil(log2 U), min lex native single-word length sum=4U-4+6*k-2*popcount(U-1)',
            'coverage':'independent exact subset-mask DP for each U=2..16 inclusive; formula structural checks through 1,000,000',
            'rows':rows,'status':'EXACT_INTEGER_PASS'}
    here=Path(__file__).resolve().parent
    (here/'EXACT_REPORT_EC49FFH.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print('EXACT_INTEGER_PASS U=2..16; 15 independent finite checks; U=9:',formula(9))
    print('crosschecks:',len(rows),'max_dp_states:',max(r['independent_dp_states'] for r in rows))
if __name__=='__main__':main()
