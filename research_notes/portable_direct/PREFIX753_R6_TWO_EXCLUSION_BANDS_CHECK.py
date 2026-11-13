#!/usr/bin/env python3
"""PREFIX-753: original PREFIX-712 two-sided offset-strip certificate.
Requires the published PREFIX-752 and PREFIX-741 checkers and their own
pinned dependencies in the same directory. Python 3 + NumPy.
Imported PREFIX-752 executes the full author-level 384x384 sign scan.
Scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Not a native X6 slice theorem; author computational verification only.
"""
from fractions import Fraction as F
import numpy as np
from PREFIX752_R6_FULL_CERTIFIED_FINE_UNION import G, mask
from PREFIX741_R6_INNER_STRIP_194 import pair, oldmu, oldW

assert G.shape == (384,384) and int(mask.sum()) == 137168
u,v=np.indices((384,384))
offset=np.abs(u-v)
inner=offset<=51
outer=offset>=171
assert int(inner.sum())==36900 and int(outer.sum())==45582
assert not np.any(inner & outer)
assert np.all(G[inner]>0.76),float(G[inner].min())
assert np.all(G[outer]>2.98),float(G[outer].min())
assert np.any(G[offset==52]<0)
assert np.any(G[offset==170]<0)
assert int(np.diagonal(mask).sum())==384
# The published PREFIX-752 IEEE754 sign-error bound is <0.01, so
# the exact rational G exceeds 3/4 in the inner band and 2.9 outside.
# The exact rational boundary spots are independently recomputed below.
def old_g(a,b):
    low=pair(F(a,768),F(b,768))[0]
    high=pair(F(a+1,768),F(b+1,768))[1]
    return oldW-high+low*low-max(F(0),(oldmu-low)/2)
def microfloor(x):
    z=x*1000000
    return z.numerator//z.denominator
for a,b,expected in [(55,106,766486),(0,171,2990905),
                     (49,101,-576380),(0,170,-681635)]:
    val=old_g(a,b)
    assert microfloor(val)==expected,(a,b,microfloor(val))
assert not np.any(mask & (G<=0))
print("ALL_CHECKS_PASS PREFIX753-R6")
print("old_712_all_q_positive",int(mask.sum()))
print("inner_offset_0_to_51",int(inner.sum()),"min_G",float(G[inner].min()))
print("outer_offset_171_to_383",int(outer.sum()),"min_G",float(G[outer].min()))
print("old_diagonal_certified",int(np.diagonal(mask).sum()))
print("remaining_if_PREFIX752_union_6794",6794//2,"unordered off-diagonal pairs")
