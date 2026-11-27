"""Exact anchor labels, available stages, and a named Riesel 12/13 switch."""

from collections import Counter
from itertools import combinations
import json
from math import gcd, isqrt, lcm, prod
from pathlib import Path


def prime(q):
    return q == 2 or q > 2 and q % 2 == 1 and all(q % d for d in range(3, isqrt(q) + 1, 2))


def exact_order(q, d):
    factors = [p for p in (2, 3, 5, 7) if d % p == 0]
    return pow(2, d, q) == 1 and all(pow(2, d // p, q) != 1 for p in factors)


def phase(q, a):
    d, value = 1, 2 % q
    while value != 1:
        d += 1
        value = 2 * value % q
    value = a * a % q
    for n in range(d):
        if value == 1:
            return q, d, n
        value = 2 * value % q
    raise ValueError(f"fixed label {q} has no phase")


def hits(descriptor, n):
    _, d, r = descriptor
    return n % d == r


def tail(q, d, w):
    return q, d, (32 + 36 * w) % d


def primitive_carrier(d, excluded):
    value = 2**d - 1
    bad = prod(2**(d // p) - 1 for p in (2, 3, 5, 7) if d % p == 0) * excluded
    while (common := gcd(value, bad)) > 1:
        value //= common
    return value


def comb(depth):
    return [(j, 2**(j - 1)) for j in range(1, depth + 1)] + [(depth, 0)]


def leaf_tree(depth, target_depth):
    if target_depth != depth - 1 or depth == 2:
        return comb(depth)
    if depth == 3:
        return [(2, r) for r in range(4)]
    leaves = comb(depth - 1)
    leaves.remove((1, 1))
    return leaves + [(2, 1), (2, 3)]


def check_tree(depth, target_depth):
    leaves = leaf_tree(depth, target_depth)
    picked = next(r for j, r in leaves if j == target_depth)
    j = target_depth + 1
    children = [(j, picked), (j, picked + 2**target_depth)]
    off = [leaf for leaf in leaves if leaf != (target_depth, picked)] + children
    slots = Counter(i for i, _ in leaves + children)
    assert all(count <= (4 if i == 2 else 3) for i, count in slots.items())
    assert len(leaves) == depth + 1 and len(off) == depth + 2
    for classes in (leaves, off):
        period = max(2**i for i, _ in classes)
        assert all(sum(u % (2**i) == r for i, r in classes) == 1 for u in range(period))


def minimum_cover(dictionary, extras, period):
    patterns = {
        sum(1 << i for i, row in enumerate(extras) if hits(row, n))
        for n in range(1, period + 1)
        if not any(hits(row, n) for row in dictionary)
    }
    assert 0 not in patterns
    forced = sum(mask for mask in patterns if mask.bit_count() == 1)
    remaining = [mask for mask in patterns if not mask & forced]
    optional = [1 << i for i in range(len(extras)) if not (1 << i) & forced]
    for size in range(len(optional) + 1):
        for selection in combinations(optional, size):
            cover = sum(selection)
            if all(mask & cover for mask in remaining):
                return {"cost": forced.bit_count() + size, "cover_patterns": len(patterns)}
    raise ValueError("activated coordinates do not cover")


def main():
    path = Path(__file__).with_name("RIESEL_R4_H20_ANCHOR_INPUTS_20261127.json")
    source = json.loads(path.read_text())
    a4, s4 = int(source["A4"]), int(source["S4"])
    fixed = set(map(int, source["fixed_primes"]))
    dictionary = source["dictionary"]
    prefix = source["prefix"]
    fixed_tails = source["fixed_tails"]
    free = source["free_anchors"]
    low = [q for q, _, _ in free]
    alternate = source["alternate_phase8_order240_prime"]
    named = set(dictionary + prefix + fixed_tails + low + source["depth2_order960_primes"]
                + source["named_budget12"] + [alternate] + [q for q, _, _ in source["named_budget14"]])
    assert len(fixed) == 74 and 6 * prod(fixed) == s4 and 0 < a4 < s4 and a4 % 6 == 3
    assert not fixed.intersection(low)
    assert all(a4 % q == 0 for q in fixed.difference(dictionary + prefix + fixed_tails))
    assert all(prime(q) for q in named)

    dict_phases = [phase(q, a4) for q in dictionary]
    prefix_phases = [phase(q, a4) for q in prefix]
    fixed_phases = [phase(q, a4) for q in fixed_tails]
    for descriptor, (h, w) in zip(fixed_phases, [(2, 1), (3, 1), (4, 2)]):
        assert descriptor[1] // gcd(descriptor[1], 36) == h and hits(descriptor, 32 + 36 * w)
    assert all(exact_order(q, d) for q, _, d in free)
    free_phases = [tail(q, d, w) for q, w, d in free]
    assert lcm(*(d for _, d, _ in dict_phases)) == 6720
    local_period = lcm(35, 140, *(d // gcd(d, 36) for _, d, _ in fixed_phases + free_phases))
    assert local_period == 420 and local_period // 20 % 2 == 1

    target_anchor = 4278255361
    auxiliary = 246241
    active = prefix_phases + fixed_phases + free_phases
    original_anchors = [row for row in active if row[0] != auxiliary]
    q_hole = primitive_carrier(5040, s4 * prod(low))
    assert q_hole > 1 and gcd(q_hole, s4 * prod(low)) == 1 and exact_order(q_hole, 5040)
    hole = q_hole, 5040, 3488
    baseline_period = lcm(5040, *(d for _, d, _ in dict_phases + active))
    assert baseline_period == 60480
    for n in range(1, baseline_period + 1):
        assert (not any(hits(row, n) for row in dict_phases + prefix_phases)) == (
            n % 36 == 32 and ((n - 32) // 36) % 35 in source["holes_mod35"]
        )
        assert (not any(hits(row, n) for row in dict_phases + original_anchors)) == hits(hole, n)
    anchor_order = prefix + [fixed_tails[0], fixed_tails[2]] + low
    private = dict(zip(anchor_order, map(int, source["private_indices"])))
    for q, n in private.items():
        assert [row[0] for row in dict_phases + active + [hole] if hits(row, n)] == [q]
    assert private[target_anchor] == 32 + 36 * 120
    assert [row[0] for row in dict_phases + active + [hole] if hits(row, 3488)] == [q_hole]

    # Across all depths only the finitely many d dividing q-1 can collide.
    old = fixed | set(low)
    depth_zero = {
        d: [q for q in sorted(old) if (q - 1) % d == 0 and exact_order(q, d)]
        for d in (80, 240, 720)
    }
    assert depth_zero == {80: [target_anchor], 240: [394783681], 720: []}
    assert alternate not in old and exact_order(alternate, 240)
    assert tail(alternate, 240, 8)[1:] == free_phases[-1][1:]
    collision_checks = 0
    for q in old:
        for base in (160, 480, 1440):
            d = base
            while (q - 1) % d == 0:
                assert not exact_order(q, d)
                collision_checks += 1
                d *= 2
    for q in source["depth2_order960_primes"]:
        assert q not in old and exact_order(q, 960)
    assert len(set(source["depth2_order960_primes"])) == 2
    for depth in range(1, 9):
        for j in range(1, depth + 1):
            check_tree(depth, j)

    def named_switch(budget, pivotal, order, added):
        assert all(q not in old and exact_order(q, d) for q, d, _ in added)
        assert len({row[0] for row in added}) == len(added)
        extras = [row for row in active if row[0] != target_anchor] + [hole] + added
        period = lcm(baseline_period, *(d for _, d, _ in extras))
        opened = minimum_cover(dict_phases, extras, period)
        closed = minimum_cover(dict_phases, [row for row in extras if row[0] != pivotal], period)
        assert (opened["cost"], closed["cost"]) == (budget, budget + 1)
        return {"target": pivotal, "order": order, "period": period,
                "opened": opened, "closed": closed, "common_and_target": added}

    pivotal, sibling, repair_left, repair_right = source["named_budget12"]
    added12 = [tail(pivotal, 160, 0), tail(sibling, 480, 20),
               tail(repair_left, 320, 0), tail(repair_right, 960, 40)]
    added14 = [tail(q, d, 20 * z) for q, d, z in source["named_budget14"]]
    print(json.dumps({
        "verified_named_primes": len(named),
        "fixed_labels": len(fixed),
        "private_anchor_indices": private,
        "anchor_private_progression_w": [120, local_period],
        "hole_carrier_bits": q_hole.bit_length(),
        "depth_zero_collisions": depth_zero,
        "alternate_phase8_order240_prime": alternate,
        "order_collision_checks": collision_checks,
        "old_phase_period": baseline_period,
        "checked_tree_depths": 8,
        "named_budget12": named_switch(12, pivotal, 160, added12),
        "named_budget14": named_switch(14, 286721, 640, added14),
    }, indent=2))


if __name__ == "__main__":
    main()
