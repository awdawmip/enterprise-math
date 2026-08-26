# Diagonal Gauge Refoundation — Independent Adversarial Review Return

Status: `FROZEN / INDEPENDENT VERDICT RETURNED / NO FOUNDATION EDIT`
Date: `2026-08-26`
Researcher-ID: `EM-DGRREV-6F2A9C`
Task-ID: `RS-DIAGONAL-GAUGE-REFOUNDATION-INDEPENDENT-REVIEW`
Owner branch: `research/diagonal-gauge-refoundation-independent-review`

Primary verdict:

`DGR_INDEPENDENT_NARROW_TYPED_CORRECTION`

Hard target disposition:

`DIAGONAL_GAUGE_REFOUNDATION_TYPED_CORRECTION_NARROWED__ALGEBRAIC_G1_DISPLACEMENT_CORE_ACCEPTED__BARE_PF_PATH_GLOBALIZATION_AND_UNTYPED_ADDRESS_SECTION_REJECTED`

## 1. Frozen authority and exact sources

Frozen candidate:

`research/diagonal-gauge-refoundation@bf9b309eb91ce22f50481a3e208789f0457ea87c`

Primary candidate return:

`research_returns/DIAGONAL_GAUGE_REFOUNDATION_RETURN_20260825.md@bf9b309eb91ce22f50481a3e208789f0457ea87c`

Taskbook:

`research_tasks/DIAGONAL_GAUGE_REFOUNDATION_INDEPENDENT_REVIEW_20260825.md`

Taskbook blob:

`10497cb4c43187ac1fc76bf22c3667407c2a9782`

Pinned current definitions audited:

- `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md#blob=393060ebfd6a86ad45f258747d78a14d9c8ac153`
- `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md#blob=03c3cd9d11df4005f2c1c3ab8bd76ee8eb6763a6`
- `definitions/ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md#blob=da35c76869ff88e46e28e33ba5bc37c95374a15d`
- `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md#blob=6ec0d73a19e28ec586c59a97d24f5798c9119771`
- `PACKET_PATH_FOUNDATION.md#blob=e725a95fd1be00f99233586311bc6d0e95888e7b`

Semantic policies used for the final typing audit:

- `FOUNDATIONAL_LOGIC.md#blob=f089400136341efbf10a5e24e8f0729800b942cd`
- `GEOMETRIC_TOOL_REFOUNDATION_POLICY.md#blob=57d87c9dda9bfbe5356492d11372d03490e2eb0f`
- `native_semantics_admissibility.json#blob=58ad0af8c2e3df56b353575bf0004095507bffbf`

Candidate packages/checker were inspected only after independently reconstructing the decisive algebraic claims. They were treated as audit targets, not premises.

## 2. Executive result

The candidate's central algebraic correction survives independent attack:

1. the frozen Stage-2 decoder is exactly
   `D_E(r,s)=can(r,s,0)`;
2. the min-zero displacement representatives with sectioned addition form an abelian group isomorphic to
   `Z^2` and to
   `Z^3 / Z(1,1,1)`;
3. the frozen reversal formula is exactly canonicalized additive inversion;
4. the current directed Pythagorean gauge is a well-defined positive-section gauge on that derived displacement group;
5. the unique globally homogeneous quadratic, `S3`-symmetric, diagonal-shift-invariant, unit-axis-calibrated form is the historical
   `Delta=a^2+b^2+c^2-ab-bc-ca`,
   and it is not the current native directed gauge;
6. current R061 Stage-2/Stage-3 formulas therefore need no mathematical change merely to recognize the derived displacement algebra.

However the frozen candidate is too strong in two typing directions:

