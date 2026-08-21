# 进取 BRC × Multipath：Boolean Shadow 与路径加厚桥

Status: `ACTIVE / CANONICAL / FROZEN`
Date: `2026-08-21`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

Canonical acceptance source:

`driver_reviews/R062_STAGE0_BRC_MULTIPATH_ENRICHMENT_BRIDGE_DRIVER_REVIEW_20260821.md`

## 1. Historical BRC identity

`BRC = Branch-Recoalescence Collapse`.

The authoritative historical BRC is the R021/R023 Boolean/result-support semantic core, canonicalized in main and implemented by:

`EnterpriseMath/Relation/BranchRecoalescence.lean`.

Its native historical carrier is support-level:

- relation `Rel X := X -> X -> Prop`;
- support `Set X`;
- relational direct image `relImage`;
- exact branch `ExactBranch X := Set X`;
- branch configuration `List (Set X)`;
- exact recoalescence by literal support union;
- relation composition by an existential shared middle witness.

Freeze:

`CANONICAL_BRC = BOOLEAN_RESULT_SUPPORT_SEMANTICS`.

Historical BRC does not retain multiplicity, path identity, provenance/correlation, probability/weights, or signed/amplitude cancellation.

## 2. Component-typed native skeleton

For a translated native sector `S_ij(P)`, use typed cell states

`c(P,ij;x,y)`.

Retain the concrete start/placement `P`, sector label `(ij)` and distinct generator relations

`R_i`, `R_j`

corresponding to native component labels `X_i`, `X_j`.

Start incidence:

`Sigma_P^(ij) : P -> c(P,ij;0,0)`.

The trace context is

`T_{P;a,b}^{(ij)}`.

Freeze:

`BRC_NATIVE_LINE_BRIDGE_REQUIRES_COMPONENT_TYPED_TRANSITION_SKELETON`.

## 3. Enrichment tower

On the same typed skeleton, define three carrier levels.

### Path-formal BRC

`PATH_FORMAL_BRC(x,y)` is a finite formal `N`-sum of typed composable concrete path witnesses from `x` to `y`.

A witness retains the generator word, prefix cell trajectory and typed placement/terminal.

Addition is formal sum; multiplication is typed concatenation extended distributively.

### N-BRC

Apply augmentation

`epsilon(sum_p n_p[p]) = sum_p n_p`.

Entries now record path multiplicity in `N`; composition is typed natural-number convolution.

### Boolean-BRC

Apply support

`beta(n)=0 iff n=0`, otherwise `beta(n)=1`.

This is the canonical BRC/result-support shadow.

Freeze:

`PATH_FORMAL_BRC -> N_BRC -> BOOLEAN_BRC`.

`BRC_IS_EXACT_BOOLEAN_SHADOW_OF_COMPONENT_TYPED_NATIVE_MULTIPATH = true`.

The word `shadow` means support projection on the same typed transition skeleton. It does not mean Boolean BRC retains hidden access to the discarded richer information.

## 4. Forgetful-map laws

Path-formal augmentation to `N` is a global homomorphism for provenance-tagged formal path occurrences and typed composition.

Freeze:

`PATH_FORMAL_SUM_TO_N = GLOBAL_HOMOMORPHISM_FOR_PROVENANCE_TAGGED_FORMAL_PATH_OCCURRENCES`.

Ordinary path-set cardinality is not a global additive semiring map because set union is idempotent:

`A={p}` gives `|A union A|=1` but `|A|+|A|=2`.

Freeze:

`PATH_SET_CARDINALITY_TO_N = NOT_GLOBAL_SEMIRING_HOMOMORPHISM`.

For `beta : N -> Boolean`, positivity is a global support homomorphism:

`beta(a+b)=beta(a) OR beta(b)`,

`beta(ab)=beta(a) AND beta(b)`.

## 5. Minimal commuting diamond

For local translated `(1,1)`:

`X_iX_j`

and

`X_jX_i`

are two distinct native path witnesses with a common typed terminal.

Therefore:

- Path-formal BRC witness count = `2`;
- N-BRC multiplicity = `2`;
- Boolean-BRC support = `1`;
- trace quotient class count = `1`.

Freeze:

`COMMUTING_DIAMOND_MULTIPATH_TO_BOOLEAN = 2 -> 2 -> 1`.

