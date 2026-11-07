#!/usr/bin/env python3
"""Exact Fraction checks for Stage279-B source-fiber minimax theorem.
The exhaustive finite checks are witnesses. Universal claims use the paper proofs.
"""
from fractions import Fraction as F
from itertools import product

def tv(a, b):
    assert len(a) == len(b) and sum(a) == sum(b) == 1
    return sum(abs(x-y) for x, y in zip(a, b))/2

def risk_for_policy(sources, decision):
    assert sources and all(len(s) == len(decision) for s in sources)
    assert all(0 <= a <= 1 for a in decision)
    weights = [sum(row) for row in sources]
    assert all(w > 0 for w in weights)
    u = [sum(a*d for a, d in zip(row, decision))/w
         for row, w in zip(sources, weights)]
    pairs = [(weights[i]*weights[j]*abs(u[i]-u[j])/(weights[i]+weights[j]))
             for i in range(len(sources)) for j in range(i+1,len(sources))]
    error = max(pairs, default=F(0))
    low = max([F(0)]+[q-error/w for q, w in zip(u, weights)])
    high = min([F(1)]+[q+error/w for q, w in zip(u, weights)])
    assert F(0) <= low <= high <= F(1)
    achieved = max(abs(w*(q-low)) for q, w in zip(u,weights))
    assert achieved == error
    return error, low, achieved

def sharp_uniform_bound(sources):
    weights = [sum(row) for row in sources]
    conditional = [[a/w for a in row] for row,w in zip(sources,weights)]
    return max((weights[i]*weights[j]/(weights[i]+weights[j]) *
                tv(conditional[i], conditional[j])
                for i in range(len(sources)) for j in range(i+1,len(sources))),
               default=F(0))

def exact_exhaustion(sources):
    k = len(sources[0])
    result = F(0)
    witness = None
    for bits in product((F(0),F(1)), repeat=k):
        val,x,achieved = risk_for_policy(sources,bits)
        if val > result:
            result,witness = val,(bits,x)
    assert result == sharp_uniform_bound(sources)
    return k,2**k,result,witness

def main():
    P=(F(1,4), F(1,8))
    Q=(F(1,8), F(1,4))
    R=(F(3,16),F(3,16))
    assert sum(P)==sum(Q)==sum(R)==F(3,8)
    two=[P,Q]
    e,x,_=risk_for_policy(two,(F(1),F(0)))
    assert (e,x)==(F(1,16), F(1,2))
    assert tv((F(2,3),F(1,3)),(F(1,3),F(2,3)))==F(1,3)
    assert exact_exhaustion(two)[2]==F(1,16)
    assert exact_exhaustion([P,Q,R])[2]==F(1,16)
    print('two-source equal fiber masses: P(C)=Q(C)=3/8; TV=1/3; sharp residual=1/16; x*=1/2')

    U=(F(1,2),F(1,8))
    assert sum(U)==F(5,8)
    data=[P,Q,R,U]
    k, cases, exact, witness=exact_exhaustion(data)
    assert exact==F(7,64), (exact,witness)
    print(f'four-source unequal masses: {cases} deterministic policies; sharp residual={exact}; witness={witness}')

    for decisions in product((F(0),F(1,3),F(2,5),F(1)), repeat=2):
        e,x,achieved=risk_for_policy(data,decisions)
        assert e==achieved and e>=0 and 0<=x<=1
    print('16 rational randomized policies: exact attained Chebyshev minmax in [0,1]')

    six=[
        (F(1,12),F(1,24),F(1,8),F(1,12),F(1,24),F(1,8)),
        (F(1,16),F(1,8),F(1,16),F(1,8),F(1,16),F(1,16)),
        (F(1,8),F(1,8),F(1,16),F(1,16),F(1,32),F(1,32)),
    ]
    k,cases,sharp,witness=exact_exhaustion(six)
    print(f'six-word fiber, 3 sources: exhaustive {cases} binary policies; sharp residual={sharp}; witness={witness}')
    assert all(sum(s)>0 for s in six)
    print('STAGE279_BRC_SOURCE_FIBER_MINIMAX_EXACT_PASS')

if __name__ == '__main__':
    main()
