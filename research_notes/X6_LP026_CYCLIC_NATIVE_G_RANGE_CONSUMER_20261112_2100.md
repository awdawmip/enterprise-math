# X6 LP026 — exact native norm range certificate on cyclic common-depth fibres

Date: 2026-11-12. Parent objective: `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. Candidate Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. This is **author-side portable research, UNREVIEWED / NOT_ADMITTED**. No native winning CLAIM, open, formal semantic checkpoint, Result or independent review is claimed.

## Grounding and scope

The *frozen scientific* baseline is `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03`, P000 V5, signed six-axis native Cell torsor `Z^6`. Historical comparison pin stays `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. The exact-depth interval and logarithmic search are **reused** from `research_checks/X6_LP026_CYCLIC_G_FAST_INTERVAL_RECOVERY_20261112_ONHOUR.py` (original observed Git blob `496764aa8ebdb19bb03b7d40b82128a82be0ed84`); this note claims a new **tight min/max certificate and native-versus-derived error interval**, not a new derivation of that search.

For a signed native word of **exactly N** unit steps, write its endpoint as
`z=r+h*1`, where `r in Z_>=0^6`, `min(r)=0`. The cyclic observer retains `(r, h mod m)` for `m>=1`; `m=0` retains exact integer depth. For fixed `N`, a lift `h` is reachable iff `sum_i |r_i+h| <= N` and `N-sum_i |r_i+h|` is even. Because there are six axes, the latter parity is independent of `h`. The convex first condition gives an exact closed integer interval `[L,U]` (or the empty set). It intersects a cyclic depth congruence in a finite arithmetic progression
`H={a, a+m, ..., b}` with exactly `1+(b-a)/m` elements, or the singleton `{h}` for `m=0`.

## New exact finite-fibre theorem and proof

Set `S=sum_i r_i`, `C=sum_i r_i^2`. The P000 native squared component norm at lift `h` is
`G(h)=sum_i(r_i+h)^2 = 6h^2+2S*h+C`, and the *derived section* norm is only `C`.

**Theorem.** For every valid observer key and exact word length N, one can compute the *attained* native norm range `[G_min,G_max]`, depths attaining both bounds, exact number of native lifts and the *attained signed section-error range* `[G_min-C,G_max-C]` in `O(6 log(N+1))` exact integer arithmetic operations. These are exact extrema over reachable native endpoints, not loose numerical estimates. The bound is arithmetic-operation complexity and does not suppress integer bit-cost.

**Proof.** The depth interval is obtained by the already proven convex binary search. For a finite progression `h_j=a+j*m`, `G(h_j)` is a strictly convex quadratic in `j`, with real vertex `h_*=-S/6`. Therefore its minimum is attained at the nearest progression point(s) to the vertex, clipped to the first/last allowable index; compare its integer floor index and next index without floating point. Its maximum is attained at one of the two progression endpoints, so compare only those. Every returned extremizer is a member of the exact reachability progression and hence an actual native endpoint reachable by a word of exactly length N; the resulting min/max are sharp. Subtract `C` for the exact observer-section error interval. When `m=0`, the same argument applies to the sole retained depth. QED.

This is a *typed consumer enhancement*: when `recover_native_norm_fast` signals `AmbiguousNativeNorm`, a consumer may still use a rigorous native range plus concrete lifting witnesses, without misreporting `Coord6.norm_squared()` as a uniquely recovered native norm. Native BRC remains a different operation and cannot be recovered from the native norm range; exact path mass still requires the signed-BRC kernel / fiber pushforward.

## Actual executable checks and certificates

Executable: `research_checks/X6_LP026_CYCLIC_NATIVE_G_RANGE_CERTIFICATE_20261112_2100.py`. It was executed locally with Python integers and independently compared against enumerated **native endpoint fibres**, not just against another quadratic shortcut, for all reachable signed 12-generator exact-length endpoints `N=0..8`, moduli `m=0..7`:

