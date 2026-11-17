# R5 — All-signed exact convex-hull certification for finite two-law seedless-LR policies

Date: **2026-10-29 Asia/Shanghai**. Classification: **AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**. Researcher identity: locally allocated `Researcher-ID: EM-R5-Q29A` (not a service-issued identity); source-native role/CLAIM/Result/review: **not granted or verified**. Research session provenance: local research lane `R5-20261029-0536-Q29A`, not an authenticated platform thread ID. This is a mathematical paper-and-program artifact, not a claim of external physics or a native X6 dynamic. The mother target remains **OPEN**: find a strictly positive rational finite two-law model with equal four-observer convex hulls and unequal actual observer sets, or establish a scoped impossibility theorem.

## 1. Immutable read sources and verified frontier

- Account source: `awdawmip/chatgpt-global-knowledge` canonical `main@f4fe10884b636ddda1529b054ed99e08093a1428`, read via connected GitHub with the `00_BOOTSTRAP.md` and `OPERATING_MANUAL.md` at the **same** immutable ref; relevant ACTIVE worldview, math/code, BRC, EM research-activity, and handoff rules checked at that pin.
- Project source: `awdawmip/enterprise-math` `main@b5ca5b1355952d5306e6099f4b76c95f9559e5c3`; read `AGENTS.md`, `p000_reality_foundation.json`, `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`, `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`, `docs/PORTABLE_RESEARCH_PROTOCOL.md`, `docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md`, `control_plane/current_control_authority.json` and applicable research identity/activity contracts.
- Predecessor is the actual Draft **PR #1663**, head `research/brc-r5-robust-interval-20261029-0440@a08ddcdb5ef9e045b82b4f70c3aef67389d4d7bf`; source `research_notes/brc_r5_robust_bellman_interval_20261029_t0440/{RESEARCH.md,NEXT_TASK.md}`. Its rigorous *fixed-diamond* support-function gap remains an exclusion result, not an instance of the mother target.
- Native service observation during this study: `research_authority_granted=false`, `control_quota.active_jobs=5`, quota limit 5, `source_sync.control.state=CODE_REVIEW_REQUIRED`, `em_control_tasks(...) -> CONTROL_QUOTA`. Accordingly active Source Owner/Claim not authenticated; the mathematical investigation below is independent portable author work, with no Source state mutation.

## 2. Finite all-signed convex-hull theorem (PROVED)

**Model and exact scope.** Fix a finite-horizon stochastic experiment under two probability laws P and Q, finite observable histories and decision nodes, finite legal action sets, and a four-vector `O=(e_P,e_Q,T_P,T_Q)` of outcome expectations. Fix two policy classes: full-observable-history `FULL`, and **seedless LR** policies whose action distribution at a node is a function only of the declared information key `(time, current likelihood ratio)`; different hidden histories sharing a key use the same local distribution, with **no persistent correlated random seed**. Every complete trajectory encounters a given information key **at most once**; in particular every decision key includes the time. Let `D_FULL`, `D_LR` be the respective finite deterministic action maps (including stop/declaration decisions). The underlying P/Q path masses do not depend on the chosen local action map except through stopping/continuation.

For either policy class `C`, the four-observer image of behavioral strategies has the *multiaffine expansion*

```
O_C(pi) = sum_{d in D_C} [ product_{j in I_C} pi_j(d_j) ] O_C(d),
```

where `I_C` is its finite set of information keys and `pi_j` is any real probability vector over the legal actions at key j (including behavior probabilities 0 and 1). The product coefficients are nonnegative and sum to one. Thus

```
conv O_C(all real behavioral strategies)
    = conv { O_C(d) : d in D_C }.
```

*Proof.* For any final history, its under-P/Q probability times error or stopping-time output is a sum over possible action choices, each factorized as a product of local action probabilities; a fixed key occurs at most once along the history, so each observer coordinate is affine separately in every local action vector. Expand each vector into its finite simplex vertices and distribute. The expansion above follows and yields inclusion in the deterministic convex hull. Every deterministic map is a legal behavioral policy, yielding the reverse convex-hull inclusion. This works even when **distinct histories reconverge into one LR key**: that key's local action variable appears on multiple distinct path terms, but still only **once per path**. No perfect-recall assumption is needed for this convexification statement; a key repeated twice along one path would invalidate its multiaffinity proof and is explicitly excluded. QED.

