#!/usr/bin/env python3
"""R185 exact integer-only checks: cardinality-promise source-oracle recovery.

The universe is ordered distinct source labels; no spatial coordinate is
collapsed. This is a scope-typed observer test, not a native BRC execution.
"""
from __future__ import annotations

from functools import lru_cache
from itertools import permutations, product
from json import dumps
from math import factorial
from pathlib import Path


def q(state: tuple[int, ...], mask: int) -> int:
    for x in reversed(state):
        if (mask >> x) & 1:
            return x
    return -1


def recover(k: int, r: int, state: tuple[int, ...], known_support: bool = False) -> tuple[tuple[int, ...], int]:
    support = set(state) if known_support else set(range(k))
    remaining = set(support)
    out_recent: list[int] = []
    calls = 0
    if r == 0:
        return (), 0
    budget = r - 1 if (known_support or r == k) else r
    for _ in range(budget):
        mask = sum(1 << x for x in remaining)
        got = q(state, mask)
        assert got in remaining, (k, r, state, got)
        out_recent.append(got)
        remaining.remove(got)
        calls += 1
    if known_support or r == k:
        assert len(remaining) == 1
        out_recent.append(next(iter(remaining)))
    else:
        assert not remaining.intersection(out_recent)
    return tuple(reversed(out_recent)), calls


def minimax(k: int, r: int) -> tuple[int, int]:
    states = tuple(permutations(range(k), r))
    full = (1 << len(states)) - 1
    partitions = []
    for mask in range(1, 1 << k):
        parts: dict[int, int] = {}
        for j, s in enumerate(states):
            ans = q(s, mask)
            parts[ans] = parts.get(ans, 0) | (1 << j)
        partitions.append(tuple(parts.values()))

    @lru_cache(None)
    def solve(belief: int) -> int:
        if belief.bit_count() == 1:
            return 0
        best = k + 1
        for classes in partitions:
            pieces = [p & belief for p in classes if p & belief]
            if len(pieces) < 2:
                continue
            depth = 1
            for piece in pieces:
                depth = max(depth, 1 + solve(piece))
                if depth >= best:
                    break
            best = min(best, depth)
        return best

    return solve(full), solve.cache_info().currsize


def adversary_transcript(k: int, masks: tuple[int, ...]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Produce canonical responses and the returned labels, newest first."""
    returned: list[int] = []  # first discovered = newest
    answers: list[int] = []
    for mask in masks:
        seen = next((x for x in returned if mask & (1 << x)), None)
        if seen is None:
            seen = next(x for x in range(k) if mask & (1 << x) and x not in returned)
            returned.append(seen)
        answers.append(seen)
    return tuple(answers), tuple(returned)


def adversary_witnesses(k: int, r: int, masks: tuple[int, ...]):
    ans, returned = adversary_transcript(k, masks)
    unseen = [x for x in range(k) if x not in returned]
    needed = r - len(returned)
    assert needed >= 1
    if r == k:
        assert len(unseen) >= 2
        old1 = list(unseen)
        old2 = list(unseen)
        old2[0], old2[1] = old2[1], old2[0]
    else:
        assert len(unseen) > needed
        old1 = list(unseen[:needed])
        old2 = list(unseen[:needed - 1]) + [unseen[needed]]
    s1 = tuple(old1 + list(reversed(returned)))
    s2 = tuple(old2 + list(reversed(returned)))
    assert s1 != s2 and len(s1) == len(s2) == r
    assert tuple(q(s1, m) for m in masks) == ans
    assert tuple(q(s2, m) for m in masks) == ans
    return s1, s2


def run() -> dict:
    summary = {
        'schema': 'R185_EXACT_SOURCE_ORACLE_PROMISE_CHECK_V1',
        'test_status': 'PASS',
        'arithmetic': 'exact integers and finite combinatorial enumeration; no floats',
        'frozen_science_pin': '43ec6098b1330ae86d0a7863be336c5d97f6ef34',
        'scope': 'whole-atom source latest-occurrence selectors q_U only; X6 branch/path/provenance not collapsed',
        'recovery_max_k': 7,
        'recovery_cases': 0,
        'known_support_recovery_cases': 0,
        'known_support_pair_distinguish_pairs': 0,
        'minimax_classes': [],
        'adversarial_all_query_prefixes': 0,
        'adversary_max_k': 5,
        'expected_formula': 'r=0:0; 1<=r<k:r; r=k:k-1; fixed known support S:r-1',
    }
    for k in range(1, 8):
        for r in range(k + 1):
            expected = 0 if r == 0 else r - 1 if r == k else r
            for s in permutations(range(k), r):
                got, calls = recover(k, r, s)
                assert got == s and calls == expected, (k, r, s, got, calls)
                summary['recovery_cases'] += 1
                got2, calls2 = recover(k, r, s, known_support=True)
                assert got2 == s and calls2 == max(0, r - 1)
                summary['known_support_recovery_cases'] += 1

            if k <= 4:
                depth, nodes = minimax(k, r)
                assert depth == expected, (k, r, depth, expected)
                summary['minimax_classes'].append({'k': k, 'r': r, 'states': factorial(k)//factorial(k-r), 'optimal_calls': depth, 'memoized_beliefs': nodes})

            if k <= 5 and r > 0:
                lower = expected
                for depth in range(lower):
                    for masks in product(range(1, 1 << k), repeat=depth):
                        adversary_witnesses(k, r, masks)
                        summary['adversarial_all_query_prefixes'] += 1

    # Fixed known-support catalog: all pair queries suffice and each is necessary.
    for k in range(2, 7):
        all_perms = list(permutations(range(k)))
        pair_masks = [((1 << i) | (1 << j)) for i in range(k) for j in range(i+1, k)]
        signatures = [tuple(q(s, mask) for mask in pair_masks) for s in all_perms]
        assert len(set(signatures)) == len(all_perms)
        for p in pair_masks:
            old = tuple(x for x in range(k) if not (p & (1 << x)))
            ij = tuple(x for x in range(k) if p & (1 << x))
            a = ij + old
            b = tuple(reversed(ij)) + old
            assert a != b
            for mask in range(1, 1 << k):
                if mask != p:
                    assert q(a, mask) == q(b, mask), (k, p, mask)
            assert q(a, p) != q(b, p)
            summary['known_support_pair_distinguish_pairs'] += 1
    return summary


if __name__ == '__main__':
    result = run()
    dest = Path(__file__).with_name('R185_verification.json')
    dest.write_text(dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(dumps(result, ensure_ascii=False, sort_keys=True))
