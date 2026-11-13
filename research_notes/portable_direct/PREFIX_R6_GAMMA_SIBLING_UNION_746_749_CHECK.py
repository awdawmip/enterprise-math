#!/usr/bin/env python3
"""Recompute the exact published PREFIX746-749 sibling cell union; no external packages.
Run in research_notes/portable_direct with the exact GitHub source JSON files.
This audits coordinate-set accounting, not the per-cell Gamma inequalities.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PIN = "f42f2906d77f24085c123f3ccfe9667d41caa96d"
BASE = 141942
GRID = 384 ** 2
SOURCES = [
  [
    "PREFIX746/114",
    "PREFIX746_R6_GAMMA_114_RESULTS.json",
    "checked_upper_cells",
    "bf569554bacee9216659a275462bc44f6257783f",
    57
  ],
  [
    "PREFIX746/30",
    "PREFIX746_R6_ADAPTIVE_8X8_30_RESULTS.json",
    "cells",
    "32d88f70c3cdb8348f8dab61d1c701feedf33ac6",
    15
  ],
  [
    "PREFIX747/68",
    "PREFIX747_R6_GAMMA_68_RESULTS.json",
    "cells",
    "123c71171647209d71f4242cd43d6f357171c9ee",
    34
  ],
  [
    "PREFIX747/4",
    "PREFIX747_R6_GAMMA_4_CELLS_RESULTS.json",
    "checked_original_cells",
    "80f6374c28e912dbd13e8688fecec7d4464ca54d",
    2
  ],
  [
    "PREFIX747/46",
    "PREFIX747_R6_GAMMA_NEW_46_RESULTS.json",
    "checked_original_cells",
    "3834a27a7586a34283eb3cb6e2a86e089e0e255d",
    23
  ],
  [
    "PREFIX748/180",
    "PREFIX748_R6_DYADIC_INTERVAL_180_RESULTS.json",
    "cells",
    "89d3b3932353620cc67ea47028981068f76565be",
    90
  ],
  [
    "PREFIX748/4",
    "PREFIX748_R6_GAMMA_NEIGHBOR_4_RESULTS.json",
    "checked_original_cells",
    "1575b5118efe787b83d9a58b9fc5f2443c07e7cc",
    2
  ],
  [
    "PREFIX749/28",
    "PREFIX749_R6_GAMMA_FRONTIER_28_RESULTS.json",
    "checked_original_cells",
    "513e6b763262cb7c80890e7c4a628f01d8d21ed9",
    14
  ],
  [
    "PREFIX749/4",
    "PREFIX749_R6_GAMMA_NEIGHBORS_4_RESULTS.json",
    "checks",
    "80020afaed0ccc7c36432d349522e110d1176d24",
    2
  ],
  [
    "PREFIX749/6",
    "PREFIX749_R6_GAMMA_6_CELLS_RESULTS.json",
    "original_cells",
    "752d513a8cd0f73ebc7c659488f46058b4e14eab",
    3
  ],
  [
    "PREFIX749/16x16/6",
    "PREFIX749_R6_ADAPTIVE16_6_RESULTS.json",
    "original_cells",
    "b2af84bee227b3034240a90c0ed78fd1fd9c4f04",
    3
  ]
]

def git_blob_oid(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\\0" + raw).hexdigest()

def pairs_from_source(tag, name, field, expected_sha, expected_count):
    raw = (ROOT / name).read_bytes()
    assert git_blob_oid(raw) == expected_sha, (tag, "Git blob mismatch")
    data = json.loads(raw)
    pin = next((data[key] for key in ("frozen_science_pin", "science_pin", "scientific_pin") if key in data), None)
    assert pin == PIN, (tag, "frozen science pin mismatch")
    seq = data[field]
    out = set()
    for r in seq:
        i, j = (r["i"], r["j"]) if isinstance(r, dict) else r[:2]
        assert isinstance(i, int) and isinstance(j, int) and 0 <= i < j < 384
        assert (i, j) not in out, (tag, "duplicate source pair", i, j)
        out.add((i, j))
    assert len(out) == expected_count, (tag, len(out), expected_count)
    return out

def main():
    owner = {}
    increments = []
    for tag, name, field, sha, expected in SOURCES:
        current = pairs_from_source(tag, name, field, sha, expected)
        overlap = current & owner.keys()
        novel = current - owner.keys()
        for pair in novel:
            owner[pair] = tag
        increments.append((tag, 2*len(current), 2*len(overlap), 2*len(novel)))
        print(tag, "raw", 2*len(current), "overlap", 2*len(overlap), "new", 2*len(novel))
        if tag == "PREFIX748/4":
            assert BASE + 2*len(owner) == 142326
    assert len(owner) == 197
    assert BASE + 2*len(owner) == 142336
    assert GRID - (BASE + 2*len(owner)) == 5120
    expected_increments = [114,16,56,0,18,180,0,4,0,0,6]
    assert [i[-1] for i in increments] == expected_increments
    print("PASS upper_pairs=197 mirrored=394 conditional_union=142336 remaining=5120")

if __name__ == "__main__":
    main()
