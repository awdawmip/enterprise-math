# P000 six-axis Tropical Plücker / valuated-matroid revision V2 return

Status: `SUCCESS / NONTRIVIAL_SURVIVOR / FINITE_VALUATION_DOMAIN_EXACT / RESULT_CHAIN_COMPLETE`

- Task: `RS-P000-SIX-AXIS-TROPICAL-PLUCKER-VALUATED-MATROID`
- Publication: `TP2-1BC640D8DA13DB3ABD24`
- Researcher: `EM-P000TP2-61A7E4`
- Claim: `chatgpt-p000tp2-20260830-61a7e4`
- Execution record: `ER-5C39A2D87F1E44B0A613`
- New Result: `RR-7F04B8A19C2D5E63AA71`
- Immutable predecessor Result: `RR-1D3266F488123BBE9369`
- Driver review input: `PR #901 / issuecomment-5466915618`
- Exact checker: `research_checks/P000_SIX_AXIS_TROPICAL_PLUCKER_VALUATED_MATROID_REVISION_V2_CHECK_20260830.py`
- Certificate: `research_artifacts/P000_SIX_AXIS_TROPICAL_PLUCKER_VALUATED_MATROID_REVISION_V2/P000_TROPICAL_PLUCKER_REVISION_V2_CERTIFICATE.json`

Hard target disposition:

`P000_TROPICAL_PLUCKER_REVISION_V2_RESULT_CHAIN_AND_VALUATION_DOMAIN_EXACT`

## 1. Revision boundary

This execution does not rewrite the first Result or any of its frozen files. It closes exactly the two Driver-requested gaps:

1. **result-envelope integrity** — the new Result record pins the return, exact checker, V2 certificate, and new execution record with both Git blob SHA-1 and SHA-256;
2. **valuation-domain typing** — `W_VP` is now frozen only on the finite nonzero-coordinate domain `D_p=(Z\{0})^6`, so no `+infinity` arithmetic is invoked or silently assumed.

The predecessor's narrow mathematical classification is preserved: `delta_T` is a derived six-weight piecewise-linear classifier. Nothing here promotes it to native P000 tropical geometry, a collapse law, a factorization mechanism, a Foundation object, or a replacement for native 6D structure.

## 2. Exact finite valuation domain

Fix a prime `p`. Define

`D_p = {x=(x_AB,x_AC,x_AD,x_BC,x_BD,x_CD) in Z^6 : x_ij != 0 for all six coordinates}`.

For `x in D_p`, define

`W_VP(x) = (v_p(x_AB), v_p(x_AC), v_p(x_AD), v_p(x_BC), v_p(x_BD), v_p(x_CD)) in N^6`.

Set

- `t1=x_AB*x_CD`,
- `t2=x_AC*x_BD`,
- `t3=x_AD*x_BC`,
- `alpha_i=v_p(t_i)`,

and

`Q=t1-t2+t3`.

Because all six coordinates are nonzero, all three products `t_i` are nonzero and all `alpha_i` are finite natural numbers. Therefore

`delta_T = second_min(alpha_1,alpha_2,alpha_3)-min(alpha_1,alpha_2,alpha_3)`

is an ordinary nonnegative integer on all of `D_p`.

**Zero-coordinate policy.** If any coordinate is zero, `W_VP` for this Result is **undefined**. Such points are outside the theorem domain. In particular, this Result defines neither `v_p(0)=+infinity` nor `second_min-min` on partially or totally infinite triples. The checker fails closed on every tested zero-containing boundary point.

## 3. Finite-domain nonarchimedean theorem

### Theorem

For every prime `p` and every `x in D_p`:

1. if `delta_T(x)>0`, then exactly one `alpha_i` is minimal;
2. if `m=min(alpha_1,alpha_2,alpha_3)` and `delta_T(x)>0`, then `v_p(Q(x))=m`, hence `Q(x)!=0`;
3. consequently, on `D_p`, `Q(x)=0 => delta_T(x)=0`.

### Proof

Assume `delta_T>0`. Then the minimum of the finite triple `(alpha_1,alpha_2,alpha_3)` is attained exactly once. Let `i0` be that index and `m=alpha_i0`.

Write each signed summand of `Q` as `p^m u_i` after extracting the common factor `p^m`. For the uniquely minimal summand, `u_i0` is a `p`-adic unit. For each other summand, `alpha_i>m`, so its normalized coefficient is divisible by `p`.

Hence

`Q/p^m ≡ +/- u_i0 (mod p)`,

which is nonzero modulo `p`. Therefore `Q!=0` and exactly `m` powers of `p` divide `Q`, i.e. `v_p(Q)=m`.

The contrapositive gives `Q=0 => delta_T=0` on `D_p`. This is the classical nonarchimedean unique-minimum cancellation obstruction, now stated only on the domain where every term in the proof is finite and defined.

No converse is claimed. The predecessor's `p=3` matched examples with the same coordinate valuation vector but different `Q`/`v_3(Q)` remain exact evidence that valuations erase residue cancellation data.

## 4. Retained carrier and finite-box results

The prior mathematical core was frozen as input and independently judged sound by the Driver at the claimed narrow scope. This execution rechecks it exactly rather than strengthening it.

For arbitrary finite six-weight vectors, with complementary pair sums

`S=(w_AB+w_CD, w_AC+w_BD, w_AD+w_BC)`,

the defect remains

`delta_T = second_min(S)-min(S)`,

and equivalently

`delta_T = sum(S)-max(S)-2*min(S)`.

Thus `delta_T=0` exactly when the minimum pair sum is attained at least twice.

