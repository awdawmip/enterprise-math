# Enterprise Math R5 — Exact likelihood-ratio collision stratification and a discontinuous Bellman gap

**Date / status.** 2026-10-29 (Asia/Shanghai). `AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING`. This is a finite *external auxiliary* two-probability stopping model, not a claim about native Heartbeat-X6 dynamics, spatial dimensions or physical measurements. The mother question (equal four-observer convex hulls but different true images) remains open.

## Frozen sources and mathematical scope

* GLOBAL_KNOWLEDGE_V1 canonical `main@6629bd6fe79d111d72f54b1b01ec1e031254bf64` (verified by connected GitHub branch-ref read 2026-10-29); `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, ACTIVE `我眼中的世界.md`, math/code/BRC/PR-handoff policies.
* Enterprise Math canonical `main@cc55cd808640ebaa973d8605e8bda137192073e5`; `AGENTS.md`, `p000_reality_foundation.json`, `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`, `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`, `definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json`, `docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md`, `docs/PORTABLE_RESEARCH_PROTOCOL.md`.
* Previous author-side frontier: PR #1663 commit `9fb912b03d745612eabe8b7becbc14ca1402eac1`, `research_notes/brc_r5_two_source_sensitive_mergers_20261029_t1435/RESEARCH.md` and `NEXT_TASK.md`. The previous full-signed Farkas separator rejects a particular two-merger candidate. This unit analyzes the **algebraic locus of exact likelihood-ratio collisions** necessary to search valid candidates, rather than reusing that rejected model.
* Live research authority: service `em_status` reports `research_authority_granted=false`, `CODE_REVIEW_REQUIRED`, `active_jobs=5/5`. One bounded `em_control_tasks` owner-read attempt returned `CONTROL_QUOTA`; current task owner, formal CLAIM/Result and independent Driver review are not established. Local author contribution only.

### 1. Model, observables and BRC carrier

Fix times `t=1,2`. At time 1 the **full history** reveals a source label `i∈{A,B}`. Under law `Q`, each label has probability `1/2`; under law `P_eta`, the respective masses are `1/2+eta` and `1/2-eta`. The conditional continuation signal `y∈{+,-}` has

\[
 Q(+\mid i)=Q(-\mid i)=\tfrac12,\quad
 P(+\mid A)=p_A=\tfrac9{10},\quad
 P(+\mid B)=p_B=\tfrac35,
\]

and `P(-|i)=1-p_i`. All probabilities are strictly positive for `|eta|<1/20`. At time 1 choose `stop+declare P`, `stop+declare Q`, or `continue`; continued paths stop and declare at time 2. Nature's entire source/signal tree can be coupled independently of these stop decisions.

The FULL class uses `i` and (if observed) `y`; the genuine seedless-LR class uses only `(t,r_t)`, where `r_t=dP/dQ` on the observed history, with arbitrary **real behavioral probabilities** and no persistent common random seed. Both use the same time-dependent stopping/declaring actions. Define

\[
 O=(e_P,e_Q,T_P,T_Q)=(P[\text{declare Q}],Q[\text{declare P}],E_P\tau,E_Q\tau),\qquad
 L(O)=e_P+e_Q+\tfrac18(T_P+T_Q).
\]

The BRC carrier retains the positive labeled masses `P(i),Q(i)` and the conditional labeled signal flows `P(i,y),Q(i,y)`, before taking the four-observer readout. At `eta=0` the LR quotient erases `i` at time 1 but the downstream terminal laws still depend on it: this is a **future-relevant structural residual**. Nothing here equates signed Bellman differences to positive BRC masses or substitutes a two-dimensional coordinate formula for the project's native X6 world.

### 2. Exact baseline separation (all real behavioral strategies)

At `eta=0`, both time-1 sources have `r_1=1`. If stopping at time 1, the minimum conditional `L`-cost per unit source probability is

\[S=\min(1,1)+2(1/8)=\tfrac54.\]

If continuing from source `i`, the Bayes-optimal terminal declaration is `P` on `+` and `Q` on `-`: the conditional sum of wrong-declaration costs is `min(p_i,1/2)+min(1-p_i,1/2)=3/2-p_i`. Since both times equal 2 on a continued path, the conditional continuation cost is

\[C_i=(\tfrac32-p_i)+\tfrac12=2-p_i,\quad C_A=\tfrac{11}{10}<S,\quad C_B=\tfrac75>S.\]

FULL optimally continues A and stops B. Its minimum is `((11/10)+(5/4))/2=47/40`. At time 1 LR must apply the same stop/continue distribution to both labels; common stopping has cost `5/4` and common continuation has cost `((11/10)+(7/5))/2=5/4`. No real randomized mixing can improve either extreme, and terminal LR values are distinct (`9/5,1/5,6/5,4/5`), so the terminal Bayes action is LR-feasible. Thus

\[
 \boxed{\min_{\rm FULL} L=\tfrac{47}{40},\quad \min_{\rm LR}L=\tfrac54,\quad \Delta(0)=\tfrac3{40}>0.}
\]

An explicit FULL witness continues A, declares P on `+` and Q on `-`, and stops B declaring P:

\[
 \boxed{O^*=(\tfrac1{20},\tfrac34,\tfrac32,\tfrac32).}
\]

Consequently **every real seedless-LR observer** obeys the exact signed supporting plane

\[
 \boxed{8e_P+8e_Q+T_P+T_Q\ge10,}\qquad
8e_P(O^*)+8e_Q(O^*)+T_P(O^*)+T_Q(O^*)=\tfrac{47}{5}<10.
\]

The all-real LR observer-image distance from `O*` in `L_infinity` norm is at least `(10-47/5)/(8+8+1+1)=1/30`. This candidate is **convex-hull unequal**, hence does not solve the mother counterexample.

### 3. Collision splitting: an arbitrarily small TV perturbation erases the entire gap

For any real `0<|eta|<1/20`, keep both conditional signal kernels fixed, but take source marginals as in §1. At time 1,

\[r_1(A)=1+2\eta,\quad r_1(B)=1-2\eta,\]

which are distinct. At time 2 the four LR values are

\[
 r_2(A,+)=\tfrac95(1+2\eta),\quad r_2(A,-)=\tfrac15(1+2\eta),\quad
 r_2(B,+)=\tfrac65(1-2\eta),\quad r_2(B,-)=\tfrac45(1-2\eta).
\]

For `|eta|<1/20`, these respectively lie in four pairwise disjoint open intervals `(81/50,99/50)`, `(9/50,11/50)`, `(27/25,33/25)`, `(18/25,22/25)`. Therefore **the map `history → (t,r_t)` is injective at every decision stage**. Any FULL real behavioral action assignment can be re-indexed by its unique LR key, with exactly the same law of decisions/stopping/declarations. Conversely every LR strategy is a FULL strategy. Hence, for every such nonzero eta,

\[
 \boxed{\mathcal O_{\rm FULL}(\eta)=\mathcal O_{\rm LR}(\eta),\quad\Delta(\eta;w)=0\ \text{for every signed }w\in\mathbb R^4.}
\]

The full exogenous path distribution under P changes by total variation **exactly** `|eta|` (the source marginal changes; its conditional signal distributions are held fixed); Q does not change at all. Hence the gap is **discontinuous** at the exact collision:

\[
 \lim_{\eta\to0,\eta\ne0}\Delta(\eta;(1,1,1/8,1/8))=0\quad\ne\quad \Delta(0)=\tfrac3{40}.
\]

This jump concerns **which policies are measurable with respect to the exact LR information**, not a discontinuity in the underlying probability laws or an assertion about physical finite-resolution measurements. Exact LR equality, approximate LR equality and finite-resolution LR bins are different interfaces.

### 4. Fixed-collision stability and exact closed-form parameter box

Now keep `eta=0` but perturb conditional P signal probabilities to

\[p_A=\tfrac9{10}+\alpha,\quad p_B=\tfrac35+\beta,\qquad |\alpha|,|\beta|\le\tfrac1{20}.\]

Time-1 LR keys stay identical (`r=1`) and the four time-2 LR keys remain pairwise distinct. The inequalities `C_A<S<C_B` persist throughout this entire real parameter box. The same Bellman calculation gives

\[
 \min_{\rm FULL}L=\tfrac{47}{40}-\tfrac\alpha2,\qquad
 \min_{\rm LR}L=\min\{\tfrac54,\tfrac54-\tfrac{\alpha+\beta}{2}\}.
\]

Thus the **exact all-real support gap** for this two-parameter box is

\[
 \boxed{\Delta(\alpha,\beta)=\tfrac3{40}+\tfrac12\min(\alpha,-\beta)\ge\tfrac1{20}>0.}
\]

It is continuous and uniformly positive **within the same LR collision stratum**, in sharp contrast to §3. All source/path flows remain positive; the Q moments and exact P/Q Bayes likelihood ratios are explicitly preserved.

### 5. General stratification lemma and continuity bound

Consider any finite time-indexed, fully labeled stopping/decision tree with strictly positive path probabilities under P and Q. For a history `h` at time `t`, write `r(h)=P(h)/Q(h)`. Two same-time histories collide if and only if

\[\boxed{P(h)Q(h')-P(h')Q(h)=0.}\]

If P and Q path masses are polynomial/rational functions of underlying model parameters, the exact collision sets are algebraic (after clearing positive denominators). Absent a structural identity, each nontrivial collision equation cuts a proper algebraic subset of an open parameter domain. If all same-time LR fibers are singletons, FULL and seedless-LR have exactly the same *actual* observer image for every observer defined on the labeled stopping tree. This proves that an interesting gap can only be found on a nontrivial collision stratum. No generic-density assertion is made when collision equations are identities imposed by the model.

**Fixed-partition TV bound (exogenous full-trajectory formulation).** Suppose two models share the same finite labeled observation tree, allowed actions, and equivalence relation `h~h' iff (t,r(h))=(t,r(h'))`; their full exogenous path laws satisfy `TV(P,P')≤epsilon_P`, `TV(Q,Q')≤epsilon_Q`. If decision times lie in `[1,H]`, then for a fixed real behavioral policy (couple its local random choices identically), each error coordinate changes by at most its corresponding TV distance, and each expected stopping time changes by at most `(H-1)` times that distance. Thus for any real signed direction `w=(a,b,c,d)`, each optimal FULL or LR linear value changes by at most

\[M=(|a|+(H-1)|c|)\epsilon_P+(|b|+(H-1)|d|)\epsilon_Q.\]

Consequently the signed support gap `Delta=min_LR w·O - min_FULL w·O` satisfies `|Delta'-Delta|≤2M`. This is a continuity guarantee on a **fixed information partition**, with no claim of uniformity across a collision split. When `epsilon_P,epsilon_Q≤epsilon`, `H=2`, and `w=(1,1,1/8,1/8)`, one obtains `|Delta'-Delta|≤(9/2)epsilon` and strict separation from baseline for `epsilon<1/60`. The explicit two-parameter bound in §4 is stronger for its constrained family.

Proof of the finite TV bound: A fixed stochastic behavioral policy defines bounded measurable expected error indicators and stopping times as functions of an exogenous entire signal trajectory after integrating independent action coins. Total variation controls expectations of `[0,1]` functions by TV, and of `[1,H]` functions by `(H-1)TV`. Equal information partitions identify the same policy parameter space in both models. Infima of functions uniformly close by `M` are themselves close by `M`; applying this to both policy classes proves the bound. QED.

### 6. Actual verification, research value and status boundaries

`VERIFY.py` uses standard-library `fractions.Fraction` and exhaustive deterministic-policy enumeration. It checks: all 144 FULL deterministic policies versus 48 LR-compatible deterministic policies at `eta=0`; the exact extrema and explicit observer/separator; six nonzero rational eta points with 144 LR policies and equality of **actual deterministic observer sets**; 25 rational fixed-collision `(alpha,beta)` pairs and the exact gap formula. Output is in `EXACT_OUTPUT.txt`. All-real results are established by the finite-policy information-bijection/Bellman derivations above, *not* by the finite grid. Exact arbitrary-real randomized stopping is covered by the affine first-decision optimization and per-terminal LR Bayes optimality. The general TV theorem follows from the analytic proof, not finite tests.

**New limitation on candidate search:** a naïve positive-rational random perturbation of a source-sensitive LR collision can destroy the collision, causing a false impression that the ALL-signed hull test suddenly passed. Candidate generation should solve the exact polynomial collision equations before searching, record BRC labeled positive masses, and stratify results by their true `(time, LR)` fibers; numerical closeness must not be substituted for equality.

**Next actual scientific unit:** parameterize a genuinely coupled two-sensitive-merger four-observer model **on** an exact nontrivial collision variety, then pass/kill it using an ALL-signed rational convex-hull certificate (each FULL vertex an LR convex combination of ≤5 vertices, or a rational Farkas separator). On a passing candidate, use exact real semialgebraic nonmembership with boundary checks. This baseline two-step example is a methodological lemma, not such a passing candidate.