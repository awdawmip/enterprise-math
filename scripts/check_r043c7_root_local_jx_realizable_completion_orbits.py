#!/usr/bin/env python3
"""
R043-C7 exact root-link shell classifier.

This checker is intentionally local: it enumerates only the 12 native neighbors
of one root in the frozen FCC/HCP 12-contact graphs. It does not enumerate
lattice animals.

For a reachable root x:
    I = occupied native neighbors of x
    A = old frontier native neighbors of x
    Z = newly exposed neighbors after occupying x

Every globally realizable shell obeys I != empty and E_link(I,Z)=empty.
Equivalently boundary_link(I) is contained in A. We enumerate the full
combinatorial superset of such shell status patterns.

The visible-current shell row signature is the induced graph on A with label
    r_Z(a) = number of Z-neighbors of a in the root link.
Because every frozen native edge x-a has exactly four common native neighbors,
    r_Z(a) = 4 - |N_G(x) intersect N_G(a)| - kappa_x(a),
where kappa_x(a)=|C intersect N(x) intersect N(a)|.

Claims checked:
* HCP: the row signature determines one A/Z-colored shell-completion orbit.
* FCC: exactly two row-signature classes are ambiguous; augmenting by the
  degree multiset of L[Z] resolves every shell-completion orbit.
* The remaining base-relative alignment is finite. Its coset index
  |Aut(Q_A)| / |res_A Aut(H)| is at most 8 in both worlds.
"""

from __future__ import annotations

import collections
import json
from typing import Set, Tuple

import networkx as nx

Point = Tuple[int, int, int]


FCC_DIRS = sorted(
    {
        tuple(v)
        for zero in range(3)
        for s1 in (-1, 1)
        for s2 in (-1, 1)
        for v in (
            [
                0 if i == zero else (s1 if i == [j for j in range(3) if j != zero][0] else s2)
                for i in range(3)
            ],
        )
    }
)

TRI_DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1))


def fcc_neighbors(p: Point) -> Set[Point]:
    return {
        (p[0] + d[0], p[1] + d[1], p[2] + d[2])
        for d in FCC_DIRS
    }


def hcp_neighbors(p: Point) -> Set[Point]:
    i, j, k = p
    out = {(i + di, j + dj, k) for di, dj in TRI_DIRS}
    offsets = ((0, 0), (-1, 0), (0, -1)) if k % 2 == 0 else ((0, 0), (1, 0), (0, 1))
    for di, dj in offsets:
        out.add((i + di, j + dj, k + 1))
        out.add((i + di, j + dj, k - 1))
    return out


def root_link(world: str):
    neighbors = fcc_neighbors if world == "FCC" else hcp_neighbors
    root = (0, 0, 0)
    shell = sorted(neighbors(root))
    graph = nx.Graph()
    graph.add_nodes_from(shell)
    for i, u in enumerate(shell):
        nu = neighbors(u)
        for v in shell[i + 1 :]:
            if v in nu:
                graph.add_edge(u, v)
    assert len(shell) == 12
    assert graph.number_of_edges() == 24
    assert sorted(dict(graph.degree()).values()) == [4] * 12
    for a in shell:
        assert len(neighbors(root) & neighbors(a)) == 4
    return graph, shell


def feasible_patterns(world: str):
    link, shell = root_link(world)
    shell_set = set(shell)
    for imask in range(1, 1 << 12):
        I = {shell[i] for i in range(12) if (imask >> i) & 1}
        boundary = {
            v
            for v in shell_set - I
            if any(u in I for u in link.neighbors(v))
        }
        free = [v for v in shell if v not in I and v not in boundary]
        for amask in range(1 << len(free)):
            A = set(boundary)
            A.update(free[j] for j in range(len(free)) if (amask >> j) & 1)
            Z = shell_set - I - A
            assert not any(link.has_edge(i, z) for i in I for z in Z)
            yield link, I, A, Z


def row_graph(link: nx.Graph, A: Set[Point], Z: Set[Point]) -> nx.Graph:
    q = link.subgraph(A).copy()
    for a in A:
        q.nodes[a]["label"] = sum(1 for z in link.neighbors(a) if z in Z)
    return q


def completion_graph(link: nx.Graph, A: Set[Point], Z: Set[Point]) -> nx.Graph:
    h = link.subgraph(A | Z).copy()
    for v in h:
        h.nodes[v]["kind"] = "A" if v in A else "Z"
    return h


NODE_ROW = nx.algorithms.isomorphism.categorical_node_match("label", None)
NODE_KIND = nx.algorithms.isomorphism.categorical_node_match("kind", None)


def exact_partition(graph_records, graph_index: int, node_match):
    classes = []
    for record in graph_records:
        g = record[graph_index]
        for cls in classes:
            if nx.is_isomorphic(g, cls[0][graph_index], node_match=node_match):
                cls.append(record)
                break
        else:
            classes.append([record])
    return classes


def classify_row_signature(world: str):
    buckets = collections.defaultdict(list)
    raw = 0
    for link, I, A, Z in feasible_patterns(world):
        q = row_graph(link, A, Z)
        h = completion_graph(link, A, Z)
        qh = nx.weisfeiler_lehman_graph_hash(q, node_attr="label", iterations=8)
        buckets[(len(I), len(Z), qh)].append((q, h, I, A, Z, link))
        raw += 1

    qclasses = []
    ambiguous = []
    for key, records in buckets.items():
        for qclass in exact_partition(records, 0, NODE_ROW):
            hclasses = exact_partition(qclass, 1, NODE_KIND)
            qclasses.append((key, qclass, hclasses))
            if len(hclasses) > 1:
                ambiguous.append((key, qclass, hclasses))

    return raw, qclasses, ambiguous


