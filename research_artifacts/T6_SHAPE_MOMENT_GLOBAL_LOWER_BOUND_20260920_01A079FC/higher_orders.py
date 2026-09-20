"""Remaining primitive p19 blocks; reuse the frozen exact order9 kernel.

Each block is independent. This does not close the separate (3,6) audit gap.
"""
import argparse
import hashlib
import json
import time
from pathlib import Path

import p19_order9 as core

BLOCKS = {(4, 6): (8124, 262), (5, 5): (8506, 8506),
          (5, 6): (8506, 262), (6, 6): (262, 262)}


def run(data, a, b, start, stop, max_seconds):
    begin = time.monotonic()
    positive = core.states(a, data)
    negative = positive if a == b else core.states(b, data)
    assert (len(positive), len(negative)) == BLOCKS[a, b]
    radius_max = (2331 - 361 * a - 18) ** 2 + (2331 - 361 * b - 18) ** 2
    assert all(n > 4 * radius_max * d for n, d in data["gram_schmidt_norms"])
    assert 0 <= start < stop <= len(positive)
    primitive = common = oriented_pairs = 0
    completed = start
    counts = [0] * 22
    hit = None
    for i in range(start, stop):
        if time.monotonic() - begin >= max_seconds:
            break
        first_j = i + 1 if a == b else 0
        for j in range(first_j, len(negative)):
            oriented_pairs += 1
            if positive[i]["mask"] & negative[j]["mask"]:
                common += 1
                continue
            primitive += 1
            hit, depth = core.check_pair(positive[i], negative[j], data)
            counts[depth] += 1
            if hit is not None:
                hit.update(positive_index=i, negative_index=j)
                break
        if hit is not None:
            break
        completed = i + 1
        if i == start or core.rem(i + 1 - start, 500) == 0:
            print(json.dumps({"block": [a, b], "completed_stop": completed,
                              "primitive": primitive, "seconds": time.monotonic() - begin}), flush=True)
    return {"schema": "T6_P19_HIGHER_PRIMITIVE_BLOCK_V1", "split": [a, b],
            "vertical_order": a + b, "state_counts": [len(positive), len(negative)],
            "status": "MODULAR_KERNEL_FOUND" if hit else "EXACT_INTERVAL_CLEAR" if completed == stop else "RESOURCE_LIMIT_PARTIAL_CLEAR",
            "requested_rows": [start, stop], "completed_rows": [start, completed],
            "symmetry": "j>i, global-sign representatives" if a == b else "one split orientation, global sign allowed",
            "oriented_pairs": oriented_pairs, "primitive_cosets_checked": primitive,
            "shared_atom_pairs": common, "rejection_depth_counts": counts,
            "radius_squared_upper_bound": radius_max,
            "kernel": hit, "brc_evaluations": core.TRACE_COUNT,
            "seconds": time.monotonic() - begin,
            "scope": "Only this primitive split; old (3,6) audit gap is not resolved by it"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--stop", type=int)
    parser.add_argument("--max-seconds", type=int, default=480)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if (args.a, args.b) not in BLOCKS:
        raise ValueError("only the four unresolved higher blocks are admitted")
    directory = Path(__file__).resolve().parent
    input_path = directory.joinpath("input.json")
    data = json.loads(input_path.read_text())
    core.verify_input(data)
    stop = args.stop if args.stop is not None else BLOCKS[args.a, args.b][0]
    result = run(data, args.a, args.b, args.start, stop, args.max_seconds)
    result["input_sha256"] = hashlib.sha256(input_path.read_bytes()).hexdigest()
    result["core_source_sha256"] = hashlib.sha256(Path(core.__file__).read_bytes()).hexdigest()
    result["consumer_source_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
