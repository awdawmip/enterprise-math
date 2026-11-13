#!/usr/bin/env python3
"""Standalone exact integer subset-sum spectrum for the frozen R5 source3/target0 coordinate."""
from fractions import Fraction as F

# Frozen 15 labeled moves ordered (j,i) = (1,1..5), (2,1..5), (5,1..5).
# Each integer weight is exactly 36 * delta_mass(target=0,source=3).
W = (336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
X03 = F(155682221,25142124560000000)
EPSMAX = F(9,115400000)
assert sum(W)==0
reachable={0}
for w in W:
    reachable |= {n+w for n in tuple(reachable)}
assert min(reachable)==-1348 and max(reachable)==1348
assert len(reachable)==2293
assert (1 in reachable) and (2 in reachable) and (-1 in reachable) and (-2 in reachable)
interior={w for w in reachable if w<=-3}
assert len(interior)==1144
assert 36*X03/EPSMAX == F(89828641517,31427655700)
assert F(2) < 36*X03/EPSMAX < F(3)
eps={-36*X03/w for w in interior}
assert len(eps)==1144 and all(0<e<EPSMAX for e in eps)
assert F(155682221,377131868400000000) in eps
assert F(155682221,301705494720000000) in eps
assert F(155682221,75426373680000000) in eps
assert sorted(eps).index(F(155682221,377131868400000000))+1 == 607
assert sorted(eps).index(F(155682221,301705494720000000))+1 == 715
assert sorted(eps).index(F(155682221,75426373680000000))+1 == 1039
print('INTEGER_WEIGHT_VECTOR',','.join(map(str,W)))
print('EXACT_SUBSET_SUM_SUPPORT_SIZE',len(reachable))
print('EXACT_SUBSET_SUM_RANGE',min(reachable),max(reachable))
print('NEGATIVE_SUMS_TOTAL',sum(w<0 for w in reachable))
print('NEGATIVE_SUMS_AT_OR_BELOW_MINUS_THREE',len(interior))
print('EXACT_INTERIOR_THRESHOLD_COUNT_FROM_ONE_COORDINATE',len(eps))
print('RESOURCES_RACE_PHASE_INDICES',607,715,1039)
print('FINAL_ENDPOINT_FROM_OTHER_COORDINATE',EPSMAX)
print('PASS_R5_ONE_COORDINATE_INTEGER_SPECTRUM_1144')
