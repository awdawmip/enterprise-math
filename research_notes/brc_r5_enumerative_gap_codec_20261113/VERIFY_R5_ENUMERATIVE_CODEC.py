#!/usr/bin/env python3
"""Exact R5 checkpoint gap enumerative codec, standard-library verifier.

Read the actual published predecessor 56B center sidecar from the stacked
PR #2232. Verify derivative centers; do not claim frozen rational E was rerun.
"""
from __future__ import annotations
from collections import Counter
from itertools import product
from pathlib import Path
import hashlib, json, math, statistics, time

HERE = Path(__file__).resolve().parent
PRIOR = HERE.parent / "brc_r5_radius_gap_codec_20261113" / "R5_CENTERS_56B.hex"
ALPHABET = (3, 4, 5)
N, FIRST, SPAN, W = 212, 1, 951, 953
OLD_SHA = "bf4f377e8a3b9823d589d0f5c5b0b5973f374a09aa986d5b729bc695c5de0326"

def prior_centers(data):
    if len(data) != 56 or int.from_bytes(data[:2], "little") != 213:
        raise ValueError("predecessor size/count")
    x = int.from_bytes(data[2:], "little")
    c = [x & 3]; x >>= 2
    for _ in range(N):
        digit = x & 3; x >>= 2
        if digit == 3:
            raise ValueError("invalid gap digit")
        c.append(c[-1] + 3 + digit)
    if x or c[0] != FIRST or c[-1] != FIRST + SPAN:
        raise ValueError("predecessor endpoints or padding")
    return c

def multinomial(counts):
    n = sum(counts.get(a, 0) for a in ALPHABET)
    return math.factorial(n) // math.prod(math.factorial(counts.get(a, 0)) for a in ALPHABET)

def multiset_rank(word, counts):
    rem = {a: counts.get(a, 0) for a in ALPHABET}
    if len(word) != sum(rem.values()):
        raise ValueError("wrong word length")
    ways = multinomial(rem); n = len(word); rank = 0
    for sym in word:
        if sym not in ALPHABET or rem[sym] <= 0:
            raise ValueError("wrong symbol count")
        for a in ALPHABET:
            if a >= sym:
                break
            rank += ways * rem[a] // n
        ways = ways * rem[sym] // n
        rem[sym] -= 1; n -= 1
    assert n == 0 and ways == 1
    return rank

def multiset_unrank(rank, counts):
    rem = {a: counts.get(a, 0) for a in ALPHABET}
    ways = multinomial(rem)
    if not 0 <= rank < ways:
        raise ValueError("rank outside class")
    n = sum(rem.values()); out = []
    while n:
        for a in ALPHABET:
            take = ways * rem[a] // n
            if rank < take:
                out.append(a); ways = take; rem[a] -= 1; n -= 1
                break
            rank -= take
        else:
            raise AssertionError("missing rank interval")
    assert rank == 0
    return out

def histograms(n, span):
    for a in range(n + 1):
        b = 5 * n - span - 2 * a
        c = n - a - b
        if b >= 0 and c >= 0:
            yield {3: a, 4: b, 5: c}

def span_rank(word, n, span):
    if len(word) != n or sum(word) != span:
        raise ValueError("word span")
    counts = Counter(word)
    offset = 0
    for h in histograms(n, span):
        if h[3] == counts[3]:
            return offset + multiset_rank(word, h)
        offset += multinomial(h)
    raise ValueError("histogram outside family")

def span_unrank(rank, n, span):
    total = sum(multinomial(h) for h in histograms(n, span))
    if not 0 <= rank < total:
        raise ValueError("span rank")
    for h in histograms(n, span):
        ways = multinomial(h)
        if rank < ways:
            return multiset_unrank(rank, h)
        rank -= ways
    raise AssertionError("missing span interval")

def restore(first, gaps):
    out = [first]
    for gap in gaps:
        out.append(out[-1] + gap)
    return out

