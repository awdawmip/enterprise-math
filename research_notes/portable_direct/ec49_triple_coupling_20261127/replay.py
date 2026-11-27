"""Verify EC49 triple-rank line compression and sparse Port-coupling witnesses."""

from collections import Counter
from itertools import combinations, combinations_with_replacement, product
from random import Random
import json


def phi(capacity, masks):
    width = len(capacity)
    value = [
        sum(c for i, c in enumerate(capacity) if w >> i & 1)
        - sum(e & w == e for e in masks)
        for w in range(1 << width)
    ]
    for i in range(width):
        for w in range(1 << width):
            value[w] = min(value[w], value[w | 1 << i])
    return value


def trace_gap(table, parts):
    return sum(table[c] for c in parts) - table[-1] - (len(parts) - 1) * table[0]


def line_table(pool, deleted_sets, rank):
    """Use all rank reads as a reference producer, independent of witness search."""
    representative = []
    classes = {}
    for x in pool:
        if rank[x,] == 0:
            classes[x] = -1
            continue
        for group, y in enumerate(representative):
            if rank[tuple(sorted((x, y)))] == 1:
                classes[x] = group
                break
        else:
            classes[x] = len(representative)
            representative.append(x)
    line_set = set()
    for a, b in combinations(range(len(representative)), 2):
        line = {a, b}
        for c in range(len(representative)):
            if c not in (a, b) and rank[tuple(sorted(representative[d] for d in (a, b, c)))] == 2:
                line.add(c)
        if len(line) > 2:
            line_set.add(tuple(sorted(line)))
    lines = sorted(line_set)
    for sample in deleted_sets:
        simple = {classes[x] for x in sample} - {-1}
        recovered = len(simple)
        if recovered == 3 and any(simple.issubset(line) for line in lines):
            recovered = 2
        assert recovered == rank[sample]
    return classes, lines


def preprocess(pool, global_classes, raw_table):
    classes, raw_lines = raw_table
    count = Counter(classes[x] for x in pool)
    assert -1 not in count
    global_of = {classes[x]: global_classes[x] for x in pool}
    assert all(global_of[classes[x]] == global_classes[x] for x in pool)
    lines = []
    for line in raw_lines:
        local_classes = tuple(c for c in line if c in count)
        histogram = Counter()
        for c in local_classes:
            histogram[global_of[c]] += count[c]
        if len(histogram) < 3:
            continue
        # Consecutive elementary symmetric polynomials of the group sizes.
        total = pairs = triples = 0
        for new in histogram.values():
            triples += pairs * new
            pairs += total * new
            total += new
        lines.append((local_classes, histogram, total, pairs, triples))
    return classes, global_of, lines


def sparse_witness(pool, tables, parts, counts):
    global_classes = tables[0][0]
    eligible = tuple(x for x in pool if global_classes[x] != -1)
    weighted = [preprocess(eligible, global_classes, table) for table in tables]
    signs = [len(parts) - 1] + [-1] * len(parts)
    contribution = Counter()
    total_gap = 0
    for sign, (classes, global_of, lines) in zip(signs, weighted):
        by_class = Counter()
        for line, histogram, total, pairs, triples in lines:
            total_gap += sign * triples
            counts["weighted_line_incidences"] += len(line)
            for c in line:
                multiplicity = histogram[global_of[c]]
                by_class[c] += pairs - multiplicity * (total - multiplicity)
        for x in eligible:
            contribution[x] += sign * by_class[classes[x]]
    assert sum(contribution.values()) == 3 * total_gap
    assert all(v >= 0 for v in contribution.values())
    if not total_gap:
        return 0, None

    x = next(x for x in eligible if contribution[x])
    x_global = global_classes[x]
    pair_contribution = Counter()
    lines_by_member = []
    for sign, (classes, global_of, lines) in zip(signs, weighted):
        by_class = {}
        active_line = {}
        for line_id, (line, histogram, total, _, _) in enumerate(lines):
            if classes[x] not in line:
                continue
            for c in line:
                if global_of[c] == x_global:
                    continue
                assert c not in by_class
                by_class[c] = total - histogram[x_global] - histogram[global_of[c]]
                active_line[c] = line_id
        for y in eligible:
            if global_classes[y] != x_global:
                pair_contribution[y] += sign * by_class.get(classes[y], 0)
        lines_by_member.append(active_line)
    assert sum(pair_contribution.values()) == 2 * contribution[x]
    assert all(v >= 0 for v in pair_contribution.values())
    y = next(y for y, v in pair_contribution.items() if v)
    y_global = global_classes[y]
    common_line_ids = [line_map.get(classes[y]) for line_map, (classes, _, _) in zip(lines_by_member, weighted)]
    assert common_line_ids[0] is not None
    z = None
    witness_gap = 0
    for q in eligible:
        if global_classes[q] in (x_global, y_global):
            continue
        line_map, (classes, _, _) = lines_by_member[0], weighted[0]
        if line_map.get(classes[q]) != common_line_ids[0]:
            continue
        together = sum(
            line_id is not None and line_map.get(classes[q]) == line_id
            for line_id, line_map, (classes, _, _) in zip(common_line_ids[1:], lines_by_member[1:], weighted[1:])
        )
        gap = len(parts) - 1 - together
        assert gap >= 0
        if gap > 0 and z is None:
            z, witness_gap = q, gap
    assert z is not None
    return total_gap, (tuple(sorted((x, y, z))), witness_gap)


