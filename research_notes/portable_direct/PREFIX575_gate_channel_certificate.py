#!/usr/bin/env python3
"""PREFIX-575-GC: companion rank-one gate channel and Perron response.

Reconstructs the frozen four-STAR native X6-BRC observer from the exact
96-port/6-action source semantics. It verifies the rank-one gate update,
the 17-state two-step transfer channel, the Q14 gate derivative, and the
finite support certificate used by the Perron-Frobenius argument.

Dependencies: Python 3 and SymPy. No floating-point arithmetic.
The Q14 irreducibility theorem is reused from PREFIX-574's published
Rabin certificate at the same frozen science pin; this script checks the
reconstructed Q14 hash against that exact prior certificate.
"""
from collections import Counter, deque
from itertools import product
import hashlib
import json
import sympy as S

PIN = "f42f2906d77f24085c123f3ccfe9667d41caa96d"
PREFIX574_Q14_SHA256 = "d258201370bd030e081aefec6c538dbea1abfc69712798080583a842ce66643e"
STARS = ((1, 3, 6), (1, 4, 5), (2, 3, 5), (2, 4, 6))
ACTIONS = tuple(product(range(3), (0, 1)))
ZERO_ROOT = (0,) * 6
ROOTS = (ZERO_ROOT,) + tuple(
    tuple(sign if j == axis else 0 for j in range(6))
    for axis in range(4) for sign in (-1, 1)
)

def near(star, current):
    return tuple((-1 if current > 0 else 1) * k
                 for k in STARS[star] if k != abs(current))

PHASES = tuple(
    (a, prev, sign * k)
    for a in range(4)
    for k in STARS[a]
    for sign in (-1, 1)
    for prev in near(a, sign * k)
)
PHASE_INDEX = {phase: i for i, phase in enumerate(PHASES)}

def successors(phase):
    a, prev, current = PHASES[phase]
    b = next(b for b in range(4)
             if b != a and abs(current) in STARS[b])
    targets = (
        [(a, current, k) for k in near(a, current) if k != prev]
        + [(b, current, k) for k in near(b, current)]
    )
    return tuple(PHASE_INDEX[t] for t in targets)

NEXT = tuple(successors(i) for i in range(48))
TARGET = PHASE_INDEX[(0, 1, -3)]

def sign_on_axis(phase, axis):
    current = PHASES[phase][2]
    return (1 if current > 0 else -1) if abs(current) == axis else 0

