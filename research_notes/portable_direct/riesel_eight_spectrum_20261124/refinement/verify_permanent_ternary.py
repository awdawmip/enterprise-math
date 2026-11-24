#!/usr/bin/env python3
"""Exact finite checks for the permanent-ternary consecutive-cover theorem.

This checks explicit input arithmetic and complete finite periods. The all-k,
all-modulus and exact-minimum arguments are in permanent_ternary_proof.md.
No native BRC execution or independent project review is claimed here.
"""

from collections import Counter
from math import gcd, isqrt, lcm
from pathlib import Path
import json

ASTAR = 690786768637635218740714348513373826260012289
P = [7, 17, 31, 41, 71, 97, 113, 127, 151, 241, 257, 281,
     337, 641, 673, 1321, 14449, 29191, 65537, 6700417]
OLD_N = [37, 3, 89, 5, 293, 117, 413, 113, 41, 33,
         87, 233, 773, 207, 237, 257, 53, 593, 63, 111]
H = {0, 1, 3, 6, 9, 10, 15, 16, 21, 30, 31, 33, 36, 45,
     48, 49, 51, 54, 55, 63, 64, 66, 69, 70, 75, 76, 78,
     79, 84, 85, 90, 91, 93, 96, 99, 100}
B = {0, 3, 5, 8, 10, 15, 21, 23, 26, 28, 30, 31, 33}
PREFIX = [
    dict(label="P5", q=5, order=4, c=1, private_n=6),
    dict(label="P13", q=13, order=12, c=0, private_n=12),
    dict(label="P19", q=19, order=18, c=4, private_n=152),
    dict(label="P73", q=73, order=9, c=1, private_n=20),
]
KNOWN = {
    "U": (87211, 54), "V": (279073, 108),
    "T0": (246241, 108), "T1": (33975937, 216),
    "D1": (38737, 72), "D2": (487824887233, 144),
}