## 6. 3-4-5 bridge

For `T_{P;3,4}^{(ij)}`:

- R061 native length = `5`;
- Path-formal BRC has `35` concrete witnesses;
- N-BRC terminal multiplicity = `35`;
- Boolean-BRC terminal support = `1`;
- trace quotient = one component trace.

For `(4,3)` the count is also `35`; `(0,5)` and `(5,0)` each contribute one path. One fixed-sector `N=25` total is `72` path witnesses.

Freeze:

`R062_N25_BRC_COLLAPSE = 35_PATHS -> 35_MULTIPLICITY -> 1_SUPPORT` on each nondegenerate 3-4 branch.

## 7. Trace quotient and Boolean quotient are distinct

Both leave the common richer path-witness source, but they forget different information.

Trace quotient keeps:

`(P, sector, component counts a,b)`

and quotients only component-preserving word order by adjacent commutations.

Boolean support quotient keeps only nonempty typed reachability/support, with component labels/placement available only when retained in the external skeleton typing.

Freeze:

`TRACE_QUOTIENT != BOOLEAN_SUPPORT_QUOTIENT` globally.

Boolean support can factor through a single already-fixed trace fiber, but that restricted factorization does not identify the two quotient constructions.

## 8. Unlabeled BRC obstruction

At translated `(1,1)`, a reverse-third carrier edge can reach the same carrier terminal as the two `ij` trace linearizations.

If generator labels are erased and only unlabeled nearest-neighbor/end-point reachability is retained, BRC support merges the shortcut with native line witnesses.

Freeze:

`UNLABELED_BRC_CANNOT_CLASSIFY_NATIVE_LINE_MEMBERSHIP`.

This is independent of coefficient enrichment; an N-valued coefficient on the same wrong unlabeled skeleton would still count a non-trace shortcut.

When component labels are retained, the third-family edge lies outside the declared `{X_i,X_j}` trace language.

Freeze:

`COMPONENT_LABELED_BRC_DISTINGUISHES_SAME_ENDPOINT_FROM_SAME_LINE = true` for the frozen reverse-third gate.

Correct construction order:

`COMPONENT_TYPED_FIRST -> CARRIER_ENRICHED_SECOND`.

## 9. Translation covariance

For any native coordinate-vertex translation `R`, the bridge transports:

- `Sigma_P^(ij)` to `Sigma_{P+R}^(ij)`;
- start placement `P`;
- sector/component trace class;
- path witness count;
- typed terminal;
- reverse-third distinction.

Parallel translated line segments are not identified.

Freeze:

`BRC_MULTIPATH_BRIDGE_TRANSLATION_COVARIANT = true`.

## 10. Reproducibility

R062 Stage 0 committed a deterministic integer-only checker:

`scripts/r062_stage0_validate_brc_multipath_bridge.py`.

The accepted replay covered:

- seven translated starts;
- all three sectors;
- all translated trace cases with `a+b<=12`;
- `1,911` trace cases;
- `172,011` explicit path witnesses;
- `1,892,394` center transitions;
- duplicate witness count `0`;
- bridge mismatch count `0`;
- witness replay SHA256 `175c7f0efa6e62497dde5abbb65d354ddfc17a557f37640ee30260815cd68726`;
- exact regeneration of the frozen R061 Stage 1R native replay targets.

## 11. Scope boundary

Freeze the strongest accepted statement:

`BRC_IS_EXACT_BOOLEAN_SHADOW_OF_COMPONENT_TYPED_NATIVE_MULTIPATH_WITH_PATH_ENRICHMENT_RECOVERING_FULL_FIBER`.

Interpretation boundaries:

1. canonical historical BRC remains Boolean/result-support semantics;
2. Path-formal BRC and N-BRC are R062 enrichments/carrier lifts, not recovered hidden historical definitions;
3. `RECOVERING_FULL_FIBER` means the enriched carrier explicitly stores the frozen R061 witness fiber from which N/Boolean projections are obtained;
4. Boolean BRC cannot be inverted after the fact to reconstruct multiplicity/provenance already discarded;
5. component labels are semantically necessary for native line membership.

Freeze:

`BRC_MULTIPATH_ENRICHMENT_BRIDGE_CLASSIFIED_AND_FALSIFIABLE = true`.

No R062 Stage 1 is implied by this definition.
