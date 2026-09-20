"""Independently establish the old (3,6) claim, not reproduce its missing code."""
import hashlib
import json
import time
from pathlib import Path

import p19_order9 as core


def main():
    started = time.monotonic()
    directory = Path(__file__).resolve().parent
    path = directory.joinpath("input.json")
    data = json.loads(path.read_text())
    core.verify_input(data)
    radius_max = 1230 ** 2 + 147 ** 2
    assert radius_max == 1534509
    assert all(n > 4 * radius_max * d for n, d in data["gram_schmidt_norms"])
    positive, negative = core.states(3, data), core.states(6, data)
    assert (len(positive), len(negative)) == (1482, 262)
    print(json.dumps({"applicability_gate": "PASS", "radius_squared_upper_bound": radius_max,
                      "state_counts": [1482, 262], "time_limit_seconds": 60}), flush=True)
    count = common = completed = 0
    counts = [0] * 22
    hit = None
    for i, pos in enumerate(positive):
        if time.monotonic() - started >= 60:
            break
        for j, neg in enumerate(negative):
            if pos["mask"] & neg["mask"]:
                common += 1
                continue
            count += 1
            hit, depth = core.check_pair(pos, neg, data)
            counts[depth] += 1
            if hit is not None:
                hit.update(positive_index=i, negative_index=j)
                break
        if hit is not None:
            break
        completed = i + 1
    complete = completed == 1482 and hit is None
    if complete:
        assert count == 335374
        assert count + common == 1482 * 262
        assert sum(counts) == count
    result = {"schema": "T6_P19_PRIOR_3_6_INDEPENDENT_RECHECK_V1",
              "status": "MODULAR_KERNEL_FOUND" if hit else "OLD_BOUNDED_CLAIM_INDEPENDENTLY_ESTABLISHED" if complete else "RESOURCE_LIMIT_UNRESOLVED",
              "split": [3, 6], "completed_rows": [0, completed],
              "primitive_cosets_checked": count, "shared_atom_pairs": common,
              "rejection_depth_counts": counts, "kernel": hit,
              "applicability_radius_squared_upper_bound": radius_max,
              "input_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
              "core_source_sha256": hashlib.sha256(Path(core.__file__).read_bytes()).hexdigest(),
              "audit_source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "brc_evaluations": core.TRACE_COUNT, "seconds": time.monotonic() - started,
              "prior_artifact": "T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_6E0914_20260917",
              "scope": "New reproducible independent proof of the same (3,6) conclusion; original builder was not recovered; no claim that its bytes were reproduced"}
    directory.joinpath("audit_3_6.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
