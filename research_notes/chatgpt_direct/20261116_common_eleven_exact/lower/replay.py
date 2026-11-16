"""Rebuild the complete finite lower-bound proof in a fresh temporary directory."""
from __future__ import annotations

import json
import subprocess
import tempfile
from collections import defaultdict
from functools import lru_cache
from itertools import combinations, permutations, product
from pathlib import Path

SOURCE = Path(__file__).resolve().parent
POINTS = list(product(range(5), repeat=3))
CEILINGS = {8: 445, 9: 587, 10: 780, 11: 965, 12: 1140, 13: 1350}
TARGETS = {11: 10925, 12: 9815}


def observation_file(path):
    masks = [[0] * 125 for _ in POINTS]
    forbidden = set()
    for t, (d, start) in enumerate(product((1, 3), POINTS)):
        groups = defaultdict(list)
        for i, point in enumerate(POINTS):
            active = tuple(j for j in range(3) if (point[j] - start[j]) % 5 in (0, d))
            groups[active].append((i, tuple(point[j] for j in active)))
        for group in groups.values():
            for (i, a), (j, b) in combinations(group, 2):
                if a != b:
                    masks[i][j] |= 1 << t
                    masks[j][i] |= 1 << t
            for (i, a), (j, b), (k, c) in combinations(group, 3):
                if len({a, b, c}) == 3:
                    forbidden.add((i, j, k))
    assert len(forbidden) == 47000
    with path.open("wb") as f:
        for row in masks:
            for word in row:
                f.write(word.to_bytes(32, "little"))
        for tri in sorted(forbidden):
            f.write(bytes(tri))


def symmetries():
    orientations = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            for a in (1, 2):
                row = []
                for p in POINTS:
                    x, y, z = (p[perm[j]] * signs[j] * a % 5 for j in range(3))
                    row.append(25 * x + 5 * y + z)
                orientations.append(row)
    shifts = [[1 << (25 * ((x+a) % 5) + 5 * ((y+b) % 5) + (z+c) % 5)
               for x, y, z in POINTS] for a, b, c in POINTS]
    return orientations, shifts


def expand(seeds, orientations, shifts):
    rotated = {tuple(sorted(g[i] for i in p)) for g in orientations for p in seeds}
    return {sum(sh[i] for i in p) for p in rotated for sh in shifts}


def families(seed_file, database):
    orientations, shifts = symmetries()
    canonical = defaultdict(set)
    for line in seed_file.read_text().splitlines():
        size, cost, *points = map(int, line.split())
        canonical[size, cost].add(tuple(points))
    families = {}
    with database.open("w") as out:
        print(len(canonical), file=out)
        for key in sorted(canonical):
            family = expand(canonical[key], orientations, shifts)
            remaining = family.copy()
            reps = set()
            while remaining:
                rep = min(remaining)
                points = [i for i in range(125) if rep >> i & 1]
                orbit = expand([points], orientations, shifts)
                assert orbit <= remaining
                reps.add(rep)
                remaining -= orbit
            print(*key, len(family), file=out)
            for mask in sorted(family):
                print(mask % (1 << 64), mask >> 64, int(mask in reps), file=out)
            families[key] = sorted(family)
    return families


def core_packing(families):
    cores = families[12, 1104]
    largest = families[13, 1296]
    assert len(cores) == len(largest) == 250
    inclusions = [(x, y) for x in cores for y in largest if (x & y) == x]
    assert len(inclusions) == len(set(x for x, _ in inclusions)) == len(set(y for _, y in inclusions)) == 250
    neighbors = [sum(1 << j for j, y in enumerate(cores) if not (x & y)) for x in cores]
    best = 0

    def clique(k, possible):
        nonlocal best
        best = max(best, k)
        while k + possible.bit_count() > best:
            low = possible & -possible
            possible ^= low
            clique(k + 1, possible & neighbors[low.bit_length() - 1])

    clique(0, (1 << len(cores)) - 1)
    assert best == 6
    return best


def profiles(label_limit, budget, minimum, known, max_cores):
    # Each wildcard is the most optimistic cost for a size/cost type outside the enumeration.
    types = [(s, c, False) for s, c in known]
    types += [(s, c + 1, True) for s, c in CEILINGS.items()]
    types += [(s, minimum[s], True) for s in range(1, 8)]
    types.sort(reverse=True)

    @lru_cache(None)
    def optimistic(n, labels, maximum, cores):
        if not labels:
            return 0 if n == 0 else 10**9
        # Every 13 requires a core. For 12s the first available core can be
        # assigned greedily: all cheap 12s save the same 12 units and sizes are descending.
        choices = []
        for s in range((n + labels - 1) // labels, min(maximum, n - labels + 1) + 1):
            if s == 13 and not cores:
                continue
            price = minimum[s] + 12 * (s == 12 and not cores)
            choices.append(price + optimistic(n - s, labels - 1, s, max(0, cores - (s >= 12))))
        return min(choices, default=10**9)

    result = []

    def visit(n, labels, first, cores, spent, chosen):
        if not labels:
            if not n:
                assert not any(wildcard for _, _, wildcard in chosen), "raise class-enumeration ceilings"
                result.append((spent, tuple(chosen)))
            return
        if spent + optimistic(n, labels, types[first][0], cores) > budget:
            return
        for j in range(first, len(types)):
            size, cost, wildcard = types[j]
            use_core = size == 13 or (size, cost) == (12, 1104)
            if size * labels < n:
                break
            if n - size < labels - 1 or (use_core and not cores):
                continue
            tail = optimistic(n - size, labels - 1, size, cores - use_core)
            if spent + cost + tail <= budget:
                visit(n - size, labels - 1, j, cores - use_core, spent + cost, chosen + [types[j]])

    visit(125, label_limit, 0, max_cores, 0, [])
    return [(v, [p.count((s, c, False)) for s, c in sorted(known)]) for v, p in sorted(result)]


def run():
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        for cpp in ("class_enumeration", "search"):
            subprocess.run(["c++", "-O3", "-std=c++17", "-mpopcnt", str(SOURCE / (cpp + ".cpp")),
                            "-o", str(root / cpp)], check=True)
        observation_file(root / "observations.bin")
        raw = subprocess.check_output([str(root / "class_enumeration"), str(root / "observations.bin"),
                                       str(root / "seeds.txt")], text=True)
        minima = {1: 0}
        for line in raw.splitlines():
            size, visits, cost, *witness = map(int, line.split())
            minima[size] = cost
        family = families(root / "seeds.txt", root / "db.txt")
        assert min(c for s, c in family if s == 12 and c > 1104) == 1116
        max_cores = core_packing(family)
        result = {}
        for labels, budget in TARGETS.items():
            rows = profiles(labels, budget, minima, family, max_cores)
            data = "".join(" ".join(map(str, [value] + counts)) + "\n" for value, counts in rows)
            transcript = subprocess.check_output([str(root / "search"), str(root / "db.txt")],
                                                 input=data, text=True)
            observed = [tuple(map(int, line.split())) for line in transcript.splitlines()]
            assert [v for v, _, _ in observed] == [v for v, _ in rows]
            assert all(found == 0 for _, _, found in observed)
            result[labels] = {"tested_budget":budget, "profiles_excluded":len(rows),
                              "search_nodes":sum(nodes for _, nodes, _ in observed), "lower_bound":budget + 1}
        return result


if __name__ == "__main__":
    print(json.dumps(run(), sort_keys=True, indent=2))
