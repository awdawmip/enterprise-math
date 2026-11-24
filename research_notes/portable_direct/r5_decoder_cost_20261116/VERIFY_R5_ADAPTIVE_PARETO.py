#!/usr/bin/env python3
"""Exact adaptive 3-query budget/readout-bit Pareto frontier for frozen R5 observer.
Dependency: ../r5_minimum_scalar_queries_20261116/VERIFY_R5_ALL_TRIPLE_DECODERS.py
scientific pin 435e77af0d180eac32bd1f9c4c464bc4010b7551.
"""
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'r5_minimum_scalar_queries_20261116'))
from VERIFY_R5_ALL_TRIPLE_DECODERS import frozen,close,spectrum
x,cuts=frozen()
sp={}
for n,lo,hi,bits in [('A',214,221,[3,8,9,10,27]),('B',223,291,[25,27]),('C',293,314,[15,17])]:
    d=[spectrum(close(x,cuts,bits,m),hi) for m in range(1<<len(bits))]
    sp[n]={k:[v[k][1] for v in d] for k in range(lo,hi+1)}
A,B,C=(sp[n] for n in 'ABC')
assert len(set(A[214]))==32
assert all(len(set(B[k]))==4 for k in range(223,292))
assert len(set(C[294]))==4
assert all(A[214][a].bit_length()<=A[k][a].bit_length() for k in range(214,222) for a in range(32))
assert all(C[294][c].bit_length()<=C[k][c].bit_length() for k in range(294,314) for c in range(4))
Amax={r:max(A[214][a].bit_length() for a in range(32) if a>>4==r) for r in (0,1)}
Cmax=max(v.bit_length() for v in C[294])
rows=[]
for cap in range(731,800):
    ub=min(291,cap-508)
    choice={}
    for bit27 in (0,1):
        bs=(2*bit27,2*bit27+1)
        worst_b,k=min((max(B[k][b].bit_length() for b in bs),k) for k in range(223,ub+1))
        choice[bit27]={'B_budget':k,'worst_B_bits':worst_b}
    worst=max(Amax[r]+choice[r]['worst_B_bits'] for r in (0,1))+Cmax
    fixed=[(max(A[214][a].bit_length()+B[k][(a>>4)*2+p].bit_length()+C[294][c].bit_length()
                for a in range(32) for p in (0,1) for c in range(4)),k) for k in range(223,ub+1)]
    n_worst,n_best=min(fixed)
    assert worst<=n_worst
    rows.append({'budget_cap':cap,'best_adaptive_worst_bits':worst,'optimal_B_by_27':choice,
                 'best_fixed_worst_bits':n_worst,'best_fixed_B':n_best})
frontier=[];prev=10**10
for r in rows:
    if r['best_adaptive_worst_bits']<prev:
        frontier.append(r)
        prev=r['best_adaptive_worst_bits']
res={'status':'PASS_R5_ADAPTIVE_COST_FRONTIER_EXACT',
     'pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
     'Amax_by_27':Amax,'Cmax':Cmax,'budget_cap_domain':[731,799],
     'adaptive_frontier':frontier,
     'worst_adaptive_vs_fixed_gap_max':max(r['best_fixed_worst_bits']-r['best_adaptive_worst_bits'] for r in rows),
     'adaptive_better_caps':[r for r in rows if r['best_adaptive_worst_bits']<r['best_fixed_worst_bits']],
     'last':rows[-1]}
print(json.dumps(res,sort_keys=True,indent=2))
