"""Reproduce the conditional X6 receipt fiber using only Python 3.10+."""
import argparse
import contextlib
import hashlib
import io
import json
from collections import Counter
from itertools import combinations, product
from pathlib import Path


REP = ("+++", "---", "-++", "+--")
C = (1, 2, 4, 8)
G = ((16,), (32,), (64, 128, 256), (512, 1024, 2048))
ALL = (1 << 12) - 1
HOM = (-1, 0, 7)
MIX = tuple(range(-1, 8))
PRIOR_BLOB = "2e35713c52145d5d9cce05753ff94cb49fc7215e"


def atoms(mask):
    while mask:
        first = mask & -mask
        yield first
        mask ^= first


def union(rows):
    mask = 0
    for row in rows:
        mask |= row
    return mask


def up(mask):
    return mask | union(union(roots) for closure, roots in zip(C, G) if mask & closure)


def down(mask):
    return mask | union(closure for closure, roots in zip(C, G) if mask & union(roots))


def encode(policy):
    ideal = 0
    for mask, closure, roots in zip(policy, C, G):
        if mask >= 0:
            ideal |= closure
            for j, root in enumerate(roots):
                if mask & (1 << j):
                    ideal |= root
    return ideal


CODE = {encode(policy): policy for policy in product(HOM, HOM, MIX, MIX)}
assert len(CODE) == 729 and set(CODE) == {i for i in range(ALL + 1) if down(i) == i}


def signature(policy):
    n = [0] * 4
    totals, signed, rooted, successor = [], [], [], []
    for rep, mask, weight in zip(REP, policy, (1, 1, 3, 3)):
        if mask < 0:
            for row in (totals, signed, rooted, successor):
                row.append(None)
            continue
        allowed = [p for p in range(3) if mask & (1 << p)]
        k = len(allowed)
        n[k] += weight
        counts = Counter(rep[p] for p in allowed)
        links = Counter(rep[p] + rep[(p + 1) % 3] for p in allowed)
        total = k * (k + 1)
        totals.append(total)
        signed.append((total, k + sum(v * v for v in counts.values())))
        rooted.append((total, tuple(sorted((s, v * (k + 1)) for s, v in counts.items()))))
        successor.append((total, tuple(sorted((s, v * (k + 1)) for s, v in links.items()))))
    positive = tuple(() if not pair else pair[1] for pair in successor)
    return tuple(n), tuple(totals), tuple(signed), tuple(rooted), tuple(successor), (tuple(n), positive)


def check_prior_source(path):
    raw = Path(path).read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\x00" + raw).hexdigest()
    if blob != PRIOR_BLOB:
        raise ValueError("Expected the frozen Git blob " + PRIOR_BLOB)
    original = {"__name__": "frozen_prior_checker"}
    exec(compile(raw, str(path), "exec"), original)
    with contextlib.redirect_stdout(io.StringIO()):
        original["classify"]()
    for sector, rep in enumerate(original["REPRESENTATIVES"]):
        for mask in HOM if sector < 2 else MIX:
            test = [0] * 4
            test[sector] = mask
            local = signature(test)
            source = original["sector_observation"](rep, mask)
            if mask == -1:
                assert source is None and local[1][sector] is None
                continue
            total, signed, roots, links = source
            signs = {1: "+", -1: "-"}
            root_counts = tuple(sorted((signs[key], v) for key, v in roots))
            link_counts = tuple(sorted((signs[a] + signs[b], v) for (a, b), v in links))
            assert (local[1][sector], local[2][sector], local[3][sector], local[4][sector]) == (
                total, (total, signed), (total, root_counts), (total, link_counts))


def raw_fiber(positive, negative):
    denied = union(negative)
    return {i for i in CODE if not i & denied and all(i & row for row in positive)}


def avoiding(forbidden):
    forbidden = up(forbidden)
    count = 1
    for closure, roots in zip(C, G):
        if not forbidden & closure:
            count *= 1 + (1 << sum(not forbidden & r for r in roots))
    return count


def count_by_exclusion(positive, negative):
    total = 0
    for size in range(len(positive) + 1):
        for selected in combinations(positive, size):
            total += (-1) ** size * avoiding(union(negative) | union(selected))
    return total


def summary(positive, negative):
    fiber = raw_fiber(positive, negative)
    denied = up(union(negative))
    possible = ALL ^ denied
    survivors = [row & possible for row in positive]
    assert bool(fiber) == all(survivors)
    assert len(fiber) == count_by_exclusion(positive, negative)
    if not fiber:
        return fiber, [], None
    assert possible in fiber and union(fiber) == possible
    forced = union(x for x in atoms(ALL) if any(row & ~up(x) == 0 for row in survivors))
    assert all(all(i & x for i in fiber) == bool(forced & x) for x in atoms(ALL))
    candidates = {down(union(selection)) for selection in product(*(atoms(row) for row in survivors))}
    minima = {s for s in candidates if not any(t != s and t & s == t for t in candidates)}
    assert minima == {s for s in fiber if not any(s ^ x in fiber for x in atoms(s))}
    return fiber, sorted(minima), possible


