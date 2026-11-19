"""Periodic Gaussian-norm avoidance, by separated tiles and exact finite strip transfers."""
import argparse
import hashlib
import json
from collections import Counter, deque
from functools import lru_cache
from math import gcd, isqrt

BASE = 65
SIDE = 13
SMALL_LIMIT = 2 * (26 + 12) ** 2
KING = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i or j]


def admissible(x, y, modulus):
    return gcd(x * x + y * y, modulus) == 1


def tile_components(i, j):
    points = {(x, y) for x in range(SIDE) for y in range(SIDE)
              if admissible(SIDE * i + x, SIDE * j + y, BASE)}
    parts = []
    while points:
        root = min(points)
        points.remove(root)
        component = [root]
        for x, y in component:
            for dx, dy in KING:
                dst = x + dx, y + dy
                if dst in points:
                    points.remove(dst)
                    component.append(dst)
        parts.append(frozenset(component))
    return sorted(parts, key=lambda c: (-len(c), min(c)))


def tile_proof():
    period = BASE // SIDE
    chosen = {}
    sizes = []
    for i in range(period):
        for j in range(period):
            parts = tile_components(i, j)
            assert len(parts) == 1 or len(parts[0]) > len(parts[1])
            chosen[i, j] = parts[0]
            sizes.append([i, j, len(parts[0]), len(parts[1]) if len(parts) > 1 else 0])
    edge_counts = []
    for (i, j), old in chosen.items():
        for di, dj in [(1, 0), (0, 1)]:
            new = chosen[(i + di) % period, (j + dj) % period]
            count = sum((x + dx - SIDE * di, y + dy - SIDE * dj) in new
                        for x, y in old for dx, dy in KING)
            assert count > 0
            edge_counts.append([i, j, di, dj, count])
    return {"tiles_i_j_largest_second": sizes, "edges_i_j_di_dj_multiplicity": edge_counts,
            "largest_size": max(v[2] for v in sizes), "least_join_count": min(v[-1] for v in edge_counts)}


