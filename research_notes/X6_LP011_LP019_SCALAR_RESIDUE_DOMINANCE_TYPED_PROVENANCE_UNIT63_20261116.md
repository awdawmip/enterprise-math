# X6 / LP019 and LP011 — first historical pure-algebra signed-residue primitive certificate (unit 63)

Date: 2026-11-16 (Asia/Hong_Kong). TASK_RESEARCH parent `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`; Research lane `chatgpt-research-onhour-enterprise-math-20260923` only. Frozen scientific comparison: X6 P000 V5 at `59538f585d037d09ef687b28715c4bc1a3f9fe03` and pre-rebase historical corpus `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.

## Previously unconsumed exact historical source and type distinction

1. Pre-rebase `research_notes/BRC_PURE_ALGEBRA_COLLAPSE_CREDIT_COORDINATE_TRANSFER_ANCHOR_20260816.md`, Git blob `e5821dcaa6d8a46e7ff166a8f2823b147adcc69e`, **lines 8–12**: its collapse is the scalar branch `5 -> 4` or `5 -> 9`, explicitly **not** path merging or endpoint argmax. **Lines 14–30** specify `L=k^p`, `U=(k+1)^p`, `G=U-L`, `C_p(n)=L+Gb`, and signed scalar residual `rho=n-C_p(n)=d-Gb`. **Lines 32–46** describe a separate affine three-coordinate compensation *hypothesis*. **Lines 89–93** identify this as a non-admitted research hypothesis and historical routing restriction, not an operative X6 primitive.
2. Pre-rebase `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md`, blob `6ec0d73a19e28ec586c59a97d24f5798c9119771`, **lines 29–33**, **63–93**, **140–154**: Boolean support, path-formal and natural `N`-BRC witness multiplicity are distinguished, with no signed/amplitude cancellation in the natural carrier. This is the actual archived typing relevant to LP019.
3. Pre-rebase `research_notes/BRC_DOMINANT_DEGENERACY_QUOTIENT_20260903.md`, blob `b5e20704c3cfaf095b9724685b1b274ca9c3b22e`, **lines 10–34** and **229–244**: `dominant` selects a **maximum positive rational branch weight**, counts ties and supports path-power semiring composition. It is not a selector of a signed X6 spatial axis; therefore this occurrence is a typed **LP011 false positive**, not the requested wrong native singleton-argmax caller.
4. Pre-rebase `definitions/ENTERPRISE_COORDINATE_SYSTEM_AND_BRC_BRIDGE_20260816.md`, blob `82c8877888f8da43a85eb8148b0d0d47a9e59d42`, **lines 3–17, 30–52**: the earlier signed-origin-one / six-direction ontology is expressly marked `SUPERSEDED / HISTORICAL_PROVENANCE`. The related `definitions/ENTERPRISE_SIGNED_ORIGIN_ONE_COORDINATE_20260817.md`, blob `aefe07dd26b783bf8928e3b1a525e2cd109fb43f`, **lines 9–15, 29–44** likewise prohibits promoting its retired origin/negative-axis ontology. Neither historical warning supplies an executable incorrect modern consumer.

## Unit 63 exact algebraic result (typed old scalar collapse, not native Cell)

For integers `p>=2`, `k>=1`, let `L=k^p`, `U=(k+1)^p`, `G=U-L`, `n=L+d`, and `0<d<G`. The two scalar collapse residuals are `rho_0=d` and `rho_1=d-G<0`. Define `g=gcd(d,G)`. All nonzero nonnegative integer pairs `(u,v)` satisfying `u rho_0+v rho_1=0` are exactly

```
(u,v)=m*((G-d)/g,d/g),  m in positive integers.
```

Thus the unique primitive positive integer cancellation carrier has **total natural multiplicity `u+v=G/g>0`**, with the exact signed contributions `(d(G-d)/g,-d(G-d)/g)`. This is a classification of two-branch **signed residual weighted aggregation**; it does **not** make the natural path-count sum equal zero.

**Proof:** `ud=v(G-d)`. Because `gcd(d/g,(G-d)/g)=1`, Euclid's lemma forces `u=m(G-d)/g` and `v=md/g`. These satisfy the identity. There is exactly one primitive pair (`m=1`). The derivation uses exact integers; no probabilistic amplitude interpretation.

**Loss-of-provenance witness:** for `p=2,k=2,G=5`, `n=5` has primitive multiplicities `(4,1)`, residuals `(1,-4)`, contributions `(4,-4)`; `n=6` has primitive multiplicities `(3,2)`, residuals `(2,-3)`, contributions `(6,-6)`. Both have positive total `5` and signed total `0`, but a future lower-branch-only read distinguishes contributions `4` versus `6`. Thus total positive `N` mass alone does not preserve branchwise signed-residual behavior. The joint typed carrier `(p,k,d,b,coefficient,residual)` is retained.

This proves a strictly scoped algebraic property suggested by the historical document. It does not prove that any historical developer actually subtracted positive native N-BRC path multiplicities, nor does it alter the P000 six-axis signed Cell model.

## Exact executed check and provenance

Executed `research_checks/X6_LP019_SIGNED_RESIDUE_PRIMITIVE_UNIT63_20261116.py` in ordinary CPython and `-O`: matching JSON outputs, 0 failures. **29,394** interior inputs in the complete declared ranges `(p,kmax)=(2,20),(3,12),(4,9),(5,6)`; all exact integer `gcd`, primitive pair, signed cancellation and positive-total equalities pass. Result: `research_checks/X6_LP019_SIGNED_RESIDUE_PRIMITIVE_UNIT63_RESULTS_20261116.json`. Local checker SHA256 `3e519dbd26890e34d474f72ab5920829574d09e9e3d50896995de414201c3933`; certificate SHA256 `85530e6bac4b789f7bb5443169318cf94e0ecc88a4c36eb4d8fd16f58dbcc994`. These finite tests are independent corroboration of the all-parameter Euclidean proof.

**Disposition:** `LP019 = KEEP_SIGNED_SCALAR_RESIDUE_AS_DISTINCT_TYPED_CARRIER; KEEP_POSITIVE_N_BRC; SPECIFIC_WRONG_HISTORICAL_NATIVE_CALLER_UNRESOLVED`. `LP011 = HISTORICAL_POSITIVE_WEIGHT_DOMINANT_NOTE_EXCLUDED_FROM_NATIVE_ARGMAX_CALLER; SPECIFIC_WRONG_HISTORICAL_NATIVE_CALLER_UNRESOLVED`. The remaining 28-LP actual consumer graph and independent Driver `REQUEST_REVISION` still require their own evidence. Do not repeat R063 or original Helly experiments; retain unit62 frozen-native +4 checkpoint as completed.

Author-side `EXACT_PROVED / BOUNDED_EXECUTED / UNREVIEWED / NOT_ADMITTED`. Formal Native Source and independent review require their own authenticated receipts.