**Exact necessary-and-sufficient containment.** Since each deterministic LR map can be implemented by the full-history class, `conv D_LR ⊆ conv D_FULL` at the observation level. Therefore the convex hulls are equal **if and only if** each `v in {O_FULL(d)}` is in the finite convex hull of LR deterministic observer vectors `u_1,...,u_k`. In four dimensions, this is exactly

```
find λ_j >= 0:  Σ_j λ_j = 1,  Σ_j λ_j*u_j = v  (all 4 coordinates).
```

For rational kernels and initial masses, every entry is rational. A feasible system has a rational solution (indeed a basic solution) with **at most five nonzero weights**. A rational λ witness is directly checkable by five rational equalities and signs. If infeasible, the rational separating-hyperplane theorem/Farkas alternative gives rational `w in Q^4` and `b in Q` such that

```
         w.v < b <= w.u_j   for every deterministic LR vector u_j.
```

A common denominator yields an integer direction. Because the first theorem includes **all real LR behavioral strategies**, this single exact certificate implies for every such real strategy:

```
||O_LR - v||_infinity >= (b - w.v)/||w||_1 > 0.
```

*Proof of rational finite support.* The feasible region is the intersection of a rational affine subspace with the nonnegative simplex, hence a nonempty compact rational polytope. A vertex has at most `rank(A) ≤ 5` positive coordinates and solves a rational square system; alternatively remove a rational nullspace direction successively from any rational feasible point. If empty, the disjoint rational point and rational convex polytope admit strict rational linear separation. QED.

**What the theorem does not say.** The finite deterministic convex hull and a *freshly randomized local behavioral image* need not be equal as sets. A five-vertex **persistent external mixture** is not by itself a legal single seedless LR strategy. Equality of hulls is only the **first filter** for the mother target; an actual observer-image membership test remains necessary after it passes. The theorem is also restricted to the visit-once information-key scope, not absent-minded repeated-use information states.

## 3. A complete all-signed 2-origin/3-signature exclusion (PROVED)

Let the full history at time 1 distinguish two positive-Q-mass origin labels A and B, each with `Q(A)=Q(B)=P(A)=P(B)=1/2` and current likelihood ratio `r=1`. The current LR policy forgets this source label. At time 1 it may stop and declare P or Q, or continue to terminal time 2. Conditional on origin `i` and continuation, the next (terminal) LR signature `s` ranges over `(1/2, 1, 3/2)`, with the strictly positive **Q** kernel

```
q_i = (p_i, 1-2*p_i, p_i),     0 < p_i < 1/2.
```

At that transition the **P** kernel is `s*q_i(s)` (the parent LR is 1); it also sums to 1 because `Σ_s s*q_i(s)=1`. All origins/histories have strictly positive masses. At terminal time 2 a policy declares P or Q; FULL can distinguish `i`, while LR uses only `(time,s)`.

Fix an **arbitrary real signed** linear objective

```
L = a*e_P + b*e_Q + c*T_P + d*T_Q,   (a,b,c,d) in R^4.
```

For one unit of incoming Q (and P) mass, the best time-1 stop value is `S=min(a,b)+c+d`. At time 2, the best terminal declaration for signature s contributes `min(a*s,b)`. Therefore the optimal conditional continuation value for origin i is

```
C_i = 2*(c+d) + p_i*min(a/2,b)
       + (1-2*p_i)*min(a,b) + p_i*min(3*a/2,b).
```

Set `H=min(a/2,b)+min(3*a/2,b)-2*min(a,b)` and `D_i=C_i-S=(c+d)+p_i*H`. The terminal minimization is shared by FULL and seedless LR: the P/Q ratio at a given terminal s is s for **both** origins, so even an origin-aware policy cannot improve this *linear terminal objective* further. At time 1 FULL may independently stop/continue A and B, whereas LR makes one common choice. Hence the **exact all-real, all-signed optimal values** satisfy

```
V_FULL = S + (min(0,D_A)+min(0,D_B))/2,
V_LR   = S + min(0,(D_A+D_B)/2),
Δ(w)   = V_LR - V_FULL
       = (|D_A|+|D_B|-|D_A+D_B|)/4 >= 0.
```

This proves the **necessary and sufficient** all-signed convex-hull classification

```
conv(O_FULL) = conv(O_LR)    iff    p_A=p_B.
```

