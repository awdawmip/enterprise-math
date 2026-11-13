# X6 / LP019 — R062 historical translation guard: exact scope, replacement witness, and typed path transport

Observation date: 2026-11-14. Parent `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. This is an **author-side source-quality and mathematical evidence unit**, not an original R062 Stage-0 rerun, native Source PROGRESS, RR, independent Driver disposition or new claim.

## Exact source and frozen scope

Historical original owner branch `research/r062-stage0-brc-multipath-bridge`, `scripts/r062_stage0_validate_brc_multipath_bridge.py`, immutable Git blob `48ba38a55969b32fab40bc33d066b10216a249d0` (730 lines). Frozen historical Driver review `driver_reviews/R062_STAGE0_BRC_MULTIPATH_ENRICHMENT_BRIDGE_DRIVER_REVIEW_20260821.md` at `fd2bcff10ca6e147348b6c1236027fc0d2877df3`, blob `d46593b6c2c257d5ff43f653ab32eb0385b238dd`, is `ACCEPTED/FROZEN` for its historical **positive two-generator, component-labeled sector**. Current X6 signed-native ontology is separate: task science pinned to P000 V5 centered baseline `59538f585d037d09ef687b28715c4bc1a3f9fe03`, historical comparison `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.

### Source-code diagnosis

Original function `translation_audit`, lines 539–569, at line 553 checks:

```python
if n_brc_terminal_count(a, b) != n_brc_terminal_count(a, b):
    mismatches.append((P, R, sector, a, b, "multiplicity"))
```

For any deterministic function returning a Python integer, this comparison is identically false. Its `"multiplicity"` mismatch branch cannot run on a well-defined input, irrespective of any translational effect. The branch therefore **does not independently test translation invariance of multiplicity**. This is a local test-adequacy defect. It is not evidence of an incorrect count or failed accepted R062 theorem.

Crucially, **other original guards remain load-bearing**: `enumerate_native_bridge`, lines 243–316, constructs typed witnesses for every one of seven original starts, each of three sector labels and each `a+b<=12`; independently compares `path_card == comb(a+b,a)` and `n_brc_terminal_count(a,b) == path_card`, checks prefix-path translation signatures and records an error on mismatch. Original `run`, lines 605–667, includes `bridge["mismatch_count"]==0` and a combined `TRANSLATION_COVARIANCE_PASS` gate. The original historical finite accepted result thus retains its distinct evidence, even though the standalone guard has the above redundancy.

## Exact statement: transported witnesses and multiplicity

Work in the **historical R062 positive component-typed sector model**, not signed X6. For arbitrary `P,R in Z²`, sector `s in {S12,S23,S31}`, nonnegative integers `a,b`, and every length-`a+b` word `w` with `a` occurrences of sector generator `i` and `b` of generator `j`, define the full prefix trajectory

```text
c(P,s,x,y) = p3(P) + ANCHOR3[s] + x*BASIS3[s][0] + y*BASIS3[s][1],
p3(u,v) = (3u,3v).
```

Every prefix at counts `(x,y)` obeys the exact integer identity

```text
c(P+R,s,x,y) = c(P,s,x,y) + p3(R).
```

Consequently `w -> w`, together with the tagged start update `P -> P+R` and the componentwise translation of all prefix points, is a **bijection between the corresponding typed path-witness fibers**. It preserves ordered word, length, component labels, multiplicity `binom(a+b,a)`, N-BRC count, and Boolean support. The path witness keys are *transported*, not literally identical: the full key includes start `P`, sector, full word and prefix trajectory. No carrier or quotient-based identification is used in this proof.

This holds for all such `P,R,a,b` by distributivity and the linearity of `p3`. It is a statement within the frozen positive-sector representation; no two-coordinate source is declared a complete P000 three-axis slice or six-axis signed-native execution.

## Executed independent finite metamorphic calculation

Using exact Python integers and `itertools.combinations`, independently reconstructed these **exact original constants**: seven `STARTS`, five `TRANSLATION_VECTORS`, three `SECTORS`, `BASIS3`, `ANCHOR3`, `p3(P)=(3P[0],3P[1])`; sampled precisely the seven historical `translation_audit` pairs:

```text
(1,1), (2,1), (3,2), (3,4), (4,3), (0,5), (5,0)
```

For every sample, enumerated every ordered word with the specified generator multiplicities, constructed full prefix trajectories at the original and translated starts, and asserted exact equality after adding `p3(R)` to every original prefix. Separately checked word-count equality to `math.comb(a+b,a)`.

Actual completed output:

```text
cases=735
path_correspondences=9135
prefix_checks=68250
mismatches=0
```

The counts also follow algebraically: `7*5*3*7=735`, `7*5*3*(2+3+10+35+35+1+1)=9135`, and `7*5*3*(2*3+3*4+10*6+35*8+35*8+1*6+1*6)=68250`.

An intentionally fault-injected **translation-dependent** consumer was then tested on `P=(0,0)`, `R=(1,0)`, `s=S12`, `(a,b)=(3,4)`: it reports 35 for the original placement and 34 after translation. The original self-comparison still returns `False`; a direct source/translated occurrence-count comparison returns `True` and catches the controlled fault. This mutation is an artificial test oracle, not a historical observed R062 output or a claim that the accepted R062 model contains such an error.

The independent calculation is **not** a byte-exact rerun of the 730-line owner script; its result is a new narrowly scoped metamorphic witness and an exact algebraic argument. The original owner result remains frozen and is not re-reviewed.

## Disposition for LP019

- Original `R062_STAGE0_REPLAY`: **`KEEP / HISTORICAL_DRIVER_ACCEPTANCE_UNCHANGED`**.
- `R062_TRANSLATION_AUDIT_LINE553_SELF_COMPARISON`: **`DEAD_INDEPENDENT_GUARD / TEST_ADEQUACY_ISSUE`**; the available bridge enumeration independently covers the actual historical finite scope. An optional later source improvement is to compare separately computed counts on original and translated typed path fibers, or assert their agreed count against `comb(a+b,a)` at both placements. Do not modify immutable accepted history to simulate a retroactive review.
- `LP019_NBRC_SIGNED_CANCELLATION_WRONG_CALLER` and `LP011_NATIVE_ARGMAX_WRONG_CALLER`: **`UNRESOLVED_PROVENANCE`**. The present branch does not establish a signed-native misuse.
- Higher-level actual consumer/dependency closure, original historical wrong-caller attribution and independent X6 Driver `REQUEST_REVISION` remain open.

## Recovery and action boundary

Last independently checked prior continuation `onhour-20261114-0211-own-continuation-read-v1` is `SUCCEEDED` as a **read**; its `execution_authorized=false`. Prior Research lineage: `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`, RA `RA-5E3FE1E761E4963EC461A892`. Existing custody record reports a live, unrevoked SID but `execution_authorized=false` and a declared owner-account conversation label; this report neither claims a current winning claim nor conducts a role-bound Source publication. Original published R062 artifact and prior X6 G25/native regression units are consumed without rerun.

Next exact step: trace an actual current/frozen **consumer** that maps the historical two-generator trace/positive N-BRC into signed-native X6; inspect its input map, omitted component/Cell and source line, with fixed typed witnesses. Classify `KEEP/RETYPE/REVISE` only against that actual caller. If none is located in the bounded corpus, retain the precise unresolved class. Do not re-run accepted R062 Stage0 or manufacture a wrong-caller source.

Status: `AUTHOR-PROVED EXACT TRANSPORT IDENTITY / INDEPENDENT 735-CASE METAMORPHIC CHECK PASS / HISTORICAL DEAD GUARD LOCATED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED`.
