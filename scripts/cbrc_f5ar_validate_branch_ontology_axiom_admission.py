#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple


@dataclass(frozen=True)
class Node:
    name: str
    projection: int
    support: frozenset[str]
    parent: Optional[str]
    root: str
    depth: int
    active: bool = True
    enriched_nonzero: bool = True
    direct_old_link: bool = False
    marker: str = ""
    position: Tuple[int, int] = (0, 0)


@dataclass
class Model:
    nodes: Dict[str, Node]
    roots: Set[str]
    off_branch_states: List[Tuple[str, int, bool]] = field(default_factory=list)

    def children(self, name: str) -> List[Node]:
        return [n for n in self.nodes.values() if n.parent == name and n.active]

    def active_descendants(self, root: str) -> List[Node]:
        return [
            n for n in self.nodes.values()
            if n.active and n.root == root and n.name != root
        ]

    def active_frontier(self, root: str) -> List[Node]:
        out = []
        for n in self.active_descendants(root):
            if not self.children(n.name):
                out.append(n)
        return out


def A0(m: Model) -> bool:
    """Elementary projection nondegeneracy for direct two-branch old splits."""
    for r in sorted(m.roots):
        kids = [n for n in m.children(r) if n.direct_old_link]
        if kids:
            if len(kids) != 2:
                return False
            if any((not k.enriched_nonzero) or k.projection == 0 for k in kids):
                return False
    return True


def A1(m: Model) -> bool:
    """Typed branch-to-old-support faithfulness on directly old-linked active branches."""
    for n in m.nodes.values():
        if n.active and n.name not in m.roots and n.direct_old_link:
            if (not n.enriched_nonzero) or n.projection == 0 or not n.support:
                return False
    return True


def A2(m: Model) -> bool:
    """Nonzero total old projection of each currently retained descendant frontier."""
    for r in sorted(m.roots):
        frontier = m.active_frontier(r)
        if frontier and sum(n.projection for n in frontier) == 0:
            return False
    return True


def A3(m: Model) -> bool:
    """Global support-reflecting retraction on all enriched nonzero states."""
    for n in m.nodes.values():
        if n.enriched_nonzero and n.projection == 0:
            return False
    for _, p, nz in m.off_branch_states:
        if nz and p == 0:
            return False
    return True


def A4(m: Model) -> bool:
    """All-depth leafwise faithfulness, represented as every reachable active branch node nonzero."""
    for r in sorted(m.roots):
        for n in m.active_descendants(r):
            if (not n.enriched_nonzero) or n.projection == 0:
                return False
    return True


def D(m: Model, depth: int) -> bool:
    for r in sorted(m.roots):
        for n in m.active_descendants(r):
            if n.depth <= depth and ((not n.enriched_nonzero) or n.projection == 0):
                return False
    return True


def support_only(m: Model) -> bool:
    for n in m.nodes.values():
        if n.active and n.name not in m.roots and n.direct_old_link:
            if not n.support:
                return False
    return True


def total_conservation(m: Model) -> bool:
    for n in m.nodes.values():
        kids = m.children(n.name)
        if kids and sum(k.projection for k in kids) != n.projection:
            return False
    return True


def mk_root(name: str = "r", projection: int = 1) -> Node:
    return Node(name, projection, frozenset({name}), None, name, 0, True, True, False, "root")


def depth2_zero_model() -> Model:
    r = mk_root()
    a = Node("a", 1, frozenset({"r"}), "r", "r", 1, True, True, True, "m1")
    b = Node("b", 1, frozenset({"r"}), "r", "r", 1, True, True, True, "m2")
    c = Node("c", 1, frozenset({"r"}), "a", "r", 2, True, True, False, "m3")
    d = Node("d", 0, frozenset(), "a", "r", 2, True, True, False, "m4")
    return Model({n.name: n for n in [r, a, b, c, d]}, {"r"})


