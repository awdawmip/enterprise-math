"""R5 f=8: exact exhaustive restricted-six-state sweep. Compile VERIFY_SIX.cpp first."""
import collections
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TABLE = ROOT / "EXACT_R5_ALL_101_BUDGETS.json"
EXPECTED_TABLE_SHA = "50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
H0 = (18, 24, 82, 34, 17)
LEFT = 25845652773852463277015040000

def maximal_supports(centers, width):
    value_mask = {}
    for i, c in enumerate(centers):
        value_mask[c] = value_mask.get(c, 0) | (1 << i)
    candidates = set()
    for c in value_mask:
        support = 0
        for v, bits in value_mask.items():
            if c <= v <= c + width:
                support |= bits
        candidates.add(support)
    return tuple(sorted(a for a in candidates
                        if not any(a != b and (a & b) == a for b in candidates)))

def main():
    assert hashlib.sha256(TABLE.read_bytes()).hexdigest() == EXPECTED_TABLE_SHA
    table = json.loads(TABLE.read_text())["counts_and_cohorts"]
    assert set(map(int, table)) == set(range(214, 315))
    assert all(len(row["counts"]) == 256 for row in table.values())
    binary = ROOT / "verify_six"
    if not binary.is_file():
        raise RuntimeError("Compile: g++ -O3 -DNDEBUG -std=c++17 VERIFY_SIX.cpp -o verify_six")
    rows = []
    action_file = ROOT / "six_extension_actions_tmp.txt"
    for h in range(256):
        if h in H0:
            continue
        H = H0 + (h,)
        cheapest = {}
        for k in range(214, 315):
            counts = table[str(k)]["counts"]
            family = maximal_supports(tuple(int(counts[q]) for q in H), LEFT)
            cheapest.setdefault(family, k)
        action_lines = [f"6 {len(cheapest)}"]
        for fam, k in sorted(cheapest.items(), key=lambda pair: pair[1]):
            action_lines.append(f"{k} {len(fam)} " + " ".join(map(str, fam)))
        action_file.write_text("\n".join(action_lines) + "\n")
        proc = subprocess.run([str(binary), str(action_file), "8"],
                              capture_output=True, text=True, check=True)
        parsed = dict(token.split("=", 1) for token in proc.stdout.split() if "=" in token)
        rows.append({"sixth_h": h, "cost": int(parsed["V"]),
                     "states": int(parsed["states"]), "family_count": len(cheapest)})
    assert len(rows) == 251
    assert set(row["cost"] for row in rows) == {8335}
    assert (min(row["states"] for row in rows), max(row["states"] for row in rows)) == (39312, 258748)
    assert sum(row["states"] for row in rows) == 28297865
    assert dict(collections.Counter(row["family_count"] for row in rows)) == {8: 192, 7: 59}
    digest = hashlib.sha256(",".join(
        f"{r['sixth_h']}:{r['cost']}:{r['states']}:{r['family_count']}" for r in rows
    ).encode()).hexdigest()
    assert digest == "c57bbe5837a4161fdd654060b5f2a07ed80bfa9b8d8354337fee4277f32410d0"
    result = {"scope": "R5_256_mask_f8_all_six_subsets_extending_H0",
              "H0": H0, "L": LEFT, "n": len(rows), "output": rows,
              "distribution": dict(collections.Counter(row["cost"] for row in rows))}
    output = ROOT / "six_sweep_results.json"
    output.write_text(json.dumps(result, indent=2))
    assert hashlib.sha256(output.read_bytes()).hexdigest() == (
        "57be8a7aeab470efd7c7e72aafb3d473ff93c5bec83f4b48b31cd5afad6b411e")
    print("PASS_R5_F8_ALL_251_SIX_MASK_EXTENSIONS_LEFT=8335",
          "rows=251", "states_total=28297865")

if __name__ == "__main__":
    main()
