# R5 — Multi-root shared-gate masked-regret identity and rational cone certificate

Date: 2026-10-28 (Asia/Shanghai). Author: locally identified `EM-R5-LOCAL-20261028-CONE-AUTHOR`; research activity `RA-EMR5-CONE-20261028-0113-7CA1`. AUTHOR_PROVED / EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED. No native Source CLAIM, Result or independent Driver admission is represented.

## Exact frozen sources and model boundary

Account canonical `awdawmip/chatgpt-global-knowledge` read snapshot: `main@ecd9a62fddac9d34492c57cf902c9c119f4e58c1`. Read both global entries at that immutable version, the current ACTIVE worldview and the TASK researcher route. Project Source `awdawmip/enterprise-math` input snapshot: `main@988974d48b6df938b9ec48f1b09d3da15c169ea1`; P000 V5, X6/time, observer-relation constraint, project AGENTS, native research protocol, and exact R5 predecessor `research_notes/brc_r5_unrestricted_8leaf_support_20261028/{PROOF.md,NEXT_TASK.md}` were read. The prior 8-leaf signed separator was an excluded model; this is a distinct model and an extension of its single-collision Bellman principle.

Type: **EXTERNAL finite dual-measure sequential decision-tree theorem**, horizon N=3 for the example. It is not a native X6 physical evolution law or an upgrade to P000/Working Truth. Reuse applied: exact positive rational P/Q branch weights multiply along paths and aggregate by addition, retaining ordered provenance; signed `lambda` occurs only in the declared linear observable, never as positive BRC mass. A likelihood-ratio observer identifies histories with identical (time,R) and may erase future-predictive residuals.

Define four-vector `O=(e_P,e_Q,T_P,T_Q)`, where `e_P=P[declare Q]`, `e_Q=Q[declare P]`, and `T_M=E_M(tau)` for `M=P,Q`. For any `lambda=(a,b,u,v) in R^4`, optimize `lambda dot O` over unrestricted full-history policies, respectively over **seedless** behavioral policies whose random action law depends only on (time,R). Early stops and terminal declarations are unrestricted, and all signed `a,b,u,v` are allowed.

## Theorem 1 — Exact multi-root masked regret and all-signed cone criterion

Let `I` be a finite nonempty set of disjoint upstream root histories. At each root `i`, the policy may stop with optimal linear cost `L_i(lambda)`, or continue into a unique-other-signature subtree with optimal cost `W_i(lambda)` and a single shared (time,R) gate. At that gate the finite available actions are `d in D`; their **optimized** downstream cost for hidden history `i` is `K_i(d;lambda)`. All remaining decision signatures are independent between roots and branches, are visited at most once on a trajectory, and allow deterministic optimal suffixes. Under the full-history policy the gate actions `d_i` can differ; under the seedless LR policy the *same* gate action distribution must be used for all `i`. The gate decision occurs after the upstream stop and before its suffix. Positive branch masses are already included in every cost.

Set `m_i=min_{d in D} K_i(d)`, `beta_i=(L_i-W_i-m_i)_+`, `r_i(d)=K_i(d)-m_i >=0`. Then for every real signed `lambda`:

```text
V_full(lambda) = sum_i min{ L_i, W_i + m_i },
V_LR(lambda)   = min_{d in D} sum_i min{ L_i, W_i + K_i(d) },
Delta(lambda)  = V_LR - V_full
               = min_{d in D} sum_i min{ beta_i, r_i(d) } >= 0.      (1)
```

Consequently `Delta(lambda)=0` **iff** the argmin sets of `K_i` have a common action over the *strictly active* root set `A(lambda)={i: beta_i>0}` (with the empty intersection requirement vacuous if `A` is empty). If all active roots are mutually compatible, a seedless LR optimum exists. If they are incompatible, `Delta>0`. A root with an upstream stop/continue tie has `beta_i=0`; it cannot force a false conflict. This is the exact **early-stop masking** condition, including tie cases.

