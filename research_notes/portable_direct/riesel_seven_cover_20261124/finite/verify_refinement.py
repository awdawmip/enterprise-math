#!/usr/bin/env python3
"""Exact finite support for the consecutive-cover observer strengthening.

Universal existence, all-k privacy, arbitrary-N compatibility, and cost minima
are proved in proof.md. These checks do not infer them from a finite sample.
"""

from collections import Counter
from math import gcd, isqrt, lcm
from pathlib import Path
import json


ASTAR = 690786768637635218740714348513373826260012289
P = [7, 17, 31, 41, 71, 97, 113, 127, 151, 241, 257, 281,
     337, 641, 673, 1321, 14449, 29191, 65537, 6700417]
OLD_PRIVATE_N = [37, 3, 89, 5, 293, 117, 413, 113, 41, 33,
                 87, 233, 773, 207, 237, 257, 53, 593, 63, 111]
H = {0, 1, 3, 6, 9, 10, 15, 16, 21, 30, 31, 33, 36, 45,
     48, 49, 51, 54, 55, 63, 64, 66, 69, 70, 75, 76, 78,
     79, 84, 85, 90, 91, 93, 96, 99, 100}
B = {0, 3, 5, 8, 10, 15, 21, 23, 26, 28, 30, 31, 33}
PREFIX = [
    {"label": "P5", "q": 5, "order2": 4, "u_period": 2, "u_phase": 1, "private_n": 6},
    {"label": "P13", "q": 13, "order2": 12, "u_period": 6, "u_phase": 0, "private_n": 12},
    {"label": "P19", "q": 19, "order2": 18, "u_period": 9, "u_phase": 4, "private_n": 152},
    {"label": "P73", "q": 73, "order2": 9, "u_period": 9, "u_phase": 1, "private_n": 20},
]
KNOWN = {
    "Z": (87211, 54), "R": (246241, 108), "T0": (279073, 108),
    "D1": (38737, 72), "D2": (487824887233, 144),
    "T1": (33975937, 216),
}


