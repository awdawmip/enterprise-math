"""Carrier-level symmetry checker for the post-#1161 imbalance-counter lift question.

The six FCC line families are the six edges of K4 and the four 3-axis slices are
its four vertex stars.  S4 acts transitively on the six edges.

Consequences checked here:
1. an S4-invariant scalar field on the six visible line slots has one orbit and
   therefore must be constant on all six slots;
2. the four slice restrictions jointly see all six slots (each slot twice), so
   no nonzero six-slot perturbation can be invisible to every slice;
3. therefore an unbounded branch-imbalance scalar cannot be both rotation
   invariant and invisible in the current FCC six-slot readout.

This is only a carrier-readout no-go.  It makes no claim about the unresolved
kernel of NATIVE_6D_STATE -> FCC_CARRIER_READOUT.
"""

from __future__ import annotations

from itertools import combinations, permutations


VERTICES = tuple("ABCD")
EDGES = tuple(combinations(VERTICES, 2))
EDGE_SET = frozenset(EDGES)
STARS = {
    v: frozenset(edge for edge in EDGES if v in edge)
    for v in VERTICES
}


def edge(a: str, b: str) -> tuple[str, str]:
    return tuple(sorted((a, b)))


def edge_action(perm: tuple[int, ...], e: tuple[str, str]) -> tuple[str, str]:
    index = {v: i for i, v in enumerate(VERTICES)}
    a, b = e
    return edge(VERTICES[perm[index[a]]], VERTICES[perm[index[b]]])


def orbit(seed: tuple[str, str]) -> frozenset[tuple[str, str]]:
    return frozenset(edge_action(p, seed) for p in permutations(range(4)))


def run() -> dict[str, object]:
    # S4 transitivity on K4 edges / FCC line families.
    edge_orbit = orbit(EDGES[0])
    if edge_orbit != EDGE_SET:
        raise AssertionError("S4 edge action is not transitive")

    # Four 3-edge stars jointly cover all 6 visible slots, each exactly twice.
    union = frozenset().union(*STARS.values())
    if union != EDGE_SET:
        raise AssertionError("slice stars do not cover every visible line slot")
    incidence = {e: sum(e in star for star in STARS.values()) for e in EDGES}
    if set(incidence.values()) != {2}:
        raise AssertionError("every FCC line slot should occur in exactly two slices")

    # Finite symbolic fixed-field audit: invariance under every S4 edge action
    # forces equality to the seed value on the single edge orbit.
    labels = {e: None for e in EDGES}
    seed = EDGES[0]
    labels[seed] = "c"
    for e in edge_orbit:
        labels[e] = "c"
    if set(labels.values()) != {"c"}:
        raise AssertionError("fixed six-slot scalar field was not constant")

    # Any perturbation invisible on every slice is zero slotwise because every
    # edge is observed in at least one slice.  Record the exact intersection of
    # complements as the set of slots that could possibly remain hidden.
    hidden_slots = EDGE_SET.difference(union)
    if hidden_slots:
        raise AssertionError("visible FCC atlas unexpectedly has hidden line slots")

    return {
        "s4_edge_orbit_size": len(edge_orbit),
        "slice_count": len(STARS),
        "slots_per_slice": sorted({len(star) for star in STARS.values()}),
        "incidence_per_slot": sorted(set(incidence.values())),
        "fixed_scalar_orbit_count": 1,
        "visible_hidden_slots": sorted(hidden_slots),
    }


if __name__ == "__main__":
    result = run()
    expected = {
        "s4_edge_orbit_size": 6,
        "slice_count": 4,
        "slots_per_slice": [3],
        "incidence_per_slot": [2],
        "fixed_scalar_orbit_count": 1,
        "visible_hidden_slots": [],
    }
    if result != expected:
        raise SystemExit(f"unexpected FCC counter-lift audit: {result!r}")
    for key, value in result.items():
        print(f"{key}={value}")