def native_edge(port, action, root):
    phase, bit = divmod(port, 2)
    slot, new_bit = action
    nxt = NEXT[phase][slot]
    weights = []
    for axis in range(1, 7):
        left = sign_on_axis(phase, axis)
        right = sign_on_axis(nxt, axis)
        r = root[axis - 1]
        value = abs(left) + abs(right) - abs(right - r) + abs(left - r)
        assert value in (0, 2)
        weights.append(value // 2)
    gate = int(bit == new_bit == 1 and nxt == TARGET)
    return 2 * nxt + new_bit, tuple(weights) + (gate,)

def native_rows(root):
    return [
        Counter((target, weights[4], weights[5], weights[6])
                for action in ACTIONS
                for target, weights in [native_edge(port, action, root)])
        for port in range(96)
    ]

def weighted_quotient(rows):
    ids = [0] * len(rows)
    growth = [1]
    for _ in range(len(rows)):
        keys = []
        for row in rows:
            out = Counter()
            for (target, a, b, gate), multiplicity in row.items():
                out[(ids[target], a, b, gate)] += multiplicity
            keys.append(tuple(sorted(out.items())))
        lookup = {}
        new_ids = [lookup.setdefault(key, len(lookup)) for key in keys]
        if new_ids == ids:
            break
        ids = new_ids
        growth.append(len(lookup))
    else:
        raise AssertionError("weighted quotient did not stabilize")
    quotient = {}
    for i, row in enumerate(rows):
        out = Counter()
        for (target, a, b, gate), multiplicity in row.items():
            out[(ids[target], a, b, gate)] += multiplicity
        if ids[i] in quotient:
            assert quotient[ids[i]] == out
        else:
            quotient[ids[i]] = out
    return ids, tuple(quotient[i] for i in range(len(quotient))), growth

def bfs(graph, start):
    distance = {start: 0}
    todo = deque([start])
    while todo:
        i = todo.popleft()
        for j in graph[i]:
            if j not in distance:
                distance[j] = distance[i] + 1
                todo.append(j)
    return distance

def all_coefficients_nonnegative(matrix, variables):
    for entry in matrix:
        if any(c < 0 for c in S.Poly(entry, *variables).coeffs()):
            return False
    return True

def main():
    assert len(PHASES) == 48 and len(ACTIONS) == 6 and len(ROOTS) == 9
    rows = native_rows(ZERO_ROOT)
    for root in ROOTS:
        assert native_rows(root) == rows

    ids, quotient, growth = weighted_quotient(rows)
    assert len(ids) == 96
    assert len(quotient) == 37
    assert growth == [1, 4, 13, 21, 33, 37]

    adjacency = [set() for _ in quotient]
    gate_edges = []
    for i, row in enumerate(quotient):
        for (j, ax, ay, gate), multiplicity in row.items():
            if multiplicity:
                adjacency[i].add(j)
            if gate:
                gate_edges.append((i, j, multiplicity))
    assert gate_edges == [(4, 5, 1), (15, 5, 1), (17, 5, 1)]

    # Exact 17/20 bipartition of the directed support.
    undirected = [set(v) for v in adjacency]
    for i, out in enumerate(adjacency):
        for j in out:
            undirected[j].add(i)
    color = [None] * 37
    for start in range(37):
        if color[start] is not None:
            continue
        color[start] = 0
        todo = deque([start])
        while todo:
            i = todo.popleft()
            for j in undirected[i]:
                if color[j] is None:
                    color[j] = color[i] ^ 1
                    todo.append(j)
                else:
                    assert color[j] != color[i]
    left = [i for i in range(37) if color[i] == 0]
    right = [i for i in range(37) if color[i] == 1]
    assert (len(left), len(right)) == (17, 20)
    li = {state: i for i, state in enumerate(left)}
    ri = {state: i for i, state in enumerate(right)}

    x, y, z, lam, u, v = S.symbols("x y z L u v")
    A = S.zeros(17, 20)
    B = S.zeros(20, 17)
    for i, row in enumerate(quotient):
        for (j, ax, ay, gate), multiplicity in row.items():
            term = multiplicity * x**ax * y**ay * z**gate
            if color[i] == 0:
                A[li[i], ri[j]] += term
            else:
                B[ri[i], li[j]] += term

    # The three gate edges share one left target, hence B's gate part is rank one.
    gate_source_positions = [ri[i] for i in (4, 15, 17)]
    target_position = li[5]
    gate_input = S.zeros(20, 1)
    for pos in gate_source_positions:
        gate_input[pos, 0] = 1
    gate_output = S.zeros(17, 1)
    gate_output[target_position, 0] = 1

    B0 = B.subs(z, 0)
    assert all(e == 0 for e in (B - B0 - z * gate_input * gate_output.T))
    P0 = A * B0
    gate_vector = A * gate_input
    Pz = A * B
    assert all(S.simplify(e) == 0
               for e in (Pz - P0 - z * gate_vector * gate_output.T))

    # The gate transfer function is c (lambda I - P0)^(-1) b.
    c_b = (gate_output.T * gate_vector)[0]
    c_P_b = (gate_output.T * P0 * gate_vector)[0]
    assert S.expand(c_b) == 0
    assert S.expand(c_P_b - 4 * (2 * (x + y) + 1)) == 0

    # Reconstruct the exact 17x17 characteristic polynomial and Q14.
    chi = (A * B).charpoly(lam).as_expr()
    symmetric_chi = 0
    for (degree_lam, degree_z), coefficient in S.Poly(chi, lam, z).terms():
        symmetric, remainder, symbols = S.symmetrize(coefficient, [x, y], formal=True)
        assert remainder == 0
        symmetric_chi += (
            symmetric.subs({symbols[0][0]: u, symbols[1][0]: v})
            * lam**degree_lam * z**degree_z
        )
    symmetric_chi = S.expand(symmetric_chi)
    Q3 = lam**3 + 4*lam**2 - (32*u + 16*v)*lam + 192*v
    q14, remainder = S.div(S.Poly(symmetric_chi, lam), S.Poly(Q3, lam))
    assert remainder.is_zero
    Q14_expr = S.expand(q14.as_expr())
    q14_text = str(Q14_expr)
    q14_sha256 = hashlib.sha256(q14_text.encode("utf-8")).hexdigest()
    assert q14_sha256 == PREFIX574_Q14_SHA256

    Q14_poly = S.Poly(Q14_expr, lam, u, v, z)
    assert Q14_poly.degree(lam) == 14 and Q14_poly.degree(z) == 1
    Q0_expr = S.expand(Q14_expr.subs(z, 0))
    Qz_expr = S.expand(S.diff(Q14_expr, z))
    Q0 = S.Poly(Q0_expr, lam, u, v)
    Qz = S.Poly(Qz_expr, lam, u, v)
    assert Q0.degree(lam) == 14 and Q0.LC() == 1
    assert Qz.degree(lam) == 12
    qz_l12 = S.Poly(Qz_expr, lam).nth(12)
    assert S.expand(qz_l12 + 4*(2*u + 1)) == 0

    # Exact support certificate for P(z): 17 vertices, strongly connected.
    P_support = [set() for _ in range(17)]
    for i in range(17):
        for j in range(17):
            if S.Poly(Pz[i, j], x, y, z).as_expr() != 0:
                P_support[i].add(j)
    P0_support = [set() for _ in range(17)]
    for i in range(17):
        for j in range(17):
            if P0[i, j] != 0:
                P0_support[i].add(j)
    assert P0_support == P_support
    P_reverse = [set() for _ in range(17)]
    for i, out in enumerate(P_support):
        for j in out:
            P_reverse[j].add(i)
    forward = bfs(P_support, 0)
    backward = bfs(P_reverse, 0)
    assert len(forward) == len(backward) == 17
    assert sum(len(s) for s in P_support) == 117
    assert max(forward.values()) == max(backward.values()) == 2

    # P0 and the gate input are nonnegative polynomial matrices/vectors.
    assert all_coefficients_nonnegative(A, (x, y))
    assert all_coefficients_nonnegative(B0, (x, y))
    assert all_coefficients_nonnegative(P0, (x, y))
    assert all_coefficients_nonnegative(gate_vector, (x, y))

    q0_text = str(Q0_expr)
    qz_text = str(Qz_expr)
    return {
        "workstream_id": "PREFIX-575-GC",
        "parallel_canonical_prefix575": {
            "commit": "61b08d67197f4422fa0d8ac1c197f608e09b69af",
            "observer": "q1=q2=q3=q4=q5=q6=1; gate count retained",
            "relationship": "distinct observer; companion result; not superseding"
        },
        "status": "ALL_CHECKS_PASS",
        "science_pin": PIN,
        "source_model": "frozen four-STAR native X6-BRC; 96 ordered ports; 6 actions; 9 roots",
        "weighted_quotient": {
            "native_ports": 96,
            "classes": 37,
            "partition_growth": growth,
            "bipartition": [17, 20]
        },
        "gate_edges": [
            {"source": i, "target": j, "multiplicity": m}
            for i, j, m in gate_edges
        ],
        "rank_one_two_step_update": {
            "right_block_gate_source_positions": gate_source_positions,
            "left_block_gate_target_position": target_position,
            "B_equals_B0_plus_z_u_c": True,
            "P_equals_P0_plus_z_b_c": True,
            "rank": 1,
            "P0_nonzero_entries": sum(1 for e in P0 if e != 0),
            "gate_vector_nonzero_entries": sum(1 for e in gate_vector if e != 0)
        },
        "P_support_certificate": {
            "vertices": 17,
            "directed_edges": sum(len(s) for s in P_support),
            "forward_reachable_from_0": len(forward),
            "reverse_reachable_to_0": len(backward),
            "max_forward_distance": max(forward.values()),
            "max_reverse_distance": max(backward.values()),
            "irreducible_for_positive_x_y_z": True,
            "P0_same_support_as_Pz": True
        },
        "Q14": {
            "degree_lambda": 14,
            "degree_z": 1,
            "nonzero_terms": len(Q14_poly.terms()),
            "sha256": q14_sha256,
            "irreducibility_reused_from": "PREFIX-574 / Q14 irreducible over Q(u,v,z) by Rabin certificate"
        },
        "gate_transfer": {
            "identity": "H(lambda) = c*(lambda*I-P0)^(-1)*b = -Qz(lambda)/Q0(lambda)",
            "denominator_degree": Q0.degree(lam),
            "denominator_terms": len(Q0.terms()),
            "denominator_sha256": hashlib.sha256(q0_text.encode("utf-8")).hexdigest(),
            "numerator_degree": Qz.degree(lam),
            "numerator_terms": len(Qz.terms()),
            "numerator_sha256": hashlib.sha256(qz_text.encode("utf-8")).hexdigest(),
            "numerator_leading_coefficient": str(S.factor(qz_l12)),
            "coprime": True,
            "coprime_reason": "A common nonconstant factor of Q14(lambda,0) and dQ14/dz would divide Q14 over Q(u,v,z), contradicting irreducibility."
        },
        "markov_parameters": {
            "c_b": str(c_b),
            "c_P0_b": "4*(2*u+1)",
            "relative_degree_in_two_step_operator": 2,
            "high_frequency_leading_term": "4*(2*u+1)/lambda^2"
        },
        "generic_positive_realization_dimension": {
            "linear_minimum": 14,
            "positive_upper_bound": 17,
            "unresolved_exact_minimum": [14, 15, 16, 17]
        },
        "Perron_gate_sensitivity": {
            "P_nonnegative_for_positive_x_y_z": True,
            "P_irreducible_for_positive_x_y_z": True,
            "gate_update_nonzero_nonnegative_rank_one": True,
            "rho_derivative": "left^T*(b*c)*right/(left^T*right) > 0"
        },
        "exact_polynomials": {
            "Q14_sha256": q14_sha256,
            "Q0_sha256": hashlib.sha256(q0_text.encode("utf-8")).hexdigest(),
            "Qz_sha256": hashlib.sha256(qz_text.encode("utf-8")).hexdigest(),
            "Q3": str(Q3)
        }
    }

if __name__ == "__main__":
    print(json.dumps(main(), ensure_ascii=False, indent=2))
