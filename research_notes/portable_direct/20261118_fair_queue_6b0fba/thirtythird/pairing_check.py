"""Finite comparison of labelled matching tables. Run with Python 3.10+."""
import json
from collections import Counter
from itertools import combinations, permutations, product


def parity(perm):
    return sum(x > y for i, x in enumerate(perm) for y in perm[i + 1:]) % 2


def states(n):
    return sorted(permutations(range(n)), key=lambda perm: (parity(perm), perm))


def mask(perm):
    n = len(perm)
    return sum(1 << (i * n + j) for i, j in enumerate(perm))


def compose(left, right):
    return tuple(left[j] for j in right)


def word_name(perm):
    return "".join(str(i + 1) for i in perm)


def norm_counts(domain):
    counts = {}
    for modulus in range(2, 13):
        count = 0
        for x in product(range(modulus), repeat=4):
            matrix = (*x[:2], 0, *x[2:], 0, 0, 0, 0)
            scores = [sum(matrix[3*i+j] for i, j in enumerate(p)) % modulus for p in domain]
            if len(set(scores[:3])) == len(set(scores[3:])) == 1 and scores[0] != scores[3]:
                count += 1
        assert count == (2 if modulus % 3 == 0 else 0)
        counts[modulus] = count
    return counts


def binary_rank(vectors):
    pivots = {}
    for v in vectors:
        while v.bit_length() in pivots:
            v ^= pivots[v.bit_length()]
        if v:
            pivots[v.bit_length()] = v
    return len(pivots)


def all_binary_sensors(permutation_masks):
    columns = {tuple((h & p).bit_count() % 2 for p in permutation_masks) for h in range(512)}
    assert len(columns) == 32
    separated = Counter(sum(x != y for x in c[:3] for y in c[3:]) for c in columns)
    assert separated == {0: 2, 4: 18, 6: 12}
    count = 0
    for u, v in product(columns, repeat=2):
        labels = list(zip(u, v))
        if set(labels[:3]).isdisjoint(labels[3:]):
            assert sorted((len(set(labels[:3])), len(set(labels[3:])))) == [1, 3]
            count += 1
    assert count == 48
    return separated, count


def code_lengths(permutation_masks, sensors):
    examples = {}
    for d in range(1, 33):
        length = (3*d + 1) // 2
        codes = [[(p & sensors[j % 3]).bit_count() % 2 for j in range(length)]
                 for p in permutation_masks]
        distance = min(sum(a != b for a, b in zip(u, v)) for u in codes[:3] for v in codes[3:])
        assert distance == d
        if d <= 7:
            examples[d] = [length, distance]
    return examples


