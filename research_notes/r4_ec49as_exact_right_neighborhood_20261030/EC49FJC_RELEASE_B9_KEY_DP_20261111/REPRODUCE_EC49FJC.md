# EC49FJC reproduction and exact certificate audit

Scope: frozen BRC pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; A/B original 94-prefix seven-key witnesses, six selected paths, released complete keys, fixed-prefix cost 84 (increment budget 9).

Download to one working directory:
1. `EC49FGW_RADIUS5_SCREEN.py` and `EC49FGJ_SEVEN_KEY_94_WITNESSES.json` from `research_notes/r4_ec49as_exact_right_neighborhood_20261030/EC49FGW_RADIUS5_EXACT_SCREENS_20261110/` at immutable ancestor `f1cfadff6d9949c5278195f0b3f5f0f39a42531d`.
2. This directory's `VERIFY_EC49FJC.py.gz.b64`, `ec49fjc_shared.py.gz.b64`, and `EXACT_REPORT_EC49FJC.json.gz.b64`.

Decode with:
```bash
base64 -d VERIFY_EC49FJC.py.gz.b64 | gzip -d > EC49FJC_KEY_DP.py
base64 -d ec49fjc_shared.py.gz.b64 | gzip -d > ec49fjc_shared.py
base64 -d EXACT_REPORT_EC49FJC.json.gz.b64 | gzip -d > EXACT_REPORT_EC49FJC.json
sha256sum EC49FJC_KEY_DP.py ec49fjc_shared.py EXACT_REPORT_EC49FJC.json
```

Expected original-byte SHA256:
- `EC49FJC_KEY_DP.py`: `0ee7c003e200ecea956654b491fb6f665a7720dd45f149d327f0c6f8eb1afedd` (2,858 bytes).
- `ec49fjc_shared.py`: `6a5c96235632a27005fa10637b1573e236cb1c1d3bee316e288b6eaa1eee0f0d` (3,658 bytes).
- `EXACT_REPORT_EC49FJC.json`: `cb528b25f44ed549bd0d724998747857d2136de16694add918ff0e0d83cef09d` (239,269 bytes).

The decoded `EC49FJC_KEY_DP.py` imports the two frozen inputs via `ec49fjc_shared.py`; it runs the exact six-requirement DP for both witness profiles. The historical executable source writes its output to an absolute working path; change this output path to your working directory when running on a different host. Full two-profile rerun may need process batching as author used 8 cases at a time; all 16 executed batch outputs are retained in the local handoff archive.

For a lightweight audit of the published complete JSON report (not a new independent run):
```python
import json
r = json.load(open("EXACT_REPORT_EC49FJC.json"))
assert r["frozen_pin"] == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
assert len(r["profiles"]) == 2
for p in r["profiles"]:
    assert p["count"] == 64
    assert len(p["rows"]) == 64
    assert all(row["status"] == "EXCLUDED_EXACT_KEY_PREFIX"
               and row["final_states"] == 0
               and row["rounds"][-1]["states"] == 0
               for row in p["rows"])
print("EC49FJC_EXACT_REPORT_STRUCTURE_PASS", 128)
```

The mathematical exclusion comes from the exhaustive complete-key and native-prefix dynamic-programming transition and the catalog/witness coverage, not from these report-format assertions alone. This is author-side finite evidence; independent Driver semantic review remains pending.
