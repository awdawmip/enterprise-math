#!/usr/bin/env python3
"""No dependency on the Stage236–239 generator: independent exact finite-face audit.
Reads published JSON; recomputes Bellman decisions, supports and all balanced edges.
Completeness is finite for 680 count states and 2**k tie assignments.
"""
import json
from fractions import Fraction as F
from itertools import combinations
from functools import lru_cache
from pathlib import Path

DATA=Path(__file__).with_name('PORTABLE_EXACT_CERT_STAGE236_239.json')
stages=json.loads(DATA.read_text(encoding='utf-8'))
P=[F(3,24),F(1,24),F(20,24)]
STATES=[(n,a,b) for n in range(15) for a in range(n+1) for b in range(n-a+1)]
assert len(STATES)==680
prev_alpha=F(237666670990705,648489579282432)
prev_value=F(647346693246113,81061197410304)
prev_slope=F(-122232,955)
node_total=0
for record in stages:
    stage=record['stage'];lp=F(record['lp']);lq=F(record['lq']);H=F(record['H'])
    @lru_cache(None)
    def cost(state):
        n,a,b=state
        d={'P':lq*F(2**(a+b),3**a),'Q':lp}
        if n<14:d['C']=1+sum(P[j]*cost((n+1,a+(j==0),b+(j==1)))[0] for j in range(3))
        least=min(d.values())
        return least,tuple(k for k,v in d.items() if v==least),d
    assert cost((0,0,0))[0]==H
    actual_ties={s:choices for s in STATES if len((choices:=cost(s)[1]))==2}
    assert all(len(cost(s)[1])<3 for s in STATES)
    assert [(list(s),list(v)) for s,v in actual_ties.items()]==[(list(s),list(v)) for s,v in zip(record['ties'],record['options'])]
    gaps=[a-cost(s)[0] for s in STATES for a in cost(s)[2].values() if a>cost(s)[0]]
    assert len(gaps)==record['strict_gaps'] and min(gaps)==F(record['min_gap'])
    corners={key:tuple(map(F,values)) for key,values in record['corners'].items()}
    assert len(corners)==2**len(actual_ties)
    assert all(c[2]+lp*c[0]+lq*c[1]==H and c[2]>c[3] for c in corners.values())
    assert sum(map(int,record['nodes'].values()))==record['total_nodes']
    node_total+=record['total_nodes']
    best_min=None;best_max=None;cnt=0;distinct=set()
    def process(alpha,t_p,t_q):
        nonlocal_not_possible=0
        assert t_p>t_q
        assert t_p+(lp+lq)*alpha==H
        return alpha,t_p,t_q
    for b,v in corners.items():
        if v[0]==v[1]:
            val=process(v[0],v[2],v[3]);cnt+=1;distinct.add(val[0])
            if best_min is None or val[0]<best_min[0]:best_min=val
            if best_max is None or val[0]>best_max[0]:best_max=val
    for (a,v),(b,w) in combinations(corners.items(),2):
        dv=v[0]-v[1];dw=w[0]-w[1]
        if dv*dw>=0:continue
        wt=-dw/(dv-dw)
        assert F(0)<wt<F(1)
        mixed=[wt*v[i]+(1-wt)*w[i] for i in range(4)]
        assert mixed[0]==mixed[1]
        val=process(mixed[0],mixed[2],mixed[3]);cnt+=1;distinct.add(val[0])
        if best_min is None or val[0]<best_min[0]:best_min=val
        if best_max is None or val[0]>best_max[0]:best_max=val
    assert cnt==record['balanced_vertices']
    assert len(distinct)==record['balanced_distinct_errors']
    for k,best in [('left',best_min),('right',best_max)]:
        witness=record[k]
        assert tuple(map(F,[witness['alpha'],witness['tP'],witness['tQ']]))==best
        weights=list(map(F,witness['weights']))
        assert sum(weights)==1 and all(a>=0 for a in weights)
        v=[sum(weights[j]*corners[bit][i] for j,bit in enumerate(witness['policies'])) for i in range(4)]
        assert v[0]==v[1] and tuple((v[0],v[2],v[3]))==best
    assert best_min[:2]==(prev_alpha,prev_value)
    assert lp+lq < -prev_slope
    assert F(record['slope'])==-(lp+lq)
    assert F(record['delta'])==best_max[0]-best_min[0]>0
    prev_alpha,prev_value,prev_slope=best_max[0],best_max[1],-(lp+lq)
    print(f'STAGE{stage}_INDEPENDENT_RATIONAL_AUDIT_PASS corners={len(corners)} edges={cnt} nodes={record["total_nodes"]}')
print('STAGE236_239_INDEPENDENT_AUDIT_PASS',node_total)
