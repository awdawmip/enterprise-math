# X6 LP028/R063 — exact three-level signed trace-fiber theorem and located downstream consumer (2026-11-12)

**Evidence status:** AUTHOR_PROVED / EXACT_INTEGER_CHECK_EXECUTED / NONBLIND / UNREVIEWED / NOT_ADMITTED / PORTABLE_RESEARCH_ONLY. Author: current ChatGPT TASK_RESEARCH working context; no other Researcher/Driver identity or authenticated CLAIM is asserted.

**Mother task:** `RS-X6-LEGACY-PLANE-RECONCILIATION`; immutable publication `TP2-B4A441B23DA3159232C2`; objective `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. Preserve scientific pin `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03` and historical comparison pin `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Current P000 V5: signed six-axis affine Cell torsor, internal six-axis sum-of-squares metric, no native two-dimensional plane. The construction below selects **one ordered pair** of signed X6 native axes, fixing the other four *relative displacement* components to zero; it is a restriction in X6.

## 1. Exact, previously unlocated R063 downstream consumer

An exact historical and still-main-visible consumer is:

- `research_notes/TOOL_DISCOVERY_NATIVE_GEOMETRY_OF_NUMBERS_MINIMA_CALCULUS_RESULT_20260822.md`, Git blob SHA1 `e3b1488a9bfdc44795f5d0e78c67e8c128bd30dc`, §10 (lines ~340–397). This is the existing tool-discovery Result of `RS-TD-GON-NATIVE-GEOMETRY-OF-NUMBERS-MINIMA-CALCULUS`, not a newly published X6 Result. Its §10 directly invokes `PathSqrt_E(r²)`, `GRoot_E(r²)`, `Lambda(a,b)`, and computes the `N=2500` positive-component-trace quotient with six component labels and `110695538274255714208` positive words. Its §9 uses positive `(a,b,0)` sector-local bodies. The same blob was read at the historical pin and current main.
- `definitions/ENTERPRISE_PATH_VALUED_SQUARE_ROOT_OPERATOR_20260821.md`, current blob `61f23f2bcf965aa21d093ae3e35c0d6cb70610b7`, remains `ACTIVE / CANONICAL / FROZEN` and explicitly defines `GRoot_E` as **ordered nonnegative** component roots and `Lambda(a,b)` as positive-generator words.
- `experiments/tool_discovery_native_geometry_of_numbers_minima_calculus_20260822.py`, current blob `643b2bac659a445891dcb5588b647972977104e0`, checks the inherited positive-sector calculation. It is source provenance, not evidence of a new signed-native test.

This source establishes a **specific R063 downstream caller**, closing that *caller-identification* question. The old tool note's 2026-08-22 positive-only "current plane" Foundation framing is dated historical context; the exact §10 trace-fiber result survives as a typed **positive-sector observer**. It does not supply a currently authenticated call in which that result is miscast as the full signed X6 shell. LP028 status for this edge: `PRESERVE_OBSERVER / TYPE_BOUNDARY`; `BROKEN_CURRENT_CONSUMER` remains unproved.

## 2. New exact signed two-axis fiber composition

Fix positive integer `r`. Define the ordered nonnegative roots and the signed fixed-pair shell:

```
P_r = {(a,b) in Z_{>=0}² : a²+b²=r²},
E_r = {(x,y) in Z² : x²+y²=r²}.
```

For every `(x,y) in E_r`, let `L(x,y)` be its **unweighted ordered shortest signed primitive words** in the two fixed axes, with the other four relative components zero. Signed axis choices for a nonzero coordinate are consistent throughout one shortest word. Write `W_r = disjoint_union_{e in E_r} L(e)`.

There are two exact surjections and their composite:

```
W_r --endpoint--> E_r --abs--> P_r.
```

Put `w(a,b)=2^[a>0] 2^[b>0]` and `B(a,b)=binom(a+b,a)`. Then

```
|abs^{-1}(a,b)| = w(a,b)
|endpoint^{-1}(x,y)| = B(|x|,|y|)
|(abs o endpoint)^{-1}(a,b)| = w(a,b) B(a,b)

|E_r| = sum_{(a,b) in P_r} w(a,b)
|W_r| = sum_{(a,b) in P_r} w(a,b) B(a,b).
```

