#!/usr/bin/env python3
"""EC49FGA independent finite audit of analytic H2/Hh BRC theorem.
The infinite lower bound is the mathematical proof in README_EC49FGA.md.
All computations are exact integers over ordered signed-X6 microsteps.
"""
from collections import Counter
import json
from pathlib import Path

CODES = {'a':(-1,-1), 'c':(1,2,-1,-2), 'd':(2,1,-2,-1),
         'e':(3,1,1,-3), 'f':(1,-1), 'g':(2,-2)}
ORDER = 'acdefg'
T = ((1,2,3,1,4,5), (1,6,7,1,1,1), (2,2,8,2,2,2),
     (3,8,3,3,3,3), (4,2,7,4,4,4), (5,6,3,5,5,5),
     (6,6,8,6,6,6), (7,8,7,7,7,7), (8,8,8,8,8,8))
SIG = (0,0,4,1,16,32,8,2,0)
REQ = {1,2,4,8}
BASE = {1:'de', 2:'ed', 4:'ce', 8:'ec'}

def trace(word, h, sig):
    assert len(word)==h
    state=0
    for char in word:
        state=T[state][ORDER.index(char)]
    assert SIG[state]==sig, (word, sig, SIG[state])
    count=Counter(word)
    assert count['e']==count['a']+1 and count['e']>=1
    key=(h+1-count['g'], h+1-2*count['e']-count['f'], count['e'])
    assert all(v>0 for v in key)
    steps=tuple(x for char in word for x in CODES[char])
    s=Counter(steps)
    assert tuple(s[i]-s[-i] for i in range(1,7))==(2,0,0,0,0,0)
    assert tuple(s[i] for i in (1,2,3))==key
    return key,steps

def witness(h):
    other={1:'gfe'+'g'*(h-4)+'d', 2:'fe'+'g'*(h-3)+'d',
           4:'fe'+'g'*(h-3)+'c', 8:'gfe'+'g'*(h-4)+'c'}
    prefixes=set()
    keys=set()
    for depth,choice in ((2,BASE),(h,other)):
        for label,word in choice.items():
            key,steps=trace(word,depth,label)
            keys.add(key)
            prefixes.update(steps[:i] for i in range(1,len(steps)+1))
    assert keys=={(3,1,1),(4,h-2,1)}
    assert len(prefixes)==4*h+42, (h,len(prefixes))
    return len(prefixes)

def first_letter_reachability():
    out={}
    for first in ORDER:
        root=T[0][ORDER.index(first)]
        seen={root}
        stack=[root]
        while stack:
            q=stack.pop()
            for nxt in T[q]:
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        out[first]=sorted({SIG[q] for q in seen}&REQ)
    return out

def main():
    table=first_letter_reachability()
    assert table=={'a':[2,8],'c':[4],'d':[1],
                   'e':[2,8],'f':[2,4],'g':[1,8]}
    covers=[a+b for i,a in enumerate(ORDER) for b in ORDER[i+1:]
            if set(table[a])|set(table[b])==REQ]
    assert covers==['fg']
    baseline=set()
    for label,word in BASE.items():
        _,steps=trace(word,2,label)
        baseline.update(steps[:i] for i in range(1,len(steps)+1))
    assert len(baseline)==28
    checked={h:witness(h) for h in range(4,201)}
    assert all(6*h+14>=4*h+42 for h in range(14,501))
    # H10..H13 were verified by earlier *published exact* DP reports.
    prior={10:82,11:86,12:90,13:94}
    assert all(cost==4*h+42 for h,cost in prior.items())
    report={
      'schema':'EC49FGA_ANALYTIC_INFINITE_BOUND_FINITE_AUDIT_V1',
      'scientific_input_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
      'first_code_low_reachability':table,
      'two_code_covering_pairs':covers,
      'baseline_native_prefix_count':len(baseline),
      'witness_range':[4,200], 'witness_cases_checked':len(checked),
      'witness_h4':checked[4], 'witness_h200':checked[200],
      'analytic_case_A':'28+2*(2h+4-1)+4+4=4h+42',
      'analytic_case_B':'6h+14>=4h+42 for h>=14',
      'h10_h13_cited_exact_prior_costs':prior,
      'audit':'PASS',
      'scope':'Signed native-X6 H2-low/Hh-low four signatures; unrestricted positive complete keys',
      'note':'Finite checks audit input/model and upper witnesses; theorem lower bound is analytic in README.'}
    Path(__file__).with_name('EXACT_AUDIT_EC49FGA.json').write_text(
        json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'audit':'PASS','witness_cases':len(checked),
                      'root_two_code_cover':covers,'h200':checked[200]}))

if __name__=='__main__':
    main()
