"""Exact replay for the RR colored/uncolored dyadic switch construction."""

from hashlib import sha256
from math import gcd, lcm, prod
from pathlib import Path
from collections import Counter
import argparse
import json
import runpy

INPUT_NAME = "RIESEL_R4_H20_ANCHOR_INPUTS_20261127.json"
HELPER_NAME = "RIESEL_R4_H20_ANCHOR_REPLAY_20261127.py"
INPUT_SHA = "7c60ff48f2e3caa582f1426c011bee4cdbce786294ea07447fdcdf345c8110a4"
HELPER_SHA = "586f75284498b3f19c6344642c3096caf73da6ab122333df06e1af763635ce56"
D864 = (68016300334849, 7311824282729722035859309520826138827918372038863677678267962656996811009)


def local_slot(k, residue, color):
    period = 1 << k
    if color is None:
        return period, residue
    base = next(residue + shift * period for shift in range(3)
                if (residue + shift * period) % 3 == color)
    return 3 * period, base


def run(anchor_dir):
    for name, expected in ((INPUT_NAME, INPUT_SHA), (HELPER_NAME, HELPER_SHA)):
        assert sha256((anchor_dir / name).read_bytes()).hexdigest() == expected
    source = json.loads((anchor_dir / INPUT_NAME).read_text())
    helper = runpy.run_path(str(anchor_dir / HELPER_NAME))
    phase, tail, order, hits = (helper[k] for k in ("phase", "tail", "exact_order", "hits"))
    primitive, prime, comb, min_cover = (helper[k] for k in ("primitive_carrier", "prime", "comb", "minimum_cover"))

    a4, s4 = map(int, (source["A4"], source["S4"]))
    fixed = set(map(int, source["fixed_primes"]))
    dict_q, prefix_q, tails_q = (source[k] for k in ("dictionary", "prefix", "fixed_tails"))
    assert len(fixed) == 74 and s4 == 6 * prod(fixed) and 0 < a4 < s4 and a4 % 6 == 3
    assert all(a4 % q == 0 for q in fixed - set(dict_q + prefix_q + tails_q))
    dictionary = [phase(q, a4) for q in dict_q]
    prefix = [phase(q, a4) for q in prefix_q]
    fixed_a, fixed_r, fixed_u = [phase(q, a4) for q in tails_q]
    backbone = prefix + [fixed_a, fixed_u]
    active_base = dictionary + backbone + [fixed_r]
    geometry_period = lcm(*(d for _, d, _ in active_base))
    assert lcm(*(d for _, d, _ in dictionary)) == 6720
    for (q, _, _), n in zip(backbone, map(int, source["private_indices"][:6])):
        assert n % 16
        assert [row[0] for row in active_base if hits(row, n)] == [q]
    B = set(source["holes_mod35"])
    for n in range(1, geometry_period+1):
        w = (n-32)//36
        hole = n % 36 == 32 and w % 35 in B
        assert (not any(hits(row,n) for row in dictionary + prefix)) == hole
        assert (not any(hits(row,n) for row in dictionary + backbone)) == (hole and w % 4 == 0)
        if hole:
            assert hits(fixed_r,n) == (w % 3 == 1)
    assert 0 in B
    assert all(gcd(35, 3 * 2**k) == 1 for k in range(1, 13))

    excluded = prod(fixed)
    for d in (32,96,288,64):
        assert primitive(d, excluded) == 1
    assert primitive(864, excluded) == prod(D864) and gcd(*D864) == 1
    assert all(order(q,864) for q in D864)
    h16 = (18446744069414584321,3457,816769)
    for q,d in zip(h16,(192,576,576)):
        assert gcd(q,excluded) == 1 and primitive(d,excluded) % q == 0 and order(q,d)
    checks = Counter()
    for q in fixed:
        for base in (432,128,384,1152):
            d = base
            while (q-1) % d == 0:
                assert not order(q,d)
                checks[base] += 1
                d *= 2

    def cover_census(t, slots, target_id):
        rows = [(i, *local_slot(k, residue, color)) for i, (k, residue, color) in enumerate(slots)]
        period = lcm(*(h for _,h,_ in rows))
        on = min_cover([], rows, period)
        off = min_cover([], [row for row in rows if row[0] != target_id], period)
        assert on["cost"] == t+3 and off["cost"] == t+4

    positive_count = 0
    zero_count = 0
    for t in range(10):
        for j in range(1,t+1):
            leaves = comb(t)
            picked = 0 if j == t else 2**(j-1)
            slots = [(0,0,1),(0,0,2)]
            for k,r in leaves:
                color = 0 if k == 1 or (k,r) == (j,picked) else None
                slots.append((k,r,color))
            target_id = slots.index((j,picked,0))
            slots += [(j+1,picked,0),(j+1,picked+2**j,None)]
            count = Counter((k,color is None) for k,_,color in slots)
            assert count[1,False] <= 2
            assert all(count[k,True] <= 3 for k in range(2,t+2))
            for k in range(2,t+2):
                assert count[k,False] <= 1
            cover_census(t,slots,target_id)
            positive_count += 1
        if t == 0:
            zero = [(0,0,0),(0,0,1),(0,0,2),(1,0,0),(1,1,0)]
        elif t == 1:
            zero = [(0,0,0),(0,0,1),(1,0,2),(1,1,2)] + [
                (2,r,None) for r in (1,2,3)] + [(3,0,None),(3,4,None)]
        else:
            zero = [(0,0,0),(0,0,1)] + [(k,r,2 if k == 1 else None) for k,r in comb(t)]
            zero += [(2,1,0),(2,3,None)]
        cover_census(t,zero,0)
        zero_count += 1

    p432, p1728, p128, p2304 = 209924353, 1718990209, 274177, 18433
    assert all(prime(q) for q in (p432,p1728,p128,p2304,3457,816769))
    d3456 = primitive(3456, excluded)
    d6912 = primitive(6912, excluded)
    d384 = primitive(384, excluded)
    geometry2 = [(p432,432,0,0,0), (D864[0],864,1,0,2), (D864[1],864,1,1,2),
                 (h16[0],192,2,1,None),(h16[1],576,2,2,None),(h16[2],576,2,3,None),
                 (p128,128,3,0,None),(d384,384,3,4,None)]
    geometry3 = [(p432,432,0,0,2),(D864[0],864,1,1,0),(3457,576,2,2,None),
                 (p1728,1728,2,0,0),(d3456,3456,3,0,0),(p128,128,3,4,None)]
    geometry4 = [(p432,432,0,0,2),(D864[0],864,1,1,0),(3457,576,2,2,None),
                 (p128,128,3,4,None),(d3456,3456,3,0,0),
                 (d6912,6912,4,0,0),(p2304,2304,4,8,None)]

    def named(budget, data, toggle):
        rows = []
        for q,d,k,r,color in data:
            h,v = local_slot(k,r,color)
            assert q > 1 and primitive(d,excluded) % q == 0 and order(q,d)
            assert d//gcd(d,144) == h and d % 16 == 0
            rows.append(tail(q,d,4*v))
        assert all(gcd(row[0],other[0]) == 1 for i,row in enumerate(rows) for other in rows[i+1:])
        extras = backbone + [fixed_r] + rows
        period = lcm(*(d for _,d,_ in dictionary + extras))
        on = min_cover(dictionary, extras, period)
        off = min_cover(dictionary, [row for row in extras if row[0] != toggle], period)
        assert (on["cost"],off["cost"]) == (budget,budget+1)
        return {"target_carrier":str(toggle),"period":period,"on":on,"off":off,
                "slot_q_order_binary_depth_binary_residue_color": [[str(q),d,k,r,c] for q,d,k,r,c in data]}

    return {
        "fixed_coordinates":len(fixed),"base_period_checked":geometry_period,
        "fixed_order_collision_checks":checks,"order864_coprime_carriers":[str(q) for q in D864],
        "uncolored_depth2_carriers":[str(q) for q in h16],
        "positive_tree_pairs_checked":positive_count,"zero_depth_tree_pairs_checked":zero_count,
        "zero_depth_budget10":named(10,geometry2,p432),
        "named_order1728_budget11":named(11,geometry3,p1728),
        "new_order3456_any_factor_budget12":named(12,geometry4,d3456),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--anchor-dir", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    print(json.dumps(run(args.anchor_dir), indent=2, sort_keys=True))