def verify(capacity, masks, parts, pool, counts):
    counts["states"] += 1
    initial = phi(capacity, masks)
    if trace_gap(initial, parts):
        return
    counts["initial_additive"] += 1
    singles_and_pairs = [d for i in (1, 2) for d in combinations(pool, i)]

    def after(deleted):
        return phi(capacity, [mask for x, mask in enumerate(masks) if x not in deleted])

    states = {(): initial}
    states.update((d, after(d)) for d in singles_and_pairs)
    if any(trace_gap(states[d], parts) for d in singles_and_pairs):
        return
    counts["lower_deletions_additive"] += 1
    triples = list(combinations(pool, 3))
    states.update((d, after(d)) for d in triples)
    tables = [
        line_table(pool, states, {d: values[s] - initial[s] for d, values in states.items()})
        for s in (0, *parts)
    ]
    true_gaps = {d: trace_gap(states[d], parts) for d in triples}
    assert all(g >= 0 for g in true_gaps.values())
    total, witness = sparse_witness(pool, tables, parts, counts)
    assert total == sum(true_gaps.values())
    assert bool(witness) == bool(total)
    if witness:
        triple, gap = witness
        assert true_gaps[triple] == gap
        counts["found_states"] += 1
        counts["max_gap"] = max(counts["max_gap"], max(true_gaps.values()))
    counts["triple_checks"] += len(triples)
    counts["coupling_triples"] += sum(g > 0 for g in true_gaps.values())
    return true_gaps



def reconstructed_rank(table, deleted):
    classes, lines = table
    chosen = {classes[x] for x in deleted} - {-1}
    if len(chosen) == 3 and any(chosen.issubset(line) for line in lines):
        return 2
    return len(chosen)


def insert_table(source, upper, gap, new_label):
    s_classes, s_lines = source
    t_classes, t_lines = upper
    if gap >= 1:
        return {**s_classes, new_label: -1}, s_lines

    new_classes = {new_label: 0}
    old_class_of = {}
    for x, s_group in s_classes.items():
        t_group = t_classes[x]
        if s_group == -1:
            new_classes[x] = -1 if t_group == -1 else 0
        else:
            new_classes[x] = t_group+1
            assert t_group >= 0
            if t_group in old_class_of:
                assert old_class_of[t_group] == s_group
            old_class_of[t_group] = s_group

    divisions = {}
    for t_group, s_group in old_class_of.items():
        divisions.setdefault(s_group, []).append(t_group+1)
    lines = [(0, *pieces) for pieces in divisions.values() if len(pieces) >= 2]
    for line in t_lines:
        surviving = [c for c in line if c in old_class_of]
        if len(surviving) >= 3 and len({old_class_of[c] for c in surviving}) >= 2:
            assert len({old_class_of[c] for c in surviving}) == len(surviving)
            lines.append(tuple(c + 1 for c in surviving))
    return new_classes, lines


