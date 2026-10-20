#!/usr/bin/env python3
"""Deterministic checker for P000 S4 lift/extension prior-art audit V8."""

from __future__ import annotations

import itertools
import json
import math
from collections import Counter, deque
from pathlib import Path

TASK = "RS-P000-6D-ROTATION-PRIOR-ART-DUPLICATION-AUDIT"
PUBLICATION = "TP2-2F8C6A1D9E7043B5C812"
TERMINAL = "CLASSICAL_S4_EXTENSION_SPLITTING_CORE_CLASSIFIED_P000_COMPOUND_LIFT_SEMANTICS_BOUNDARY_FROZEN"

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "research_artifacts/P000_S4_LIFT_EXTENSION_PRIOR_ART_AUDIT_V8"
CLAIM_MAP = ART / "claim_map.json"
SOURCE_LEDGER = ART / "source_ledger.json"
FINITE_CERT = ART / "finite_s4_certificate.json"
RETURN = ROOT / "research_returns/P000_S4_LIFT_EXTENSION_PRIOR_ART_AUDIT_V8_RETURN_20260830.md"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def compose(p, q):
    """p o q, apply q first."""
    return tuple(p[q[i]] for i in range(len(p)))


def ppow(p, n):
    r = tuple(range(len(p)))
    for _ in range(n):
        r = compose(r, p)
    return r


def generated_group(gens):
    ident = tuple(range(len(gens[0])))
    seen = {ident}
    q = deque([ident])
    while q:
        g = q.popleft()
        for h in gens:
            for x in (compose(g, h), compose(h, g)):
                if x not in seen:
                    seen.add(x)
                    q.append(x)
    return seen