def readout(fiber, minima, maximum, predicate, monotone=False):
    values = sorted({int(predicate(i)) for i in fiber})
    ends = sorted({int(predicate(i)) for i in [*minima, maximum]})
    edges = [(i, i | x) for i in fiber for x in atoms(ALL ^ i) if i | x in fiber]
    changed = sum(predicate(i) != predicate(j) for i, j in edges)
    assert (changed == 0) == (len(values) == 1)
    if monotone:
        assert all(predicate(i) <= predicate(j) for i, j in edges)
        assert (len(values) == 1) == (len(ends) == 1)
    return {"values": values, "extreme_values": ends, "changed_cover_edges": changed}


def example(positive, negative, functions):
    fiber, minima, maximum = summary(positive, negative)
    return {"policies": sorted(CODE[i] for i in fiber), "minima": sorted(CODE[i] for i in minima),
            "maximum": CODE[maximum],
            "readouts": {name: readout(fiber, minima, maximum, f, monotone)
                         for name, (f, monotone) in functions.items()}}


def check_conflict(roots):
    disjunction = union(roots)
    assert not raw_fiber([disjunction], roots)
    witnesses = [len(raw_fiber([], roots))]
    witnesses += [len(raw_fiber([disjunction], [x for x in roots if x != r])) for r in roots]
    assert all(witnesses)
    return {"rows": len(roots) + 1, "survivors_on_omitting_each_row": witnesses}


def context_cover(x, y):
    rows = (([x | y], []), ([], [x]), ([], [y]))
    fibers = [raw_fiber(positive, negative) for positive, negative in rows]
    pooled = set.intersection(*fibers)
    pair_sizes = [len(a & b) for a, b in combinations(fibers, 2)]
    covers = {tuple(i for i, family in enumerate(fibers) if ideal in family) for ideal in CODE}
    for size in range(1, len(fibers) + 1):
        if any(set().union(*choice) == {0, 1, 2} for choice in combinations(covers, size)):
            break
    assert not pooled and pair_sizes == [162, 162, 243] and size == 2
    return {"pooled": len(pooled), "pair_sizes": pair_sizes, "least_background_labels": size}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--prior-checker", help="optionally replay the byte-pinned original observer")
    args = p.parse_args()
    if args.prior_checker:
        check_prior_source(args.prior_checker)
    names = ("returns", "support", "signed_agreement", "root_sign",
             "root_and_successor_sign", "full_positive_sources")
    prior = dict(zip(names, map(len, map(set, zip(*(signature(p) for p in CODE.values()))))))
    assert tuple(prior.values()) == (90, 225, 324, 441, 729, 640)
    w, x, y = G[2]
    z, v, u = G[3]
    has = lambda i, r: bool(i & r)
    common = {"x": (lambda i: has(i, x), True), "y": (lambda i: has(i, y), True)}
    first = example([C[0], x | y], [G[0][0], C[1], C[3], w], {
        **common, "x_or_y": (lambda i: bool(i & (x | y)), True),
        "enabled_majorities": (lambda i: (i & (x | y)).bit_count(), True)})
    second = example([C[2], C[3], x | y, y | z], [C[0], C[1], w, v, u], {
        **common, "z": (lambda i: has(i, z), True),
        "y_or_x_and_z": (lambda i: has(i, y) or (has(i, x) and has(i, z)), True),
        "y_and_x_xor_z": (lambda i: has(i, y) and (has(i, x) != has(i, z)), False)})
    assert [len(first["policies"]), len(second["policies"])] == [3, 5]
    assert first["readouts"]["x_or_y"]["values"] == [1]
    assert second["readouts"]["y_or_x_and_z"]["values"] == [1]
    assert second["readouts"]["y_and_x_xor_z"] == {
        "values": [0, 1], "extreme_values": [0], "changed_cover_edges": 4}
    for r in ("x", "y", "z"):
        assert second["readouts"][r]["values"] == [0, 1]
    left, right = (0, 0, 2, 0), (0, 0, 4, 0)
    assert signature(left)[:4] == signature(right)[:4] and signature(left)[4] != signature(right)[4]
    assert encode(left) & x and not encode(right) & x
    false_joint = sum(any(has(i, j) for j in (x, y)) and any(not has(i, j) for j in (x, y))
                      for i in CODE)
    joined = sum(any(has(i, j) and not has(i, j) for j in (x, y)) for i in CODE)
    assert false_joint == 324 and joined == 0
    masks = [union(atom for atom, chosen in zip((x, y, z), bits) if chosen)
             for bits in product((False, True), repeat=3)]
    families = 0
    for size in (0, 1, 2):
        for positive in combinations(masks[1:], size):
            for deny in masks:
                summary(positive, [deny])
                families += 1
    assert families == 232
    actual, _, _ = summary([], [])
    output = {"prior_checker_git_blob": PRIOR_BLOB, "prior_counts": prior,
              "native_rows_qualified_in_cited_sources": 0, "native_surviving_candidates": len(actual),
              "conditional_example_1": first, "conditional_example_2": second,
              "same_root_witness": {"joined": joined, "unjoined": false_joint},
              "sharp_conflicts": {"one_mixed_sector": check_conflict(G[2]),
                                  "all_sectors": check_conflict(tuple(x for roots in G for x in roots))},
              "old_root_sign_equivalent_distinct_link_example": [left, right],
              "conditional_context_cover": context_cover(x, y),
              "additional_three_coordinate_receipt_families": families}
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
