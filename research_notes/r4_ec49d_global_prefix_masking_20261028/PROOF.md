# EC49D — Exogenous-prefix no-masking, controlled-prefix masking, and delay threshold

**Date:** 2026-10-28 (Asia/Shanghai). **State:** AUTHOR_PROVED / EXACT_FRACTION_CHECK_PASS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. This author-side research follows EC49C PR #1623, immutable commit 00b0353661d9880e6ddea273d88ce83733c7aea8. This document is not a native Research-Activity, Task CLAIM, Result or accepted Foundation theorem.

## Objects and permitted operations

An **auxiliary positive-mass BRC branch observer** carries a finite common labeled sample space with strictly positive P and Q rational masses. Its information reduction hides a branch label W. It observes the **raw** four-vector
\[
O=(\alpha,\beta,E_PT,E_QT)
=(P(\mathrm{accept}),Q(\mathrm{accept}),E_PT,E_QT).
\]
At decision time T=1 it may reject, accept or continue. Continuation exposes a final informative signal at T=2 and then an accept/reject action. Randomized behavioral policies are arbitrary real and **source-neutral**. No true-source selector or retained secret random seed is allowed. T is an auxiliary two-stage counter, not physical Heartbeat time. This does not assert native X6 dynamics, signed-amplitude BRC, or an X6-to-probability theorem.

## Theorem 1 — no local spectral defect can be masked by a *fixed exogenous* observable prefix

Let Z be a finite, publicly observed **exogenous** prefix with positive masses q_z=Q(Z=z) and p_z=lambda_z q_z=P(Z=z). At each z a finite label W is ancillary to the source:
\[
P(W=w\mid z)=Q(W=w\mid z)=\kappa_z(w)>0.
\]
Each continued terminal signal Y has positive conditional kernels K_P^{z,w},K_Q^{z,w} and relative likelihood ratio R_{z,w}(y)=K_P^{z,w}(y)/K_Q^{z,w}(y). At T=1 the coarse policy sees z, the refined policy sees (z,w); at T=2 the coarse policy can see z and the **complete** terminal LR lambda_z R_{z,w}(y), and the refined policy may also retain w. Both have unrestricted source-neutral stop/accept/continue controls. Policies at the distinct publicly observed z branches are independently selectable: no cross-z budget or linked memory restriction.

Write the conditional terminal Q law of the relative LR as
\[
\nu_{z,w}(r)=\sum_{y:R_{z,w}(y)=r}K_Q^{z,w}(y).
\]
Then **the complete raw four-vector regions are identical, S_coarse=S_refined, if and only if at every reached z the conditional spectrum nu_{z,w} does not depend on w.**

**Sufficiency.** At each z, average the fine first-stage action probabilities with the common W weights kappa_z. At each terminal complete-LR fiber, set the coarse acceptance probability equal to fine continued-and-accepted **Q mass** divided by coarse continued **Q mass** on that fiber (arbitrary if the denominator is zero). Equality of the conditional LR spectra ensures these ratios are legitimate functions of z and current LR, without needing W. Since all atoms in one complete-LR fiber have the same P/Q ratio, equality of accepted Q mass also gives accepted P mass. Immediate source acceptance and both source-specific continuation masses match by W ancillarity, so both E_PT and E_QT match. This construction applies independently at each z and preserves each *raw* vector; refinement can ignore W for reverse inclusion.

**Necessity.** Suppose spectra differ at some z_*. The finite call transform
\[
C_w(\tau)=\sum_r\nu_{z_*,w}(r)(r-\tau)_+,\quad
D_w(\tau)=C_w(\tau)-(1-\tau)_+\ge0
\]
determines the spectrum: C is piecewise linear with knots at the positive LR values, and its one-sided slope changes recover the Q atom weights. Therefore for some nonnegative threshold tau, D_w(tau) differs with w (a rational support knot suffices for rational kernels). Choose any c strictly between its minimum and maximum, and use the **single global** linear functional
\[
L(O)=\alpha-\lambda_*\tau\beta-
 \frac{\lambda_*c}{1+\lambda_*}(E_PT+E_QT),
\quad \lambda_*=\lambda_{z_*}.
\]
The exact local support improvement at z_* is
\[
G_*=\lambda_* q_*\left[
 \sum_w\kappa_*(w)(D_w(\tau)-c)_+
 -\Big(\sum_w\kappa_*(w)D_w(\tau)-c\Big)_+
 \right]>0.
\]
Indeed the first-stage stop-now contrast is (1-tau)_+ per unit P mass; continuing yields an extra D_w and incurs normalized cost c. Optimization at both stages is linear in behavioral probabilities. Positivity of all kappa and choice of c across the kink makes the bracket strictly positive. Refinement can ignore W at **every other** z and hence their optimized L-values never decrease. Because policies at z are independently selectable and the prefix law is exogenous, the global support supremum is the **sum of conditional suprema**, plus a common baseline. It therefore increases by at least G_*. Strict support separation proves the raw sets unequal regardless of nonconvexity. This proves both directions.

