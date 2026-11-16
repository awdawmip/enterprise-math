#!/usr/bin/env python3
"""Exact budget/bit-cost sweep for R5's 8,280 three-count decoders.
Requires prior verified sibling source:
../r5_minimum_scalar_queries_20261116/VERIFY_R5_ALL_TRIPLE_DECODERS.py
at pinned source commit 143ada28910f2b0e042d2d0ffcb066fee45d083e.
"""
from itertools import product
from pathlib import Path
import sys, json
sibling=Path(__file__).resolve().parent.parent/'r5_minimum_scalar_queries_20261116'
sys.path.insert(0,str(sibling))
from VERIFY_R5_ALL_TRIPLE_DECODERS import frozen, close, spectrum

x,cuts=frozen()
specs={}
for name,lo,hi,bits in [('A',214,221,[3,8,9,10,27]),('B',223,291,[25,27]),('C',293,314,[15,17])]:
    data=[spectrum(close(x,cuts,bits,m),hi) for m in range(1<<len(bits))]
    specs[name]={k:[d[k][1] for d in data] for k in range(lo,hi+1)}
A,B,C=(specs[n] for n in 'ABC')
valid_A=list(range(214,220));valid_B=list(range(223,292));valid_C=list(range(294,314))
assert all(len(set(A[k]))==32 for k in valid_A)
assert all(len(set(B[k]))==4 for k in valid_B)
assert all(len(set(C[k]))==4 for k in valid_C)
assert A[220][9]==A[220][12]==38336726601491749449844654080000
assert C[293][1]==C[293][2]==13102659259476980304288153600
proj=[((v&15)|((v>>7&1)<<4),(v>>6)&3,(v>>4)&3) for v in range(256)]
pointwise={}
for name,table,budgets,k0 in [('A',A,range(214,222),214),('B',B,valid_B,291),('C',C,valid_C,294)]:
    failures=[(k,m) for k in budgets for m in range(len(table[k0]))
              if table[k][m].bit_length()<table[k0][m].bit_length()]
    assert not failures,(name,failures[:5])
    pointwise[name]={'dominating_budget':k0,'tested_budgets':len(budgets),'tested_masks':len(table[k0])}

stats={}
for a,b,c in product(valid_A,valid_B,valid_C):
    ia=[v.bit_length() for v in A[a]]
    ib=[v.bit_length() for v in B[b]]
    ic=[v.bit_length() for v in C[c]]
    assert len({(A[a][i],B[b][j],C[c][k]) for i,j,k in proj})==256
    totals=[ia[i]+ib[j]+ic[k] for i,j,k in proj]
    stats[a,b,c]=(max(totals),sum(totals),max(map(max,(ia,ib,ic))),a+b+c)
assert len(stats)==8280
order={
    'budget_sum':(3,0,1,2),
    'worst_total_bits':(0,1,3,2),
    'mean_total_bits':(1,0,3,2),
    'max_single_bits':(2,0,1,3)
}
best={}
for metric,indices in order.items():
    triple,t=min(stats.items(),key=lambda v:(tuple(v[1][i] for i in indices),v[0]))
    best[metric]={'budgets':list(triple),'worst_total_bits':t[0],
        'mean_total_bits_num':t[1],'mean_total_bits_den':256,
        'max_single_bits':t[2],'budget_sum':t[3]}
by_worst={}
for triple,t in stats.items():
    w=t[0]
    if w not in by_worst or (t[3],triple)<(by_worst[w][1],by_worst[w][0]):by_worst[w]=(triple,t[3])
frontier=[];last=10**10
for w in sorted(by_worst):
    triple,total=by_worst[w]
    if total<last:
        frontier.append({'worst_bits':w,'budget_sum':total,'budgets':list(triple)})
        last=total
result={'status':'PASS_R5_DECODER_COST_EXACT','input_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
    'source_commit':'143ada28910f2b0e042d2d0ffcb066fee45d083e',
    'domain':{'events':954,'gap_cuts':28,'quotient_signatures':256,'valid_triples':8280},
    'bit_metric':'Positive count N.bit_length; three raw integers; budget cost=sum K; uniform 256 signatures',
    'pointwise':pointwise,'baseline':{'budgets':[214,223,294], 'metrics':stats[214,223,294]},
    'best':best,'pareto_worst_bits_vs_budget_sum':frontier}
print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))
