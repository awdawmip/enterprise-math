from collections import Counter
from functools import cache
from itertools import combinations
import json
from math import comb
from pathlib import Path
from random import Random


def bits(mask):
    while mask:
        bit = mask & -mask
        yield bit
        mask ^= bit


def submasks(mask):
    yield 0
    submask = mask
    while submask:
        yield submask
        submask = (submask - 1) & mask


def from_masks(values, selected):
    return sum(1 << i for i, value in enumerate(values) if selected(value))


def cut_table(caps, edges):
    p = (1 << len(caps)) - 1
    cap = {w: sum(caps[b.bit_length() - 1] for b in bits(w)) for w in submasks(p)}
    costs = [(w, from_masks(edges, lambda e: e & w != e)) for w in cap]
    rank = min(cap[w] + crossing.bit_count() for w, crossing in costs)
    return rank, cap, [(w, crossing, cap[w] + crossing.bit_count() - rank) for w, crossing in costs]


def largest_cut(rows, deleted=0):
    best = 0
    largest = 0
    for w, crossing, slack in rows:
        cost = slack - (deleted & crossing).bit_count()
        if cost < best:
            best = cost
            largest = w
        elif cost == best:
            largest |= w
    return largest


def slot_rank(caps, edges):
    slot_ports = [1 << p for p, c in enumerate(caps) for _ in range(c)]
    eligibility = [from_masks(slot_ports, lambda p: bool(p & e)) for e in edges]
    all_labels = (1 << len(edges)) - 1

    @cache
    def rank(deleted, removed_ports=0):
        slots = from_masks(slot_ports, lambda p: not p & removed_ports)
        matched = [-1] * len(slot_ports)

        def augment(label):
            nonlocal seen
            for s in bits(eligibility[label] & slots & ~seen):
                if s & seen:
                    continue
                seen |= s
                pos = s.bit_length() - 1
                if matched[pos] < 0 or augment(matched[pos]):
                    matched[pos] = label
                    return True
            return False

        size = 0
        for label in bits(all_labels & ~deleted):
            seen = 0
            size += augment(label.bit_length() - 1)
        return size

    return rank


def independent_partition(rows, ports):
    values = {
        s: min(slack for w, _, slack in rows if s & w == s)
        for s in submasks(ports)
    }

    def refine(w):
        for left in submasks(w):
            if left and left != w and values[left] + values[w ^ left] == values[w]:
                return refine(left) + refine(w ^ left)
        return [w]

    partition = sorted(refine(ports))
    assert all(values[w] == sum(values[w & block] for block in partition) for w in values)
    return partition


def bridges(edges, partition, saturated, deleted=0):
    for i, e in enumerate(edges):
        if not deleted & (1 << i) and sum(bool(e & ~saturated & block) for block in partition) > 1:
            yield 1 << i


def defect(rank, partition, deleted):
    full = rank(deleted, 0)
    return sum(rank(deleted, block) for block in partition) - (len(partition) - 1) * full


def hall_circuits(rows, w0, pool, budget):
    merged = {}
    full_rows = Counter()
    kept_rows = Counter()
    full_occurrences = Counter()
    kept_occurrences = Counter()
    for w, crossing, slack in rows:
        size = slack + 1
        if size > budget:
            continue
        available = (crossing & pool).bit_count()
        full_rows[size] += 1
        full_occurrences[size] += comb(available, size)
        if w & ~w0:
            continue
        kept_rows[size] += 1
        kept_occurrences[size] += comb(available, size)
        for choice in combinations(bits(crossing & pool), size):
            deleted = sum(choice)
            merged[deleted] = merged.get(deleted, 0) | w

    circuits = {}
    for deleted in sorted(merged, key=int.bit_count):
        if all(deleted & smaller != smaller for smaller in circuits):
            circuits[deleted] = merged[deleted]
    return circuits, {
        "full_low_slack_cuts": sum(full_rows.values()),
        "kept_low_slack_cuts": sum(kept_rows.values()),
        "full_candidate_occurrences": sum(full_occurrences.values()),
        "kept_candidate_occurrences": sum(kept_occurrences.values()),
        "kept_distinct_candidates": len(merged),
    }


def matching_circuits(rank, pool, budget):
    initial_rank = rank(0, 0)
    queries = set()
    circuits = set()

    def unchanged(deleted):
        queries.add(deleted)
        return rank(deleted, 0) == initial_rank

    def search(prefix, remainder):
        for choice in bits(remainder):
            remainder ^= choice
            deleted = prefix | choice
            if unchanged(deleted):
                if deleted.bit_count() < budget:
                    search(deleted, remainder)
            elif all(unchanged(deleted ^ b) for b in bits(deleted)):
                circuits.add(deleted)

    search(0, pool)
    return circuits, len(queries - {0})


