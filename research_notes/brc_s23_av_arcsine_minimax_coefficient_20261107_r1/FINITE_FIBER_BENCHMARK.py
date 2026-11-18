#!/usr/bin/env python3
"""Finite-n, one conditional R-slice comparison; not a global minimax test."""
from VERIFY import weights, binom_pmf

for n in (20_000, 100_000):
    r=n//4
    m=n-r
    q=weights(n,r)
    indices=[k for k,w in enumerate(q) if w>0]
    lo,hi=indices[0],indices[-1]
    length=hi-lo+1
    results=[]
    for numerator in range(5):
        p=(2/3)+(20/21-2/3)*(numerator/4)
        source=binom_pmf(m,p)
        overlap_adaptive=sum(min(qi,bi) for qi,bi in zip(q,source))
        overlap_uniform=sum(min(bi,1/length) for bi in source[lo:hi+1])
        results.append((overlap_adaptive,overlap_uniform))
    print('n=%d R=%d, fixed z=1/4, p fractions [0,1/4,1/2,3/4,1]:'%(n,r))
    for i,(adaptive,uniform) in enumerate(results):
        print('  p_step=%d/4 adaptive=%.9f uniform=%.9f'%(i,adaptive,uniform))
    print('  five-point min adaptive=%.9f uniform=%.9f'%(
        min(x for x,y in results),min(y for x,y in results)))
    assert min(x for x,y in results)>min(y for x,y in results)
print('PASS_S23_AV_FINITE_CONDITIONAL_FIBER_EQUALIZATION_20261107')
