#!/usr/bin/env python3
"""Replay Q22 on actual decorated cycle adjacencies and test the finite inverse."""
import argparse
import hashlib
import importlib.util
import json
from collections import Counter
from itertools import combinations, combinations_with_replacement, product
from math import comb, gcd
from pathlib import Path


KERNEL = "P000_PHILOSOPHY_FIRST_RETURN_PROFILE_ITERATED_REFINEMENT_FRONTIER_CHECK_20260831.py"
SHA = "e0c6ce8d79fa4e725c89d0f7132c67d01ed48d47933a53c8f1aea45c3213fb14"


def get_kernel(path):
    if path is None:
        roots = (Path.cwd(), *Path(__file__).resolve().parents)
        path = next((root / "research_checks" / KERNEL for root in roots
                     if (root / "research_checks" / KERNEL).is_file()), None)
    if path is None or hashlib.sha256(path.read_bytes()).hexdigest() != SHA:
        raise SystemExit("Specify the pinned Q22 Python checker with --source PATH")
    spec = importlib.util.spec_from_file_location("frozen_q22", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def bracelet(word):
    n = len(word)
    return min(w[j:] + w[:j] for w in (word, word[::-1]) for j in range(n))


def phi(d):
    return sum(gcd(j, d) == 1 for j in range(1, d + 1))


def reflection(fixed, pairs, marks):
    return sum(comb(fixed, i) * comb(pairs, (marks - i) // 2)
               for i in range(fixed + 1)
               if 0 <= marks - i <= 2 * pairs and (marks - i) % 2 == 0)


def burnside(k, marks):
    rotation = sum(phi(d) * comb(k // d, marks // d)
                   for d in range(1, k + 1) if k % d == marks % d == 0)
    if k % 2:
        reflected = k * reflection(1, (k - 1) // 2, marks)
    else:
        reflected = k // 2 * (reflection(0, k // 2, marks)
                              + reflection(2, (k - 2) // 2, marks))
    assert (rotation + reflected) % (2 * k) == 0
    return (rotation + reflected) // (2 * k)


def deck(word, t):
    k = len(word)
    return tuple(sorted(min(s, s[::-1]) for s in
                        ("".join(word[(j + d) % k] for d in range(1 - t, t))
                         for j in range(k))))


def adjacency(kernel, word):
    k = len(word)
    edges = [(i, (i + 1) % k) for i in range(k)]
    n = k
    for i, bit in enumerate(word):
        if bit == "1":
            edges.extend(((i, n), (n, n + 1), (n + 1, n + 2), (n + 2, n)))
            n += 3
    return kernel.adj_from_edges(n, edges)


def native_rounds(kernel, word, depth):
    adj = adjacency(kernel, word)
    k = len(word)
    profiles, _, (base, layers, final), _ = kernel.stable_packet(adj)
    for i, profile in enumerate(profiles):
        length = k if i < k else 3
        assert sum(profile) == 1 and profile[length - 3] == 1
    # Preserve semantic dictionaries as in Q22. A local numeric color alone
    # is not a cross-graph observable. Recover early bags from the exact packet.
    counts = Counter(final)
    states = {}
    for t in range(len(layers), -1, -1):
        if t <= depth:
            states[t] = (base, layers[:t], tuple(sorted(counts.items())))
        if t:
            previous = Counter()
            for color, count in counts.items():
                previous[layers[t - 1][color][0]] += count
            counts = previous
    embedded = []
    for color, count in states[1][2]:
        old, neighbors = layers[0][color]
        embedded.extend([(base[old], tuple(base[x] for x in neighbors))] * count)
    assert tuple(sorted(embedded)) == kernel.semantic_round_one(adj)
    return [states[t] for t in range(depth + 1)]


def census(kernel):
    rows = []
    total = 0
    for k in range(4, 12):
        words = sorted({bracelet("".join(bits)) for bits in product("01", repeat=k)
                        if "1" in bits})
        depth = (k + 2) // 2
        observed = {}
        reverse = {}
        for w in words:
            m = w.count("1")
            for t, state in enumerate(native_rounds(kernel, w, depth)):
                key = (m, t)
                packet = deck(w, t) if t else ()
                assert observed.setdefault(key, {}).setdefault(packet, state) == state
                assert reverse.setdefault(key, {}).setdefault(state, packet) == packet
        sizes = [sum(w.count("1") == m for w in words) for m in range(1, k + 1)]
        assert sizes == [burnside(k, m) for m in range(1, k + 1)]
        assert sum(len(observed[m, k // 2]) for m in range(1, k + 1)) == len(words)
        rows.append({"k": k, "recovery_upper_bound_verified_at_round": k // 2,
                     "bracelets_by_positive_weight": sizes,
                     "distinct_packets_all_weights_by_round":
                     [sum(len(observed[m, t]) for m in range(1, k + 1))
                      for t in range(depth + 1)]})
        total += len(words)
    return {"graphs": total, "labelled_nonempty_subsets": sum(2**k - 1 for k in range(4, 12)),
            "by_k": rows}


def earliest(kernel):
    pairs = 0
    rows = []
    graph_count = 0
    for k in range(4, 33):
        ds = range(1, k // 2 + 1)
        words = ["".join("1" if i in (0, d) else "0" for i in range(k)) for d in ds]
        limit = 1 + k // 4
        observations = [native_rounds(kernel, w, limit) for w in words]
        histogram = Counter()
        for t in range(1, limit + 1):
            assert len({states[t] for states in observations}) == min(len(ds), 2 * t - 1)
        for a, b in combinations(range(len(words)), 2):
            first = next(t for t, (p, q) in enumerate(zip(observations[a], observations[b]))
                         if p != q)
            assert first == 1 + (ds[a] + 1) // 2
            histogram[first] += 1
        assert max(histogram) == limit
        rows.append({"k": k, "first_separation_pair_counts": sorted(histogram.items())})
        graph_count += len(ds)
        pairs += sum(histogram.values())
    return {"original_kernel_graphs": graph_count, "distinct_distance_pairs": pairs, "by_k": rows}


def eulerian(directed):
    balance = Counter()
    neighbors = {}
    for word, count in directed.items():
        if not count:
            continue
        a, b = word[:-1], word[1:]
        balance[a] += count
        balance[b] -= count
        neighbors.setdefault(a, set()).add(b)
        neighbors.setdefault(b, set()).add(a)
    if not neighbors or any(balance.values()):
        return False
    seen = set()
    todo = [next(iter(neighbors))]
    while todo:
        v = todo.pop()
        if v not in seen:
            seen.add(v)
            todo.extend(neighbors[v] - seen)
    return len(seen) == len(neighbors)


def admits_orientation(window_deck):
    counts = Counter(window_deck)
    fixed = {w: n for w, n in counts.items() if w == w[::-1]}
    pairs = [(w, n) for w, n in counts.items() if w != w[::-1]]
    for splits in product(*(range(n + 1) for _, n in pairs)):
        directed = fixed.copy()
        for (w, n), j in zip(pairs, splits):
            directed[w], directed[w[::-1]] = j, n - j
        if eulerian(directed):
            return True
    return False


def test_euler():
    alphabet = sorted({min(w, w[::-1]) for w in map("".join, product("01", repeat=3))})
    rows = []
    for k in range(4, 11):
        actual = {deck("".join(word), 2) for word in product("01", repeat=k)}
        total = 0
        accepted = 0
        for candidate in combinations_with_replacement(alphabet, k):
            good = admits_orientation(candidate)
            assert good == (candidate in actual)
            total += 1
            accepted += good
        rows.append({"k": k, "tested_all_decks_including_zero_weight": total,
                     "representable": accepted})
    assert not admits_orientation(("000", "000", "111", "111"))
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, help="pinned original Q22 Python file")
    kernel = get_kernel(parser.parse_args().source)
    data = {"kernel": KERNEL, "kernel_sha256": SHA, "source_graph_class": "finite simple Cell adjacency, degrees 2/3",
            "full_bracelet_census": census(kernel), "two_triangles": earliest(kernel),
            "euler_three_letter_decks": test_euler()}
    print(json.dumps(data, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