**Exact rational certificate method.** At each z aggregate Q mass by the reduced LR. When two conditional spectra differ, choose a rational knot tau where the D values differ and a rational midpoint c of their minimum/maximum. The displayed L and positive G_* are a finite rational global inequality certificate. The other prefix states need not have the same lambda.

## Example 1 — eight strictly positive leaves, unmaskable fixed prefix

Let P(Z=0)=Q(Z=0)=1/3; conditional on Z=0 use the four (W,V) leaves shown below. Let P(Z=1)=Q(Z=1)=2/3; conditional on Z=1 draw W and V independently fair under both P,Q, so each of its four **unconditional** leaves has P=Q=1/6. All eight leaves are positive and both P/Q measures normalize to one.

For
\[
F'(O)=\alpha-\beta-\frac3{16}(E_PT+E_QT-2),
\]
the coarse maximum equals 0 and the refined maximum equals 1/48. At Z=0 the maxima are respectively 0 and 1/16 (below); at Z=1 both are 0 because P=Q and continuation has positive cost. Refined policy: if Z=0 and W=0 continue, otherwise stop/reject; after continuing, accept iff current LR>1. It realizes
\[
O_{\rm fixed}=(1/8,1/24,7/6,7/6),\qquad F'(O_{\rm fixed})=1/48.
\]
This explicitly checks the noncancellation phenomenon with two positive-mass prefix states.

## Exact local four-leaf kernel

| W,V | P | Q | P/Q |
|---|---:|---:|---:|
| 0,0 | 1/8 | 3/8 | 1/3 |
| 0,1 | 3/8 | 1/8 | 3 |
| 1,0 | 1/4 | 3/8 | 2/3 |
| 1,1 | 1/4 | 1/8 | 2 |

Here P(W)=Q(W)=1/2. Conditional Q spectra are nu_0={1/3:3/4,3:1/4} and nu_1={2/3:3/4,2:1/4}. At tau=1, D_0=1/2 and D_1=1/4. With c=3/8 the local gap equals
\[
\frac12(1/2-3/8)_++\frac12(1/4-3/8)_+
-\big((1/2)(1/2+1/4)-3/8\big)_+=1/16.
\]
The coarse F' optimum is 0, refined optimum 1/16. Refined witness O_A=(3/8,1/8,3/2,3/2), outside the coarse convex hull. The four terminal current-LR values are distinct, so the coarse terminal LR identifies (W,V) when continuation occurs. This is the local EC49C building block, not a new claim to the classical information-order principle.

## Theorem 2 — a controllable alternative route masks strict *local* loss globally

Introduce an independent ancillary fair coin U, with P(U=u|W,V)=Q(U=u|W,V)=1/2. The fixed latent space consists of the **eight positive** atoms (W,U,V), with P8(w,u,v)=P(w,v)/2 and Q8(w,u,v)=Q(w,v)/2. Before seeing any hidden value, a controller chooses a publicly observed **route A or B** (potentially randomized). Both routes have the **same** P/Q kernels and the **same** stopping clock; the route is an *action*, not a source-revealing latent random variable.

At T=1: route A hides W,U from coarse but shows W to refined; route B shows (W,U) to **both**. At T=2 after continuation: A coarse sees the exact complete LR, A refined also has W, and B sees (W,U,V) to both. B is strictly richer as an observation (it additionally reveals ancillary U), yet is shared.

