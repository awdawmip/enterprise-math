"""EC49FCC — exact 720 H7+H8 four-slot exchange search.

Run 'python VERIFY_EC49FCC.py 0 96', '96 192', ..., '672 720'.
Run 'python VERIFY_EC49FCC.py merge' after all eight chunks.
Uses only Python standard library and the immutable EC49FBY generator in its sibling dir.
"""
from pathlib import Path
from itertools import combinations, product
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] /
                       "EC49FBY_COMPLETE_TRIPLE_RIGIDITY"))
from VERIFY_EC49FBY import build

PIN = "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
BASELINE = 158
ROOT = Path(__file__).resolve().parent
REQUIRED_SUBFAMILIES = {"4+4":96, "4+5":128, "4+6":256,
                        "5+5":16, "5+6":128, "6+6":96}


def group_sets(early, late):
    seven = [k for k in late if k.startswith("7:")]
    eight = [k for k in late if k.startswith("8:")]
    groups = [tuple(E + L) for E in combinations(early, 2)
              for L in product(seven, eight)]
    assert len(groups) == 720 and len(set(groups)) == 720
    return groups


def run(start, stop):
    assert 0 <= start < stop <= 720
    chosen, early, late, pools, single = build()
    assert len(chosen) == 24 and len(early) == len(late) == 10
    groups = group_sets(early, late)[start:stop]
    rows = []
    for slots in groups:
        fixed = 0
        for key, mask in single.items():
            if key not in slots:
                fixed |= mask
        base = fixed.bit_count()
        limit = BASELINE - base
        arrays = []
        raw = 1
        for key in slots:
            raw *= len(pools[key])
            residuals = {mask & ~fixed for mask in pools[key]
                         if (mask & ~fixed).bit_count() < limit}
            arrays.append((key, tuple(sorted(residuals))))
        arrays.sort(key=lambda item: len(item[1]))
        a, b, c, d = (items for _, items in arrays)
        pair_pruned = triple_pruned = checks = 0
        minimum = BASELINE
        for x in a:
            for y in b:
                xy = x | y
                if xy.bit_count() >= limit:
                    pair_pruned += 1
                    continue
                for z in c:
                    xyz = xy | z
                    if xyz.bit_count() >= limit:
                        triple_pruned += 1
                        continue
                    for w in d:
                        checks += 1
                        minimum = min(minimum, base + (xyz | w).bit_count())
        rows.append({
            "slots": list(slots), "base": base, "limit": limit,
            "filtered_candidate_counts": [len(items) for _, items in arrays],
            "raw": raw,
            "eligible_product": len(a) * len(b) * len(c) * len(d),
            "pair_pruned": pair_pruned, "triple_pruned": triple_pruned,
            "fourth_evaluations": checks, "minimum": minimum
        })
        assert minimum == BASELINE, (slots, minimum)
    result = {"schema": "EC49FCC_CHUNK_V1", "pin": PIN,
              "source": "EC49FBY@5b10f1c296cb8826d4b69f6fd83dba89d765df1c",
              "range": [start, stop], "groups": len(rows),
              "per_group": rows}
    target = ROOT / f"REPORT_EC49FCC_{start:04d}_{stop:04d}.json"
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("PASS", start, stop, "groups", len(rows),
          "fourth", sum(x["fourth_evaluations"] for x in rows))
    return result


def merge():
    ranges = [(i, min(i + 96, 720)) for i in range(0, 720, 96)]
    rows = []
    for a, b in ranges:
        p = ROOT / f"REPORT_EC49FCC_{a:04d}_{b:04d}.json"
        v = json.loads(p.read_text(encoding="utf-8"))
        assert v["range"] == [a, b] and len(v["per_group"]) == b - a
        assert v["pin"] == PIN and all(r["minimum"] == BASELINE
                                       for r in v["per_group"])
        rows.extend(v["per_group"])
    assert len(rows) == 720 and len({tuple(r["slots"]) for r in rows}) == 720
    keys = ("raw", "eligible_product", "pair_pruned",
            "triple_pruned", "fourth_evaluations")
    sums = {k: sum(r[k] for r in rows) for k in keys}
    expected = {"raw": 411505920000,
                "eligible_product": 48517505776,
                "pair_pruned": 54820, "triple_pruned": 2904388,
                "fourth_evaluations": 5395584}
    assert sums == expected, (sums, expected)
    classes = {}
    for r in rows:
        label = "+".join(key.split(":")[0] for key in r["slots"][:2])
        classes.setdefault(label, []).append(r)
    assert {k: len(v) for k, v in classes.items()} == REQUIRED_SUBFAMILIES
    full = {"schema":"EC49FCC_ALL_720_CERTIFICATE_V1",
            "scientific_pin": PIN, "groups":720, "minimum":158,
            "aggregate": sums, "per_group": rows}
    (ROOT / "FULL_REPORT_EC49FCC.json").write_text(
        json.dumps(full, indent=2) + "\n", encoding="utf-8")
    print("PASS MERGED ALL 720", sums)


if __name__ == "__main__":
    if sys.argv[1:] == ["merge"]:
        merge()
    elif len(sys.argv) == 3:
        run(int(sys.argv[1]), int(sys.argv[2]))
    else:
        raise SystemExit("Provide start stop, or merge")
