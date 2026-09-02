#!/usr/bin/env python3
"""Deterministic exact checker for P000 philosophy-first Q25.

The frozen observable is exactly Q22:
  c0(x) = primitive simple-cycle multiplicity profile through x,
  c_{t+1}(x) = (c_t(x), multiset of neighboring c_t-colors).

Q25 does not add any observable.  It certifies the n=10 collision-free frontier
by a complete orbit certificate: one graph representative per distinct stable
packet, exact automorphism group orders, and exact connected labeled
realization counts for every degree sector 3^r 2^(10-r).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from functools import lru_cache
from pathlib import Path

EXPECTED_Q22_CONNECTED = {
    4: {2: 1, 4: 1},
    5: {2: 7, 4: 6},
    6: {2: 54, 4: 54, 6: 70},
    7: {2: 450, 4: 552, 6: 810},
    8: {2: 4080, 4: 6012, 6: 10080, 8: 19320},
    9: {2: 40320, 4: 69840, 6: 132660, 8: 282240},
}
EXPECTED_N10_CONNECTED = {
    2: 433440,
    4: 866520,
    6: 1847340,
    8: 4329360,
    10: 11166120,
}
EXPECTED_N10_REPRESENTATIVES = {2: 18, 4: 109, 6: 198, 8: 113, 10: 19}
EXPECTED_TOTAL_REPRESENTATIVES = 457
EXPECTED_TOTAL_CONNECTED = 18642780
EXPECTED_COMBINED_PACKET_SHA256 = "fc81927d21515e237caf5ed8023ebcb51835b160d133c112d2c89b870b1f53ba"


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def parse_graph6(text: str) -> tuple[int, ...]:
    """Decode short-form graph6 (sufficient here because n=10 < 63)."""
    check(isinstance(text, str) and text, "graph6 text missing")
    values = [ord(ch) - 63 for ch in text]
    check(all(0 <= value <= 63 for value in values), "invalid graph6 byte")
    n = values[0]
    check(n == 10, f"graph6 n drift: {n}")
    bits = []
    for value in values[1:]:
        bits.extend((value >> shift) & 1 for shift in (5, 4, 3, 2, 1, 0))
    check(len(bits) >= n * (n - 1) // 2, "truncated graph6 payload")
    adj = [0] * n
    k = 0
    for j in range(1, n):
        for i in range(j):
            if bits[k]:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
            k += 1
    check(all(bit == 0 for bit in bits[k:]), "nonzero graph6 padding")
    return tuple(adj)

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


def root_profiles(adj: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    """Q22 primitive-return multiplicities: simple unoriented cycles through each root."""
    n = len(adj)
    counts = [[0] * (n + 1) for _ in range(n)]
    for start in range(n):
        path = [start]
        higher = ~((1 << (start + 1)) - 1)

        def dfs(v: int, used: int) -> None:
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
    """Lossless finite-DAG compression of the exact Q22 semantic stable packet."""
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


def packet_encoding(packet) -> str:
    return json.dumps(packet, separators=(",", ":"))


@lru_cache(maxsize=None)
def simple_graph_count(degrees: tuple[int, ...]) -> int:
    """Exact labeled simple-graph realization count for a degree multiset.

    A distinguished labeled vertex of maximum degree is connected to k labels
    from each remaining degree class; binomial factors count those label choices.
    Sorting only quotients permutation-equivalent residual states and does not
    quotient the labeled graphs themselves.
    """
    seq = tuple(sorted((d for d in degrees if d > 0), reverse=True))
    if not seq:
        return 1
    n = len(seq)
    d = seq[0]
    if d >= n:
        return 0
    rest = list(seq[1:])
    groups = [(value, rest.count(value)) for value in sorted(set(rest), reverse=True)]
    answer = 0

    def choose_group(i: int, left: int, picked: list[int], multiplicity: int) -> None:
        nonlocal answer
        if i == len(groups):
            if left:
                return
            nxt = []
            for (value, count), k in zip(groups, picked):
                nxt.extend([value - 1] * k)
                nxt.extend([value] * (count - k))
            if min(nxt, default=0) < 0:
                return
            answer += multiplicity * simple_graph_count(tuple(nxt))
            return
        value, count = groups[i]
        for k in range(min(count, left) + 1):
            if value == 0 and k:
                continue
            choose_group(
                i + 1,
                left - k,
                picked + [k],
                multiplicity * math.comb(count, k),
            )

    choose_group(0, d, [], 1)
    return answer


@lru_cache(maxsize=None)
def total_sector(c2: int, c3: int) -> int:
    return simple_graph_count((2,) * c2 + (3,) * c3)


@lru_cache(maxsize=None)
def connected_sector(c2: int, c3: int) -> int:
    """Exact connected labeled count by the component of one distinguished vertex."""
    n = c2 + c3
    if n == 0:
        return 0
    answer = total_sector(c2, c3)
    if c3:
        # Distinguish one degree-3 label.
        rem3, rem2 = c3 - 1, c2
        for other3 in range(rem3 + 1):
            for s2 in range(rem2 + 1):
                s3 = 1 + other3
                size = s2 + s3
                if size == n or size <= 3:
                    continue
                ways = math.comb(rem3, other3) * math.comb(rem2, s2)
                answer -= ways * connected_sector(s2, s3) * total_sector(c2 - s2, c3 - s3)
    else:
        # Only used as a recursive primitive; distinguish one degree-2 label.
        rem2 = c2 - 1
        for other2 in range(rem2 + 1):
            s2 = 1 + other2
            if s2 == n or s2 <= 2:
                continue
            ways = math.comb(rem2, other2)
            answer -= ways * connected_sector(s2, 0) * total_sector(c2 - s2, 0)
    return answer


def automorphism_count(
    adj: tuple[int, ...], profiles: tuple[tuple[int, ...], ...], colors: tuple[int, ...]
) -> int:
    """Exact automorphism count by invariant-bucketed adjacency backtracking."""
    n = len(adj)
    degrees = [row.bit_count() for row in adj]
    keys = [(degrees[v], profiles[v], colors[v]) for v in range(n)]
    buckets = {}
    for w, key in enumerate(keys):
        buckets.setdefault(key, []).append(w)
    candidates = [buckets[key] for key in keys]
    order = sorted(range(n), key=lambda v: (len(candidates[v]), -degrees[v], v))
    mapping = [-1] * n
    total = 0

    def rec(i: int, used: int) -> None:
        nonlocal total
        if i == n:
            total += 1
            return
        v = order[i]
        for w in candidates[v]:
            bit = 1 << w
            if used & bit:
                continue
            if all(
                ((adj[v] >> order[j]) & 1) == ((adj[w] >> mapping[order[j]]) & 1)
                for j in range(i)
            ):
                mapping[v] = w
                rec(i + 1, used | bit)
                mapping[v] = -1

    rec(0, 0)
    check(total > 0, "identity automorphism missing")
    return total


def verify_degree_count_regression() -> None:
    for n, sectors in EXPECTED_Q22_CONNECTED.items():
        for r, expected in sectors.items():
            actual = connected_sector(n - r, r)
            check(actual == expected, f"Q22 normalized connected count drift n={n} r={r}: {actual} != {expected}")
    for r, expected in EXPECTED_N10_CONNECTED.items():
        actual = connected_sector(10 - r, r)
        check(actual == expected, f"n=10 normalized connected count drift r={r}: {actual} != {expected}")


def verify_artifact(path: Path) -> dict[str, int]:
    value = json.loads(path.read_text(encoding="utf-8"))
    check(value.get("schema") == "P000_Q25_RETURN_PROFILE_1WL_N10_EXACT_ORBIT_CERTIFICATE_V1", "artifact schema drift")
    check(value.get("n") == 10, "artifact n drift")
    check(value.get("task_id") == "RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-FIRST-COLLISION-FRONTIER", "artifact task drift")
    check(value.get("publication_id") == "TP2-00DBAF3804A8CB88ED06", "artifact publication drift")
    check(value.get("total_representatives") == EXPECTED_TOTAL_REPRESENTATIVES, "artifact representative total drift")
    check(value.get("total_normalized_connected") == EXPECTED_TOTAL_CONNECTED, "artifact connected total drift")
    check(value.get("q22_regression_normalized_connected") == {str(n): {str(r): c for r, c in rows.items()} for n, rows in EXPECTED_Q22_CONNECTED.items()}, "artifact Q22 regression count drift")
    check(value.get("sector_expected_normalized_connected") == {str(r): c for r, c in EXPECTED_N10_CONNECTED.items()}, "artifact n=10 sector count drift")

    sectors = value.get("sectors")
    check(isinstance(sectors, dict), "artifact sectors missing")
    all_packet_encodings = []
    seen_graph6 = set()
    total_reps = 0
    total_labels = 0

    for r in (2, 4, 6, 8, 10):
        sector = sectors.get(str(r))
        check(isinstance(sector, dict), f"sector r={r} missing")
        graph6_rows = sector.get("graph6")
        aut_sizes = sector.get("aut_sizes")
        check(isinstance(graph6_rows, list), f"sector r={r} graph6 list missing")
        check(isinstance(aut_sizes, list), f"sector r={r} aut-size list missing")
        check(len(graph6_rows) == EXPECTED_N10_REPRESENTATIVES[r], f"sector r={r} representative count drift")
        check(len(aut_sizes) == len(graph6_rows), f"sector r={r} aut-size length drift")
        check(sector.get("representative_count") == len(graph6_rows), f"sector r={r} metadata representative count drift")
        check(graph6_rows == sorted(graph6_rows), f"sector r={r} graph6 rows not sorted")

        packet_encodings = []
        orbit_sum = 0
        normalized_label_factor = math.factorial(r) * math.factorial(10 - r)
        for text, frozen_aut in zip(graph6_rows, aut_sizes):
            check(isinstance(text, str), f"sector r={r} graph6 row not string")
            check(text not in seen_graph6, "duplicate graph6 representative")
            seen_graph6.add(text)
            adj = parse_graph6(text)
            check(connected(adj), f"sector r={r} representative disconnected")
            degrees = [x.bit_count() for x in adj]
            check(Counter(degrees) == Counter({3: r, 2: 10 - r}), f"sector r={r} degree sequence drift")

            profiles, colors, packet, _stabilization = stable_packet(adj)
            encoded = packet_encoding(packet)
            aut = automorphism_count(adj, profiles, colors)
            check(frozen_aut == aut, f"sector r={r} automorphism count drift")
            check(normalized_label_factor % aut == 0, f"sector r={r} nonintegral orbit size")
            orbit_sum += normalized_label_factor // aut
            packet_encodings.append(encoded)
            all_packet_encodings.append(encoded)

        check(len(packet_encodings) == len(set(packet_encodings)), f"stable packet collision inside sector r={r}")
        packet_encodings.sort()
        sector_digest = hashlib.sha256(("\n".join(packet_encodings) + "\n").encode("utf-8")).hexdigest()
        check(sector.get("packet_image_sha256") == sector_digest, f"sector r={r} packet image digest drift")
        expected_labels = EXPECTED_N10_CONNECTED[r]
        check(orbit_sum == expected_labels, f"sector r={r} orbit cover incomplete: {orbit_sum} != {expected_labels}")
        check(sector.get("normalized_label_orbit_sum") == orbit_sum, f"sector r={r} artifact orbit sum drift")
        total_reps += len(graph6_rows)
        total_labels += orbit_sum

    check(total_reps == EXPECTED_TOTAL_REPRESENTATIVES, "total representative count drift")
    check(total_labels == EXPECTED_TOTAL_CONNECTED, "total n=10 orbit cover drift")
    check(len(all_packet_encodings) == len(set(all_packet_encodings)), "stable packet collision across n=10 degree sectors")
    all_packet_encodings.sort()
    combined_digest = hashlib.sha256(("\n".join(all_packet_encodings) + "\n").encode("utf-8")).hexdigest()
    check(combined_digest == EXPECTED_COMBINED_PACKET_SHA256, "combined packet image digest drift")
    check(value.get("combined_packet_image_sha256") == combined_digest, "artifact combined packet digest drift")

    return {
        "representatives": total_reps,
        "normalized_connected": total_labels,
        "packets": len(all_packet_encodings),
    }

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--artifact",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "research_artifacts"
        / "P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_FIRST_COLLISION_FRONTIER"
        / "P000_Q25_RETURN_PROFILE_1WL_N10_EXACT_ORBIT_CERTIFICATE_V1.json",
    )
    args = parser.parse_args()
    verify_degree_count_regression()
    summary = verify_artifact(args.artifact)
    print(
        "PASS Q25 n=10 exact orbit certificate: "
        f"representatives={summary['representatives']} "
        f"normalized_connected={summary['normalized_connected']} "
        f"stable_packets={summary['packets']} "
        "collision=0 lower_bound=n<=10"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
