#!/usr/bin/env python3
"""EC49FOD: exhaustive native BRC 18-demand future-cost lattices.
Needs unchanged master_and_radius3_cases.txt and VERIFY_EC49FNY_INDEPENDENT.py
from the EC49FOC evidence package in the same directory.
"""
import hashlib, json, struct
from pathlib import Path
import VERIFY_EC49FNY_INDEPENDENT as native

ROOTS = (3,5,6,7)
CASES = (32264,32274,32279,32315,32318)
MASKS = (0,5,138,8192)
B = 155
MASTER_SHA = "cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"
FROZEN = "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
INF = 10**9

def lattice(words,keys,case):
    profiles={r:native.table(words,keys,r) for r in ROOTS}
    used=0
    for j,mask in enumerate(MASKS):
        assert not used & mask
        used |= mask
        for i in range(24):
            if mask>>i&1: assert i in profiles[ROOTS[j]][1]
    U=tuple(i for i in range(24) if not used>>i&1)
    assert len(U)==18
    n=len(U); N=1<<n
    dp=[INF]*N; dp[0]=0
    for j,r in enumerate(ROOTS):
        labels,indices,cost,_=profiles[r]
        source_bits=[(1<<indices[i]) if i in indices else 0 for i in U]
        eligible=sum(1<<i for i,b in enumerate(source_bits) if b)
        base=0
        for i in range(24):
            if MASKS[j]>>i&1: base |= 1<<indices[i]
        mapped=[0]*N
        cover=[INF]*N
        cover[0]=cost[base]
        for subset in range(1,N):
            low=subset&-subset; i=low.bit_length()-1
            mapped[subset]=mapped[subset^low] | source_bits[i]
            if subset & ~eligible == 0:
                cover[subset]=cost[base|mapped[subset]]
        nxt=[INF]*N
        for subset in range(N):
            sub=subset&eligible
            while True:
                v=dp[subset^sub]+cover[sub]
                if v<nxt[subset]: nxt[subset]=v
                if sub==0: break
                sub=(sub-1)&(subset&eligible)
        dp=nxt
    assert all(v<INF for v in dp)
    H=[max(dp[s] for s in range(N) if s.bit_count()==h) for h in range(n+1)]
    strict=[sum(dp[s]>B for s in range(N) if s.bit_count()==h) for h in range(n+1)]
    minimal=[s for s in range(1,N) if dp[s]>B and
             all(dp[s^(1<<i)]<=B for i in range(n) if s>>i&1)]
    digest=hashlib.sha256(b''.join(struct.pack('<I',v) for v in dp)).hexdigest()
    record={'case':case,'fixed_masks':MASKS,'future':U,'B':B,
            'H0_to_H18':H,'strict_by_cardinality':strict,
            'inclusion_minimal_cores':[[U[i] for i in range(n) if s>>i&1] for s in minimal],
            'h_star':min((s.bit_count() for s in minimal),default=None),
            'full_cost':dp[-1],
            'one_deletion_costs':{str(U[i]):dp[(N-1)^(1<<i)] for i in range(n)},
            'future_legal_roots':{str(i):[r for r in ROOTS if i in profiles[r][1]] for i in U},
            'cost_lattice_sha256_le_uint32':digest,'subset_count':N}
    print('CASE',case,'h*',record['h_star'],'full',dp[-1],
          'minimal',len(minimal),'strict',sum(strict),flush=True)
    return record,dp

def main():
    src=Path('master_and_radius3_cases.txt')
    assert hashlib.sha256(src.read_bytes()).hexdigest()==MASTER_SHA
    records=[];vectors={}
    for case in CASES:
        words,keys=native.frozen(src,case=case)
        record,dp=lattice(words,keys,case)
        records.append(record);vectors[case]=dp
    assert records[2]['H0_to_H18'][1:]==[
        59,75,89,102,113,118,126,131,134,137,140,143,146,149,151,153,155,156]
    assert len(records[2]['inclusion_minimal_cores'])==1
    assert vectors[32264]==vectors[32315]
    U=records[2]['future'];comparisons=[]
    for a,b in ((32264,32315),(32279,32315),(32315,32318)):
        diffs=[s for s,(x,y) in enumerate(zip(vectors[a],vectors[b])) if x!=y]
        s=diffs[0] if diffs else None
        comparisons.append({'a':a,'b':b,'exact_equal_all_262144':not diffs,
          'different_subset_count':len(diffs),
          'first_different_subset':None if s is None else
              [U[i] for i in range(len(U)) if s>>i&1],
          'cost_a':None if s is None else vectors[a][s],
          'cost_b':None if s is None else vectors[b][s]})
    assert comparisons[1]['different_subset_count']==211351
    assert comparisons[2]['different_subset_count']==22154
    out={'frozen_scientific_input_pin':FROZEN,'master_sha256':MASTER_SHA,
         'method':'exact min-plus rooted subset partition DP',
         'cross_case_comparisons':comparisons,'cases':records}
    Path('EC49FOD_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
    print('EC49FOD_PASS cases=5 subsets=1310720 h*=17,17,18,17,17')
if __name__=='__main__':main()