**Proof.** Each root's full-history minimization is independent, giving the first equality. In the compressed class the single gate action is common to all roots, yielding the second. For fixed `d` and root `i`, subtract `min(L_i,W_i+m_i)` from `min(L_i,W_i+m_i+r_i(d))`. If `L_i-W_i-m_i <=0`, the difference is zero. Otherwise it equals `min(L_i-W_i-m_i,r_i(d))`. This proves (1). All summands are nonnegative. Their sum is zero exactly when every strictly active root has `r_i(d)=0`; minimizing over finite `D` proves the intersection statement. Local randomized strategies cannot improve a linear objective beyond a deterministic strategy: here each (time,R) action parameter occurs at most once on any trajectory, so expected cost is multi-affine in independent behavioral probabilities, and a minimum occurs at a product-simplex vertex. Thus the formulas cover all real local action probabilities, not just rational randomizations. QED.

**Exact finite rational cone-cover criterion.** Suppose every P/Q branch mass and terminal observation vector is rational and there are finitely many suffix choices. Then each `L_i,W_i,K_i(d)` is a minimum of finitely many rational linear forms in `lambda`; `Delta` is continuous, nonnegative, positively homogeneous, piecewise rational-linear. Build the common rational hyperplane arrangement of pairwise differences of all underlying forms, and split its chambers by the finitely many action comparisons, activation and outer `d` comparisons. On each chamber the expressions in (1) are linear, so the zero-or-positive decision is exact. In particular, all-signed hull equality is equivalent to `Delta(lambda)=0` on the finite fan; any failure has a *strict rational* witness, equivalently a rational open cone containing it. To find such a chamber solve its rational strict linear inequalities, rescaled to non-strict inequalities with margin 1 (homogeneity), and verify `Delta>0`. Rational chamber boundaries with ties cannot conceal a positive gap: continuity gives a nearby generic interior point of positive gap. No restriction to nonnegative sampling costs is valid for this all-signed test.

This is an exact *criterion*, not a claim that the complete fan of the present model has been enumerated. The executable witness below verifies one explicit rational failure cone and a global signed supporting inequality.

## New strictly positive 8-leaf fan-in model (different from predecessor)

At t=1: `Q(A)=Q(B)=1/2`, `R(A)=P/Q=1/2`, `R(B)=3/2`. At t=2:

| t=1 root | conditional Q(U,V) | conditional P/Q factors (U,V) | resulting R(U,V) |
|---|---|---|---|
| A | (1/3, 2/3) | (2, 1/2) | (1, 1/4) |
| B | (1/2, 1/2) | (2/3, 4/3) | (1, 2) |

At t=3, for each of AU, AV, BU, BV, conditional Q is (1/2,1/2). Conditional P/Q multipliers are respectively `AU:(1/3,5/3)`, `AV:(2/5,8/5)`, `BU:(3/4,5/4)`, `BV:(3/5,7/5)`; each has Q-mean 1. The resulting terminal likelihood ratios, preserving ordered leaf labels AU0,AU1,AV0,AV1,BU0,BU1,BV0,BV1, are:

```text
1/3, 5/3, 1/10, 2/5, 3/4, 5/4, 6/5, 14/5.
```

They are pairwise distinct, so the only nontrivial shared (time,R) gate is `AU/BU` at t=2 with R=1. Every terminal P and Q leaf mass is strictly positive; both measures sum to 1. These terminal kernels differ from the 2026-10-28 preceding 8-leaf model, which used AU multipliers (1/4,7/4) and AV/BU/BV multipliers (1/2,3/2).

## Theorem 2 — Exact unrestricted signed support separator

Choose `lambda_0=(-20,-10,-2,3)`. For the new tree, direct rational Bellman costs at t=2 are:

| node | stop declare P | stop declare Q | continue with optimal terminals |
|---|---:|---:|---:|
| AU | -4/3 | -3 | -28/9 |
| AV | -5/3 | 0 | -5/6 |
| BU | -2 | -9/2 | -17/4 |
| BV | -3 | -21/2 | -43/4 |

At t=1 the optimal stop values are `L_A=-4, L_B=-15`. The independent V-suffix values are `W_A=-5/3,W_B=-43/4`. The full-history optimizer continues from both roots, continues at AU, stops P at AV, stops Q at BU, continues at BV, then declares `(P,Q)` at AU's terminals and `(Q,Q)` at BV's. It realizes

