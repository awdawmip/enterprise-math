#!/usr/bin/env python3
from __future__ import annotations

import json
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "research_artifacts/GEO6_PHYSICAL_REFINEMENT_SUPPORT_TRANSPORT_CORE/typed_classification_certificate.json"


def powerset(xs: tuple[int, ...]) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []
    for mask in range(1 << len(xs)):
        out.append(tuple(x for i, x in enumerate(xs) if (mask >> i) & 1))
    return out


def pullback(support: tuple[int, ...], q: dict[int, int], domain: tuple[int, ...]) -> tuple[int, ...]:
    target = set(support)
    return tuple(x for x in domain if q[x] in target)


def main() -> int:
    coarse_cells = (0, 1)
    fine_cells = (0, 1, 2, 3)
    finer_cells = tuple(range(8))

    q10 = {0: 0, 1: 0, 2: 1, 3: 1}
    q21 = {i: i // 2 for i in finer_cells}
    q20 = {i: q10[q21[i]] for i in finer_cells}

    coarse_edges = {frozenset((0, 1))}
    fine_edges = {
        frozenset((0, 2)),
        frozenset((2, 1)),
        frozenset((1, 3)),
        frozenset((3, 0)),
    }

    mapped_edges = {
        frozenset((q10[a], q10[b]))
        for edge in fine_edges
        for a, b in [tuple(edge)]
        if q10[a] != q10[b]
    }
    assert mapped_edges == coarse_edges
    assert sorted(sum(q10[x] == c for x in fine_cells) for c in coarse_cells) == [2, 2]

    coarse_states = list(product((0, 1), repeat=2))
    fine_states = list(product((0, 1), repeat=4))

    def parity_coarse(y: tuple[int, int, int, int]) -> tuple[int, int]:
        return (y[0] ^ y[1], y[2] ^ y[3])

    projection_fibers = {
        x: [y for y in fine_states if parity_coarse(y) == x]
        for x in coarse_states
    }
    assert {len(v) for v in projection_fibers.values()} == {4}
    compatible_sections = 1
    for x in coarse_states:
        compatible_sections *= len(projection_fibers[x])
    assert compatible_sections == 256

    def left_section(x: tuple[int, int]) -> tuple[int, int, int, int]:
        return (x[0], 0, x[1], 0)

    def zero_arrow(_x: tuple[int, int]) -> tuple[int, int, int, int]:
        return (0, 0, 0, 0)

    assert all(parity_coarse(left_section(x)) == x for x in coarse_states)
    zero_failures = sum(parity_coarse(zero_arrow(x)) != x for x in coarse_states)
    assert zero_failures == 3

    swap = {(a, b): (b, a) for a, b in coarse_states}
    assert len(set(swap.values())) == len(coarse_states)

    observation_fibers = {
        bit: [x for x in coarse_states if x[0] == bit]
        for bit in (0, 1)
    }
    assert sorted(len(v) for v in observation_fibers.values()) == [2, 2]

    coarse_supports = powerset(coarse_cells)
    fine_supports = powerset(fine_cells)
    finer_supports = powerset(finer_cells)
    assert len(coarse_supports) == 4
    assert len(fine_supports) == 16
    assert len(finer_supports) == 256

    incidence_checks = 0
    for s0 in coarse_supports:
        s1 = pullback(s0, q10, fine_cells)
        assert s1 in fine_supports
        for c1 in fine_cells:
            assert ((c1 in s1) == (q10[c1] in s0))
            incidence_checks += 1
        s2_direct = pullback(s0, q20, finer_cells)
        s2_step = pullback(s1, q21, finer_cells)
        assert s2_direct == s2_step
    assert incidence_checks == 16

    defective_fine_supports = [(), (0, 2), (1, 3), (0, 1, 2, 3)]
    missing = [
        s0
        for s0 in coarse_supports
        if pullback(s0, q10, fine_cells) not in defective_fine_supports
    ]
    assert missing == [(0,), (1,)]

    data = json.loads(CERT.read_text(encoding="utf-8"))
    assert data["schema"] == "GEO6_PHYSICAL_REFINEMENT_SUPPORT_TRANSPORT_CERTIFICATE_V1"
    assert data["task_id"] == "RS-GEO6-PHYSICAL-REFINEMENT-SUPPORT-TRANSPORT-CORE"
    assert data["publication_id"] == "TP2-596ED944A7D5C5F8065B"
    assert data["researcher_id"] == "EM-G6REF-6D3A91"
    assert data["finite_cover_witness"]["compatible_state_sections"] == compatible_sections
    assert data["finite_cover_witness"]["fiber_sizes"] == [2, 2]
    assert data["separation_witnesses"]["bad_cross_state_arrow"]["parity_coarse_consistency_failures"] == zero_failures
    assert data["support_pullback_theorem"]["powerset_model"]["incidence_equivalence_checks"] == incidence_checks
    assert data["support_pullback_theorem"]["defective_fine_support_model"]["missing_for_coarse_supports"] == [[0], [1]]

    classes = {
        row["candidate"]: row["classification"]
        for row in data["current_candidate_classification"]
    }
    expected = {
        "FULL_CELL_EQUIVALENCE_OR_AUTOMORPHISM": "EQUIVALENCE_ONLY",
        "SLICE_SELECTION_OBSERVATION_OR_REDUCT": "OBSERVATION_REDUCT_ONLY",
        "FINITE_QUOTIENT_OR_GRAPH_COVER": "ABSTRACT_REFINEMENT_ONLY",
        "Q17_ABSTRACT_REFINEMENT_GRAMMAR": "TYPE_MAP_REJECTED",
        "Q20_EFFECTIVITY_REFINEMENT_GRAMMAR": "TYPE_MAP_REJECTED",
        "Q22_RETURN_PROFILE_1WL_REFINEMENT": "TYPE_MAP_REJECTED",
        "NAMED_PRIMARY_ROTATION_WITHOUT_TYPED_SOURCE_TARGET_ACTION_LAW": "TYPE_MAP_REJECTED",
    }
    assert classes == expected

    clauses = data["minimal_extension_interface"]["independent_semantic_clauses"]
    assert clauses == [
        "TYPED_DISTINCT_FULL_CELL_LEVELS_AND_NON_EQUIVALENCE_STATE_ARROW",
        "NATIVE_NONTRIVIAL_LOCALITY_FIBER_MAP",
        "EXPLICIT_PHYSICAL_SCALE_WITNESS_NOT_DERIVED_FROM_COVER_CARDINALITY",
        "STATE_LOCALITY_UPDATE_PRESERVATION_AND_COMPOSITION_LAW",
    ]

    print(
        "PASS GEO6_PHYSICAL_REFINEMENT "
        f"cover_fibers=2,2 state_sections={compatible_sections} "
        f"zero_arrow_failures={zero_failures} "
        f"support_incidence_checks={incidence_checks} "
        f"support_missing_pullbacks={len(missing)} "
        "terminal=CURRENT_P000_NO_GO_WITH_MINIMUM_EXTENSION_INTERFACE_CLASSIFIED"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
