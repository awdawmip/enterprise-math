"""Independent tuple-valued signed-native prefix crosscheck for EC49FCC.
Requires the regenerated FULL_REPORT_EC49FCC.json.
Six samples span all six early-slot-pair horizon classes.
"""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] /
                       "EC49FBY_COMPLETE_TRIPLE_RIGIDITY"))
from VERIFY_EC49FBY import W, STEPS, observe, candidates

HERE = Path(__file__).resolve().parent
SELECTED = (
    ("4:1", "4:2", "7:8", "8:1"),
    ("4:2", "5:16", "7:1", "8:1"),
    ("4:1", "6:1", "7:2", "8:1"),
    ("5:16", "5:32", "7:1", "8:1"),
    ("5:16", "6:1", "7:2", "8:1"),
    ("6:1", "6:2", "7:4", "8:1"),
)


def native_prefixes(w):
    seq = tuple(step for op in w for step in STEPS[op])
    return frozenset(seq[:k] for k in range(1, len(seq) + 1))


def run():
    report = json.loads((HERE / "FULL_REPORT_EC49FCC.json").read_text())
    rows = {tuple(r["slots"]): r for r in report["per_group"]}
    chosen = {f"{h}:{observe(w)}": w for h, words in W.items()
              for w in words}
    pools = {f"{h}:{sig}": words for h in range(4, 10)
             for sig, words in candidates(h).items()}
    pref = {w: native_prefixes(w) for w in set(chosen.values()) |
            {w for group in pools.values() for w in group}}
    assert len(set().union(*(pref[w] for w in chosen.values()))) == 158
    evidence = []
    for slots in SELECTED:
        fixed = frozenset().union(*(pref[w] for key, w in chosen.items()
                                    if key not in slots))
        cutoff = 158 - len(fixed)
        arrays = [{pref[w] - fixed for w in pools[key]
                   if len(pref[w] - fixed) < cutoff} for key in slots]
        arrays.sort(key=len)
        a, b, c, d = arrays
        checked = 0
        best = 158
        for x in a:
            for y in b:
                xy = x | y
                if len(xy) >= cutoff:
                    continue
                for z in c:
                    xyz = xy | z
                    if len(xyz) >= cutoff:
                        continue
                    for w in d:
                        checked += 1
                        best = min(best, len(fixed | xyz | w))
        r = rows[slots]
        assert best == r["minimum"] == 158
        assert checked == r["fourth_evaluations"]
        assert len(fixed) == r["base"]
        evidence.append({"slots": list(slots), "base": len(fixed),
                         "fourth_evaluations": checked, "minimum": best})
    (HERE / "TUPLE_CHECK_REPORT_EC49FCC.json").write_text(
        json.dumps({"status": "PASS", "rows": evidence}, indent=2) + "\n")
    print("PASS independent signed integer tuple prefixes", len(evidence))


if __name__ == "__main__":
    run()
