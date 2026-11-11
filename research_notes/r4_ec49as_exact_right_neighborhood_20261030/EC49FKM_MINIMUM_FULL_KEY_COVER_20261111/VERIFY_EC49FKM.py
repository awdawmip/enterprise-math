#!/usr/bin/env python3
"""EC49FKM: exact complete raw-key incidence proof in frozen native BRC/X6 catalogue."""
import collections
import itertools
import json
import os
import sys
from pathlib import Path
P = Path(__file__).resolve().parent
D = Path(os.environ.get("EC49FKM_INPUT_DIR", P.parent / "EC49FJD_RELEASE_B11_COMPLETE_20261111"))
sys.path.insert(0, str(D))
import EC49FGW_RADIUS5_SCREEN as g

PIN = "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
assert g.PIN == PIN
LABELS = sorted((h, s) for h, ss in g.REQ.items() for s in ss)
LAB_INDEX = {lab: i for i, lab in enumerate(LABELS)}
SENTINELS = [(2, 16), (2, 32), (3, 16), (4, 1), (7, 1)]
K0 = {(2,1,1), (3,0,1), (3,1,1)}
U = {(3,3,1), (4,2,1), (5,1,1), (5,1,2)}
V = {(5,5,1), (6,4,1), (7,3,1), (7,3,2)}
EXPECTED = {frozenset(K0 | {u,v}) for u in U for v in V}
WITNESS = {
    (2,16):"fe",(2,32):"ge",(3,16):"feg",(3,32):"gef",
    (4,1):"gedg",(4,2):"edgg",(4,4):"cegg",(4,8):"gecg",
    (5,16):"feggg",(5,32):"gefgg",
    (6,1):"geddgd",(6,2):"eddggd",(6,4):"ceggcc",(6,8):"gecgcc",
    (7,1):"geddggf",(7,2):"eddgggf",(7,4):"ceggcfg",(7,8):"gecgcfg",
    (8,1):"gefggfgd",(8,2):"fegggfgd",(8,4):"fegggfgc",(8,8):"gefggfgc",
    (9,16):"fegggfgfg",(9,32):"gefggfgfg"
}

def main():
    masks = collections.defaultdict(int)
    word_count = 0
    for lab, word in g.all_words():
        masks[g.raw_key(word)] |= 1 << LAB_INDEX[lab]
        word_count += 1
    assert word_count == 178850 and len(masks) == 94 and len(LABELS) == 24
    assert len(set(masks.values())) == 21
    families = [[k for k, m in masks.items() if m & (1 << LAB_INDEX[lab])]
                for lab in SENTINELS]
    assert [len(f) for f in families] == [1,1,2,7,34]
    assert all(set(families[i]).isdisjoint(families[j])
               for i in range(5) for j in range(i+1,5))
    full_mask = (1 << 24) - 1
    solutions = set()
    tries = 0
    for combination in itertools.product(*families):
        tries += 1
        union = 0
        for k in combination:
            union |= masks[k]
        if union == full_mask:
            solutions.add(frozenset(combination))
    assert tries == 476
    assert solutions == EXPECTED and len(solutions) == 16
    # Independently check all signed ordered steps, full raw keys and every label
    assert set(WITNESS) == set(LABELS)
    prefixes = set()
    actual_keys = set()
    for lab, word in WITNESS.items():
        assert len(word) == lab[0]
        q = 0
        pos = [0]*6
        for char in word:
            q = g.T[q][g.OPS.index(char)]
            assert q != 8
            for step in g.STEPS[char]:
                pos[abs(step)-1] += 1 if step > 0 else -1
        assert pos == [2,0,0,0,0,0] and g.SIG[q] == lab[1]
        actual_keys.add(g.raw_key(word))
        prefixes.update(g.pref(word))
    assert actual_keys == K0 | {(3,3,1),(5,5,1)}
    assert len(prefixes) == 136
    print("EC49FKM_EXACT_PASS", word_count, len(masks),
          "5-key solutions",len(solutions),"native-prefix witness",len(prefixes))

if __name__ == "__main__":
    main()