**Claim.** Although route A alone has the strict 1/16 fine/coarse support gap,
\[
S_{\rm coarse,global}=S_{\rm refined,global}=S_B
\]
as **raw four-vector sets for all real source-neutral behavioral root/continuation policies**. Thus local spectral mismatch at a *controllable* reachable prefix is not necessary evidence of global information loss.

**Constructive proof.** Every route-A downstream strategy can run on B by ignoring extra observed labels. Fix an arbitrary mixed root policy, with weights theta_a (a=A,B), and regard its route-specific downstream policies as functions on B histories h=(w,u). Write r_a(h),s_a(h),c_a(h) for reject/accept/continue probabilities and t_a(h,v) for terminal accept probability (A functions ignore unobserved variables). Construct one B-only policy by
\[
r_*(h)=\sum_a\theta_a r_a(h),\quad
s_*(h)=\sum_a\theta_a s_a(h),\quad
c_*(h)=\sum_a\theta_a c_a(h),
\]
\[
t_*(h,v)=
 \frac{\sum_a\theta_a c_a(h)t_a(h,v)}{c_*(h)}
\quad(c_*(h)>0),
\]
and arbitrary terminal t_* if c_*=0. At **each fixed latent atom** (w,u,v) the accept and continue probabilities are exactly the root-averaged originals. Since P8,Q8 are identical kernels across routes, summing these probabilities against **either** measure reproduces the same alpha,beta,E_PT,E_QT. This uses neither the source identity nor a retained random route seed. Consequently all global fine/coarse policies are simulatable by the shared B route, and B itself is available in both models. Equality of the full raw regions follows. In particular the local A refined witness can be implemented globally by the coarse B route simply by observing W, ignoring U and applying the same decision rule.

## Theorem 3 — exact route-delay boundary

In a separate declared model family, route B incurs an extra source-independent time-accounting offset delta>=0 to **both** expected stopping times (A has no offset), with the observation kernels unchanged. This abstract offset may be fractional; integral offsets can be realized as extra discrete clock steps.

For the same F', the optimized coarse and refined global support values are exactly
\[
V_c(\delta)=\max(0,1/16-3\delta/8),\qquad
V_f(\delta)=1/16.
\]
Proof: route A has maxima 0 and 1/16; B has maximum 1/16 for both at zero delay, reduced by (3/16)*2delta=3delta/8. Root mixing cannot exceed the maximum arm support of a linear objective. Hence
\[
V_f(\delta)-V_c(\delta)=\min(1/16,3\delta/8).
\]
At delta=0 the above constructive **raw** equivalence holds; for every delta>0 there is strict global support separation. The gap saturates when delta>=1/6. No physical heartbeat-time calibration follows from this abstract auxiliary accounting model.

## Verification, prior art and limitations

Run VERIFY.py with ordinary Python; EXACT_REPORT.json contains its actual stdout. All calculations use exact fractions.Fraction: 48 A-coarse, 144 A-refined and 20,736 B-public deterministic policies (20,928 total); 1,400 seeded rational mixed-root policies; positive leaves, source normalization, exact supports, deterministic inclusions, fixed-prefix witness and six delay values all pass. Finite enumeration establishes the model-specific linear support optima, not the all-real theorems. Those follow from the explicit conditional Q-mass construction, independent-prefix support decomposition and root-policy simulation above. There is no general quantifier-elimination run, Lean/Coq proof or native P000 X6 experiment.

Historical/information-theoretic background: David Blackwell, “Equivalent Comparisons of Experiments,” Ann. Math. Stat. 24(2):265–272 (1953), DOI 10.1214/aoms/1177729032; Khan–Yu–Zhang (2025), Economics Letters 247:112146, DOI 10.1016/j.econlet.2024.112146; Monahan (1982), Management Science 28(1):1–16, DOI 10.1287/mnsc.28.1.1. EC49D does **not** claim Blackwell information comparison or POMDP sufficient-statistic principles as first discoveries. The new scoped distinction is *fixed exogenous multiple-state no-masking versus controlled-route full raw masking*, with a sharp explicit delay threshold.

NEXT_TASK.md preserves the two-future-decision open unit. P000/ACTIVE worldview and Source task ownership are untouched. Current Gateway read had research_authority_granted=false and the current-owner query returned CONTROL_QUOTA; this material remains author-side, unreviewed and not formally admitted.