def parity(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2


def mm(A, B):
    return tuple(
        sum(A[2 * i + k] * B[2 * k + j] for k in range(2)) % 3
        for i in range(2)
        for j in range(2)
    )


def mpow(A, n):
    ident = (1, 0, 0, 1)
    r = ident
    for _ in range(n):
        r = mm(r, A)
    return r


def det(A):
    return (A[0] * A[3] - A[1] * A[2]) % 3


def normalize(v):
    x, y = v
    if x % 3:
        inv = 1 if x % 3 == 1 else 2
        return (1, (y * inv) % 3)
    return (0, 1)


def act(A, v):
    x, y = v
    return (
        (A[0] * x + A[1] * y) % 3,
        (A[2] * x + A[3] * y) % 3,
    )


def projective_perm(A, points):
    return tuple(points.index(normalize(act(A, v))) for v in points)


def main():
    checks = 0
    claim_map = load(CLAIM_MAP)
    ledger = load(SOURCE_LEDGER)
    cert = load(FINITE_CERT)
    ret = RETURN.read_text(encoding="utf-8")

    assert claim_map["task_id"] == TASK
    assert claim_map["publication_id"] == PUBLICATION
    assert len(claim_map["claims"]) == 12
    assert [r["claim_no"] for r in claim_map["claims"]] == list(range(1, 13))
    checks += 4

    expected_counts = {
        "EXACT_DUPLICATE": 9,
        "PARTIAL_ANTECEDENT": 1,
        "ADJACENT_METHOD": 1,
        "NO_MATERIAL_MATCH": 1,
    }
    actual_counts = Counter(r["classification"] for r in claim_map["claims"])
    assert dict(actual_counts) == expected_counts
    assert claim_map["classification_counts"] == expected_counts
    checks += 2

    source_ids = {s["source_id"] for s in ledger["external_sources"]}
    source_ids |= {s["source_id"] for s in ledger["internal_dependencies"]}
    for row in claim_map["claims"]:
        assert row["scope_guard"].strip()
        assert row["external_boundary"].strip()
        assert row["source_ids"]
        assert set(row["source_ids"]) <= source_ids
        checks += 4

    guards = claim_map["required_guards"]
    assert "abelian" in guards["H2"].lower()
    assert "module" in guards["H2"].lower()
    assert "H^3" in guards["NONABELIAN"]
    assert "H^2" in guards["NONABELIAN"]
    assert "NO_MATERIAL_MATCH != NOVELTY" in guards["NOVELTY"]
    assert guards["FLATNESS"] == "STANDARD_FLATNESS != TRIVIAL_GLOBAL_HOLONOMY."
    checks += 6

    ident4 = (0, 1, 2, 3)
    a = (0, 2, 3, 1)
    b = (1, 0, 2, 3)
    assert ppow(a, 3) == ident4
    assert ppow(b, 2) == ident4
    assert ppow(compose(a, b), 4) == ident4
    G = generated_group([a, b])
    assert len(G) == 24
    checks += 4

    edges = list(itertools.combinations(range(4), 2))
    edge_index = {e: i for i, e in enumerate(edges)}

    def edge_perm(p):
        out = []
        for u, v in edges:
            out.append(edge_index[tuple(sorted((p[u], p[v])))])
        return tuple(out)

    edge_image = {edge_perm(g) for g in G}
    assert len(edges) == 6
    assert len(edge_image) == 24
    assert cert["s4_natural_action"]["induced_two_subset_image_order"] == 24
    checks += 3

    assert all(math.factorial(n) < 24 for n in range(1, 4))
    assert math.factorial(4) == 24
    assert cert["s4_natural_action"]["minimum_faithful_permutation_degree"] == 4
    checks += 3

    def emul(x, y):
        c, g = x
        d, h = y
        return ((c + d) % 2, compose(g, h))

    for g in G:
        for h in G:
            assert emul((0, g), (0, h)) == (0, compose(g, h))
            assert emul((parity(g), g), (parity(h), h)) == (
                parity(compose(g, h)),
                compose(g, h),
            )
            checks += 2

    assert any((0, g) != (parity(g), g) for g in G)
    checks += 1

    def F(x):
        c, g = x
        return ((c + parity(g)) % 2, g)

    E = [(c, g) for c in (0, 1) for g in G]
    assert len(E) == 48
    for x in E:
        for y in E:
            assert F(emul(x, y)) == emul(F(x), F(y))
            checks += 1
    assert all(F((0, g)) == (parity(g), g) for g in G)
    checks += 1

    Atilde = (1, a)
    Btilde = (0, b)

    def epow(x, n):
        r = (0, ident4)
        for _ in range(n):
            r = emul(r, x)
        return r

    assert epow(Atilde, 3) == (1, ident4)
    assert epow(Btilde, 2) == (0, ident4)
    assert epow(emul(Atilde, Btilde), 4) == (0, ident4)
    checks += 3

    I2 = (1, 0, 0, 1)
    minusI = (2, 0, 0, 2)
    GL = [A for A in itertools.product(range(3), repeat=4) if det(A)]
    assert len(GL) == 48
    points = [(1, 0), (0, 1), (1, 1), (1, 2)]
    image = {projective_perm(A, points) for A in GL}
    assert len(image) == 24
    kernel = [A for A in GL if projective_perm(A, points) == ident4]
    assert set(kernel) == {I2, minusI}
    checks += 3

    lifts_a = [A for A in GL if projective_perm(A, points) == a]
    lifts_b = [A for A in GL if projective_perm(A, points) == b]
    assert len(lifts_a) == 2 and len(lifts_b) == 2
    pairs = list(itertools.product(lifts_a, lifts_b))
    assert len(pairs) == 4
    checks += 2

    for A, B in pairs:
        assert mpow(mm(A, B), 4) == minusI
        checks += 1
    assert cert["GL2_F3_central_extension"]["nonsplit"] is True
    assert cert["GL2_F3_central_extension"]["all_lift_pairs_fail_homomorphic_section"] is True
    checks += 2

    lg = cert["logic_guards"]
    assert lg["relation_residue_implies_nonsplit"] is False
    assert lg["split_implies_canonical_section"] is False
    assert lg["one_positive_model_implies_universal_existence"] is False
    assert lg["ordinary_H2_of_nonabelian_kernel_is_general_classifier"] is False
    assert lg["no_material_match_implies_novelty"] is False
    checks += 5

    required_phrases = [
        TERMINAL,
        "NO_MATERIAL_MATCH != NOVELTY",
        "STANDARD_FLATNESS != TRIVIAL_GLOBAL_HOLONOMY",
        "H^3(S4,Z(K))",
        "H^2(S4,Z(K))",
        "GEN12_REPRESENTATION_CORE = CLASSICAL",
        "P000_COMPOUND_SEMANTICS = NO_MATERIAL_MATCH_ONLY",
        "UNIVERSAL_EXISTENCE != ONE_MODEL_EXISTENCE",
        "RELATION_RESIDUE != NONSPLITTING_CERTIFICATE",
        "SPLIT != CANONICAL_SECTION",
    ]
    for phrase in required_phrases:
        assert phrase in ret, phrase
        checks += 1

    print("PASS P000_S4_LIFT_EXTENSION_PRIOR_ART_AUDIT_V8_CHECK")
    print(f"checks={checks}")
    print(f"claims={len(claim_map['claims'])}")
    print(f"classification_counts={dict(actual_counts)}")
    print(f"s4_order={len(G)} edge_image_order={len(edge_image)} min_faithful_degree=4")
    print("split_comparator=C2xS4 sections=2+ automorphism_swaps")
    print("nonsplit_comparator=GL2(3)->PGL2(3)~=S4 all_4_target_lift_pairs_have_(AB)^4=-I")
    print(f"terminal_class={TERMINAL}")


if __name__ == "__main__":
    main()
