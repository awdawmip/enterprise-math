"""Replay HHH private progressions, inventory checks and named Riesel switches."""

from collections import Counter
from hashlib import sha256
from math import gcd, lcm, prod
from pathlib import Path
import argparse
import json
import runpy

SOURCE_NAMES = {
    "RIESEL_R4_H20_ANCHOR_INPUTS_20261127.json":
        "7c60ff48f2e3caa582f1426c011bee4cdbce786294ea07447fdcdf345c8110a4",
    "RIESEL_R4_H20_ANCHOR_REPLAY_20261127.py":
        "586f75284498b3f19c6344642c3096caf73da6ab122333df06e1af763635ce56",
}


def run(anchor_dir):
    for name, wanted in SOURCE_NAMES.items():
        assert sha256((anchor_dir / name).read_bytes()).hexdigest() == wanted
    source = json.loads((anchor_dir / next(iter(SOURCE_NAMES))).read_text())
    reused = runpy.run_path(str(anchor_dir / "RIESEL_R4_H20_ANCHOR_REPLAY_20261127.py"))
    prime, order, phase, hits, tail = (reused[key] for key in ("prime", "exact_order", "phase", "hits", "tail"))
    primitive, min_cover, comb = (reused[key] for key in ("primitive_carrier", "minimum_cover", "comb"))

    a4, s4 = map(int, (source["A4"], source["S4"]))
    fixed = set(map(int, source["fixed_primes"]))
    dict_q, prefix_q, tails_q = (source[key] for key in ("dictionary", "prefix", "fixed_tails"))
    dictionary = [phase(q, a4) for q in dict_q]
    prefix = [phase(q, a4) for q in prefix_q]
    fixed_a, optional_r, fixed_u = [phase(q, a4) for q in tails_q]
    backbone = prefix + [fixed_a, fixed_u]
    assert len(fixed) == 74 and s4 == 6*prod(fixed) and 0 < a4 < s4 and a4 % 6 == 3
    assert all(a4 % q == 0 for q in fixed - set(dict_q + prefix_q + tails_q))
    assert len(backbone) == 6
    assert lcm(*(d for _, d, _ in dictionary)) == 6720
    assert (fixed_a[1] // gcd(fixed_a[1], 36), fixed_u[1] // gcd(fixed_u[1], 36)) == (2, 4)

    B = set(source["holes_mod35"])
    slots = [0, 8, 16]
    private_w = [0, 108, 336]
    global_parents = [((32 + 36*a) % 80) for a in slots]
    assert global_parents == [32, 0, 48] and all(p % 16 == 0 for p in global_parents)
    assert [w for w in range(0, 20, 4) if w % 5 in {r % 5 for r in B}] == slots
    bases = [(4278255361, 80, 0), (394783681, 240, 8), (8369281, 720, 16)]
    base_rows = [tail(q, d, a) for q, d, a in bases]
    all_rows = dictionary + backbone + [optional_r] + base_rows
    period = lcm(*(d for _, d, _ in all_rows))
    assert period == 60480
    assert all(q not in fixed and order(q, d) for q, d, _ in bases)
    for n in range(1, period + 1):
        w = (n-32)//36
        hole = n % 36 == 32 and w % 35 in B
        assert (not any(hits(r,n) for r in dictionary + prefix)) == hole
        if hole:
            assert hits(fixed_a,n) == (w % 2 == 1)
            assert hits(optional_r,n) == (w % 3 == 1)
            assert hits(fixed_u,n) == (w % 4 == 2)
            assert sum(hits(r,n) for r in base_rows) == (w % 4 == 0)
        assert any(hits(r,n) for r in dictionary + backbone + base_rows)
    for (q, _, _), n in zip(backbone, map(int, source["private_indices"][:6])):
        assert n % 16 != 0
        assert [r[0] for r in all_rows if hits(r,n)] == [q]
    for (q, _, a), w in zip(bases, private_w):
        assert w % 20 == a and w % 35 in B and w % 3 != 1
        n = 32 + 36*w
        assert [r[0] for r in all_rows if hits(r,n)] == [q]
    assert 420 == lcm(20, 35, 3) and 420//20 == 21

    checks = 0
    for q in fixed:
        for d0 in (80,240,720):
            d = d0
            while (q-1) % d == 0:
                assert not order(q, d)
                d *= 2
                checks += 1

    second160, prime1440 = 44479210368001, 37441
    assert 2**64 - 2**48 + 2**32 - 2**16 + 1 == 414721 * second160
    assert primitive(160, prod(fixed)) == 414721 * second160 and order(second160, 160)
    assert order(prime1440, 1440)
    assert all(order(q, 960) for q in source["depth2_order960_primes"])
    named_q = {q for q, _, _ in bases}
    named_q.update([second160, prime1440, *source["depth2_order960_primes"],
                    *source["named_budget12"], *(q for q, _, _ in source["named_budget14"])])
    assert all(prime(q) for q in named_q)

    for depth in range(1, 10):
        for j in range(1, depth+1):
            reused["check_tree"](depth, j)
    for depth in range(10):
        zero_tree = comb(depth)
        inventory = Counter(i for i, _ in zero_tree + [(1,0),(1,1)] if i)
        assert all(n <= (4 if depth == i == 1 else 3) for i,n in inventory.items())
        assert all(sum(u % (2**i) == a for i,a in zero_tree) == 1 for u in range(2**depth))

    def check_named(budget, q, added):
        extras = backbone + [optional_r] + [tail(p,d,a) for p,d,a in added]
        assert len(set(r[0] for r in extras)) == len(extras)
        for p,d,_ in added:
            assert p in named_q and p not in fixed and order(p,d)
        common_period = lcm(*(d for _,d,_ in dictionary + extras))
        opened = min_cover(dictionary, extras, common_period)
        closed = min_cover(dictionary, [row for row in extras if row[0] != q], common_period)
        assert (opened["cost"], closed["cost"]) == (budget, budget+1)
        return {"q": q, "period": common_period, "opened": opened, "closed": closed,
                "extra_h_triples_q_d_w": added}

    zero_trial = [bases[0], bases[2], (414721,160,0), (23041,480,20),
                  (second160,160,8), (prime1440,1440,28)]
    one_trial = bases[1:] + [(414721,160,0),(23041,480,20),
                             (3602561,320,0),(26881,960,40)]
    three_trial = bases[1:] + [(q,d,20*u) for q,d,u in source["named_budget14"]]
    return {
        "fixed_coordinates": len(fixed), "named_primality_checked": len(named_q),
        "fixed_order_collision_checks": checks, "private_exponents_of_fixed_backbone": source["private_indices"][:6],
        "base_period_checked": period, "private_slot_initial_w": private_w, "private_slot_period_w": 420,
        "global_parent_residues_mod80": global_parents, "primitive_order160_second_prime": second160,
        "order1440_named_prime": prime1440, "positive_tree_pairs_checked": 45, "zero_depth_trees_checked": 10,
        "named_zero_depth_budget10": check_named(10, 4278255361, zero_trial),
        "named_positive_depth_budget10": check_named(10, 414721, one_trial),
        "named_depth3_budget12": check_named(12, 286721, three_trial),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--anchor-dir", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    print(json.dumps(run(args.anchor_dir), indent=2, sort_keys=True))
