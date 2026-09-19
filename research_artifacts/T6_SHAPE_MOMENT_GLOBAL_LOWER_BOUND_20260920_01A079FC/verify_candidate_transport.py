"""Known exact feasible/infeasible q0 points transported by lattice vectors."""
import json
from pathlib import Path

import p19_order9 as check


def main():
    data = json.loads(Path(__file__).with_name("input.json").read_text())
    check.verify_input(data)
    empty = {"cost": 1823, "atoms": [], "weighted_representative": [0] * 18,
             "centers": [0] * 18}
    cases = 0
    for index in range(18):
        for sign in (-1, 1):
            u = [0] * 18
            u[0], u[1] = 48, -13  # masses 864 <= 869 and 481 <= 508.
            weighted = [a * w for a, w in zip(u, check.WEIGHTS)]
            translated = [a + sign * 7 * b for a, b in zip(weighted, data["weighted_basis"][index])]
            positive = {"cost": 1462, "atoms": [], "weighted_representative": translated,
                        "centers": [check.dot(translated, p) for p in data["projector_numerators"]]}
            hit, _ = check.check_pair(positive, empty, data)
            assert hit is not None and hit["q0"] == u
            assert hit["positive_mass"] == 2326 and hit["negative_mass"] == 2304
            cases += 1
    # The uniquely possible q0 point exceeds the positive side budget.
    bad = [0] * 18
    bad[0] = 49 * 18
    positive = {"cost": 1462, "atoms": [], "weighted_representative": bad,
                "centers": [check.dot(bad, p) for p in data["projector_numerators"]]}
    assert check.check_pair(positive, empty, data)[0] is None
    print(json.dumps({"status": "KNOWN_POINT_TRANSPORT_CHECK_PASS", "feasible_cases": cases,
                      "side_budget_rejection_cases": 1, "brc_evaluations": check.TRACE_COUNT}))


if __name__ == "__main__":
    main()
