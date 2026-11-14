#!/usr/bin/env python3
"""EC49FOW class-25 integer certificate verifier.

Usage:
    python VERIFY_EC49FOW_STANDALONE.py frozen_original_master.txt PROFILES_25_COMPLETE.csv

Verifies frozen-corpus census, all 442 class members, exact terminal/root
equivalence, three independent Python native byte-Trie checks, and seven
sufficient terminal observers. Requires only Python standard library.
"""
import collections
import csv
import hashlib
import itertools
import json
import math
import sys
from pathlib import Path

ROOTS = (3, 5, 6, 7)
EXPECTED_SHA = "cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"
SEVEN = (390, 477, 547, 107, 137, 110, 182)


def source(path):
    assert hashlib.sha256(path.read_bytes()).hexdigest() == EXPECTED_SHA
    with path.open() as f:
        nk, nw, nc = map(int, f.readline().split())
        assert (nk, nw, nc) == (94, 178850, 38169)
        masks, words, count = [], [], 0
        for k in range(nk):
            num = int(f.readline())
            count += num
            m = {r: 0 for r in ROOTS}
            w = []
            for _ in range(num):
                label, sequence = f.readline().split()
                label, code = int(label), bytes.fromhex(sequence)
                assert label in range(24) and code[0] in ROOTS
                m[code[0]] |= 1 << label
                w.append((label, code))
            masks.append(m)
            words.append(w)
        assert count == nw
        cases = [tuple(map(int, f.readline().split())) for _ in range(nc)]
        assert all(len(c) == 7 and all(0 <= i < nk for i in c) for c in cases)
        return masks, words, cases


def legal(case, masks):
    domain = [0] * 24
    for k in case:
        for j, root in enumerate(ROOTS):
            bits = masks[k][root]
            while bits:
                bit = bits & -bits
                domain[bit.bit_length() - 1] |= 1 << j
                bits -= bit
    assert all(domain)
    return tuple(domain)


def independent_root(case, words, root, domain):
    paths = [(label, code[1:]) for k in case for label, code in words[k] if code[0] == root]
    labels = sorted({label for label, _ in paths})
    position = {label: i for i, label in enumerate(labels)}
    head = {"edges": {}, "labels": 0}
    for label, path in paths:
        node = head
        for byte in path:
            node = node["edges"].setdefault(byte, {"edges": {}, "labels": 0})
        node["labels"] |= 1 << position[label]

    def visit(node):
        table = {0: 0}
        if node["labels"]:
            table[node["labels"]] = 0
        for child in node["edges"].values():
            other, nxt = visit(child), {}
            for a, ca in table.items():
                for b, cb in other.items():
                    key = a | b
                    nxt[key] = min(nxt.get(key, 10**10), ca + cb)
            table = nxt
        return {mask: cost + (mask != 0) for mask, cost in table.items()}

    exact = visit(head)
    costs = [10**10] * (1 << len(labels))
    for mask, value in exact.items():
        costs[mask] = value
    for bit in range(len(labels)):
        for mask in range(len(costs)):
            if not ((mask >> bit) & 1):
                costs[mask] = min(costs[mask], costs[mask | (1 << bit)])
    mandatory = [label for label in labels if domain[label].bit_count() == 1]
    optional = [label for label in labels if domain[label].bit_count() > 1]
    answer = {}
    for choices in itertools.product((0, 1), repeat=len(optional)):
        selected = mandatory + [label for label, yes in zip(optional, choices) if yes]
        subset = sum(1 << label for label, yes in zip(optional, choices) if yes)
        answer[subset] = costs[sum(1 << position[label] for label in selected)]
    return answer


