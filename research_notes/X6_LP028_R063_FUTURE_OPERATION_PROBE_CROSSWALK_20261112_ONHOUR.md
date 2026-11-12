# X6 LP028/R063 — future-operation capacity and signed endpoint recovery by two native norm probes

**Observed/published:** 2026-11-12. **Status:** AUTHOR_PROVED / EXACT_INTEGER_CHECK_EXECUTED / NONBLIND / UNREVIEWED / NOT_ADMITTED / PORTABLE_RESEARCH_ONLY. This is an additional observer-specific crosswalk, not a new Foundation axiom or a native Result.

**Parent:** `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`, objective `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. Retain frozen science `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03` and historical comparison `@fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Current P000 V5 and Heartbeat World maintain six signed native spatial axes; this experiment fixes **two selected axes** with the remaining four displacement coordinates zero, without asserting a native plane or selecting a complete 晶包 layer.

## Actual source-level consumer crosswalk

| Actual evidence (exact source) | Typed disposition / correction |
| --- | --- |
| `definitions/ENTERPRISE_PATH_VALUED_SQUARE_ROOT_OPERATOR_20260821.md`, main Git blob `61f23f2bcf965aa21d093ae3e35c0d6cb70610b7`, §§2–6: Gaussian local component carrier, ordered nonnegative `GRoot_E(r²)`, positive-generator path words `Lambda(a,b)`. | **PRESERVE_CARRIER / PRESERVE_PATH_BRC.** This operator has a real, correctly typed positive-sector domain. Its frozen theorem is unchanged. |
| `research_notes/TOOL_DISCOVERY_NATIVE_GEOMETRY_OF_NUMBERS_MINIMA_CALCULUS_RESULT_20260822.md`, blob `e3b1488a9bfdc44795f5d0e78c67e8c128bd30dc`, §10, lines 340–397: directly consumes `PathSqrt_E`, `GRoot_E`, `Lambda`, and computes exactly 6 positive trace classes and 110695538274255714208 positive words for `r=50`. | **PRESERVE_OBSERVER / TYPE_BOUNDARY.** Six is sufficient for trace-invariant functions on that explicitly positive path population. The result cannot silently serve a larger signed endpoint or future-step operation language. |
| The same tool-discovery note §9 (lines 296–339) says the positive sector is “current native sector” and denies native negative axes, describing the **2026-08-22 historical ontology**. | **SUPERSEDED HISTORICAL NATIVE INTERPRETATION** under current P000 V5; retain the modular positive-sector counting identity as a restricted observer construction, not a current global Foundation assertion. Historical original text is preserved. |
| `experiments/tool_discovery_native_geometry_of_numbers_minima_calculus_20260822.py`, blob `643b2bac659a445891dcb5588b647972977104e0`, `groots_square`, `path_fiber_size`, `check_roots`: explicit positive roots and binomial word counts. | **PRESERVE_EXECUTED_POSITIVE_CHECK.** The script asserts the inherited R063 positive calculation, not signed X6 future-operation completeness. |
| Original frozen X6 28-row `research_artifacts/X6_LEGACY_PLANE_RECONCILIATION/claim_ledger.json`, branch `a0bfa8eace20b061f5b228c733acdc46221388d7`, blob `5881055c0801ca5bb0970756d500daa0114d36b0`, `LP-028`. | This specific old ledger concluded zero broken consumers only for its named main snapshot/audit set. The present evidence identifies a concrete surviving downstream **historical** caller and a precise future-operation guard. Whether any current active native operation improperly consumes its output still requires an actual dependency edge. |

## Exact LP028 future-operation theorem

In the declared fixed X6 axis pair let `r` be an arbitrary **positive integer** and define

`P_r={(a,b) in N_0² : a²+b²=r²}`,
`E_r={(x,y) in Z² : x²+y²=r²}`.

The first is the inherited ordered positive R063 root set; the second is the signed endpoint lift. Write `k(r)=|{(a,b) in P_r : a>0,b>0}|`. For `r>0`, exactly two positive roots lie on axes: `(0,r),(r,0)`.

Declare a native-square norm on the two fixed signed displacement coordinates `G(x,y)=x²+y²`, the **allowed one-step future operations** `U_x(x,y)=(x+1,y)`, `U_y(x,y)=(x,y+1)`, and the observation signatures

`q_0(x,y)=(|x|,|y|)`,
`q_x(x,y)=G(U_x(x,y))`,
`q_{xy}(x,y)=(G(U_x(x,y)),G(U_y(x,y)))`.

These are typed raw relative-displacement and future-operation observations; no final nonnegative Cell address, independent two-dimensional world, or time flow is asserted.

**Theorem LP028-F1 (exact capacity ladder).** For every integer `r>=1`,

```text
|q_0(E_r)| = k(r)+2,
|q_x(E_r)| = 2k(r)+3,
|q_xy(E_r)| = |E_r| = 4k(r)+4.
```

The paired future observations recover each signed endpoint **exactly**:

```text
x = (G(U_x(x,y)) - r² - 1)/2,
y = (G(U_y(x,y)) - r² - 1)/2.
```

