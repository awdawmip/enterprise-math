#!/usr/bin/env python3
"""Exact 78,561-case seven-key two-swap demand-cover screen on frozen EC49 model."""
from __future__ import annotations
import collections
import itertools
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE.parent / "EC49FJD_RELEASE_B11_COMPLETE_20261111"
sys.path.insert(0, str(SRC))
from EC49FGW_RADIUS5_SCREEN import PIN, all_words, raw_key

EXPECTED_PIN = "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
BASE = {(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}

def main():
    assert PIN == EXPECTED_PIN
    catalogue = list(all_words())
    labels = sorted({label for label, _ in catalogue})
    assert len(catalogue) == 178850 and len(labels) == 24
    label_id = {label: i for i, label in enumerate(labels)}
    covers = collections.defaultdict(int)
    for label, word in catalogue:
        covers[raw_key(word)] |= 1 << label_id[label]
    allkeys = sorted(covers)
    assert len(allkeys) == 94 and BASE <= set(allkeys)
    outside = sorted(set(allkeys) - BASE)
    assert len(outside) == 87
    full_mask = (1 << len(labels)) - 1

    counts = []
    feasible = []
    for old in itertools.combinations(sorted(BASE), 2):
        kept = BASE - set(old)
        fixed_mask = 0
        for key in kept:
            fixed_mask |= covers[key]
        n = 0
        first = []
        for added in itertools.combinations(outside, 2):
            if fixed_mask | covers[added[0]] | covers[added[1]] == full_mask:
                n += 1
                feasible.append({"drop": old, "add": added})
                if len(first) < 2:
                    first.append(added)
        counts.append({"drop": old, "coverable": n, "not_coverable": 3741-n, "first_two": first})

    assert len(counts) == 21
    assert len(feasible) == 6315
    assert sum(x["not_coverable"] for x in counts) == 72246
    assert sum(x["coverable"] == 0 for x in counts) == 13
    assert all(x["coverable"] == 0 for x in counts if (2,1,1) in x["drop"])
    payload = {
        "schema": "EC49FKZ_TWO_KEY_COVER_V1",
        "frozen_scientific_pin": PIN,
        "legal_words": len(catalogue),
        "demands": len(labels),
        "raw_cache_keys": len(allkeys),
        "two_key_sets": 78561,
        "coverable": len(feasible),
        "not_coverable": 72246,
        "per_dropped_pair": counts,
    }
    output = HERE / "REGENERATED_EC49FKZ_COVER.json"
    output.write_text(json.dumps(payload, indent=2, ensure_ascii=False)+"\n")
    print("EC49FKZ_78561_TWO_KEY_COVER_EXACT_PASS",
          len(feasible), 72246, "zero_drop_classes", 13)

if __name__ == "__main__":
    main()