def strict_hall_minimum(caps, edges, partition, cap, rank, w0, pool):
    ports = (1 << len(caps)) - 1
    all_labels = (1 << len(edges)) - 1
    best = None
    stats = Counter()
    for v in submasks(w0):
        stats["cuts_examined"] += 1
        possible_bridges = list(bridges(edges, partition, v))
        if not possible_bridges:
            continue
        outside = ports ^ v
        external = from_masks(edges, lambda e: bool(e & outside))
        stats["internal_matching_queries"] += 1
        if rank(external, outside) != cap[v]:
            continue
        constraints = [
            (external & from_masks(edges, lambda e: e & outside & ~u == 0), cap[u] - 1)
            for u in submasks(outside) if u
        ]

        def independent(labels):
            stats["strict_hall_queries"] += 1
            return all((labels & eligible).bit_count() <= threshold for eligible, threshold in constraints)

        required = external & (all_labels ^ pool)
        if not independent(required):
            continue
        if not any(required & b for b in possible_bridges):
            bridge = next((b for b in possible_bridges if independent(required | b)), 0)
            if not bridge:
                continue
            required |= bridge
        stats["feasible_cuts"] += 1
        retained = required
        for b in bits(external & ~required):
            if independent(retained | b):
                retained |= b
        deleted = external ^ retained
        candidate = deleted.bit_count(), deleted, v
        if best is None or candidate < best:
            best = candidate
    return best, stats


def unlimited(rows, edges, partition, pool):
    saturated = largest_cut(rows, pool)
    possible_bridges = list(bridges(edges, partition, saturated))
    if not possible_bridges:
        return None
    if any(not pool & b for b in possible_bridges):
        return pool
    return pool ^ possible_bridges[0]


def label_list(labels, selection):
    return [labels[b.bit_length() - 1] for b in bits(selection)]


def benchmark(caps, labels, edges, archive_rank):
    base, cap, rows = cut_table(caps, edges)
    assert archive_rank == base
    rank = slot_rank(caps, edges)
    assert rank(0, 0) == base
    partition = independent_partition(rows, (1 << len(caps)) - 1)
    w0 = largest_cut(rows)
    pool = (1 << len(edges)) - 1
    greedy, greedy_stats = strict_hall_minimum(caps, edges, partition, cap, rank, w0, pool)
    horizon = greedy[0]
    stages = {}
    for budget in sorted({1, horizon, 5}):
        hc, stats = hall_circuits(rows, w0, pool, budget)
        mc, queries = matching_circuits(rank, pool, budget)
        assert hc.keys() == mc
        first = Counter()
        for d, w in hc.items():
            assert w == largest_cut(rows, d)
            gap = defect(rank, partition, d)
            assert bool(gap) == any(bridges(edges, partition, w, d))
            if gap:
                first[(d.bit_count(), gap)] += 1
        stats.update({"matching_deletion_queries": queries, "global_circuits": len(hc),
                      "failing_circuits_by_size_and_gap": {f"{h},{d}": count for (h, d), count in sorted(first.items())}})
        stages[str(budget)] = stats
        assert min((h for h, _ in first), default=None) == (horizon if budget >= horizon else None)

    _, deleted, winning_cut = greedy
    assert winning_cut == largest_cut(rows, deleted)
    assert defect(rank, partition, deleted) > 0
    assert all(defect(rank, partition, d) == 0 for d in submasks(deleted) if d != deleted)
    assert defect(rank, partition, unlimited(rows, edges, partition, pool)) > 0
    return {"ports": len(caps), "labels": len(edges), "initial_rank": base,
            "partition_bitmasks": partition, "initial_largest_cut": w0,
            "horizons": stages, "minimum": horizon, "minimum_witness_original_labels": label_list(labels, deleted),
            "minimum_witness_largest_cut": winning_cut, "minimum_witness_gap": defect(rank, partition, deleted),
            "strict_hall_cut_solver": greedy_stats}


def check_seeded_cases():
    rng = Random(4926112711)
    summary = Counter()
    for _ in range(240):
        p = rng.randrange(2, 6)
        ports = (1 << p) - 1
        caps = tuple(rng.randrange(3) for _ in range(p))
        edges = tuple(rng.randrange(1 << p) for _ in range(rng.randrange(7)))
        full = (1 << len(edges)) - 1
        base, cap, rows = cut_table(caps, edges)
        rank = slot_rank(caps, edges)
        assert rank(0, 0) == base
        partition = independent_partition(rows, ports)
        w0 = largest_cut(rows)
        failures = []
        for d in submasks(full):
            w = largest_cut(rows, d)
            assert w & ~w0 == 0
            gap = defect(rank, partition, d)
            assert bool(gap) == any(bridges(edges, partition, w, d))
            if gap:
                failures.append(d)
            summary["deletion_states"] += 1
        summary["instances"] += 1
        for pool in submasks(full):
            expect = min((d.bit_count() for d in failures if not d & ~pool), default=None)
            result, _ = strict_hall_minimum(caps, edges, partition, cap, rank, w0, pool)
            witness = unlimited(rows, edges, partition, pool)
            assert (None if result is None else result[0]) == expect
            assert (witness is not None) == (expect is not None)
            if result:
                _, d, v = result
                assert d & ~pool == 0 and d in failures and v == largest_cut(rows, d)
                assert witness & ~pool == 0 and witness in failures
            summary["deletion_pools"] += 1
            summary["pools_allowing_coupling"] += expect is not None
    return summary


def main():
    source = json.loads(Path(__file__).with_name("frozen_cases.json").read_bytes())
    records = {}
    for index, record in source["first_witness"].items():
        labels = sorted(map(int, record["opts"]))
        masks = tuple(record["opts"][str(x)] for x in labels)
        records[index] = benchmark(record["caps"], labels, masks, record["H"])
    print(json.dumps({"frozen_records_all_labels_allowed": records, "seeded_pool_checks": check_seeded_cases()},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