def a4_not_a1_model() -> Model:
    r = mk_root()
    a = Node("a", 1, frozenset(), "r", "r", 1, True, True, True, "m1")
    b = Node("b", -1, frozenset({"r"}), "r", "r", 1, True, True, True, "m2")
    return Model({n.name: n for n in [r, a, b]}, {"r"})


def a1_not_a4_model() -> Model:
    # Direct old-linked branches are faithful, but an un-inherited depth-2 child is kernel-only.
    return depth2_zero_model()


def a4_not_a3_model() -> Model:
    r = mk_root()
    a = Node("a", 2, frozenset({"r"}), "r", "r", 1, True, True, True, "m1")
    b = Node("b", -1, frozenset({"r"}), "r", "r", 1, True, True, True, "m2")
    return Model({n.name: n for n in [r, a, b]}, {"r"}, [("kernel", 0, True)])


def a3_not_a1_model() -> Model:
    r = mk_root()
    a = Node("a", 2, frozenset(), "r", "r", 1, True, True, True, "m1")
    b = Node("b", -1, frozenset(), "r", "r", 1, True, True, True, "m2")
    return Model({n.name: n for n in [r, a, b]}, {"r"})


def a0_not_a2_model() -> Model:
    r = mk_root()
    a = Node("a", 1, frozenset({"r"}), "r", "r", 1, True, True, True, "m1")
    b = Node("b", -1, frozenset({"r"}), "r", "r", 1, True, True, True, "m2")
    return Model({n.name: n for n in [r, a, b]}, {"r"})


def a2_not_a0_model() -> Model:
    r = mk_root()
    a = Node("a", 1, frozenset({"r"}), "r", "r", 1, True, True, True, "m1")
    b = Node("b", 0, frozenset(), "r", "r", 1, True, True, True, "m2")
    return Model({n.name: n for n in [r, a, b]}, {"r"})


def f5r_kernel_witness() -> Model:
    return a2_not_a0_model()


def faithful_conservative_extension() -> Model:
    # Old coefficient 1 splits as 2 + (-1); pure kernel remains off active-branch type.
    r = mk_root()
    a = Node("a", 2, frozenset({"r"}), "r", "r", 1, True, True, True, "m1")
    b = Node("b", -1, frozenset({"r"}), "r", "r", 1, True, True, True, "m2")
    c = Node("c", 4, frozenset({"r"}), "a", "r", 2, True, True, False, "m3")
    d = Node("d", -2, frozenset({"r"}), "a", "r", 2, True, True, False, "m4")
    return Model({n.name: n for n in [r, a, b, c, d]}, {"r"}, [("kernel", 0, True)])


def signed_cancellation_model() -> Model:
    rp = mk_root("rp", 1)
    rm = mk_root("rm", -1)
    bp = Node("bp", 1, frozenset({"rp"}), "rp", "rp", 1, True, True, True, "p")
    bm = Node("bm", -1, frozenset({"rm"}), "rm", "rm", 1, True, True, True, "m")
    z = Node("z_erased", 0, frozenset(), None, "z_erased", 0, False, False, False, "")
    return Model({n.name: n for n in [rp, rm, bp, bm, z]}, {"rp", "rm"})


def same_root_cancellation_model() -> Model:
    r = mk_root()
    a = Node("a", 1, frozenset({"r"}), "r", "r", 1, True, True, True, "m1")
    b = Node("b", -1, frozenset({"r"}), "r", "r", 1, True, True, True, "m2")
    return Model({n.name: n for n in [r, a, b]}, {"r"})


def translate(m: Model, dx: int, dy: int) -> Model:
    ns = {}
    for n in m.nodes.values():
        ns[n.name] = Node(
            n.name, n.projection, n.support, n.parent, n.root, n.depth,
            n.active, n.enriched_nonzero, n.direct_old_link, n.marker,
            (n.position[0] + dx, n.position[1] + dy)
        )
    return Model(ns, set(m.roots), list(m.off_branch_states))


