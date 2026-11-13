"""PREFIX-765: exact rectangle phase switch scan from the PREFIX-760 certificate.

This executable does not reconstruct or rerun the frozen 189-layer kernel. It
consumes the already published rational certificate with its fixed SHA-256.
"""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import hashlib
import json

SOURCE = Path(__file__).with_name("PREFIX760_R6_EXACT_GAMMA_VARIANCE_RESULTS.json")
raw = SOURCE.read_bytes()
assert len(raw) == 24743
assert hashlib.sha256(raw).hexdigest() == (
    "1a480a9a05c4773f82091037fa8f6b695855ffbb885b21e804d56fdc181d4e76"
)
data = json.loads(raw)
assert data["scientific_input_commit"] == "f42f2906d77f24085c123f3ccfe9667d41caa96d"
rows = data["variance_comparisons"]
points = ("0", "1/16", "5/64", "3/32", "1/4", "1/2")
assert tuple(rows) == points

def parse(z):
    r = rows[z]
    assert r["p0"] == "0" and r["p1"] == "1/4"
    dvar = Q(int(r["exact_delta_variance_numerator"]),
             int(r["exact_delta_variance_denominator"]))
    dv2 = Q(int(r["exact_delta_Vq2_numerator"]),
            int(r["exact_delta_Vq2_denominator"]))
    # V_2 = 4 Var - 2 E[Y]; hence delta E[Y] = 2 delta Var - delta V_2/2.
    dmu = 2*dvar - dv2/2
    return dmu, dvar

best = None
scanned = 0
valid = 0
for z0, z1 in combinations(points, 2):
    scanned += 1
    m0,v0 = parse(z0)
    m1,v1 = parse(z1)
    dm, dv = m1-m0, v1-v0
    if dm < 0 and dv < 0:
        valid += 1
        qr = dm/dv
        if best is None or qr < best[2]:
            best = (z0,z1,qr,dm,dv)
assert scanned == 15 and valid == 13
assert (best[0], best[1]) == ("1/16","5/64")
z0,z1,qr,dm,dv = best
lower = Q(69741060, 10**9)
upper = Q(69741061, 10**9)
assert lower < qr < upper
witness_q = Q(7,100)
assert witness_q > qr
assert witness_q*witness_q*dv-witness_q*dm < 0
old_upper = Q(190006,1000000)
assert upper < old_upper
out = {
    "schema": "PREFIX765_R6_RECTANGLE_PHASE_SCAN_V1",
    "frozen_scientific_input": data["scientific_input_commit"],
    "reference_source": "PREFIX760_R6_EXACT_GAMMA_VARIANCE_RESULTS.json",
    "reference_sha256": hashlib.sha256(raw).hexdigest(),
    "source_bytes": len(raw),
    "grid_z": list(points),
    "rectangles_scanned": scanned,
    "rectangles_with_negative_delta_mu_and_variance": valid,
    "minimum_ratio_rectangle_p": ["0", "1/4"],
    "minimum_ratio_rectangle_z": [z0,z1],
    "q_rectangle_decimal": format(float(qr), ".17g"),
    "q_rectangle_strict_lower": "69741060/1000000000",
    "q_rectangle_strict_upper": "69741061/1000000000",
    "q_c_upper_bound_strict": "69741061/1000000000",
    "prior_q_c_strict_upper": "190006/1000000",
    "relative_upper_bound_improvement": format(float(old_upper/upper),".17g"),
    "simple_negative_witness_q": "7/100",
    "simple_negative_witness_verified": True,
    "exact_delta_mu_sign": "NEGATIVE",
    "exact_delta_variance_sign": "NEGATIVE",
    "exact_qr_ratio_numerator": str(qr.numerator),
    "exact_qr_ratio_denominator": str(qr.denominator),
    "proof_scope": "finite six-parameter 15-rectangle scan; q_c bound for frozen external Gamma auxiliary only",
    "not_claimed": ["global minimizer of q_R over all continuous rectangles", "native X6 theorem", "new grid exclusion", "independent review"],
    "result": "ALL_CHECKS_PASS PREFIX765"
}
Path(__file__).with_name("PREFIX765_R6_RECTANGLE_PHASE_SCAN_RESULTS.json").write_text(
    json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8"
)
print(json.dumps({k:out[k] for k in (
    "rectangles_scanned","rectangles_with_negative_delta_mu_and_variance",
    "minimum_ratio_rectangle_z","q_rectangle_decimal","q_c_upper_bound_strict", "result")},indent=2))
