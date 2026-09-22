"""Exact new p17/order1/r1 support problem; no old task claim or acceptance.

Reuses the pinned BRC arithmetic and exact Gram-Schmidt utilities. The search
has two candidates at each level and carries exact signed side budgets.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE.joinpath("dependencies")))
import p19_order9 as exact

R = exact.Rat


def pack(q):
    return [str(q.n), str(q.d)]


def greater(a, b):
    return a.n * b.d > b.n * a.d


def solve_modular(a, b, modulus):
    rows = [list(row) + [value] for row, value in zip(a, b)]
    size = len(rows)
    for k in range(size):
        pivot = next(i for i in range(k, size) if exact.rem(rows[i][k], 17))
        rows[k], rows[pivot] = rows[pivot], rows[k]
        inverse = exact.inv(rows[k][k], modulus)
        rows[k] = [exact.rem(x * inverse, modulus) for x in rows[k]]
        for i in range(size):
            if i != k:
                factor = rows[i][k]
                rows[i] = [exact.rem(x - factor * y, modulus) for x, y in zip(rows[i], rows[k])]
    assert all(rows[i][j] == int(i == j) for i in range(size) for j in range(size))
    return [row[-1] for row in rows]


def prepare():
    raw = BASE.joinpath("dependencies", "p17_q0_certificate.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == "fdf0b060d47bccd5b2a5095dc4b72d13b68476f49494eb4435b0b50dd30c65f6"
    old = json.loads(raw)
    basis = old["weighted_basis"]
    weights = [17 * j - 1 for j in range(1, 17)]
    unweighted = [[exact.exact(x, w) for x, w in zip(row, weights)] for row in basis]
    assert abs(exact.determinant(unweighted)) == 17 ** 21
    for k in range(1, 7):
        m = 17 ** k
        coeff = [exact.inv(j ** k, m) for j in range(1, 17)]
        assert all(exact.rem(exact.dot(row, coeff), m) == 0 for row in unweighted)
    unit_minor = [[exact.inv(j ** k, 17) for j in range(1, 7)] for k in range(1, 7)]
    assert exact.rem(exact.determinant(unit_minor), 17) != 0
    norms, projectors = exact.gram_schmidt(basis)
    assert [q.pair() for q in norms] == old["gram_schmidt_squared"]
    radius = 2026 ** 2 + 2331 ** 2
    assert radius == 9538237
    assert all(q.n > radius * q.d for q in norms)
    modulus = 17 ** 6
    matrix = [[exact.inv(j ** k, modulus) for j in range(1, 7)] for k in range(1, 7)]
    target = [-exact.inv(18 ** k, modulus) for k in range(1, 7)]
    u0 = solve_modular(matrix, target, modulus) + [0] * 10
    for k in range(1, 7):
        m = 17 ** k
        assert exact.rem(sum(u * exact.inv(j ** k, m) for j, u in enumerate(u0, 1)) + exact.inv(18 ** k, m), m) == 0
    x0 = [u * w for u, w in zip(u0, weights)]
    mu = [[sum(x * q for x, q in zip(row, projector)) for projector in projectors] for row in basis]
    # Reduce this representative by a lattice vector only to keep its numbers
    # small. This step does not discard any member of the affine coset.
    for i in range(15, -1, -1):
        center = sum(x * q for x, q in zip(x0, projectors[i]))
        n = exact.qr(2 * center.n + center.d, 2 * center.d)[0]
        x0 = [x - n * b for x, b in zip(x0, basis[i])]
    u0 = [exact.exact(x, w) for x, w in zip(x0, weights)]
    centers = [sum(x * q for x, q in zip(x0, projector)) for projector in projectors]
    portable = {
        "schema": "T6_P17_R1_PORTABLE_INPUT_V1",
        "scope": "Direct-user finite support problem; existing global T6 Task remains awaiting independent review",
        "prime": "17", "residue": "1", "vertical_order": "1",
        "dimension": 16, "degree": 6,
        "positive_vertical_denominator": "306", "positive_vertical_mass": "305",
        "q0_positive_budget": "2026", "q0_negative_budget": "2331",
        "radius_squared": str(radius), "weights": [str(w) for w in weights],
        "weighted_basis": [[str(x) for x in row] for row in basis],
        "unweighted_basis": [[str(x) for x in row] for row in unweighted],
        "particular_q0": [str(x) for x in u0],
        "weighted_particular": [str(x) for x in x0],
        "gram_schmidt_squared": [pack(q) for q in norms],
        "mu": [[pack(q) for q in row] for row in mu],
        "centers": [pack(q) for q in centers],
        "source_q0_sha256": hashlib.sha256(raw).hexdigest(),
        "arithmetic_dependency_sha256": hashlib.sha256(BASE.joinpath("dependencies", "p19_order9.py").read_bytes()).hexdigest(),
        "tree_node_bound_including_root": "131071",
        "integer_encoding": "All mathematical integers are decimal strings; do not parse them as IEEE-754 Number",
    }
    return portable, basis, weights, x0, norms, mu, centers


def run(max_seconds):
    started = time.monotonic()
    portable, basis, weights, x0, norms, mu, centers = prepare()
    portable_bytes = (json.dumps(portable, indent=2) + "\n").encode()
    BASE.joinpath("portable_input.json").write_bytes(portable_bytes)
    chosen = [0] * 16
    nodes = []
    kernel = None
    timed_out = False
    leaves = 0

    def visit(level, partial):
        nonlocal kernel, timed_out, leaves
        if time.monotonic() - started >= max_seconds:
            timed_out = True
            return None
        index = len(nodes)
        assert index < 131071
        center = centers[level] + sum(chosen[j] * mu[j][level] for j in range(level + 1, 16))
        quotient, remainder = exact.qr(center.n, center.d)
        node = {"id": index, "level": level, "center": pack(center),
                "partial_before": pack(partial),
                "floor_witness": {"numerator": str(center.n), "denominator": str(center.d),
                                  "quotient": str(quotient), "remainder": str(remainder)}, "options": []}
        nodes.append(node)
        for candidate in (-quotient - 1, -quotient):
            chosen[level] = candidate
            error = center + candidate
            term = error * error * norms[level]
            total = partial + term
            option = {"coefficient": str(candidate), "squared_component": pack(term), "partial_after": pack(total)}
            node["options"].append(option)
            if greater(total, R(9538237)):
                option["decision"] = "PRUNE_EXACT_SQUARED_NORM"
            elif level:
                option["decision"] = "DESCEND"
                option["child"] = visit(level - 1, total)
                if timed_out or kernel is not None:
                    return index
            else:
                leaves += 1
                weighted = [x0[t] + sum(chosen[i] * basis[i][t] for i in range(16)) for t in range(16)]
                assert sum(x * x for x in weighted) * total.d == total.n
                pos = sum(max(0, x) for x in weighted)
                neg = sum(max(0, -x) for x in weighted)
                option.update(positive_q0_mass=str(pos), negative_q0_mass=str(neg))
                if pos <= 2026 and neg <= 2331:
                    u = [exact.exact(x, w) for x, w in zip(weighted, weights)]
                    for k in range(1, 7):
                        m = 17 ** k
                        assert exact.rem(sum(a * exact.inv(j ** k, m) for j, a in enumerate(u, 1)) + exact.inv(18 ** k, m), m) == 0
                    kernel = {"q0": [str(x) for x in u], "positive_total_mass": str(pos + 305), "negative_total_mass": str(neg)}
                    option["decision"] = "MODULAR_KERNEL_FOUND"
                else:
                    option["decision"] = "PRUNE_EXACT_SIDE_BUDGET"
        return index

    root = visit(15, R(0))
    result = {"schema": "T6_P17_R1_TWO_BRANCH_CERTIFICATE_V1",
              "status": "MODULAR_KERNEL_FOUND" if kernel else "RESOURCE_LIMIT_UNDETERMINED" if timed_out else "R1_AFFINE_CLASS_EMPTY",
              "root": root, "nodes": nodes, "node_count": len(nodes), "full_leaves": leaves,
              "kernel": kernel, "portable_input_sha256": hashlib.sha256(portable_bytes).hexdigest(),
              "solver_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "brc_evaluations": exact.TRACE_COUNT, "trace_samples": exact.TRACE_SAMPLES,
              "elapsed_seconds": time.monotonic() - started,
              "authority": "Direct-user finite support; no old Task claim, no Driver acceptance, no global T6 conclusion"}
    BASE.joinpath("certificate.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({k: v for k, v in result.items() if k not in {"nodes", "trace_samples"}}), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-seconds", type=int, default=180)
    args = parser.parse_args()
    run(args.max_seconds)
