#!/usr/bin/env python3
"""Exact rational checks for R749SMO; independent of external packages."""
from fractions import Fraction as F
from itertools import product
from math import comb
import json

def chi(mask, source):
    return -1 if (mask & source).bit_count() % 2 else 1

def observer(d, masks, biases):
    """Complete depth-h public binary tree, heap-ordered internal nodes."""
    depth = (len(masks)+1).bit_length()-1
    assert len(masks) == len(biases) == (1 << depth)-1
    rows = [[] for _ in range(1 << depth)]
    for x in range(1 << d):
        def visit(node, level, probability, leaf):
            if level == depth:
                rows[leaf].append(probability)
                return
            a, lam = masks[node], biases[node]
            for j, sign in enumerate((-1, 1)):
                visit(2*node+1+j, level+1,
                      probability*(1+sign*lam*chi(a,x))/2, leaf*2+j)
        visit(0, 0, F(1), 0)
    return rows

def coefficients(rows, d, q):
    return [sum((p*chi(q,x) for x,p in enumerate(row)), F(0))/(1<<d) for row in rows]

def total_variation(p, q):
    return sum((abs(a-b) for a,b in zip(p,q)),F(0))/2

def source_mixture(rows, d, mask, sign):
    return [sum((row[x]*(1+sign*chi(mask,x)) for x in range(1<<d)),F(0))/(1<<d) for row in rows]

def signed_channel(n, lam):
    p=(1+abs(lam))/2
    m=(1-abs(lam))/2
    return sum((F(comb(n,k))*abs(p**k*m**(n-k)-m**k*p**(n-k)) for k in range(n+1)),F(0))/2

def repeat_observer(rows, n, d=2):
    r=[(F(1),)* (1<<d)]
    for _ in range(n):
        r=[tuple(v[x]*w[x] for x in range(1<<d)) for v in r for w in rows]
    return r

count_general=0
max_sensitivity=F(0)
for d, patterns in ((2, 96),(3, 80)):
    internal=7
    alphabet=(0,1,2,3,(1<<d)-1)
    bs=(F(-1),F(-1,2),F(0),F(1,2),F(1))
    for z in range(patterns):
        masks=[alphabet[(z+3*i+z//(i+1))%len(alphabet)] for i in range(internal)]
        biases=[bs[(2*z+7*i+z//(i+2))%len(bs)] for i in range(internal)]
        rows=observer(d,masks,biases)
        assert all(sum((row[x] for row in rows),F(0))==1 for x in range(1<<d))
        for q in range(1,1<<d):
            coef=coefficients(rows,d,q)
            S=sum(map(abs,coef),F(0))
            plus=source_mixture(rows,d,q,1)
            minus=source_mixture(rows,d,q,-1)
            assert total_variation(plus,minus)==S
            assert F(0)<=S<=F(1)
            max_sensitivity=max(max_sensitivity,S)
            count_general+=1

checks_repeat=0
examples=[]
for alpha,beta in ((F(1,2),F(1,2)), (F(1,4),F(3,4)),
                   (F(-1,2),F(1,2)), (F(0),F(3,4)),
                   (F(1),F(-1,2)), (F(-1),F(1))):
    base=observer(2,[1,2,2],[alpha,beta,beta])
    for n in range(1,7):
        rows=repeat_observer(base,n)
        S=sum(map(abs,coefficients(rows,2,3)),F(0))
        expected=signed_channel(n,alpha)*signed_channel(n,beta)
        assert S==expected, (alpha,beta,n,S,expected)
        plus=source_mixture(rows,2,3,1)
        minus=source_mixture(rows,2,3,-1)
        assert total_variation(plus,minus)==S
        checks_repeat+=1
        if alpha==beta==F(1,2):
            examples.append({'n':n,'D_n':'%s'%signed_channel(n,alpha),
                             'S_ab':'%s'%S,'minimax_error':'%s'%(S/2)})

assert examples[0]['S_ab']=='1/4'
assert examples[0]['minimax_error']=='1/8'
summary={'status':'PASS', 'general_exact_witness_checks':count_general,
         'general_depth':3,'general_sources':[2,3],
         'repeated_exact_factorization_checks':checks_repeat,
         'max_observed_sensitivity':str(max_sensitivity),
         'equal_half_bias_horizon':examples,
         'arithmetic':'Python fractions.Fraction: all probability, coefficient and TV comparisons exact',
         'statement_scope':'Finite public binary trees and iid reinitialized two-stage shared-Port family, source fixed across blocks'}
with open('R749SMO_SINGLE_WALSH_MINIMAX_RESULTS.json','w') as f:
    json.dump(summary,f,indent=2,ensure_ascii=False)
print(json.dumps(summary,indent=2,ensure_ascii=False))
