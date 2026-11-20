#!/usr/bin/env python3
"""Directly import frozen P022 Python producer; check full SC6 shell and interval BRC.

Run: python research_checks/X6_UNIT193_PINNED_P022_PYTHON_DIRECT_SIX_AXIS_CHECK_20261120.py \
  --source /path/to/frozen/src/enterprise_math/p022_geodesic_multiplicity.py
This is a direct historical-source validation, not an X6 production bridge or R063 run.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from functools import lru_cache
from itertools import product
from pathlib import Path

EXPECTED_SOURCE_BLOB = "46373050168d2430b6cb3952aa763f3081284632"
EXPECTED_SOURCE_SHA256 = "3e920f21b9ed4124323dbc4d982e2df43381b573f43fcc5ca84952a51bb19237"
FROZEN_COMMIT = "fd2bcff10ca6e147348b6c1236027fc0d2877df3"


def require(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def endpoints_of_radius(radius: int, dimension: int = 6):
    """Distinct signed L1-shell endpoints, without an exponentially large cube scan."""
    def visit(prefix: tuple[int, ...], remaining: int):
        if len(prefix) == dimension:
            if remaining == 0:
                yield prefix
            return
        for magnitude in range(remaining + 1):
            if magnitude == 0:
                yield from visit(prefix + (0,), remaining)
            else:
                yield from visit(prefix + (magnitude,), remaining - magnitude)
                yield from visit(prefix + (-magnitude,), remaining - magnitude)
    yield from visit((), radius)


@lru_cache(None)
def independent_brc(z: tuple[int, ...]) -> int:
    if not any(z):
        return 1
    total = 0
    for i, v in enumerate(z):
        if v:
            next_z = list(z)
            next_z[i] -= 1 if v > 0 else -1
            total += independent_brc(tuple(next_z))
    return total


def independent_interval(z: tuple[int, ...]):
    result = (1,)
    for coord in z:
        next_result = [0] * (len(result) + abs(coord))
        for j, weight in enumerate(result):
            for k in range(abs(coord) + 1):
                next_result[j + k] += weight
        result = tuple(next_result)
    return result


def all_midpoints(z):
    ranges = [range(min(0, v), max(0, v) + 1) for v in z]
    yield from product(*ranges)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="src/enterprise_math/p022_geodesic_multiplicity.py")
    parser.add_argument("--max-radius", type=int, default=6)
    args = parser.parse_args()
    require(args.max_radius == 6, "certificate validation fixed to radius 6")
    source = Path(args.source).read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(source)).encode() + b"\0" + source).hexdigest()
    require(blob == EXPECTED_SOURCE_BLOB, f"historical producer blob drift: {blob}")
    require(hashlib.sha256(source).hexdigest() == EXPECTED_SOURCE_SHA256, "historical producer SHA256 drift")
    spec = importlib.util.spec_from_file_location("p022_frozen_exact_u193", args.source)
    require(spec is not None and spec.loader is not None, "import spec missing")
    producer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(producer)
    counts = []
    endpoint_total = 0
    layer_total = 0
    midpoint_total = 0
    path_total = 0
    radius6_midpoints = 0
    for radius in range(args.max_radius + 1):
        shell_count = 0
        shell_mass = 0
        for z in endpoints_of_radius(radius):
            shell_count += 1
            endpoint_total += 1
            require(producer.sc_graph_radius(z) == radius, f"wrong radius {z}")
            actual_brc = producer.sc_geodesic_path_count(z)
            require(actual_brc == independent_brc(z), f"path mismatch {z}")
            actual_profile = producer.sc_geodesic_interval_profile(z)
            require(actual_profile == independent_interval(z), f"profile mismatch {z}")
            midpoint_weights = [0] * (radius + 1)
            midpoint_counts = [0] * (radius + 1)
            for mid in all_midpoints(z):
                degree = sum(abs(v) for v in mid)
                rem = tuple(a - b for a, b in zip(z, mid))
                midpoint_counts[degree] += 1
                midpoint_weights[degree] += producer.sc_geodesic_path_count(mid) * producer.sc_geodesic_path_count(rem)
                midpoint_total += 1
                if radius == 6:
                    radius6_midpoints += 1
            for degree in range(radius + 1):
                require(midpoint_counts[degree] == actual_profile[degree], f"layer count mismatch {z, degree}")
                require(midpoint_weights[degree] == actual_brc, f"layer BRC mismatch {z, degree}")
                layer_total += 1
            shell_mass += actual_brc
        require(shell_mass == producer.sc_shell_total_geodesic_paths(6, radius), f"shell mismatch {radius}")
        counts.append({"radius": radius, "endpoints": shell_count, "brc_mass": shell_mass})
        path_total += shell_mass
    invalid_cases = [(True, 0, 0, 0, 0, 0), (1.1, 0, 0, 0, 0, 0), (), [1, 0, 0, 0, 0, 0]]
    for invalid in invalid_cases:
        try:
            producer.sc_geodesic_path_count(invalid)
            raise RuntimeError(f"invalid input accepted: {invalid}")
        except ValueError:
            pass
    result = {
        "schema": "X6_UNIT193_PINNED_P022_DIRECT_PYTHON_RESULT_V1",
        "date": "2026-11-20",
        "source_commit": FROZEN_COMMIT,
        "source_path": "src/enterprise_math/p022_geodesic_multiplicity.py",
        "source_blob_sha1": blob,
        "source_sha256": hashlib.sha256(source).hexdigest(),
        "original_module_imported": True,
        "native_R063_rerun": False,
        "graph_interface": "P022 simple-cubic six-axis adapter, not existing X6 native runtime caller",
        "radius_0_to_6": counts,
        "endpoints_checked": endpoint_total,
        "midpoint_instances_checked": midpoint_total,
        "radius6_midpoint_instances_checked": radius6_midpoints,
        "layer_BRC_and_profile_checks": layer_total,
        "all_shell_mass_sum": path_total,
        "invalid_input_checks": len(invalid_cases),
        "violations": 0,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