def z_degree_multiset(record):
    _, _, _, _, Z, link = record
    return tuple(sorted(dict(link.subgraph(Z).degree()).values()))


def enriched_fcc_unique():
    buckets = collections.defaultdict(list)
    raw = 0
    for link, I, A, Z in feasible_patterns("FCC"):
        q = row_graph(link, A, Z)
        h = completion_graph(link, A, Z)
        qh = nx.weisfeiler_lehman_graph_hash(q, node_attr="label", iterations=8)
        delta = tuple(sorted(dict(link.subgraph(Z).degree()).values()))
        buckets[(len(I), len(Z), delta, qh)].append((q, h, I, A, Z, link))
        raw += 1

    class_count = 0
    ambiguity_count = 0
    for records in buckets.values():
        for qclass in exact_partition(records, 0, NODE_ROW):
            class_count += 1
            if len(exact_partition(qclass, 1, NODE_KIND)) > 1:
                ambiguity_count += 1
    return raw, class_count, ambiguity_count


def alignment_index_spectrum(world: str):
    spectrum = collections.Counter()
    raw = 0
    for link, I, A, Z in feasible_patterns(world):
        q = row_graph(link, A, Z)
        h = completion_graph(link, A, Z)

        aut_q = list(
            nx.algorithms.isomorphism.GraphMatcher(
                q, q, node_match=NODE_ROW
            ).isomorphisms_iter()
        )
        aut_h = list(
            nx.algorithms.isomorphism.GraphMatcher(
                h, h, node_match=NODE_KIND
            ).isomorphisms_iter()
        )

        a_order = sorted(A)
        restrictions = {tuple(phi[a] for a in a_order) for phi in aut_h}
        assert len(aut_q) % len(restrictions) == 0
        index = len(aut_q) // len(restrictions)
        spectrum[index] += 1
        raw += 1
    return raw, dict(sorted(spectrum.items()))


def main():
    fcc_raw, fcc_qclasses, fcc_amb = classify_row_signature("FCC")
    hcp_raw, hcp_qclasses, hcp_amb = classify_row_signature("HCP")
    fcc_enriched_raw, fcc_enriched_classes, fcc_enriched_amb = enriched_fcc_unique()
    fcc_align_raw, fcc_alignment = alignment_index_spectrum("FCC")
    hcp_align_raw, hcp_alignment = alignment_index_spectrum("HCP")

    fcc_amb_summary = []
    for key, qclass, hclasses in sorted(fcc_amb, key=lambda x: (x[0][0], x[0][1])):
        outcomes = []
        for hc in hclasses:
            outcomes.append(
                {
                    "raw_realizations": len(hc),
                    "z_degree_multiset": list(z_degree_multiset(hc[0])),
                }
            )
        fcc_amb_summary.append(
            {
                "occupied_shell_count": key[0],
                "new_shell_count": key[1],
                "row_signature_raw_realizations": len(qclass),
                "completion_outcomes": sorted(outcomes, key=lambda x: x["z_degree_multiset"]),
            }
        )

    result = {
        "schema": "R043C7_ROOT_LINK_SHELL_CLASSIFICATION_V1",
        "scope": "exact 12-vertex root-link status classification; no lattice-animal census",
        "edge_common_neighbor_count": {"FCC": 4, "HCP": 4},
        "FCC": {
            "feasible_shell_patterns": fcc_raw,
            "row_signature_exact_classes": len(fcc_qclasses),
            "row_signature_ambiguous_classes": len(fcc_amb),
            "ambiguous_classes": fcc_amb_summary,
            "row_signature_plus_z_degree_multiset_exact_classes": fcc_enriched_classes,
            "row_signature_plus_z_degree_multiset_ambiguous_classes": fcc_enriched_amb,
            "alignment_index_raw_pattern_distribution": {str(k): v for k, v in fcc_alignment.items()},
            "max_alignment_index": max(fcc_alignment),
        },
        "HCP": {
            "feasible_shell_patterns": hcp_raw,
            "row_signature_exact_classes": len(hcp_qclasses),
            "row_signature_ambiguous_classes": len(hcp_amb),
            "alignment_index_raw_pattern_distribution": {str(k): v for k, v in hcp_alignment.items()},
            "max_alignment_index": max(hcp_alignment),
        },
    }

    assert fcc_raw == 8567
    assert hcp_raw == 8657
    assert len(fcc_qclasses) == 230
    assert len(hcp_qclasses) == 681
    assert len(hcp_amb) == 0
    assert len(fcc_amb) == 2
    assert [
        (x["occupied_shell_count"], x["new_shell_count"])
        for x in fcc_amb_summary
    ] == [(1, 4), (1, 5)]
    assert fcc_enriched_raw == 8567
    assert fcc_enriched_classes == 232
    assert fcc_enriched_amb == 0
    assert fcc_align_raw == 8567
    assert hcp_align_raw == 8657
    assert fcc_alignment == {1: 8079, 2: 476, 3: 6, 8: 6}
    assert hcp_alignment == {1: 8301, 2: 305, 3: 6, 4: 27, 8: 18}

    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
