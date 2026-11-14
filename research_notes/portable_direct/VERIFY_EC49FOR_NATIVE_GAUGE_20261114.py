#!/usr/bin/env python3
"""Independent exact byte-trie verifier for the original-corpus gauge pairs.

Usage: python3 VERIFY_EC49FOR_NATIVE_GAUGE.py /path/to/master_and_radius3_cases.txt
"""
import hashlib
import itertools
import sys
from pathlib import Path

SOURCE_HASH = 'cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
ROOTS = (3, 5, 6, 7)
WITNESSES = (
    (14361, 15331, (0, 2, -2, 0)),
    (17928, 38165, (0, -4, 4, 0)),
    (24541, 38166, (0, -2, 2, 0)),
)


class Node:
    def __init__(self):
        self.next = {}
        self.mask = 0


def rooted_table(case, words, root):
    items = [(label, code[1:]) for key in case for label, code in words[key]
             if code[0] == root]
    labels = sorted({label for label, _ in items})
    bits = {label: 1 << index for index, label in enumerate(labels)}
    head = Node()
    for label, suffix in items:
        node = head
        for char in suffix:
            node = node.next.setdefault(char, Node())
        node.mask |= bits[label]

    def visit(node):
        states = {0: 0}
        if node.mask:
            states[node.mask] = 0
        for _, child in sorted(node.next.items()):
            other = visit(child)
            combined = {}
            for left, left_cost in states.items():
                for right, right_cost in other.items():
                    mask = left | right
                    cost = left_cost + right_cost
                    if cost < combined.get(mask, 10**9):
                        combined[mask] = cost
            states = combined
        return {mask: value + (mask != 0) for mask, value in states.items()}

    states = visit(head)
    costs = [10**9] * (1 << len(labels))
    for mask, value in states.items():
        costs[mask] = value
    for bit in range(len(labels)):
        for mask in range(len(costs)):
            if not (mask & (1 << bit)):
                costs[mask] = min(costs[mask], costs[mask | (1 << bit)])
    return labels, costs


def profile(case, words):
    tables = {r: rooted_table(case, words, r) for r in ROOTS}
    legal = {label: tuple(r for r in ROOTS if label in tables[r][0])
             for label in range(24)}
    assert all(legal.values())
    options = {label: legal[label] for label in range(24) if len(legal[label]) > 1}
    profiles = {}
    for root, (labels, costs) in tables.items():
        index = {label: j for j, label in enumerate(labels)}
        must = [label for label in labels if len(legal[label]) == 1]
        optional = [label for label in labels if len(legal[label]) > 1]
        for choice in itertools.product((0, 1), repeat=len(optional)):
            chosen = must + [label for label, yes in zip(optional, choice) if yes]
            local_mask = sum(1 << index[label] for label in chosen)
            named_optional_mask = sum(1 << label for label, yes in zip(optional, choice) if yes)
            profiles[root, named_optional_mask] = costs[local_mask]
    return profiles, options


def main(filename):
    raw = Path(filename).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SOURCE_HASH, 'wrong original input'
    with Path(filename).open() as f:
        nk, nw, nc = map(int, f.readline().split())
        assert (nk, nw, nc) == (94, 178850, 38169)
        words = []
        for key in range(nk):
            n = int(f.readline())
            family = []
            for _ in range(n):
                label, code = f.readline().split()
                family.append((int(label), bytes.fromhex(code)))
            words.append(family)
        cases = [tuple(map(int, f.readline().split())) for _ in range(nc)]
    for a, b, expected_delta in WITNESSES:
        P, opt_a = profile(cases[a], words)
        Q, opt_b = profile(cases[b], words)
        assert opt_a == opt_b and set(P) == set(Q)
        for root, expected in zip(ROOTS, expected_delta):
            assert all(Q[root, subset] - value == expected
                       for (r, subset), value in P.items() if r == root)
        optional = sorted(opt_a)
        choices = [opt_a[label] for label in optional]
        checks = 0
        for assignment in itertools.product(*choices):
            selected = {r: 0 for r in ROOTS}
            for label, root in zip(optional, assignment):
                selected[root] |= 1 << label
            assert sum(P[r, selected[r]] for r in ROOTS) == sum(Q[r, selected[r]] for r in ROOTS)
            checks += 1
        assert checks == 144
        print('PASS', a, b, 'root delta', expected_delta, 'assignments', checks)
    print('PASS all six original configurations, 3 nonzero gauges')


if __name__ == '__main__':
    assert len(sys.argv) == 2, 'pass original frozen master_and_radius3_cases.txt'
    main(sys.argv[1])