```text
O_full=(8/9,5/12,8/3,29/12),       V_full=-721/36.
```

The seedless LR optimizer uses the shared action `Q` (stop and declare Q at both AU/BU), AV stop P, BV continue and declare Q at both terminals. It realizes

```text
O_LR=(11/12,1/3,5/2,9/4),          V_LR=-239/12.
```

The exact masked regrets (1), over common actions P/Q/C, are `37/36, 1/9, 1/4`, so the global minimum is **`Delta=1/9`**. Equivalently every all-real seedless LR strategy satisfies

```text
20 e_P + 10 e_Q + 2 T_P - 3 T_Q <= 239/12 = 717/36,       (2)
```

but `O_full` has left side `721/36`, strictly violating (2). Therefore `O_full notin conv(O_LR)` and this *new* model is rigorously excluded from the equal-hull/unequal-image mother-problem candidate set.

**Verified open witness cone.** Fix the eight optimal terminal declarations `AU:PQ, AV:PP, BU:QQ, BV:QQ`; the four optimal t=2 actions `AU:C(PQ), AV:P, BU:Q, BV:C(QQ)`; and continuation at each t=1 root. For any signed `lambda`, impose eight strict terminal declaration comparisons, eight strict t=2 action comparisons (chosen versus the other two P/Q/C actions), and four strict t=1 continuation-versus-stop P/Q comparisons. Each is a homogeneous rational linear inequality in `lambda`. The finite checker evaluates all **20** at `lambda_0`; their minimum margin is **1/9**. Every direction satisfying the 20 inequalities has two strictly active roots with uniquely incompatible optimal shared actions `C` and `Q`, hence `Delta>0` by Theorem 1.

There is also an independently checkable uniform robustness certificate: all four coordinates of any policy's `O` obey `0<=e_P,e_Q<=1`, `1<=T_P,T_Q<=3`, so `|lambda dot O - lambda' dot O|<=8 ||lambda-lambda'||_infty`. Each optimum is 8-Lipschitz, hence their difference is 16-Lipschitz. Thus `||lambda-lambda_0||_infty<1/144` implies `Delta(lambda)>0`, including arbitrarily signed time coefficients.

## Exhaustive exact verification and native-interpretation limit

`VERIFY.py` uses `fractions.Fraction` (never floating-point inference) and exhausts *effective* deterministic policies, quotienting only unreachable descendants: full class `38*38=1444`, LR class `18*8*8=1152`. These cover all deterministic stop/declaration trees, because each t=2 node has two stop choices and four terminal-declaration pairs. The common LR gate has two shared stops plus 16 independent terminal declaration-pairs conditional on the common continue action. Explicit enumeration independently reproduces both Bellman optima and the four-vector witnesses. All-real extrapolation comes from multi-affinity, not the enumeration of random fractions. The local proof does not claim an external novelty search, formal prover verification or independent review.

For optional native interpretation: choose a chart-relative native X6 Cell, encode A/B by ordered primitive E1/E2 steps, U/V by E3/E4, and terminal lower/higher outcomes by E5/E6; keep six-axis path provenance and typed t=1/2/3 separate. This is an observer encoding into native X6, **not** a native six-dimensional propagation rule, physical calibration, or inference from Euclidean low-dimensional geometry.

## Provenance, state and next discriminating action

Native Enterprise Math task listing returned `CONTROL_QUOTA` during this run, and no live owner/CLAIM/Result or Driver review was obtained. The own GitHub research-activity record is only local author bookkeeping: it grants no formal execution permission or independence. The proof and exact output are author-level material awaiting normal review/admission.

Next: implement a full exact rational cone fan classifier from (1), or equivalently a rational LP dual certificate for each distinct full deterministic observation vector. Search a *different* strictly positive fan-in model whose every signed support direction passes the hull-equality gate, then attempt an all-real polynomial nonmembership certificate for the seedless image. The two eight-leaf separators are excluded models, not equal-hull examples.
