"""Exact finite certificates for costs 5,6,7,8 and all >=5 by refinement.

Arithmetic is integer-only.  The infinite theorem is the induction in proof.md;
finite symbolic tests exercise its formulas without claiming numeric primes.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
from itertools import combinations
import json
from math import gcd, isqrt, lcm, prod
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ASTAR = 690786768637635218740714348513373826260012289
OLD = [
    (7, 3, 1, 37), (17, 8, 3, 3), (31, 5, 4, 89),
    (41, 20, 5, 5), (71, 35, 13, 293), (97, 48, 21, 117),
    (113, 28, 21, 413), (127, 7, 1, 113), (151, 15, 11, 41),
    (241, 24, 9, 33), (257, 16, 7, 87), (281, 70, 23, 233),
    (337, 21, 17, 773), (641, 64, 15, 207),
    (673, 48, 45, 237), (1321, 60, 17, 257),
    (14449, 84, 53, 53), (29191, 105, 68, 593),
    (65537, 32, 31, 63), (6700417, 64, 47, 111),
]
P = [r[0] for r in OLD]
M = prod(P)
H = {0, 1, 3, 6, 9, 10, 15, 16, 21, 30, 31, 33, 36, 45,
     48, 49, 51, 54, 55, 63, 64, 66, 69, 70, 75, 76, 78,
     79, 84, 85, 90, 91, 93, 96, 99, 100}
SEED = [
    {"p": p, "order2": o, "d": d, "c": c, "private_u": w}
    for p, o, d, c, w in [(5, 4, 2, 1, 3), (73, 9, 9, 1, 10),
                          (13, 12, 6, 0, 6), (19, 18, 9, 4, 76),
                          (109, 36, 18, 16, 16)]
]
BINARY_PAIRS = [(433, 38737), (577, 487824887233), (1153, 6337)]
PATTERN = [(2, 0, 2), (3, 0, 3), (4, 1, 1), (6, 5, 11), (12, 7, 7)]


def prime_trial(p):
    if p < 2 or p % 2 == 0:
        return p == 2
    return all(p % d for d in range(3, isqrt(p) + 1, 2))


def exact_order(p, claimed):
    return pow(2, claimed, p) == 1 and all(
        pow(2, e, p) != 1 for e in range(1, claimed))


def strip(value, primes):
    for p in primes:
        while value % p == 0:
            value //= p
    return value


def crt_pair(a, modulus, b, q):
    assert gcd(modulus, q) == 1
    return a + modulus * (((b - a) * pow(modulus, -1, q)) % q), modulus * q


def old_hit(n):
    return [p for p, o, c, _ in OLD if n % o == c]


def q_hit(u, rows):
    return [r["p"] for r in rows if u % r["d"] == r["c"]]


def compact_private_witnesses(rows):
    period = lcm(105, *(r["d"] for r in rows))
    for row in rows:
        row["private_u"] = next(
            u for u in range(1, period + 1)
            if u % 105 in H and q_hit(u, rows) == [row["p"]])


def binary_split(rows, pair):
    rows = [dict(r) for r in rows]
    parent = max(rows, key=lambda r: r["d"])
    d, c, w = parent["d"], parent["c"], parent["private_u"]
    L = lcm(105, *(r["d"] for r in rows))
    assert L == 35*d
    children = []
    for b, q in enumerate(pair):
        assert prime_trial(q) and exact_order(q, 4*d)
        v0 = (w-c)//d
        t = (b-v0) % 2  # 35 is odd.
        children.append({"p": q, "order2": 4*d, "d": 2*d,
                         "c": (c+d*b) % (2*d), "private_u": w+L*t})
    rows = [r for r in rows if r is not parent] + children
    compact_private_witnesses(rows)
    return rows


def check_seed(rows):
    assert len(set(P) | {r["p"] for r in rows}) == 20+len(rows)
    L = lcm(105, *(r["d"] for r in rows))
    assert L == 35*max(r["d"] for r in rows)
    for row in rows:
        q, order, d, c = (row[k] for k in ("p", "order2", "d", "c"))
        assert prime_trial(q) and exact_order(q, order)
        assert d == order//gcd(order, 2)
        row["root_residue"] = pow(2, -c, q)
        assert pow(2, 210, q) != 1  # compatible with T_{3,1}.
        assert row["private_u"] % 105 in H
        assert q_hit(row["private_u"], rows) == [q]
    for u in range(L):
        assert u % 105 not in H or q_hit(u, rows)
    full_period = lcm(*(r[1] for r in OLD), *(r["order2"] for r in rows))
    for n in range(1, full_period+1):
        hits = old_hit(n) + [r["p"] for r in rows
                            if n % r["order2"] == 2*r["c"] % r["order2"]]
        assert hits
    for p, _, _, n in OLD:
        assert old_hit(n) == [p]
        assert all(n % r["order2"] != 2*r["c"] % r["order2"] for r in rows)
    return {"additional_cost": len(rows), "total_cost": 20+len(rows),
            "period_u": L, "full_period_n": full_period, "rows": rows,
            "full_period_checked": True, "all_private_witnesses_checked": True}


def refine_symbolic(rows, count):
    rows = [dict(r) for r in rows]
    for stage in range(count):
        parent = max(rows, key=lambda r: r["d"])
        d, c, w = (parent[k] for k in ("d", "c", "private_u"))
        L = lcm(105, *(r["d"] for r in rows))
        assert L == 35*d
        all_used = {r[1] for r in OLD} | {r["order2"] for r in rows}
        orders = [2*d*m for m, _, _ in PATTERN]
        assert len(set(orders)) == 5 and all(o > 6 and o not in all_used for o in orders)
        children = []
        for m, b, private in PATTERN:
            v0 = (w-c)//d
            t = ((private-v0)*pow(35, -1, 12)) % 12
            children.append({"p": f"primitive_prime_order_{2*d*m}",
                             "order2": 2*d*m, "d": d*m, "c": (c+d*b) % (d*m),
                             "private_u": w+L*t})
        rows = [r for r in rows if r is not parent]+children
        for r in rows:
            assert r["private_u"] % 105 in H
            assert q_hit(r["private_u"], rows) == [r["p"]]
            assert 210 % r["order2"] != 0
        assert lcm(105, *(r["d"] for r in rows)) == 35*12*d
    return {"refinements": count, "extra_count": len(rows),
            "dmax": max(r["d"] for r in rows), "private_witnesses": [r["private_u"] for r in rows]}


def numeric_exact_root(rows):
    channels = P + [r["p"] for r in rows]
    indices = [r[3] for r in OLD]+[2*r["private_u"] for r in rows]
    differences = sorted({abs(i-j) for i, j in combinations(indices, 2)})
    D = lcm(*((1 << d)-1 for d in differences))
    E = strip(D, channels)
    T = strip((1 << 210)-1, P)
    forcing = lcm(E, T)
    a, modulus = ASTAR, 2*M
    for row in rows:
        a, modulus = crt_pair(a, modulus, row["root_residue"], row["p"])
    a, modulus = crt_pair(a, modulus, 0, forcing)
    if 2*a*a-1 <= max(channels):
        a += modulus
    assert a > 0 and a % 2 == 1 and (a-ASTAR) % (2*M) == 0 and a % T == 0
    terms = [(a*a << n)-1 for n in indices]
    for q, term in zip(channels, terms):
        assert 1 < q < term and term % q == 0
    assert all(gcd(x, y) == 1 for x, y in combinations(terms, 2))
    assert all(all(term % p for p in P) for term in terms[len(P):])
    encoded = str(a)
    return {"additional_cost": len(rows), "total_cost": len(channels),
            "root_hex": hex(a), "progression_modulus_hex": hex(modulus),
            "root_decimal_digits": len(encoded), "root_bit_length": a.bit_length(),
            "root_decimal_sha256": sha256(encoded.encode()).hexdigest(),
            "private_indices": indices, "gcd_pair_count": len(indices)*(len(indices)-1)//2,
            "all_pairwise_gcd_one": True, "T_3_1_divides_root": True,
            "E_bit_length": E.bit_length(), "proper_cover": True}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=HERE/"small_spectrum_certificate.json")
    args = parser.parse_args()
    sys.set_int_max_str_digits(0)
    assert M == 1397394912916194098609132326092145093313722687204526281
    for p, order, phase, n in OLD:
        assert prime_trial(p) and exact_order(p, order)
        assert (ASTAR*ASTAR*pow(2, phase, p)-1) % p == 0
        assert n % 2 == 1 and n % order == phase
    for u in range(3360):
        assert (not old_hit(2*u)) == (u % 105 in H)
    assert all(old_hit(n) for n in range(1, 6720, 2))
    for v in range(12):
        assert any(v % m == b for m, b, _ in PATTERN)
    for m, b, w in PATTERN:
        assert [(mm, bb) for mm, bb, _ in PATTERN if w % mm == bb] == [(m, b)]
    seeds = []
    rows = [dict(r) for r in SEED]
    seeds.append(check_seed(rows))
    for pair in BINARY_PAIRS:
        rows = binary_split(rows, pair)
        seeds.append(check_seed(rows))
    skeletons = [dict(seed_size=len(seed["rows"]), **refine_symbolic(seed["rows"], h))
                 for seed in seeds for h in range(5)]
    numeric = numeric_exact_root(seeds[-1]["rows"])
    result = {"schema": "riesel-small-spectrum-v1", "status": "AUTHOR_EXACT_CERTIFICATE",
              "source_dependency": {"commit": "2feef401388e6e81a35dd8b0e66383f43561ad12",
                  "path": "research_notes/portable_direct/riesel_budget_20261120/cost/proof.md"},
              "a_star": str(ASTAR), "M": str(M), "old_rows": OLD, "holes_u_mod_105": sorted(H),
              "binary_pairs": BINARY_PAIRS, "seeds": seeds, "symbolic_checks": skeletons,
              "numeric_cost_8": numeric,
              "theorem": "Every integer s>=5 occurs infinitely often as delta_P=s and tau=20+s in the old residue class, with T_3_1|a.",
              "infinite_proof": "Four explicit seeds + induction and Bang exact-order prime theorem; finite checks are not the infinite proof."}
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"output": str(args.output), "seed_costs": [s["additional_cost"] for s in seeds],
                      "seed_periods_u": [s["period_u"] for s in seeds],
                      "numeric_root_digits": numeric["root_decimal_digits"],
                      "numeric_gcd_pairs": numeric["gcd_pair_count"],
                      "symbolic_induction_formula_checks": len(skeletons)}))


if __name__ == "__main__":
    main()
