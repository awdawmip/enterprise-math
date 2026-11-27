from collections import Counter
from functools import cache
from itertools import combinations_with_replacement, product
import json
from random import Random


def bits(mask):
    while mask:
        bit = mask & -mask
        yield bit
        mask ^= bit


def hall_rows(capacity, masks):
    port_sets = range(1 << len(capacity))
    cut_capacity = [
        sum(c for p, c in enumerate(capacity) if cut & (1 << p))
        for cut in port_sets
    ]
    cut_labels = [
        sum(1 << x for x, mask in enumerate(masks) if mask & cut == mask)
        for cut in port_sets
    ]
    supersets = [[cut for cut in port_sets if cut & query == query] for query in port_sets]
    full = (1 << len(masks)) - 1
    rows = []
    for deleted in range(full + 1):
        live = full ^ deleted
        cost = [c - (live & labels).bit_count() for c, labels in zip(cut_capacity, cut_labels)]
        rows.append([min(cost[cut] for cut in cuts) for cuts in supersets])

    crossing_by_size = [[] for _ in range(len(masks) + 1)]
    for cap, contained in zip(cut_capacity, cut_labels):
        threshold = cap - contained.bit_count() - rows[0][0] + 1
        crosses = full ^ contained
        if threshold <= crosses.bit_count():
            crossing_by_size[threshold].append(crosses)
    circuits = [False] * len(rows)
    contains_candidate = [False] * len(rows)
    for deleted in range(1, len(rows)):
        size = deleted.bit_count()
        candidate = any(deleted & crosses == deleted for crosses in crossing_by_size[size])
        proper_candidate = any(contains_candidate[deleted ^ bit] for bit in bits(deleted))
        circuits[deleted] = candidate and not proper_candidate
        contains_candidate[deleted] = candidate or proper_candidate
    return rows, circuits


def matching_dual_ranks(capacity, masks):
    slot_ports = [1 << p for p, c in enumerate(capacity) for _ in range(c)]
    eligible_slots = [
        sum(1 << s for s, port in enumerate(slot_ports) if port & mask)
        for mask in masks
    ]
    full = (1 << len(masks)) - 1

    @cache
    def matching_rank(labels, slots):
        if not labels or not slots:
            return 0
        chosen = labels & -labels
        eligible = slots & eligible_slots[chosen.bit_length() - 1]
        labels ^= chosen
        rank = matching_rank(labels, slots)
        for slot in bits(eligible):
            rank = max(rank, 1 + matching_rank(labels, slots ^ slot))
        return rank

    @cache
    def dual_row(removed_ports):
        slots = sum(1 << s for s, port in enumerate(slot_ports) if not port & removed_ports)
        base = matching_rank(full, slots)
        return [
            deleted.bit_count() - base + matching_rank(full ^ deleted, slots)
            for deleted in range(full + 1)
        ]

    return dual_row


def all_query_gaps(phi, partition):
    return [
        sum(phi[query & block] - phi[0] for block in partition) - phi[query] + phi[0]
        for query in range(len(phi))
    ]


def verify_instance(capacity, masks, partitions, counts):
    hall, hall_circuits = hall_rows(capacity, masks)
    rank_row = matching_dual_ranks(capacity, masks)
    counts["instances"] += 1
    for partition in partitions:
        counts["partitions"] += 1
        if any(all_query_gaps(hall[0], partition)):
            continue
        counts["initially_additive_partitions"] += 1
        global_rank = rank_row(0)
        block_ranks = [rank_row(block) for block in partition]
        has_failing_subset = [False] * len(hall)
        minimal = {}
        for deleted, phi in enumerate(hall[1:], start=1):
            size = deleted.bit_count()
            predecessors = [deleted ^ bit for bit in bits(deleted)]
            query_gaps = all_query_gaps(phi, partition)
            gap = query_gaps[-1]
            counts["named_deletions"] += 1
            assert all(0 <= value <= gap for value in query_gaps)
            formula = sum(row[deleted] for row in block_ranks) - size
            formula -= (len(partition) - 1) * global_rank[deleted]
            assert gap == formula, (capacity, masks, partition, deleted)
            for predecessor in predecessors:
                global_increment = global_rank[deleted] - global_rank[predecessor]
                assert all(row[deleted] - row[predecessor] >= global_increment for row in block_ranks)

            proper_failure = any(has_failing_subset[pred] for pred in predecessors)
            has_failing_subset[deleted] = gap > 0 or proper_failure
            first_failure = gap > 0 and not proper_failure
            circuit = global_rank[deleted] == size - 1 and all(
                global_rank[pred] == size - 1 for pred in predecessors
            )
            assert circuit == hall_circuits[deleted], (capacity, masks, deleted)
            lifts = sum(row[deleted] == size for row in block_ranks)
            assert first_failure == (circuit and lifts >= 2), (capacity, masks, partition, deleted)
            counts["positive_defects"] += gap > 0
            counts["safe_sets_containing_failures"] += gap == 0 and proper_failure
            if first_failure:
                assert gap == lifts - 1
                assert len(masks) >= size + gap
                counts[f"minimal_failures_size_{size}"] += 1
                minimal[deleted] = gap
        yield partition, minimal


def run_cases(cases, counts):
    for capacity, masks, partitions in cases:
        for _ in verify_instance(capacity, masks, partitions, counts):
            pass


def exhaustive_two_ports():
    for capacity in product(range(3), repeat=2):
        for n in range(7):
            for masks in combinations_with_replacement(range(4), n):
                yield capacity, masks, [(1, 2)]


def sampled_ports():
    rng = Random(4926112710)
    for p in range(3, 6):
        singleton = tuple(1 << i for i in range(p))
        for _ in range(100):
            capacity = tuple(rng.randrange(3) for _ in range(p))
            masks = tuple(rng.randrange(1 << p) for _ in range(rng.randrange(2, 8)))
            contiguous = (3, ((1 << p) - 1) ^ 3)
            mixed = (5, ((1 << p) - 1) ^ 5)
            yield capacity, masks, [singleton, contiguous, mixed]


def verify_sharp_family(counts):
    for k in range(2, 7):
        partition = tuple(1 << p for p in range(k))
        for h in range(1, 6):
            for d in range(1, k):
                allowed = (1 << (d + 1)) - 1
                placement = tuple(allowed for _ in range(h + d))
                checks = list(verify_instance((1,) * k, placement, [partition], counts))
                assert len(checks) == 1
                minimal = checks[0][1]
                expected = {
                    deleted: d for deleted in range(1 << len(placement))
                    if deleted.bit_count() == h
                }
                assert minimal == expected


def main():
    exhaustive = Counter()
    sampled = Counter()
    sharp = Counter()
    run_cases(exhaustive_two_ports(), exhaustive)
    run_cases(sampled_ports(), sampled)
    verify_sharp_family(sharp)
    stats = {"exhaustive_two_ports": exhaustive, "sampled_three_to_five_ports": sampled,
             "sharp_family": sharp}
    print(json.dumps(stats, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