The carrier `S4` action on the six edge labels induces the full `S3` on the three complementary-pair blocks with Klein-four kernel. Therefore `delta_T` is carrier-`S4` invariant. The complement involution swaps entries inside each complementary pair and fixes all three pair sums, so it also fixes `delta_T`.

For `W_COORD` on the box `{-B,...,B}^6`, writing `q=2B+1`, the retained exact formulas are

- triple ties: `T(q)=q^2(q^2+1)/2`;
- exactly two equal minima: `M(q)=q^2(q-1)(4q^2+q+3)/4`;
- survivors: `N_T(q)=T(q)+M(q)=q^2(4q^3-q^2+2q-1)/4`;
- all-distinct: `q^6-T(q)-2M(q)`.

Exact regressions remain:

| raw box | total | `delta_T=0` | `delta_T>0` | triple tie | exactly two minima |
|---|---:|---:|---:|---:|---:|
| `{-1,0,1}^6` | 729 | 234 | 495 | 45 | 189 |
| `{-2,-1,0,1,2}^6` | 15625 | 3025 | 12600 | 325 | 2700 |

The matched-control separation also remains at the tested derived-classifier scope only:

- `x=(-2,-2,0,2,1,1)`,
- `y=(-2,-1,-1,2,2,0)`,

share the locally computed Johnson coarse tuple `(0,22,18)`, `Q_orb=(-4,0,0)`, and `rho` carrier-orbit type `((0,1,1),0)`, while `delta_T(x)=0` and `delta_T(y)=3`.

This proves nonreconstructibility only relative to that exact tested coarse tuple. It does not turn those sibling quantities into accepted terminal Working Truth and does not make `delta_T` complete information.

## 5. Exact checker and boundary regression

The V2 checker is an extension of the predecessor's task-local exact-integer checker; no new general-purpose tool family was created.

Reuse resolution:

- predecessor task-local checker: `REUSE_EXECUTED_AND_EXTENDED_TASK_LOCALLY`;
- `T1_SCALE_ENUMERATION_VALUATION`: `REUSE_APPLIED` for finite valuation typing/census;
- `T3_TYPED_INCIDENCE_CIRCUIT`: `REUSE_APPLIED_FOR_VALUATED_MATROID_TYPING_ONLY`;
- `T7_FINITE_SYMMETRY_EQUIVARIANCE`: `REUSE_APPLIED`;
- new general tool family: `NONE`.

The checker verifies:

- faithful carrier `S4`, induced `S3`, V4 kernel, and stabilizers;
- carrier/complement invariance;
- defect formula;
- exact all-box formulas for `B=1,2`;
- `W_ABS` and finite `W_VP` censuses;
- matched nonredundancy controls;
- exhaustive `p=3` unique-minimum / `Q=0` implication on `{+-1,+-2,+-3,+-4}^6`;
- independent exhaustive `p=2` regression on `{-2,-1,1,2}^6`;
- explicit rejection of zero-containing `W_VP` boundary points;
- same-valuation/different-residue cancellation examples.

Deterministic local result:

`LOCAL_DETERMINISTIC_PASS checks=184315`

All arithmetic in the checker is exact integer arithmetic; no floating-point tolerance or post-selection is used.

## 6. Result-envelope repair

The new Result is not a mutation of `RR-1D3266F488123BBE9369`. It is a new immutable envelope for publication generation 2.

The output manifest in `research_result_records/RS-P000-SIX-AXIS-TROPICAL-PLUCKER-VALUATED-MATROID/RR-7F04B8A19C2D5E63AA71.json` pins every output of this execution required by the task:

1. `research_returns/P000_SIX_AXIS_TROPICAL_PLUCKER_VALUATED_MATROID_REVISION_V2_RETURN_20260830.md`;
2. `research_checks/P000_SIX_AXIS_TROPICAL_PLUCKER_VALUATED_MATROID_REVISION_V2_CHECK_20260830.py`;
3. `research_artifacts/P000_SIX_AXIS_TROPICAL_PLUCKER_VALUATED_MATROID_REVISION_V2/P000_TROPICAL_PLUCKER_REVISION_V2_CERTIFICATE.json`;
4. `research_execution_records/RS-P000-SIX-AXIS-TROPICAL-PLUCKER-VALUATED-MATROID/ER-5C39A2D87F1E44B0A613.json`.

Each row carries both `git_blob_sha1` and `sha256`. The Result record itself is not self-hashed inside its own manifest.

## 7. Terminal classification

Final research verdict:

`SUCCESS / NONTRIVIAL_SURVIVOR / FINITE_VALUATION_DOMAIN_EXACT / RESULT_CHAIN_COMPLETE`.

Safe statement:

`P000_DERIVED_SIX_WEIGHT_TROPICAL_CLASSIFIER_SURVIVES_ON_ITS_DECLARED_SCOPE_AND_THE_P_ADIC_PFAFFIAN_IMPLICATION_IS_PROVED_ON_THE_FINITE_NONZERO_COORDINATE_DOMAIN`.

Exact negative boundary:

`ZERO_COORDINATE_W_VP_EXTENSION_NOT_CLAIMED`.

Forbidden promotions remain:

- `P000_NATIVE_TROPICAL_GEOMETRY`;
- `P000_TROPICAL_COLLAPSE_LAW`;
- `TROPICAL_PLUCKER_IS_A_FOUNDATION_AXIOM`;
- `VALUATED_MATROID_REPLACES_NATIVE_6D`;
- `DELTA_T_IS_A_FACTORIZATION_MECHANISM`.

Next action: Driver re-review the new immutable Result and its complete dual-digest manifest. No downstream successor is published from the researcher lane.
