"""Independent exact-integer witnesses for an author-side X6 source crosswalk.

Scope: pinned six-axis signed torsor with a selected Cell anchor;
R061/R062 signed/observer distinction, R063 fixed positive two-axis sector,
and the translated two-step signed native midpoint interface.
This checker uses always-on guards in CPython normal/-O/-OO.
"""
from itertools import product
from math import comb, factorial, isqrt
import json


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def brc(z):
    length = sum(abs(x) for x in z)
    den = 1
    for x in z:
        den *= factorial(abs(x))
    return factorial(length) // den


def norm2(z):
    return sum(x*x for x in z)


forward = (3, 4, 0, 0, 0, 0)
reverse = tuple(-x for x in forward)
observer_reverse = (1, 0, 4, 0, 0, 0)
require((norm2(forward), norm2(reverse), norm2(observer_reverse)) == (25,25,17), 'R061_NORM')
require((brc(forward), brc(reverse), brc(observer_reverse)) == (35,35,5), 'R062_BRC')

shell = [z for z in product(range(-5,6), repeat=3) if norm2(z) == 25]
require(len(shell) == 30, 'SIGNED_SHELL_ENDPOINTS')
shell_mass = sum(brc(z) for z in shell)
require(shell_mass == 846, 'SIGNED_SHELL_BRC')

roots = [(a,isqrt(2500-a*a)) for a in range(51)
         if isqrt(2500-a*a)**2 == 2500-a*a]
require(roots == [(0,50),(14,48),(30,40),(40,30),(48,14),(50,0)], 'R063_ROOTS')
sector_brc = sum(comb(a+b,a) for a,b in roots)
require(sector_brc == 110695538274255714208, 'R063_POSITIVE_SECTOR_BRC')

start = (1,0,1,0,0,0)
end = (0,1,1,0,0,0)
d = tuple(b-a for a,b in zip(start,end))
require(sum(abs(x) for x in d) == 2 and brc(d) == 2, 'TRIAD_MIDPOINT_DOMAIN')
mids = [tuple(a+(1 if j==i and di>0 else -1 if j==i else 0)
              for j,a in enumerate(start))
        for i,di in enumerate(d) if di]
require(set(mids) == {(0,0,1,0,0,0),(1,1,1,0,0,0)}, 'MIDPOINT_NATIVE')
legacy_mids = {(0,)*6,tuple(a+b for a,b in zip(start,end))}
require(not (legacy_mids & set(mids)), 'LEGACY_MIDPOINT_COUNTEREXAMPLE')

result = {
    'schema':'X6_UNIT133_AUTHOR_INTEGER_WITNESS_V1',
    'status':'EXACT_INTEGER_EXECUTED_AUTHOR_UNREVIEWED',
    'native_forward_reverse_norms':[norm2(forward),norm2(reverse)],
    'native_forward_reverse_minimum_brc':[brc(forward),brc(reverse)],
    'relative_observer_reverse_norm_and_brc':[norm2(observer_reverse),brc(observer_reverse)],
    'three_axis_g25_endpoints':len(shell),
    'three_axis_g25_minimum_brc_mass':shell_mass,
    'fixed_positive_two_axis_g2500_roots':roots,
    'fixed_positive_two_axis_g2500_brc_mass':sector_brc,
    'translated_two_step_correct_midpoints':sorted(mids),
    'legacy_fixed_zero_midpoints_disjoint':True,
    'always_on_guards':8,
}
print(json.dumps(result,ensure_ascii=False,sort_keys=True,separators=(',',':')))
