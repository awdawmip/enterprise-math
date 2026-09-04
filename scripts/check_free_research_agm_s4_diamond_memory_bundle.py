"""Task-local S4/FCC diamond-memory naturality checker for post-#1161 AGM research.

Use the frozen K4 model of the six FCC line families.  A local commuting diamond
inside one three-line star is determined by two incident line families, i.e. by
an unordered K4 wedge.  Ordering the two incident axes selects one of the two
concrete word witnesses X_i X_j / X_j X_i.

The checker verifies:
- 12 unordered diamonds and 24 ordered witness orientations;
- S4 is transitive on diamonds and regular on ordered orientations;
- each diamond stabilizer is C2 and its nontrivial element swaps the two
  witnesses;
- no S4-equivariant global orientation section exists;
- the signed memory fiber is the associated sign local system, while the
  absolute imbalance |z| is invariant under every witness-fiber bijection and
  therefore descends canonically without choosing a section.
"""

from __future__ import annotations

from itertools import combinations, permutations, product


VERTICES = tuple("ABCD")
GROUP = tuple(permutations(VERTICES))


def pmap(p: tuple[str, ...], x: str) -> str:
    return p[VERTICES.index(x)]


def canonical_pair(a: str, b: str) -> tuple[str, str]:
    return tuple(sorted((a, b)))


def unordered_diamonds() -> tuple[tuple[str, tuple[str, str]], ...]:
    result = []
    for center in VERTICES:
        leaves = [v for v in VERTICES if v != center]
        for u, v in combinations(leaves, 2):
            result.append((center, canonical_pair(u, v)))
    return tuple(result)


def ordered_witnesses() -> tuple[tuple[str, str, str], ...]:
    result = []
    for center in VERTICES:
        leaves = [v for v in VERTICES if v != center]
        for first in leaves:
            for second in leaves:
                if first != second:
                    result.append((center, first, second))
    return tuple(result)


DIAMONDS = unordered_diamonds()
ORDERED = ordered_witnesses()


def act_diamond(p: tuple[str, ...], diamond: tuple[str, tuple[str, str]]):
    center, (u, v) = diamond
    return (pmap(p, center), canonical_pair(pmap(p, u), pmap(p, v)))


def act_ordered(p: tuple[str, ...], witness: tuple[str, str, str]):
    center, first, second = witness
    return (pmap(p, center), pmap(p, first), pmap(p, second))


def orientations(diamond: tuple[str, tuple[str, str]]):
    center, (u, v) = diamond
    return ((center, u, v), (center, v, u))


def run() -> dict[str, object]:
    if len(DIAMONDS) != 12 or len(set(DIAMONDS)) != 12:
        raise AssertionError("expected 12 unordered K4 wedges/diamonds")
    if len(ORDERED) != 24 or len(set(ORDERED)) != 24:
        raise AssertionError("expected 24 ordered diamond witnesses")

    d0 = DIAMONDS[0]
    o0 = orientations(d0)[0]
    diamond_orbit = {act_diamond(p, d0) for p in GROUP}
    ordered_orbit = {act_ordered(p, o0) for p in GROUP}
    diamond_stabilizer = [p for p in GROUP if act_diamond(p, d0) == d0]
    ordered_stabilizer = [p for p in GROUP if act_ordered(p, o0) == o0]

    if len(diamond_orbit) != 12 or len(diamond_stabilizer) != 2:
        raise AssertionError("unordered diamond orbit/stabilizer mismatch")
    if len(ordered_orbit) != 24 or len(ordered_stabilizer) != 1:
        raise AssertionError("ordered witness orbit should be regular S4")

    nontrivial = [p for p in diamond_stabilizer if p != VERTICES]
    if len(nontrivial) != 1:
        raise AssertionError("diamond stabilizer should have one nontrivial swap")
    if act_ordered(nontrivial[0], o0) != orientations(d0)[1]:
        raise AssertionError("nontrivial stabilizer element did not swap witnesses")

    # Exhaust every possible orientation section (2 choices on each of 12
    # diamonds).  None is S4-equivariant because the local C2 stabilizer swaps
    # the two orientations.
    equivariant_sections = 0
    for bits in product((0, 1), repeat=len(DIAMONDS)):
        section = {d: orientations(d)[bit] for d, bit in zip(DIAMONDS, bits)}
        good = True
        for p in GROUP:
            for d in DIAMONDS:
                if act_ordered(p, section[d]) != section[act_diamond(p, d)]:
                    good = False
                    break
            if not good:
                break
        equivariant_sections += int(good)
    if equivariant_sections != 0:
        raise AssertionError("unexpected S4-equivariant orientation section")

    # Fixed nonzero |z|: branch-resolved states have two signs per diamond and
    # are naturally identified with the 24 ordered witnesses, a regular S4
    # orbit.  The unlabeled |z| quotient has 12 states and stabilizer C2.
    for magnitude in range(1, 33):
        signed_states = {(ordered, magnitude) for ordered in ORDERED}
        orbit = {(act_ordered(p, o0), magnitude) for p in GROUP}
        if orbit != signed_states:
            raise AssertionError("fixed-magnitude signed memory is not one S4 orbit")

    # Any bijection of a two-element witness fiber is identity or swap.  On a
    # temporary coordinate z, these act by z or -z; the AGM predictive counter
    # |z| is invariant under both.  This is the local full-lift-fiber
    # transparency needed for a scalar first-return observer.
    bijections = ((0, 1), (1, 0))
    scalar_cases = 0
    for z in range(-128, 129):
        for bijection in bijections:
            transported = z if bijection == (0, 1) else -z
            if abs(transported) != abs(z):
                raise AssertionError("absolute branch imbalance lost naturality")
            scalar_cases += 1

    return {
        "unordered_diamonds": len(DIAMONDS),
        "ordered_witnesses": len(ORDERED),
        "diamond_stabilizer_order": len(diamond_stabilizer),
        "ordered_stabilizer_order": len(ordered_stabilizer),
        "equivariant_orientation_sections": equivariant_sections,
        "signed_fixed_magnitude_orbit_size": len(ordered_orbit),
        "unlabeled_fixed_magnitude_orbit_size": len(diamond_orbit),
        "scalar_bijection_naturality_cases": scalar_cases,
    }


if __name__ == "__main__":
    result = run()
    expected = {
        "unordered_diamonds": 12,
        "ordered_witnesses": 24,
        "diamond_stabilizer_order": 2,
        "ordered_stabilizer_order": 1,
        "equivariant_orientation_sections": 0,
        "signed_fixed_magnitude_orbit_size": 24,
        "unlabeled_fixed_magnitude_orbit_size": 12,
        "scalar_bijection_naturality_cases": 514,
    }
    if result != expected:
        raise SystemExit(f"unexpected S4 diamond-memory bundle output: {result!r}")
    for key, value in result.items():
        print(f"{key}={value}")
