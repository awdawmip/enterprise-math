#!/usr/bin/env python3
"""Check literal signed-primitive-prefix inclusion for 6 redundant slots."""
import json
from frozen_model import W, observe, primpref

CARRIERS = {
    "2:16": ["8:2", "8:4"], "3:16": ["8:2", "8:4"], "5:16": ["8:2", "8:4"],
    "2:32": ["8:1", "8:8"], "3:32": ["8:1", "8:8"], "5:32": ["8:1", "8:8"]
}
chosen = {f"{h}:{observe(w)}": w for h, words in W.items() for w in words}
assert len(chosen) == 24
rows = []
for key, carriers in CARRIERS.items():
    source = primpref(chosen[key])
    for target in carriers:
        assert target.startswith("8:") and target in chosen
        longer = primpref(chosen[target])
        assert len(longer) > len(source) and longer[:len(source)] == source, (key, target)
    rows.append({"slot": key, "word": chosen[key], "prefix_count": len(source), "carriers": carriers})
print(json.dumps({"model_blob":"7e97065ac9a0ff70435b92ee2f4bd718c9bf1859",
                  "source_pin":"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
                  "checked_slots":len(rows),"verified_inclusions":12,"rows":rows},
                 sort_keys=True, indent=2))