def split_primes(limit):
    table = bytearray(b"\1") * (limit + 1)
    for p in range(2, isqrt(limit) + 1):
        if table[p]:
            table[p*p::p] = bytes((limit - p*p) // p + 1)
    return [p for p in range(5, limit + 1, 4) if table[p] and p not in (5, 13)]


def root_minus_one(p):
    for a in range(2, p):
        root = pow(a, (p - 1) // 4, p)
        if root * root % p == p - 1:
            return root
    raise AssertionError(p)


def vertical_closure(mask, allowed):
    mask &= allowed
    while True:
        expanded = (mask | (mask << 1) | (mask >> 1)) & allowed
        if expanded == mask:
            return mask
        mask = expanded


class Strip:
    def __init__(self, radius):
        self.radius = radius
        self.width = 2 * radius + 1
        self.old = [sum(1 << (y + radius) for y in range(-radius, radius + 1)
                        if admissible(x, y, BASE)) for x in range(BASE)]

        @lru_cache(None)
        def step(mask, allowed):
            return vertical_closure(mask | (mask << 1) | (mask >> 1), allowed)

        @lru_cache(None)
        def clean(phase, mask, length):
            for i in range(1, length + 1):
                mask = step(mask, self.old[(phase + i) % BASE])
            return mask

        self.step = step
        self.clean = clean
        self.idempotent_checks = 0
        for phase in range(BASE):
            for y in range(self.width):
                once = clean(phase, 1 << y, BASE)
                assert clean(phase, once, BASE) == once
                self.idempotent_checks += 1

    def gap(self, x, mask, length):
        if length >= BASE:
            length = BASE + length % BASE
        return self.clean(x % BASE, mask, length)

    def endpoint(self, p, root):
        r = self.radius
        holes = {}
        for y in range(-r, r + 1):
            for z in {root * y % p, -root * y % p}:
                holes[z] = holes.get(z, 0) | (1 << (y + r))
        events = sorted(holes.items())
        bit = 1 << (r + 1)
        mask = vertical_closure(bit, self.old[0] & ~holes[0])
        previous = 0
        for cycle in range(BASE):
            for z, removed in events:
                x = cycle * p + z
                if x == 0:
                    continue
                mask = self.step(self.gap(previous, mask, x - previous - 1), self.old[x % BASE] & ~removed)
                if not mask:
                    return 0
                previous = x
        return self.step(self.gap(previous, mask, BASE * p - previous - 1), self.old[0] & ~holes[0])


def direct_endpoint(p, radius):
    length = BASE * p
    allowed = lambda x: sum(1 << (y + radius) for y in range(-radius, radius + 1)
                            if admissible(x, y, length))
    mask = vertical_closure(1 << (radius + 1), allowed(0))
    for x in range(1, length + 1):
        mask = vertical_closure(mask | (mask << 1) | (mask >> 1), allowed(x))
    return mask


def explicit_smallest_path():
    p, r = 17, 15
    modulus = p * BASE
    moves = {"E": (1, 0), "U": (1, 1), "D": (1, -1), "+": (0, 1), "-": (0, -1)}
    start, goal = (0, 1), (modulus, 1)
    queue = deque([start])
    parent = {start: None}
    while goal not in parent:
        x, y = queue.popleft()
        for name, (dx, dy) in moves.items():
            nxt = x + dx, y + dy
            if nxt in parent or nxt[0] > modulus or abs(nxt[1]) > r or not admissible(*nxt, modulus):
                continue
            parent[nxt] = ((x, y), name)
            queue.append(nxt)
    v, reverse = goal, []
    while v != start:
        v, move = parent[v]
        reverse.append(move)
    path = "".join(reversed(reverse))
    x, y = start
    for ch in path:
        dx, dy = moves[ch]
        x += dx
        y += dy
        assert abs(y) <= r and admissible(x, y, modulus)
    assert (x, y) == goal
    assert direct_endpoint(p, 15) & (1 << 16)
    assert not direct_endpoint(p, 14) & (1 << 15)
    return {"p": p, "horizontal_period": modulus, "least_symmetric_half_width_for_x_nondecreasing": r,
            "number_of_edges": len(path), "E_U_D_plus_minus": path}


def scan(limit):
    strips = {r: Strip(r) for r in (12, 15)}
    histogram = Counter()
    digest = hashlib.sha256()
    checked = 0
    primes = split_primes(limit)
    for p in primes:
        root = root_minus_one(p)
        for radius, strip in strips.items():
            mask = strip.endpoint(p, root)
            if p <= 73:
                assert mask == direct_endpoint(p, radius)
                checked += 1
            if mask & (1 << (radius + 1)):
                histogram[radius] += 1
                digest.update(f"{p} {radius} {mask}\n".encode("ascii"))
                break
        else:
            raise AssertionError(("no anchored positive winding", p))
    return {"inclusive_upper_bound": limit, "first_last_prime": [primes[0], primes[-1]],
            "split_primes_excluding_5_and_13": len(primes), "first_working_radii_12_then_15": dict(histogram),
            "all_terminal_masks_sha256": digest.hexdigest(), "direct_full_strip_comparisons": checked,
            "one_period_idempotence_singletons": {r: s.idempotent_checks for r, s in strips.items()}}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--extended", action="store_true", help="also scan all eligible primes up to 136900")
    options = parser.parse_args()
    result = {"coarse_tiles": tile_proof(), "sparse_constant_single_prime_cutoff": SMALL_LIMIT,
              "bounded_prime_scan": scan(SMALL_LIMIT), "explicit_17": explicit_smallest_path()}
    if options.extended:
        result["extended_prime_scan"] = scan(136900)
    print(json.dumps(result, ensure_ascii=False, indent=2))