def prime_trial(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


def distinct_prime_factors(n):
    result = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            result.append(d)
            while n % d == 0:
                n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        result.append(n)
    return result


def exact_order(base, q):
    order = q - 1
    for p in distinct_prime_factors(order):
        while order % p == 0 and pow(base, order // p, q) == 1:
            order //= p
    return order


def check_order(q, order):
    assert pow(2, order, q) == 1
    assert all(pow(2, order // p, q) != 1 for p in distinct_prime_factors(order))


def make_row(label, m, b, order=None):
    order = 36 * m if order is None else order
    d = order // gcd(order, 2)
    c = (16 + 18 * b) % d
    return {"label": label, "m": m, "b": b % m, "order2": order,
            "u_period": d, "u_phase": c}


def covering_rows(k):
    assert k >= 0
    if k == 0:
        return [make_row("Z", 3, 0, 54), make_row("R", 3, 1), make_row("T0", 3, 2)]
    rows = [make_row(f"D{j}", 2 ** j, 2 ** (j - 1)) for j in range(1, k + 1)]
    rows.append(make_row("R", 3, 1))
    half, full = 3 * 2 ** (k - 1), 3 * 2 ** k
    rows.append(make_row(f"T{k-1}", half, 0 if k % 2 == 0 else 2 ** k))
    rows.append(make_row(f"T{k}", full, 2 ** (k + 1) if k % 2 == 0 else 0))
    return rows


def private_w_residues(k):
    if k == 0:
        return [0, 1, 2]
    dyadic = [2 ** (j - 1) if j % 2 == 0 else 3 * 2 ** (j - 1)
               for j in range(1, k + 1)]
    tail = [2 ** k, 0, 2 ** (k + 1)] if k % 2 == 0 else [2 ** (k + 1), 2 ** k, 0]
    return dyadic + tail


def lift_to_old_hole(w, period):
    return 35 * ((w * pow(35, -1, period)) % period)


def hits_u(row, u):
    return u % row["u_period"] == row["u_phase"]


def hits_n(row, n):
    return n % row["order2"] == 2 * row["u_phase"] % row["order2"]


def j_threshold(BN, lower):
    j = lower
    while 54 * 2 ** j <= BN:
        j += 1
    return j


def crt_coprime(pairs):
    value, modulus = 0, 1
    for residue, qpower in pairs:
        assert gcd(modulus, qpower) == 1
        t = ((residue - value) * pow(modulus, -1, qpower)) % qpower
        value += modulus * t
        modulus *= qpower
    return value, modulus


def main():
    assert ASTAR % 3 == 0 and ASTAR % 2 == 1
    assert len(P) == len(OLD_PRIVATE_N) == 20
    ord_old = {q: exact_order(2, q) for q in P}
    assert max(ord_old.values()) == 105
    for q in P:
        check_order(q, ord_old[q])
    old_n_classes = {}
    for q in P:
        zeros = [n for n in range(ord_old[q])
                 if (ASTAR * ASTAR * pow(2, n, q) - 1) % q == 0]
        assert len(zeros) == 1
        old_n_classes[q] = zeros[0]
    for q, n in zip(P, OLD_PRIVATE_N):
        hits = [p for p in P if n % ord_old[p] == old_n_classes[p]]
        assert hits == [q]
        assert n % 2 == 1 and n % 9 != 2

    known_prime_records = {}
    for label, (q, order) in KNOWN.items():
        assert prime_trial(q)
        assert q not in P and q not in {3, 5, 13, 19, 73, 11, 61, 331, 37, 109, 433}
        check_order(q, order)
        known_prime_records[label] = {"prime": q, "order2": order}
    for row in PREFIX:
        assert prime_trial(row["q"])
        check_order(row["q"], row["order2"])
    assert [pow(2, -r["u_phase"], r["q"]) for r in PREFIX] == [3, 1, 6, 37]
    check_order(433, 72)
    assert pow(2, -34, 38737) == 38733

    # Verify the inherited old-hole/prefix reduction over a complete u-period.
    remaining = {u for u in range(630)
                 if u % 105 in H and not any(hits_u(row, u) for row in PREFIX)}
    assert remaining == {16 + 18 * w for w in B}

    patterns = []
    for k in range(9):
        rows = covering_rows(k)
        period = 3 * 2 ** k
        assert len(rows) == k + 3
        assert lcm(*(row["m"] for row in rows)) == period
        assert gcd(period, 35) == 1
        assert len({row["label"] for row in rows}) == len(rows)
        hits = [[i for i, row in enumerate(rows) if w % row["m"] == row["b"]]
                for w in range(period)]
        assert all(hits)
        private = [[w for w, indices in enumerate(hits) if indices == [i]]
                   for i in range(len(rows))]
        assert all(private)
        chosen = private_w_residues(k)
        assert all(0 <= w < period and w in private[i] for i, w in enumerate(chosen))

        # Concrete parent-coordinate phases match the abstract w-cover,
        # including Z's smaller u-period at k=0.
        for row in rows:
            assert 210 % row["order2"] != 0
            assert row["order2"] % 2 == 0
            assert all(hits_u(row, 16 + 18 * w) == (w % row["m"] == row["b"])
                       for w in range(period))
        for prefix in PREFIX:
            n = prefix["private_n"]
            u = n // 2
            assert u % 105 in H
            all_rows = PREFIX + rows
            assert [r["label"] for r in all_rows if hits_n(r, n)] == [prefix["label"]]
        assert all(not any(hits_n(row, n) for row in PREFIX + rows) for n in OLD_PRIVATE_N)

        lifted = [lift_to_old_hole(w, period) for w in chosen]
        new_n = [32 + 36 * w for w in lifted]
        for i, (w, n) in enumerate(zip(lifted, new_n)):
            assert w % 35 == 0 and (n // 2) % 105 == 16
            assert [r["label"] for r in PREFIX + rows if hits_n(r, n)] == [rows[i]["label"]]
        all_private = OLD_PRIVATE_N + [r["private_n"] for r in PREFIX] + new_n
        assert len(all_private) == 27 + k and len(set(all_private)) == len(all_private)

        # Three fixed old-witness differences force the inactive coordinates.
        assert 63 in OLD_PRIVATE_N and 3 in OLD_PRIVATE_N and 63 - 3 == 60
        assert 41 in OLD_PRIVATE_N and 5 in OLD_PRIVATE_N and 41 - 5 == 36
        assert 113 in OLD_PRIVATE_N and 41 in OLD_PRIVATE_N and 113 - 41 == 72

        complementary = None
        if k >= 1:
            leftover = [w for w in range(period)
                        if not any(w % r["m"] == r["b"] for r in rows[:k])]
            assert leftover == [2 ** k * t for t in range(3)]
            complementary = [[t for t, w in enumerate(leftover) if w % r["m"] == r["b"]]
                             for r in rows[k:]]
            assert complementary == ([[1], [0], [2]] if k % 2 == 0 else [[2], [1], [0]])
        patterns.append({
            "k": k, "supplement_size": k + 7, "total_size": k + 27,
            "rows": rows, "complete_w_period": period,
            "private_w_residues": chosen, "lifted_w_mod_35_zero": lifted,
            "private_tail_exponents": new_n,
            "multiplicity_counts": dict(sorted(Counter(map(len, hits)).items())),
            "complementary_t_phases": complementary,
        })

    transitions = []
    for k in range(8):
        before = {r["label"]: r for r in covering_rows(k)}
        after = {r["label"]: r for r in covering_rows(k + 1)}
        removed = sorted(before.keys() - after.keys())
        added = sorted(after.keys() - before.keys())
        retained = sorted(before.keys() & after.keys())
        assert removed == (["Z"] if k == 0 else [f"T{k-1}"])
        assert added == [f"D{k+1}", f"T{k+1}"]
        assert all(before[label] == after[label] for label in retained)
        changing = [before[removed[0]]["order2"]] + [after[label]["order2"] for label in added]
        assert changing == [54 * 2 ** k, 72 * 2 ** k, 216 * 2 ** k]
        transitions.append({"from_k": k, "removed": removed, "added": added,
                            "retained": retained, "changing_orders": changing})

    # Concrete complete n-period checks for both exceptional small members.
    concrete = []
    for k in (0, 1):
        tails = covering_rows(k)
        new_rows = [dict(r) for r in PREFIX]
        for row in tails:
            q, order = KNOWN[row["label"]]
            assert order == row["order2"]
            new_rows.append(dict(row, q=q))
        period = lcm(*ord_old.values(), *(r["order2"] for r in new_rows))
        masks = [0] * period
        for index, q in enumerate(P):
            for n in range(old_n_classes[q], period, ord_old[q]):
                masks[n] |= 1 << index
        for index, row in enumerate(new_rows, start=20):
            q, order, c = row["q"], row["order2"], row["u_phase"]
            residue = pow(2, -c, q)
            phase = 2 * c % order
            assert (residue * residue * pow(2, phase, q) - 1) % q == 0
            row["root_residue"] = residue
            for n in range(phase, period, order):
                masks[n] |= 1 << index
        assert all(masks)
        private_n = OLD_PRIVATE_N + [r["private_n"] for r in PREFIX] + patterns[k]["private_tail_exponents"]
        assert all(masks[n % period] == 1 << i for i, n in enumerate(private_n))
        concrete.append({"k": k, "complete_n_period": period, "uncovered_positions": 0,
                         "all_private_exponents": private_n, "numerical_extra_rows": new_rows})

    boundaries = []
    for BN in (1, 53, 54, 71, 72, 107, 108, 143, 144, 179, 180, 215, 216, 431, 432, 864, 1000, 1000000):
        j1, j2 = j_threshold(BN, 0), j_threshold(BN, 1)
        for lower, j in ((0, j1), (1, j2)):
            assert 54 * 2 ** j > BN
            assert j == lower or 54 * 2 ** (j - 1) <= BN
        boundaries.append({"B_N": BN, "R1_j": j1, "R1_first_cost": j1 + 7,
                           "R2_j": j2, "R2_first_cost": j2 + 7})

    # Representative finite prime-power observer fixtures. The proof handles
    # arbitrary N; these exercise both dictionary lifts and absent-prime zeroes.
    fixtures = [
        [(2, 8), (3, 4), (7, 3), (5, 3), (13, 2), (101, 2)],
        [(2, 5), (433, 3), (38737, 2), (246241, 2), (279073, 2), (87211, 2)],
        [(487824887233, 2), (33975937, 2), (61, 3), (109, 2), (19, 2), (73, 2)],
    ]
    known_label_for_q = {q: label for label, (q, _) in KNOWN.items()}
    observer_records = []
    for fixture in fixtures:
        orders = {q: exact_order(2, q) for q, _ in fixture if q != 2}
        BN = max([1] + list(orders.values()))
        j = j_threshold(BN, 0)
        assert j <= 8
        stable = {r["label"]: r for r in PREFIX + covering_rows(j)}
        pairs, lifts = [], []
        for q, power in fixture:
            modulus = q ** power
            label = next((r["label"] for r in PREFIX if r["q"] == q), known_label_for_q.get(q))
            if q == 2 or q in P:
                residue = ASTAR % modulus
                category = "old"
            elif label in stable:
                residue = pow(2, -stable[label]["u_phase"], modulus)
                category = "retained_dictionary"
            else:
                residue = 0
                category = "absent"
            pairs.append((residue, modulus))
            lifts.append({"q": q, "power": power, "category": category, "residue": residue})
            for k in range(j, 9):
                rows = {r["label"]: r for r in PREFIX + covering_rows(k)}
                if label is not None:
                    assert (label in stable) == (label in rows)
                    if label in stable:
                        assert rows[label] == stable[label]
                        assert residue % q == pow(2, -rows[label]["u_phase"], q)
                elif q not in P and q != 2:
                    matching = [r for r in rows.values() if r["order2"] == orders[q]]
                    assert all(r["label"] in KNOWN and KNOWN[r["label"]][0] != q for r in matching)
        rN, N = crt_coprime(pairs)
        assert all(rN % modulus == residue for residue, modulus in pairs)
        observer_records.append({"N": N, "r_N": rN, "B_N": BN, "start_k": j,
                                 "checked_through_k": 8, "prime_power_lifts": lifts})

    # One explicit observation for the complete twelve-coordinate budget-seven
    # observer. No enormous coprimalized root is needed for this CRT residue.
    T_primes = [181, 577, 631, 23311, 54001, 87211, 246241, 262657, 279073,
                18837001, 29247661, 487824887233]
    T_orders = {q: exact_order(2, q) for q in T_primes}
    assert all(prime_trial(q) for q in T_primes)
    assert max(T_orders.values()) == 180
    assert j_threshold(180, 1) == 2
    T_residues = {q: (pow(2, -34, q) if q == 246241 else
                      pow(2, -52, q) if q == 487824887233 else 0)
                  for q in T_primes}
    assert T_residues[246241] == 182629
    assert T_residues[487824887233] == 487823838657
    rT, T = crt_coprime([(T_residues[q], q) for q in T_primes])
    assert all(rT % q == T_residues[q] for q in T_primes)
    C_primes = {181, 631, 23311, 54001, 18837001, 29247661}
    D_primes = {87211, 246241, 262657, 279073}
    assert all(T_residues[q] == 0 for q in C_primes)
    assert [q for q in D_primes if T_residues[q] != 0] == [246241]
    assert T_residues[577] == 0
    T_application = {"additional_primes": T_primes, "T": T, "r_T": rT,
                     "orders": T_orders, "B_T": 180, "start_k": 2,
                     "root_residues": T_residues,
                     "all_later_exact_supplementary_costs": "every integer s>=9",
                     "all_later_exact_total_costs": "20+s",
                     "fixed_plus_additional_prime_trajectory_count": 43,
                     "seven_budget_family_predicates": {"binary": False, "ternary": False, "modulo_five": False}}

    result = {
        "status": "PASS: author exact arithmetic support; not independent project Review",
        "scope": {"activity": "RA-D2EC212845B63844081F9A14", "researcher": "EM-DIRECT-970E1C",
                  "new_native_execution": False, "independent_review": False},
        "old_prime_orders": ord_old, "old_private_exponents": OLD_PRIVATE_N,
        "known_seed_primes": known_prime_records,
        "primality_method": "deterministic trial division through integer square root",
        "checked_k": list(range(9)), "patterns": patterns, "adjacent_transitions": transitions,
        "concrete_complete_period_checks": concrete, "threshold_boundary_checks": boundaries,
        "prime_power_observer_fixtures": observer_records,
        "seven_budget_observer_application": T_application,
        "universal_R1_threshold": "j_N=min{j>=0:54*2^j>B_N}; all costs s>=j_N+7 in one residue fiber",
        "universal_R2_threshold": "j_N=min{j>=1:54*2^j>B_N}; all costs s>=j_N+7 in one residue fiber",
        "necessary_order_bounds": {"R1": "B_N >= (27/64)*2^b for b>=7",
                                   "R2": "B_N >= (27/64)*2^b for b>=8"},
        "external_existence_input": "Inherited base-two primitive-prime theorem for every requested exact order greater than six; two order-108 primes explicitly supplied.",
        "universal_proof": "proof.md Sections 2-7; finite checks are not an extrapolation to all k or all N",
    }
    output = Path(__file__).with_name("refinement_certificate.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "checked_k": result["checked_k"],
                      "costs": [k + 7 for k in range(9)],
                      "concrete_n_periods": [r["complete_n_period"] for r in concrete],
                      "concrete_private_term_counts": [len(r["all_private_exponents"]) for r in concrete],
                      "first_transition_orders": transitions[0]["changing_orders"],
                      "T": T, "r_T": rT,
                      "observer_fixture_count": len(observer_records), "output": str(output)}, indent=2))


if __name__ == "__main__":
    main()
