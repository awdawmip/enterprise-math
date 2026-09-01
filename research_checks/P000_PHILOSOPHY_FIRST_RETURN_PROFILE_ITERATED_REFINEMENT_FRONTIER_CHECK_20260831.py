#!/usr/bin/env python3
"""Deterministic exact checker for P000 philosophy-first Q22.

The native observable is frozen first:
    c0(x) = primitive-return multiplicity profile m_X(x)
    c_{t+1}(x) = (c_t(x), multiset_{y~x} c_t(y)).

For cross-graph exact comparison we store each round as a canonical finite DAG:
raw c0 profiles are sorted, then every next-round color is a sorted signature over
prior-round canonical color IDs.  This is lossless compression of the recursively
nested semantic colors, not a hash approximation.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import multiprocessing as mp
import os
from collections import Counter
from pathlib import Path

EXPECTED = {
    4: {
        "normalized_connected": 2,
        "packets": 2,
        "image_sha256": "682f52266af9a4d8ee944747c9b4bb4a3494fc4e093890353dba583206ab5efa",
        "by_r": {2: (1, 1), 4: (1, 1)},
    },
    5: {
        "normalized_connected": 13,
        "packets": 3,
        "image_sha256": "c5606b5c5e8f252718e6a602add00a86394bdcab39f4bb7c93b2866929e34cd2",
        "by_r": {2: (7, 2), 4: (6, 1)},
    },
    6: {
        "normalized_connected": 178,
        "packets": 10,
        "image_sha256": "15f5e8bc28cb7264bfca8359dd5cd08b934ffd75177bdb284cead1c748ed07df",
        "by_r": {2: (54, 4), 4: (54, 4), 6: (70, 2)},
    },
    7: {
        "normalized_connected": 1812,
        "packets": 20,
        "image_sha256": "f6c9dcf76b9da113b10684f243bfb634355b8541ba6d964ef60ea342797518f7",
        "by_r": {2: (450, 6), 4: (552, 10), 6: (810, 4)},
    },
    8: {
        "normalized_connected": 39492,
        "packets": 59,
        "image_sha256": "2dbd311eb413a2dc853c8ea350c0172cb7f5949c01e115f5b582394b92298055",
        "by_r": {2: (4080, 10), 4: (6012, 25), 6: (10080, 19), 8: (19320, 5)},
    },
    9: {
        "normalized_connected": 525060,
        "packets": 147,
        "image_sha256": "4030985011a7b14a08caa565a44165a7fdbf1a4070b8020557a531142f657844",
        "by_r": {2: (40320, 13), 4: (69840, 52), 6: (132660, 63), 8: (282240, 19)},
    },
}
EXPECTED_COMBINED = "9f95149157883d6253f28ba39663c93fc3aa577f9311639927b0da0862d3e1bc"
EXPECTED_STABILIZATION = {
    4: {0: 2},
    5: {0: 3},
    6: {0: 8, 1: 2},
    7: {0: 11, 1: 8, 2: 1},
    8: {0: 29, 1: 23, 2: 7},
    9: {0: 49, 1: 63, 2: 33, 3: 2},
}
EXPECTED_STABLE_CLASS_COUNTS = {
    4: {1: 1, 2: 1},
    5: {2: 1, 3: 2},
    6: {1: 2, 2: 4, 3: 2, 4: 2},
    7: {3: 6, 4: 10, 5: 3, 7: 1},
    8: {1: 2, 2: 6, 3: 13, 4: 9, 5: 15, 6: 6, 7: 3, 8: 5},
    9: {2: 3, 3: 1, 4: 21, 5: 38, 6: 34, 7: 12, 8: 14, 9: 24},
}

H9_EDGES = (
    (0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 4),
    (2, 6), (3, 7), (3, 8), (5, 6), (7, 8),
)
G9_EDGES = (
    (0, 1), (0, 4), (0, 5), (1, 4), (1, 6), (2, 3),
    (2, 5), (2, 6), (3, 7), (3, 8), (7, 8),
)


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def connected(adj: tuple[int, ...]) -> bool:
    n = len(adj)
    seen = 1
    stack = [0]
    while stack:
        v = stack.pop()
        unseen = adj[v] & ~seen
        while unseen:
            bit = unseen & -unseen
            unseen -= bit
            seen |= bit
            stack.append(bit.bit_length() - 1)
    return seen == (1 << n) - 1


def graphical(seq: list[int]) -> bool:
    work = sorted((d for d in seq if d), reverse=True)
    while work:
        d = work.pop(0)
        if d > len(work):
            return False
        for i in range(d):
            work[i] -= 1
            if work[i] < 0:
                return False
        work.sort(reverse=True)
    return True


def normalized_realizations(n: int, r: int, chunk: int = 0, chunks: int = 1):
    """Exact labeled cover with degree-3 vertices normalized to 0..r-1.

    Optional chunks partition the first vertex's neighbor-combination index.  The
    chunks are disjoint and their union is the same exact normalized cover.
    """
    rem = [3] * r + [2] * (n - r)
    adj = [0] * n

    def rec(v: int):
        while v < n and rem[v] == 0:
            v += 1
        if v == n:
            yield tuple(adj)
            return
        d = rem[v]
        candidates = [u for u in range(v + 1, n) if rem[u] > 0]
        if d > len(candidates):
            return
        for index, nbrs in enumerate(itertools.combinations(candidates, d)):
            if v == 0 and index % chunks != chunk:
                continue
            rem[v] = 0
            ok = True
            for u in nbrs:
                rem[u] -= 1
                adj[v] |= 1 << u
                adj[u] |= 1 << v
                if rem[u] < 0:
                    ok = False
            if ok and graphical(rem[v + 1 :]):
                yield from rec(v + 1)
            for u in nbrs:
                rem[u] += 1
                adj[v] &= ~(1 << u)
                adj[u] &= ~(1 << v)
            rem[v] = d

    yield from rec(0)


def root_profiles(adj: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    """Primitive-return multiplicities: simple unoriented cycles through each root."""
    n = len(adj)
    counts = [[0] * (n + 1) for _ in range(n)]
    for start in range(n):
        path = [start]
        higher = ~((1 << (start + 1)) - 1)

        def dfs(v: int, used: int) -> None:
            # start is the least cycle vertex; path[1] < path[-1] chooses one orientation.
            if len(path) >= 3 and ((adj[v] >> start) & 1) and path[1] < path[-1]:
                k = len(path)
                for x in path:
                    counts[x][k] += 1
            nxt = adj[v] & ~used & higher
            while nxt:
                bit = nxt & -nxt
                nxt -= bit
                w = bit.bit_length() - 1
                path.append(w)
                dfs(w, used | bit)
                path.pop()

        dfs(start, 1 << start)
    return tuple(tuple(row[3:]) for row in counts)


def stable_packet(adj: tuple[int, ...]):
    """Losslessly compressed semantic R_n packet and minimum stabilization index."""
    n = len(adj)
    profiles = root_profiles(adj)
    legend0 = tuple(sorted(set(profiles)))
    ids = {sig: i for i, sig in enumerate(legend0)}
    colors = [ids[p] for p in profiles]
    layers = []
    class_count = len(legend0)
    stabilization = None

    for t in range(n):
        signatures = []
        for v in range(n):
            neighbor_colors = []
            bits = adj[v]
            while bits:
                bit = bits & -bits
                bits -= bit
                neighbor_colors.append(colors[bit.bit_length() - 1])
            signatures.append((colors[v], tuple(sorted(neighbor_colors))))
        legend = tuple(sorted(set(signatures)))
        ids = {sig: i for i, sig in enumerate(legend)}
        new_colors = [ids[sig] for sig in signatures]
        next_count = len(legend)
        if stabilization is None and next_count == class_count:
            stabilization = t
        layers.append(legend)
        colors = new_colors
        class_count = next_count

    check(stabilization is not None, "refinement failed finite stabilization bound")
    packet = (legend0, tuple(layers), tuple(sorted(colors)))
    return profiles, tuple(colors), packet, stabilization


def semantic_round_one(adj: tuple[int, ...]):
    profiles = root_profiles(adj)
    return tuple(sorted(
        (profiles[v], tuple(sorted(profiles[u] for u in range(len(adj)) if (adj[v] >> u) & 1)))
        for v in range(len(adj))
    ))


def isomorphic(
    adj1: tuple[int, ...], adj2: tuple[int, ...],
    prof1, prof2, col1: tuple[int, ...], col2: tuple[int, ...],
) -> bool:
    n = len(adj1)
    deg1 = [row.bit_count() for row in adj1]
    deg2 = [row.bit_count() for row in adj2]
    keys1 = [(deg1[v], prof1[v], col1[v]) for v in range(n)]
    keys2 = [(deg2[v], prof2[v], col2[v]) for v in range(n)]
    if Counter(keys1) != Counter(keys2):
        return False
    buckets = {}
    for w, key in enumerate(keys2):
        buckets.setdefault(key, []).append(w)
    candidates = [buckets[key] for key in keys1]
    order = sorted(range(n), key=lambda v: (len(candidates[v]), -deg1[v], v))
    mapping = [-1] * n

    def rec(i: int, used: int) -> bool:
        if i == n:
            return True
        v = order[i]
        for w in candidates[v]:
            bit = 1 << w
            if used & bit:
                continue
            if all(
                ((adj1[v] >> order[j]) & 1) == ((adj2[w] >> mapping[order[j]]) & 1)
                for j in range(i)
            ):
                mapping[v] = w
                if rec(i + 1, used | bit):
                    return True
                mapping[v] = -1
        return False

    return rec(0, 0)


def adj_from_edges(n: int, edges) -> tuple[int, ...]:
    adj = [0] * n
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    return tuple(adj)


def edges_from_adj(adj: tuple[int, ...]):
    return tuple(
        (i, j) for i in range(len(adj)) for j in range(i + 1, len(adj))
        if (adj[i] >> j) & 1
    )


def packet_encoding(packet) -> str:
    return json.dumps(packet, separators=(",", ":"))


def worker(spec):
    n, r, chunk, chunks = spec
    reps = {}
    normalized_connected = 0
    for adj in normalized_realizations(n, r, chunk, chunks):
        if not connected(adj):
            continue
        normalized_connected += 1
        profiles, colors, packet, stabilization = stable_packet(adj)
        encoded = packet_encoding(packet)
        prior = reps.get(encoded)
        if prior is None:
            reps[encoded] = (adj, profiles, colors, stabilization)
        else:
            p_adj, p_profiles, p_colors, _ = prior
            check(
                isomorphic(adj, p_adj, profiles, p_profiles, colors, p_colors),
                f"stable packet collision inside exact chunk n={n}, r={r}, chunk={chunk}",
            )
    return n, r, chunk, chunks, normalized_connected, reps


def task_specs():
    specs = []
    for n in range(4, 9):
        for r in range(2, n + 1, 2):
            specs.append((n, r, 0, 1))
    # n=9 is the new exact frontier. Split each degree sector deterministically.
    split = {2: 2, 4: 2, 6: 4, 8: 8}
    for r, chunks in split.items():
        for chunk in range(chunks):
            specs.append((9, r, chunk, chunks))
    return specs


def verify_witness() -> None:
    h = adj_from_edges(9, H9_EDGES)
    g = adj_from_edges(9, G9_EDGES)
    hp = root_profiles(h)
    gp = root_profiles(g)
    check(tuple(sorted(hp)) == tuple(sorted(gp)), "Q19 witness c0 equality drift")
    check(semantic_round_one(h) != semantic_round_one(g), "Q19 witness not separated by c1")
    _, _, _, h_stab = stable_packet(h)
    _, _, _, g_stab = stable_packet(g)
    check((h_stab, g_stab) == (2, 1), "Q19 witness stabilization indices drift")


def load_artifact(path: Path):
    value = json.loads(path.read_text(encoding="utf-8"))
    check(value.get("schema") == "P000_Q22_RETURN_PROFILE_ITERATED_REFINEMENT_EXACT_PREFIX_V1", "artifact schema drift")
    return value


def verify_artifact_representatives(artifact) -> None:
    metadata = artifact.get("ordered_packet_metadata")
    check(isinstance(metadata, dict), "artifact ordered packet metadata missing")
    total = 0
    for n in range(4, 10):
        rows = metadata.get(str(n))
        check(isinstance(rows, list) and len(rows) == EXPECTED[n]["packets"], f"artifact n={n} packet metadata count drift")
        stab = Counter()
        classes = Counter()
        sector = Counter()
        for row in rows:
            check(isinstance(row, list) and len(row) == 3, "artifact compact row shape drift")
            degree3_count, expected_stab, expected_classes = map(int, row)
            check(2 <= degree3_count <= n and degree3_count % 2 == 0, "artifact degree-3 sector drift")
            check(expected_stab >= 0, "artifact stabilization index invalid")
            check(1 <= expected_classes <= n, "artifact stable class count invalid")
            sector[degree3_count] += 1
            stab[expected_stab] += 1
            classes[expected_classes] += 1
        for r in range(2, n + 1, 2):
            check(sector[r] == EXPECTED[n]["by_r"][r][1], f"artifact n={n},r={r} packet count drift")
        check(dict(stab) == EXPECTED_STABILIZATION[n], f"artifact n={n} stabilization census drift")
        check(dict(classes) == EXPECTED_STABLE_CLASS_COUNTS[n], f"artifact n={n} stable-class census drift")
        total += len(rows)
    check(total == 241, "artifact total packet metadata count drift")


def full_exact(jobs: int, artifact):
    specs = task_specs()
    if jobs <= 1:
        results = [worker(spec) for spec in specs]
    else:
        with mp.Pool(processes=jobs) as pool:
            results = pool.map(worker, specs)

    by_n = {n: {} for n in range(4, 10)}
    connected_by_nr = Counter()
    packets_by_nr = {}
    for n, r, chunk, chunks, count, reps in results:
        connected_by_nr[(n, r)] += count
        nr = packets_by_nr.setdefault((n, r), {})
        for encoded, value in reps.items():
            if encoded in nr:
                adj, profiles, colors, _ = value
                p_adj, p_profiles, p_colors, _ = nr[encoded]
                check(
                    isomorphic(adj, p_adj, profiles, p_profiles, colors, p_colors),
                    f"stable packet cross-chunk collision n={n}, r={r}",
                )
            else:
                nr[encoded] = value

    combined_parts = []
    artifact_metadata = artifact["ordered_packet_metadata"]
    exact_summary = {}
    for n in range(4, 10):
        reps = {}
        by_r = {}
        for r in range(2, n + 1, 2):
            nr = packets_by_nr[(n, r)]
            by_r[r] = (connected_by_nr[(n, r)], len(nr))
            for encoded, value in nr.items():
                if encoded in reps:
                    adj, profiles, colors, _ = value
                    p_adj, p_profiles, p_colors, _ = reps[encoded]
                    check(
                        isomorphic(adj, p_adj, profiles, p_profiles, colors, p_colors),
                        f"stable packet cross-degree-sector collision n={n}",
                    )
                else:
                    reps[encoded] = value

        encoded_packets = sorted(reps)
        image = "[" + ",".join(encoded_packets) + "]"
        digest = hashlib.sha256(image.encode()).hexdigest()
        exp = EXPECTED[n]
        check(sum(x[0] for x in by_r.values()) == exp["normalized_connected"], f"n={n}: normalized count drift")
        check(len(reps) == exp["packets"], f"n={n}: packet/image size drift")
        check(digest == exp["image_sha256"], f"n={n}: exact image SHA drift")
        check(by_r == exp["by_r"], f"n={n}: degree-sector exact counts drift")

        stab = Counter(value[3] for value in reps.values())
        class_counts = Counter(len(set(value[2])) for value in reps.values())
        check(dict(stab) == EXPECTED_STABILIZATION[n], f"n={n}: stabilization census drift")
        check(dict(class_counts) == EXPECTED_STABLE_CLASS_COUNTS[n], f"n={n}: stable-class census drift")
        ordered_metadata = []
        for encoded in encoded_packets:
            adj, profiles, colors, stabilization = reps[encoded]
            r = sum(row.bit_count() == 3 for row in adj)
            ordered_metadata.append([r, stabilization, len(set(colors))])
        check(ordered_metadata == artifact_metadata[str(n)], f"n={n}: artifact ordered packet metadata mismatch")
        exact_summary[n] = (exp["normalized_connected"], len(reps), dict(stab), dict(class_counts))
        combined_parts.append(f"{n}\n{image}")

    combined = hashlib.sha256("\n".join(combined_parts).encode()).hexdigest()
    check(combined == EXPECTED_COMBINED, "combined exact image SHA drift")
    check(combined == artifact["combined_image_sha256"], "artifact combined image SHA drift")
    return exact_summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true", help="verify witness and compact frozen packet certificates only")
    parser.add_argument("--jobs", type=int, default=min(8, max(1, os.cpu_count() or 1)))
    parser.add_argument(
        "--artifact",
        default="research_artifacts/P000_PHILOSOPHY_FIRST_RETURN_PROFILE_ITERATED_REFINEMENT_FRONTIER/P000_Q22_RETURN_PROFILE_ITERATED_REFINEMENT_EXACT_PREFIX_V1.json",
    )
    args = parser.parse_args()
    artifact = load_artifact(Path(args.artifact))
    verify_witness()
    verify_artifact_representatives(artifact)
    if args.quick:
        print("PASS P000_Q22_RETURN_PROFILE_REFINEMENT_QUICK; Q19_n9_separated_at_c1; frozen_packet_metadata=241")
        return
    summary = full_exact(max(1, args.jobs), artifact)
    total = sum(EXPECTED[n]["normalized_connected"] for n in EXPECTED)
    print(
        "PASS P000_Q22_RETURN_PROFILE_REFINEMENT_FULL; "
        f"exact_prefix_n=4..9; normalized_connected={total}; packets=241; "
        f"per_n_packets={[EXPECTED[n]['packets'] for n in range(4,10)]}; "
        f"max_stabilization_index=3; discrete_stable=30/241; combined_image_sha256={EXPECTED_COMBINED}"
    )


if __name__ == "__main__":
    main()
