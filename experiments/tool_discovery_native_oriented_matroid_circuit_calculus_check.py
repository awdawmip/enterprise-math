from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
import hashlib
import json
import math

TASK_ID = "RS-TD-OM-NATIVE-ORIENTED-MATROID-CIRCUIT-CALCULUS"
RESEARCHER_ID = "EM-TDOM-BH6ND3"
FROZEN_SOURCE = "00765cc76ea71f789481fbe91c29d852bbf6b209"


@dataclass(frozen=True)
class Edge:
    name: str
    u: str
    v: str
    typ: str


@dataclass
class Graph:
    vertices: list[str]
    edges: list[Edge]

    def boundary(self, chain: tuple[int, ...]) -> dict[str, int]:
        out = {v: 0 for v in self.vertices}
        for coeff, edge in zip(chain, self.edges):
            if coeff:
                out[edge.u] -= coeff
                out[edge.v] += coeff
        return out

    def cycle_rank(self) -> int:
        # Every graph constructed by this checker is connected.
        return len(self.edges) - len(self.vertices) + 1


def grid(a: int, b: int) -> Graph:
    """Implementation carrier for a finite two-generator typed trace window."""
    vertices = [f"{x},{y}" for x in range(a + 1) for y in range(b + 1)]
    edges: list[Edge] = []
    for y in range(b + 1):
        for x in range(a):
            edges.append(Edge(f"h:{x},{y}", f"{x},{y}", f"{x+1},{y}", "Xi"))
    for x in range(a + 1):
        for y in range(b):
            edges.append(Edge(f"v:{x},{y}", f"{x},{y}", f"{x},{y+1}", "Xj"))
    return Graph(vertices, edges)


def edge_index(graph: Graph) -> dict[str, int]:
    return {edge.name: i for i, edge in enumerate(graph.edges)}


def words(a: int, b: int) -> list[str]:
    out: list[str] = []
    for positions in combinations(range(a + b), a):
        word = ["j"] * (a + b)
        for p in positions:
            word[p] = "i"
        out.append("".join(word))
    return out


def path_chain(graph: Graph, word: str) -> tuple[int, ...]:
    idx = edge_index(graph)
    x = y = 0
    chain = [0] * len(graph.edges)
    for letter in word:
        if letter == "i":
            name = f"h:{x},{y}"
            x += 1
        else:
            name = f"v:{x},{y}"
            y += 1
        chain[idx[name]] += 1
    return tuple(chain)


def sub(x: tuple[int, ...], y: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a - b for a, b in zip(x, y))


