#!/usr/bin/env python3
"""Exact rational BRC fan-in parameter-family certificate.

The local 8-leaf experiment is an EXTERNAL finite sequential decision model.
All P and Q branch masses are positive; signed objectives act only on the
four-coordinate readout. This script uses only exact fractions.
"""
from fractions import Fraction as Q
from itertools import product


ZERO = (Q(0),) * 4
LAM = (Q(20), Q(10), Q(-2), Q(3))
FACET = (Q(1800), Q(900), Q(-208), Q(355))
ALPHA = Q(1, 10)
BETA = Q(4, 5)


def sum_obs(*xs):
    return tuple(sum(column, Q(0)) for column in zip(*xs))


def scalar(x, y):
    return sum((a * b for a, b in zip(x, y)), Q(0))


def stop(q, r, t, declaration):
    assert declaration in ("P", "Q")
    return (q * r if declaration == "Q" else Q(0),
            q if declaration == "P" else Q(0), q * r * t, q * t)


def model(alpha, beta):
    assert Q(0) < alpha < Q(1, 2)
    assert Q(3, 5) < beta < Q(1)
    roots = {"A": (Q(1, 2), Q(1, 2)), "B": (Q(1, 2), Q(3, 2))}
    # node: (conditional Q branch mass, cumulative likelihood ratio, epsilon)
    nodes = {
        "AU": (Q(1, 3), Q(1), alpha),
        "AV": (Q(2, 3), Q(1, 4), Q(0)),
        "BU": (Q(1, 2), Q(1), beta),
        "BV": (Q(1, 2), Q(2), Q(0)),
    }
    leaves = []
    for node, (conditional_q, ratio, epsilon) in nodes.items():
        root_q, _ = roots[node[0]]
        for outcome, factor in enumerate((1 - epsilon, 1 + epsilon)):
            leaf_q = root_q * conditional_q / 2
            leaf_r = ratio * factor
            leaves.append((f"{node}{outcome}", leaf_q, leaf_q * leaf_r, leaf_r))
            assert leaf_q > 0 and leaf_q * leaf_r > 0
    assert sum((q for _, q, _, _ in leaves), Q(0)) == 1
    assert sum((p for _, _, p, _ in leaves), Q(0)) == 1
    for root, (root_q, root_r) in roots.items():
        children = [node for node in nodes if node.startswith(root)]
        assert sum((nodes[k][0] for k in children), Q(0)) == 1
        assert sum((nodes[k][0] * nodes[k][1] for k in children), Q(0)) == root_r
        assert sum((nodes[k][0] * ((1 - nodes[k][2]) + (1 + nodes[k][2])) / 2 * nodes[k][1] for k in children), Q(0)) == root_r
    assert nodes["AU"][1] == nodes["BU"][1] == 1
    return roots, nodes, leaves


def actions_for_node(root, node_name, roots, nodes, compressed):
    conditional_q, r, epsilon = nodes[node_name]
    q = roots[root][0] * conditional_q
    out = [("P", stop(q, r, 2, "P")), ("Q", stop(q, r, 2, "Q"))]
    choices = (("P", "P"), ("Q", "Q")) if compressed and epsilon == 0 else tuple(product("PQ", repeat=2))
    for a, b in choices:
        value = sum_obs(stop(q / 2, r * (1-epsilon), 3, a), stop(q / 2, r * (1+epsilon), 3, b))
        out.append((f"C{a}{b}", value))
    return out


def full_points(roots, nodes):
    choices = {}
    for root in "AB":
        q, r = roots[root]
        choices[root] = [
            (f"{root}:P", stop(q, r, 1, "P")),
            (f"{root}:Q", stop(q, r, 1, "Q")),
        ]
        for left, right in product(actions_for_node(root, root + "U", roots, nodes, False),
                                   actions_for_node(root, root + "V", roots, nodes, False)):
            choices[root].append((f"{root}:{left[0]}/{right[0]}",sum_obs(left[1],right[1])))
    assert len(choices["A"]) == len(choices["B"]) == 38
    raw = [(p[0]+"|"+q[0], sum_obs(p[1], q[1])) for p, q in product(choices["A"], choices["B"])]
    assert len(raw) == 1444
    return raw