def median_microseconds(fn, repeats=100, rounds=11):
    result = []
    for _ in range(rounds):
        t = time.perf_counter_ns()
        for __ in range(repeats):
            fn()
        result.append((time.perf_counter_ns() - t) / repeats / 1000)
    return statistics.median(result)

old = bytes.fromhex(PRIOR.read_text().strip())
assert hashlib.sha256(old).hexdigest() == OLD_SHA
centers = prior_centers(old)
word = [b-a for a,b in zip(centers, centers[1:])]
hist = Counter(word)
assert hist == Counter({3:16, 4:77, 5:119})
assert len(centers) == 213 and centers[0] == 1 and centers[-1] == 952
M = multinomial(hist)
T = sum(multinomial(h) for h in histograms(N, SPAN))
assert M.bit_length() == 264 and T.bit_length() == 275
rank33 = multiset_rank(word, hist)
rank35 = span_rank(word, N, SPAN)
fixed33 = rank33.to_bytes(33, "big")
span35 = rank35.to_bytes(35, "big")
self37 = bytes((213, 1, 16, 77)) + fixed33
assert restore(1, multiset_unrank(int.from_bytes(fixed33,"big"),hist)) == centers
assert restore(1, span_unrank(int.from_bytes(span35,"big"),N,SPAN)) == centers
assert restore(self37[1], multiset_unrank(int.from_bytes(self37[4:],"big"),{
    3:self37[2],4:self37[3],5:self37[0]-1-self37[2]-self37[3]})) == centers
invalid_count = 0
for fn, bad, extra in ((multiset_unrank,-1,hist),(multiset_unrank,M,hist),
                       (span_unrank,-1,(N,SPAN)),(span_unrank,T,(N,SPAN))):
    try:
        if isinstance(extra,tuple):
            fn(bad,*extra)
        else:
            fn(bad,extra)
    except ValueError:
        invalid_count += 1
assert invalid_count == 4
tested = 0
for n in range(9):
    for w0 in product(ALPHABET,repeat=n):
        w = list(w0)
        assert multiset_unrank(multiset_rank(w,Counter(w)),Counter(w)) == w
        assert span_unrank(span_rank(w,n,sum(w)),n,sum(w)) == w
        tested += 1
assert tested == 9841
report = {
    "status":"PASS_DERIVATIVE_CENTER_CODEC",
    "scientific_pin":"435e77af0d180eac32bd1f9c4c464bc4010b7551",
    "predecessor_56B_sha256":OLD_SHA,
    "scope":"Frozen predecessor centers and exhaustive small ternary words; NOT full rational E/certificate checks",
    "centers":213,"first_center":1,"last_center":952,
    "gap_hist":{"3":16,"4":77,"5":119},
    "fixed_hist_family_bits":M.bit_length(),
    "fixed_span_family_bits":T.bit_length(),
    "fixed_hist_family_cardinality":str(M),
    "fixed_span_family_cardinality":str(T),
    "fixed_hist_codec_bytes":33,"fixed_span_codec_bytes":35,"hist_header_codec_bytes":37,
    "fixed33_hex":fixed33.hex(),"span35_hex":span35.hex(),"self37_hex":self37.hex(),
    "fixed33_sha256":hashlib.sha256(fixed33).hexdigest(),
    "span35_sha256":hashlib.sha256(span35).hexdigest(),
    "self37_sha256":hashlib.sha256(self37).hexdigest(),
    "exhaustive_ternary_words_length_0_to_8":tested,
    "invalid_ranks_rejected":invalid_count,
    "timings_local_median_us":{
        "prior_56B_decode":round(median_microseconds(lambda:prior_centers(old),200),3),
        "fixed_hist_33B_decode":round(median_microseconds(lambda:multiset_unrank(rank33,hist)),3),
        "span_35B_decode":round(median_microseconds(lambda:span_unrank(rank35,N,SPAN)),3)
    },
    "formal_claim":False,"independent_review":False
}
(HERE / "EXACT_OUTPUT.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
print(json.dumps(report,indent=2))
