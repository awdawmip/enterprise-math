#!/usr/bin/env python3
"""Deterministic finite checks for GEO6 native translation/Følner semantic obstruction.

This checker proves only the finite witness claims in the task-local certificate:
- two incompatible readout-preserving C4 actions on the same eight-state carrier;
- exhaustive absence of a readout-preserving C4-action conjugacy between them;
- incompatible fiberwise-regular C4 and V4 actions on the same readout carrier.

It does not decide the accepted-evidence census; that authority is frozen in the
cited GEO6 selector atlas and Driver review.
"""

from __future__ import annotations

import itertools
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
CERT_PATH = ROOT / "research_artifacts/GEO6_NATIVE_TRANSLATION_FOLNER_SEMANTICS/certificate_20260901.json"

X = [(b, u, v) for b in (0, 1) for u in (0, 1) for v in (0, 1)]
C4 = tuple(range(4))
V4 = tuple(itertools.product((0, 1), repeat=2))


def obs(x: tuple[int, int, int]) -> int:
    return x[0]


def idx(x: tuple[int, int, int]) -> int:
    _, u, v = x
    return 2 * u + v


def from_idx(b: int, i: int) -> tuple[int, int, int]:
    i %= 4
    return (b, i // 2, i % 2)


def c4_mul(g: int, h: int) -> int:
    return (g + h) % 4


def action_a(g: int, x: tuple[int, int, int]) -> tuple[int, int, int]:
    return from_idx(x[0], idx(x) + g)


def action_b(g: int, x: tuple[int, int, int]) -> tuple[int, int, int]:
    if x[0] == 0:
        return from_idx(0, idx(x) + g)
    return x


def v4_mul(g: tuple[int, int], h: tuple[int, int]) -> tuple[int, int]:
    return (g[0] ^ h[0], g[1] ^ h[1])


def action_v(g: tuple[int, int], x: tuple[int, int, int]) -> tuple[int, int, int]:
    b, u, v = x
    return (b, u ^ g[0], v ^ g[1])


def assert_action(group, mul, identity, act) -> None:
    for x in X:
        assert act(identity, x) == x
    for g in group:
        for h in group:
            for x in X:
                assert act(mul(g, h), x) == act(g, act(h, x))


def faithful(group, act) -> bool:
    tables = {tuple(act(g, x) for x in X) for g in group}
    return len(tables) == len(group)


def readout_preserving(group, act) -> bool:
    return all(obs(act(g, x)) == obs(x) for g in group for x in X)


def fiberwise_regular(group, act) -> bool:
    for b in (0, 1):
        fiber = {x for x in X if obs(x) == b}
        for x in fiber:
            orbit = [act(g, x) for g in group]
            if len(set(orbit)) != len(fiber) or set(orbit) != fiber:
                return False
    return True


def fixed_points(act, g) -> int:
    return sum(act(g, x) == x for x in X)


def obs_preserving_bijections():
    fibers = {b: [x for x in X if obs(x) == b] for b in (0, 1)}
    for p0 in itertools.permutations(fibers[0]):
        m0 = dict(zip(fibers[0], p0))
        for p1 in itertools.permutations(fibers[1]):
            yield {**m0, **dict(zip(fibers[1], p1))}


def conjugates_a_to_b(mapping) -> bool:
    return all(
        mapping[action_a(g, x)] == action_b(g, mapping[x])
        for g in C4
        for x in X
    )


def order_c4(g: int) -> int:
    for n in range(1, 5):
        if (n * g) % 4 == 0:
            return n
    raise AssertionError("unreachable")


def order_v4(g: tuple[int, int]) -> int:
    acc = (0, 0)
    for n in range(1, 5):
        acc = v4_mul(acc, g)
        if acc == (0, 0):
            return n
    raise AssertionError("unreachable")


def main() -> int:
    cert = json.loads(CERT_PATH.read_text(encoding="utf-8"))

    assert cert["task_id"] == "RS-GEO6-NATIVE-TRANSLATION-FOLNER-SEMANTICS"
    assert cert["publication_id"] == "TP2-2DACFDB1816BE0DEB532"
    assert cert["researcher_id"] == "EM-G6TRANSFOL-9D7E05"
    assert cert["native_action_count"] == 0
    assert cert["partial_action_count_at_density_strength"] == 0
    assert cert["evidence_cut"]["selector_atlas"]["translation_action_status"] == "UNRESOLVED"
    assert cert["evidence_cut"]["selector_atlas"]["translation_action_resolvers"] == []
    assert cert["evidence_cut"]["selector_atlas"]["translation_folner_status"] == "UNRESOLVED"
    assert cert["downstream_gate"]["translation_folner_selector"] == "BLOCKED_BY_TRANSLATION_ACTION_SELECTOR"

    classes = [row["classification"] for row in cert["candidate_inventory"]]
    assert "NATIVE_ACTION" not in classes
    assert set(classes) <= {
        "PARTIAL_ACTION",
        "PRESENTATION_EQUIVALENCE_ONLY",
        "COMPARISON_ONLY",
        "TYPE_MAP_REJECTED",
    }

    assert_action(C4, c4_mul, 0, action_a)
    assert_action(C4, c4_mul, 0, action_b)
    assert faithful(C4, action_a)
    assert faithful(C4, action_b)
    assert readout_preserving(C4, action_a)
    assert readout_preserving(C4, action_b)
    assert fiberwise_regular(C4, action_a)
    assert not fiberwise_regular(C4, action_b)

    fixed_a = fixed_points(action_a, 1)
    fixed_b = fixed_points(action_b, 1)
    assert fixed_a == 0
    assert fixed_b == 4

    checked = 0
    conjugacies = 0
    for mapping in obs_preserving_bijections():
        checked += 1
        conjugacies += int(conjugates_a_to_b(mapping))
    assert checked == 576
    assert conjugacies == 0

    assert_action(V4, v4_mul, (0, 0), action_v)
    assert faithful(V4, action_v)
    assert readout_preserving(V4, action_v)
    assert fiberwise_regular(V4, action_v)

    c4_orders = sorted(order_c4(g) for g in C4)
    v4_orders = sorted(order_v4(g) for g in V4)
    assert c4_orders == [1, 2, 4, 4]
    assert v4_orders == [1, 2, 2, 2]

    finite = cert["finite_countermodels"]
    assert finite["same_group_pair"]["obs_preserving_bijections_checked"] == checked
    assert finite["same_group_pair"]["obs_preserving_conjugacy_count"] == conjugacies
    assert cert["terminal_theorem"]["terminal_state"] == (
        "CURRENT_P000_NATIVE_TRANSLATION_UNDERDETERMINED_WITH_EXACT_ACTION_TYPING_OBSTRUCTION"
    )

    print(
        "PASS GEO6_TRANSLATION_FOLNER "
        f"states={len(X)} fibers=2 fiber_size=4 "
        f"c4A_faithful={int(faithful(C4, action_a))} "
        f"c4B_faithful={int(faithful(C4, action_b))} "
        f"c4A_fiber_regular={int(fiberwise_regular(C4, action_a))} "
        f"c4B_fiber_regular={int(fiberwise_regular(C4, action_b))} "
        f"generator_fixed_A={fixed_a} generator_fixed_B={fixed_b} "
        f"obs_bijections={checked} obs_conjugacies={conjugacies} "
        f"v4_fiber_regular={int(fiberwise_regular(V4, action_v))} "
        "native_action_count=0 "
        "terminal=CURRENT_P000_NATIVE_TRANSLATION_UNDERDETERMINED_WITH_EXACT_ACTION_TYPING_OBSTRUCTION"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