- **380,544** exact fibre comparisons; **PASS** for min/max, attaining depths, number of lifts and section-error interval.
- **16,536** of these state-length-modulus cases have nonconstant native G and were correctly exposed as genuine non-singleton norm ranges; maximal lift count in the tested range: 3.
- `N=6, m=1, r=(0,0,0,0,0,0), [h]=0`: attainable depths `{-1,0,1}`, native-G range **[0,6]**, three lifts. Native zero and derived section zero are not a general licence to discard depth.
- `N=9, m=3, r=(0,0,3,2,2,2), [h]=0`: two lifts `h=-3,0` and **G_min=G_max=21**. This preserves the earlier finding that equal norms still do not force equal signed-BRC endpoint counts (10,080 versus 7,560).
- `N=10^12, m=1, r=0`: exact lift count **333,333,333,333**, norm range `[0,166666666665333333333336]`, obtained without enumerating that many depth values. This is **not** a timed benchmark.

Observed executable Git blob `7e0255431adc6d8aa339c76271ecb38b8d57df2f`, locally independently checked against the exact Git blob and re-executed. Local SHA256 `88e02d96834b7bd1b2da50cec8577d006c119960c742235546360664a838b86c`.

## Source and execution boundaries / durable continuation

Current code sources were read via the authorized GitHub connector: `experiments/x6_native_coordinate_completion_v7_20260905/x6_coordinate.py` (blob `ef66285d8ae81569cbbd3195b3e38daae37944ef`); `x6_cover.py` (blob `3f7d9e62a4dd66e7888a69ff87276b283c891aac`); `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` (blob `300a96e3dc24bf6fff73743037a0347a8bc83176`). The present range checker is **self-contained** and did **not** import these original modules. Earlier source-import checks of the different native-G recovery API are already recorded. Do not replace or relabel the still-outstanding complete `check_x6_coordinate.py` original-regression rerun with this proof or its PASS.

Current verified Task state from `onhour-20261112-2100-x6-current-task`: `HANDOFF_READY / NEEDS_DISPATCH`, `REQUEST_REVISION`, no verified own winning CLAIM/open. There is no authority in a task read or this neutral GitHub evidence to assert formal task ownership. The previously referenced activity `RA-629C868A22A736334628BEFA.json` is Source-bound to SID `MCP-de3e5bafb24f43f4a5e6285e7601676a` / Researcher `EM-ENTERPRISE-9C9163`; its ownership by this scheduled on-hour logical lane is **not established**. Do not append this unit to that activity or register it under its identity without verified continuity. This artifact does not create a second native activity.

**Continuation packet** — Parent: `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`; Task/publication: as above; frozen source pin: `59538f...`; historical pin: `fd2bcf...`. Completed/reuse, **do not redo**: signed path BRC and finite cover pushforward, sharp observer thresholds, prior exact-G ambiguity/recovery tests, earlier imported-source checks, and this newly executed *norm-range* checker. Unfinished: full corrected `experiments/x6_native_coordinate_completion_v7_20260905/check_x6_coordinate.py` original regression rerun in an actual complete source checkout; LP011/LP019 exact original consumers and remaining 28-LP dependency closure; independent native review/Result handling. Next action: run that original script with exact on-main modules (including the old six-axis vendor atlas), record SHA-pinned output and failed branch if any; then amend the LP crosswalk only for source-proven consumer changes. Session/claim/open: **not verified** for this lane. Exact read requests: `onhour-20261112-2100-x6-current-task` SUCCEEDED; `onhour-20261112-2100-x6-exact-continuation` SUCCEEDED with `persisted_checkpoint=NOT_FOUND` and five historical artifacts flagged `DRAFT_OR_UNVERIFIED` because they are absent from the current immutable manifest, not a certification that the original branch data never existed. This read does not grant execution authority. Own native RESEARCHER registration request `onhour-20261112-2100-own-researcher-start-v1` remains QUEUED at the last read; service returned pending SID `MCP-082892eb480e45dea6d4b9fcc0491034` under host-managed private custody. That SID is not a verified registered identity or CLAIM/open until original completion receipt. Reconcile the same original request, never resubmit. Recovery/ownership and eventual formal checkpoint must follow the current native contract, not borrow the maintenance lane or the D24 session.

No experimental performance speedup, native admission, Result freeze or schema-execution success beyond the stated portable local check is claimed.