- it repeatedly identifies the current min-zero **point/sector address atlas** with the canonical section of the displacement quotient. The safe construction must instead introduce a separately typed displacement section `A_D`, numerically represented by the same min-zero triples but not identified with primitive native point-address ontology `A_E`;
- Phase C states a total forgetful functor from arbitrary bare PF `PATH` to the Stage-2 displacement action groupoid. That map is not currently well-typed: PF paths are packet/cell adjacency walks, whereas Stage-2 `D_E(P->Q)` is defined on integer coordinate vertices / typed line endpoints. A bare packet walk has no declared canonical coercion to a Stage-2 endpoint pair.

A third, downstream typing repair is also required:

- the proposed `N[G_D]` multiplicative endpoint pushforward on a fixed-start path-formal object suppresses source/target placement. Composition is correctly typed by an action-groupoid/category algebra, or by a separately declared translation-identification convention, not automatically by the ordinary group semiring on bare displacements.

Therefore the correct disposition is narrowing, not full acceptance and not refutation.

## 3. Claim-by-claim proof / counterexample matrix

| Attack | Independent result | Verdict |
|---|---|---|
| A. kernel / canonical section | `can(z)=z-min(z)1`; `can(z)=can(z') iff z-z' in Z(1,1,1)`; every diagonal class has one min-zero representative | `PASS`, but section must be typed as displacement section `A_D`, not primitive point quotient |
| B. composition / inverse | `x (+)_D y=can(x+y)` is associative/commutative; `(-)_D x=can(-x)=(M-x_i)`; exactly matches Stage-2 composition/reversal | `PASS` |
| C. metric fork | unique global homogeneous quadratic under the stated symmetries is `Delta`; current `q_E(can(g))` is quotient-well-defined but piecewise/positive-section and inversion-asymmetric | `PASS` |
| D. trace / BRC non-collapse | same endpoint displacement is strictly coarser than path/trace identity; start typing preserves parallel translations; third-family shortcut remains outside current fixed two-component line/BRC skeleton | `PASS WITH DOMAIN GUARD` |
| E. zero displacement vs identity path | current sources do establish nonidentity length-3 closed packet paths from a commuting diamond plus reversed third-family adjacency; `PATH_COUNT=3 != 0` | `PASS AS CLOSED PATH`; Stage-2 displacement label requires endpoint decoration / explicit cell-to-displacement bridge |
| F. semantic layer | quotient is not N0 primitive and no N0 definability certificate exists; strongest valid status is current-line-derived endpoint/displacement structure | `G1_CURRENT_LINE_DERIVED_ENDPOINT_OBJECT` |

Primary narrowing witnesses:

1. **Domain mismatch witness**: PF-04/PF-06 define a path as an ordered adjacency walk of packets/cells. Stage-2 defines `delta_I(P,Q)` and `D_E(P->Q)` for integer coordinate/triple-intersection vertices / line endpoints. Therefore the expression `F_D(p)=(P,delta_D(P,Q))` is not a total function on bare PF paths unless `P,Q` are added as endpoint decorations or a new canonical coercion is independently defined.
2. **Type-alias hazard**: the same set of min-zero triples can represent both current sector-address values and canonical displacement representatives, but equal underlying tuples do not make the two semantic types identical. Reusing `A_E` as the quotient section risks reintroducing exactly the primitive point-coordinate equivalence the current foundation forbids.
3. **Semiring typing witness**: a fixed-start collection of paths is not closed under ordinary concatenation with itself unless targets are transported back or source/target placement is retained. Hence multiplicative pushforward belongs naturally in the action-groupoid/category algebra, not automatically in `N[G_D]`.

## 4. Independent algebraic derivation

### 4.1 Kernel and decoder

Define

`chi(a,b,c)=(a-c,b-c)`.

Then

`chi(a,b,c)=0`

iff

`a=c` and `b=c`,

iff

`(a,b,c)=k(1,1,1)`.

Therefore

`ker(chi)=Z(1,1,1)`

and `chi` is surjective by `(r,s,0)`, so

`Z^3 / Z(1,1,1) ~= Z^2`.

For

`m=min(r,s,0)`, Stage-2 freezes