**Proof.** Each positive coordinate has two signs, whereas zero has one. Taking absolute values recovers a unique ordered nonnegative pair, so the sign fibers partition `E_r`. The shortest word length to `(x,y)` is `|x|+|y|` by signed native step minimality, and its ordered axis-interleavings are `binom(|x|+|y|,|x|)`. Disjoint union and fiberwise multiplication yield every identity. QED.

**Scoped information sufficiency.** For the universal class of functions of the label `(a,b)`, one representative per nonempty positive-component-trace fiber is necessary and sufficient; the exact pushforward **sum** on that label needs multiplicity `w(a,b) B(a,b)`. For the universal class of signed-endpoint functions, one representative per signed endpoint is necessary and sufficient, with weight `B(|x|,|y|)`. General ordered-path observables require an equivalence certificate on their actual path fibers. Minimality for the universal label-function classes follows by testing the indicator of each label; omitting any label changes its indicator readout. The two quotients describe different observer languages, preserving the ordered-path and sign residual when needed.

For any positive-sector observable `f(a,b)`, the *signed* weighted word sum is precisely
```
sum_{word in W_r} f(abs(endpoint(word)))
 = sum_{(a,b) in P_r} w(a,b) B(a,b) f(a,b).
```
For a signed-endpoint observable `g(x,y)`, use `sum_{(x,y) in E_r} B(|x|,|y|) g(x,y)`. This is a precise type-safe composition of the inherited R063 positive roots, the signed X6 endpoint lift, and the existing finite-fiber calculus; no change to their originals is required.

## 3. Exact `r=50` certificate and discriminating observer

The inherited ordered positive roots are
`(0,50), (14,48), (30,40), (40,30), (48,14), (50,0)`.

The original positive-sector words remain exactly `110695538274255714208`. The signed fixed-pair lift has **20** signed endpoints and **442782153097022856828** shortest words. The two exact finite-fiber collision defects are

```
delta_signed_endpoint = |W_50|-|E_50|
                      = 442782153097022856808
delta_positive_trace  = |W_50|-|P_50|
                      = 442782153097022856822
extra signed labels   = |E_50|-|P_50| = 14.
```

A concrete sign-sensitive test is `g(x,y)=1[x<0]`. Its full shortest-word weighted value is **221391076548511428413**. The positive-component-trace alone cannot evaluate it, as `(14,48)` and `(-14,48)` have the same absolute trace and opposite `g`. Sign-lift or a retained signed endpoint is therefore a necessary part of this observer's interface.

Companion checker `research_checks/X6_R063_TYPED_TRACE_FIBERS_AND_CONSUMER_20261112_ONHOUR.py` enumerates both root sets independently and uses exact Python integers for every `1<=r<=128`, checking the signed cardinality, two pushforwards and a sign-sensitive witness. Executed locally on 2026-11-12: **EXACT_INTEGER_CHECKS_PASS (128 radii)**. The all-`r` identities have the combinatorial proof above; the finite execution checks the implementation.

## 4. Additional source audit: 14 new exact historical research-note readbacks

At frozen old commit `fd2bcff10ca6e147348b6c1236027fc0d2877df3`, the prior research audited all 72 `definitions/` blobs and 24 X6/R059D/SIX_AXIS `research_notes/` blobs. This turn additionally fetched these **14 distinct** historical research-note bodies (each verified by connected GitHub read):

