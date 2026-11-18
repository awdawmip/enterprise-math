"""Combine the individually labeled and common-origin sweeps using rational arithmetic."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
REPORT = 10**8


def combine(phase, labels):
    assert phase["templates"] == labels["n"] and phase["p"] == labels["p"]
    n = labels["n"]
    v_lo, v_hi = (F(k, 10**14) for k in phase["variance_1e14"])
    common_mean = [F(k, 10**14) for k in phase["mean_1e14"]]
    label_mean = [F(k, 10**12) for k in labels["mean_q_1e12"]]
    assert max(common_mean[0], label_mean[0]) <= min(common_mean[1], label_mean[1])
    s_lo, s_hi = (F(k, 10**12) for k in labels["independent_offsets_switch_1e12"])
    factor2 = 2*v_hi / s_lo**2
    factor_upper = isqrt((factor2.numerator * REPORT**2) // factor2.denominator) + 1
    assert F(factor_upper, REPORT)**2 > factor2
    ratio_lo, ratio_hi = 2*n*v_lo/s_hi, 2*n*v_hi/s_lo
    return {"c": labels["c"], "p": labels["p"], "n": n,
            "cancellation_lower_1e8": max(0, REPORT-factor_upper),
            "variance_ratio_1e8": [ratio_lo*REPORT//1, -(-ratio_hi*REPORT//1)]}


if __name__ == "__main__":
    phases = json.loads((BASE.parent/"profile"/"phase_components.json").read_text())
    labels = {r["c"]: r for r in json.loads((BASE/"individual_profiles.json").read_text())}
    rows = [combine(r,labels[r["c"]]) for r in phases if r["c"] in labels]
    (BASE/"common_counts.json").write_text(json.dumps(rows, indent=2)+"\n")
    print("matched common and individually labeled means for", len(rows), "catalogues")
