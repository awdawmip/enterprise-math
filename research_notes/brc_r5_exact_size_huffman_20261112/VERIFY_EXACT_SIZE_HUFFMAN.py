#!/usr/bin/env python3
"""Exact subtree-size canonical Huffman index on the frozen R5 1,065-word corpus.

From repository root of this stacked branch:
python research_notes/brc_r5_exact_size_huffman_20261112/VERIFY_EXACT_SIZE_HUFFMAN.py

The pinned PR #2171 source computes the original 28-coordinate corpus and
checks 57,600 prefix queries. This script independently recodes exact subtree
sizes, includes the complete self-describing codebook and query suffix,
decodes from packed bytes, and compares new prefix counts to actual words.
"""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
from math import ceil
import heapq
import itertools
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] /
                       "brc_r5_huffman_width_20261112"))
import VERIFY_HUFFMAN_WIDTH_FULL as previous
old = previous.old
sizes = old.sizes
N = len(sizes)
assert N == 2880 and len(old.pairs) == 1065
freq = Counter(sizes)
assert len(freq) == 78 and max(sizes) == 2880
heap = []
serial = itertools.count()
for symbol, count in freq.items():
    heapq.heappush(heap, (count, next(serial), symbol))
while len(heap) > 1:
    a, b = heapq.heappop(heap), heapq.heappop(heap)
    heapq.heappush(heap, (a[0]+b[0], next(serial), (a[2], b[2])))
lengths = {}
def depths(node, n):
    if isinstance(node, int):
        lengths[node] = n
    else:
        depths(node[0], n+1)
        depths(node[1], n+1)
depths(heap[0][2], 0)
assert max(lengths.values()) == 12
code = {}
value = last_length = 0
for width, symbol in sorted((w, s) for s, w in lengths.items()):
    value <<= width-last_length
    assert value < (1 << width)
    code[symbol] = (value, width)
    value += 1
    last_length = width

def ubits(n, width):
    assert 0 <= n < (1 << width)
    return [(n >> i) & 1 for i in range(width-1, -1, -1)]

book = ubits(len(freq), 7)
for symbol in sorted(lengths):
    book.extend(ubits(symbol, 12))
    book.extend(ubits(lengths[symbol], 5))
assert len(book) == 1333
stream_bits = sum(freq[s] * lengths[s] for s in freq)
assert stream_bits == 8472
# The source-verified 28,987-bit suffix stores operation labels, terminal
# flags, q masks, all 29 wavelet rows and the complete rank directories.
suffix = old.w.v[16*len(old.offsets)+len(old.var.v):]
assert len(suffix) == 28987

def encoded(stride):
    tags = []
    offsets = []
    for i, symbol in enumerate(sizes):
        if i % stride == 0:
            offsets.append(len(tags))
        bits, width = code[symbol]
        tags.extend(ubits(bits, width))
    assert len(tags) == 8472 and max(offsets) < 65536
    out = book + [bit for o in offsets for bit in ubits(o, 16)] + tags + suffix
    assert len(out) == 1333 + 16*ceil(N/stride) + 8472 + 28987
    blob = bytearray((len(out)+7)//8)
    for i, bit in enumerate(out):
        if bit:
            blob[i//8] |= 1 << (7-i%8)
    return bytes(blob), len(out)

def decoded(blob, nbits, stride):
    raw = [(blob[i//8] >> (7-i%8)) & 1 for i in range(nbits)]
    cursor = 0
    def get(k):
        nonlocal cursor
        val = 0
        for bit in raw[cursor:cursor+k]:
            val = val*2+bit
        cursor += k
        return val
    count = get(7)
    assert count == 78
    lengths2 = {}
    for _ in range(count):
        s, width = get(12), get(5)
        assert s not in lengths2
        lengths2[s] = width
    assert lengths2 == lengths
    inverse = {}
    value = last_length = 0
    for width, symbol in sorted((w, s) for s, w in lengths2.items()):
        value <<= width-last_length
        inverse[width, value] = symbol
        value += 1
        last_length = width
    offsets = [get(16) for _ in range(ceil(N/stride))]
    start = cursor
    assert raw[start+8472:] == suffix
    def subtree_size(i):
        pos = start + offsets[i//stride]
        result = None
        for _ in range(i%stride+1):
            v = 0
            for width in range(1, 13):
                v = (v << 1) | raw[pos]
                pos += 1
                if (width, v) in inverse:
                    result = inverse[width, v]
                    break
            else:
                raise AssertionError("Not a valid canonical Huffman codeword")
        return result
    return subtree_size

for stride in (8, 16, 32, 64, 128):
    blob, bits = encoded(stride)
    size = decoded(blob, bits, stride)
    assert all(size(i) == s for i, s in enumerate(sizes))
    print("EXACT_SIZE_STRIDE", stride, "BITS", bits, "BYTES", len(blob),
          "REAL_NODE_ROUNDTRIPS", N)
    if stride == 64:
        size64 = size
        bits64 = bits
        bytes64 = len(blob)
assert bits64 == 39512 and bytes64 == 4939

def query(i, r):
    lo = old.rt.rank(i)
    hi = old.rt.rank(i + size64(i))
    if r == F(1, 23):
        return hi-lo
    delta = 1-23*r
    assert delta > 0
    a, b = old.rm3.rank(lo), old.rm3.rank(hi)
    c, d = old.rm12.rank(lo), old.rm12.rank(hi)
    spans = {3:(a,b), 12:(c,d), 15:(lo-a-c,hi-b-d)}
    return sum(old.upto(q, *spans[q],
                        (36*q*delta.denominator)//delta.numerator)
               for q in (3,12,15))

words = old.old.old.words
assert len(words) == 1065
checks = 0
for r in old.samples:
    observed = Counter()
    for (q,n), word in words.items():
        if r == F(1,23) or r >= (1-F(36*q,n))/23:
            for j in range(len(word)+1):
                observed[word[:j]] += 1
    for i, prefix in enumerate(old.paths):
        assert query(i,r) == observed[prefix]
        checks += 1
assert checks == 57600
assert query(0,F(0)) == 605 and query(0,F(1,23)) == 1065
print("DISTINCT_SIZE_SYMBOLS",len(freq),"MAX_CODEWORD_BITS",max(lengths.values()))
print("CODEBOOK_BITS",len(book),"EXACT_SIZE_STREAM_BITS",stream_bits)
print("UNCHANGED_QUERY_SUFFIX_BITS",len(suffix))
print("FULL_INDEX_BITS",bits64,"FULL_INDEX_BYTES",bytes64)
print("REAL_CORPUS_EXACT_PREFIX_QUERIES",checks)
print("PASS_R5_CANONICAL_EXACT_SIZE_HUFFMAN_FULL_FROZEN_CORPUS")
