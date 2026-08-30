#!/usr/bin/env python3
"""Deterministic exact checker for P000 Q16 return-multiplicity collision frontier."""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path

EXPECTED = {
    4: (7, 2, "7f3e64e5aa1bc09ca670921483ec634bc185c0ccf49055968857aeb62c0f9a24"),
    5: (100, 3, "32c14a8c2d811c910733bbca5f29fafde34b6a73df7d4a02f312c53560fc6e93"),
    6: (1690, 10, "6cb627ace9d539b96cb9953ee773dbcc68e6bb96004bf958db76ede1bcf9103e"),
    7: (34440, 20, "f7ee6ecaaf16dba6c0da8e1f08182a431abedb0ab82358004ecf048a0655133b"),
}
EXPECTED_COMBINED = "e3c294c684bf89d62646510eefe945f5ab2f1b92fbba3ef7e70a02496f9c3ceb"

H_EDGES = (
    (0, 2), (0, 4), (1, 5), (1, 6), (2, 3),
    (2, 4), (3, 6), (4, 7), (5, 6), (5, 7),
)
G_EDGES = (
    (0, 1), (0, 2), (0, 4), (1, 4), (2, 5),
    (2, 7), (3, 5), (3, 6), (4, 6), (5, 7),
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


def profiles_packet(adj: tuple[int, ...]):
    n = len(adj)
    cycles = primitive_cycles(adj)
    counts = [[0] * (n + 1) for _ in range(n)]
    for cyc in cycles:
        k = len(cyc)
        for v in cyc:
            counts[v][k] += 1
    profiles = tuple(tuple(row[3:]) for row in counts)
    return profiles, tuple(sorted(profiles)), cycles


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

    candidates = {
        v: [w for w in range(n) if keys2[w] == keys1[v]]
        for v in range(n)
    }
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
            compatible = True
            for j in range(i):
                u = order[j]
                z = mapping[u]
                if ((adj1[v] >> u) & 1) != ((adj2[w] >> z) & 1):
                    compatible = False
                    break
            if compatible:
                mapping[v] = w
                if rec(i + 1, used | bit):
                    return True
                mapping[v] = -1
        return False

    return rec(0, 0)


def sparse_packet(packet: tuple[tuple[int, ...], ...]):
    return [
        {str(k): int(c) for k, c in enumerate(profile, start=3) if c}
        for profile in packet
    ]


def enumerate_exact_prefix(n: int):
    """Enumerate every labeled graph in U_BR(n), deduping only after packet computation."""
    edges = tuple(itertools.combinations(range(n), 2))
    reps: dict[tuple[tuple[int, ...], ...], tuple[tuple[int, ...], tuple[tuple[int, ...], ...]]] = {}
    labeled = 0

    for r in range(2, n + 1, 2):
        m = n + r // 2
        for chosen in itertools.combinations(range(len(edges)), m):
            degree = [0] * n
            bad = False
            for idx in chosen:
                u, v = edges[idx]
                degree[u] += 1
                degree[v] += 1
                if degree[u] > 3 or degree[v] > 3:
                    bad = True
                    break
            if bad:
                continue
            if any(d < 2 or d > 3 for d in degree):
                continue
            if sum(d == 3 for d in degree) != r:
                continue

            adj = [0] * n
            for idx in chosen:
                u, v = edges[idx]
                adj[u] |= 1 << v
                adj[v] |= 1 << u
            adj_t = tuple(adj)
            if not connected(adj_t):
                continue

            labeled += 1
            profiles, packet, _ = profiles_packet(adj_t)
            prior = reps.get(packet)
            if prior is None:
                reps[packet] = (adj_t, profiles)
            else:
                prior_adj, prior_profiles = prior
                check(
                    isomorphic_with_profiles(adj_t, prior_adj, profiles, prior_profiles),
                    f"unexpected multiplicity collision below n=8 at n={n}",
                )

    packets = sorted(reps)
    encoded = json.dumps(
        [sparse_packet(packet) for packet in packets],
        sort_keys=True,
        separators=(",", ":"),
    )
    return labeled, packets, hashlib.sha256(encoded.encode()).hexdigest(), encoded


def main() -> None:
    combined_parts = []
    exact_summaries = {}

    for n in range(4, 8):
        labeled, packets, digest, encoded = enumerate_exact_prefix(n)
        exp_labeled, exp_packets, exp_digest = EXPECTED[n]
        check(labeled == exp_labeled, f"n={n}: labeled count drift {labeled}")
        check(len(packets) == exp_packets, f"n={n}: packet image size drift {len(packets)}")
        check(digest == exp_digest, f"n={n}: representability image digest drift")
        exact_summaries[str(n)] = {
            "labeled_models": labeled,
            "isomorphism_types": len(packets),
            "representable_packets": len(packets),
            "image_sha256": digest,
            "packets": [sparse_packet(packet) for packet in packets],
        }
        combined_parts.append(f"{n}\n{encoded}")

    combined_digest = hashlib.sha256("\n".join(combined_parts).encode()).hexdigest()
    check(combined_digest == EXPECTED_COMBINED, "combined representability image digest drift")

    H = adj_from_edges(8, H_EDGES)
    G = adj_from_edges(8, G_EDGES)
    for name, adj in (("H", H), ("G", G)):
        degrees = tuple(row.bit_count() for row in adj)
        check(connected(adj), f"{name}: disconnected")
        check(all(2 <= d <= 3 for d in degrees), f"{name}: not subcubic branching family")
        check(any(d == 3 for d in degrees), f"{name}: no branching Cell")
        check(Counter(degrees) == Counter({2: 4, 3: 4}), f"{name}: degree multiset drift")

    H_profiles, H_packet, H_cycles = profiles_packet(H)
    G_profiles, G_packet, G_cycles = profiles_packet(G)
    check(H_packet == G_packet, "8-Cell witness packet mismatch")
    check(not isomorphic_with_profiles(H, G, H_profiles, G_profiles), "8-Cell witnesses unexpectedly isomorphic")

    A = (1, 0, 0, 1, 2, 1)
    B = (1, 0, 0, 0, 1, 1)
    C = (0, 0, 0, 1, 2, 1)
    expected_packet = tuple(sorted((A,) * 4 + (B,) * 2 + (C,) * 2))
    check(H_packet == expected_packet, "8-Cell common packet is not A^4 B^2 C^2")
    check(Counter(map(len, H_cycles)) == Counter({3: 2, 6: 1, 7: 2, 8: 1}), "H cycle totals drift")
    check(Counter(map(len, G_cycles)) == Counter({3: 2, 6: 1, 7: 2, 8: 1}), "G cycle totals drift")

    H_C = tuple(v for v, profile in enumerate(H_profiles) if profile == C)
    G_C = tuple(v for v, profile in enumerate(G_profiles) if profile == C)
    check(H_C == (3, 7), f"H C-profile vertices drift: {H_C}")
    check(G_C == (3, 6), f"G C-profile vertices drift: {G_C}")
    H_CC = int(bool((H[H_C[0]] >> H_C[1]) & 1))
    G_CC = int(bool((G[G_C[0]] >> G_C[1]) & 1))
    check((H_CC, G_CC) == (0, 1), f"C-C adjacency certificate drift: {(H_CC, G_CC)}")

    root = Path(__file__).resolve().parents[1]
    artifact_path = root / "research_artifacts/P000_PHILOSOPHY_FIRST_RETURN_MULTIPLICITY_COLLISION_FRONTIER/P000_Q16_RETURN_MULTIPLICITY_COLLISION_FRONTIER_V1.json"
    artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
    check(artifact["schema"] == "P000_Q16_RETURN_MULTIPLICITY_COLLISION_FRONTIER_V1", "artifact schema drift")
    check(
        artifact["exact_collision_free_prefix"]["combined_image_sha256"] == combined_digest,
        "artifact combined image digest drift",
    )
    check(
        artifact["exact_collision_free_prefix"]["summaries"] == exact_summaries,
        "artifact representability image differs from exact enumeration",
    )
    check(
        artifact["first_collision"]["H_edges"] == [list(e) for e in H_EDGES]
        and artifact["first_collision"]["G_edges"] == [list(e) for e in G_EDGES],
        "artifact witness edge sets drift",
    )
    check(
        artifact["first_collision"]["nonisomorphism_certificate"]["H_C_C_native_edges"] == H_CC
        and artifact["first_collision"]["nonisomorphism_certificate"]["G_C_C_native_edges"] == G_CC,
        "artifact C-C relation certificate drift",
    )

    print(
        "PASS P000_Q16_RETURN_MULTIPLICITY; "
        f"checks={CHECKS}; "
        "prefix_labeled=7,100,1690,34440; "
        "prefix_iso_packets=2,3,10,20; "
        "first_collision_n=8; packet=A4_B2_C2; C_edge=0_vs_1"
    )


if __name__ == "__main__":
    main()
