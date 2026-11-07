# EC49G — Action-selected sensing: marginal likelihood-ratio spectra do not preserve adaptive observation

**Status:** author-side proved finite-model separation, exact rational verification; `UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING`. Date: 2026-10-28. Role: `TASK_RESEARCH`, researcher identity **not native-issued** in this run. Scope is a finite **positive-rational two-source BRC auxiliary observation model**, not native signed BRC or X6 heartbeat physics. Parent: EC49F, immutable `c4d82147b86b3e5e372f760b3b1615cb7e5542db` (Draft PR #1633). Nothing here changes P000 or ACTIVE worldview.

## 1. Exact scientific question and typed carrier

Does preserving the **individual action-marginal likelihood-ratio histogram** for each of two genuinely selectable sensor actions A and B, together with their fixed rational acquisition clocks, suffice to forget a source-neutral initial history label W, if the observer may adaptively choose acquisition order and a second acquisition?

The carrier is the eight labeled terminal branches `(W,A,B)` with strictly positive masses in each source `P,Q`. Alternative branches add masses; conditionals divide exact rational masses; acquisitions reveal one of A or B at cost `tau_A=2`, `tau_B=3/2`; each sensor may be acquired at most once. The observer may accept, reject, buy A or buy B initially, then accept/reject or buy the remaining sensor, and finally accept/reject. `T` is **total acquired auxiliary clock cost**, not physical heartbeat time. Full observer sees W for free; coarse observer cannot see W and observes only acquired signals. Both use a single source-independent causal behavioral policy. Both P and Q assign `Pr(W=0)=Pr(W=1)=1/2`.

The raw observable vector, with exact interpretation, is

`O=(alpha,beta,E_P T,E_Q T)` where `alpha=P(accept)`, `beta=Q(accept)`.

No shared random variable reveals W to the coarse observer. Randomization may be real-valued; the control tree is finite and has perfect recall of selected actions and observed outputs.

## 2. Complete strictly positive rational model

The following entries are **conditional on W**. Multiply every entry by `1/2` to obtain joint `(W,A,B)` masses. Within every W, each source sums to one.

| W | (A,B) | P(A,B given W) | Q(A,B given W) |
|:--:|:--:|--:|--:|
|0|11|1/2|1/12|
|0|10|1/4|1/6|
|0|01|1/6|1/4|
|0|00|1/12|1/2|
|1|11|7/12|1/6|
|1|10|1/6|1/12|
|1|01|1/12|1/6|
|1|00|1/6|7/12|

Every one of the 16 source-specific joint probabilities is strictly positive. For both `W=0` and `W=1`, the **action-specific marginal** mass pairs are:

- A=1: `(P,Q)=(3/4,1/4)` and likelihood ratio `3`; A=0: `(1/4,3/4)` and likelihood ratio `1/3`.
- B=1: `(P,Q)=(2/3,1/3)` and likelihood ratio `2`; B=0: `(1/3,2/3)` and likelihood ratio `1/2`.

Thus neither the *full per-action output distribution under each source* nor its likelihood-ratio spectrum carries W. But joint action-conditioned predictions **do** differ. After taking action B and seeing `B=1`, the complete prefix likelihood ratio is `2` for both W branches, while

`Q(A=1 | W=0,B=1)=1/4` and `Q(A=1 | W=1,B=1)=1/2`.

Consequently an attempted quotient discarding W violates action-conditioned Q-kernel lumpability **even after the acquired B output and the exact prefix likelihood ratio agree**. It erases an adaptive-value structural residual; a first-step histogram alone cannot establish future-operation safety.

## 3. Rational support separation and exhaustive finite proof

Define the linear support functional

`H(O) = alpha - 2 beta - (E_P T + E_Q T)/24`.

An available decision `accept` at a prefix with P and Q masses `p,q` yields local support `p-2q`, and `reject` yields `0`. If an unacquired sensor `s` is purchased, it incurs `-(tau_s/24)*(p+q)` and yields the sum of the optimized subbranch supports. Therefore the exact Bellman recursion is

`V(p,q; prefix) = max(0, p-2q, max_{s unacquired} [-(tau_s/24)(p+q) + sum_{z=0,1} V(p_z,q_z; prefix,s,z)])`.

All terms are rational; terminal prefixes have no purchase actions. The recursion enumerates all deterministic history-dependent policies under the declared acquisition interface. Equivalently, at the root there are exactly `2+2*(2+2^2)^2 = 74` pure policies: immediate reject/accept, or choose a first sensor (2 ways), with for each of its two outputs either immediate reject/accept or buy the remaining sensor and use one of four binary acceptance masks (6 choices per output). When W is visible, one policy may be chosen separately for each W, giving `74^2=5476` deterministic full policies. On a finite acyclic perfect-recall control tree a linear objective reaches its maximum at a deterministic behavioral strategy, so the exact rational maxima below apply to arbitrary source-neutral real randomized strategies as well.

The verifier obtains the **root maxima by first action**, with the branch recursion exactly realized by enumerating the 74 trees:

| W knowledge | Reject | Accept | Buy A first | Buy B first | Overall |
|---|---:|---:|---:|---:|---:|
| W=0 | 0 | -1 | 5/48 | **1/8** | **1/8** |
| W=1 | 0 | -1 | **1/12** | 1/24 | **1/12** |
| W hidden; mixture law | 0 | -1 | **1/12** | **1/12** | **1/12** |

The coarse observer sees the mixture of W=0 and W=1 laws, since W is source-neutral and no acquired single sensor reveals W at root. Hence its support maximum is exactly `1/12`.

With W visible, choose the following explicit policies:

- **W=0:** purchase **B**. If B=0, reject. If B=1, purchase **A**, then accept exactly when A=1.
- **W=1:** purchase **A**, then accept exactly when A=1; no second purchase.

Their conditional four-vectors are respectively

`O_0=(1/2,1/12,17/6,13/6)` and `O_1=(3/4,1/4,2,2)`.

Averaging over source-neutral W gives the **fully implementable exact vector**

`O_full=(5/8, 1/6, 29/12, 25/12)`.

Its functional value is

`H(O_full)=5/8-2*(1/6)-(29/12+25/12)/24 = 5/48`.

For **every** coarse behavioral policy, including any real randomization, exact enumeration plus extremality establishes `H(O_coarse) <= 1/12 = 4/48`. Therefore

`H(O_full) - sup_{O in S_coarse} H(O) = 1/48 > 0`.

This rational separating hyperplane proves `O_full` lies **outside even the convex hull of the coarse region**, so `S_full != S_coarse`. It also witnesses an **action-choice reversal**: W=0 optimally buys B first, W=1 optimally buys A first; the different clocks `(2,3/2)` matter. It is not merely the fixed-order two-future-signal obstruction already recorded in EC49E.

## 4. Action-and-clock aware sufficient quotient theorem

**Proposition (finite rational causal LR/action-kernel lumpability, constructive sufficient condition).** Consider a finite-horizon positive-rational two-source observation/control tree with source-neutral behavioral policies, arbitrary legal stop/accept/reject/acquisition actions, and a class map `h -> s` that (i) is observable and causally updateable from the compressed history; (ii) includes stage, remaining action budget, and **exact P/Q prefix likelihood ratio** `r(s)>0`; (iii) makes the legal action set and each action's rational auxiliary clock increment `tau(s,a)` identical within every class; and (iv) for every permitted action, the **conditional Q distribution on successor classes** is identical for all fine histories in a class. Then the full and compressed **raw** four-vector regions `S={(Paccept,Qaccept,E_PT,E_QT)}` are equal even with arbitrary real source-neutral behavioral randomization, and the region is a rational occupation-flow LP projection. Every rational feasible raw vector has a rational compressed behavioral witness.

**Proof.** Given any full behavioral strategy, let `x_Q(s,a)` be the sum of Q prefix masses on active fine histories of class `s` choosing action `a`; let `d_Q(s)=sum_a x_Q(s,a)`. For each such fine history the policy/action choice likelihood cancels in its two-source likelihood ratio, and by (ii) this ratio equals `r(s)`; hence `x_P(s,a)=r(s)x_Q(s,a)`. By (iv), flow to any successor class `s'` equals `sum_{s,a} K_Q(s,a,s') x_Q(s,a)` with well-defined rational `K_Q`. Set the compressed policy to `pi_s(a)=x_Q(s,a)/d_Q(s)` for positive `d_Q(s)` (arbitrary legal choice if zero). Causal updateability and finite horizon reconstruct exactly these Q flows by induction. Classwise LR equality reconstructs the P flows. Stop/accept mass satisfies `beta=sum_s x_Q(s,accept)`, `alpha=sum_s r(s)x_Q(s,accept)`; cost-flow equality gives `E_Q T=sum_{s,a} tau(s,a)x_Q(s,a)` and `E_P T=sum_{s,a} r(s)tau(s,a)x_Q(s,a)` for acquisition actions. All four components match exactly. Conversely, every compressed policy is implementable on the full tree because the class is causally readable, giving equality of *raw* regions, not merely of their hulls. All flow, normalization and output equations have rational coefficients; a rational right-hand-side feasible bounded rational polyhedron contains a rational basic feasible point. Its rational action-flow ratios supply the claimed rational behavioral policy. QED.

The proposition is an application in the present typed observer/cost interface of established predictive-state and stochastic-bisimulation ideas; **no general originality priority or necessity/minimality is claimed**. Its action-by-action kernel condition is **strictly stronger than** maintaining each action's one-step marginal likelihood-ratio histogram. The preceding eight-leaf model demonstrates precisely why that weakening is unsound.

## 5. Evidence, exact scope and unresolved bridge

Run `python VERIFY.py` (Python standard library only), capture stdout, and compare with `EXACT_REPORT.json`. The program checks strict positivity and normalization of all eight labeled atoms per source, one-step P/Q marginals, the Q-kernel mismatch after B=1, all 74 coarse deterministic policies, all 5476 W-visible pure policy pairs, the root action support table, explicit full four-vector and the strict rational support gap. The 5476-case test is exhaustive **only for this exact finite two-action/two-acquisition model**; the general quotient proposition is an algebraic proof, not a finite-test extrapolation.

**BRC reuse classification:** `COMPOSE_APPLIED` — branchwise positive P/Q masses and source-provenance are the carrier; alternative sum and serial conditionalization are actually used; W is a proposed quotient; `H` audits observer/future-operation preservation. Signed amplitudes, phase cancellation, native rotations, X6 six-space and heartbeat time are **not present** in this carrier. A native transfer requires explicit six-axis cell/path/ports, signed BRC operation typing, time interpretation, and a demonstrated map preserving acquisition/readout and future transition relations.

**Owner/authority scope:** In this run GitHub `awdawmip` has repository push permission. Native site gateway reports `research_authority_granted=false`, static read-only scopes, and the bounded owner/task query returned `CONTROL_QUOTA`. Thus the live winning owner/CLAIM was not authenticated; no native registration, Result, review or canonical task publication is asserted. The GitHub Draft is **author-side portable handoff evidence**, not official mathematical admission.
