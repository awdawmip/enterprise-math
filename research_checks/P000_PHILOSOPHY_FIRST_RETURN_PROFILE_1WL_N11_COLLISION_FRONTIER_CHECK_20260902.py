#!/usr/bin/env python3
"""Deterministic exact checker for P000 philosophy-first Q27.

The observable is bit-for-bit the frozen Q22/Q25 observable:
  c0(x) = primitive simple-cycle multiplicity profile through x,
  c_{t+1}(x) = (c_t(x), multiset of neighboring c_t-colors),
with graph output the anonymous complete stabilized packet R_inf(X).

Representative discovery is deliberately not completeness authority.  A fixed
SplitMix64 stream only finds candidate isomorphism classes.  The proof closes
when exact automorphism/orbit sizes of one representative per distinct packet
sum to the independently computed exact connected degree-sector count.  Since
isomorphic graphs have equal packets, distinct packet representatives lie in
disjoint isomorphism classes.  Equality of the disjoint orbit sum with the
whole sector leaves no omitted class -- including no second nonisomorphic
class hiding in an already-seen packet.  Hence packet injectivity is exact.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from functools import lru_cache
from pathlib import Path

TASK_ID = "RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-1WL-N11-COLLISION-FRONTIER"
PUBLICATION_ID = "TP2-875D6C62E617BCC7CE63"
CLAIM_ID = "chatgpt-pq27-20260902-0923-6f3a9c"
BASE_SEED = 0x20260902
SEED_MIX = 0xD1B54A32D192ED03
MASK64 = (1 << 64) - 1

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
EXPECTED_N11_CONNECTED = {
    2: 5050080,
    4: 11476080,
    6: 27213300,
    8: 69824160,
    10: 194934600,
}
EXPECTED_N11_REPRESENTATIVES = {2: 23, 4: 197, 6: 536, 8: 482, 10: 114}
EXPECTED_CLOSURE_SAMPLE = {2: 179, 4: 1852, 6: 13207, 8: 10701, 10: 1707}
EXPECTED_PACKET_SHA256 = {
    2: "08d08ab8ce8ce8237ecada9ea9ec76c7a6c87a4bf06ef455c61aafb28cdc8738",
    4: "0527cbbeb5474498b2252d9e417dba49fa020ef0a9f6d39d2a26631c2f11cd71",
    6: "fd60fdc131487e40f0a40e26ef9e63fd5d7a0c6d2b2e01763c2fa4189055852d",
    8: "e94a4220802e9b99b446a619dd203194b0fb7007b47980559649313d68e1315c",
    10: "e84ca3046ab07862854cdb783e8ee0ac6d54eed061f53a2c28f03d5adc1f3fa0",
}
EXPECTED_STABILIZATION_CENSUS = {
    2: {1: 3, 2: 11, 3: 8, 4: 1},
    4: {0: 5, 1: 60, 2: 90, 3: 40, 4: 2},
    6: {0: 56, 1: 277, 2: 165, 3: 37, 4: 1},
    8: {0: 172, 1: 215, 2: 82, 3: 13},
    10: {0: 85, 1: 17, 2: 12},
}
EXPECTED_AUT_CENSUS = {
    2: {2: 7, 4: 12, 8: 3, 12: 1},
    4: {1: 37, 2: 81, 4: 61, 8: 16, 16: 2},
    6: {1: 181, 2: 203, 4: 110, 8: 38, 16: 3, 32: 1},
    8: {1: 177, 2: 166, 4: 92, 6: 3, 8: 37, 12: 3, 16: 4},
    10: {1: 24, 2: 40, 4: 31, 8: 13, 16: 5, 32: 1},
}
EXPECTED_TOTAL_REPRESENTATIVES = 1352
EXPECTED_TOTAL_CONNECTED = 308498220
EXPECTED_COMBINED_PACKET_SHA256 = "195df8a4567cec68de826035eee044c9915b3dafb207f260324a04e29a3535d2"


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


def root_profiles(adj: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    """Frozen Q22 primitive-return profile: simple unoriented cycles through each root."""
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
    """Exact finite-DAG compression used by Q25, now with n=11 and no semantic change."""
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
    """Exact labeled simple-graph realization count for a degree multiset."""
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
    """Exact connected labeled count by subtracting the distinguished component."""
    n = c2 + c3
    if n == 0:
        return 0
    answer = total_sector(c2, c3)
    if c3:
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
        rem2 = c2 - 1
        for other2 in range(rem2 + 1):
            s2 = 1 + other2
            if s2 == n or s2 <= 2:
                continue
            answer -= math.comb(rem2, other2) * connected_sector(s2, 0) * total_sector(c2 - s2, 0)
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


class SplitMix64:
    """Self-contained reproducible discovery PRNG; it is not proof authority."""

    def __init__(self, seed: int):
        self.state = seed & MASK64

    def next64(self) -> int:
        self.state = (self.state + 0x9E3779B97F4A7C15) & MASK64
        z = self.state
        z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & MASK64
        z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & MASK64
        return (z ^ (z >> 31)) & MASK64

    def randbelow(self, n: int) -> int:
        return self.next64() % n

    def shuffle(self, values: list[int]) -> None:
        for i in range(len(values) - 1, 0, -1):
            j = self.randbelow(i + 1)
            values[i], values[j] = values[j], values[i]


def discovery_graph(r: int, rng: SplitMix64) -> tuple[int, ...] | None:
    """Configuration-model discovery. Conditional distribution is irrelevant to proof closure."""
    n = 11
    degrees = [3] * r + [2] * (n - r)
    for _ in range(100):
        stubs = [v for v, d in enumerate(degrees) for _ in range(d)]
        rng.shuffle(stubs)
        adj = [0] * n
        ok = True
        for i in range(0, len(stubs), 2):
            a, b = stubs[i], stubs[i + 1]
            if a == b or ((adj[a] >> b) & 1):
                ok = False
                break
            adj[a] |= 1 << b
            adj[b] |= 1 << a
        if ok and connected(tuple(adj)):
            return tuple(adj)
    return None


def discover_and_certify_sector(r: int) -> dict:
    target = EXPECTED_N11_CONNECTED[r]
    factor = math.factorial(r) * math.factorial(11 - r)
    rng = SplitMix64(BASE_SEED ^ ((r * SEED_MIX) & MASK64))
    reps: dict[str, tuple[int, int]] = {}
    orbit_sum = 0
    max_samples = 20000
    closure_sample = None

    for sample in range(1, max_samples + 1):
        adj = discovery_graph(r, rng)
        if adj is None:
            continue
        degrees = Counter(row.bit_count() for row in adj)
        check(degrees == Counter({3: r, 2: 11 - r}), f"degree drift r={r}")
        check(connected(adj), f"disconnected discovery graph r={r}")
        profiles, colors, packet, stabilization = stable_packet(adj)
        encoded = packet_encoding(packet)
        if encoded in reps:
            continue

        aut = automorphism_count(adj, profiles, colors)
        check(factor % aut == 0, f"nonintegral normalized orbit r={r} aut={aut}")
        orbit = factor // aut
        reps[encoded] = (aut, stabilization)
        orbit_sum += orbit
        check(orbit_sum <= target, f"disjoint orbit sum exceeded exact sector total r={r}")
        if orbit_sum == target:
            closure_sample = sample
            break

    check(closure_sample is not None, f"exact orbit cover did not close r={r}")
    check(closure_sample == EXPECTED_CLOSURE_SAMPLE[r], f"deterministic closure-sample drift r={r}")
    check(len(reps) == EXPECTED_N11_REPRESENTATIVES[r], f"representative count drift r={r}")

    encodings = sorted(reps)
    digest = hashlib.sha256(("\n".join(encodings) + "\n").encode("utf-8")).hexdigest()
    check(digest == EXPECTED_PACKET_SHA256[r], f"packet image digest drift r={r}")
    stabilization_census = dict(sorted(Counter(stab for _aut, stab in reps.values()).items()))
    aut_census = dict(sorted(Counter(aut for aut, _stab in reps.values()).items()))
    check(stabilization_census == EXPECTED_STABILIZATION_CENSUS[r], f"stabilization census drift r={r}")
    check(aut_census == EXPECTED_AUT_CENSUS[r], f"automorphism census drift r={r}")

    return {
        "r": r,
        "closure_sample": closure_sample,
        "representatives": len(reps),
        "normalized_connected": orbit_sum,
        "packet_sha256": digest,
        "encodings": encodings,
        "stabilization_census": stabilization_census,
        "aut_census": aut_census,
    }


def verify_degree_count_regression() -> None:
    for n, sectors in EXPECTED_Q22_CONNECTED.items():
        for r, expected in sectors.items():
            actual = connected_sector(n - r, r)
            check(actual == expected, f"Q22 connected-count drift n={n} r={r}: {actual} != {expected}")
    for r, expected in EXPECTED_N10_CONNECTED.items():
        actual = connected_sector(10 - r, r)
        check(actual == expected, f"Q25 n=10 connected-count drift r={r}: {actual} != {expected}")
    for r, expected in EXPECTED_N11_CONNECTED.items():
        actual = connected_sector(11 - r, r)
        check(actual == expected, f"Q27 n=11 connected-count drift r={r}: {actual} != {expected}")


def verify_artifact(path: Path, sectors: dict[int, dict], combined_digest: str) -> None:
    value = json.loads(path.read_text(encoding="utf-8"))
    check(value.get("schema") == "P000_Q27_RETURN_PROFILE_1WL_N11_EXACT_ORBIT_CERTIFICATE_V1", "artifact schema drift")
    check(value.get("task_id") == TASK_ID, "artifact task drift")
    check(value.get("publication_id") == PUBLICATION_ID, "artifact publication drift")
    check(value.get("claim_id") == CLAIM_ID, "artifact claim drift")
    check(value.get("n") == 11, "artifact n drift")
    check(value.get("sector_expected_normalized_connected") == {str(r): v for r, v in EXPECTED_N11_CONNECTED.items()}, "artifact connected counts drift")
    check(value.get("sector_representatives") == {str(r): v for r, v in EXPECTED_N11_REPRESENTATIVES.items()}, "artifact representative counts drift")
    check(value.get("sector_samples_to_exact_orbit_closure") == {str(r): v for r, v in EXPECTED_CLOSURE_SAMPLE.items()}, "artifact closure samples drift")
    check(value.get("sector_packet_image_sha256") == {str(r): v for r, v in EXPECTED_PACKET_SHA256.items()}, "artifact packet digests drift")
    check(value.get("total_representatives") == EXPECTED_TOTAL_REPRESENTATIVES, "artifact total representatives drift")
    check(value.get("total_normalized_connected") == EXPECTED_TOTAL_CONNECTED, "artifact total connected drift")
    check(value.get("combined_packet_image_sha256") == combined_digest, "artifact combined packet digest drift")
    check(value.get("collision_count") == 0, "artifact collision count drift")
    check(value.get("terminal_class") == "RETURN_PROFILE_1WL_COLLISION_FREE_LOWER_BOUND_EXTENDED_THROUGH_N11", "artifact terminal class drift")
    for r, result in sectors.items():
        frozen_stab = {int(k): v for k, v in value["sector_stabilization_census"][str(r)].items()}
        frozen_aut = {int(k): v for k, v in value["sector_automorphism_size_census"][str(r)].items()}
        check(frozen_stab == result["stabilization_census"], f"artifact stabilization census drift r={r}")
        check(frozen_aut == result["aut_census"], f"artifact automorphism census drift r={r}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--artifact",
        type=Path,
        default=Path(__file__).resolve().parents[1]
        / "research_artifacts"
        / "P000_PHILOSOPHY_FIRST_RETURN_PROFILE_1WL_N11_COLLISION_FRONTIER"
        / "P000_Q27_RETURN_PROFILE_1WL_N11_EXACT_ORBIT_CERTIFICATE_V1.json",
    )
    args = parser.parse_args()

    verify_degree_count_regression()
    sector_results = {r: discover_and_certify_sector(r) for r in (2, 4, 6, 8, 10)}
    total_reps = sum(v["representatives"] for v in sector_results.values())
    total_connected = sum(v["normalized_connected"] for v in sector_results.values())
    check(total_reps == EXPECTED_TOTAL_REPRESENTATIVES, "total representative count drift")
    check(total_connected == EXPECTED_TOTAL_CONNECTED, "total normalized connected count drift")

    all_encodings = [e for r in (2, 4, 6, 8, 10) for e in sector_results[r]["encodings"]]
    check(len(all_encodings) == len(set(all_encodings)), "stable packet collision across n=11 degree sectors")
    all_encodings.sort()
    combined_digest = hashlib.sha256(("\n".join(all_encodings) + "\n").encode("utf-8")).hexdigest()
    check(combined_digest == EXPECTED_COMBINED_PACKET_SHA256, "combined packet image digest drift")
    verify_artifact(args.artifact, sector_results, combined_digest)

    print(
        "PASS Q27 n=11 exact orbit certificate: "
        f"representatives={total_reps} "
        f"normalized_connected={total_connected} "
        f"stable_packets={len(all_encodings)} "
        "collision=0 lower_bound=n<=11"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
