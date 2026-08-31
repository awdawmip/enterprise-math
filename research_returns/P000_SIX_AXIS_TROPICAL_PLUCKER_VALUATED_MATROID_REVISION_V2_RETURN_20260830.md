# P000 six-axis Tropical Plücker / valuated-matroid revision V2 return

Status: `SUCCESS / NONTRIVIAL_SURVIVOR / FINITE_VALUATION_DOMAIN_EXACT / RESULT_CHAIN_COMPLETE`

- Task: `RS-P000-SIX-AXIS-TROPICAL-PLUCKER-VALUATED-MATROID`
- Publication: `TP2-1BC640D8DA13DB3ABD24`
- Researcher: `EM-P000TP2-61A7E4`
- Claim: `chatgpt-p000tp2-20260830-61a7e4`
- Execution record: `ER-5C39A2D87F1E44B0A613`
- New Result: `RR-7F04B8A19C2D5E63AA71`
- Immutable predecessor: `RR-1D3266F488123BBE9369`
- Driver review input: `PR #901 / issuecomment-5466915618`

Hard target:

`P000_TROPICAL_PLUCKER_REVISION_V2_RESULT_CHAIN_AND_VALUATION_DOMAIN_EXACT`

## 1. Exact revision boundary

This execution does not mutate the predecessor Result or its frozen outputs. It closes exactly the two Driver gaps:

1. the new Result manifest pins the V2 return, exact checker, V2 certificate and new execution record with Git blob SHA-1 plus SHA-256;
2. `W_VP` is restricted to the finite nonzero-coordinate domain, so no implicit `+infinity` arithmetic remains.

The prior narrow classification is preserved: `delta_T` is a derived six-weight piecewise-linear classifier only. No native P000 tropical geometry, collapse law, factorization mechanism, Foundation status, or 6D replacement is claimed.

## 2. Finite valuation domain and theorem

Fix a prime `p` and define

`D_p = {(x_AB,x_AC,x_AD,x_BC,x_BD,x_CD) in Z^6 : every coordinate is nonzero}`.

For `x in D_p`, put

`W_VP(x)=(v_p(x_AB),v_p(x_AC),v_p(x_AD),v_p(x_BC),v_p(x_BD),v_p(x_CD)) in N^6`.

Let

`t1=x_AB*x_CD`, `t2=x_AC*x_BD`, `t3=x_AD*x_BC`,

`alpha=(v_p(t1),v_p(t2),v_p(t3))`,

`Q=t1-t2+t3`, and

`delta_T=second_min(alpha)-min(alpha)`.

All `t_i` are nonzero, hence every `alpha_i` is finite and `delta_T` is defined on all of `D_p`.

**Theorem.** For every prime `p` and `x in D_p`,

`delta_T>0 => v_p(Q)=min(alpha) => Q!=0`.

Consequently,

`Q=0 => delta_T=0`

on `D_p`.

**Proof.** If `delta_T>0`, the minimum `m=min(alpha)` occurs exactly once. Factor `p^m` from the three signed summands of `Q`. The unique minimal normalized summand is a unit modulo `p`; the other two normalized summands are divisible by `p`. Thus `Q/p^m` is nonzero modulo `p`, so `v_p(Q)=m` and `Q!=0`. The final implication is the contrapositive.

**Zero boundary.** If any coordinate is zero, `W_VP` in this Result is undefined. No `v_p(0)=+infinity` convention and no partially/all-infinite `second_min-min` calculus is claimed. The checker explicitly fails closed on zero-containing boundary points.

The converse `delta_T=0 => Q=0` remains false: the predecessor's equal-valuation examples with different `Q` and `v_3(Q)` continue to certify the residue-cancellation boundary.

## 3. Retained exact classifier facts

For any finite six-weight vector set

`S=(w_AB+w_CD, w_AC+w_BD, w_AD+w_BC)`.

Then

`delta_T=second_min(S)-min(S)=sum(S)-max(S)-2*min(S)`,

so `delta_T=0` exactly when the minimum pair sum is attained at least twice.

