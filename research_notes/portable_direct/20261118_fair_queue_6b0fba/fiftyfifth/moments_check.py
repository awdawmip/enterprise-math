#!/usr/bin/env python3
"""Exact non-17 primary signatures for the fixed order-(7,7) T6 roster."""
import argparse
import hashlib
import json
from itertools import combinations
from pathlib import Path

CAP = 2331
ROSTER_SHA = "242e4872003368905b9355fc666c307a6182482152922b83273708b1a1d07e54"
PRIMES = (2, 3, 5, 7, 11, 13, 17)
STAGES = ((13, 1), (11, 1), (5, 2), (3, 2), (2, 3), (7, 1))
PEEL = (7, 11, 13, 25)
DEGREES = (1, 2, 3, 4, 5, 6)
ZERO = (0,) * 6


def smooth(n):
    for p in PRIMES:
        while n % p == 0:
            n //= p
    return n == 1


def order(n, p):
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v


def roster():
    atoms = [(q, r) for q in range(1, 8) for r in range(1, 17) if smooth(17*q + r)]
    den = [17*(17*q + r) for q, r in atoms]
    sides = []
    budgets = []

    def visit(qleft, cap, start, seq):
        if qleft == 0:
            sides.append(seq)
            budgets.append(cap)
            return
        for k in range(start, len(atoms)):
            q = atoms[k][0]
            if q > qleft:
                break
            if den[k]-1 <= cap:
                visit(qleft-q, cap-den[k]+1, k, seq+(k,))

    visit(7, CAP, 0, ())
    return atoms, den, sides, budgets


class Primary:
    """Coordinate j represents p^(hj)/d^j modulo p^((h-t+1)j)."""

    def __init__(self, p, t, denominators):
        self.p = p
        self.h = max(order(d, p) for d in denominators)
        self.moduli = tuple(p**((self.h - t + 1)*j) for j in DEGREES)

    def value(self, d):
        p = self.p
        v = order(d, p)
        unit = d // p**v
        return tuple(pow(p**(self.h-v) * pow(unit, -1, m), j, m)
                     for j, m in zip(DEGREES, self.moduli))

    def add(self, a, b):
        return tuple((x+y) % m for x, y, m in zip(a, b, self.moduli))

    def difference(self, a, b):
        return tuple((x-y) % m for x, y, m in zip(a, b, self.moduli))


def dictionary(group, den, limit):
    """DFS emits each affordable multiset once. Store minimum cost for each value."""
    weights = [(d-1, group.value(d)) for d in den]
    cheapest = {}
    raw = 0

    def visit(start, cost, key):
        nonlocal raw
        raw += 1
        if cost < cheapest.get(key, limit+1):
            cheapest[key] = cost
        for i in range(start, len(weights)):
            w, v = weights[i]
            if cost + w > limit:
                break
            visit(i, cost+w, group.add(key, v))

    visit(0, 0, ZERO)
    # Separate scalar generating-function count of all multisets of each cost.
    count = [1] + [0]*limit
    for w, _ in weights:
        for b in range(w, limit+1):
            count[b] += count[b-w]
    assert raw == sum(count)
    return cheapest, raw


def vertical(group, den, sides):
    values = [group.value(d) for d in den]
    return [tuple(sum(values[k][j] for k in side) % group.moduli[j] for j in range(6))
            for side in sides]


