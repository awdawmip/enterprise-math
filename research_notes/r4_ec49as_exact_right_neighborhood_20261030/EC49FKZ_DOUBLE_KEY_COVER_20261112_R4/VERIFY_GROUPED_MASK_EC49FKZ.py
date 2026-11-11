#!/usr/bin/env python3
"""Independent exact grouped-frequency check of two-key replacement cover counts."""
import collections
import itertools
import json
import math
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/"EC49FJD_RELEASE_B11_COMPLETE_20261111"))
from EC49FGW_RADIUS5_SCREEN import PIN,all_words,raw_key

assert PIN=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
BASE={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}

def main():
    catalogue=list(all_words())
    labels=sorted({l for l,w in catalogue})
    assert len(catalogue)==178850 and len(labels)==24
    label_ids={label:i for i,label in enumerate(labels)}
    covers=collections.defaultdict(int)
    for label,word in catalogue:
        covers[raw_key(word)] |= 1<<label_ids[label]
    assert len(covers)==94
    outside=sorted(set(covers)-BASE)
    report=json.loads((HERE/"REGENERATED_EC49FKZ_COVER.json").read_text())
    total=0
    for old,row in zip(itertools.combinations(sorted(BASE),2),report["per_dropped_pair"]):
        missing=(1<<24)-1
        for key in BASE-set(old):
            missing &= ~covers[key]
        freq=collections.Counter(covers[key]&missing for key in outside)
        masks=sorted(freq)
        pairs=sum(freq[a]*freq[b] for a,b in itertools.combinations(masks,2)
                  if a|b==missing)
        pairs+=sum(math.comb(n,2) for m,n in freq.items() if m==missing)
        assert pairs==row["coverable"],(old,pairs,row["coverable"])
        total+=pairs
    assert total==6315 and 21*math.comb(87,2)-total==72246
    print("EC49FKZ_GROUPED_MASK_INDEPENDENT_PASS",len(report["per_dropped_pair"]),total,72246)

if __name__=="__main__":
    main()
