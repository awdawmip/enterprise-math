"""Exact necessary 2-adic sieve for a signed T6 v2=5 population gap of 64.

Inputs: per-side mass <=2331, proven cancellation for v2>=6, and S1..S6 equality.
All calculations use exact integer and modular arithmetic, never sampling.
"""
from collections import deque, Counter
from functools import lru_cache
import heapq

K = tuple(range(1, 7))
M = tuple(1 << k for k in K)
M2 = tuple(1 << (2 * k) for k in K)
ZERO = (0,) * 6


def add(a, b):
    return tuple((x + y) % mod for x, y, mod in zip(a, b, M))


@lru_cache(None)
def partitions(n, cap):
    if n == 0:
        return ((),)
    return tuple(
        (h,) + tail
        for h in range(min(n, cap), 0, -1)
        for tail in partitions(n - h, h)
    )


POW = {
    a: tuple(pow(1 + 2 * a, -k, M2[k - 1]) for k in K)
    for a in range(36)
}


def vector(n, parts):
    return tuple(
        (n + sum(POW[a][i] - 1 for a in parts)) % M2[i]
        for i in range(6)
    )


def subgroup():
    gens = [tuple(pow(j, -k, M[k - 1]) for k in K)
            for j in range(1, 64, 2)]
    reached = {ZERO}
    queue = deque([ZERO])
    while queue:
        v = queue.popleft()
        for g in gens:
            w = add(v, g)
            if w not in reached:
                reached.add(w)
                queue.append(w)
    assert len(reached) == 2048
    return reached


def min_v4_costs():
    # The maximal residual side budget here is 640.
    # The j=41 generator costs 655 and cannot affect any admissible result.
    gens = [(16 * j - 1, tuple(pow(j, -k, M[k - 1]) for k in K))
            for j in range(1, 42, 2)]
    dist = {ZERO: 0}
    heap = [(0, ZERO)]
    while heap:
        c, v = heapq.heappop(heap)
        if c != dist[v]:
            continue
        for cost, g in gens:
            w = add(v, g)
            nc = c + cost
            if nc < dist.get(w, 10 ** 9):
                dist[w] = nc
                heapq.heappush(heap, (nc, w))
    assert len(dist) == 2048
    return dist


def required_v4(heavy, light):
    d = tuple((x - y) % mod for x, y, mod in zip(heavy, light, M2))
    if any(value % m for value, m in zip(d, M)):
        return None
    return tuple((-(value // m)) % m for value, m in zip(d, M))


def main():
    G = subgroup()
    dist = min_v4_costs()
    all_pairs = first_tier = group_tier = budget_tier = 0
    final = []
    for low_count in range(12):
        high_count = 64 + low_count
        heavy_options = [
            (a, parts, vector(high_count, parts))
            for a in range((2331 - 31 * high_count) // 64 + 1)
            for parts in partitions(a, a)
            if len(parts) <= high_count
        ]
        light_options = [
            (b, parts, vector(low_count, parts))
            for b in range((2331 - 31 * low_count) // 64 + 1)
            for parts in partitions(b, b)
            if len(parts) <= low_count
        ]
        stage = [0, 0, 0, 0]
        for a, pa, heavy in heavy_options:
            ra = 2331 - (31 * high_count + 64 * a)
            for b, pb, light in light_options:
                rb = 2331 - (31 * low_count + 64 * b)
                stage[0] += 1
                target = required_v4(heavy, light)
                if target is None:
                    continue
                stage[1] += 1
                if target not in G:
                    continue
                stage[2] += 1
                if not any(
                    dist[v] <= rb and dist[add(v, target)] <= ra
                    for v in G
                ):
                    continue
                stage[3] += 1
                final.append((low_count, pa, pb, ra, rb))
        all_pairs += stage[0]
        first_tier += stage[1]
        group_tier += stage[2]
        budget_tier += stage[3]
        print(f"low_count={low_count} tested={stage[0]} tier1={stage[1]} "
              f"unbounded_v4_group={stage[2]} budgeted_v4={stage[3]}")
    assert (all_pairs, first_tier, group_tier, budget_tier) == (382145, 2906, 39, 7)
    assert Counter(x[0] for x in final) == {5: 1, 6: 2, 7: 2, 8: 2}
    print(f"PASS 64-count-gap: {all_pairs} full budget pairs -> {first_tier} "
          f"local -> {group_tier} group -> {budget_tier} budgeted v4 candidates")
    print("7 surviving (light_count, heavy_excess_parts, light_excess_parts, "
          "heavy_residual_mass, light_residual_mass):")
    for item in final:
        print(item)


if __name__ == "__main__":
    main()
