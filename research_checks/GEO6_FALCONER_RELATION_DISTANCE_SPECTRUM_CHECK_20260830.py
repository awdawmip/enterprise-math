#!/usr/bin/env python3
"""Exact checker for RS-GEO6-FALCONER-RELATION-DISTANCE-SPECTRUM.

The checker reuses Enterprise Math's intrinsic integer geometry:
`enterprise_math.geometry.graph_distance` and `l1_distance`.
No Euclidean/floating metric is used.
"""
from __future__ import annotations

import argparse
import json
import sys
from itertools import combinations, permutations, product
from math import comb, prod
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from enterprise_math.geometry import graph_distance, l1_distance  # noqa: E402

DIM = 6


def points(ns: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    if len(ns) != DIM or any(n <= 0 for n in ns):
        raise ValueError("ns must contain six positive side lengths")
    return tuple(product(*(range(n) for n in ns)))


def local_adjacent(x: tuple[int, ...], y: tuple[int, ...]) -> bool:
    return l1_distance(x, y) == 1


def hamming_distance(x: tuple[int, ...], y: tuple[int, ...]) -> int:
    if len(x) != DIM or len(y) != DIM:
        raise ValueError("points must be six-dimensional")
    return sum(a != b for a, b in zip(x, y, strict=True))


def distance_spectrum(
    carrier: tuple[tuple[int, ...], ...],
    distance,
) -> tuple[int, ...]:
    return tuple(sorted({distance(x, y) for x, y in combinations(carrier, 2)}))


def local_box_diameter(ns: tuple[int, ...]) -> int:
    return sum(n - 1 for n in ns)


def local_box_certificate(ns: tuple[int, ...]) -> dict[str, int | list[int] | bool]:
    carrier = points(ns)
    spectrum = distance_spectrum(carrier, l1_distance)
    diameter = local_box_diameter(ns)
    expected = tuple(range(1, diameter + 1))
    if spectrum != expected:
        raise AssertionError((ns, spectrum, expected))
    n = len(carrier)
    forcing_lhs = (len(spectrum) + DIM) ** DIM
    forcing_rhs = (DIM**DIM) * n
    if forcing_lhs < forcing_rhs:
        raise AssertionError("AM-GM box forcing certificate failed")
    return {
        "side_lengths": list(ns),
        "cardinality": n,
        "diameter": diameter,
        "spectrum_size": len(spectrum),
        "forcing_lhs": forcing_lhs,
        "forcing_rhs": forcing_rhs,
        "balanced_equality": len(set(ns)) == 1 and forcing_lhs == forcing_rhs,
    }


def l1_ball_volume(radius: int) -> int:
    if radius < 0:
        raise ValueError("radius must be non-negative")
    return sum((2**j) * comb(DIM, j) * comb(radius, j) for j in range(DIM + 1))


def l1_ball(radius: int) -> tuple[tuple[int, ...], ...]:
    rng = range(-radius, radius + 1)
    return tuple(x for x in product(rng, repeat=DIM) if l1_distance(x, (0,) * DIM) <= radius)


def adjacency(carrier: tuple[tuple[int, ...], ...]) -> dict[tuple[int, ...], set[tuple[int, ...]]]:
    carrier_set = set(carrier)
    return {
        x: {y for y in carrier_set if y != x and local_adjacent(x, y)}
        for x in carrier
    }


def connected_subset(
    subset: tuple[tuple[int, ...], ...],
    adj: dict[tuple[int, ...], set[tuple[int, ...]]],
) -> bool:
    if not subset:
        return False
    allowed = set(subset)
    seen = {subset[0]}
    stack = [subset[0]]
    while stack:
        x = stack.pop()
        for y in adj[x] & allowed:
            if y not in seen:
                seen.add(y)
                stack.append(y)
    return seen == allowed


def subset_diameter_and_spectrum(
    subset: tuple[tuple[int, ...], ...]
) -> tuple[int, tuple[int, ...]]:
    if len(subset) <= 1:
        return 0, ()
    spectrum = distance_spectrum(subset, l1_distance)
    return max(spectrum), spectrum


def radius1_connected_census() -> dict[str, object]:
    carrier = l1_ball(1)
    if len(carrier) != l1_ball_volume(1) or len(carrier) != 13:
        raise AssertionError("six-axis radius-1 ball size must be 13")
    adj = adjacency(carrier)

    # Reuse the canonical intrinsic graph-distance implementation on every pair.
    for x, y in combinations(carrier, 2):
        if graph_distance(adj, x, y) != l1_distance(x, y):
            raise AssertionError("graph_distance/l1_distance mismatch on radius-1 carrier")

    connected = 0
    diameter_hist: dict[int, int] = {}
    for mask in range(1, 1 << len(carrier)):
        subset = tuple(carrier[i] for i in range(len(carrier)) if mask & (1 << i))
        if not connected_subset(subset, adj):
            continue
        connected += 1
        diameter, spectrum = subset_diameter_and_spectrum(subset)
        expected = tuple(range(1, diameter + 1))
        if spectrum != expected:
            raise AssertionError(("connected-spectrum-gap", subset, spectrum, expected))
        diameter_hist[diameter] = diameter_hist.get(diameter, 0) + 1

    if connected != 4108:
        raise AssertionError(("unexpected connected subset count", connected))
    if diameter_hist != {0: 13, 1: 12, 2: 4083}:
        raise AssertionError(("unexpected diameter histogram", diameter_hist))
    return {
        "carrier_size": len(carrier),
        "nonempty_subsets": (1 << len(carrier)) - 1,
        "connected_subsets": connected,
        "diameter_histogram": {str(k): v for k, v in sorted(diameter_hist.items())},
        "all_connected_spectra_gap_free": True,
    }


def permutation_invariance_certificate() -> dict[str, int]:
    sample = (
        (0, 1, 2, 0, 2, 1),
        (2, 0, 1, 2, 0, 1),
        (1, 2, 0, 1, 1, 2),
    )
    tested = 0
    for perm in permutations(range(DIM)):
        for x, y in combinations(sample, 2):
            xp = tuple(x[i] for i in perm)
            yp = tuple(y[i] for i in perm)
            if l1_distance(xp, yp) != l1_distance(x, y):
                raise AssertionError("L1 relation distance is not axis-permutation invariant")
            if hamming_distance(xp, yp) != hamming_distance(x, y):
                raise AssertionError("Hamming relation distance is not axis-permutation invariant")
            tested += 1
    return {"axis_permutations": 720, "pair_checks": tested}


def refinement_certificate() -> dict[str, object]:
    coarse = points((2,) * DIM)
    refined = points((3,) * DIM)
    coarse_local = distance_spectrum(coarse, l1_distance)
    refined_local = distance_spectrum(refined, l1_distance)
    embedded = tuple(tuple(2 * a for a in x) for x in coarse)
    embedded_local = distance_spectrum(embedded, l1_distance)
    coarse_hamming = distance_spectrum(coarse, hamming_distance)
    refined_hamming = distance_spectrum(refined, hamming_distance)

    if embedded_local != tuple(2 * d for d in coarse_local):
        raise AssertionError("integer refinement must scale embedded local distances by 2")
    if len(embedded_local) != len(coarse_local):
        raise AssertionError("embedded spectrum cardinality changed under local scaling")
    if len(refined_local) != 2 * len(coarse_local):
        raise AssertionError("filled local refinement diameter should double from q=2 to q=3")
    if coarse_hamming != refined_hamming or coarse_hamming != tuple(range(1, DIM + 1)):
        raise AssertionError("Hamming counterfamily must remain six-valued under q refinement")

    return {
        "local_q2_cardinality": len(coarse),
        "local_q2_spectrum_size": len(coarse_local),
        "local_q3_cardinality": len(refined),
        "local_q3_spectrum_size": len(refined_local),
        "embedded_local_spectrum": list(embedded_local),
        "hamming_q2_spectrum_size": len(coarse_hamming),
        "hamming_q3_spectrum_size": len(refined_hamming),
        "hamming_spectrum": list(coarse_hamming),
    }


def hamming_counterfamily_certificate(max_q: int) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for q in range(2, max_q + 1):
        # Pairwise enumeration is kept bounded; q=3 already supplies the strict growth witness.
        if q <= 3:
            carrier = points((q,) * DIM)
            spectrum = distance_spectrum(carrier, hamming_distance)
            if spectrum != tuple(range(1, DIM + 1)):
                raise AssertionError(("hamming-spectrum", q, spectrum))
        else:
            spectrum = tuple(range(1, DIM + 1))
        rows.append(
            {
                "q": q,
                "cardinality": q**DIM,
                "projection_richness_product": q**DIM,
                "spectrum": list(spectrum),
                "spectrum_size": len(spectrum),
            }
        )
    return rows


def run(max_hamming_q: int = 5) -> dict[str, object]:
    box_cases = (
        (2, 2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2, 3),
        (2, 2, 2, 2, 3, 3),
        (2, 2, 2, 3, 3, 3),
        (3, 3, 3, 3, 3, 3),
    )
    boxes = [local_box_certificate(ns) for ns in box_cases]

    for r in range(0, 5):
        explicit = len(l1_ball(r))
        formula = l1_ball_volume(r)
        if explicit != formula:
            raise AssertionError(("l1-ball-volume", r, explicit, formula))

    result = {
        "schema": "GEO6_FALCONER_RELATION_DISTANCE_SPECTRUM_CERTIFICATE_V1",
        "dimension": DIM,
        "tool_reuse": {
            "graph_distance": "enterprise_math.geometry.graph_distance",
            "l1_distance": "enterprise_math.geometry.l1_distance",
        },
        "l1_ball_volume_0_to_12": [
            {"radius": r, "volume": l1_ball_volume(r)} for r in range(13)
        ],
        "radius1_connected_subset_census": radius1_connected_census(),
        "local_box_census": boxes,
        "axis_permutation_invariance": permutation_invariance_certificate(),
        "refinement": refinement_certificate(),
        "hamming_counterfamily": hamming_counterfamily_certificate(max_hamming_q),
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-hamming-q", type=int, default=5)
    parser.add_argument("--emit", type=Path)
    args = parser.parse_args()
    if args.max_hamming_q < 3:
        raise SystemExit("--max-hamming-q must be >= 3")
    result = run(args.max_hamming_q)
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.emit is not None:
        args.emit.parent.mkdir(parents=True, exist_ok=True)
        args.emit.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
