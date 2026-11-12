#!/usr/bin/env python3
"""Exact R5 four-class Huffman subtree-width codec on the frozen 1,065-word corpus.

Run at the root of the stacked research branch:
python research_notes/brc_r5_huffman_width_20261112/VERIFY_HUFFMAN_WIDTH_FULL.py

Imports the unchanged PR #2166 exact original-corpus verifier, including its
28-coordinate frozen-source computation and 57,600 full prefix-count checks.
This file adds the prefix-free width encoding, byte-stream round trip,
preorder navigation, and queries on the *new* indexed representation.
"""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] /
                       "brc_r5_variable_skip_full_20261112"))
import VERIFY_R5_VARIABLE_SKIP_FULL as old

N = len(old.sizes)
assert N == 2880 and len(old.pairs) == 1065
CODES = {2: (0,), 4: (1, 0), 8: (1, 1, 0), 12: (1, 1, 1)}
WIDTHS = (2, 4, 8, 12)

def width(s):
    return 2 if s <= 3 else 4 if s <= 15 else 8 if s <= 255 else 12

def uintbits(x, k):
    assert 0 <= x < (1 << k)
    return [(x >> j) & 1 for j in range(k - 1, -1, -1)]

def encode(stride):
    tags = []
    offsets = []
    for i, s in enumerate(old.sizes):
        if i % stride == 0:
            offsets.append(len(tags))
        k = width(s)
        tags.extend(CODES[k])
        tags.extend(uintbits(s, k))
    assert max(offsets) < 65536
    # Previous full bitstream: 45*16 fixed-block offsets, 13,436
    # old tagged-size bits, then the 28,987 unchanged indexed fields.
    base = 16*len(old.offsets) + len(old.var.v)
    unchanged = old.w.v[base:]
    assert base == 14156 and len(unchanged) == 28987
    bits = [z for o in offsets for z in uintbits(o, 16)]
    bits += tags + unchanged
    blob = bytearray((len(bits) + 7)//8)
    for i, bit in enumerate(bits):
        if bit:
            blob[i//8] |= 1 << (7-i%8)
    raw = [(blob[i//8] >> (7-i%8)) & 1 for i in range(len(bits))]
    assert raw == bits and raw[-len(unchanged):] == unchanged
    return offsets, tags, unchanged, bytes(blob), raw

def decoder(stride, raw, taglength):
    nblocks = (N + stride - 1)//stride
    offsetbits = 16*nblocks
    offsets = []
    for block in range(nblocks):
        v = 0
        for bit in raw[16*block:16*(block+1)]:
            v = (v << 1) | bit
        offsets.append(v)
    tagstart = offsetbits
    assert tagstart + taglength <= len(raw)

    def decode_one(pos):
        assert pos < taglength
        p = tagstart + pos
        if raw[p] == 0:
            k, p = 2, p + 1
        elif raw[p+1] == 0:
            k, p = 4, p + 2
        elif raw[p+2] == 0:
            k, p = 8, p + 3
        else:
            k, p = 12, p + 3
        value = 0
        for bit in raw[p:p+k]:
            value = (value << 1) | bit
        assert width(value) == k
        return value, p + k - tagstart

    def lookup(i):
        assert 0 <= i < N
        p = offsets[i//stride]
        result = None
        for _ in range(i%stride + 1):
            result, p = decode_one(p)
        return result
    return lookup, offsets

sizes = old.sizes
assert Counter(map(width, sizes)) == {2: 2182, 4: 572, 8: 122, 12: 4}
tag_cost = sum(len(CODES[k])*c for k, c in Counter(map(width, sizes)).items())
assert tag_cost == 3704
original_tag_cost = 2*N
assert original_tag_cost - tag_cost == 2056

for stride in (8, 16, 32, 64, 128, 256, 512):
    offsets, tags, suffix, blob, raw = encode(stride)
    assert len(tags) == 11380
    totalbits = 40367 + 16*((N + stride - 1)//stride)
    assert len(raw) == totalbits
    assert len(blob) == (totalbits + 7)//8
    size, new_offsets = decoder(stride, raw, len(tags))
    assert all(size(i) == s for i, s in enumerate(sizes))
    assert offsets == new_offsets
    print("HUFFMAN_STRIDE", stride, "BITS", totalbits, "BYTES", len(blob),
          "ALL_NODE_ROUNDTRIPS", N)
    if stride == 64:
        size64 = size
        raw64 = raw
        blob64 = blob

assert len(raw64) == 41087 and len(blob64) == 5136
recovered = [None] * N

def walk(i, path):
    recovered[i] = path
    j = i + 1
    while j < i + size64(i):
        walk(j, path + (old.labels[j-1],))
        j += size64(j)
    assert j == i + size64(i)

walk(0, ())
assert recovered == old.paths
assert sum(old.terms) == 1065
assert {p for p, term in zip(recovered, old.terms) if term} == \
       set(old.old.words.values())

def query(i, r):
    l = old.rt.rank(i)
    h = old.rt.rank(i + size64(i))
    if r == F(1, 23):
        return h - l
    delta = 1 - 23*r
    assert delta > 0
    a, b = old.rm3.rank(l), old.rm3.rank(h)
    c, d = old.rm12.rank(l), old.rm12.rank(h)
    spans = {3: (a, b), 12: (c, d), 15: (l-a-c, h-b-d)}
    return sum(old.upto(q, *spans[q],
                        (36*q*delta.denominator)//delta.numerator)
               for q in (3, 12, 15))

checks = 0
for r in old.samples:
    for i in range(N):
        assert query(i, r) == old.query(i, r)
        checks += 1
assert checks == 57600
assert query(0, F(0)) == 605 and query(0, F(1,23)) == 1065
print("HUFFMAN_TAG_BITS", tag_cost, "PREVIOUS_TAG_BITS", original_tag_cost)
print("NEW_TAGGED_SUBTREE_BITS", len(tags))
print("NEW_FULL_BITS", len(raw64), "NEW_FULL_BYTES", len(blob64))
print("EXACT_ALL_PREFIX_QUERIES", checks)
print("PASS_R5_HUFFMAN_WIDTH_FULL_FROZEN_CORPUS")
