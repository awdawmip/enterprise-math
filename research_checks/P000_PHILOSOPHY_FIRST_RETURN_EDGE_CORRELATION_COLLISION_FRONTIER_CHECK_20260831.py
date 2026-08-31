#!/usr/bin/env python3
"""Deterministic exact checker for P000 Q19 edge-profile correlation collision frontier."""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path

EXPECTED = {
    4: (2, 2, "f120e82dd929f416b6e5c780dce8d78f005efacf5bd88935acfbbf7ca68367a8"),
    5: (13, 3, "ca8468ebdecfa51617b2d6b47546ec27ed3791ae0e587ac23867ff34e492ce5c"),
    6: (178, 10, "712f36ab512258c9dee46f7eacc58a844b0fe50173ae26e5f080978bb5097379"),
    7: (1812, 20, "85f69c4334c48b7ebfa778783dc5a9c91b814aaef58b8cb933794590196c70cf"),
    8: (39492, 59, "c71aa7149b6348d731872a23ca9d04c130980391b2dae2da7aad59c7a448579f"),
}
EXPECTED_COMBINED = "16024b3075aca19423f8c920ba6aa911c74042af20d7e1ea9827280904ec5f0a"

Q16_H_EDGES = (
    (0, 2), (0, 4), (1, 5), (1, 6), (2, 3),
    (2, 4), (3, 6), (4, 7), (5, 6), (5, 7),
)
Q16_G_EDGES = (
    (0, 1), (0, 2), (0, 4), (1, 4), (2, 5),
    (2, 7), (3, 5), (3, 6), (4, 6), (5, 7),
)

H9_EDGES = (
    (0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 4),
    (2, 6), (3, 7), (3, 8), (5, 6), (7, 8),
)
G9_EDGES = (
    (0, 1), (0, 4), (0, 5), (1, 4), (1, 6), (2, 3),
    (2, 5), (2, 6), (3, 7), (3, 8), (7, 8),
)

CHECKS = 0


def check(cond: bool, message: str) -> None:
    global CHECKS
    CHECKS += 1
    if not cond:
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


def adj_from_edges(n: int, edges: tuple[tuple[int, int], ...]) -> tuple[int, ...]:
    adj = [0] * n
    for u, v in edges:
        check(0 <= u < v < n, f"invalid edge {(u, v)}")
        check(not ((adj[u] >> v) & 1), f"duplicate edge {(u, v)}")
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    return tuple(adj)


def primitive_cycles(adj: tuple[int, ...]) -> set[tuple[int, ...]]:
    """All unoriented simple cycles, each rooted at its least vertex."""
    n = len(adj)
    out: set[tuple[int, ...]] = set()
    for start in range(n):
        path = [start]

        def dfs(v: int, used: int) -> None:
            if len(path) >= 3 and ((adj[v] >> start) & 1):
                forward = tuple(path)
                reverse = (start,) + tuple(reversed(path[1:]))
                out.add(min(forward, reverse))
            nxt = adj[v] & ~used
            nxt &= ~((1 << (start + 1)) - 1)
            while nxt:
                bit = nxt & -nxt
                nxt -= bit
                w = bit.bit_length() - 1
                path.append(w)
                dfs(w, used | bit)
                path.pop()

        dfs(start, 1 << start)
    return out


