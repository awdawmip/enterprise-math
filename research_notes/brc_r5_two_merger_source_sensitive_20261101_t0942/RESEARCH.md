# R5 — true-time, true-likelihood-ratio two-merger model: robust four-dimensional no-go cube

**Date:** 2026-11-01. **Scope:** a newly specified *auxiliary* finite stopping/terminal-sensor model; not an X6 native result and not a solution of the four-observer mother problem. **Status:** AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## Frozen inputs and provenance

- GLOBAL_KNOWLEDGE_V1 verified canonical `main@8cff27a01b9dc454220fad100377400fc7dfc02e`. `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, `projects/enterprise-math/00_EM_PROJECT_BOOTSTRAP.md`, `P000_STARTUP.json`, the original `P000_REALITY_FOUNDATION.json` and ACTIVE `我眼中的世界.md` were read at this one snapshot. P000 projection's `canonical_blob_sha1=770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` equals the fetched original's blob SHA.
- Enterprise Math canonical `main@71f5e22a2d4de499694c6db4bf7f195df6d63ab0`; applicable `docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md`, `docs/PORTABLE_RESEARCH_PROTOCOL.md`, `AGENTS.md` read at that snapshot.
- Immediately preceding **unreviewed** R5 portable front: PR #1663 commit `66e1aeb87d0a5ce75c8e161d5f09b6567979af25`, `research_notes/brc_r5_four_kernel_source_fiber_20261101_t0838/{RESEARCH.md,NEXT_TASK.md}`. This work tackles the stated next question by changing topology to two real LR-key mergers rather than repeating the previous four-kernel classification.
- Authored as this conversation's portable mathematical contribution; no self-asserted independent review, no current formal Source owner/CLAIM/Result. A bounded `em_control_tasks` owner check returned `CONTROL_QUOTA`. Current authenticated gateway had `research_authority_granted=false`, `executor_binding_configured=false`, 5/5 active native job slots. These facts do not invalidate neutral mathematical work or bestow task execution authority.

## Exact finite model (two strict-positive laws, no approximate LR keys)

Under either hypothesis/law P or Q, nature first selects a **source** S in {A,B}, each with probability 1/2 under both laws. FULL sees S, seedless LR sees only (decision time, likelihood ratio of the *entire observed source-labelled path*). At time 1 there is the first genuine decision-key collision: both sources have LR=1. Action `stop` outputs terminal response 0 at time 1; `continue` leads to a strictly positive binary signal U in {low,high} and another decision at time 3.

The U kernels are:

| S | Q(low\|S) | P(low\|S) | Q(high\|S) | P(high\|S) |
| --- | --- | --- | --- | --- |
| A | 1/4 | 1/8 | 3/4 | 7/8 |
| B | 1/2 | 1/4 | 1/2 | 3/4 |

At time 3 the **second genuine decision-key collision** is A-low with B-low: both have LR=(1/8)/(1/4)=(1/4)/(1/2)=1/2. The two high keys have distinct LR values 7/6 and 3/2. Thus the LR keys are precisely `t1:1`, `t3:1/2`, `t3:7/6`, `t3:3/2`; no single key occurs twice on a trajectory. FULL's six keys are t1-A, t1-B, t3-A-low, t3-A-high, t3-B-low, t3-B-high. All stop/continue behavioral randomizations use fresh independent coins conditional on the current key (no persistent policy seed).

At time 3, `stop` outputs response 0 at time 3; `continue` incurs one more time step, draws terminal W in {0,1}, and **has no further control decision**. It outputs response W at time 4. W is strictly positive under both laws, with independent source-dependent success probabilities

`pA=P(W=1|A), pB=P(W=1|B), qA=Q(W=1|A), qB=Q(W=1|B)`.

All four parameters vary **independently over the entire real closed cube**

```
pA in [23/32,25/32],  pB in [7/32,9/32],
qA in [7/32,9/32],    qB in [23/32,25/32].
```

The W kernels assign strictly positive probabilities to both outcomes everywhere in this cube. The observer is genuinely `(eP,eQ,TP,TQ)`, with `eP=P(final response=1)`, `eQ=Q(final response=0)`, and each T the expected terminal time under its own law. The model's terminal decision rule is fixed; the FULL/LR comparison concerns the declared stop/continue controls. All labelled branch P and Q masses remain separate in a positive-rational BRC flow carrier `(S,U,W; law, mass, time, branch)`. The signed difference used below is introduced only at the final observation/support functional, not treated as cancellation of positive branch mass.

## Theorem — all-real robust two-merger obstruction and LR rank four

For every real quadruple `(pA,pB,qA,qB)` in the cube, both observation hulls are well-defined, the LR observation hull has **affine dimension exactly 4**, and

```
max_FULL (eP+eQ) - max_LR (eP+eQ)
    = pA/16 - qA/8 >= 5/512 > 0.
