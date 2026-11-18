# EC49FJA — exact H8–H9 pair barrier in released-key B=9 six-path neighborhood (2026-11-11)

## Result (author-side exact finite claim)

The frozen nine-state, ordered signed six-axis BRC experiment is pinned by `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Reuse two 24-demand, seven-complete-cache-key, 94-distinct-native-prefix witnesses A and B from EC49FGJ.

For a six-position replacement set `Q`, let `F(Q)` be the union of all native signed prefixes of the other 18 unchanged witness words. Inspect precisely the cases where:

1. `|F(Q)|=84`, so a 93-prefix replacement has an increment budget of `9`;
2. at least one original complete raw key is released;
3. among the six changed observations there is exactly one H8 observation and exactly one H9 observation;
4. every legal completion using at most seven complete raw keys is forced to reuse *all seven* original keys. This is checked, not assumed: for each released key `k`, a complete finite key-cover DP with the other fixed keys and up to `r=7-|K_F|` new keys fails if `k` is excluded.

There are **7,080** such positions per witness (A and B), in **56 distinct fixed-prefix/key/observation backgrounds** per witness, with group-size histogram `{1:8, 12:16, 66:8, 90:8, 352:16}`. For each background, using the full legal-word catalog restricted to the forced seven keys, exhaustive exact enumeration yields

```
min_{u legal for changed H8, v legal for changed H9}
    |(P(u) union P(v)) \ F(Q)| = 10.
```

The equality is computed with paths whose individual prefix differences have size at most 9; omitted paths each cost at least 10 on their own, and the enumeration supplies a pair achieving 10. Each case therefore requires at least `84+10=94` native prefixes, while the unchanged original witness supplies a 94-prefix feasible completion. Thus **14,160 distinct six-position fixed-background subproblems have exact optimum 94**, within the frozen seven-key/24-observation model. This is not a global seven-key optimality theorem, nor independent Driver acceptance.

## Exact complete-domain counting

- The native legal-word generator enumerates **178,850** words and **94** complete raw-key types; each witness has seven keys, with **9,838** corresponding legal words.
- Each witness has **134,596** six-position choices. Exactly **7,888** release an original key and have `|F(Q)|=84`; **7,088** of those contain exactly one H8 and one H9 demand. **8** of these 7,088 per witness admit a key-cover possibility omitting some original key and are *not* included in the theorem. The remaining **7,080** per witness are all-seven-key forced.
- Across the 56 backgrounds per witness, the H8 eligible new-prefix-set counts range from **18 to 24**, and the H9 counts equal **6**; all 112 background minimum union costs equal **10**.
- Every candidate preserves native microstep order and sign; raw key means the complete original key tuple, not a collapsed endpoint.

## Reproduction and exact evidence

Canonical input files from immutable PR ancestor `f1cfadff6d9949c5278195f0b3f5f0f39a42531d`:

- `../EC49FGW_RADIUS5_EXACT_SCREENS_20261110/EC49FGW_RADIUS5_SCREEN.py`
- `../EC49FGW_RADIUS5_EXACT_SCREENS_20261110/EC49FGJ_SEVEN_KEY_94_WITNESSES.json`

The local reproduction's 48 demand words were compared with the exact remote canonical compact witness serialization; both A/B demand lists match. The remote compact serialization's Git blob is `6e54f83f9d39bf932d7f36addf4b1987ca88b077`. Source generator behavior is the frozen EC49FGW nine-state model.

In a Python standard-library environment, decode `VERIFY_EC49FJA.py.gz.b64` by `base64 -d ... | gzip -d > VERIFY_EC49FJA.py`; place it alongside the two above inputs and run `python VERIFY_EC49FJA.py`. Output includes the complete 112-group `EXACT_REPORT_EC49FJA.json`. To examine the actually executed report without rerunning, decode `EXACT_REPORT_EC49FJA.json.gz.b64` the same way.

Executed original-byte SHA256:
- `VERIFY_EC49FJA.py`: `722713722f70429f8f0df7d3479fe304e81d9f2bd826a06d8a3c81ea34bf4206` (6,175 bytes).
- `EXACT_REPORT_EC49FJA.json`: `da1025a534f4f1d4fd5f69db104eb494234770af9803765527a5687851a811e6` (71,217 bytes).

The script independently cross-checks the exhaustive pair minimum via integer-prefix-bitsets (bit_count) and ordinary set unions for each of the 112 groups. Actual output: `EC49FJA_PROFILE_EXACT_PASS A 7080 groups 56`, corresponding B line, and `EC49FJA_EXACT_PASS 14160`. The local run used 4.87 seconds, peak RSS 152,652 KB (environment-dependent, not a speed claim).

## Current status / next discriminating unit

`AUTHOR_EXACT_FINITE_COMPUTATION / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED`. This is source evidence, not a CLAIM, Result, Driver review, P000 revision or worldview change. The native research activity is `RA-3D374FF8D860D14A0A87B9FA` / `EM-DIRECT-1F534E`; this author has no active EC49AS task claim.

Next: classify the **744** remaining released B=9, forced-key positions per witness without a one-H8/one-H9 pair (660 single H8/no H9, 24 triple H8/no H9, 60 two-release/single H8/no H9), using an exact two- or three-observation bound. Separately handle the eight reallocation-possible one-H8/one-H9 positions without assuming original keys remain fixed. Retain the mother objective: determine whether a global seven-cache-key 93-native-prefix construction exists.

Contributors and provenance: previous verified author-side EC49FIY/FIZ, original EC49FGW/FGJ witnesses; present calculations and exact report are a new independent author-side increment, not mathematically independently reviewed.