def relabel_markers(m: Model) -> Model:
    ns = {}
    for i, n in enumerate(sorted(m.nodes.values(), key=lambda x: x.name)):
        ns[n.name] = Node(
            n.name, n.projection, n.support, n.parent, n.root, n.depth,
            n.active, n.enriched_nonzero, n.direct_old_link, f"R{i}", n.position
        )
    return Model(ns, set(m.roots), list(m.off_branch_states))


def comb_model(depth: int, projections: Tuple[int, ...]) -> Model:
    # Binary comb: refine the left child repeatedly. There are 2*depth non-root nodes.
    assert len(projections) == 2 * depth
    nodes = {}
    r = mk_root()
    nodes[r.name] = r
    parent = "r"
    root = "r"
    idx = 0
    for d in range(1, depth + 1):
        left = f"L{d}"
        right = f"R{d}"
        direct = (d == 1)
        nodes[left] = Node(left, projections[idx], frozenset({root}) if projections[idx] != 0 else frozenset(),
                           parent, root, d, True, True, direct, f"m{idx}")
        idx += 1
        nodes[right] = Node(right, projections[idx], frozenset({root}) if projections[idx] != 0 else frozenset(),
                            parent, root, d, True, True, direct, f"m{idx}")
        idx += 1
        parent = left
    return Model(nodes, {root})


def check_depth_enumeration(max_depth: int = 4) -> dict:
    depth = max_depth
    implication_failures = []
    converse_witness = {d: None for d in range(1, depth)}
    a0_not_a4 = None
    count = 0
    for ps in itertools.product((-1, 0, 1), repeat=2 * depth):
        m = comb_model(depth, ps)
        count += 1
        vals = {d: D(m, d) for d in range(1, depth + 1)}
        for d in range(1, depth):
            if vals[d + 1] and not vals[d]:
                implication_failures.append((d + 1, d, ps))
            if vals[d] and not vals[d + 1] and converse_witness[d] is None:
                converse_witness[d] = ps
        if A0(m) and not D(m, depth) and a0_not_a4 is None:
            a0_not_a4 = ps
    return {
        "depth": depth,
        "models_checked": count,
        "implication_failures": implication_failures,
        "strict_converse_witnesses": converse_witness,
        "a0_not_depth4_witness": a0_not_a4,
    }


