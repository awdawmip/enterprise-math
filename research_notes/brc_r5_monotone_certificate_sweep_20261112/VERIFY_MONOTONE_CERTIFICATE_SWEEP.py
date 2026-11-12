#!/usr/bin/env python3
"""Exact R5 monotone activation sweep over predecessor's frozen 1,065 words.
Requires sibling brc_r5_dual_zero_right_persistence_20261112 artifacts.
Python 3 standard library only. Does not create task claims or Source Results.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import groupby
from pathlib import Path
import sys

source_dir = (Path(__file__).resolve().parents[1] /
              "brc_r5_dual_zero_right_persistence_20261112")
sys.path.insert(0, str(source_dir))
import VERIFY_TRIE_CODEC as old

words = old.words
f = old.f
assert len(words) == 1065
assert len(old.seen_paths) == old.N == 2880
assert old.E == 2879
assert sum(map(len, words.values())) == 6379

I_left = F(-427508577031693280, 628800490619)
I_right = F(1, 23)
pair_order = sorted(words)
pair_rank = {pair: rank for rank, pair in enumerate(pair_order)}
node_of_prefix = {tuple(path): i for i, path in enumerate(old.seen_paths)}
assert len(node_of_prefix) == old.N
assert node_of_prefix[()] == 0

events = []
for pair in pair_order:
    q, n = pair
    word = words[pair]
    assert q in (3, 12, 15) and n > 0
    assert len(set(word)) == len(word)
    tau = (1 - F(36*q, n)) / 23
    assert I_left < tau < I_right
    mask = sum(1 << (atom-1) for atom in word)
    assert -f.P[mask][f.k0] == n
    assert -f.P[mask][f.k1] == 36*q
    # Independent prefix-by-prefix rational checks at both ends and midpoint.
    for r in (tau, (tau + I_right) / 2, I_right):
        epsilon = f.x * (1 - 23*r) / q
        prefix_mask = 0
        for atom in (None,) + word:
            if atom is not None:
                prefix_mask |= 1 << (atom-1)
            assert all(
                f.X[k] + r*f.x*f.H[k] + (epsilon/36)*f.P[prefix_mask][k] >= 0
                for k in range(28)
            )
    r_left = (I_left + tau) / 2
    epsilon_left = f.x * (1 - 23*r_left) / q
    mass_left_k0 = (f.X[f.k0] + r_left*f.x*f.H[f.k0]
                    + (epsilon_left/36)*f.P[mask][f.k0])
    assert mass_left_k0 < 0
    events.append((tau, pair))
events.sort()

active = [0] * len(pair_order)
counts = [0] * old.N
groups = 0
counter_increments = 0
flag_mutations = 0
max_tie = 0
for threshold, grouped in groupby(events, key=lambda x: x[0]):
    pairs_now = [pair for _, pair in grouped]
    groups += 1
    max_tie = max(max_tie, len(pairs_now))
    # For a given q, n -> tau is injective; at most one event per q.
    assert len(pairs_now) <= 3
    assert len({q for q, _ in pairs_now}) == len(pairs_now)
    for pair in pairs_now:
        rank = pair_rank[pair]
        assert active[rank] == 0
        active[rank] = 1
        flag_mutations += 1
        word = words[pair]
        for d in range(len(word)+1):
            counts[node_of_prefix[word[:d]]] += 1
            counter_increments += 1
    # Full independent counter recomputation after every activation group.
    rebuilt = [0] * old.N
    for pair in pair_order:
        if active[pair_rank[pair]]:
            word = words[pair]
            for d in range(len(word)+1):
                rebuilt[node_of_prefix[word[:d]]] += 1
    assert counts == rebuilt
    assert counts[0] == flag_mutations

assert groups <= 1065 and max_tie <= 3
assert flag_mutations == 1065
assert counter_increments == 6379+1065 == 7444
assert counts[0] == 1065
assert max(counts) == 1065
assert len(events) == 1065

# Recompute exact storage arithmetic rather than trusting the narrative.
N, E, T, total_len = old.N, old.E, len(words), 6379
trie_bits = (N+E)+4*E+N
flat_bits = 4*total_len+4*T
assert trie_bits == 20155 and flat_bits == 29776
assert N < 2**12 and flat_bits < 2**15 and T < 2**11
trie_indexed_bits = trie_bits + 12*T + T
flat_indexed_bits = flat_bits + 15*T + T
counter_bits = 11*N
assert trie_indexed_bits == 34000
assert flat_indexed_bits == 46816
assert (trie_indexed_bits+7)//8 == 4250
assert (flat_indexed_bits+7)//8 == 5852
assert ((flat_indexed_bits+7)//8 -
        (trie_indexed_bits+7)//8) == 1602
assert counter_bits == 31680
assert (trie_bits+counter_bits+T+7)//8 == 6613
assert (trie_bits+counter_bits+T+12*T+7)//8 == 8210

print("SELECTED_COLLISION_CERTIFICATES", T)
print("DISTINCT_CERTIFICATE_ACTIVATION_PARAMETERS", groups)
print("MAX_CERTIFICATES_AT_ONE_PARAMETER", max_tie)
print("PREFIX_COUNTER_INCREMENTS_EXACT", counter_increments)
print("TERMINAL_ACTIVATION_FLAG_WRITES", flag_mutations)
print("COMBINED_MUTATIONS", counter_increments+flag_mutations)
print("INDEXED_ACTIVE_TRIE_BYTES", (trie_indexed_bits+7)//8)
print("INDEXED_ACTIVE_FLAT_BYTES", (flat_indexed_bits+7)//8)
print("INDEXED_BYTES_SAVED", 1602)
print("ACTIVE_COUNTER_TRIE_BYTES", 6613)
print("INDEXED_ACTIVE_COUNTER_TRIE_BYTES", 8210)
print("PASS_R5_MONOTONE_CERTIFICATE_SWEEP")