def check(input_path, csv_path):
    masks, words, cases = source(input_path)
    classes = collections.defaultdict(list)
    for index, case in enumerate(cases):
        classes[legal(case, masks)].append(index)
    assert len(classes) == 625
    domain = legal(cases[25], masks)
    ids = classes[domain]
    assert ids[0] == 25 and len(ids) == 442
    optional = [i for i, mask in enumerate(domain) if mask.bit_count() > 1]
    assert optional == [5, 7, 11, 13, 15, 17, 19, 21]
    options = [tuple(ROOTS[j] for j in range(4) if domain[label] & (1 << j)) for label in optional]
    allocations = list(itertools.product(*options))
    assert len(allocations) == 576

    entries = {}
    with csv_path.open() as f:
        for row in csv.DictReader(f):
            c, root, must, opt, subset, cost = (int(row[k]) for k in
                    ("config", "root", "must", "opt", "subset", "cost"))
            assert c in ids and (c, root, subset) not in entries
            entries[c, root, subset] = (cost, must, opt)
    assert len(entries) == 129064
    terminal, profiles = {}, {}
    for c in ids:
        lookup, profile = {}, []
        for j, root in enumerate(ROOTS):
            allowed = [label for label in optional if domain[label] & (1 << j)]
            must = sum(1 << label for label in range(24) if domain[label] == 1 << j)
            opt = sum(1 << label for label in allowed)
            for choice in itertools.product((0, 1), repeat=len(allowed)):
                subset = sum(1 << label for label, yes in zip(allowed, choice) if yes)
                cost, m, o = entries[c, root, subset]
                assert (m, o) == (must, opt) and 0 <= cost < 10**9
                lookup[root, subset] = cost
                profile.append(cost)
        assert len(profile) == 292
        profiles[c] = tuple(profile)
        values = []
        for choices in allocations:
            subsets = {root: 0 for root in ROOTS}
            for label, root in zip(optional, choices):
                subsets[root] |= 1 << label
            values.append(sum(lookup[root, subsets[root]] for root in ROOTS))
        terminal[c] = tuple(values)

    by_profile, by_terminal = collections.defaultdict(list), collections.defaultdict(list)
    for c in ids:
        by_profile[profiles[c]].append(c)
        by_terminal[terminal[c]].append(c)
    equal_pairs = lambda groups: sum(math.comb(len(g), 2) for g in groups.values())
    assert len(by_profile) == len(by_terminal) == 344
    assert equal_pairs(by_profile) == equal_pairs(by_terminal) == 98
    for group in by_terminal.values():
        assert len({profiles[c] for c in group}) == 1
    for c in (25, 27676, 33162):
        for root in ROOTS:
            check = independent_root(cases[c], words, root, domain)
            for subset, value in check.items():
                assert entries[c, root, subset][0] == value, (c, root, subset)
        assert sum(len(independent_root(cases[c], words, r, domain)) for r in ROOTS) == 292

    representatives = [group[0] for group in by_terminal.values()]
    assert len({tuple(terminal[c][index] for index in SEVEN) for c in representatives}) == 344
    collisions = []
    for n in range(1, len(SEVEN) + 1):
        groups = collections.Counter(tuple(terminal[c][index] for index in SEVEN[:n])
                                     for c in representatives)
        collisions.append(sum(math.comb(size, 2) for size in groups.values()))
    assert collisions == [1253, 68, 12, 4, 2, 1, 0]
    return {"configs": len(ids), "terminal_classes": len(by_terminal),
            "root_classes": len(by_profile), "equal_terminal_pairs": equal_pairs(by_terminal),
            "equal_root_pairs": equal_pairs(by_profile), "root_entries": len(entries),
            "terminal_evaluations": len(ids) * len(allocations),
            "seven_indices": list(SEVEN), "seven_remaining_collisions": collisions,
            "independent_root_cost_checks": 3 * 292,
            "status": "AUTHOR_CHECKED_NOT_REVIEWED"}


if __name__ == "__main__":
    assert len(sys.argv) == 3
    print(json.dumps(check(Path(sys.argv[1]), Path(sys.argv[2])), indent=2))