def root_profiles(adj: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    n = len(adj)
    counts = [[0] * (n + 1) for _ in range(n)]
    for cyc in primitive_cycles(adj):
        k = len(cyc)
        for v in cyc:
            counts[v][k] += 1
    return tuple(tuple(row[3:]) for row in counts)


def relation_packet(adj: tuple[int, ...]):
    profiles = root_profiles(adj)
    root_packet = tuple(sorted(profiles))
    edges = Counter()
    n = len(adj)
    for u in range(n):
        nxt = adj[u] & ~((1 << (u + 1)) - 1)
        while nxt:
            bit = nxt & -nxt
            nxt -= bit
            v = bit.bit_length() - 1
            a, b = profiles[u], profiles[v]
            if b < a:
                a, b = b, a
            edges[(a, b)] += 1
    edge_packet = tuple(sorted((a, b, c) for (a, b), c in edges.items()))
    return profiles, (root_packet, edge_packet)


def isomorphic_with_profiles(
    adj1: tuple[int, ...],
    adj2: tuple[int, ...],
    prof1: tuple[tuple[int, ...], ...],
    prof2: tuple[tuple[int, ...], ...],
) -> bool:
    n = len(adj1)
    if n != len(adj2):
        return False
    deg1 = tuple(row.bit_count() for row in adj1)
    deg2 = tuple(row.bit_count() for row in adj2)
    keys1 = [(deg1[v], prof1[v]) for v in range(n)]
    keys2 = [(deg2[v], prof2[v]) for v in range(n)]
    if Counter(keys1) != Counter(keys2):
        return False
    candidates = {v: [w for w in range(n) if keys2[w] == keys1[v]] for v in range(n)}
    order = sorted(range(n), key=lambda v: (len(candidates[v]), -deg1[v], keys1[v], v))
    mapping = [-1] * n

    def rec(i: int, used: int) -> bool:
        if i == n:
            return True
        v = order[i]
        for w in candidates[v]:
            bit = 1 << w
            if used & bit:
                continue
            for j in range(i):
                u = order[j]
                z = mapping[u]
                if ((adj1[v] >> u) & 1) != ((adj2[w] >> z) & 1):
                    break
            else:
                mapping[v] = w
                if rec(i + 1, used | bit):
                    return True
                mapping[v] = -1
        return False

    return rec(0, 0)


def graphical(seq: list[int]) -> bool:
    """Havel-Hakimi decision for the remaining simple degree sequence."""
    work = sorted((d for d in seq if d), reverse=True)
    while work:
        d = work.pop(0)
        if d < 0 or d > len(work):
            return False
        for i in range(d):
            work[i] -= 1
            if work[i] < 0:
                return False
        work.sort(reverse=True)
    return True


def normalized_realizations(n: int, r: int):
    """All labeled realizations with degree-3 vertices normalized to 0..r-1.

    Every isomorphism type in U_BR(n) with r degree-3 vertices has at least one
    such labeling, so this is exact for invariant images/collision detection
    modulo Cell relabeling without enumerating all n! relabelings.
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
        for nbrs in itertools.combinations(candidates, d):
            rem[v] = 0
            for u in nbrs:
                rem[u] -= 1
                adj[v] |= 1 << u
                adj[u] |= 1 << v
            if all(x >= 0 for x in rem[v + 1:]) and graphical(rem[v + 1:]):
                yield from rec(v + 1)
            for u in nbrs:
                rem[u] += 1
                adj[v] &= ~(1 << u)
                adj[u] &= ~(1 << v)
            rem[v] = d

    yield from rec(0)


def sparse_profile(profile: tuple[int, ...]) -> dict[str, int]:
    return {str(k): int(c) for k, c in enumerate(profile, start=3) if c}


def packet_object(packet):
    root_packet, edge_packet = packet
    multiplicities = Counter(root_packet)
    classes = sorted(multiplicities)
    ids = {p: f"P{i}" for i, p in enumerate(classes)}
    return {
        "classes": [
            {
                "id": ids[p],
                "profile": sparse_profile(p),
                "multiplicity": multiplicities[p],
            }
            for p in classes
        ],
        "edge_profile_counts": [
            [ids[a], ids[b], count] for a, b, count in edge_packet
        ],
    }


def enumerate_exact_image(n: int):
    reps = {}
    normalized_connected = 0
    for r in range(2, n + 1, 2):
        for adj in normalized_realizations(n, r):
            if not connected(adj):
                continue
            normalized_connected += 1
            profiles, packet = relation_packet(adj)
            prior = reps.get(packet)
            if prior is None:
                reps[packet] = (adj, profiles)
            else:
                prior_adj, prior_profiles = prior
                check(
                    isomorphic_with_profiles(adj, prior_adj, profiles, prior_profiles),
                    f"unexpected edge-profile collision at n={n}",
                )
    objects = [packet_object(packet) for packet in reps]
    encoded_packets = sorted(
        json.dumps(obj, sort_keys=True, separators=(",", ":")) for obj in objects
    )
    encoded = "[" + ",".join(encoded_packets) + "]"
    digest = hashlib.sha256(encoded.encode()).hexdigest()
    return normalized_connected, len(reps), digest, encoded, [json.loads(x) for x in encoded_packets]


def neighbor_profile_multiset(adj: tuple[int, ...], profiles, v: int):
    c = Counter()
    bits = adj[v]
    while bits:
        bit = bits & -bits
        bits -= bit
        u = bit.bit_length() - 1
        c[profiles[u]] += 1
    return tuple(sorted(c.items()))


def local_incidence_packet(adj: tuple[int, ...], profiles):
    return tuple(sorted(Counter(
        (profiles[v], neighbor_profile_multiset(adj, profiles, v))
        for v in range(len(adj))
    ).items()))


def main() -> None:
    combined_parts = []
    exact_summaries = {}
    for n in range(4, 9):
        normalized, image_size, digest, encoded, packets = enumerate_exact_image(n)
        exp_normalized, exp_image_size, exp_digest = EXPECTED[n]
        check(normalized == exp_normalized, f"n={n}: normalized realization count drift")
        check(image_size == exp_image_size, f"n={n}: image size drift")
        check(digest == exp_digest, f"n={n}: image digest drift")
        exact_summaries[str(n)] = {
            "degree_normalized_connected_realizations": normalized,
            "isomorphism_types": image_size,
            "representable_packets": image_size,
            "image_sha256": digest,
        }
        combined_parts.append(f"{n}\n{encoded}")

    combined_digest = hashlib.sha256("\n".join(combined_parts).encode()).hexdigest()
    check(combined_digest == EXPECTED_COMBINED, "combined exact image digest drift")

    # Mandatory Q16 repair check.
    q16_h = adj_from_edges(8, Q16_H_EDGES)
    q16_g = adj_from_edges(8, Q16_G_EDGES)
    q16_hp, q16_hpacket = relation_packet(q16_h)
    q16_gp, q16_gpacket = relation_packet(q16_g)
    check(tuple(sorted(q16_hp)) == tuple(sorted(q16_gp)), "Q16 multiplicity equality drift")
    check(q16_hpacket != q16_gpacket, "edge-profile packet failed to repair Q16 witness")

    # First Q19 collision witness at n=9.
    H = adj_from_edges(9, H9_EDGES)
    G = adj_from_edges(9, G9_EDGES)
    for name, adj in (("H9", H), ("G9", G)):
        degs = Counter(row.bit_count() for row in adj)
        check(connected(adj), f"{name}: disconnected")
        check(degs == Counter({2: 5, 3: 4}), f"{name}: degree multiset drift {degs}")

    hp, hpacket = relation_packet(H)
    gp, gpacket = relation_packet(G)
    check(hpacket == gpacket, "n=9 relation-packet equality drift")
    check(not isomorphic_with_profiles(H, G, hp, gp), "n=9 witnesses unexpectedly isomorphic")

    A = (0, 0, 1, 1, 0, 0, 0)  # 5:1, 6:1
    B = (1, 0, 0, 0, 0, 0, 0)  # 3:1
    C = (1, 0, 0, 1, 0, 0, 0)  # 3:1, 6:1
    D = (1, 0, 1, 1, 0, 0, 0)  # 3:1, 5:1, 6:1
    expected_root = tuple(sorted((A,) * 3 + (B,) * 3 + (C,) + (D,) * 2))
    check(hpacket[0] == expected_root, "n=9 common root profile packet drift")
    expected_edges = tuple(sorted((
        (A, A, 2), (A, B, 1), (A, D, 2),
        (B, B, 3), (C, D, 2), (D, D, 1),
    )))
    check(hpacket[1] == expected_edges, "n=9 common edge-profile histogram drift")

    h_local = local_incidence_packet(H, hp)
    g_local = local_incidence_packet(G, gp)
    check(h_local != g_local, "rootwise neighbor-profile incidence unexpectedly equal")

    target_neighbor_multiset = ((A, 2),)
    h_A_AA = sum(
        1 for v in range(9)
        if hp[v] == A and neighbor_profile_multiset(H, hp, v) == target_neighbor_multiset
    )
    g_A_AA = sum(
        1 for v in range(9)
        if gp[v] == A and neighbor_profile_multiset(G, gp, v) == target_neighbor_multiset
    )
    check((h_A_AA, g_A_AA) == (1, 0), f"A-root AA-incidence certificate drift {(h_A_AA, g_A_AA)}")

    root = Path(__file__).resolve().parents[1]
    artifact_path = root / (
        "research_artifacts/P000_PHILOSOPHY_FIRST_RETURN_EDGE_CORRELATION_COLLISION_FRONTIER/"
        "P000_Q19_RETURN_EDGE_CORRELATION_COLLISION_FRONTIER_V1.json"
    )
    artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
    check(artifact["schema"] == "P000_Q19_RETURN_EDGE_CORRELATION_COLLISION_FRONTIER_V1", "artifact schema drift")
    check(
        artifact["exact_collision_free_prefix"]["combined_image_sha256"] == combined_digest,
        "artifact combined image digest drift",
    )
    check(
        artifact["exact_collision_free_prefix"]["summaries"] == exact_summaries,
        "artifact exact representability image drift",
    )
    check(
        artifact["first_collision"]["H9_edges"] == [list(e) for e in H9_EDGES]
        and artifact["first_collision"]["G9_edges"] == [list(e) for e in G9_EDGES],
        "artifact n=9 witness edges drift",
    )
    check(
        artifact["first_collision"]["next_missing_information"]["H_A_root_with_AA_neighbors"] == h_A_AA
        and artifact["first_collision"]["next_missing_information"]["G_A_root_with_AA_neighbors"] == g_A_AA,
        "artifact local-incidence certificate drift",
    )

    print(
        "PASS P000_Q19_EDGE_PROFILE_CORRELATION; "
        f"checks={CHECKS}; "
        "exact_prefix_n=4..8; normalized_connected=2,13,178,1812,39492; "
        "packet_images=2,3,10,20,59; first_collision_n=9; "
        "common_packet=A3_B3_C1_D2+AA2_AB1_AD2_BB3_CD2_DD1; "
        "next_gap=A-root incidence co-occurrence; A{AA}=1_vs_0"
    )


if __name__ == "__main__":
    main()
