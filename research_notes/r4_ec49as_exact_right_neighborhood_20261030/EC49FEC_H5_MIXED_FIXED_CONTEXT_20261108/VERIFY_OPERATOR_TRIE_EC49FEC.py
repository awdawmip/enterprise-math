#!/usr/bin/env python3
"""EC49FEC exact weighted operator-Trie identity, standard-library verifier.
Run alongside EC49FEC_FIXED_CONTEXT_CERTIFICATES.json.
"""
import json
from collections import defaultdict
from pathlib import Path

OPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}

def operator_cost(words):
    children=defaultdict(set)
    for w in words:
        for i,s in enumerate(w):
            children[w[:i]].add(s)
    total=sum(sum(len(OPS[s]) for s in ch) for ch in children.values())
    fc=sum({'f','c'}<=ch for ch in children.values())
    dg=sum({'d','g'}<=ch for ch in children.values())
    return total-fc-dg, (total,fc,dg,len(children))

def native_cost(words):
    pre=set()
    for w in words:
        native=tuple(v for ch in w for v in OPS[ch])
        pre.update(native[:i] for i in range(1,len(native)+1))
    return len(pre)

def words_of(system):
    return [w for ws in system.values() for w in ws]

data=json.loads(Path('EC49FEC_FIXED_CONTEXT_CERTIFICATES.json').read_text())
assert len(data['rows'])==12
for i,row in enumerate(data['rows']):
    fixed=row['fixed']
    for label,suffix,cost in [('pure','pure_h5','pure'),('mixed','mixed_h5','mixed')]:
        wordset=words_of({**fixed,'5':row[suffix]})
        x,details=operator_cost(wordset)
        assert x==native_cost(wordset)==row[cost],(i,label,x,row[cost])
BEST={
 '2':['ce','ed','ge','ec'],
 '3':['feg','gef'],
 '4':['fegg','gefg'],
 '5':['gefgd','feggd','feggc','gefgc'],
 '6':['feggfg','gefgfg'],
 '7':['gefgdfd','feggddf','feggcfc','gefgccf'],
 '8':['gefgdfgf','feggfgfd','feggcffg','gefgfgfc'],
 '9':['feggfgfgf','gefgfgffg']
}
value,details=operator_cost(words_of(BEST))
assert value==native_cost(words_of(BEST))==109
assert details==(116,5,2,29), details
print(json.dumps({'checked_full_systems':25,'all_exact_equalities':True,'best_cost':value,'best_cost_terms':list(details)},indent=2))
