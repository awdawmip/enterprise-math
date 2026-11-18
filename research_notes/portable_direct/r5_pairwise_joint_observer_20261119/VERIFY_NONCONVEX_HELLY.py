#!/usr/bin/env python3
"""Finite exhaustive tests for a symbolic all-m two-interval Helly counterexample."""
from itertools import combinations
for m in range(3,13):
    omega=set(range(m))
    A=[omega-{i} for i in range(m)]
    B=[omega.copy() for _ in range(m)]
    trueA={frozenset(J) for r in range(m+1) for J in combinations(range(m),r)
           if set.intersection(omega,*(A[i] for i in J))}
    trueB={frozenset(J) for r in range(m+1) for J in combinations(range(m),r)
           if set.intersection(omega,*(B[i] for i in J))}
    assert len(trueA)==(1<<m)-1 and len(trueB)==(1<<m)
    assert all(len(set.intersection(omega,*(A[i] for i in J)))==m-len(J)
               for r in range(m+1) for J in combinations(range(m),r))
    maximalA={J for J in trueA if not any(J<T for T in trueA)}
    maximalB={J for J in trueB if not any(J<T for T in trueB)}
    assert len(maximalA)==m and all(len(J)==m-1 for J in maximalA)
    assert maximalB=={frozenset(range(m))}
    assert all(set.intersection(A[i],A[j]) for i,j in combinations(range(m),2))
    assert all(set.intersection(B[i],B[j]) for i,j in combinations(range(m),2))
    assert all(sum((x in A[i] and (x==0 or x-1 not in A[i]))
                   for x in range(m))<=2 for i in range(m))
print('PASS_NONCONVEX_HELLY_ARITY',list(range(3,13)),'EXHAUSTIVE_ALL_SUBSETS')
