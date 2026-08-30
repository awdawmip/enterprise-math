#!/usr/bin/env python3
"""Exact finite checks for P000 philosophy-first Q7 naturality/choice.

This task-local checker deliberately reuses T7_FINITE_SYMMETRY_EQUIVARIANCE
from ``src/enterprise_math/finite_symmetry.py`` for fixed-point/orbit tests.
It adds no new global tool family.
"""
from __future__ import annotations

import sys
from itertools import permutations
from math import factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from enterprise_math.finite_symmetry import global_fixed_points, orbit_partition  # noqa: E402


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[i]] for i in range(len(left)))


def inverse(p: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def parity(p: tuple[int, ...]) -> int:
    return sum(
        p[i] > p[j]
        for i in range(len(p))
        for j in range(i + 1, len(p))
    ) % 2


def point_actions(group: tuple[tuple[int, ...], ...]) -> dict[tuple[int, ...], dict[int, int]]:
    return {g: {i: g[i] for i in range(len(g))} for g in group}


def subgroup_generated(
    generators: set[tuple[int, ...]], n: int
) -> set[tuple[int, ...]]:
    identity = tuple(range(n))
    subgroup = {identity}
    changed = True
    while changed:
        changed = False
        for h in tuple(subgroup):
            for g in generators:
                for value in (compose(h, g), compose(g, h)):
                    if value not in subgroup:
                        subgroup.add(value)
                        changed = True
    return subgroup


def commutator(g: tuple[int, ...], h: tuple[int, ...]) -> tuple[int, ...]:
    return compose(compose(compose(g, h), inverse(g)), inverse(h))


checks = 0


def check(condition: bool, label: str) -> None:
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1


S6 = tuple(permutations(range(6)))
S4 = tuple(permutations(range(4)))
id6 = tuple(range(6))
id4 = tuple(range(4))

# 1. Bare symmetric coordinate selection: six channels under S6.
coordinate_actions = point_actions(S6)
check(len(S6) == factorial(6), "S6 order")
check(
    global_fixed_points(tuple(range(6)), coordinate_actions) == frozenset(),
    "symmetric six-channel model has no invariant coordinate",
)
coordinate_orbits = orbit_partition(tuple(range(6)), coordinate_actions)
check(
    len(coordinate_orbits) == 1 and len(coordinate_orbits[0]) == 6,
    "six coordinates form one S6 orbit",
)
check(
    sum(g[0] == 0 for g in S6) == factorial(5),
    "coordinate stabilizer has order 120",
)

# 2. Axis-channel frames: all bijections A -> C form an S6 torsor.
frames = S6
frame_orbit = {compose(g, id6) for g in S6}
check(len(frames) == 720, "frame count is 6!")
check(len(frame_orbit) == 720, "frame action is transitive")
check(
    sum(compose(g, id6) == id6 for g in S6) == 1,
    "frame stabilizer is trivial",
)
transposition = (1, 0, 2, 3, 4, 5)
check(
    all(compose(transposition, frame) != frame for frame in frames),
    "no frame is fixed by full S6",
)

# 3. Accepted K4-star probe family: ordering the four probes is noncanonical.
# The unordered four-star atlas is preserved; the 24 total orderings form an S4 torsor.
probe_order_actions = {
    g: {frame: compose(g, frame) for frame in S4}
    for g in S4
}
check(len(S4) == 24, "ordered four-star probe atlases count 4!")
probe_orbits = orbit_partition(S4, probe_order_actions)
check(
    len(probe_orbits) == 1 and len(probe_orbits[0]) == 24,
    "ordered probe atlases form one S4 orbit",
)
check(
    global_fixed_points(S4, probe_order_actions) == frozenset(),
    "no ordered K4-star probe atlas is invariant",
)
check(
    sum(compose(g, id4) == id4 for g in S4) == 1,
    "ordered probe-atlas stabilizer is trivial",
)

# 4. Split lift envelope C2 x S4 -> S4.
# [S4,S4]=A4, hence Hom(S4,C2) has exactly two elements: trivial and sign.
commutators = {commutator(g, h) for g in S4 for h in S4}
derived = subgroup_generated(commutators, 4)
even = {g for g in S4 if parity(g) == 0}
check(len(derived) == 12 and derived == even, "S4 derived subgroup is A4")
for character in (lambda _g: 0, parity):
    check(
        all(
            character(compose(g, h)) == (character(g) ^ character(h))
            for g in S4
            for h in S4
        ),
        "trivial/sign maps are C2 characters",
    )
# q-preserving automorphisms are indexed by the same two characters and act
# on the two homomorphic sections by XOR; the action is free and transitive.
section_actions = {
    psi: {chi: chi ^ psi for chi in (0, 1)}
    for psi in (0, 1)
}
check(
    orbit_partition((0, 1), section_actions) == (frozenset({0, 1}),),
    "two split sections form one q-preserving automorphism orbit",
)
check(
    global_fixed_points((0, 1), section_actions) == frozenset(),
    "split extension has sections but no invariant section",
)

# 5. Positive symmetry-breaking regression: a primitive distinguished channel.
S5_fix_0 = tuple(g for g in S6 if g[0] == 0)
rooted_actions = point_actions(S5_fix_0)
check(len(S5_fix_0) == 120, "root-preserving automorphism image is S5")
check(
    global_fixed_points(tuple(range(6)), rooted_actions) == frozenset({0}),
    "primitive root produces exactly one natural coordinate",
)

# 6. Gen12 K=1 logic regression: once q is an isomorphism on the frozen
# generated lift group, its inverse section is a singleton candidate.
singleton_actions = {"id": {"q_inverse": "q_inverse"}}
check(
    global_fixed_points(("q_inverse",), singleton_actions) == frozenset({"q_inverse"}),
    "singleton section is uniquely invariant",
)

print(
    "PASS P000_NATURALITY_CHOICE_KILLER; "
    f"checks={checks}; "
    "finite_groupoid_rule=natural_selections_product_of_component_Aut_fixed_sets; "
    "coordinate=S6:candidates6:fixed0:stab120; "
    "frame=S6:candidates720:one_free_orbit:fixed0; "
    "probe_order=S4:candidates24:one_free_orbit:fixed0; "
    "split_lift=C2xS4:sections2:one_free_qAut_orbit:fixed0; "
    "rooted_coordinate=S5:fixed1; gen12_K1_section=singleton"
)
