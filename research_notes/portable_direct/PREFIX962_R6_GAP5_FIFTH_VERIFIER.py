#!/usr/bin/env python3
"""Exact m=5 candidate-domain identity and original XOR source regression."""
from collections import Counter
from pathlib import Path
import json
PIN='f42f2906d77f24085c123f3ccfe9667d41caa96d'

def candidate(p,a,b):
    H=1<<(p-1)
    return 2*(a-H)-5*(b-H)>=1

def closed_count(p):
    N=1<<(p-2)
    return (N*N - (1 if p%2==0 else -1))//5

def original(p,k,a,b):
    x=k*a; out=[]
    for j in range(p):
        v=x^(1<<j)
        for i in range(p):
            z=v-(1<<i)
            if z>0 and z%b==0:out.append((z//b,i,j))
    return out

def verify(p):
    H=1<<(p-1); Q=range(H+1,2*H,2)
    eligible={(a,b) for a in Q for b in Q if candidate(p,a,b)}
    assert len(eligible)==closed_count(p)
    c=Counter(); example=None
    for k in range(1,H-2,2):
        for a in Q:
            for b in Q:
                if a==b:continue
                w=original(p,k,a,b)
                if not w:continue
                W=original(p,k+2,a,b)
                for t,i,j in w:
                    for T,I,J in W:
                        if T-t!=5:continue
                        assert (a,b) in eligible
                        c1=(1<<i)-(1-2*((k*a>>j)&1))*(1<<j)
                        c2=(1<<I)-(1-2*(((k+2)*a>>J)&1))*(1<<J)
                        assert c2-c1==2*a-5*b
                        assert (bool((i==0) != (j==0))) != (bool((I==0) != (J==0)))
                        c['named_gap5']+=1
                        if example is None:example=[p,k,a,b,t,T,i,j,I,J]
    return {'p':p,'candidate_pairs':len(eligible),'full_pair_domain':len(Q)**2,
            'core_count':len(range(1,H-2,2)), 'counts':dict(c),'example':example}

if __name__=='__main__':
    res=[verify(p) for p in range(4,9)]
    N=1<<17
    out={'frozen_scientific_pin':PIN,'status':'AUTHOR_PROOF_PLUS_FINITE_ORIGINAL_EQUATION_CHECK;NOT_REVIEWED',
         'claim':'For m=5, candidate domain 2v-5u>=1 has exactly (N^2-(-1)^p)/5 odd ordered pairs, N=2^(p-2); named residual parity opposite.',
         'verification':'p=4..8 full Qp^2 and odd k,k+2<H, all source indices and quotients directly from XOR',
         'per_width':res,'Q19_candidate_count':closed_count(19),'Q19_total_ordered_pairs':N*N}
    path=Path(__file__).with_name('PREFIX962_R6_EXACT_RESULTS.json')
    path.write_text(json.dumps(out,sort_keys=True,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'count_by_width':[(r['p'],r['candidate_pairs'],r['counts'].get('named_gap5',0)) for r in res],
         'Q19_candidate_count':closed_count(19)},ensure_ascii=False))