def report():
    domain = states(3)
    permutation_masks = [mask(p) for p in domain]
    # Exhaust all ambient binary tables before applying margins and capacities.
    row_masks = [7 << (3*j) for j in range(3)]
    col_masks = [73 << j for j in range(3)]
    feasible = [h for h in range(512) if all((h & m).bit_count() == 1 for m in row_masks + col_masks)]
    assert sorted(feasible) == sorted(permutation_masks)
    assert sorted(h for h in feasible if h & 1 == 0) == sorted(mask(p) for p in domain if p[0] != 0)

    odd = permutation_masks[3]
    sensors = []
    for p in permutation_masks[:3]:
        edge = p & odd
        assert edge.bit_count() == 1
        sensors.append(odd ^ edge)
    assert sensors[0] == (1 << 5) + (1 << 7)
    separated, pairs = all_binary_sensors(permutation_masks)
    sensor = {p: (sensors[0] & mask(p)).bit_count() % 2 for p in domain}
    trace = {p: sum(i == j for i, j in enumerate(p)) % 3 for p in domain}
    assert all(trace[p] == parity(p) for p in domain)

    id3, a, b = (0, 1, 2), (1, 0, 2), (0, 2, 1)
    words = [("", id3), ("A", a), ("B", b), ("AB", compose(a, b)), ("BA", compose(b, a))]
    full_table = {}
    forbidden_table = {}
    for p in domain:
        full_table[word_name(p)] = {
            "A_exit": word_name(compose(a, p)), "B_exit": word_name(compose(b, p)),
            "h_on_empty_A_B_AB_BA": [sensor[compose(g, p)] for _, g in words],
            "trace_mod3": trace[p],
        }
        if p[0] != 0:
            forbidden_table[word_name(p)] = [trace[p]] + [
                "blocked" if compose(g, p)[0] == 0 else trace[compose(g, p)] for g in (a, b)
            ]

    witnesses = {}
    lengths = Counter()
    for p, q in combinations(domain, 2):
        name = next(w for w, g in words if sensor[compose(g, p)] != sensor[compose(g, q)])
        witnesses[word_name(p) + "/" + word_name(q)] = name or "empty"
        lengths[len(name)] += 1
    assert lengths == {0: 8, 1: 6, 2: 1}
    assert all([sensor[compose(g, p)] for g in (a, b)] == [0, 0] for p in domain[:3])
    assert sorted(2*sensor[compose(a, p)] + sensor[compose(b, p)] for p in domain[3:]) == [1, 2, 3]
    assert {tuple(sensor[compose(g, p)] for p in domain) for _, g in (words[0], *words[3:])} == {
        tuple((h & p).bit_count() % 2 for p in permutation_masks) for h in sensors
    }
    forbid_lengths = Counter()
    for x, y in combinations(forbidden_table.values(), 2):
        assert x[:2] != y[:2]
        forbid_lengths[int(x[0] == y[0])] += 1
    assert forbid_lengths == {0: 4, 1: 2}

    # Encodings 0,1,2,3 correspond to zero, one, omega, omega+1 in F4.
    omega = (0, 2, 3, 1)
    four = [Counter(), Counter()]
    for p in states(4):
        value = p[2] ^ p[0] ^ omega[p[1] ^ p[0]]
        four[parity(p)][value] += 1
    assert four == [{0: 12}, {1: 4, 2: 4, 3: 4}]
    ranks = {}
    for n in range(2, 8):
        ps = states(n)
        base = mask(ps[0])
        ranks[n] = [binary_rank(mask(p) ^ base for p in selected)
                    for selected in (ps[:len(ps)//2], ps)]
    assert all(ranks[n] == [(n-1)**2]*2 for n in (5, 6, 7))

    return {
        "external_finite_model": True, "cell_port_binding": "UNKNOWN", "native_BRC_calls": 0,
        "full_observation_table": full_table, "binary_shortest_word_for_each_pair": witnesses,
        "binary_shortest_length_counts": lengths, "forbidden_11_trace_on_empty_A_B": forbidden_table,
        "forbidden_11_shortest_length_counts": forbid_lengths,
        "gauge_normalized_nonconstant_parity_matrices": norm_counts(domain),
        "s3_distinct_binary_columns": 32, "cross_separations_per_column": separated,
        "ordered_parity_decoding_pairs_of_columns": pairs, "masks_bit_number_3i_plus_j": sensors,
        "length_and_measured_minimum_cross_distance": code_lengths(permutation_masks, sensors),
        "all_distances_verified_to": 32, "s4_F4_symbol_even_odd_distributions": four,
        "binary_affine_hull_dimensions_even_full": ranks,
        "logical_costs": {
            "binary_tables_tested": 512, "feasible_full_matched_states": len(feasible),
            "feasible_forbidden_11_states": len(forbidden_table), "full_domain_named_transitions": 12,
            "forbidden_11_attempted_transitions": 8, "forbidden_11_blocked_transitions": 2,
            "full_stored_scalar_observations_2_per_state": 12, "full_pair_witnesses": len(witnesses),
            "full_pair_word_search_max_depth": 2, "binary_weight_matrices_tested": 512,
            "weight_matrix_matching_sums": 512*6, "ordered_column_pairs_tested": 1024,
            "normalized_scalar_weight_matrices_tested": sum(m**4 for m in range(2, 13)),
        },
    }


if __name__ == "__main__":
    print(json.dumps(report(), ensure_ascii=False, sort_keys=True, indent=2))
