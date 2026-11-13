#!/usr/bin/env python3
"""R366 exact signed-BRC coefficient-space stability certificate.

Input: R365 signed 12-term BRC K/J full 5584-line c_(r,j) output.
Rebuild it with published R365_scan.py if needed. All signs use big integers.
Usage: python R366_robust.py /path/to/R365_Q345_352_FULL_COEFFICIENTS.txt
"""
import json
import sys
from hashlib import sha256
from pathlib import Path
from collections import defaultdict

EXPECTED = "50bf1a56fabe89d4752ed71634cbb95d6c7c320d61b09aba1c501857650555a7"
if len(sys.argv) != 2:
    raise SystemExit("Provide complete R365_Q345_352_FULL_COEFFICIENTS.txt")
raw = Path(sys.argv[1]).read_bytes()
assert sha256(raw).hexdigest() == EXPECTED, "R365 immutable input mismatch"
rows = defaultdict(dict)
for line in raw.splitlines():
    r,j,c = map(int,line.split(b","))
    assert j not in rows[r], ("duplicate",r,j)
    rows[r][j] = c
assert sorted(rows) == list(range(345,353))
C = {}
for r, row in rows.items():
    assert sorted(row) == list(range(2*r+1))
    c = [row[j] for j in range(2*r+1)]
    assert all(v>0 for v in c)
    C[r] = c

def holds(p):
    for r,c in C.items():
        n=2*r
        A=(n-1)*c[1]*c[1]
        B=2*n*c[0]*c[2]
        if not B*(p-1)**2 > A*(p+1)**2:
            return False
        for j in range(1,n):
            if not c[j]*c[j]*(p-1)**2 > c[j-1]*c[j+1]*(p+1)**2:
                return False
    return True

hi=2
while not holds(hi):
    hi *= 2
lo=1
while hi-lo > 1:
    mid = (hi+lo)//2
    if holds(mid): hi=mid
    else: lo=mid
assert hi==730 and holds(730) and not holds(729)
# Actual adversarial perturbation at r352,j344 with relative error 1/729.
q=C[352]
assert q[344]**2*728**2 - q[343]*q[345]*730**2 < 0
results=[]
for r,c in sorted(C.items()):
    n=2*r
    A=(n-1)*c[1]**2
    B=2*n*c[0]*c[2]
    assert 0<A<B and B*31**2 > A*33**2
    tm = min(c[j]*c[j]*729**2-c[j-1]*c[j+1]*731**2
             for j in range(1,n))
    um = B*729**2-A*731**2
    assert tm>0 and um>0
    original = b"".join(f"{r},{j},{v}\n".encode() for j,v in enumerate(c))
    results.append({"r":r,"coefficient_count":len(c),
                    "turan_count":n-1,
                    "row_sha256":sha256(original).hexdigest(),
                    "all_turan_lower_bounds_positive":True,
                    "j1_ulc_upper_bound_negative":True,
                    "margin_turan_decimal_digits":len(str(tm)),
                    "margin_j1_ulc_decimal_digits":len(str(um))})
# The small explicit F1-root demonstration is independent of the large scan.
assert 126**2-4*131*45 == -7704 == -36*214
out={"schema":"R366_BRC_PF2_NONPFINFTY_ROBUSTNESS_V1",
     "model":"original signed twelve-term BRC K/J auxiliary coefficients",
     "input_sha256":EXPECTED,"r_range":[345,352],
     "coefficients_checked":sum(x["coefficient_count"] for x in results),
     "turan_lower_bounds_checked":sum(x["turan_count"] for x in results),
     "j1_ulc_obstructions_checked":8,
     "smallest_valid_integer_inverse_radius_denominator":hi,
     "all_radius_1_over_730_perturbations_remain":"PF2 and not PF-infinity",
     "radius_1_over_729_counterexample":"r352 j344",
     "r1_roots":"(-21 +/- i*sqrt(214))/15",
     "status":"author-side exact / unreviewed / not admitted",
     "rows":results}
print(json.dumps(out,ensure_ascii=False,indent=2))
