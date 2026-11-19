#!/usr/bin/env python3
"""Exact R5 auxiliary model budget-spectrum verification. No native Bellman or BRC execution."""
from collections import deque
import json
from pathlib import Path

def safe_budget(transitions,costs,labels,source,alternatives,budget):
    assert budget>=0
    acts=tuple(transitions)
    assert all(all(c>=0 for c in costs[a].values()) for a in acts)
    ys=tuple((y,0) if labels[source]<=labels[y] else None for y in alternatives)
    init=(source,0,ys)
    q=deque([(init,())])
    visited={init}
    while q:
        (x,cx,cur),word=q.popleft()
        if all(t is None for t in cur):
            return False,''.join(word)
        for a in acts:
            nx=transitions[a][x]
            nc=cx+costs[a][x]
            if nc>budget:
                continue
            others=[]
            for t in cur:
                if t is None:
                    others.append(None)
                    continue
                y,cy=t
                ny=transitions[a][y]
                nyc=cy+costs[a][y]
                others.append((ny,nyc) if nyc<=budget and labels[nx]<=labels[ny] else None)
            after=(nx,nc,tuple(others))
            if after not in visited:
                visited.add(after)
                q.append((after,word+(a,)))
    return True,None

def family(q,d):
    names=('x','y','z')
    return dict(transitions={'a':{'x':'x','y':'z','z':'z'}},
                costs={'a':{'x':q,'y':q+d,'z':q}},
                labels={v:frozenset({'named-port-A'}) for v in names},
                source='x',alternatives=('y',))

def expected(q,d,b):
    return b<q or b%q>=d

def main():
    tests=0
    for q in range(2,10):
        for d in range(1,q):
            m=family(q,d)
            for b in range(6*q+3):
                ok,w=safe_budget(**m,budget=b)
                assert ok==expected(q,d,b),(q,d,b,w)
                if not ok:
                    assert w=='a'*(b//q),(q,d,b,w)
                tests+=1
    old=dict(transitions={'a':{0:0,1:0,2:0},'b':{0:0,1:2,2:0}},
             costs={'a':{0:0,1:0,2:0},'b':{0:0,1:1,2:1}},
             labels={i:frozenset({'named-port-A'}) for i in (0,1,2)},
             source=2,alternatives=(1,))
    regression=[safe_budget(**old,budget=b)[0] for b in range(4)]
    assert regression==[True,False,True,True],regression
    spectrum=[safe_budget(**family(2,1),budget=b)[0] for b in range(33)]
    assert spectrum==[b<2 or b%2==1 for b in range(33)]
    result={'schema':'R5_BUDGET_SPECTRUM_EXACT_V1',
            'model':'finite deterministic positive-label prefix observer',
            'family_count':36,'budget_checks':tests,'range_q':[2,9],
            'd':'1..q-1','range_b':'0..6q+2',
            'parity_budget_0_to_32':spectrum,
            'previous_BCPT3_regression_b_0_to_3':regression,
            'result':'PASS',
            'scope':'finite check only; infinite claims proved symbolically in RESEARCH.md'}
    Path(__file__).with_name('RESULT_BUDGET_SPECTRUM.json').write_text(
        json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('PASS_R5_BUDGET_SPECTRUM',36,tests,regression)

if __name__=='__main__':
    main()
