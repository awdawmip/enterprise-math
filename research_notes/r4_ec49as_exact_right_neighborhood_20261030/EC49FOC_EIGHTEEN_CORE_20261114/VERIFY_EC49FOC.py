#!/usr/bin/env python3
"""Exact native BRC horizon-18 and 128-descendant verification.
Run alongside the unmodified VERIFY_EC49FNY_INDEPENDENT.py from PR #2343:
    python VERIFY_EC49FOC.py master_and_radius3_cases.txt EC49FOC_CERTIFICATE.json
"""
import hashlib
import itertools
import json
import sys
from functools import lru_cache
from pathlib import Path
import VERIFY_EC49FNY_INDEPENDENT as native

ROOTS = (3, 5, 6, 7)
MASTER_SHA = "cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"
PIN = "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
ORIGINAL = (32768, 5312869, 8668826, 10240)
BASE_ERASURES = (4,5,6,8,9,10,15,12,14,16,18,20,22,23)
EXTRA = (0,1,2,3,7,11,13)
B = 155

def erase(masks, labels):
    m = list(masks)
    for label in labels:
        j = [k for k in range(4) if (m[k] >> label) & 1]
        assert len(j) == 1, (label, j)
        m[j[0]] ^= 1 << label
    return tuple(m)

def future(masks):
    used = 0
    for mask in masks:
        assert not used & mask
        used |= mask
    return tuple(label for label in range(24) if not (used >> label) & 1)

def run(master, output):
    assert hashlib.sha256(master.read_bytes()).hexdigest() == MASTER_SHA
    words, keys = native.frozen(master, case=32279)
    profiles = {r: native.table(words, keys, r) for r in ROOTS}
    bits = {r: {l: 1 << b for l, b in profiles[r][1].items()} for r in ROOTS}
    options = {l: tuple(r for r in ROOTS if l in bits[r]) for l in range(24)}
    assert all(options.values())

    @lru_cache(None)
    def optimum(masks, requirements):
        root_bits = {r: 0 for r in ROOTS}
        for j, r in enumerate(ROOTS):
            for l in range(24):
                if (masks[j] >> l) & 1:
                    root_bits[r] |= bits[r][l]
        flexible = []
        for l in requirements:
            if len(options[l]) == 1:
                r = options[l][0]
                root_bits[r] |= bits[r][l]
            else:
                flexible.append(l)
        best = 10**9
        best_roots = None
        count = 0
        minimizers = 0
        for selection in itertools.product(*(options[l] for l in flexible)):
            trial = root_bits.copy()
            for l, r in zip(flexible, selection):
                trial[r] |= bits[r][l]
            value = sum(profiles[r][2][trial[r]] for r in ROOTS)
            count += 1
            if value < best:
                best = value
                best_roots = tuple(zip(flexible, selection))
                minimizers = 1
            elif value == best:
                minimizers += 1
        assert count > 0
        return best, best_roots, count, minimizers

    def certificate(masks):
        U = future(masks)
        full = optimum(masks, U)
        deletion = [(l, optimum(masks, tuple(x for x in U if x != l)))
                    for l in U]
        return {
            "masks": masks, "U": U,
            "full": {"cost": full[0], "flexible_roots": full[1],
                     "legal_placements": full[2], "minimizers": full[3]},
            "deletion": [{"label": l, "cost": o[0], "roots": o[1],
                          "legal_placements": o[2]} for l, o in deletion],
            "minimal_strict_core": full[0] > B and
                 all(o[0] <= B for l, o in deletion),
        }

    p17 = erase(ORIGINAL, BASE_ERASURES)
    p18 = erase(p17, (11,))
    assert p17 == (0,5,138,10240)
    assert p18 == (0,5,138,8192)
    c17, c18 = certificate(p17), certificate(p18)
    assert len(c17["U"]) == 17 and c17["minimal_strict_core"]
    assert len(c18["U"]) == 18 and c18["minimal_strict_core"]
    assert (c17["full"]["cost"], c17["full"]["legal_placements"]) == (156,162)
    assert (c18["full"]["cost"], c18["full"]["legal_placements"]) == (156,324)

    # Unique-root erasure lemma plus these two extreme-cost witnesses
    # prove that optional erasure of 0..3 leaves h* at exactly 17 or 18.
    assert optimum(erase(p17,(0,1,2,3)), c17["U"])[0] == 156
    assert optimum(erase(p18,(0,1,2,3)), c18["U"])[0] == 156
    assert optimum(erase(p17,(7,)), future(erase(p17,(7,))))[0] == 155
    assert optimum(erase(p17,(13,)), future(erase(p17,(13,))))[0] == 154

    descendants = []
    for n in range(8):
        for extra in itertools.combinations(EXTRA, n):
            masks = erase(p17, extra)
            U = future(masks)
            cost = optimum(masks, U)[0]
            predicted = 154 if 13 in extra else 155 if 7 in extra else 156
            assert cost == predicted, (extra,cost,predicted)
            status = ("FEASIBLE" if 7 in extra or 13 in extra else
                      "H18" if 11 in extra else "H17")
            if status != "FEASIBLE":
                core = c18["U"] if status == "H18" else c17["U"]
                assert optimum(masks, core)[0] == 156
            descendants.append({"erasures":extra, "future_count":len(U),
                                "full_optimum":cost, "class":status})
    histogram = {label:sum(x["class"]==label for x in descendants)
                 for label in ("H17","H18","FEASIBLE")}
    assert histogram == {"H17":16,"H18":16,"FEASIBLE":96}
    payload = {"frozen_input_pin":PIN,"original_root_masks":ORIGINAL,
               "master_sha256":MASTER_SHA,"threshold":B,
               "mandatory_erasures":BASE_ERASURES,"h17":c17,"h18":c18,
               "descendant_histogram":histogram,"descendants":descendants}
    output.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",
                      encoding="utf-8")
    print("EC49FOC_EXACT_PASS H17=16 H18=16 FEASIBLE=96")
    print("FULL18",c18["full"])
    print("DELETIONS18",[(d["label"],d["cost"]) for d in c18["deletion"]])
    print("OUTPUT_SHA256",hashlib.sha256(output.read_bytes()).hexdigest())

if __name__ == "__main__":
    assert len(sys.argv)==3
    run(Path(sys.argv[1]),Path(sys.argv[2]))
