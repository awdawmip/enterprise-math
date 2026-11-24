"""C90 exact 15-pair rank certificate at h=0, U=1/250.

The unchanged local c89_interval_kernel.py is C89's Fraction interval kernel.
Only the initial rational root brackets below were found numerically. Every
accepted root bracket, branch Jacobian and 15 determinant signs are re-proved
here with exact rational interval operations and outward rational rounding.
"""

from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import hashlib
import json

from c89_interval_kernel import branch


SPECS = [
    ("L_minus_low", "left", "0.696797114537", "0.696797114539", 1),
    ("L_minus_high", "left", "0.907335131163", "0.907335131165", -1),
    ("L_plus", "left", "1.048583909758", "1.048583909761", 1),
    ("R_minus_low", "right", "0.365059349986", "0.365059349989", 1),
    ("R_minus_high", "right", "0.974109052306", "0.974109052309", -1),
    ("R_plus", "right", "1.022207509817", "1.022207509821", 1),
]


def certificate():
    branches = {}
    gradients = {}
    for label, side, lo, hi, direction in SPECS:
        data, gradient = branch(side, lo, hi, Q(1, 250), direction)
        # Six disjoint, strictly interior source boxes are part of the claim.
        A_lo, A_hi = map(Q, data["A"])
        assert 0 < A_lo < A_hi < 4
        assert 0 < Q(lo) < Q(hi) < 4
        assert (A_hi < 1) if side == "left" else (A_lo > 1)
        assert Q(hi) < 1 if "minus" in label else Q(lo) > 1
        branches[label] = data
        gradients[label] = gradient

    determinants = []
    minimum_abs = None
    for first, second in combinations(branches, 2):
        x, y = gradients[first], gradients[second]
        value = x[0] * y[1] - x[1] * y[0]
        assert value.a * value.b > 0, (first, second)
        distance = min(abs(value.a), abs(value.b))
        minimum_abs = distance if minimum_abs is None else min(minimum_abs, distance)
        determinants.append({
            "pair": [first, second],
            "reduced_determinant": value.json(),
            "display_interval": value.approx(),
            "sign": 1 if value.a > 0 else -1,
        })
    assert len(determinants) == 15
    assert minimum_abs > 0
    kernel = Path(__file__).with_name("c89_interval_kernel.py")
    return {
        "schema": "C90_SIX_BRANCH_PAIR_RANK_CERTIFICATE_V1",
        "arithmetic": "Fraction; outward interval rounding on the exact rational 10^-100 grid",
        "target": {"h": "0", "U": "1/250"},
        "kernel_origin": "C89 joint/certify_double_slope.py, unchanged bytes",
        "kernel_sha256": hashlib.sha256(kernel.read_bytes()).hexdigest(),
        "determinant_meaning": "det d(t_i,t_j)/d(U,h) = K_i K_j * reduced_determinant; K_i,K_j > 0",
        "branches": branches,
        "pairs": determinants,
        "minimum_absolute_reduced_determinant_lower_bound": str(minimum_abs),
        "display_minimum_absolute_lower_bound": float(minimum_abs),
        "proof_scope": "Six regular roots and all 15 pair ranks at the fixed rational target. Global analytic continuation is proved in GLOBAL_PAIR_TRANSVERSALITY.md.",
    }


if __name__ == "__main__":
    result = certificate()
    out = Path(__file__).with_name("six_branch_rank_certificate.json")
    out.write_text(json.dumps(result, indent=2) + "\n")
    for entry in result["pairs"]:
        print(" / ".join(entry["pair"]), entry["display_interval"])
    print("All 15 strict signs passed.")
    print("Minimum certified absolute lower bound:", result["display_minimum_absolute_lower_bound"])
