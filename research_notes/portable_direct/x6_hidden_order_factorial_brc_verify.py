#!/usr/bin/env python3
"""All labelled future words h<=2 in the conditional signed-X6 vacancy model."""
from itertools import permutations
from math import factorial
import json

def cell(x): return (x,0,0,0,0,0)
def move(pos,event):
    s,axis,sign=event
    x=list(pos[s]);x[axis]+=sign;target=tuple(x)
    if target in pos:return None
    new=list(pos);new[s]=target
    return tuple(new)
def language(pos,h):
    alphabet=[(s,a,d) for s in range(len(pos)) for a in range(6) for d in (-1,1)]
    out={()};level=[(pos,())]
    for _ in range(h):
        nxt=[]
        for p,w in level:
            for event in alphabet:
                q=move(p,event)
                if q is not None:
                    w1=w+(event,);out.add(w1);nxt.append((q,w1))
        level=nxt
    return frozenset(out)
def build(k,order):
    ps=[None]*(k+2)
    ps[0]=cell(0);ps[k+1]=cell(k+1)
    for i,label in enumerate(order,1):ps[label]=cell(i)
    return tuple(ps)
def witness(k,first,second):
    a=(0,)+first+(k+1,)
    b=(0,)+second+(k+1,)
    pred={a[i]:a[i-1] for i in range(1,k+1)}
    pred2={b[i]:b[i-1] for i in range(1,k+1)}
    s=next(i for i in range(1,k+1) if pred[i]!=pred2[i])
    t=pred[s]
    return ((s,1,1),(t,0,1))
def run():
    rows=[];word_count=0;checks=0
    for k in range(1,6):
        orders=list(permutations(range(1,k+1)))
        L1=[];L2=[]
        for order in orders:
            ps=build(k,order)
            a=language(ps,1);b=language(ps,2)
            L1.append(a);L2.append(b);word_count+=len(a)+len(b)
        assert len(set(L1))==1
        assert len(set(L2))==factorial(k)
        for i,p in enumerate(orders):
            for j,q in enumerate(orders):
                if i==j:continue
                w=witness(k,p,q)
                assert w in L2[i] and w not in L2[j],(k,p,q,w)
                checks+=1
        rows.append({"interior_labels":k,"states":factorial(k),
                     "h1_language_classes":len(set(L1)),
                     "h2_language_classes":len(set(L2)),
                     "h2_min_bits":(factorial(k)-1).bit_length()})
    out={
        "result":"PASS",
        "conditional_model":"finite sources move one signed X6 axis step iff target vacant; exact source+Port word support; not native TRIADIC_CLOSURE_E permission",
        "domain":"all interior label permutations for k=1..5, endpoints fixed, positions 0..k+1 on native e1 within the full six-dimensional signed Cell chart",
        "rows":rows,
        "cumulative_legal_word_observations_h1_and_h2":word_count,
        "ordered_distinguishing_pair_witness_checks":checks,
        "universal_formula":"h1 classes=1; h2 classes=k!; horizon-2 distinguishing bits=ceil(log2(k!)) for all integers k>=1; symbolic proof independent of finite tests"}
    print(json.dumps(out,sort_keys=True,indent=2))
if __name__=="__main__":run()