def prime_trial(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


def factors(n):
    result = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            result.append(p)
            while n % p == 0:
                n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        result.append(n)
    return result


def order2(q):
    d = q - 1
    for p in factors(d):
        while d % p == 0 and pow(2, d // p, q) == 1:
            d //= p
    return d


def check_order(q, d):
    assert prime_trial(q)
    assert pow(2, d, q) == 1
    assert all(pow(2, d // p, q) != 1 for p in factors(d))


def row(label, m, b, order=None):
    return dict(label=label, m=m, b=b, order=order or 36 * m,
                c=16 + 18 * b)


def rows(k):
    return ([row(f"D{j}", 2**j, 2**(j-1)) for j in range(1, k+1)]
            + [row("U", 3, 1, 54), row("V", 3, 2, 108),
               row(f"T{k}", 3 * 2**k, 0)])


def hits_n(r, n):
    return n % r["order"] == 2 * r["c"] % r["order"]


def private_residues(k):
    return ([3 * 2**(j-1) for j in range(1, k+1)]
            + [2**k * (1 if k % 2 == 0 else 2),
               2**k * (2 if k % 2 == 0 else 1), 0])


def lift35(w, period):
    return 35 * ((w * pow(35, -1, period)) % period)


def threshold(BN, lower):
    j = lower
    while 72 * 2**j <= BN:
        j += 1
    return j


def crt_coprime(pairs):
    a, m = 0, 1
    for r, n in pairs:
        assert gcd(m, n) == 1
        a += m * ((r-a) * pow(m, -1, n) % n)
        m *= n
    return a, m


def main():
    old_orders = {p: order2(p) for p in P}
    assert max(old_orders.values()) == 105
    old_phases = {}
    for p, d in old_orders.items():
        zero = [n for n in range(d) if (ASTAR**2 * pow(2, n, p) - 1) % p == 0]
        assert len(zero) == 1
        old_phases[p] = zero[0]
    for p, n in zip(P, OLD_N):
        assert [q for q in P if n % old_orders[q] == old_phases[q]] == [p]
    for q, d in KNOWN.values():
        check_order(q, d)
        assert q not in P
    for r in PREFIX:
        check_order(r["q"], r["order"])
    assert [pow(2, -r["c"], r["q"]) for r in PREFIX] == [3, 1, 6, 37]
    assert pow(2, -34, 38737) == 38733

    # The original dictionary's exact even holes and the four fixed phases.
    assert {u for u in range(105) if not any(
        2*u % old_orders[q] == old_phases[q] for q in P)} == H
    remaining = {u for u in range(630) if u % 105 in H
                 and not any(hits_n(r, 2*u) for r in PREFIX)}
    assert remaining == {16+18*w for w in B}

    patterns = []
    for k in range(13):
        rs = rows(k)
        period = 3 * 2**k
        assert len(rs) == k+3 and lcm(*(r["m"] for r in rs)) == period
        hit_lists = [[i for i, r in enumerate(rs) if w % r["m"] == r["b"]]
                     for w in range(period)]
        assert all(hit_lists)
        chosen = private_residues(k)
        assert len(chosen) == len(rs)
        assert all(0 <= w < period and hit_lists[w] == [i]
                   for i, w in enumerate(chosen))
        for r in rs:
            assert r["order"] % 2 == 0
            assert all(hits_n(r, 32+36*w) == (w % r["m"] == r["b"])
                       for w in range(period))
        for r in PREFIX:
            assert r["private_n"]//2 % 105 in H
            assert [s["label"] for s in PREFIX + rs if hits_n(s, r["private_n"])] == [r["label"]]
        assert all(not any(hits_n(r, n) for r in PREFIX + rs) for n in OLD_N)
        lifted = [lift35(w, period) for w in chosen]
        private_n = [32+36*w for w in lifted]
        for i, n in enumerate(private_n):
            assert n//2 % 105 == 16
            assert [r["label"] for r in PREFIX + rs if hits_n(r, n)] == [rs[i]["label"]]
        assert len(set(OLD_N + [r["private_n"] for r in PREFIX] + private_n)) == k+27
        patterns.append(dict(k=k, cost=k+7, total_cost=k+27, w_period=period,
                             rows=rs, chosen_private_w=chosen,
                             lifted_private_w=lifted, private_n=private_n,
                             multiplicity_counts=dict(sorted(Counter(map(len, hit_lists)).items()))))

    transitions = []
    for k in range(12):
        before, after = ({r["label"]: r for r in rows(j)} for j in (k, k+1))
        retained = before.keys() & after.keys()
        removed = before.keys() - after.keys()
        added = after.keys() - before.keys()
        assert removed == {f"T{k}"}
        assert added == {f"D{k+1}", f"T{k+1}"}
        assert all(before[label] == after[label] for label in retained)
        orders = [before[f"T{k}"]["order"], after[f"D{k+1}"]["order"],
                  after[f"T{k+1}"]["order"]]
        assert orders == [108*2**k, 72*2**k, 216*2**k]
        transitions.append(dict(k=k, removed=f"T{k}", added=sorted(added),
                                retained=sorted(retained), changing_orders=orders,
                                minimum_changing_order=min(orders)))

    # Full numerical prime covers at the two smallest sizes; higher rows use
    # the inherited exact-order existence theorem in the written proof.
    concrete = []
    for k in (0, 1):
        rs = [dict(r) for r in rows(k)]
        for r in rs:
            r["q"] = KNOWN[r["label"]][0]
            assert KNOWN[r["label"]][1] == r["order"]
            r["root_residue"] = pow(2, -r["c"], r["q"])
            assert (r["root_residue"]**2 * pow(2, 2*r["c"], r["q"]) - 1) % r["q"] == 0
        nr = PREFIX + rs
        period = lcm(*old_orders.values(), *(r["order"] for r in nr))
        masks = [0] * period
        for i, q in enumerate(P):
            for n in range(old_phases[q], period, old_orders[q]):
                masks[n] |= 1 << i
        for i, r in enumerate(nr, start=20):
            for n in range(2*r["c"] % r["order"], period, r["order"]):
                masks[n] |= 1 << i
        assert all(masks)
        private_n = OLD_N + [r["private_n"] for r in PREFIX] + patterns[k]["private_n"]
        assert all(masks[n % period] == 1 << i for i, n in enumerate(private_n))
        concrete.append(dict(k=k, complete_n_period=period, uncovered_positions=0,
                             all_private_n=private_n, tail_rows=rs))

    # Check arbitrary finite precision on representative retained and absent
    # prime coordinates; no claim of exhaustive N enumeration is made.
    fixtures = [
        [(2, 8), (3, 4), (7, 3), (5, 3), (13, 2), (101, 2)],
        [(2, 5), (433, 3), (38737, 2), (246241, 2), (279073, 2), (87211, 2)],
        [(487824887233, 2), (33975937, 2), (61, 3), (109, 2), (19, 2), (73, 2)],
    ]
    label_for_q = {q: label for label, (q, _) in KNOWN.items()}
    label_for_q.update({r["q"]: r["label"] for r in PREFIX})
    observer_checks = []
    for fixture in fixtures:
        BN = max([1] + [order2(q) for q, _ in fixture if q != 2])
        j = threshold(BN, 0)
        stable = {r["label"]: r for r in PREFIX + rows(j)}
        lifts = []
        for q, e in fixture:
            modulus, label = q**e, label_for_q.get(q)
            if q == 2 or q in P:
                r, category = ASTAR % modulus, "old"
            elif label in stable:
                r, category = pow(2, -stable[label]["c"], modulus), "retained"
            else:
                r, category = 0, "absent"
            for k in range(j, 13):
                now = {r["label"]: r for r in PREFIX + rows(k)}
                if label is not None:
                    assert (label in stable) == (label in now)
                    if label in stable:
                        assert stable[label] == now[label]
                        assert r % q == pow(2, -now[label]["c"], q)
            lifts.append(dict(q=q, e=e, residue=r, category=category))
        rN, N = crt_coprime([(x["residue"], x["q"]**x["e"]) for x in lifts])
        assert all(rN % x["q"]**x["e"] == x["residue"] for x in lifts)
        observer_checks.append(dict(N=N, rN=rN, BN=BN, j=j, lifts=lifts))

    bounds = []
    for BN in (1, 53, 54, 71, 72, 107, 108, 143, 144, 179, 180,
               215, 216, 287, 288, 431, 432, 575, 576, 1000):
        js = [threshold(BN, lower) for lower in (0, 1)]
        assert all(72*2**j > BN for j in js)
        bounds.append(dict(BN=BN, R1_j=js[0], R2_j=js[1]))

    data = dict(status="PASS", scope="Author collaboration, exact arithmetic checks; no independent project Review or new native execution",
                old_prime_orders=old_orders, seed_primes=KNOWN,
                checked_k=list(range(13)), patterns=patterns, transitions=transitions,
                concrete=concrete, prime_power_fixtures=observer_checks, thresholds=bounds,
                theorem=dict(R1="j=min{j>=0:72*2^j>B_N}; all exact costs s>=j+7",
                             R2="j=min{j>=1:72*2^j>B_N}; all exact costs s>=j+7",
                             observer_bound_R1="Omega_b >= (9/16)*2^b for b>=7",
                             observer_bound_R2="Omega_b >= (9/16)*2^b for b>=8"))
    output = Path(__file__).with_name("permanent_ternary_certificate.json")
    output.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(dict(status="PASS", checked_k=list(range(13)),
                          first_changing_orders=transitions[0]["changing_orders"],
                          concrete_periods=[x["complete_n_period"] for x in concrete],
                          concrete_private_terms=[len(x["all_private_n"]) for x in concrete],
                          observer_fixtures=len(observer_checks), output=str(output)), indent=2))


if __name__ == "__main__":
    main()