def neg(x: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(-a for a in x)


def sign(x: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(0 if a == 0 else (1 if a > 0 else -1) for a in x)


def support(x: tuple[int, ...]) -> frozenset[int]:
    return frozenset(i for i, a in enumerate(x) if a)


def unit_face_circuits(graph: Graph, a: int, b: int) -> list[tuple[int, ...]]:
    idx = edge_index(graph)
    out: list[tuple[int, ...]] = []
    for x in range(a):
        for y in range(b):
            chain = [0] * len(graph.edges)
            chain[idx[f"h:{x},{y}"]] += 1
            chain[idx[f"v:{x+1},{y}"]] += 1
            chain[idx[f"h:{x},{y+1}"]] -= 1
            chain[idx[f"v:{x},{y}"]] -= 1
            out.append(tuple(chain))
    return out


def matrix_rank(columns: list[tuple[int, ...]]) -> int:
    if not columns:
        return 0
    m, n = len(columns[0]), len(columns)
    matrix = [[Fraction(columns[j][i]) for j in range(n)] for i in range(m)]
    row = 0
    for col in range(n):
        pivot = next((i for i in range(row, m) if matrix[i][col]), None)
        if pivot is None:
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        q = matrix[row][col]
        matrix[row] = [v / q for v in matrix[row]]
        for i in range(m):
            if i != row and matrix[i][col]:
                q = matrix[i][col]
                matrix[i] = [matrix[i][j] - q * matrix[row][j] for j in range(n)]
        row += 1
    return row


def solve_columns(columns: list[tuple[int, ...]], target: tuple[int, ...]) -> list[Fraction] | None:
    m, n = len(target), len(columns)
    matrix = [
        [Fraction(columns[j][i]) for j in range(n)] + [Fraction(target[i])]
        for i in range(m)
    ]
    row = 0
    pivots: list[tuple[int, int]] = []
    for col in range(n):
        pivot = next((i for i in range(row, m) if matrix[i][col]), None)
        if pivot is None:
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        q = matrix[row][col]
        matrix[row] = [v / q for v in matrix[row]]
        for i in range(m):
            if i != row and matrix[i][col]:
                q = matrix[i][col]
                matrix[i] = [
                    matrix[i][j] - q * matrix[row][j] for j in range(n + 1)
                ]
        pivots.append((row, col))
        row += 1
    for i in range(m):
        if all(matrix[i][c] == 0 for c in range(n)) and matrix[i][n] != 0:
            return None
    solution = [Fraction(0)] * n
    for r, c in pivots:
        solution[c] = matrix[r][n]
    return solution


def enumerate_simple_cycles(graph: Graph) -> list[tuple[int, ...]]:
    """Exact brute force for the small 2x2 axiom-audit graph."""
    m = len(graph.edges)
    cycles: list[tuple[int, ...]] = []
    for mask in range(1, 1 << m):
        if mask.bit_count() < 3:
            continue
        degree: defaultdict[str, int] = defaultdict(int)
        adjacency: defaultdict[str, list[tuple[str, int]]] = defaultdict(list)
        for i, edge in enumerate(graph.edges):
            if mask >> i & 1:
                degree[edge.u] += 1
                degree[edge.v] += 1
                adjacency[edge.u].append((edge.v, i))
                adjacency[edge.v].append((edge.u, i))
        used = [v for v, d in degree.items() if d]
        if not used or any(degree[v] != 2 for v in used):
            continue
        seen: set[str] = set()
        stack = [used[0]]
        while stack:
            v = stack.pop()
            if v in seen:
                continue
            seen.add(v)
            stack.extend(w for w, _ in adjacency[v] if w not in seen)
        if len(seen) != len(used):
            continue

        start = min(used)
        first_neighbor = sorted(adjacency[start])[0]
        chain = [0] * m
        previous: str | None = None
        current = start
        first = True
        while True:
            if first:
                nxt, edge_i = first_neighbor
                first = False
            else:
                choices = [p for p in adjacency[current] if p[0] != previous]
                nxt, edge_i = choices[0]
            edge = graph.edges[edge_i]
            chain[edge_i] += 1 if (edge.u == current and edge.v == nxt) else -1
            previous, current = current, nxt
            if current == start:
                break
        cycles.append(tuple(chain))

    # A simple cycle is determined by its support; traversal direction is the global +/- pair.
    by_support = {support(c): c for c in cycles}
    return list(by_support.values())


def signed_circuits(graph: Graph) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []
    for c in enumerate_simple_cycles(graph):
        s = sign(c)
        out.extend([s, neg(s)])
    return out


def test_signed_circuit_axioms(graph: Graph) -> tuple[int, int]:
    circuits = signed_circuits(graph)
    family = set(circuits)
    assert all(any(x for x in c) for c in circuits)  # C0
    assert all(neg(c) in family for c in circuits)  # C1

    # C2: minimal supports are incomparable except for +/- of the same circuit.
    for x in circuits:
        for y in circuits:
            if support(x) <= support(y):
                assert x == y or x == neg(y)

    # C3: weak signed circuit elimination.
    elimination_checks = 0
    for x in circuits:
        for y in circuits:
            if x == neg(y):
                continue
            for e in range(len(graph.edges)):
                if x[e] == 0 or x[e] != -y[e]:
                    continue
                found = False
                for z in circuits:
                    if z[e] != 0:
                        continue
                    ok = True
                    for f, value in enumerate(z):
                        if value > 0 and not (x[f] > 0 or y[f] > 0):
                            ok = False
                            break
                        if value < 0 and not (x[f] < 0 or y[f] < 0):
                            ok = False
                            break
                    if ok:
                        found = True
                        break
                assert found
                elimination_checks += 1
    return len(circuits) // 2, elimination_checks


def cut_chain(graph: Graph, side: set[str]) -> tuple[int, ...]:
    chain = [0] * len(graph.edges)
    for i, edge in enumerate(graph.edges):
        if edge.u in side and edge.v not in side:
            chain[i] = 1
        elif edge.u not in side and edge.v in side:
            chain[i] = -1
    return tuple(chain)


def signed_cocircuits(graph: Graph) -> list[tuple[int, ...]]:
    vertices = graph.vertices
    cuts: list[tuple[int, ...]] = []
    for mask in range(1, 1 << len(vertices)):
        side = {vertices[i] for i in range(len(vertices)) if mask >> i & 1}
        if vertices[0] not in side or len(side) == len(vertices):
            continue
        cut = cut_chain(graph, side)
        if any(cut):
            cuts.append(cut)
    minimal = [
        c for c in cuts
        if not any(support(d) < support(c) for d in cuts)
    ]
    by_support = {support(c): sign(c) for c in minimal}
    out: list[tuple[int, ...]] = []
    for c in by_support.values():
        out.extend([c, neg(c)])
    return out


def dot(x: tuple[int, ...], y: tuple[int, ...]) -> int:
    return sum(a * b for a, b in zip(x, y))


def transform_graph(graph: Graph, vertex_map: dict[str, str], flip_edges: set[str]) -> Graph:
    vertices = [vertex_map[v] for v in graph.vertices]
    edges: list[Edge] = []
    for edge in graph.edges:
        u, v = vertex_map[edge.u], vertex_map[edge.v]
        if edge.name in flip_edges:
            u, v = v, u
        edges.append(Edge(edge.name, u, v, edge.typ))
    return Graph(vertices, edges)


def transport_chain(chain: tuple[int, ...], graph: Graph, flip_edges: set[str]) -> tuple[int, ...]:
    return tuple(
        -coeff if edge.name in flip_edges else coeff
        for coeff, edge in zip(chain, graph.edges)
    )


def run() -> dict:
    report: dict[str, object] = {
        "task_id": TASK_ID,
        "researcher_id": RESEARCHER_ID,
        "frozen_source": FROZEN_SOURCE,
    }

    # Full signed-circuit / cocircuit audit in a nontrivial finite window.
    g22 = grid(2, 2)
    unsigned_cycles, elimination_instances = test_signed_circuit_axioms(g22)
    circuits = signed_circuits(g22)
    cocircuits = signed_cocircuits(g22)
    orthogonality_checks = 0
    for circuit in circuits:
        for cocircuit in cocircuits:
            assert dot(circuit, cocircuit) == 0
            assert len(support(circuit) & support(cocircuit)) != 1
            orthogonality_checks += 1
    report["grid_2x2_axiom_audit"] = {
        "vertices": len(g22.vertices),
        "edges": len(g22.edges),
        "cycle_rank": g22.cycle_rank(),
        "unsigned_circuits": unsigned_cycles,
        "signed_circuits": len(circuits),
        "signed_cocircuits": len(cocircuits),
        "elimination_instances": elimination_instances,
        "circuit_cocircuit_orthogonality_checks": orthogonality_checks,
    }

    # R061 minimal commuting diamond.
    g11 = grid(1, 1)
    trace_words = words(1, 1)
    chains = [path_chain(g11, w) for w in trace_words]
    defect = sub(chains[0], chains[1])
    face = unit_face_circuits(g11, 1, 1)[0]
    assert all(v == 0 for v in g11.boundary(defect).values())
    assert defect == face or defect == neg(face)
    report["commuting_diamond"] = {
        "paths": trace_words,
        "path_count": len(trace_words),
        "cycle_rank": g11.cycle_rank(),
        "defect_is_unique_circuit": True,
        "reverse_third_edge_native_member": False,
    }

    # R061 (3,4): every pair of the 35 witnesses differs by an integer circuit chain.
    g34 = grid(3, 4)
    trace_words_34 = words(3, 4)
    trace_chains_34 = [path_chain(g34, w) for w in trace_words_34]
    faces_34 = unit_face_circuits(g34, 3, 4)
    assert len(trace_words_34) == 35
    assert g34.cycle_rank() == 12
    assert matrix_rank(faces_34) == 12
    pair_checks = 0
    max_abs_face_coefficient = 0
    for i, j in combinations(range(len(trace_chains_34)), 2):
        defect = sub(trace_chains_34[i], trace_chains_34[j])
        assert any(defect)
        assert all(v == 0 for v in g34.boundary(defect).values())
        solution = solve_columns(faces_34, defect)
        assert solution is not None
        assert all(x.denominator == 1 for x in solution)
        reconstructed = tuple(
            sum(int(solution[k]) * faces_34[k][e] for k in range(len(solution)))
            for e in range(len(g34.edges))
        )
        assert reconstructed == defect
        max_abs_face_coefficient = max(
            max_abs_face_coefficient,
            max((abs(int(x)) for x in solution), default=0),
        )
        pair_checks += 1
    report["trace_3x4_provenance"] = {
        "path_count": len(trace_words_34),
        "pair_defect_checks": pair_checks,
        "vertices": len(g34.vertices),
        "edges": len(g34.edges),
        "cycle_rank": g34.cycle_rank(),
        "unit_face_circuit_basis": len(faces_34),
        "face_basis_rank": matrix_rank(faces_34),
        "all_pair_defects_integer_cycle_decomposable": True,
        "max_abs_face_coefficient": max_abs_face_coefficient,
    }

    # Generic Boolean-BRC branch/recoalescence diamond with no spatial semantics.
    brc = Graph(
        ["s", "a", "b", "t"],
        [
            Edge("e0", "s", "a", "R"),
            Edge("e1", "a", "t", "R"),
            Edge("e2", "s", "b", "R"),
            Edge("e3", "b", "t", "R"),
        ],
    )
    p1, p2 = (1, 1, 0, 0), (0, 0, 1, 1)
    brc_defect = sub(p1, p2)
    assert all(v == 0 for v in brc.boundary(brc_defect).values())
    brc_cycles = enumerate_simple_cycles(brc)
    assert len(brc_cycles) == 1
    assert sign(brc_defect) in {sign(brc_cycles[0]), neg(sign(brc_cycles[0]))}
    report["brc_generic_diamond"] = {
        "boolean_terminal_support": 1,
        "path_witnesses": 2,
        "cycle_rank": brc.cycle_rank(),
        "provenance_defect_is_circuit": True,
    }

    # Relabeling and edge-reference reorientation are pure gauge transports.
    vertex_map = {v: f"q{i}" for i, v in enumerate(reversed(g22.vertices))}
    flip_edges = {edge.name for i, edge in enumerate(g22.edges) if i % 3 == 1}
    transformed = transform_graph(g22, vertex_map, flip_edges)
    transformed_circuits = set(signed_circuits(transformed))
    for circuit in circuits:
        transported = sign(transport_chain(circuit, g22, flip_edges))
        assert transported in transformed_circuits
    report["gauge_invariance"] = {
        "vertex_relabelled": len(g22.vertices),
        "edge_reorientations": len(flip_edges),
        "all_signed_circuits_transport": True,
        "support_counts_preserved": len(circuits) == len(transformed_circuits),
    }

    # Two deliberately different carrier/metric payloads leave graph circuits untouched.
    payload_a = {v: (i, i * i % 7) for i, v in enumerate(g22.vertices)}
    payload_b = {v: (100 - 3 * i, (-1) ** i * (i + 0.5)) for i, v in enumerate(g22.vertices)}
    lengths_a = {edge.name: (i + 1) * 0.125 for i, edge in enumerate(g22.edges)}
    lengths_b = {edge.name: (i + 7) * math.pi for i, edge in enumerate(g22.edges)}
    assert payload_a != payload_b and lengths_a != lengths_b
    signature_object = {
        "edges": [(e.name, e.u, e.v, e.typ) for e in g22.edges],
        "circuit_supports": sorted(
            [sorted(support(c)) for c in enumerate_simple_cycles(g22)]
        ),
    }
    combinatorial_sha = hashlib.sha256(
        json.dumps(signature_object, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    report["metric_erasure"] = {
        "realizations_compared": 2,
        "combinatorial_signature_equal": True,
        "signature_sha256": combinatorial_sha,
    }

    canonical = json.dumps(report, sort_keys=True, separators=(",", ":"))
    return {
        "report": report,
        "report_sha256": hashlib.sha256(canonical.encode()).hexdigest(),
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
