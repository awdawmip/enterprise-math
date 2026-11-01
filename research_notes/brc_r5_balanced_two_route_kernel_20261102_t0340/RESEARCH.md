# R5 — two independent pre-J routes with exactly compensated downstream kernels

**Observed on:** 2026-11-02 (Asia/Shanghai). **Scientific status:** AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

**Frozen scientific input pins (unchanged):** `GLOBAL_KNOWLEDGE_V1 main@a01383f825ef9d43b4b754254303298c64041568`; `awdawmip/enterprise-math main@86149263e38c22292c9def1e0f69092efa1be77e`.

**Predecessor:** `awdawmip/enterprise-math@ad54b2dafe1004b33ad63e5f43144d0a4c97b8fd`, `research_notes/brc_r5_mixed_C_kernel_global_classification_20261102_t0244/{RESEARCH.md,VERIFY.py,NEXT_TASK.md}`. Current normative read: Global Knowledge `main@00b4d0b03dd693005b0e518a32af3f61f03e12fa`; Enterprise Math `main@56cad12f8e2de790486960eb99d49008b5f78261`. P000 Git blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488` is identical at the frozen/current source pins; protected ACTIVE worldview was read, not changed.

## Question

Does adding a second genuinely independent route into shared key J, with an **opposing source-dependent downstream kernel whose incoming mass exactly cancels the first source's departure**, remove the four-observer FULL/LR hull gap? Here is a complete answer for one strictly-positive one-parameter family. The mother target remains: find a finite two-law stop/continue model with equal four-observer convex hulls but unequal actual real behavior images.

## Fully specified finite two-measure experiment

The two measures are P and Q. An observable is `O=(e_P,e_Q,T_P,T_Q)`, where `e_P=P(final answer P)`, `e_Q=Q(final answer Q)`, and `T_P,T_Q` are expectations of terminal integer time. `FULL` sees source/path history; `LR` has one real Bernoulli action per shared `(time,P/Q likelihood-ratio)` key, with no shared random seed. Source-tagged P,Q mass is preserved throughout as the positive BRC carrier. Signed normals are only observer-level functionals, not signed physical masses.

Initially sources are `A1=A2=(1/8,1/8)` at `I=(1,1)`, `B=(1/4,1/8)` at `J=(2,2)`, `C=(1/4,1/3)` at `(1,3/4)`, and `D=(1/4,7/24)` at `(1,6/7)`. Total mass equals one in each law. At I, the action may stop answering P at time 1; otherwise nature terminates Q at time 2 with conditional P,Q fractions `(1/2,3/4)`, or sends `(1/2,1/4)` to J. At the distinct C and D keys the action may stop answering Q at time 1; otherwise nature terminates Q at time 2 or sends a branch to J. Define `0<=t<=7/32`, `delta=32t/7`:

- C's J branch conditional natural probabilities are `(2t/3,t/4)` under P,Q.
- D's J branch probabilities are `(7delta/12,delta/4)` under P,Q.

Every J branch has likelihood ratio 2. With both C,D continuing, J receives Q masses `t/12` and `t/3`, a **1:4 ratio**. Their respective P masses are twice these Q masses. The C/D upstream keys have distinct likelihood ratios (3/4 and 6/7), so they are genuinely separate actions before J. For `0<t<=7/32`, every specified natural conditional probability and its complement is strictly positive.

At J the action may stop answering P at time 2 or continue through the source-dependent post-J kernel. The A1/A2/B kernel is `N`, C's is `C`, D's is `D`. The following *conditional* P/Q coefficients specify **all** terminal branches and next-key branches; absent C routes are not edges:

| Outcome from J | N (P,Q) | C (P,Q) | D (P,Q) |
|---|---|---|---|
| Q at time 3 | (3/10, 1/4) | (3/5, 1/2) | (9/40, 3/16) |
| P at time 3 | (1/10, 1/8) | — | (1/8, 5/32) |
| K=(3,8/5) | (1/10, 1/8) | (2/5, 1/2) | (1/40, 1/32) |
| P at time 4 | (1/20, 1/16) | — | (1/16, 5/64) |
| Q at time 4 | (3/20, 3/16) | — | (3/16, 15/64) |
| L=(4,12/5) | (3/10, 1/4) | — | (3/8, 5/16) |

All present entries are strictly positive and column sums are 1 under each law. At K, the action can stop answering P at time 3; if it continues, nature answers Q at time 4 with `(1/4,1/2)` or sends `(3/4,1/2)` to L. At L, the action stops answering P at time 4 or answers Q at time 5. Every nonterminal destination preserves the exact claimed time and likelihood ratio.

**Exact source-weighted cancellation:** branch by branch and in both laws,

`D=(5*N-C)/4`, equivalently `C+4*D=5*N`.

Because the incoming Q masses of C,D are in the ratio 1:4, **their combined J-continuation kernel is exactly N when their upstream actions agree**. In particular, this cancellation holds before any observer compression; it is a positive two-law probability-flow identity. Independent upstream actions may change the ratio, and FULL can choose different J actions for C and D. This is precisely what the candidate tests.

## Theorem — compensated kernels still have an exact all-real support gap

For the experiment above, set `n=(14,-5,5,0)`. For **every real** `0<=t<=7/32`,

`max_{LR real policies} n·O = 8097/640 + (2657/192)*t`,

`max_{FULL real policies} n·O = 8097/640 + (14029/960)*t`.

Consequently,

**`max_FULL n·O - max_LR n·O = (31/40)*t`.**

At `t>0`, the FULL and LR four-observer convex hulls are distinct. A single explicit FULL witness achieves the upper support value and obeys

`dist_infinity(W(t),conv(LR)) >= (31/960)*t > 0`,

because `||n||_1=24`. At `t=0`, the actual real four-observer behavior images coincide by source-blind key-flow aggregation. Thus within this one-parameter family both actual images and convex hulls coincide exactly at the boundary `t=0`; all `t>0` have a strict observer gap.

A strictly positive rational instance is `t=7/64`, `delta=1/2`. It has the following legal deterministic FULL witness, with bits ordered `(p,rC,rD,qN,qC,qD,kN,kC,kD,lN,lC,lD)`:

`Wbits=(1,0,0,0,1,0,1,0,1,1,0,1)`.

Its observation is

`W=(689/1536, 7981/12288, 1723/768, 3067/1536)`.

The maximizing LR bit vector, ordered `(p,rC,rD,q,k,l)`, is `b*=(1,0,0,0,1,1)`. At `t=7/64`,

`n·W=175103/12288`, `max_LR n·O=870307/61440`, `gap=217/2560`, and

**`dist_infinity(W,conv(LR)) >=217/61440`.**

## Proof

1. All paths visit each decision key at most once. The LR behavior map is multi-affine in its six Bernoulli probabilities, so its image lies in the convex hull of the `2^6=64` deterministic LR observations. The same signed maximum is attained at one of those 64 vertices. Source/path-dependent FULL actions are similarly optimized deterministically. For a signed linear observer, histories with the same key likelihood ratio **and identical conditional future kernel** have identical Bellman action preference: A1/A2/B at J all use N, A1/A2 at I are identical, and the K,L future kernels are identical across all histories. Therefore the 12-bit reduced FULL class in the accompanying verifier attains the unrestricted FULL support maximum for the stated direction. This reduction is for *signed support optimization*; no observer-level quotient of the full source state is asserted.
2. Fix any of the 64 LR deterministic policies or 4096 reduced FULL policies. Every observation component is affine in `t`: all C/D incoming J masses are linear in `t`, their source-dependent conditional kernels are fixed, and no path contains two occurrences of a t-dependent natural branch. The same is true of `n·O`.
3. The exact Fraction verifier evaluates all 64 LR and 4096 reduced FULL deterministic policies at **both endpoints** `t=0,7/32` (8320 complete policy-observation evaluations). At *both* endpoints, the same LR vector `b*` and FULL vector `Wbits` attain their respective maximum. Since the difference between each of these candidates and every other corresponding vertex is affine in `t` and nonnegative at both endpoints, it is nonnegative throughout the entire real closed interval.
4. Direct exact evaluation of the maximizing LR observation gives `V(0)=(31/80,87/128,17/8,31/16)` and derivative `dV/dt=(11/24,-15/64,5/4,5/8)`. The maximizing FULL witness has the same base and derivative `dW/dt=(67/120,-53/192,13/12,13/24)`. Dotting with n yields the displayed affine supports and their difference `31t/40`. Positive gap implies separation of the full convex hulls, and Hölder's inequality gives the distance lower bound.
5. For `t=0`, neither C nor D enters J. At I,J,K,L all histories arriving at a shared key have the same source-blind conditional future kernel and the same P/Q ratio. For any FULL real policy, collect its Q occupancy and Q stop flow at each key and choose the LR stop probability as their ratio (arbitrary on zero occupancy). P occupancy and stop flow are the key ratio times Q flow. Source-blind natural transition then propagates equal P/Q flows inductively. Final answers and terminal-time expectations match. This establishes equality of actual real images at the boundary.

The argument in step 3 is an exact finite endpoint certificate *plus a proved interpolation law*, not a claim from finite sampled parameter values. Its scope is the declared auxiliary two-measure stopping model. P000 and native X6 geometry are unchanged; a native Heartbeat embedding and any physical calibration are separate open research questions.

## Executed evidence and current authority

`VERIFY.py` uses only Python standard-library `fractions.Fraction` and `itertools.product`; it checks normalization, the P/Q ratio at every visited I/J/K/L key, positivity of specified natural transitions, exact compensated kernel identities, all endpoint deterministic supports, explicit rational observation formulas, and three additional interior parameter regressions. Its captured, actual output is `EXACT_OUTPUT.txt`, ending `PASS_EXACT_R5_BALANCED_TWO_ROUTE_PROVENANCE_SEPARATION`.

Native gateway status observed 2026-11-02: version 0.6.11, `research_authority_granted=false`, `executor_binding_configured=false`, upstream `CODE_REVIEW_REQUIRED`, `active_jobs=5/5`. One current-owner bounded read returned `CONTROL_QUOTA`; the current canonical owner is therefore unconfirmed. This is independent author-side mathematical evidence, not a Source CLAIM, Result, Driver review or Foundation admission. The accepted mother objective remains open.

## Smallest next question

Can a **different** two-route topology with source-sensitive kernels yield an exact rational primal convex-combination certificate for **every** FULL deterministic four-observer vertex, even though the actual LR real image is smaller? For each candidate, first check this paper's n and other inexpensive exact normals; then perform all-signed hull membership with <=5 LR vertices per FULL vector, returning a rational Farkas separator on failure. Keep origin labels and branch-flow provenance until the observer safety question is settled.
