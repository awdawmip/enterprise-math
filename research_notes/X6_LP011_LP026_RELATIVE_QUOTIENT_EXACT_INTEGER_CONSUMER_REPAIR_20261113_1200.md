# X6 LP011/LP026 — live diagonal quotient exact-integer input repair and original regression

Date: 2026-11-13 (Asia/Hong_Kong). Task `RS-X6-LEGACY-PLANE-RECONCILIATION` / `TP2-B4A441B23DA3159232C2`; parent `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. Author Research lane: `chatgpt-research-onhour-enterprise-math-20260923`; Researcher `EM-X6-FB6990`, session `MCP-082892eb480e45dea6d4b9fcc0491034`, own winning claim `MCP-bdd4acf9d96a8f1f0dfab4e9`, open RUN `RUN-756de85b94c23b46b181f7b8` (original open request `onhour-20261113-1222-x6-own-winning-claim-open`, SUCCEEDED). AUTHOR CHECKED / EXACT ORIGINAL SOURCE EXECUTED / UNREVIEWED / NOT_ADMITTED.

Frozen scientific baseline `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03` P000 V5, historical comparison `@fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Current Source reads used for code repairs; no scientific pin was rebased.

## Real active caller and exact defect

The reusable live `src/enterprise_math/diagonal_quotient.py` (pre-repair Git blob `3ac387c0103665943f13ba9e306a6167080c701d`) exposes the observer quotient `Z^3/Z(1,1,1)`, min-zero section, diagonal shifts and inverse/composition. Its correct module-level documentation already restricts it to *relative representation*, not a native Cell identity. The actual validation used `isinstance(v,int)` for all three coordinates and `isinstance(k,int)` for common shifts. In Python `isinstance(True,int)` is true; the public operators therefore accepted Boolean pseudo-coordinates and pseudo-depths contrary to the declared integer/signed coordinate domain.

Executed pre-repair witness against the same predicate/operation semantics:
```
canonical_min_zero((True,0,0)) = (1,0,0)
diagonal_shift((0,0,0), True) = (1,1,1)
```
The first should reject an input with non-integer coordinate *type*, and the second should reject non-integer common-depth *type*. The numerical images above are the Python coercion values, not legitimate X6 endpoints created from the declared domain. This is a located **current executable API/input-domain defect**, distinct from the historical, as-yet-unattributed LP011 wrong native-dominance caller. No evidence was found here that the mathematical quotient identities or existing signed-path BRC coefficients were wrong.

## Smallest exact current-main repair

- Replaced the coordinate predicate with `type(value) is int`; and shift predicate with `type(k) is int`, retaining the rest of the quotient group and observer operations verbatim. Immutable commit [`7079cec570074e16ed24c173b0f08ef60d3e2e37`](https://github.com/awdawmip/enterprise-math/blob/7079cec570074e16ed24c173b0f08ef60d3e2e37/src/enterprise_math/diagonal_quotient.py), Git blob `a527e347e33d0a0039258a9b25f48b1f1466d149`.
- Added six negative input-domain assertions to original consumer `scripts/diagonal_quotient_normalization_check.py`: Boolean / non-integral components and Boolean / non-integral common shifts. Immutable commit [`78bd1208202fb0e9d8106b3ba1dec19cb5dea41e`](https://github.com/awdawmip/enterprise-math/blob/78bd1208202fb0e9d8106b3ba1dec19cb5dea41e/scripts/diagonal_quotient_normalization_check.py), Git blob `095d37643b2a8aa134ed5cd91926040b90bd123a`.
- Both exact current-main blobs were independently fetched, copied into a local source layout and verified by the Git blob algorithm before executing **the original patched script**, not a replacement algorithm. Local byte-match: `a527e347e33d0a0039258a9b25f48b1f1466d149`, `095d37643b2a8aa134ed5cd91926040b90bd123a`.

## Executed original checker: PASS, exact integer coverage

Python exited 0, `status=PASS`, `failure_count=0`, output digest SHA256 `fdaea86286cff37d3e0d5e1b5687c48cc27187202617aad0510b6cbc1d66dd2d`.

| Original operation / check | Executed cases |
| --- | ---: |
| signed integer triple points in `[-4,4]^3` | 729 |
| common shifts `k=-4..4` | 6,561 |
| exact class equivalence of all ordered point pairs | 531,441 |
| quotient addition on 64 selected representatives | 4,096 |
| inverse and identity representative cases | 64 |
| explicit invalid coordinate/depth inputs rejected | 6 |

Algebraic meaning remains exact at the declared relative observer layer: `r=can3(z)`, `h=min(z)` give lossless reconstruction `z=r+h(1,1,1)`, and the kernel of `chi(a,b,c)=(a-c,b-c)` remains `Z(1,1,1)`. The successful finite regression is an implementation test; the previously established elementary algebraic proof supports the all-integer identities. The operation is not a native-Cell quotient.

## Continuation, outstanding work and provenance

Completed/not to repeat: existing P000 and signed-X6 canonical certificates, 23/23 bounded August-definition review, 11:00 R25 exact two-axis root-fibre calculation, full previous V7/Cover original regressions, and the present exact-current-blob original diagonal-quotient regression.

Remaining mother objective: complete located active/current LP consumer dependency edges beyond bounded cohorts; isolate if/where the old LP011 argmax or LP019 signed-cancellation assertions actually fed a historically wrong native caller; preserve `UNRESOLVED_PROVENANCE` until path/line evidence exists; independent Driver `REQUEST_REVISION` needs current verifiable artifacts. Next exact action: use the current indexed source/tree to inspect the caller(s) of the typed quotient and any actual native Cell or signed BRC transfer; patch only located semantic misuse.

Native Source PROGRESS for this new repair requires fresh same-lane authenticated publishing and readback; a GitHub main commit and original checker execution do not by themselves constitute Result or review admission. No mutation to P000, ACTIVE worldview, unrelated task, maintenance lane or scheduler.
