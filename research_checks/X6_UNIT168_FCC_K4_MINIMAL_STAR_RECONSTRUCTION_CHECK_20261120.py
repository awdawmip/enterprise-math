"""Unit168: exact three-star / signed-X6 observer reconstruction certificate.

P000-compatible coordinate observers only; no physical-circle promotion.
Frozen input 59538f585d037d09ef687b28715c4bc1a3f9fe03.
"""
import itertools
import json
from collections import Counter
from math import factorial

SCHEMA = "X6_UNIT168_MINIMAL_STAR_OBSERVER_RECONSTRUCTION_RESULT_V1"
EDGES = list(itertools.combinations(range(4), 2))  # K4 six lines = signed-X6 axes
STARS = [tuple(i for i, e in enumerate(EDGES) if v in e) for v in range(4)]
TRIPLES = list(itertools.combinations(range(6), 3))


def check(condition, label):
    if not condition:
        raise AssertionError(label)


def can(x):
    m = min(x)
    return tuple(t - m for t in x)


def obs(x, triple):
    return can(tuple(x[i] for i in triple))


def components(family):
    adj = [set() for _ in range(6)]
    for triple in family:
        for a, b in itertools.combinations(triple, 2):
            adj[a].add(b)
            adj[b].add(a)
    unseen = set(range(6))
    result = []
    while unseen:
        todo = [min(unseen)]
        seen = set()
        while todo:
            u = todo.pop()
            if u in seen:
                continue
            seen.add(u)
            todo.extend(adj[u] - seen)
        unseen -= seen
        result.append(tuple(sorted(seen)))
    return tuple(result)


def recover_relative(family, observations):
    """BFS computes each coordinate difference from min-zero observations."""
    adj = [set() for _ in range(6)]
    for S, readings in zip(family, observations):
        for j in range(len(S)):
            for k in range(j + 1, len(S)):
                u, v = S[j], S[k]
                delta = readings[k] - readings[j]
                adj[u].add((v, delta))
                adj[v].add((u, -delta))
    potentials = {0: 0}
    todo = [0]
    while todo:
        u = todo.pop()
        for v, delta in adj[u]:
            value = potentials[u] + delta
            if v in potentials:
                check(potentials[v] == value, "inconsistent observer data")
            else:
                potentials[v] = value
                todo.append(v)
    if len(potentials) != 6:
        return None
    return can(tuple(potentials[i] for i in range(6)))


def brc(z):
    length = sum(abs(x) for x in z)
    result = factorial(length)
    for x in z:
        result //= factorial(abs(x))
    return result


def compute():
    check(STARS == [(0, 1, 2), (0, 3, 4), (1, 3, 5), (2, 4, 5)], "K4 star map")
    classes = Counter(len(components(f)) for f in itertools.combinations(TRIPLES, 3))
    check(classes == Counter({1: 480, 2: 600, 3: 60}), "all 1140 triple selections")
    for family in itertools.combinations(TRIPLES, 2):
        check(len(components(family)) >= 2, "two triples cannot connect 6 axes")
    star3_families = list(itertools.combinations(STARS, 3))
    check(len(star3_families) == 4, "four K4 triples-of-three")
    check(all(len(components(f)) == 1 for f in star3_families), "every 3-star family connected")
    check(all(len(components(f)) == 2 for f in itertools.combinations(STARS, 2)), "each 2-star family disconnected")
    state_checks = 0
    distinct_raw_states = 0
    for family in star3_families:
        inverse = {}
        for z in itertools.product((-1, 0, 1), repeat=6):
            readings = tuple(obs(z, S) for S in family)
            reconstructed = recover_relative(family, readings)
            check(reconstructed == can(z), "relative reconstruction")
            h = min(z)
            restored = tuple(t + h for t in reconstructed)
            check(restored == z, "lossless raw Cell coordinate restoration")
            fp = readings
            if fp in inverse:
                check(inverse[fp] == can(z), "observer fiber should be diagonal only")
            else:
                inverse[fp] = can(z)
            state_checks += 1
        distinct_raw_states += len(inverse)
    a = (1, 0, 0, 0, 0, 0)
    b = (1, 0, 0, 0, 0, 1)
    # STAR 0 and STAR 1 do not see coordinate index 5 (K4 edge 2--3).
    check(tuple(obs(a, S) for S in STARS[:2]) == tuple(obs(b, S) for S in STARS[:2]), "2-star alias")
    check(brc(a) == 1 and brc(b) == 2, "2-star BRC loss")
    D = (1,) * 6
    check(all(obs((0,) * 6, S) == obs(D, S) for S in STARS), "diagonal hidden in all star observations")
    check(brc((0,) * 6) == 1 and brc(D) == 720, "BRC distinction across depth")
    for t in range(-7, 8):
        check(all(obs((t,) * 6, S) == (0, 0, 0) for S in STARS), "unbounded depth fiber")
    return {
        "schema": SCHEMA,
        "date": "2026-11-20",
        "task_id": "RS-X6-LEGACY-PLANE-RECONCILIATION",
        "scientific_input_pin": "59538f585d037d09ef687b28715c4bc1a3f9fe03",
        "source_function": "Obs_S(z)=can3(z|S)",
        "k4_edges_axis_order": [list(edge) for edge in EDGES],
        "four_established_k4_star_observers": [list(S) for S in STARS],
        "all_3_of_20_families": 1140,
        "family_counts_by_component_number": {str(k): v for k, v in sorted(classes.items())},
        "connected_three_triple_families": classes[1],
        "established_four_star_choose_three": len(star3_families),
        "established_three_star_connected": 4,
        "established_two_star_connected": 0,
        "raw_state_reconstruction_checks": state_checks,
        "total_distinct_relative_states_seen_across_four_families": distinct_raw_states,
        "two_star_witness": {"x": list(a), "y": list(b), "x_NBRC": brc(a), "y_NBRC": brc(b)},
        "all_star_depth_witness": {"x": [0] * 6, "y": [1] * 6, "x_NBRC": 1, "y_NBRC": 720},
        "full_original_R063_benchmark_rerun": False,
        "mathematical_review": "UNREVIEWED_NOT_ADMITTED",
        "violations": 0
    }


if __name__ == "__main__":
    print(json.dumps(compute(), ensure_ascii=False, sort_keys=True, separators=(",", ":")))