`D_E(r,s)=(r-m,s-m,-m)`.

But this is exactly

`can(r,s,0)`.

Also

`chi(D_E(r,s))=(r,s)`.

Hence Stage-2 already contains a complete derived displacement chart. No historical Euclidean metric is needed for this reconstruction.

### 4.2 Unique min-zero displacement section

For any `z in Z^3`,

`can(z)=z-min(z)(1,1,1)`

is nonnegative with minimum zero.

If `can(z)=can(z')`, subtracting gives

`z-z'=(min(z)-min(z'))(1,1,1)`.

Conversely a diagonal shift does not change `can`.

Thus every derived displacement class has exactly one min-zero representative.

Required typing repair:

define

`A_D := {displacement representatives encoded by (A,B,C) in N_0^3 with min=0}`.

Do **not** infer

`A_E_POINT_ADDRESS = A_D`

as semantic types merely because both admit the same tuple representation.

### 4.3 Group law and reversal

For `x,y in A_D`, set

`x (+)_D y = can(x+y)`.

Because `can(z+k1)=can(z)`,

`can(can(x)+can(y))=can(x+y)`,

which yields associativity.

Identity is `(0,0,0)`.

For canonical `x=(A,B,C)` and `M=max(A,B,C)`,

`can(-x)=(M-A,M-B,M-C)`.

This is exactly the frozen Stage-2 reverse decode.

Therefore composition and reversal are not merely compatible with the quotient presentation; they are the transported abelian-group law and inverse.

### 4.4 Metric fork

An `S3`-invariant homogeneous quadratic form on three lifted coordinates has form

`Q=alpha(a^2+b^2+c^2)+beta(ab+bc+ca)`.

Diagonal-shift invariance forces the diagonal direction into the radical, hence

`alpha+beta=0`.

Unit-axis calibration `Q(1,0,0)=1` gives `alpha=1`, so

`Q=Delta=a^2+b^2+c^2-ab-bc-ca`.

But

`Delta(1,1,0)=1`,

whereas the current sector gauge requires

`q_E(1,1,0)=2`.

No contradiction follows because

`q_E(g)=sum_i can(g)_i^2`

is not a global homogeneous quadratic form on the abelian group in the signed-scalar sense; in particular it is generally inversion-asymmetric.

Thus:

`QUOTIENT_STRUCTURE != CHOICE_OF_LENGTH_FUNCTIONAL`.

The historical `Delta` may remain a derived/classical symmetric quadratic readout; it is not thereby restored as the current native Enterprise length.

## 5. Required regressions

Independent checker:

`scripts/check_diagonal_gauge_refoundation_independent_review.py#blob=4332d78be69fb77d49fe7b21e91f66f72e4f3d26`

Independent report:

`research_results/DIAGONAL_GAUGE_REFOUNDATION/DIAGONAL_GAUGE_REFOUNDATION_INDEPENDENT_REVIEW_CHECK_REPORT.json#blob=f8c6a1fbf096e3468c2eaea65a53b27088f2d0e4`

Report status:

`PASS_WITH_REQUIRED_TYPING_NARROWING`

Report SHA-256:

`cfd8e53632fedadc10c30b301bc6eb39c6386efd61a1f53e5da1dcc8366350c8`

The independently executed certificate covers:

- `531,441` kernel-iff lift pairs;
- `8,019` canonical-section / diagonal-shift checks;
- `3,721` Stage-2 decoder/chart pairs;
- `16,129` group-law pairs;
- `50,653` associativity triples;
- `16,129` integer triangle-certificate pairs;
- `762` `S3` covariance cases;
- `15,309` `Delta` diagonal-invariance cases;
- required unit-axis, `3-4-5`, `(1,1,1)`, and metric-fork examples.

Exact required examples:

