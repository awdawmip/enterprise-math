#!/usr/bin/env python3
"""R749STW exact five-source symbolic provenance/Port certificate.

This program checks an explicitly typed candidate non-cancelling source-branch
carrier. It does not execute a physical native heartbeat or installed BRC kernel.
"""
from functools import lru_cache
from itertools import product
from collections import defaultdict
from math import factorial, comb, prod
from pathlib import Path
import json

ALPHABET = ("A", "B", "C", "D", "E")
WEIGHTS = (1, 1, 2, 3, 6)

@lru_cache(None)
def count_suffixes(counts, r):
    """Count possible length-r provenance suffixes in an endpoint count fiber."""
    assert all(c >= 0 for c in counts)
    if r == 0:
        return 1
    if r > sum(counts):
        return 0
    return sum(
        count_suffixes(counts[:i] + (c-1,) + counts[i+1:], r-1)
        for i, c in enumerate(counts) if c
    )

def multinomial(counts):
    return factorial(sum(counts)) // prod(factorial(c) for c in counts)

def closed_formula(counts, r):
    """Independent multinomial sum over allowed suffix inventories."""
    return sum(
        multinomial(a)
        for a in product(*(range(n+1) for n in counts))
        if sum(a) == r
    )

def rank_suffix(counts, suffix):
    c = list(counts)
    r, rank = len(suffix), 0
    if r > sum(c):
        raise ValueError("suffix exceeds inventory")
    for letter in suffix:
        i = ALPHABET.index(letter)
        if not c[i]:
            raise ValueError("invalid suffix")
        for j in range(i):
            if c[j]:
                nxt = c.copy()
                nxt[j] -= 1
                rank += count_suffixes(tuple(nxt), r-1)
        c[i] -= 1
        r -= 1
    return rank

def unrank_suffix(counts, r, rank):
    c = list(counts)
    if not (0 <= rank < count_suffixes(tuple(c), r)):
        raise ValueError("rank outside range")
    output = []
    while r:
        for i, available in enumerate(c):
            if not available:
                continue
            nxt = c.copy()
            nxt[i] -= 1
            span = count_suffixes(tuple(nxt), r-1)
            if rank < span:
                c = nxt
                output.append(ALPHABET[i])
                r -= 1
                break
            rank -= span
        else:
            raise AssertionError("rank decoder failed")
    return tuple(output)

def fixed_width_bits(n):
    return (n-1).bit_length()

def example(counts):
    ell = sum(counts)
    return {
        "counts": list(counts),
        "length": ell,
        "full_histories": multinomial(counts),
        "suffix_budget": [
            {
                "pop_budget": r,
                "observable_suffixes": count_suffixes(tuple(counts), r),
                "minimum_extra_fixed_bits": fixed_width_bits(
                    count_suffixes(tuple(counts), r)
                ),
            }
            for r in range(ell+1)
        ],
    }

def check():
    words_checked = 0
    vectors_checked = 0
    cases_checked = 0
    for ell in range(8):
        by_content = defaultdict(list)
        for word in product(ALPHABET, repeat=ell):
            counts = tuple(word.count(x) for x in ALPHABET)
            by_content[counts].append(word)
            words_checked += 1
        for counts, words in by_content.items():
            vectors_checked += 1
            assert len(words) == multinomial(counts)
            for r in range(ell+1):
                observed = {w[-r:] if r else () for w in words}
                n = count_suffixes(counts, r)
                assert len(observed) == n == closed_formula(counts, r)
                ranks = {rank_suffix(counts, suffix) for suffix in observed}
                assert ranks == set(range(n))
                assert {
                    unrank_suffix(counts, r, rank) for rank in ranks
                } == observed
                assert (n == 5**r) == all(x >= r for x in counts)
                cases_checked += 1
            if ell >= 1:
                assert count_suffixes(counts, ell-1) == len(words)
            if ell >= 2 and sum(x > 0 for x in counts) >= 2:
                assert count_suffixes(counts, ell-2) < len(words)
    for ell in range(15):
        for k in range(ell+1):
            counts = (k, ell-k, 0, 0, 0)
            assert count_suffixes(counts, ell) == comb(ell, k)
    return {
        "status": "PASS",
        "scientific_scope": "exact typed symbolic provenance-branch counting, no executed native physical BRC event",
        "source_weights": dict(zip(ALPHABET, WEIGHTS)),
        "ambient_spatial_axes": 6,
        "traces_all_5_sources_checked_up_to_length": 7,
        "exhaustive_source_words_checked": words_checked,
        "endpoint_composition_vectors_checked": vectors_checked,
        "composition_pop_budget_cases_checked": cases_checked,
        "binary_predecessor_specialization_checked_up_to_length": 14,
        "example_2_1_1_1_1": example((2, 1, 1, 1, 1)),
        "example_2_each": example((2, 2, 2, 2, 2)),
        "claim": "given raw endpoint and <=r lifetime pops, exact future classes equal feasible suffixes of length min(r,ell)",
        "proof_status": "author exact mathematical proof; independent review pending",
    }

if __name__ == "__main__":
    result = check()
    target = Path(__file__).with_name("R749STW_BOUNDED_PORT_SUFFIX_RESULTS.json")
    target.write_text(json.dumps(result, indent=2, ensure_ascii=False)+"\n",
                      encoding="utf-8")
    print(json.dumps({
        k: v for k, v in result.items()
        if not k.startswith("example_")
    }, ensure_ascii=False, indent=2))
