"""Verify exact TOTAL finite cover cost and mixed 4/5 refinements.

The two numeric roots below have exact total cover cost 25 and 29.  Arbitrary
mixed refinement depths use a proved induction plus Bang's theorem, not a
numeric primality claim about the symbolic prime names in the skeletons.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import combinations, product
import json
from math import gcd, isqrt, lcm, prod
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
BASE_REL = Path("research_notes/portable_direct/riesel_mixed_20261119/certificate.json")
ROOT = next(p for p in HERE.parents if (p / BASE_REL).is_file())
SOURCE_DEFAULT = next(p for p in (ROOT / "src", ROOT / "vendor_src")
                      if (p / "enterprise_math/brc_transport.py").is_file())
PIN = "b1efc6c805661ed7b476e6e730107da6043176ee"
PATTERNS = {
    "5": [(2, 0, 2), (3, 0, 3), (4, 1, 1), (6, 5, 11), (12, 7, 7)],
    "6": [(2, 0, 2), (3, 0, 15), (4, 1, 1), (8, 3, 11), (12, 7, 7), (24, 23, 23)],
}
Q0 = [
    {"p": 5, "ord2": 4, "period_u": 2, "phase_u": 1, "private_u": 3},
    {"p": 73, "ord2": 9, "period_u": 9, "phase_u": 1, "private_u": 10},
    {"p": 13, "ord2": 12, "period_u": 6, "phase_u": 0, "private_u": 6},
    {"p": 19, "ord2": 18, "period_u": 9, "phase_u": 4, "private_u": 76},
    {"p": 109, "ord2": 36, "period_u": 18, "phase_u": 16, "private_u": 16},
]
FIVE_PRIMES = [433, 246241, 577, 33975937, 209924353]
Q11 = [
    {"p": p, "ord2": order, "period_u": d, "phase_u": c, "private_u": w}
    for p, order, d, c, w in [
        (13, 12, 6, 0, 6), (19, 18, 9, 1, 10), (73, 9, 9, 7, 16),
        (37, 36, 18, 3, 3), (109, 36, 18, 15, 15), (61, 60, 30, 1, 31),
        (433, 72, 36, 9, 9), (38737, 72, 36, 27, 63),
        (631, 45, 45, 4, 49), (23311, 45, 45, 40, 85), (181, 180, 90, 76, 76),
    ]
]


def git_blob(data):
    return sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def decimal_digest(value):
    text = str(value)
    return {"decimal_digits": len(text), "decimal_sha256": sha256(text.encode()).hexdigest(),
            "bit_length": value.bit_length()}


def prime_trial(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def exact_order(b, p, order):
    return pow(b, order, p) == 1 and all(pow(b, j, p) != 1 for j in range(1, order))


def strip(value, primes):
    removed = {}
    for p in sorted(primes):
        count = 0
        while value % p == 0:
            value //= p
            count += 1
        if count:
            removed[str(p)] = count
    return value, removed


def crt_pair(a, modulus, b, p):
    assert gcd(modulus, p) == 1
    return a + modulus * (((b - a) * pow(modulus, -1, p)) % p), modulus * p


def skeleton(word, old_orders, holes, seed=5):
    """Inductively construct a finite cover with private witnesses in H_u."""
    assert seed in (5, 11)
    rows = [dict(row) for row in (Q0 if seed == 5 else Q11)]
    used_orders = set(old_orders) | {r["ord2"] for r in rows}
    stages = []
    for number, kind in enumerate(word, 1):
        pattern = PATTERNS[kind]
        R = max(m for m, _, _ in pattern)
        parent = max(rows, key=lambda r: r["period_u"])
        d, c, w = (parent[k] for k in ("period_u", "phase_u", "private_u"))
        exceptional_first = seed == 11 and number == 1
        multiplier = 35 if seed == 5 else (14 if exceptional_first else 7)
        L = multiplier * d
        assert lcm(105, *(r["period_u"] for r in rows)) == L
        assert (w - c) % d == 0
        if exceptional_first:
            assert (parent["p"], d, c) == (181, 90, 76)
            for private_u in (76, 346):
                assert private_u % 105 in holes
                assert [r["p"] for r in rows if private_u % r["period_u"] == r["phase_u"]] == [181]
        else:
            assert gcd(multiplier, R) == 1
        v0 = (w - c) // d
        children = []
        for m, b, private in pattern:
            order = 2 * d * m
            assert order > 6 and order not in used_orders
            assert order > 2 * d
            used_orders.add(order)
            if exceptional_first:
                # L/d=14 has gcd 2 with R=12 or 24.  Two private
                # parent fibers supply the two parity classes of v.
                lifted_from = 76 if private % 2 == 0 else 346
                lift_v0 = (lifted_from-c)//d
                assert (private-lift_v0) % 2 == 0
                t = (((private-lift_v0)//2)*pow(7, -1, R//2)) % (R//2)
            else:
                lifted_from = w
                t = ((private-v0)*pow(multiplier, -1, R)) % R
            child = {"p": f"primitive_prime_order_{order}", "ord2": order,
                     "period_u": d * m, "phase_u": (c + d * b) % (d * m),
                     "private_u": lifted_from + L*t,
                     "existence": "Bang: exact base-2 order exists for exponent > 6"}
            assert child["private_u"] % (d * m) == child["phase_u"]
            children.append(child)
        rows = [r for r in rows if r is not parent] + children
        assert max(r["period_u"] for r in rows) == d * R
        stages.append({"stage": number, "pattern": kind, "parent_period_u": d,
                       "parent_phase_u": c, "parent_private_u": w,
                       "old_common_period_u": L,
                       "used_two_parent_parity_fibers": exceptional_first,
                       "new_max_period_u": d * R,
                       "new_orders": [r["ord2"] for r in children]})
    h, j = word.count("5"), word.count("6")
    dmax = (18 if seed == 5 else 90) * 12**h * 24**j
    multiplier = 35 if seed == 5 else (14 if not word else 7)
    assert len(rows) == seed + 4*h + 5*j
    assert max(r["period_u"] for r in rows) == dmax
    assert lcm(105, *(r["period_u"] for r in rows)) == multiplier * dmax
    assert len({r["p"] for r in rows}) == len(rows)
    for i, row in enumerate(rows):
        u = row["private_u"]
        assert u > 0 and u % 105 in holes
        assert [j for j, r in enumerate(rows) if u % r["period_u"] == r["phase_u"]] == [i]
        assert 210 % row["ord2"] != 0
        if row["p"] not in (73, 631, 23311):
            assert row["ord2"] % 2 == 0  # Its zero n-phase is even.
        if isinstance(row["p"], str):
            assert row["ord2"] not in old_orders
    if len(word) <= 1:
        for u in range(multiplier * dmax):
            assert u % 105 not in holes or any(u % r["period_u"] == r["phase_u"] for r in rows)
    return {"seed_additional_channels": seed,
            "word": word, "five_refinements": h, "six_refinements": j,
            "additional_prime_count": len(rows), "total_prime_count": 20 + len(rows),
            "dmax": dmax, "period_u": multiplier*dmax, "rows": rows, "stages": stages,
            "all_private_witnesses_checked": True,
            "complete_even_period_checked": len(word) <= 1}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, default=SOURCE_DEFAULT)
    parser.add_argument("--output", type=Path, default=HERE / "total_cost_certificate.json")
    parser.add_argument("--skeleton-depth", type=int, default=4)
    args = parser.parse_args()
    sys.set_int_max_str_digits(0)
    old_bytes = (ROOT / BASE_REL).read_bytes()
    old = json.loads(old_bytes)
    assert old["project_source_commit"] == PIN
    source_checks = {}
    for filename, expected in old["project_source_blobs"].items():
        observed = git_blob((args.source_dir / "enterprise_math" / filename).read_bytes())
        assert observed == expected
        source_checks[filename] = {"expected_git_blob_sha1": expected,
                                   "observed_git_blob_sha1": observed, "matches": True}
    astar = int(old["optimized"]["a"])
    old_rows = old["optimized"]["rows"]
    P = [r["p"] for r in old_rows]
    Pset = set(P)
    M = prod(P)
    old_orders = {r["order"] for r in old_rows}
    period = lcm(*(r["order"] for r in old_rows))
    assert period == 6720 and len(Pset) == 20
    for row in old_rows:
        p = row["p"]
        assert prime_trial(p) and exact_order(2, p, row["order"])
        assert astar % p == row["a_residue"]
        assert (astar * astar * pow(2, row["exponent_phase"], p) - 1) % p == 0
    odd_private = {p: [] for p in P}
    for n in range(1, period, 2):
        hits = [r["p"] for r in old_rows if n % r["order"] == r["exponent_phase"]]
        assert hits
        if len(hits) == 1:
            odd_private[hits[0]].append(n)
    old_witnesses = []
    for p in P:
        assert odd_private[p]
        # A direct small choice; the proof also gives a 3-lift construction.
        selected = next(n for n in odd_private[p] if n % 9 != 2)
        old_witnesses.append({"p": p, "private_odd_count_in_6720": len(odd_private[p]),
                              "first_private_odd_n": min(odd_private[p]),
                              "private_n_avoiding_73": selected})

    # The second seed has three odd-order channels.  In each old 6720
    # fiber the q=73 condition excludes at most one of three lifts.  The
    # q=631 and q=23311 conditions have different phases modulo 15 and
    # hence jointly exclude at most one further lift.
    odd_rows_11 = [r for r in Q11 if r["ord2"] % 2]
    assert [(r["p"], r["ord2"], 2*r["phase_u"] % r["ord2"]) for r in odd_rows_11] == [
        (73, 9, 5), (631, 45, 8), (23311, 45, 35)]
    assert 6720 % 45 == 15 and 6720 % 9 == 6
    old_witnesses_11 = []
    for p in P:
        first = min(odd_private[p])
        lifts = [first + 6720*t for t in range(3)]
        admissible = [n for n in lifts if all(n % r["ord2"] != 2*r["phase_u"] % r["ord2"]
                                             for r in odd_rows_11)]
        assert admissible
        for n in admissible:
            assert [r["p"] for r in old_rows if n % r["order"] == r["exponent_phase"]] == [p]
            assert all(n % r["ord2"] != 2*r["phase_u"] % r["ord2"] for r in Q11)
        # Also retain a small optional numerical witness in the full period.
        minimal = min(n + period*t for n in odd_private[p] for t in range(3)
                      if all((n + period*t) % r["ord2"] != 2*r["phase_u"] % r["ord2"]
                             for r in odd_rows_11))
        old_witnesses_11.append({"p": p, "first_old_private_odd_n": first,
                                 "admissible_three_lifts": admissible,
                                 "smallest_private_n_avoiding_Q11": minimal})
    for row in Q11:
        assert row["p"] not in Pset and row["p"] > 11
        assert prime_trial(row["p"]) and exact_order(2, row["p"], row["ord2"])
        assert row["period_u"] == row["ord2"] // gcd(2, row["ord2"])

    holes = {u for u in range(105) if all((astar*astar*pow(2, 2*u, p)-1) % p for p in P)}
    assert len(holes) == 36
    for u in range(period // 2):
        actual_hole = all((astar*astar*pow(2, 2*u, p)-1) % p for p in P)
        assert actual_hole == (u % 105 in holes)
    for kind, pattern in PATTERNS.items():
        R = max(m for m, _, _ in pattern)
        assert all(any(v % m == b for m, b, _ in pattern) for v in range(R))
        assert len({m for m, _, _ in pattern}) == len(pattern)
        for i, (_, _, private) in enumerate(pattern):
            assert [j for j, (m, b, _) in enumerate(pattern) if private % m == b] == [i]

    sys.path.insert(0, str(args.source_dir))
    from enterprise_math.brc_transport import Affine, EffectHistogram
    step = EffectHistogram.from_terms(1, [(1, Affine(((2,),), (1,)), 1)])
    twice = step.then(step)
    assert twice.entries == ((Fraction(1), Affine(((4,),), (3,)), 1),)

    def advance(packet, value):
        (point, weights), = packet.evaluate((value,)).items()
        assert weights.entries == ((Fraction(1), 1),)
        assert point[0].denominator == 1
        return int(point[0])

    assert advance(step, -1) == -1 and advance(twice, -1) == -1

    def numeric_certificate(word):
        skel = skeleton(word, old_orders, holes)
        rows = [dict(r) for r in skel["rows"]]
        if word == "5":
            for row, p in zip(rows[-5:], FIVE_PRIMES):
                row["p"] = p
                row.pop("existence", None)
        else:
            assert word == ""
        Q = [r["p"] for r in rows]
        assert len(set(Q)) == len(Q) and not set(Q) & Pset
        for row in rows:
            assert prime_trial(row["p"]) and exact_order(2, row["p"], row["ord2"])
            assert row["period_u"] == row["ord2"] // gcd(2, row["ord2"])
            row["root_residue"] = pow(pow(2, row["phase_u"], row["p"]), -1, row["p"])
            # Improve the numerical certificate size without changing the proof.
            row["private_u"] = next(u for u in range(1, skel["period_u"] + 1)
                if u % 105 in holes and [r["p"] for r in rows
                if u % r["period_u"] == r["phase_u"]] == [row["p"]])
        ns = [r["private_n_avoiding_73"] for r in old_witnesses] + [2*r["private_u"] for r in rows]
        all_primes = P + Q
        assert len(set(ns)) == len(ns) == len(all_primes)
        diffs = sorted({abs(i-j) for i, j in combinations(ns, 2)})
        D = lcm(*((1 << d) - 1 for d in diffs))
        E, removed = strip(D, set(all_primes))
        T1, T1_removed = strip((1 << 210) - 1, Pset)
        T = lcm(E, T1)
        b, K = astar, 2*M
        for row in rows:
            b, K = crt_pair(b, K, row["root_residue"], row["p"])
        assert gcd(T, K) == 1 and K == 2*M*prod(Q)
        a = T*((b*pow(T, -1, K)) % K)
        assert 0 < a < T*K and a > max(all_primes)
        assert a % (2*M) == astar and a % T == 0 and a % 3 == 0
        assert all(a % r["p"] == r["root_residue"] for r in rows)
        # Native BRC evaluation generates every selected term from x_0=a^2-1.
        x = a*a-1
        values = {}
        nset = set(ns)
        for n in range(1, max(ns)+1):
            x = advance(step, x)
            if n in nset:
                assert x == (a*a << n)-1
                values[n] = x
        witnesses = []
        for p, n in zip(all_primes, ns):
            hits = [q for q in all_primes if values[n] % q == 0]
            assert hits == [p]
            assert 1 < p < values[n]
            witnesses.append({"p": p, "n": n, "only_cover_prime": p, **decimal_digest(values[n])})
        gcd_checks = []
        for i, j in combinations(ns, 2):
            g = gcd(values[i], values[j])
            assert g == 1
            gcd_checks.append({"n1": i, "n2": j, "gcd": g})
        full_period = lcm(period, *(r["ord2"] for r in rows))
        combined = [(r["p"], r["order"], r["exponent_phase"]) for r in old_rows]
        combined += [(r["p"], r["ord2"], (2*r["phase_u"]) % r["ord2"]) for r in rows]
        for p, order, phase in combined:
            assert (a*a*pow(2, phase, p)-1) % p == 0
        # Exact phase congruences cover the full common period, not just a prefix.
        for n in range(full_period):
            assert any(n % order == phase for p, order, phase in combined)
        assert 2*a*a-1 > max(all_primes)
        return {"refinement_word": word, "P": P, "Q": rows,
                "root_a": str(a), "root_summary": decimal_digest(a),
                "square_k_summary": decimal_digest(a*a),
                "crt_b": str(b), "crt_K": str(K),
                "D_summary": decimal_digest(D), "D_removed_valuations": removed,
                "E_summary": decimal_digest(E), "T1": str(T1),
                "T1_removed_valuations": T1_removed, "T_summary": decimal_digest(T),
                "root_progression_modulus": str(T*K),
                "witnesses": witnesses, "witness_exponent_differences": diffs,
                "all_pairwise_gcds": gcd_checks,
                "full_cover_period_n": full_period,
                "full_common_period_exhausted": True,
                "exact_delta_P": len(Q), "exact_total_tau": len(all_primes),
                "old_T_B3_m1_forcing_preserved": True,
                "native_BRC_every_step_through_n": max(ns)}

    numeric = [numeric_certificate(""), numeric_certificate("5")]
    skeletons = [skeleton("".join(word), old_orders, holes, seed)
                 for seed in (5, 11)
                 for depth in range(args.skeleton_depth+1)
                 for word in product("56", repeat=depth)]
    # Four consecutive s values, followed by arbitrary increments of 4,
    # prove every s>=13 occurs in one of the two seed families.
    cofinite_bases = [(13, 5, 2, 0), (14, 5, 1, 1), (15, 5, 0, 2), (16, 11, 0, 1)]
    assert all(s == seed+4*h+5*j for s, seed, h, j in cofinite_bases)
    result = {
        "schema": "enterprise-math.riesel-exact-total-cover-cost.v1",
        "researcher_id": "EM-DIRECT-970E1C",
        "research_activity_id": "RA-D2EC212845B63844081F9A14",
        "status": "new author derivation and exact finite checks; not independent project Review",
        "project_source_commit": PIN, "project_source_blob_checks": source_checks,
        "base_certificate_sha256": sha256(old_bytes).hexdigest(),
        "a_star": str(astar), "M": str(M), "P": P,
        "old_period_n": period, "old_holes_u_mod105": sorted(holes),
        "old_P_private_odd_witnesses": old_witnesses,
        "old_P_private_odd_witnesses_for_seed11": old_witnesses_11,
        "seed11_rows": Q11,
        "all_20_old_channels_irredundant_on_odd_indices": True,
        "patterns": {kind: [{"modulus": m, "phase": b, "private_residue": w}
                              for m, b, w in pattern] for kind, pattern in PATTERNS.items()},
        "numeric_certificates": numeric, "mixed_skeletons": skeletons,
        "mixed_skeleton_count": len(skeletons),
        "cofinite_bases_s_seed_h_j": cofinite_bases,
        "general_theorem": "For each seed b in {5,11} and every h,j >= 0, infinitely many positive odd a congruent to a_star modulo 2M have delta_P(a)=b+4h+5j and total tau(a^2)=20+b+4h+5j. The b=5 family can also satisfy T_{3,1}|a; the b=11 family can satisfy T_{11,1}|a.",
        "cofinite_corollary": "Every additional cost s>=13, and thus every total cost N>=33, occurs infinitely often in this same old P root class. These are sufficient thresholds, not minimality claims.",
        "native_brc": {"module": "enterprise_math.brc_transport", "source_commit": PIN,
                       "one_step": "x -> 2x+1", "even_step": "x -> 4x+3",
                       "positive_singleton_weight": 1, "multiplicity": 1,
                       "anchor": "fixed X6; arithmetic index is not physical time"},
        "primitive_prime_source": {
            "url": "https://people.math.sc.edu/filaseta/papers/SierpinskiEtCoPap5.pdf",
            "location": "Lemma 2; cites A. S. Bang (1886)",
            "used_statement": "For every integer t>6, a prime with exact base-2 order t exists."},
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({"verified": True, "output": str(args.output),
                      "old_P_private_channels": len(old_witnesses),
                      "numeric": [{"delta_P": c["exact_delta_P"], "tau": c["exact_total_tau"],
                                   "a_digits": c["root_summary"]["decimal_digits"],
                                   "period_n": c["full_cover_period_n"],
                                   "pairwise_gcd_checks": len(c["all_pairwise_gcds"])} for c in numeric],
                      "mixed_skeletons_verified": len(skeletons)}, indent=2))


if __name__ == "__main__":
    main()