- unit forward: `(1,0,0)`, `q=1`;
- unit reverse: `(0,1,1)`, `q=2`;
- `3-4-5` forward: `(3,4,0)`, `q=25`;
- reverse: `(1,0,4)`, `q=17`;
- balanced lift: `can(1,1,1)=(0,0,0)`;
- metric fork: `Delta(1,1,0)=1` while `q_E(1,1,0)=2`.

No repository CI or Foundation promotion is claimed by this return.

## 6. Trace / BRC non-collapse audit

The derived displacement object is safe only as a **forgetful target**, not as an upstream equality rule.

### 6.1 Parallel translations

Bare `g in G_D` is insufficient globally because the same displacement appears at many starts.

The safe endpoint arrow is

`(P,g): P -> P·g`.

Retaining `P` prevents identification of parallel translated segments.

### 6.2 Same endpoint, different path provenance

In a local commuting diamond,

`X_iX_j`

and

`X_jX_i`

are distinct concrete path witnesses with the same endpoint displacement.

Thus endpoint displacement is intentionally non-injective on path provenance.

### 6.3 Same endpoint, different line membership

The frozen reverse-third carrier shortcut reaches the same carrier endpoint as the `(1,1)` two-component trace but is explicitly not a member of that native line trace.

Therefore

`SAME_DISPLACEMENT != SAME_NATIVE_LINE`.

### 6.4 Current R062 remains intact

R062 fixes component typing before enrichment and excludes the third-family shortcut from the declared `{X_i,X_j}` line skeleton.

Adding a separate endpoint-displacement readout does not alter:

`PATH_FORMAL_BRC -> N_BRC -> BOOLEAN_BRC`.

The diagonal displacement quotient is not the trace quotient and not Boolean support.

No R062 formula requires mathematical change.

## 7. Closed-path audit

From current line/BRC sources, local `(1,1)` has two distinct length-2 packet paths

`p_1=X_iX_j`,

`p_2=X_jX_i`

from anchor cell `s` to common terminal cell `t`, and a third-family adjacent shortcut between the same cells.

PF-06 explicitly permits reversal and loops. Therefore reversing the shortcut and concatenating yields two distinct closed packet paths

`L_1=p_1;(e_k^-)^{-1}`,

`L_2=p_2;(e_k^-)^{-1}`

with

`PATH_COUNT(L_1)=PATH_COUNT(L_2)=3`.

They are not the identity path, whose transition count is `0`.

So the path-theoretic statement

`NONTRIVIAL_CLOSED_PATH != IDENTITY_PATH`

is exact.

The candidate's stronger unqualified statement

`ZERO_STAGE2_DISPLACEMENT != IDENTITY_PATH`

must be typed more carefully. It is valid for endpoint-decorated/anchored realizations once their endpoint map to the Stage-2 displacement group is declared; it is not currently a total theorem on arbitrary bare PF paths.

## 8. Semantic-strength audit

Strongest valid classification:

`G1_CURRENT_LINE_DERIVED_ENDPOINT_OBJECT`.

Rejected stronger classifications:

- `N0_PRIMITIVE` — not declared in PF base;
- `N0_DEFINABLE_DERIVED` — no packet/adjacency-only choice-independence / automorphism certificate exists;
- primitive native point quotient — directly conflicts with the current point/sector-address freeze.

The construction is stronger than mere implementation carrier bookkeeping because it exactly reconstructs already-frozen G1 Stage-2 composition, reversal and directed gauge behavior.

Target-leak audit:

`NO_DECISIVE_TARGET_LEAK_IN_ALGEBRAIC_CORE`.

Reason: the diagonal kernel was independently reconstructed from the current Stage-2 `Z^2` decoder and sectioned composition, not imported from the superseded Euclidean metric. The same quotient presentation existed historically, but historical existence is not used as proof.

Semantic hazard remains if the result is promoted beyond G1 or if the numerical min-zero tuple representation is used to erase the distinction between point addresses and displacement representatives.

## 9. Smallest exact narrowing

The candidate is accepted after replacing the broad claim bundle with the following typed bundle:

