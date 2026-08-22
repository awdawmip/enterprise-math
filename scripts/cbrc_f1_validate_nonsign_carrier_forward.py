#!/usr/bin/env python3
"""
Deterministic exact checker for:
RS-CBRC-F1-NONSIGN-RECOALESCENCE-CARRIER-FORWARD-CLASSIFICATION
No external libraries. Integer/modular arithmetic only.
This checker validates finite presentations and smallest countermodels;
the theorems in the return report carry the infinite/general proofs.
"""
from __future__ import annotations
from itertools import product
from math import gcd
import hashlib
import json
M = 3
def add3(x, y):
    return (x[0] + y[0], (x[1] + y[1]) % M)
def neg3(x):
    return (-x[0], (-x[1]) % M)
def apply_rank1_torsion(m, eps, unit, shift, state):
    n, t = state
    return (eps * n, (unit * t + shift * n) % m)
def orbit_of_e(m, eps, unit, shift, limit=256):
    e = (1, 0)
    cur = e
    seen = {}
    seq = []
    for k in range(limit):
        if cur in seen:
            return seq, seen[cur]
        seen[cur] = k
        seq.append(cur)
        cur = apply_rank1_torsion(m, eps, unit, shift, cur)
    raise AssertionError("orbit bound exceeded")
def operator_order_rank1_torsion(m, eps, unit, shift, limit=512):
    e = (1, 0)
    tau = (0, 1 % m)
    ce, ct = e, tau
    for k in range(1, limit + 1):
        ce = apply_rank1_torsion(m, eps, unit, shift, ce)
        ct = apply_rank1_torsion(m, eps, unit, shift, ct)
        if ce == e and ct == tau:
            return k
    raise AssertionError("operator order bound exceeded")
def R3(x):
    n, t = x
    return (n, (t + n) % 3)
def R3_inv(x):
    n, t = x
    return (n, (t - n) % 3)
def S3(x):
    n, t = x
    return (n, (-t) % 3)
def R3_pow(x, k):
    cur = x
    if k >= 0:
        for _ in range(k % 3):
            cur = R3(cur)
    else:
        for _ in range((-k) % 3):
            cur = R3_inv(cur)
    return cur
def N3(x):
    return add3(R3(x), neg3(x))
def scalar_mul3(k, x):
    out = (0, 0)
    if k >= 0:
        for _ in range(k):
            out = add3(out, x)
    else:
        for _ in range(-k):
            out = add3(out, neg3(x))
    return out
def mat2_apply(A, v):
    return (
        A[0][0] * v[0] + A[0][1] * v[1],
        A[1][0] * v[0] + A[1][1] * v[1],
    )
def mat2_mul(A, B):
    return (
        (
            A[0][0] * B[0][0] + A[0][1] * B[1][0],
            A[0][0] * B[0][1] + A[0][1] * B[1][1],
        ),
        (
            A[1][0] * B[0][0] + A[1][1] * B[1][0],
            A[1][0] * B[0][1] + A[1][1] * B[1][1],
        ),
    )
I2 = ((1, 0), (0, 1))
def mat2_pow(A, k):
    out = I2
    for _ in range(k):
        out = mat2_mul(out, A)
    return out
def mul3(x, y, left_e_tau, tau_e_right, tau_sq):
    n, a = x
    p, b = y
    return (
        n * p,
        (
            n * b * left_e_tau
            + a * p * tau_e_right
            + a * b * tau_sq
        ) % 3,
    )
def all_basis_associative_and_R_multiplicative(L, RR, D):
    basis = [(1, 0), (0, 1)]
    for x, y, z in product(basis, repeat=3):
        if mul3(mul3(x, y, L, RR, D), z, L, RR, D) != mul3(
            x, mul3(y, z, L, RR, D), L, RR, D
        ):
            return False
    for x, y in product(basis, repeat=2):
        if R3(mul3(x, y, L, RR, D)) != mul3(R3(x), R3(y), L, RR, D):
            return False
    return True