The carrier `S4` action on the six edge labels induces the full `S3` on the three complementary-pair blocks with V4 kernel. Hence `delta_T` is carrier-`S4` invariant. Complement swaps entries within each complementary pair and also fixes `delta_T`.

For `W_COORD` on `{-B,...,B}^6`, with `q=2B+1`, the retained exact counts are

`T(q)=q^2(q^2+1)/2`  (triple ties),

`M(q)=q^2(q-1)(4q^2+q+3)/4`  (exactly two equal minima),

`N_T(q)=q^2(4q^3-q^2+2q-1)/4`  (survivors).

Regressions remain exact:

| box | total | survivor | nonsurvivor | triple | two minima |
|---|---:|---:|---:|---:|---:|
| `{-1,0,1}^6` | 729 | 234 | 495 | 45 | 189 |
| `{-2,-1,0,1,2}^6` | 15625 | 3025 | 12600 | 325 | 2700 |

At tested derived-classifier scope, the matched states

`x=(-2,-2,0,2,1,1)`, `y=(-2,-1,-1,2,2,0)`

share Johnson coarse tuple `(0,22,18)`, `Q_orb=(-4,0,0)` and `rho` carrier-orbit type `((0,1,1),0)`, while `delta_T(x)=0` and `delta_T(y)=3`. This proves nonreconstructibility only relative to those tested coarse observables.

## 4. Deterministic checker

Exact checker:

`research_checks/P000_SIX_AXIS_TROPICAL_PLUCKER_VALUATED_MATROID_REVISION_V2_CHECK_20260830.py`

It reuses and extends the predecessor task-local checker; no new general-purpose tool family is introduced. Reuse resolution:

- predecessor checker: `REUSE_EXECUTED_AND_EXTENDED_TASK_LOCALLY`;
- `T1_SCALE_ENUMERATION_VALUATION`: `REUSE_APPLIED`;
- `T3_TYPED_INCIDENCE_CIRCUIT`: `REUSE_APPLIED_FOR_VALUATED_MATROID_TYPING_ONLY`;
- `T7_FINITE_SYMMETRY_EQUIVARIANCE`: `REUSE_APPLIED`.

The checker revalidates symmetry, exact box formulas, censuses and matched controls; exhaustively verifies the finite-domain valuation implication for the declared `p=3` test domain and an independent `p=2` domain; and rejects zero-coordinate `W_VP` inputs.

Deterministic result:

`LOCAL_DETERMINISTIC_PASS checks=184315`

All checker arithmetic is exact integer arithmetic.

## 5. Complete output envelope

The new Result `RR-7F04B8A19C2D5E63AA71` pins every output of this execution required by the task:

1. `research_returns/P000_SIX_AXIS_TROPICAL_PLUCKER_VALUATED_MATROID_REVISION_V2_RETURN_20260830.md`
2. `research_checks/P000_SIX_AXIS_TROPICAL_PLUCKER_VALUATED_MATROID_REVISION_V2_CHECK_20260830.py`
3. `research_artifacts/P000_SIX_AXIS_TROPICAL_PLUCKER_VALUATED_MATROID_REVISION_V2/P000_TROPICAL_PLUCKER_REVISION_V2_CERTIFICATE.json`
4. `research_execution_records/RS-P000-SIX-AXIS-TROPICAL-PLUCKER-VALUATED-MATROID/ER-5C39A2D87F1E44B0A613.json`

Each manifest row carries Git blob SHA-1 and SHA-256.

## 6. Terminal verdict

`SUCCESS / NONTRIVIAL_SURVIVOR / FINITE_VALUATION_DOMAIN_EXACT / RESULT_CHAIN_COMPLETE`

Safe statement:

`P000_DERIVED_SIX_WEIGHT_TROPICAL_CLASSIFIER_SURVIVES_ON_ITS_DECLARED_SCOPE_AND_THE_P_ADIC_PFAFFIAN_IMPLICATION_IS_PROVED_ON_THE_FINITE_NONZERO_COORDINATE_DOMAIN`.

Exact negative boundary:

`ZERO_COORDINATE_W_VP_EXTENSION_NOT_CLAIMED`.

Next action: Driver re-review the new immutable Result and dual-digest manifest. The researcher publishes no downstream successor.