1. `L_D = Z^3` is a **lifted displacement label carrier**, not native point ontology.
2. `G_D = L_D / Z(1,1,1) ~= Z^2` is an exact **derived G1 displacement group** reconstructed from current Stage-2 mathematics.
3. `A_D` is the unique min-zero displacement section of `G_D`.
4. `A_D` and current point/sector address type `A_E` may share the same tuple representation but are semantically distinct types.
5. Stage-2 decoder, composition, reversal, directed gauge and triangle law are unchanged.
6. Stage-3 spectrum remains exactly `{ell_E(g),ell_E(-g)}` at the endpoint-displacement level.
7. Trace-to-displacement descent is valid for typed translated traces.
8. Path-to-displacement descent is valid only for endpoint-anchored/decorated path objects until a separate global PF-path endpoint bridge is frozen.
9. Closed packet loops of length `3` are exact; zero Stage-2 displacement for them requires the preceding endpoint decoration/bridge.
10. Endpoint pushforward with multiplication must preserve source/target typing via an action-groupoid/category algebra, or explicitly declare a translation identification before using `N[G_D]`.
11. Endpoint displacement remains strictly coarser than native trace/path/BRC semantics and is not a line-membership classifier.

## 10. Impact on current R061 / R062

Mathematical change required:

`NONE`.

Keep unchanged:

- Stage-2 decoder;
- translated sector selection;
- line identity;
- path-fiber cardinality;
- triangle inequality;
- reversal formula;
- reversal asymmetry;
- Stage-3 bidirectional trace pair;
- Stage-3 length spectrum;
- R062 component-typed multipath tower;
- reverse-third exclusion from current line membership.

Only interpretation/source typing may need correction if the control plane later integrates the result.

## 11. Minimal source-change recommendation

No Foundation edit is authorized in this task.

If a later control-plane integration accepts this narrowed verdict, the minimum safe source transaction should:

1. narrow the blanket plane-foundation prohibition to something equivalent to
   `NO_PRIMITIVE_NATIVE_POINT_DIAGONAL_SHIFT_QUOTIENT`;
2. add a dedicated G1 definition for `L_D`, `G_D` and separately typed canonical displacement section `A_D`;
3. add a Stage-2 compatibility note stating that the existing decoder/composition/reversal are exactly the canonical section/group operations of `G_D`;
4. explicitly state that `A_D` tuple values are not a new point-address equivalence and do not retype `A_E` as a quotient;
5. leave the current directed sector gauge and Stage-3 spectrum unchanged;
6. leave R062 unchanged;
7. withhold any global `PF_PATH -> G_D` functor until an endpoint-anchor/decorated-path bridge is defined;
8. withhold the ordinary `N[G_D]` multiplicative pushforward claim unless source/target placement has been handled by a groupoid/category algebra or an explicit transport convention.

## 12. Tool / method classification

No new general-purpose research mechanism was introduced.

Tool-reuse classification:

`NOT_APPLICABLE` — the added script is a task-local independent regression certificate, not a new reusable tool family.

## 13. Final verdict

`DGR_INDEPENDENT_NARROW_TYPED_CORRECTION`.

The central refoundation insight is real: current R061 already carries an exact derived diagonal displacement algebra, and the 2026-08-20 deletion of every diagonal quotient was broader than necessary.

But the safe theorem is narrower than the frozen candidate:

`DERIVED_G1_DISPLACEMENT_QUOTIENT = ACCEPTED`

while

`PRIMITIVE_POINT_ADDRESS_QUOTIENT = REJECTED`

and

`BARE_GLOBAL_PF_PATH_ENDPOINT_FUNCTOR = NOT_YET_TYPED`.

This completes the independent review hard target without editing the current Foundation.

Stop boundary:

`STOP_AFTER_INDEPENDENT_VERDICT_AND_SOURCE_IMPACT_RECOMMENDATION`.
