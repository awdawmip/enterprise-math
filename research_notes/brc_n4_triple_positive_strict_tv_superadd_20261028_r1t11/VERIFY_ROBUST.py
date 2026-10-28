#!/usr/bin/env python3
"""Exact rational independent check of the analytic robust-interval corollary."""
from fractions import Fraction as F
from pathlib import Path
import runpy
# Consume actual pinned certificate verifier, which also checks its three exact minima.
base=runpy.run_path(str(Path(__file__).with_name('VERIFY.py')))
law=base['law'];full=base['full'];tv=base['tv']
e=F(9,20);radius=F(1,10000)
lo,hi=e-radius,e+radius
assert (lo,hi)==(F(4499,10000),F(4501,10000))
for a,b in ((lo,e),(e,hi),(lo,hi),(F(0),F(1,2))):
 assert tv(law(full(a)),law(full(b)))==(abs(b-a)/4,abs(b-a)/4)
gap=F(243712321,1847261790000)
floor=gap-F(3,4)*radius
assert floor==F(420670747,7389047160000)>0
s2=F(37,30360)-radius/4
assert s2==F(36241,30360000)>0
assert lo>F(255,572)
s3=F(143,31000)*(lo-F(255,572))
assert s3==F(5857,310000000)>0
print('PASS_EXACT_N4_SUPERADD_REAL_INTERVAL',lo,hi,
      'gap_floor',floor,'d2_floor',s2,'d3_floor',s3)