| File (under `research_notes/`) | Blob SHA1 |
| --- | --- |
| `BRC_PURE_ALGEBRA_COLLAPSE_CREDIT_COORDINATE_TRANSFER_ANCHOR_20260816.md` | `e5821dcaa6d8a46e7ff166a8f2823b147adcc69e` |
| `DIAGONAL_GAUGE_DERIVED_DISPLACEMENT_THEOREM_PACKAGE_20260826.md` | `609334fa07dac0c9485f806c12bda2f8f9af9680` |
| `VIETE_NATIVE_TRACE_ORIENTATION_QUOTIENT_OBSTRUCTION_20260903.md` | `290fdafd1751b43e31245a666bc2ed04cec6fd20` |
| `VIETE_NATIVE_DIRECTION_DECK_SHEET_SOURCE_NOGO_20260904.md` | `bf7624a468c35b808b21e59fa8a2119a4e941241` |
| `VIETE_DIRECTION_SHEET_SWEEP_CHIRALITY_V4_CORRECTION_20260904.md` | `8bfe58a1a50a937e85911bbef0b61859de058105` |
| `VIETE_PIVOT_LOCAL_TRANSLATION_QUOTIENT_C12_20260905.md` | `a0f14086e65b877d3d4cc4039be8223037d72593` |
| `VIETE_T11_PATH_TORSOR_FIXED_RADIUS_ROTATION_NOGO_20260903.md` | `704402c999f8e9002e62e44a6d6227d6a41b55af` |
| `VIETE_ORIENTATION_TORSOR_BRANCH_COVER_CELL_MEMORY_20260903.md` | `6d79dd1aa47fa6da7f637dc90224d2e43f857dd6` |
| `VIETE_V4_OBSERVER_QUOTIENT_AGM_BRIDGE_20260904.md` | `e664a5d4291710c3b326eb63883d47f536152878` |
| `VIETE_Z2_UNIT_CHARACTER_GAUGE_PRINCIPAL_ROOT_RIGIDITY_20260904.md` | `06c0673423ebe8be7593095396ff89a428d7eb63` |
| `VIETE_C3_TO_C6_BINARY_COVER_HOLONOMY_BIT_20260903.md` | `d256569c0f01a1ed043c36841d1bbfcfce68cfdf` |
| `VIETE_C6_MINIMAL_WINDING_PARITY_MEMORY_20260904.md` | `74213a9102d6305a94d150731a777bd72ed3c0fe` |
| `VIETE_FIRST_PHYSICAL_LAYER_HOLONOMY_GATE_ROOT_CLOSURE_20260905.md` | `8edec603d54f81e5364cd42e8049860f2f3e2887` |
| `TOOL_DISCOVERY_NATIVE_GEOMETRY_OF_NUMBERS_MINIMA_CALCULUS_RESULT_20260822.md` | `e3b1488a9bfdc44795f5d0e78c67e8c128bd30dc` |

The `DIAGONAL_GAUGE...` line 75 `M=max(A,B,C)` is the derived observer inverse; the `BRC_PURE_ALGEBRA...` line 12 says `endpoint argmax` only in an exclusion. Neither is a proven LP011 original native signed dominant-axis selector. The old `research_notes/` tree contains 230 direct blobs, of which **38 have now been read** in the specified two audit tranches. This is a bounded source census, not a repository-wide caller absence claim.

## 5. Exact continuation

**Preserve/do not repeat:** native signed X6 frozen baseline, pre-existing 72/111 shell/disk proofs, 28-row ledger, the 72 old definition readbacks, the 24+14 checked research-note files, LP011 chamber/median reconstruction, R063 positive proof and prior signed fixed-pair lift. Existing review `HIRR-1C60C7CCFAE8636E82F43A76=REQUEST_REVISION` persists.

**Smallest unresolved scientific work:** trace the actual current active consumer path from the positive-sector geometry-of-numbers tool result into any present signed-X6 execution or theorem-facing assertion. Build a source-line dependency row per affected LP ledger claim. Continue auditing remaining old research notes by semantic clusters, without reclassifying the two derived `M=max` inverses.

**Control:** Old GitHub Chat continuation issue `awdawmip/kimi-query-bridge#6827`, original request `onhour-research-20261112-0422-x6-continuation-v1`, SUCCEEDED / HANDOFF_READY / execution_authorized=false. Initial ordinary prepare `#6826` failed with `TYPED_CONTINUATION_REQUIRED_FOR_PREDECESSOR`. This lane's read-only status request `onhour-research-20261112-0907-status-v1` in `#6843` returned SUCCEEDED and identified the existing Research-only session, but no current winning CLAIM/open. Pending step: verify exact typed continuation evidence and authorize own legitimate `continuation_prepare -> claim -> open`; until then this research note is a GitHub scientific artifact and not a native semantic checkpoint or Result. Maintenance conversation never used.

**Review:** AUTHOR_PROVED / UNREVIEWED / NOT_ADMITTED, source-exposed (NONBLIND); the numeric checker is an executable finite certificate, not an independent review.
