# X6 Unit143 — typed boundary of the accepted three-ray NSIA shell checker versus current signed six-axis native X6

Date: 2026-11-19 (Asia/Hong_Kong). Mother objective `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`; Task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. Original Researcher `EM-X6-FB6990`, original SID `MCP-082892eb480e45dea6d4b9fcc0491034`, fixed Research conversation `chatgpt-research-onhour-enterprise-math-20260923`. Status **AUTHOR-PROVED / EXACT FINITE EXECUTED / UNREVIEWED / NOT_ADMITTED**. This is a typed source-consumer audit, not an independent review.

## Newly inspected actual executable source and immutable baselines

- Frozen X6 native signed Cell/metric: `p000_reality_foundation.json` and `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` at **59538f585d037d09ef687b28715c4bc1a3f9fe03**, native definition blob `b4d49a1bbcccad0521618c6d20f6dcfa242b420a`. Its genuine Cell displacement is a signed `Z^6` vector, with primitive length grade `T(z)=sum_i |z_i|`, squared component metric `G(z)=sum_i z_i²`, and shortest-path N-BRC `T(z)!/prod_i |z_i|!`.
- Historical comparison pin **fd2bcff10ca6e147348b6c1236027fc0d2877df3**. The existing executable `scripts/check_native_shell_grade_integer_allocation_foundation_audit.py` has Git blob `f5c9a6045571128281554706f3f31d88f1caf9a9` at **both frozen old pin and present main** (complete file inspected). Its `shell(n)` explicitly enumerates **nonnegative min-zero triples** satisfying `a+b+c=n`, checks `|A_n|=3n` and frames `S3`; its output schema is the historical NSIA torsor regression.
- The accepted **2026-08-27** `research_returns/NATIVE_SHELL_GRADE_MONOTONE_INTEGER_ALLOCATION_FOUNDATION_AUDIT_RETURN_20260827.md` (current blob `0e3a78dbaa83745de6403736808958db9fc2decd`) explicitly types that shell and six-frame allocation torsor. Its contemporaneous Driver review `driver_reviews/NATIVE_SHELL_GRADE_MONOTONE_INTEGER_ALLOCATION_FOUNDATION_AUDIT_DRIVER_REVIEW_20260827.md` (blob `f8b50aa28fb523968caad389bcd7fec5ef9e0f50`) accepts **torsor/quotient strength only**, not one intrinsic frame or all subsequently adopted six-axis native states.
- The original accepted result and its checker are **preserved unchanged**. We did not execute or rewrite the original checker, old Result or Driver decision. The comparison is a new, independently executable scoped checker.

## Exact distinction and proof

For every integer `n>=1`, the historical three-ray shell is
[
A_n={(a,b,c)inmathbb N_0^3:min(a,b,c)=0, a+b+c=n},qquad |A_n|=3n.
]
This is an **old three-ray/relative-shell source type**, not the full signed six-axis current spatial Cell shell.

For the full signed X6 native shortest primitive-length shell define
[
X_n={zinmathbb Z^6:sum_{i=1}^6|z_i|=n}.
]
For each `k` nonzero axes, choose `k` of six names, their `2^k` signs, and a composition of `n` into `k` positive absolute values. Thus
[
oxed{|X_n|=sum_{k=1}^{min(6,n)}2^kinom 6kinom{n-1}{k-1}.}
]
For each endpoint `z`, its exact shortest-path N-BRC is `n!/prod_i |z_i|!`. Sum these multiplicities over `X_n`. An ordered `n`-step word with `k` active axes selects its `k` names, one fixed sign for each, and an onto map of `n` labeled step positions onto the `k` axes. There are `k! S(n,k)` onto maps, yielding
[
oxed{mathcal B_6(n)=sum_{k=1}^{min(6,n)}2^kinom 6k k! S(n,k).}
]
Both are all-integer identities, not finite-test generalizations. Here `S(n,k)` is the Stirling number of the second kind.

