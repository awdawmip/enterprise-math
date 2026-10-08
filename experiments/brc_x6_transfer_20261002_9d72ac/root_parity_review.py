#!/usr/bin/env python3
"""Independent closed-form and atomwise review of the audit author's parity probe."""
from fractions import Fraction as Q
import json
from math import prod
from pathlib import Path

HERE = Path(__file__).resolve().parent


def run():
    data = json.loads((HERE / "parity_results.json").read_text())
    checked = 0
    for name, rows in data["trajectories"].items():
        for row in rows:
            n = row["n"]
            if name == "independent":
                variance = 1 + n*n
                cumulant = -2*(1+n**4)
            else:
                sign = 1 if name == "parity_plus" else -1
                variance = (1+sign*n)**2
                cumulant = -2*variance**2
            assert Q(row["mean"]) == 0
            assert Q(row["variance"]) == variance
            assert Q(row["kappa4"]) == cumulant
            if variance:
                assert Q(row["gamma4"]) == Q(cumulant, variance**2)
            else:
                assert row["gamma4"] is None
            total = Q()
            seen = set()
            expected_count = 64 if name == "independent" else 32
            for atom in row["law"]:
                x = tuple(atom["raw_chart"])
                q = prod(x[1:])
                initial_first = x[0] - n*q
                assert initial_first in (-1,1) and all(t in (-1,1) for t in x[1:])
                if name != "independent":
                    assert initial_first*q == (1 if name == "parity_plus" else -1)
                assert x not in seen
                seen.add(x)
                assert Q(atom["probability"]) == Q(1,expected_count)
                total += Q(atom["probability"])
                checked += 1
            assert len(seen) == expected_count and total == 1
    result = {
        "status":"PASS", "reviewer":"EM-BRCFIT-9D72AC", "author_reviewed":"EM-BRCAUDIT-9D72AC",
        "method":"Independent explicit orbit F^n(x)=(x1+n*product(x2..x6),x2..x6), equiprobable support and closed moments, without importing parity_probe.py",
        "trajectory_rows":27, "atom_checks":checked,
        "low_order_argument":"For parity +/- densities (1 +/- product_i xi) relative to the uniform sign law, any monomial of total degree <=5 leaves some axis with odd exponent in its product correction. Summing that sign gives zero. Thus all <=5 moments agree; the sixfold product does not.",
        "scope":"conditional native X6 unit-step model only; Q is a joint statistic, not a seventh spatial axis",
        "formal_driver_acceptance":False,
    }
    (HERE / "root_parity_review.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(result,ensure_ascii=False))


if __name__ == "__main__":
    run()
