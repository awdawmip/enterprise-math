#!/usr/bin/env python3
"""Independent exact audit of frozen Euler FCC chirality K4 two-sheet cover.

Historical input: enterprise-math@fd2bcff10ca6e147348b6c1236027fc0d2877df3
src/enterprise_math/euler_fcc_chirality.py and
src/enterprise_math/euler_fcc_chirality_connectivity.py.
Counts here are DERIVED cover geodesic words, not native signed X6 BRC.
"""
import json
from collections import Counter, deque
from itertools import combinations, product

EDGES = tuple(combinations(range(4), 2))
FACES = tuple(combinations(range(4), 3))
INDEX = {edge: index for index, edge in enumerate(EDGES)}
ROOTS = tuple(product(range(4), (0, 1)))

PROFILES = {
    "flat": ((1, 1), (3, 3)),
    "two_odd_intersection": ((1, 1), (3, 3), (3, 4), (1, 4)),
    "two_odd_complement": ((1, 1), (3, 3), (2, 2), (2, 4)),
    "all_odd": ((1, 1), (3, 3), (3, 6), (1, 6)),
}


def require(flag, why):
    if not flag:
        raise RuntimeError(why)


def face_holonomy(bits):
    return tuple(
        bits[INDEX[(a, b)]] ^ bits[INDEX[(a, c)]] ^ bits[INDEX[(b, c)]]
        for a, b, c in FACES
    )


def next_states(bits, state):
    a, sheet = state
    return tuple((b, sheet ^ bits[INDEX[tuple(sorted((a, b)))]]) for b in range(4) if b != a)


def bfs_counts(bits, root):
    distances = {root: 0}
    multiplicities = {root: 1}
    todo = deque([root])
    while todo:
        vertex = todo.popleft()
        d = distances[vertex]
        for neighbor in next_states(bits, vertex):
            if neighbor not in distances:
                distances[neighbor] = d + 1
                multiplicities[neighbor] = multiplicities[vertex]
                todo.append(neighbor)
            elif distances[neighbor] == d + 1:
                multiplicities[neighbor] += multiplicities[vertex]
    profile = tuple((sum(d == k for d in distances.values()),
                     sum(multiplicities[v] for v in distances if distances[v] == k))
                    for k in range(max(distances.values()) + 1))
    return distances, multiplicities, profile


def independent_walk_counts(bits, root, max_length=3):
    # All word prefixes of length <=3, including detours; no BFS recurrence reused.
    words = Counter({root: 1})
    all_lengths = [words]
    for _ in range(max_length):
        nxt = Counter()
        for vertex, count in words.items():
            for neighbor in next_states(bits, vertex):
                nxt[neighbor] += count
        all_lengths.append(nxt)
        words = nxt
    return all_lengths


def expected_profile(h, base_index):
    ones = [FACES[j] for j, bit in enumerate(h) if bit]
    if not ones:
        return "flat"
    if len(ones) == 4:
        return "all_odd"
    require(len(ones) == 2, "face parity must be even")
    shared_vertices = set(ones[0]).intersection(ones[1])
    require(len(shared_vertices) == 2, "two odd faces intersect in one edge")
    return "two_odd_intersection" if base_index in shared_vertices else "two_odd_complement"


def main():
    result_classes = Counter()
    holonomy_assignment_count = Counter()
    root_checks = 0
    shortest_path_checks = 0
    gauge_checks = 0
    for bits in product((0, 1), repeat=6):
        h = face_holonomy(bits)
        holonomy_assignment_count["".join(map(str,h))] += 1
        for root in ROOTS:
            distances, counts, profile = bfs_counts(bits, root)
            profile_kind = expected_profile(h, root[0])
            require(profile == PROFILES[profile_kind], f"wrong profile bits={bits} root={root}: {profile} vs {profile_kind}")
            walks = independent_walk_counts(bits, root, 3)
            for target in distances:
                d = distances[target]
                require(walks[d][target] == counts[target], f"independent word mismatch for {bits}/{root}/{target}")
                shortest_path_checks += 1
            root_checks += 1
            result_classes[profile_kind] += 1
        # Double-cover gauge transformation is an actual source operation.
        for g in product((0,1), repeat=4):
            transformed = tuple(bits[index] ^ g[a] ^ g[b] for index,(a,b) in enumerate(EDGES))
            require(face_holonomy(transformed) == h, "gauge changed face holonomy")
            for root in ROOTS:
                moved_root = (root[0], root[1] ^ g[root[0]])
                require(bfs_counts(bits, root)[2] == bfs_counts(transformed, moved_root)[2],
                        "gauge changed rooted shell path profile")
                gauge_checks += 1
    require(sum(holonomy_assignment_count.values()) == 64, "wrong assignment count")
    require(len(holonomy_assignment_count) == 8, "wrong face holonomy class count")
    require(all(v == 8 for v in holonomy_assignment_count.values()), "wrong gauge orbit count")
    require(result_classes == Counter(flat=64, two_odd_intersection=192,
                                      two_odd_complement=192, all_odd=64), "wrong rooted class frequencies")
    report = {
        "schema":"X6_UNIT167_FCC_CHIRALITY_ROOTED_BRC_EXACT_RESULT_V1",
        "frozen_source":"fd2bcff10ca6e147348b6c1236027fc0d2877df3",
        "source_semantic_type":"DERIVED_TETRAHEDRAL_FCC_K4_TWO_SHEET_ORIENTATION_COVER_NOT_NATIVE_SIGNED_X6",
        "edge_assignments":64, "face_holonomy_classes":8,
        "assignments_per_holonomy_class":8,
        "rooted_instances":root_checks,
        "independent_shortest_endpoint_word_checks":shortest_path_checks,
        "gauge_equivariant_rooted_checks":gauge_checks,
        "rooted_profile_frequencies":dict(sorted(result_classes.items())),
        "profiles":{"flat":PROFILES['flat'],"two_odd_intersection":PROFILES['two_odd_intersection'],
                    "two_odd_complement":PROFILES['two_odd_complement'],"all_odd":PROFILES['all_odd']},
        "violations":0,
        "original_frozen_tests_executed":False,
        "original_R063_native_benchmark_rerun":False,
        "review":"UNREVIEWED/NOT_ADMITTED"
    }
    print(json.dumps(report, ensure_ascii=False, sort_keys=True, separators=(',', ':')))

if __name__ == '__main__':
    main()