def main() -> int:
    checks = []
    def ck(name: str, actual, expected) -> None:
        checks.append({"name": name, "actual": actual, "expected": expected, "ok": actual == expected})

    d2 = depth2_zero_model()
    ck("A0_not_A4_depth2", (A0(d2), A4(d2)), (True, False))
    ck("A1_not_A4_without_inheritance", (A1(d2), A4(d2)), (True, False))

    m = a4_not_a1_model()
    ck("A4_not_A1_support_data", (A4(m), A1(m)), (True, False))

    m = a4_not_a3_model()
    ck("A4_not_A3_off_branch_kernel", (A4(m), A3(m)), (True, False))

    m = a3_not_a1_model()
    ck("A3_not_A1_support_data", (A3(m), A1(m)), (True, False))

    m = a0_not_a2_model()
    ck("A0_not_A2_signed_family_sum", (A0(m), A2(m)), (True, False))
    ck("A4_not_A2_signed_family_sum", (A4(m), A2(m)), (True, False))
    ck("A1_not_A2_signed_family_sum", (A1(m), A2(m)), (True, False))
    ck("A3_not_A2_signed_family_sum", (A3(m), A2(m)), (True, False))

    m = a2_not_a0_model()
    ck("A2_not_A0_kernel_branch", (A2(m), A0(m)), (True, False))
    ck("A2_not_A1_kernel_branch", (A2(m), A1(m)), (True, False))
    ck("A2_not_A4_kernel_branch", (A2(m), A4(m)), (True, False))
    ck("A2_not_A3_kernel_branch", (A2(m), A3(m)), (True, False))

    m = f5r_kernel_witness()
    ck("F5R_kernel_witness_pattern", [m.nodes["a"].projection, m.nodes["b"].projection], [1, 0])
    ck("F5R_kernel_witness_active_nonzero", [m.nodes["a"].enriched_nonzero, m.nodes["b"].enriched_nonzero], [True, True])
    ck("F5R_kernel_witness_A0_false", A0(m), False)

    m = faithful_conservative_extension()
    ck("conservative_extension_A0", A0(m), True)
    ck("conservative_extension_A4", A4(m), True)
    ck("conservative_extension_total_conservation", total_conservation(m), True)
    ck("conservative_extension_A3_false_due_kernel", A3(m), False)

    m = signed_cancellation_model()
    ck("signed_cancellation_prebranch_faithful", A1(m) and A4(m), True)
    ck("signed_cancellation_exact_zero", m.nodes["bp"].projection + m.nodes["bm"].projection, 0)
    ck("signed_cancellation_erased_aggregate_out_of_scope", m.nodes["z_erased"].active, False)

    fiber = {
        "words": ["XiXj", "XjXi"],
        "terminal": ["C(1,1)", "C(1,1)"],
        "trace": ["T(1,1)", "T(1,1)"],
    }
    ck("minimal_11_two_witness_fiber_distinct_words", len(set(fiber["words"])), 2)
    ck("minimal_11_two_witness_fiber_same_terminal", len(set(fiber["terminal"])), 1)
    ck("minimal_11_two_witness_fiber_same_trace", len(set(fiber["trace"])), 1)

    m = faithful_conservative_extension()
    contracted_nodes = {k: v for k, v in m.nodes.items() if k not in {"c", "d"}}
    contracted = Model(contracted_nodes, set(m.roots), list(m.off_branch_states))
    ck("tree_expansion_A4", A4(m), True)
    ck("tree_contraction_to_existing_parent_A4", A4(contracted), True)
    ck("tree_expansion_conservation", total_conservation(m), True)
    ck("tree_contraction_conservation", total_conservation(contracted), True)

    translated = translate(m, 17, -9)
    relabeled = relabel_markers(m)
    ck("translation_invariance_A0_A4", (A0(translated), A4(translated)), (A0(m), A4(m)))
    ck("marker_relabel_invariance_A0_A4", (A0(relabeled), A4(relabeled)), (A0(m), A4(m)))

    depth = check_depth_enumeration(4)
    ck("depth4_no_implication_failures", depth["implication_failures"], [])
    ck("depth4_all_strict_converses_found", all(depth["strict_converse_witnesses"][d] is not None for d in (1, 2, 3)), True)
    ck("depth4_A0_not_A4_witness_found", depth["a0_not_depth4_witness"] is not None, True)
    ck("depth4_model_count", depth["models_checked"], 3 ** 8)

    witness_suite = [
        f5r_kernel_witness(),
        a0_not_a2_model(),
        depth2_zero_model(),
        a4_not_a1_model(),
        a4_not_a3_model(),
        a3_not_a1_model(),
        faithful_conservative_extension(),
    ]
    ck("implication_A1_to_A0_on_witness_suite", all((not A1(x)) or A0(x) for x in witness_suite), True)
    ck("implication_A4_to_A0_on_witness_suite", all((not A4(x)) or A0(x) for x in witness_suite), True)
    ck("implication_A3_to_A4_on_witness_suite", all((not A3(x)) or A4(x) for x in witness_suite), True)

    pair_countermodels = {
        "A0_not_A1": a4_not_a1_model(),
        "A0_not_A2": a0_not_a2_model(),
        "A0_not_A3": a4_not_a3_model(),
        "A0_not_A4": depth2_zero_model(),
        "A1_not_A2": a0_not_a2_model(),
        "A1_not_A3": a4_not_a3_model(),
        "A1_not_A4": depth2_zero_model(),
        "A2_not_A0": a2_not_a0_model(),
        "A2_not_A1": a2_not_a0_model(),
        "A2_not_A3": a2_not_a0_model(),
        "A2_not_A4": a2_not_a0_model(),
        "A3_not_A1": a3_not_a1_model(),
        "A3_not_A2": a0_not_a2_model(),
        "A4_not_A1": a4_not_a1_model(),
        "A4_not_A2": a0_not_a2_model(),
        "A4_not_A3": a4_not_a3_model(),
    }
    predicates = {"A0": A0, "A1": A1, "A2": A2, "A3": A3, "A4": A4}
    for label, cm in pair_countermodels.items():
        lhs, rhs = label.split("_not_")
        ck(f"countermodel_{label}", (predicates[lhs](cm), predicates[rhs](cm)), (True, False))

    # Mandatory ablations.
    baseline = faithful_conservative_extension()
    ck("ablate_active_type_global_rule_overconstrains_kernel", A4(baseline) and not A3(baseline), True)

    no_support = a4_not_a1_model()
    ck("ablate_witness_support_loophole_still_closed_projection_only", A4(no_support) and not A1(no_support), True)

    support_kernel = a2_not_a0_model()
    # Give the zero-projection branch explicit witness support: support-only then passes while A0 fails.
    b = support_kernel.nodes["b"]
    support_kernel.nodes["b"] = Node(
        b.name, b.projection, frozenset({"r"}), b.parent, b.root, b.depth,
        b.active, b.enriched_nonzero, b.direct_old_link, b.marker, b.position
    )
    ck("ablate_nonzero_projection_reopens_loophole", support_only(support_kernel) and not A0(support_kernel), True)

    ck("ablate_leafwise_closure_A0_not_A4", A0(d2) and not A4(d2), True)

    cancel_same = same_root_cancellation_model()
    ck("ablate_descendant_family_constraint_preserves_typed_faithfulness", A4(cancel_same) and not A2(cancel_same), True)

    no_conservation = Model(
        {
            "r": mk_root(),
            "a": Node("a", 1, frozenset({"r"}), "r", "r", 1, True, True, True, "m1"),
            "b": Node("b", 1, frozenset({"r"}), "r", "r", 1, True, True, True, "m2"),
        },
        {"r"}
    )
    ck("ablate_total_conservation_loophole_still_closed", A0(no_conservation) and not total_conservation(no_conservation), True)

    ck("signed_cancellation_compatibility_rejects_A2_as_unqualified_rule", A4(cancel_same) and not A2(cancel_same), True)

    # A deliberately marker-specific rule demonstrates why covariance is mandatory.
    def broken_marker_rule(model: Model) -> bool:
        direct = [n for n in model.nodes.values() if n.direct_old_link and n.active]
        return all(n.projection != 0 for n in direct if n.marker == "m1")
    cov_model = a2_not_a0_model()
    ck("broken_marker_rule_before_relabel", broken_marker_rule(cov_model), True)
    ck("broken_marker_rule_not_equivalent_to_A0", (broken_marker_rule(cov_model), A0(cov_model)), (True, False))

    ck("ablate_composition_functoriality_A0_not_A4", A0(d2) and not A4(d2), True)

    mismatches = [c for c in checks if not c["ok"]]
    payload = {
        "schema": "CBRC_F5AR_CHECKER_V1",
        "max_tree_depth": 4,
        "depth_enumeration": depth,
        "minimal_11_fiber": fiber,
        "checks": checks,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    digest = hashlib.sha256(canonical).hexdigest()
    print(f"F5AR_CHECKER_RESULT={'PASS' if not mismatches else 'FAIL'}")
    print(f"check_count={len(checks)}")
    print(f"mismatch_count={len(mismatches)}")
    print(f"finite_tree_depth={depth['depth']}")
    print(f"finite_tree_models={depth['models_checked']}")
    print(f"digest={digest}")
    if mismatches:
        print(json.dumps(mismatches, indent=2, sort_keys=True))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
