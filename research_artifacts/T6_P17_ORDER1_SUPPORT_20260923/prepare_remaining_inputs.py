"""Generate exact next-question inputs, without enumerating their solutions."""
import hashlib
import json
from pathlib import Path

import solve_r1 as solver


def main():
    root = Path(__file__).resolve().parent
    raw = root.joinpath("portable_input.json").read_bytes()
    data = json.loads(raw)
    R, exact = solver.R, solver.exact
    basis = [[int(x) for x in row] for row in data["weighted_basis"]]
    weights = [int(x) for x in data["weights"]]
    norms = [R(int(n), int(d)) for n, d in data["gram_schmidt_squared"]]
    mu = [[R(int(n), int(d)) for n, d in row] for row in data["mu"]]
    modulus = 17 ** 6
    matrix = [[exact.inv(j ** k, modulus) for j in range(1, 7)] for k in range(1, 7)]
    cases = []
    for residue in range(2, 17):
        target = [-exact.inv((17 + residue) ** k, modulus) for k in range(1, 7)]
        u = solver.solve_modular(matrix, target, modulus) + [0] * 10
        weighted = [a * w for a, w in zip(u, weights)]
        centers = []
        for j in range(16):
            value = R(exact.dot(weighted, basis[j]))
            value = value - sum(centers[k] * mu[j][k] * norms[k] for k in range(j))
            centers.append(value.ratio(norms[j]))
        for k in range(1, 7):
            m = 17 ** k
            assert exact.rem(sum(a * exact.inv(j ** k, m) for j, a in enumerate(u, 1)) + exact.inv((17 + residue) ** k, m), m) == 0
        cost = 17 * (17 + residue) - 1
        radius = (2331 - cost) ** 2 + 2331 ** 2
        assert all(n.n > radius * n.d for n in norms)
        cases.append({"residue": str(residue), "vertical_denominator": str(cost + 1),
                      "vertical_mass": str(cost), "positive_q0_budget": str(2331 - cost),
                      "negative_q0_budget": "2331", "radius_squared": str(radius),
                      "maximal_prime17_admissible": residue not in {2, 6, 12, 14},
                      "particular_q0": [str(x) for x in u],
                      "weighted_particular": [str(x) for x in weighted],
                      "centers": [solver.pack(x) for x in centers],
                      "status": "EXACT_INPUT_ONLY_NO_FEASIBILITY_VERDICT"})
    output = {"schema": "T6_P17_ORDER1_REMAINING_PORTABLE_INPUTS_V1",
              "common_input_file": "portable_input.json", "common_input_sha256": hashlib.sha256(raw).hexdigest(),
              "replace_r1_fields_with_each_case": True,
              "admissible_unfinished_residues": [3,4,5,7,8,9,10,11,13,15,16],
              "domain_exclusions": {"2":"17+r=19", "6":"17+r=23", "12":"17+r=29", "14":"17+r=31"},
              "cases": cases, "arithmetic_verification": "All six affine congruences and the two-candidate bound checked; no search run"}
    root.joinpath("remaining_inputs.json").write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status": "REMAINING_INPUTS_VERIFIED", "relaxed_classes": 15, "maximal_prime17_admissible": 11}))


if __name__ == "__main__":
    main()
