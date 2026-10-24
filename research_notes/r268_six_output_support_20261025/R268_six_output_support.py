#!/usr/bin/env python3
"""R268 exact positive formal BRC; not a native heartbeat model."""
from collections import Counter, defaultdict
from itertools import product
import json

EDGES = {
    0: ((2,-1,-1),(2,+1,-1)),
    1: ((0,-1,-1),(0,+1,-1)),
    2: ((1,+1,+1),(2,+1,-1)),
}
DELTA = ((1,0),(2,0),(2,2))
OUTPUTS = tuple((q,h) for q in range(3) for h in (0,1))
EXPECTED_MAX = (1,1,1,3,4,4,5,6)
BASE_EFFECTS = {7:(1,-3),8:(1,0),9:(-1,-1)}

def step(s,a):
    q,r,eps,k=s
    t,eta,b=EDGES[q][a]
    return t,DELTA[r][a],eta*eps,eta*k+b

def evaluate(word):
    s=(0,0,1,0)
    for a in word: s=step(s,int(a))
    return s

def forward(p):
    d=Counter()
    for state,mass in p.items():
        for a in (0,1): d[step(state,a)]+=mass
    return d

def by_effect(p):
    ans=defaultdict(Counter)
    for (q,r,eps,k),weight in p.items():
        ans[(eps,k)][(q,int(r==2))]+=weight
    return ans

def main():
    p=Counter({(0,0,1,0):1})
    max_support=[]; base_table={}; brute_tests=0
    for n in range(97):
        assert sum(p.values())==2**n,(n,'mass')
        fibers=by_effect(p)
        max_size=max(len(d) for d in fibers.values())
        if n<=7: max_support.append(max_size)
        if n in BASE_EFFECTS:
            g=BASE_EFFECTS[n]
            counts=[fibers[g].get(c,0) for c in OUTPUTS]
            assert all(v>0 for v in counts),(n,g,counts)
            base_table[str(n)]={'effect':list(g),'counts':counts}
        if 7<=n<=96:
            assert max_size==6,(n,max_size)
        if n<=11:
            direct=Counter()
            samples=defaultdict(dict)
            for bits in product('01',repeat=n):
                word=''.join(bits)
                q,r,eps,k=evaluate(word)
                direct[(q,r,eps,k)]+=1
                g=(eps,k);c=(q,int(r==2))
                samples[g].setdefault(c,word)
                brute_tests+=1
            assert direct==p,(n,'independent word enumeration disagrees')
            if n in BASE_EFFECTS:
                base_table[str(n)]['witnesses']={f'{q},{h}':samples[BASE_EFFECTS[n]][(q,h)] for q,h in OUTPUTS}
        if n<96:p=forward(p)
    assert tuple(max_support)==EXPECTED_MAX,max_support
    assert evaluate('101')==(0,0,1,-1)
    base_samples={int(n):record['witnesses'] for n,record in base_table.items()}
    for n in range(7,220):
        j=7+(n-7)%3; h=(n-j)//3; gj=BASE_EFFECTS[j]
        same=(gj[0],gj[1]-gj[0]*h)
        for c,word in base_samples[j].items():
            q,r,eps,k=evaluate('101'*h+word)
            assert (eps,k)==same and f'{q},{int(r==2)}'==c,(n,c,word)
    result={
        'schema':'EM_R268_SIX_OUTPUT_FIBER_SUPPORT_V1',
        'status':'PASS',
        'mathematical_scope':'formal positive two-branch BRC; terminal (q,contains_00), full affine effect unchanged',
        'start_state':(0,0,1,0),
        'max_distinct_terminal_channels_one_effect_fiber_depths_0_to_7':max_support,
        'first_six_output_depth':7,
        'witnesses_and_exact_counts_for_depths_7_8_9':base_table,
        'total_direct_words_evaluated':brute_tests,
        'positive_dynamic_programming_verified_through_depth':96,
        'prefix_reset_word':'101',
        'prefix_reset_state_and_effect':(0,0,1,-1),
        'universal_witness_construction_checked_through_depth':219,
        'universal_lemma_proven_separately':'m=j+3h, j in {7,8,9}, effect=(eps_j,k_j-eps_j*h)',
        'lower_bound':'Any positive BRC with a single-valued terminal decoder D(state,depth,effect) reproducing all six-output joint histograms has at least six control states',
        'not_proven':['existence or impossibility of six-state unrestricted aggregate representation',
                      'native Enterprise Math package execution',
                      'R193 native provenance/time-port mapping',
                      'formal Result/Driver acceptance']}
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
