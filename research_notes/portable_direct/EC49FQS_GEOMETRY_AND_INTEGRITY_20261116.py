#!/usr/bin/env python3
"""EC49FQS exact rational geometry and complete local evidence integrity check.
Usage: python EC49FQS_GEOMETRY_AND_INTEGRITY_20261116.py /path/to/EC49FQS_TWO_SLICES_25GRID_COMPLETE_EVIDENCE_20261116
For independent unrestricted Bellman recomputation, also run the archive's
  PYTHONPATH=code python3 code/EC49FQS_INDEPENDENT_VERIFY.py 0 4
  PYTHONPATH=code python3 code/EC49FQS_INDEPENDENT_VERIFY.py 4 8
This short script only checks evidence hashes and exact rational geometry.
"""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
import json
import sys

base=Path(sys.argv[1]).resolve()
assert base.is_dir()
j=json.loads((base/"MANIFEST_SHA256.json").read_text())
assert j["file_count"]==133
assert j["frozen_science_pin"]=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
for rel,entry in j["files"].items():
    b=(base/rel).read_bytes()
    assert len(b)==entry["bytes"] and sha256(b).hexdigest()==entry["sha256"], rel
assert len(list((base/"certificates").glob("*.json")))==97
assert sha256((base/"source/frozen_original_master.txt").read_bytes()).hexdigest()=="cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"
assert sha256((base/"source/EC49FPG_PROFILE.csv").read_bytes()).hexdigest()=="a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f"

G=sorted({Q(1),Q(13,12),Q(7,6),Q(5,4),Q(4,3),Q(17,12),Q(3,2),
    Q(13,8),Q(7,4),Q(15,8),Q(2),Q(17,8),Q(35,16),
    Q(9,4),Q(37,16),Q(19,8),Q(39,16),Q(5,2),Q(31,12),
    Q(8,3),Q(11,4),Q(17,6),Q(23,8),Q(47,16),Q(3)})
assert len(G)==25
K=lambda x:Q(7557)-169*x
gamma=lambda x:Q(310)*(3-x)/K(x)
assert gamma(Q(35,16))==Q(4030,114997)
assert gamma(Q(37,16))==Q(3410,114659)
pairs=list(zip(G,G[1:]))
area=sum((b-a)*(gamma(a)-gamma(b)) for a,b in pairs)
assert area==Q(3218137345754103957378935,426045785417908030352880504)
fraction=1-area/2
assert fraction==Q(848873433490061956748382073,852091570835816060705761008)

wide=[(a,b) for a,b in pairs if b-a==Q(1,8)]
assert len(wide)==5
assert max(a for a,b in wide)==Q(2)
assert (Q(2),Q(17,8)) in wide
assert all(b-a<=Q(1,12) for a,b in pairs if (a,b) not in wide)
assert K(Q(3))==7050 and K(Q(2))==7219
assert K(Q(17,8))==Q(57583,8)
# M(a,b)=50*(b-a)/(sqrt(K(a))+sqrt(K(b)))**2:
# at fixed width it increases to the right; shorter widths are dominated
# by strict rational bounds, hence unique maximum on [2,17/8].
assert Q(50,12*4*7050) < Q(50,8*4*7219)

for x,g in ((Q(35,16),Q(4030,114997)),(Q(37,16),Q(3410,114659))):
    for lam,first in ((Q(0),[32,34]),(g,[32,34,140,142]),
                      (Q(620,3299),[16,23,140,142]),(Q(1),[16,23])):
        cert=json.loads((base/"certificates"/
            f"{x.numerator}_{x.denominator}_{lam.numerator}_{lam.denominator}.json").read_text())
        assert cert["optimal_first_interpolated"]==first
        assert sorted(map(int,cert["all_optimal_first_trees"].keys()))==first
        assert cert["frozen_scientific_commit"]=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
print("EC49FQS_GEOMETRY_AND_133_FILE_INTEGRITY_PASS",len(G),len(pairs),str(area),str(fraction))
