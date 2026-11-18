#!/usr/bin/env python3
"""EC49FSX exact rational envelope audit, not the native Bellman recomputation.
For full original data and 141-path tree replay, run the self-contained evidence archive's EC49FSX_VERIFY.py.
"""
from fractions import Fraction as Q
import json
from pathlib import Path
C=json.loads(Path(__file__).with_name("EC49FSX_CERT.json").read_text())
assert C["frozen_source_pin"]=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
def direct(a,b,z): return 319-18*a-75*b-141*z
def swapped(a,b,z): return min(325-94*a-9*b-141*z,323-89*a-12*b-141*z)
for row in C["bellman_vertices"]:
    a,b,z=Q(row["a"]),Q(row["b"]),Q(row["z"])
    assert (direct if row["orientation"]=="D" else swapped)(a,b,z)==Q(row["value"])
a0,a1=Q(1,2),Q(2,3)
b0,b1=Q(7,16),Q(57,128)
z0=Q(1531,2304)
p=[(a0,b0),(a0,b1),(a1,b0),(a1,b1),(Q(53,80),b0),(a1,Q(4,9))]
gap=lambda a,b:direct(a,b,z0)-swapped(a,b,z0)
assert min(gap(a,b) for a,b in p)==Q(441,128)
assert max(gap(a,b) for a,b in p)==Q(379,24)
assert 325-94*Q(53,80)-9*b0-141*z0==323-89*Q(53,80)-12*b0-141*z0
assert 325-94*a1-9*Q(4,9)-141*z0==323-89*a1-12*Q(4,9)-141*z0
assert (319-12*b0-81*Q(31,64)-141*z0) < (323-89*Q(31,64)-12*b0-141*z0)
assert (324-8*b0-141*(a1+Q(1,1024))-93*z0) < (325-94*(a1+Q(1,1024))-9*b0-141*z0)
print("PASS algebra/vertices/gap/sharp boundary witness inequalities")
print("NATIVE_BELLMAN_ORACLE_AND_TREE_REPLAY: see full evidence archive")
