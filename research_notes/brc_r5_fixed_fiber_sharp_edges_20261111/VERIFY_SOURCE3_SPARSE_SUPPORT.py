#!/usr/bin/env python3
"""Exact source-port-3 target-sparsity obstruction for frozen R5 witness."""
from fractions import Fraction as Q
from itertools import combinations
R=(2,10,15,20,25,30,38)
M=tuple(map(Q,('10022571/135903376','1898238/8493961',
 '1460251/8493961','377644447/2548188300',
 '1544855/16987922','2161731/33975844',
 '10022571/135903376')))
q=Q('1076926147/2548188300')
t=Q('1076926147/127409415')
assert t==20*q
counts={'mass_insufficient':0,'moment_insufficient':0}
best=None
best_triple=None
for triple in combinations(range(7),3):
    if sum(M[i] for i in triple)<q:
        counts['mass_insufficient']+=1
        continue
    # Ratios increase: fill greatest ratios first for maximum moment.
    left=q;score=Q(0)
    for i in sorted(triple,reverse=True):
        amount=min(left,M[i]);score+=R[i]*amount;left-=amount
    assert left==0
    assert score<t,(triple,score)
    counts['moment_insufficient']+=1
    if best is None or score>best:
        best=score;best_triple=triple
assert counts=={'mass_insufficient':26,'moment_insufficient':9}
assert best_triple==(1,3,6)
assert best==Q('3961511143/509637660')
assert t-best==Q('23079563/33975844')>0
print('TRIPLES_TOTAL',35)
print('MASS_INSUFFICIENT',counts['mass_insufficient'])
print('MOMENT_INSUFFICIENT',counts['moment_insufficient'])
print('MAX_MOMENT_THREE_TARGETS',best)
print('MAXIMIZER',best_triple)
print('SOURCE3_REQUIRED_MOMENT',t)
print('STRICT_DEFICIT',t-best)
print('SOURCE3_MINIMUM_DISTINCT_POSITIVE_TARGET_ARCS',4)
print('PASS_EXACT_SOURCE3_SPARSE_SUPPORT_OBSTRUCTION')
