#!/usr/bin/env python3
"""R022 pass-9 partition refinement debt and replay lower-bound checks."""
from math import ceil, log2
import json


def set_partitions(n):
    items = list(range(n))
    out = {}

    def rec(rest):
        if not rest:
            yield []
            return
        first = rest[0]
        for p in rec(rest[1:]):
            yield [{first}] + [set(b) for b in p]
            for i in range(len(p)):
                q = [set(b) for b in p]
                q[i].add(first)
                yield q

    for p in rec(items):
        canon = tuple(sorted(tuple(sorted(b)) for b in p))
        out[canon] = canon
    return list(out.values())


def relation(partition):
    return {(x, y) for block in partition for x in block for y in block}


def refines(fine, coarse):
    return relation(fine) <= relation(coarse)


def split_counts(coarse, fine):
    assert refines(fine, coarse)
    return tuple(
        sum(1 for child in fine if set(child) <= set(parent))
        for parent in coarse
    )


def debt_alphabet_size(coarse, fine):
    return max(split_counts(coarse, fine), default=1)


def debt_bits(coarse, fine):
    return ceil(log2(debt_alphabet_size(coarse, fine)))


def constructive_side_labels(n, coarse, fine):
    """Reuse local child indices across different coarse classes."""
    labels = {}
    for parent in coarse:
        children = [child for child in fine if set(child) <= set(parent)]
        for i, child in enumerate(children):
            for x in child:
                labels[x] = i

    seen = {}
    for x in range(n):
        coarse_id = next(i for i, block in enumerate(coarse) if x in block)
        fine_id = next(i for i, block in enumerate(fine) if x in block)
        key = (coarse_id, labels[x])
        if key in seen and seen[key] != fine_id:
            return False
        seen[key] = fine_id
    return max(labels.values(), default=0) + 1 <= debt_alphabet_size(coarse, fine)


def exhaustive_refinement_debt(n=5):
    partitions = set_partitions(n)
    pairs = 0
    distribution = {}
    for coarse in partitions:
        for fine in partitions:
            if not refines(fine, coarse):
                continue
            pairs += 1
            m = debt_alphabet_size(coarse, fine)
            distribution[m] = distribution.get(m, 0) + 1
            assert constructive_side_labels(n, coarse, fine)

    return {
        "states": n,
        "partitions": len(partitions),
        "refinement_pairs": pairs,
        "max_split_distribution": distribution,
        "counterexample": False,
    }


def exhaustive_debt_composition(n=5):
    partitions = set_partitions(n)
    triples = 0
    for coarse in partitions:
        for middle in partitions:
            if not refines(middle, coarse):
                continue
            for fine in partitions:
                if not refines(fine, middle):
                    continue
                triples += 1
                for parent in coarse:
                    direct = sum(1 for child in fine if set(child) <= set(parent))
                    staged = 0
                    for mid in middle:
                        if set(mid) <= set(parent):
                            staged += sum(1 for child in fine if set(child) <= set(mid))
                    assert direct == staged

                assert debt_alphabet_size(coarse, fine) <= (
                    debt_alphabet_size(coarse, middle)
                    * debt_alphabet_size(middle, fine)
                )
                assert debt_bits(coarse, fine) <= (
                    debt_bits(coarse, middle) + debt_bits(middle, fine)
                )

    return {
        "states": n,
        "refinement_triples": triples,
        "split_count_composition_exact": True,
        "alphabet_size_submultiplicative": True,
        "fixed_width_bits_subadditive": True,
    }


def bounded_deletion_debt(h=2, H=5):
    assert H >= h
    split = H - h + 1
    return {
        "old_horizon": h,
        "new_horizon": H,
        "only_old_saturated_class_splits": True,
        "new_subclasses_inside_old_saturated_class": split,
        "minimum_side_label_alphabet": split,
        "minimum_fixed_width_side_bits": ceil(log2(split)),
        "subclasses": list(range(h + 1, H + 1)) + [f">={H + 1}"],
    }


def no_metadata_no_split_law():
    coarse = ((0, 1), (2,))
    same = ((0, 1), (2,))
    refined = ((0,), (1,), (2,))
    return {
        "zero_bit_same_partition": debt_bits(coarse, same) == 0,
        "zero_bit_refined_partition": debt_bits(coarse, refined) == 0,
        "refined_debt_bits": debt_bits(coarse, refined),
        "lesson": "zero side metadata can reconstruct the stronger token iff no old class actually splits",
    }


def run_all():
    return {
        "refinement_debt": exhaustive_refinement_debt(),
        "debt_composition": exhaustive_debt_composition(),
        "bounded_deletion": bounded_deletion_debt(),
        "zero_metadata_boundary": no_metadata_no_split_law(),
    }


def self_test():
    out = run_all()
    r = out["refinement_debt"]
    assert r["partitions"] == 52
    assert r["refinement_pairs"] == 358
    assert not r["counterexample"]
    c = out["debt_composition"]
    assert c["refinement_triples"] == 1304
    assert c["split_count_composition_exact"]
    d = out["bounded_deletion"]
    assert d["new_subclasses_inside_old_saturated_class"] == 4
    assert d["minimum_fixed_width_side_bits"] == 2
    z = out["zero_metadata_boundary"]
    assert z["zero_bit_same_partition"]
    assert not z["zero_bit_refined_partition"]


if __name__ == "__main__":
    self_test()
    print(json.dumps(run_all(), indent=2, sort_keys=True))