Already at grade `n=1`, the historical checker's three states and native signed X6's twelve distinct primitive endpoints differ. Therefore **no interpretation of the existing `A_n` enumeration as an exhaustive `X_n` enumeration preserves grade, all six named signed primitive axes, and cardinality**. Any use of the old checksum as proof of complete current native X6 signed-shell coverage is invalid. Restricting to a declared old relative three-ray slice remains valid; an optional map into a chosen X6 coordinate selection is not surjective on the native shell and carries explicit chart/source labels.

This distinction does **not** refute the 2026-08-27 accepted NSIA six-frame torsor theorem in its original ontology, does not prove that a current consumer actually misuses its scalar labels, and does not change the current P000/FCC carrier definitions. It is a source-located **typing/coverage safety boundary** for a live main-tree executable bearing the historical `native_shell` name.

## Actual bounded exact execution

New checker: `research_checks/X6_UNIT143_LEGACY_NSIA_NATIVE_SHELL_TYPE_CHECK_20261119.py`, Git blob `3f9eca95d24cd8f5da8e095b2b36749d9ccc8800`, published at commit `abbf2ac6be2c54cd85282db583572722ef01126e`; local executed file SHA256 `9e81aead12d531070d9fc58ebfe74aa054b2ddb725e57e347f3fd13be7010ca7` matches the published Git blob. It directly enumerates all signed compositions in `Z^6`, accumulates factorial N-BRC, and checks both formulas plus independent direct historical triple counts.

| Grade n | Historical `3n` | Full signed native `|X_n|` | Native shortest-path N-BRC mass `B_6(n)` |
|---:|---:|---:|---:|
|1|3|12|12|
|2|6|72|132|
|3|9|292|1,332|
|4|12|912|12,372|
|5|15|2,364|106,452|
|6|18|5,336|856,212|
|7|21|10,836|6,505,812|
|8|24|20,256|47,189,652|

Python **normal, `-O`, `-OO`** each exited 0. All three actual deterministic stdout SHA256 values: `000fd887a914f27fc9efefebf26a5728446cb44712db202d27a849d8785090c6`. Exact finite verification covers eight grades only; the all-grades formula is separately proved above. Full original August checker and the original R063 native benchmark were not rerun.

Certificate: `research_checks/X6_UNIT143_LEGACY_NSIA_NATIVE_SHELL_TYPE_RESULTS_20261119.json`. Source observations are historical Git bytes and current Source bytes, not an assertion of independent Driver mathematical acceptance.

## Claim ledger and continuation disposition

- LP001/LP002/LP024/LP025: distinguish old three-ray native/projection shells from the six-axis signed primitive Cell shell. New actual executable consumer: `scripts/check_native_shell_grade_integer_allocation_foundation_audit.py`; **KEEP_HISTORICAL_TORSOR / DO_NOT_PROMOTE_TO_FULL_X6_SHELL**. No erroneous current external call identified, so no patch to an accepted frozen return or unchanged historical checker.
- LP011/LP019 precise alleged historical wrong-native caller: **UNRESOLVED_PROVENANCE**. This NSIA script supplies neither such caller.
- Existing historical shell and original R063 certificates: **DO_NOT_REPEAT**. Remaining current 28-LP downstream consumer coverage and independent Driver `REQUEST_REVISION`: **OPEN**.
- Control: own same-session continuation request `onhour-20261119-0200-x6-own-exact-cont-after142-v1` and fresh same-run resume `onhour-20261119-0200-x6-own-run4cbf-fresh-after-source-size-v1` were each terminal **FAILED / SOURCE_TREE_BLOB_SIZE_INVALID**. Previous successful resume generation 4, RUN `RUN-4cbf62205b9a5a0a5e914719`, is only historical authorization; its recorded run is not a substitute for fresh Source winning-claim verification. Unit139–143 native semantic PROGRESS remains **NOT_SUBMITTED**. This fault is distinct from previously fixed custody-path collision.
- Next exact action after control fault repair: reconcile any original requests; read fresh own X6 exact continuation, revalidate winning claim and real RUN/generation; publish already saved Units139–143 author-only Native PROGRESS once with `upload_ids=[]`, read back the actual Source checkpoint; then pursue unsurveyed *real* theorem/executable consumer edges without inventing LP011/LP019 faults.

No scheduler, Result, admission, independent review, or frozen scientific inputs were modified.