```

Consequently `conv O_FULL != conv O_LR` for every point in the four-dimensional real cube, despite LR full affine rank. At the center `(pA,pB,qA,qB)=(3/4,1/4,1/4,3/4)`:

```
max_LR(eP+eQ)   = 79/64,
max_FULL(eP+eQ) = 5/4,
strict support gap = 1/64,
FULL witness        = (3/8, 7/8, 5/2, 5/2),
LR rank-four determinant = 9/256.
```

The FULL witness is not even in the LR closed convex hull and lies at L-infinity distance **at least 1/128** from it: its `eP+eQ` value exceeds the LR maximum by 1/64, and the two-coordinate functional has L1 coefficient norm 2. This is a lower bound, not an asserted exact distance.

### Proof 1: exact Bellman/source-fiber contrast, entire real cube

For a source S and a U outcome, the improvement in `J=eP+eQ` from `continue` rather than `stop` at time 3 equals `P(S,U) pS - Q(S,U) qS`. Denote the four changes

```
alpha = A-low  = pA/16 - qA/8,
beta  = A-high = 7pA/16 - 3qA/8,
gamma = B-low  = pB/8 - qB/4,
delta = B-high = 3pB/8 - qB/4.
```

The baseline of `J` when every terminal response is 0 is exactly `1` (eP=0, eQ=1). Write `c,l,hA,hB in [0,1]` for LR continuation at t1, t3-low, t3-highA, t3-highB. By the law of total probability, independently of any finite-vertex argument,

```
J_LR = 1 + c[(alpha+gamma)l + beta*hA + delta*hB].
```

For FULL, use six separate continuation parameters `cA,cB,lA,hA,lB,hB`:

```
J_FULL = 1 + cA[alpha*lA + beta*hA] + cB[gamma*lB + delta*hB].
```

The entire real cube gives the following *exact* bounds:

```
alpha >= 5/512 >0,
beta  >= 107/512 >0,
gamma <= -37/256 <0,
delta <= -19/256 <0,
alpha + gamma <= -63/512 <0.
```

Hence FULL takes `cA=lA=hA=1` and ignores B, attaining `1+alpha+beta`; LR takes `c=hA=1`, `l=hB=0`, attaining `1+beta`. These choices are admissible deterministic policies, so the inequalities are also attained upper bounds for all **real** behavioral probabilities. Their difference is exactly alpha and is uniformly at least 5/512. This proves the support obstruction without sampling or unstated continuity assumptions.

At the center, `(alpha,beta,gamma,delta)=(1/64,15/64,-5/32,-3/32)`. The above exact FULL policy has actions `(cA,cB,lA,hA,lB,hB)=(1,0,1,1,0,0)` and observer `(3/8,7/8,5/2,5/2)`. The exact LR optimizer `(c,l,hA,hB)=(1,0,1,0)` gives `(21/64,29/32,55/16,27/8)`.

### Proof 2: explicit four-dimensional LR affine-rank certificate

Use five LR **deterministic** policy bitstrings ordered as `(c,l,hA,hB)`:

```
0000  -> (0,1,1,1)
1000  -> (0,1,3,3)
1001  -> at center (3/32,13/16,27/8,13/4)
1010  -> at center (21/64,29/32,55/16,27/8)
1100  -> at center (5/64,25/32,51/16,27/8)
```

Form the 4-by-4 matrix of each of the last four observation vectors minus the first, with each difference as a **row**. Direct symbolic elimination yields

```
det = [pA*qA + 9*pA*qB - 9*pB*qA - pB*qB]/128.
```

At the center this equals 9/256. For the entire cube the numerator `N` has partial derivative signs:

```
∂N/∂pA=qA+9qB>0,
∂N/∂pB=-(9qA+qB)<0,
∂N/∂qA=pA-9pB<0,
∂N/∂qB=9pA-pB>0.
```

Therefore the exact global minimum is at `(pA,pB,qA,qB)=(23/32,9/32,9/32,23/32)`, where `N=63/16`, so `det>=63/2048>0` for **all real** cube parameters. Four affine dimensions follow, and the four-dimensional observer space gives the matching upper bound.

### Proof 3: scope of finite deterministic enumeration

Every complete trajectory visits each of its LR `(time,LR)` keys **at most once**, and every action uses a fresh conditional coin. Hence each observer coordinate is a multi-affine polynomial in the corresponding behavioral continuation variables. Holding all other variables fixed, an affine coordinate is the convex interpolation of its 0/1 endpoints. Iterating over variables proves that every real behavioral observation lies in the convex hull of deterministic observations; the reverse inclusion is immediate. Thus the 16 LR and 64 FULL deterministic vertices are exhaustive **for this exact model**, though Proof 1 establishes the support extrema directly. This argument is **not** asserted for key-revisit models with parameter powers.

## Exact arithmetic check, evidence and boundaries

`VERIFY.py` is standalone Python standard-library `Fraction` code. The executed file checked both-law U normalization, actual LR collision and distinct high keys, 81 rational W-kernel quadruples (all 3^4 center/endpoint grid points), all 16+64 deterministic policies per grid point (6480 observation computations), the exact support formulas, center witnesses and center/boundary rank determinants. `EXACT_OUTPUT.txt` contains the actual standard-output transcript; end marker:

`PASS_EXACT_R5_TWO_GENUINE_MERGERS_SOURCE_SENSITIVE_CUBE_NO_GO`.

**Only** the algebraic bounds and determinant monotonicity prove the continuous real cube statement; the 81-point grid is a regression test, not an inference from sampling. No Lean proof, external prior-art priority check, native BRC/X6 embedding, independent mathematical review, formal Source Result or admission has been obtained. The two decision-key mergers do not imply the unrestricted mother problem is impossible: this is one precisely specified auxiliary family and it is rejected.

## New mathematical question

Can a genuine serial two-merger time/LR model have `(eP,eQ,TP,TQ)` **full affine rank four** and **exactly equal FULL/LR convex hulls** while the actual real behavioral images differ? Search first in a model that defeats the explicit local stop/continue advantage sign-separation test at every reachable exposed collision, not simply by sampling more source kernel constants. The new four-dimensional cube rules out a nontrivial open neighborhood of source-sensitive terminal laws in this first double-merger topology. See `NEXT_TASK.md` for a precise symbolic next experiment.