Therefore `q_xy` is injective on `E_r`; it is a lossless readout for every signed-endpoint observable and its subsequent deterministic operations, given the fixed norm/scope. A single `q_x` is not endpoint-complete for any `r>0`, since the distinct states `(0,r)` and `(0,-r)` have equal `q_x=r²+1`. The analogous fact holds for `q_y`. Thus **both of these particular unit-axis probes** are necessary if one is limited to choosing a subset of `{q_x,q_y}` and needs full endpoint recovery; this is not a claim of an absolute lower bound across all possible composite probes.

**Proof.** A positive root with both coordinates positive has four signed lifts, and either of the two axis roots has two. Hence `|E_r|=4k+4`. The absolute map has `k+2` labels. On `E_r`, the identity `q_x=r²+1+2x` makes `q_x` equivalent to knowing `x`; the list of nonnegative `x` values has `k+2` entries, of which one is zero, so the signed list has `2(k+1)+1=2k+3` entries. The pair `(q_x,q_y)` gives both `x` and `y` by the displayed integer formulas, so all `4k+4` signed endpoints are distinguished. The one-probe witness establishes the stated necessity within the declared probe family. QED.

### Concrete operational counterexample / typed repair

For `r=50` (`N=2500`) the existing six positive roots and previous signed-X6 result give:

| Observer/allowed future language | Required exact number of endpoint labels |
| --- | ---: |
| Absolute positive R063 component trace `q_0` | **6** |
| Future squared norm after `+e_x`: `q_x` | **11** |
| Future squared norms after both `+e_x,+e_y`: `q_xy` | **20** |

For two signed lifts of the *same* positive root, `(14,48)` and `(-14,48)`,

`G(U_x(14,48))=2529`, while `G(U_x(-14,48))=2473`.

For `(14,48)` versus `(14,-48)`, the `+e_y` values are respectively `2597` and `2405`.

The old six-class trace compression is therefore fully valid for its declared trace-invariant query, while a consumer that subsequently allows these native future operations must retain the signed endpoint or the equivalent pair of probe outputs. The fiber sizes quantify exactly what information is needed for the chosen future-operation language. On the signed shell, shortest-path BRC mass remains the previously verified **442782153097022856828** unweighted ordered primitive words, pushed forward with multinomial multiplicities. This theorem does not collapse ordered-word identity when a later operation queries path order.

## Executed exact regression

The checker `research_checks/X6_LP028_NATIVE_NORM_PROBE_CAPACITY_20261112_ONHOUR.py`, immutable commit `8b0f6309bde84f4bbaea4feb7b9b7edfed8927af`, Git blob `8b2ae2ca320a336d5fe92a1b55152dfd0576508d`, independently enumerates positive roots and the signed shell, checks the capacity identities, checks exact integer endpoint recovery for every signed endpoint, and separately checks the inherited BRC pushforward.

**Actually executed locally 2026-11-12:** every integer `1<=r<=256`, all checks **PASS** (Python exact integers; no floats). Local file SHA256 `9963792ce89e5e044f657684989d97eeb783a30419d3afb87853de6064d2303e`; the immutable remote Git blob matches the executed file blob. The all-`r` result has its own algebraic/combinatorial proof above; finite execution checks the implementation.

## Project/review and exact next frontier

**Completed and consumed:** old 28-row ledger; fixed signed-X6 baseline; LP011 signed dominant readout and typed guard; LP019 signed thickness/native positive-BRC crosswalk; LP026 metric/depth resonance; R063 signed endpoint/path trace fibers; actual R063 geometry-of-numbers historical consumer. No previously completed shell or BRC test was reclassified as a new native result.

**Newly resolved:** a concrete LP028 source-to-result dependency with exact *allowed future-operation* sufficiency and a 6→11→20 capacity ladder. This refines the original “no broken consumer found in eight named definitions” result without falsely relabeling a historical positive calculation as erroneous or an active native execution defect.

**Smallest unfinished:** locate the precise **current active** theorem/code caller, if any, that imports the old tool-discovery §9 positive-sector Foundation wording or §10 six-class compression into a signed X6 future-step claim. Record the actual file, line, typed input, future operation, observer, classification and needed action for the existing LP028/28-row crosswalk. Continue selective old `research_notes/` audit beyond the already verified 38 files. The old LP011/LP019 historical independent caller gaps remain explicitly bounded.

**Authority and control:** Original X6 task remains `HANDOFF_READY / NEEDS_DISPATCH` with Driver `REQUEST_REVISION`; native Research-only conversation `chatgpt-research-onhour-enterprise-math-20260923` has its old recorded session but no currently verified winning X6 CLAIM/open. Original continuation request `onhour-research-20261112-0422-x6-continuation-v1` succeeded; the exact old progress artifact was refused as `ARTIFACT_NOT_IN_CONTINUATION_PACKET` under original #6845. Existing support issue `awdawmip/enterprise-math#2141` identifies the control-plane artifact allowlist and acceptance criterion; no new control request or identity was created here. This note is independent GitHub evidence, awaiting legitimate typed continuation and later independent mathematical review.