def lr_points(roots, nodes):
    # All terminal LR values are distinct across different t2 nodes in the
    # tested parameter grid, except that AV/BV internally duplicate their own R.
    term = {k: {nodes[k][1] * (1-nodes[k][2]), nodes[k][1] * (1+nodes[k][2])} for k in nodes}
    for i, k in enumerate(nodes):
        for h in list(nodes)[i+1:]:
            assert term[k].isdisjoint(term[h]), (k, h, "cross-node t3 collision")
    result = []
    for gate in ("P", "Q", "C"):
        left_gate = [(a, v) for a, v in actions_for_node("A", "AU", roots, nodes, True)
                     if a == gate or (gate == "C" and a.startswith("C"))]
        right_gate = [(a, v) for a, v in actions_for_node("B", "BU", roots, nodes, True)
                      if a == gate or (gate == "C" and a.startswith("C"))]
        options = {}
        for root, gate_choices in (("A", left_gate), ("B", right_gate)):
            q, r = roots[root]
            options[root] = [(root+":P", stop(q,r,1,"P")), (root+":Q",stop(q,r,1,"Q"))]
            for gl, other in product(gate_choices, actions_for_node(root, root+"V", roots, nodes, True)):
                options[root].append((f"{root}:{gl[0]}/{other[0]}", sum_obs(gl[1],other[1])))
        for p, q in product(options["A"], options["B"]):
            result.append((f"gate={gate}; {p[0]}|{q[0]}",sum_obs(p[1],q[1])))
    assert len(result) == 396
    return result


def predicted_gap(beta):
    return min(Q(1,6), (10 * beta - 6) / 4)


def verify(alpha, beta, verbose=False):
    roots, nodes, leaves = model(alpha,beta)
    full = full_points(roots,nodes)
    lr = lr_points(roots,nodes)
    full_min = min((scalar(LAM, v) for _,v in full))
    lr_min = min((scalar(LAM, v) for _,v in lr))
    predicted_full = Q(16,3) + (25 - 10*beta)/4
    predicted_lr = predicted_full + predicted_gap(beta)
    assert full_min == predicted_full
    assert lr_min == predicted_lr
    # Explicit full-history and seedless LR optimizers for the frozen model.
    if alpha == ALPHA and beta == BETA:
        full_witness = sum_obs(
            stop(Q(1,6),Q(1),2,"P"),
            stop(Q(1,3),Q(1,4),2,"Q"),
            stop(Q(1,8),Q(1)-beta,3,"Q"),
            stop(Q(1,8),Q(1)+beta,3,"P"),
            stop(Q(1,4),Q(2),3,"P"),
        )
        lr_witness = sum_obs(
            stop(Q(1,6),Q(1),3,"P"),
            stop(Q(1,3),Q(1,4),2,"Q"),
            stop(Q(1,8),Q(1)-beta,3,"Q"),
            stop(Q(1,8),Q(1)+beta,3,"P"),
            stop(Q(1,4),Q(2),3,"P"),
        )
        assert full_witness == (Q(13,120),Q(13,24),Q(11,4),Q(5,2))
        assert lr_witness == (Q(13,120),Q(13,24),Q(35,12),Q(8,3))
        assert scalar(LAM,full_witness) == full_min == Q(115,12)
        assert scalar(LAM,lr_witness) == lr_min == Q(39,4)
        # A second independent signed objective: exact rational facet normal.
        assert min((scalar(FACET,v) for _,v in lr)) == Q(2045,2)
        assert min((scalar(FACET,v) for _,v in full)) == Q(998)
        assert scalar(FACET, full_witness) == Q(998)
        face = [
            (Q(13,120),Q(13,24),Q(35,12),Q(8,3)),
            (Q(1,40),Q(7,8),Q(5,2),Q(2)),
            (Q(1,12),Q(2,3),Q(5,4),Q(3,2)),
            (Q(11,40),Q(3,8),Q(5,2),Q(2)),
        ]
        assert all(p in {v for _,v in lr} for p in face)
        assert all(scalar(FACET,p)==Q(2045,2) for p in face)
        if verbose:
            print(f"MODEL alpha={alpha} beta={beta} Q/P leaf sums=1/1, all 8 leaves positive")
            for name,q,p,r in leaves:
                print(f"LEAF {name}: Q={q}, P={p}, R={r}")
            print(f"DESCRIPTIONS full={len(full)}, LR={len(lr)}; DISTINCT full={len(set(v for _,v in full))}, LR={len(set(v for _,v in lr))}")
            print(f"LAMBDA {LAM}: V_full={full_min}, V_LR={lr_min}, gap={lr_min-full_min}")
            print(f"FULL O={full_witness}, LR O={lr_witness}")
            print(f"FACET {FACET}: V_full=998, V_LR=2045/2, gap=49/2")
            print(f"FACET: 4 distinct LR support points verified exactly")
    return full_min, lr_min, len(set(v for _,v in full)), len(set(v for _,v in lr))


def main():
    verify(ALPHA,BETA,True)
    cases = [(Q(1,10),Q(31,50)),(Q(1,10),Q(2,3)),(Q(1,10),Q(9,10)),
             (Q(2,5),Q(31,50)), (Q(2,5),Q(2,3)),(Q(2,5),Q(4,5)),(Q(2,5),Q(9,10)), (Q(49,100),Q(601,1000))]
    for a,b in cases:
        f,l,nf,nl = verify(a,b)
        print(f"PARAM a={a}, b={b}: full={f}, LR={l}, gap={l-f}, distinct=({nf},{nl})")
    print("ALL EXACT CHECKS PASSED")

if __name__ == "__main__":
    main()