def contract_table(table, label):
    classes, lines = table
    block = classes[label]
    if block == -1:
        return {x: c for x, c in classes.items() if x != label}, []
    new_group = {block: -1}
    for line in lines:
        if block not in line:
            continue
        keep = [c for c in line if c != block]
        leader = min(keep)
        assert all(c not in new_group for c in keep)
        new_group.update((c, leader) for c in keep)
    return {x: new_group.get(c, c) for x, c in classes.items() if x != label}, []


def verify_updates(capacity, masks, new_mask, counts):
    n = len(masks)
    old = tuple(range(n))
    enlarged = tuple(range(n+1))
    subsets = [d for i in range(4) for d in combinations(enlarged, i)]

    def hall_states(masks):
        return {
            d: phi(capacity, [mask for x, mask in enumerate(masks) if x not in d])
            for d in subsets
            if not d or d[-1] < len(masks)
        }

    first = hall_states(masks)
    next_state = hall_states(masks + (new_mask,))
    values = {
        s: line_table(old, first, {d: q[s] - first[()][s] for d, q in first.items()})
        for s in range(1 << len(capacity))
    }
    for s, table in values.items():
        target = s | new_mask
        delta = first[()][target] - first[()][s]
        updated = insert_table(table, values[target], delta, n)
        counts["insertion_tables"] += 1
        if delta == 0:
            counts["nontrivial_insertion_tables"] += 1
        for d, q in next_state.items():
            assert reconstructed_rank(updated, d) == q[s] - next_state[()][s]
            counts["insertion_rank_checks"] += 1
        for x in enlarged:
            contracted = contract_table(updated, x)
            counts["contraction_tables"] += 1
            for i in range(3):
                for d in combinations((y for y in enlarged if y != x), i):
                    rank = next_state[tuple(sorted(d + (x,)))][s] - next_state[x,][s]
                    assert reconstructed_rank(contracted, d) == rank
                    counts["contraction_rank_checks"] += 1


def run():
    counts = Counter()
    for width, limit in ((2, 5), (3, 4)):
        parts = tuple(1 << i for i in range(width))
        for capacity in product(range(3), repeat=width):
            for n in range(limit + 1):
                for masks in combinations_with_replacement(range(1 << width), n):
                    verify(capacity, masks, parts, tuple(range(n)), counts)
    seed = 4926112704
    random = Random(seed)
    sampled = Counter()
    for _ in range(500):
        width = random.randint(4, 6)
        capacity = tuple(random.randrange(3) for i in range(width))
        groups = Counter()
        for i in range(width):
            groups[random.randrange(width)] |= 1 << i
        parts = tuple(groups.values())
        if len(parts) < 2:
            continue
        n = random.randrange(10)
        masks = tuple(random.randrange(1 << width) for x in range(n))
        pool = tuple(x for x in range(n) if random.randrange(4))
        verify(capacity, masks, parts, pool, sampled)

    sharp = Counter()
    for k in range(2, 9):
        for d in range(1, k):
            t = d + 1
            capacity = (1,) * k
            parts = tuple(1 << i for i in range(k))
            masks = ((1 << t) - 1,) * (t + 2)
            values = verify(capacity, masks, parts, tuple(range(t + 2)), sharp)
            assert set(values.values()) == {d}
    same_pairs = ((3, 3, 3, 3), (1, 3, 3, 3))
    for n in range(3):
        for d in combinations(range(4), n):
            states = [phi((1, 1), [m for i, m in enumerate(masks) if i not in d]) for masks in same_pairs]
            assert states[0] == states[1]
    assert [trace_gap(phi((1, 1), masks[:1]), (1, 2)) for masks in same_pairs] == [1, 0]
    update_seed = 4926112705
    random = Random(update_seed)
    updates = Counter()
    for _ in range(160):
        width = random.randint(1,6)
        capacity = tuple(random.randrange(4) for _ in range(width))
        masks = tuple(random.randrange(1<<width) for _ in range(random.randrange(8)))
        verify_updates(capacity, masks, random.randrange(1<<width), updates)
    return {"exhaustive": counts, "seed": seed, "sampled": sampled, "sharp_examples": sharp,
            "updates": updates, "update_seed": update_seed,
            "same_h2_different_named_triple": same_pairs}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