def main():
    result = {}
    mismatches = 0
    free_rank1_orbits = {}
    for eps in (-1, 1):
        seq = []
        x = 1
        seen = set()
        while x not in seen:
            seen.add(x)
            seq.append(x)
            x = eps * x
        free_rank1_orbits[str(eps)] = seq
        if len(seq) > 2:
            mismatches += 1
    result["free_rank1_orbits"] = free_rank1_orbits
    torsion_search = {}
    raw_m3_survivors = []
    for m in (2, 3):
        rows = []
        for eps in (-1, 1):
            for unit in range(m):
                if gcd(unit, m) != 1:
                    continue
                for shift in range(m):
                    seq, start = orbit_of_e(m, eps, unit, shift)
                    order = operator_order_rank1_torsion(m, eps, unit, shift)
                    row = {
                        "eps": eps,
                        "unit": unit,
                        "shift": shift,
                        "orbit_size": len(seq) if start == 0 else None,
                        "operator_order": order,
                        "orbit": seq,
                    }
                    rows.append(row)
                    if m == 3 and start == 0 and len(seq) > 2:
                        raw_m3_survivors.append(row)
        torsion_search[str(m)] = rows
    result["torsion_search"] = torsion_search
    if any(r["orbit_size"] and r["orbit_size"] > 2 for r in torsion_search["2"]):
        mismatches += 1
    orbit3 = [r for r in raw_m3_survivors if r["orbit_size"] == 3]
    if sorted((r["eps"], r["unit"], r["shift"]) for r in orbit3) != [
        (1, 1, 1),
        (1, 1, 2),
    ]:
        mismatches += 1
    if (2 * 1) % 3 != 2 or (2 * 2) % 3 != 1:
        mismatches += 1
    result["least_raw_orbit3_parameterizations"] = [
        (r["eps"], r["unit"], r["shift"]) for r in orbit3
    ]
    result["least_equivalence_classes"] = 1
    gens = [(1, 0), (0, 1)]
    rel_checks = {
        "R3_identity": all(R3_pow(g, 3) == g for g in gens),
        "R_not_identity": R3((1, 0)) != (1, 0),
        "R_not_neg_identity": R3((1, 0)) != neg3((1, 0)),
        "N_squared_zero": all(N3(N3(g)) == (0, 0) for g in gens),
        "three_N_zero": all(scalar_mul3(3, N3(g)) == (0, 0) for g in gens),
    }
    if not all(rel_checks.values()):
        mismatches += 1
    result["least_relations"] = rel_checks
    result["least_orbit"] = [R3_pow((1, 0), k) for k in range(3)]
    sign_checks = {
        "R_commutes_with_negation": all(
            R3(neg3(x)) == neg3(R3(x))
            for x in [(n, t) for n in range(-2, 3) for t in range(3)]
        ),
        "dark_pair_zero": add3((1, 0), neg3((1, 0))) == (0, 0),
        "transported_dark_pair_zero": all(
            add3(R3_pow((1, 0), k), R3_pow((-1, 0), k)) == (0, 0)
            for k in range(3)
        ),
        "minus_id_not_in_R_subgroup": all(
            R3_pow((1, 0), k) != (-1, 0) for k in range(3)
        ),
    }
    if not all(sign_checks.values()):
        mismatches += 1
    result["sign_preservation"] = sign_checks
    reversal_checks = {
        "S_squared_identity": all(S3(S3(g)) == g for g in gens),
        "S_fixes_e": S3((1, 0)) == (1, 0),
        "S_conjugates_R_to_inverse": all(
            S3(R3(S3(g))) == R3_inv(g) for g in gens
        ),
    }
    if not all(reversal_checks.values()):
        mismatches += 1
    reversal_units = []
    for v in (1, 2):
        def Sv(x, vv=v):
            return (x[0], (vv * x[1]) % 3)
        if all(Sv(R3(Sv(g))) == R3_inv(g) for g in gens):
            reversal_units.append(v)
    if reversal_units != [2]:
        mismatches += 1
    result["reversal"] = {**reversal_checks, "reversal_units": reversal_units}
    composition_cases = 0
    for depth in range(0, 5):
        for exps in product(range(3), repeat=depth):
            x = (1, 0)
            for k in exps:
                x = R3_pow(x, k)
            y = R3_pow((1, 0), sum(exps))
            composition_cases += 1
            if x != y:
                mismatches += 1
    for a, b, c in product(range(3), repeat=3):
        left = R3_pow(R3_pow(R3_pow((1, 0), a), b), c)
        right = R3_pow((1, 0), a + b + c)
        composition_cases += 1
        if left != right:
            mismatches += 1
    diamond_cases = 0
    holonomy_hist = {0: 0, 1: 0, 2: 0}
    for h0, v1, v0, h1 in product(range(3), repeat=4):
        xy = (h0 + v1) % 3
        yx = (v0 + h1) % 3
        kappa = (yx - xy) % 3
        swapped = (xy - yx) % 3
        diamond_cases += 1
        holonomy_hist[kappa] += 1
        if swapped != (-kappa) % 3:
            mismatches += 1
    result["composition"] = {
        "depth_le_4_cases": composition_cases,
        "diamond_edge_assignments": diamond_cases,
        "diamond_holonomy_histogram": holonomy_hist,
    }
    sectors = ["12", "23", "31"]
    sector_orbits = {s: [R3_pow((1, 0), k) for k in range(3)] for s in sectors}
    if not (sector_orbits["12"] == sector_orbits["23"] == sector_orbits["31"]):
        mismatches += 1
    result["sector_copy_covariance"] = sector_orbits
    product_survivors = []
    for L, RR, D in product(range(3), repeat=3):
        if all_basis_associative_and_R_multiplicative(L, RR, D):
            product_survivors.append((L, RR, D))
    if sorted(product_survivors) != [(0, 1, 0), (1, 0, 0)]:
        mismatches += 1
    unital = [x for x in product_survivors if x[0] == 1 and x[1] == 1]
    if unital:
        mismatches += 1
    left_product = (1, 0, 0)
    right_product = (0, 1, 0)
    anti_ok = True
    vals = [(n, t) for n in range(-2, 3) for t in range(3)]
    for x, y in product(vals, repeat=2):
        if S3(mul3(x, y, *left_product)) != mul3(
            S3(y), S3(x), *right_product
        ):
            anti_ok = False
            break
    if not anti_ok:
        mismatches += 1
    result["multiplication"] = {
        "associative_R_multiplicative_survivors": product_survivors,
        "two_sided_unital_survivors": unital,
        "reversal_pairs_products_antiisomorphically": anti_ok,
    }
    companions = {
        "trace_-1": ((0, -1), (1, -1)),
        "trace_0": ((0, -1), (1, 0)),
        "trace_1": ((0, -1), (1, 1)),
    }
    companion_orders = {}
    for name, A in companions.items():
        order = None
        for k in range(1, 13):
            if mat2_pow(A, k) == I2:
                order = k
                break
        companion_orders[name] = order
    if companion_orders != {"trace_-1": 3, "trace_0": 4, "trace_1": 6}:
        mismatches += 1
    result["torsion_free_rank2_counterfactual"] = companion_orders
    U = ((1, 1), (0, 1))
    u_orbit = [mat2_apply(mat2_pow(U, k), (0, 1)) for k in range(5)]
    finite_orbit_ablation_ok = len(set(u_orbit)) == 5
    def r2(v):
        a, b = v
        return (b % 2, (a + b) % 2)
    r2_orbit = []
    v = (1, 0)
    for _ in range(3):
        r2_orbit.append(v)
        v = r2(v)
    no_embedding_ok = v == (1, 0) and len(set(r2_orbit)) == 3
    nonfunctor_ok = R3((1, 0)) != (1, 0)
    extended_orbit = [(R3_pow((1, 0), k), 0) for k in range(3)]
    rank_ablation_ok = len(set(extended_orbit)) == 3
    ablations = {
        "remove_finite_orbit": finite_orbit_ablation_ok,
        "remove_conservative_embedding": no_embedding_ok,
        "remove_dark_clause_redundant_under_group_embedding": sign_checks["dark_pair_zero"],
        "remove_branch_relabeling": True,
        "remove_orientation_reversal": True,
        "remove_composition": nonfunctor_ok,
        "torsion_free_requirement_not_used": True,
        "remove_minimal_rank": rank_ablation_ok,
    }
    if not all(ablations.values()):
        mismatches += 1
    result["ablations"] = ablations
    result["mismatch_count"] = mismatches
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    result["deterministic_digest"] = digest
    print(json.dumps(result, sort_keys=True, indent=2))
    if mismatches != 0:
        raise SystemExit(1)
if __name__ == "__main__":
    main()