For `p_A != p_B`, select `a=b=1, c=(p_A+p_B)/4, d=0`; then `H=-1/2`, `D_A=(p_B-p_A)/4` and `D_B=(p_A-p_B)/4`, yielding the **strict gap** `Δ=|p_A-p_B|/8`. For `p_A=p_B`, the origin conditional laws coincide: any full policy is matched by a seedless LR policy by averaging its two origin-specific time-1 action distributions, and—conditional on continuing—averaging the origin-specific time-2 declaration probabilities using the exact origin-specific continue masses. Because conditional kernels agree, the same averaging preserves the **whole terminal `(time,s,declare)` mass under P and Q**, not merely the optimal value. Thus in the equal-p case **the actual four-observer sets coincide**, in addition to their hulls. This model family is a proved **NO-GO** for the mother target.

## 4. Explicit strictly-positive rational witnesses and finite exact checks

Set `p_A=1/4`, `p_B=1/8`. FULL chooses to continue on A and stop/declare Q on B. For A at time 2, it declares Q at `s=1/2,1` and P at `s=3/2`. Its four-observer vector is

```
v* = (e_P,e_Q,T_P,T_Q) = (13/16,1/8,3/2,3/2).
```

Take the **integer** objective `w=(32,32,3,0)`. Exhaustive deterministic observer enumeration (10 LR action maps; 100 FULL action-map pairs, 75 distinct FULL vectors) and the analytic Bellman formula give

```
min_FULL w.O = w.v* = 69/2,
min_LR   w.O = 35,
Δ = 1/2,
forall real seedless LR:  ||O_LR-v*||_infinity >= 1/134.
```

An independent SymPy rational simplex computation returns a valid dual separator `w'=(64,64,0,6)` and threshold `b'=70`, with `w'.v*=69<70<=w'.u` for **all 10** deterministic LR vectors. An exact primal simplex query for a positive identical-kernel case produces the two-sparse mixture `1/2*u_0+1/2*u_7`. Independently of SymPy, the identical-kernel identity `v_full(plan_A,plan_B)=[u(plan_A)+u(plan_B)]/2` was checked for **all 100** ordered pairs of the 10 source plans. The code reruns the signed gap formula on **1,152** exact rational kernel/direction instances, including **negative** objective coefficients.

`VERIFY.py` is the executed Python `fractions.Fraction` verification program (SymPy 1.14.0 provides candidate LP outputs, independently rechecked by Fraction). `EXACT_OUTPUT.txt` records its real stdout. The finite tests support model arithmetic and the solver/witness implementation; the all-real theorem follows from the complete multilinearity and Bellman proofs, not finite sampling.

## 5. Prior art, BRC semantics and remaining questions

**Verified external context** (the cited sources are bibliographic/abstract checks, not proof dependencies or claims of novelty): Aliprantis, Glycopantis & Muir, *On mixed and behavioural strategies*, Economics Bulletin 29(3), 1783–1795 (2009), explicitly discusses information sets that no path meets more than once (https://econpapers.repec.org/article/eblecbull/eb-09-00331.htm). Cohen & Parmentier, *Future memories are not needed for large classes of POMDPs* (2023), studies memoryless policies as a distinct class, not this paper's exact mother-problem classification (https://www.research-collection.ethz.ch/entities/publication/9e7ebef3-5bd6-4103-8cc8-531794e68e0f). These comparisons constrain novelty: the multilinearity/finite LP reduction is a scoped research tool, not claimed to be an unprecedented general theorem.

**BRC use.** Preserve the origin label and Q/P mass pair, the exact path `(origin,time,s)`, and future conditional terminal laws through the declared observation `O`. The signed support direction is not replaced by a positive scalar. Any observer quotient is certified only for its declared four-vector and time horizon; the origin-erasure proof for `p_A=p_B` is exact only for this finite model. This is an auxiliary stochastic relation model; no native X6 spatial embedding, pulse law, physical probability calibration or P000 axiom amendment is claimed. Protected ACTIVE worldview and six-axis-plus-time model remain unchanged.

**Next independent question.** Implement this finite exact primal/Farkas filter for genuinely source-sensitive **two-route reconvergent** kernels using complete finite deterministic action maps, with exact source/path mass recursion and no terminal-declaration oracle. Remove only duplicate observer vectors, not origin/path information from the experiment. If **every** full deterministic vector has a ≤5-term rational LR mixture, test whether some full-history observer vector fails real polynomial LR membership (CAD or an explicit sign/resultant certificate). Otherwise publish an exact signed separating direction as a **new exclusion**, not as a mother counterexample. Keep existing PR #1663 as the R5 author-side handoff; preserve the parent target and formal Source constraints.