def bit_indices(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length()-1
        mask -= bit


def postings(candidates, group, base, budgets, costs):
    # A previous side occurs in this posting precisely if it attained the same total.
    owners = {}
    for i, (shift, cap) in enumerate(zip(base, budgets)):
        hits = 0
        bit = 1 << i
        for c, key in costs:
            if c > cap:
                break
            total = group.add(shift, key)
            previous = owners.get(total, 0)
            hits |= previous
            owners[total] = previous | bit
        candidates[i] &= hits


def direct(candidates, group, base, budgets, costs, cheapest):
    # The same test after few pairs survive. Probe a smaller dictionary against the larger.
    for i, mask in enumerate(candidates):
        for j in bit_indices(mask):
            a, b = (i, j) if budgets[i] <= budgets[j] else (j, i)
            delta = group.difference(base[a], base[b])
            found = False
            for cost, key in costs:
                if cost > budgets[a]:
                    break
                partner_cost = cheapest.get(group.add(key, delta))
                if partner_cost is not None and partner_cost <= budgets[b]:
                    found = True
                    break
            if not found:
                candidates[i] ^= 1 << j


def terminal_projection(group, base, budgets, cheapest, pair):
    # In this restricted dictionary, test which subsets of moments can eliminate the pair.
    i, j = pair
    left, right = [{group.add(base[a], k) for k, b in cheapest.items() if b <= budgets[a]}
                   for a in pair]
    assert left.isdisjoint(right)
    rejected = []
    tested = 0
    for n in range(1, 7):
        for js in combinations(range(6), n):
            def select(key):
                return tuple(key[t] for t in js)
            l = {select(x) for x in left}
            tested += 1
            if all(select(y) not in l for y in right):
                rejected.append([j+1 for j in js])
        if rejected:
            break
    return {"ordered_indices": [i, j], "full_spectrum_sizes": [len(left), len(right)],
            "joint_vectors_in_common": 0, "least_number_of_separator_coordinates": n,
            "all_minimum_degree_sets": rejected, "coordinate_subsets_checked": tested}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--roster', type=Path, help='optional original frozen roster JSON to verify')
    args = parser.parse_args()
    atoms, den, sides, budgets = roster()
    if args.roster:
        data = args.roster.read_bytes()
        assert hashlib.sha256(data).hexdigest() == ROSTER_SHA
        source = json.loads(data)
        assert source["atoms"] == [list(a) for a in atoms]
        assert source["roster_index_arrays"] == [list(s) for s in sides]

    limit = max(budgets)
    future = [d for d in range(2, limit+2) if smooth(d)]
    masks = [sum(1 << a for a in set(s)) for s in sides]
    candidates = [sum(1 << j for j in range(i) if not (mask & masks[j]))
                  for i, mask in enumerate(masks)]
    total = sum(x.bit_count() for x in candidates)
    assert (len(sides), len(atoms), total, limit) == (1907, 60, 809566, 292)
    stages = []
    injective = set()
    for p, t in STAGES:
        group = Primary(p, t, den+future)
        relevant = [d for d in future if d % p**t == 0]
        cheapest, raw = dictionary(group, relevant, limit)
        base = vertical(group, den, sides)
        costs = sorted((b, key) for key, b in cheapest.items())
        if p == 7:
            direct(candidates, group, base, budgets, costs, cheapest)
        else:
            postings(candidates, group, base, budgets, costs)
        if len(cheapest) == raw:
            injective.add(p**t)
        stages.append({"p": p, "minimum_valuation": t, "max_valuation": group.h,
                       "atom_types": len(relevant), "raw_multisets": raw,
                       "signatures": len(cheapest), "remaining_pairs":sum(x.bit_count() for x in candidates)})
        del cheapest, costs

    pairs = [(i, j) for i, mask in enumerate(candidates) for j in bit_indices(mask)]
    assert pairs == [(1808, 0), (1899, 277), (1899, 1204)]
    assert set(PEEL) <= injective
    for i, j in pairs:
        assert all(den[k] % u for k in sides[i]+sides[j] for u in PEEL)
    retained = [d for d in future if all(d % u for u in PEEL)]
    group = Primary(3, 2, den+retained)
    relevant = [d for d in retained if d % 9 == 0]
    cheapest, raw = dictionary(group, relevant, limit)
    base = vertical(group, den, sides)
    final = []
    for pair in pairs:
        result = terminal_projection(group, base, budgets, cheapest, pair)
        result["vertical_denominators"] = [[den[k] for k in sides[i]] for i in pair]
        result["budgets"] = [budgets[i] for i in pair]
        final.append(result)

    answer = {"side_mass_bound": CAP, "roster_source_sha256": ROSTER_SHA,
              "roster_count": len(sides), "named_vertical_atoms":len(atoms), "disjoint_pairs":total,
              "future_max_denominator":limit+1, "stage_statistics":stages,
              "injective_divisibility_thresholds":sorted(injective),
              "terminal_prime":3, "terminal_minimum_valuation":2, "terminal_max_valuation":group.h,
              "terminal_projected_dictionary":relevant, "terminal_raw_multisets":raw,
              "terminal_distinct_signatures":len(cheapest), "terminal_pairs":final,
              "surviving_completed_pairs":0, "tested_17_adic_affine_instances":0}
    print(json.dumps(answer, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
