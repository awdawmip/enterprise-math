#!/usr/bin/env python3
"""EC49FHG: fully enumerate 112 key-releasing B=17 joint-H9 cases per witness.
The three-group exact prefix-trie solver from EC49FHF is applied without any cache-key restriction.
"""
import collections
import itertools
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
SOURCE = PARENT / "EC49FGW_RADIUS5_EXACT_SCREENS_20261110"
PAIR = PARENT / "EC49FHF_H9_PAIR_BOUND_20261111"
sys.path.insert(0, str(SOURCE))
sys.path.insert(0, str(PAIR))
from EC49FGW_RADIUS5_SCREEN import W, PIN, all_words, pref, raw_key, validate_profile
from VERIFY_EC49FHF import solve_group_tree, H9_LABELS, catalog as h9catalog

assert PIN == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
h8catalog = collections.defaultdict(list)
catalog_count = 0
for lab, word in all_words():
    catalog_count += 1
    if lab[0] == 8:
        h8catalog[lab].append(pref(word)[-1])
assert catalog_count == 178850
assert [len(h8catalog[(8,s)]) for s in (1,2,4,8)] == [28063,34777,28063,34777]

def evaluate(profile):
    rows, paths = validate_profile(profile)
    labs = [(row["window"],row["signature"]) for row in rows]
    assert tuple(labs[22:]) == H9_LABELS
    key_support = collections.defaultdict(int)
    prefix_support = collections.defaultdict(int)
    for i,(row,ps) in enumerate(zip(rows,paths)):
        key_support[raw_key(row["word"])] |= 1 << i
        for prefix in ps:
            prefix_support[prefix] |= 1 << i
    assert len(key_support) == 7 and len(prefix_support) == 94
    groups = collections.defaultdict(list)
    for Q in itertools.combinations(range(24), 5):
        mask = sum(1 << i for i in Q)
        B = sum((support & mask) == support for support in prefix_support.values()) - 1
        released = sum((support & mask) == support for support in key_support.values())
        if B != 17 or not released or not (22 in Q and 23 in Q):
            continue
        h8indices = [i for i in Q if 18 <= i <= 21]
        assert len(h8indices) == 1
        F = frozenset(p for p,support in prefix_support.items() if (support & mask) != support)
        assert len(F) == 76
        groups[(F,labs[h8indices[0]])].append(Q)
    assert len(groups) == 4
    evidence = []
    for (F, lab), positions in sorted(groups.items(), key=lambda x:x[0][1]):
        min_cost, metrics = solve_group_tree([h9catalog[x] for x in H9_LABELS] +
                                             [h8catalog[lab]], set(F))
        assert min_cost == 18
        assert len(positions) == 28
        for Q in positions:
            evidence.append({"Q":list(Q),"B":17,"H8":list(lab),
                             "min_H9H9H8_added":min_cost,
                             "lower_bound_total":76+min_cost})
    assert len(evidence) == 112
    return {"id":profile["profile_id"],"exact_groups":len(groups),
            "positions":len(evidence),"all_min":18,"all_native_cost_lower_bound":94,
            "cases":sorted(evidence,key=lambda r:r["Q"])}

if __name__=="__main__":
    report={"schema":"EC49FHG_EXACT_TRIPLE_V1","frozen_pin":PIN,"catalog":catalog_count,
            "profiles":[evaluate(profile) for profile in W["profiles"]]}
    assert [x["positions"] for x in report["profiles"]] == [112,112]
    (HERE/"EXACT_REPORT_EC49FHG.json").write_text(json.dumps(report,indent=2)+"\n")
    print("EC49FHG_EXACT_PASS",[(x["id"],x["positions"]) for x in report["profiles"]])
