# R5: Exact two-parameter time-hull rigidity of the three-class STOP tree

Date: 2026-10-30 Asia/Shanghai. Researcher-ID: EM-R5-2BDD96 (locally allocated; REGISTER_PENDING). Evidence classification: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED. This is author-side finite probability mathematics, not a Source CLAIM/Result, Driver review, or native X6 physical inference.

## Frozen sources
GLOBAL_KNOWLEDGE_V1 canonical main: d824e268516f38a10dcb58e45cd2bb58c0fd70b3. Enterprise Math canonical main: 00d5d6d954eb542ef8d3d9cb9924304757c6318b. Scientific predecessor: research_notes/brc_r5_threeclass_time_only_obstruction_20261030_t2240/RESEARCH.md at 36f3433b3142fa5234afdd4ccd0fdb9bf76b8392 (Draft PR #1663). Read global bootstrap/manual/P000/ACTIVE worldview and local portable-research/operations contracts. P000 and ACTIVE worldview unchanged.

## Fixed natural tree; two real parameters
Nature draws X∈{0,1}, U∈{0,1}, V∈{0,1,2}. Q(X,U)=(3/8,1/8,1/8,3/8) in (00,01,10,11) order. The stage-3 likelihood ratios are r_0=3/4 and r_1=5/4. The terminal ratios are R=(1/2,1,3/2). Let t0,t1∈(0,1/4). With t=t_x, stage-4 conditional Q laws are
~~~
K_(x,0)=(1/2+t, 1/2-2t, t)
K_(x,1)=(t, 1/2-2t, 1/2+t).
q_xuv=Q(x,u)K_(x,u)(v), p_xuv=R_v q_xuv.
~~~
Every one of the twelve p,q masses is positive; both measures sum to 1, and Σ_v K_(x,u)(v)R_v=r_u exactly. Time-2 ratios for X=0,1 are 7/8 and 9/8. At time 3 FULL remembers X while LR sees U from the likelihood-ratio class; at time 4 LR sees V. STOP at decisions 2,3,4 absorbs immediately, CONTINUE from 4 absorbs at 5. Real behavioral probabilities lie in [0,1]; LR has no persistent shared random seed. Time observations are (T_P,T_Q).

## Theorem: all-real time-hull classification and exact quantitative separator
For every real t0,t1∈(0,1/4):
~~~
conv(T_FULL)=conv(T_LR)  iff  t0=t1.
~~~
For t0≠t1, let
\[
\ell(t)=\frac{5-2t}{6-4t},\qquad
\lambda_*=\frac{10-3t_0-t_1}{2(6-3t_0-t_1)},\qquad
H_*=T_P-\lambda_* T_Q.
\]
Then
\[
\boxed{\sup_{\mathrm{FULL}} H_*-\sup_{\mathrm{LR}} H_*
=\Delta_*=\frac{3|t_1-t_0|}{16(6-3t_0-t_1)}>0.}
\]
The gap is strictly bounded by
\[
|t_1-t_0|/32<\Delta_*<3|t_1-t_0|/80.
\]
A concrete maximizing FULL deterministic witness has distance at least Δ*/(1+λ*) from the whole real LR time-image in the infinity norm. The time-only separation persists regardless of ANY legal terminal error probabilities that leave natural path masses, stop times, action sets and predecision information unchanged. Consequently the FULL/LR four-observer convex hulls differ whenever t0≠t1.

If t0=t1, conditional next-LR transitions are lumpable. By exact seedless occupancy Markovization, the actual real (T_P,T_Q) images coincide. With the additional requirement of LR-state-measurable P/Q terminal error rewards, the actual four-observer sets (e_P,e_Q,T_P,T_Q) also coincide. This diagonal four-image conclusion is not asserted for source-sensitive error rewards.

## Analytic proof (all real behavioral strategies, not just a grid)
1. A trajectory visits each control key at most once. Holding other behavioral parameters fixed, any expected linear stopping-time payoff is affine in one control parameter. It is therefore multiaffine on each compact FULL/LR policy cube, so every support maximum occurs at a deterministic policy vertex.

2. Optimize H=T_P−λT_Q for λ∈(5/6,9/10). A unit Q mass with likelihood ratio r receives CONTINUE-over-STOP payoff r−λ for one additional time step. At stage 4 the optimized gains for V=0,1,2 are L=(0,1−λ,3/2−λ). The stage-3 CONTINUE-over-STOP gains per Q(x,u) are
\[
G_{x0}=5/4-(3/2)\lambda+t_x(\lambda-1/2)
=(3/2-t_x)(\ell(t_x)-\lambda),
\quad
G_{x1}=5/2-2\lambda+t_x(\lambda-1/2)>0.
\]
The derivative \ell'(t)=2/(3−2t)^2>0, so \ell(t)∈(5/6,9/10). Set
\[
w_0=(3/8)(3/2-t_0),\quad w_1=(1/8)(3/2-t_1).
\]
Then λ*=(w0\ell(t0)+w1\ell(t1))/(w0+w1). Thus λ* lies strictly between the two thresholds if unequal, and
\[
(3/8)G_{00}+(1/8)G_{10}=0,
\]
while G00,G10 have opposite strict signs.

3. Every FULL support optimizer continues at time 2 in both X sources: the optimal source-specific CONTINUE gain E_x^F=Σ_u Q(x,u)[r_u−λ+max(0,G_xu)] has lower bounds
\[
E_0^F\ge B_0=(3/4)(1-\lambda)+(t_0/8)(\lambda-1/2)>3/40,
\]
\[
E_1^F\ge B_1=3/2-(5/4)\lambda+(3t_1/8)(\lambda-1/2)>3/8.
\]
It continues at time 3 whenever U=1, and makes the independent optimal sign choice at U=0.

4. For LR, early stopping at either source loses at least E_x^F>3/40 against FULL, whereas the explicit LR candidate that continues at both source nodes and at U=1 is only Δ*<3/320 from FULL. Hence an LR support optimizer cannot stop early. Given both early CONTINUE choices, skipping U=1 loses strictly positive Σ_x Q(x,1)G_x1. With U=1 CONTINUE, both U=0 choices give identical LR support because the weighted G gains sum to zero. For either choice early continuation remains strictly profitable: G_x0>−1/10, B0>3/40 and B1>3/8. Thus the LR maximum is exactly this balanced policy value.

5. FULL additionally collects the positive side of the two opposite-sign U=0 gains:
\[
\Delta_*=(3/8)\max(0,G_{00})+(1/8)\max(0,G_{10})
=(3/8)|G_{00}|=(1/8)|G_{10}|.
\]
Use
\[
\ell(t_1)-\ell(t_0)=
\frac{2(t_1-t_0)}{(3-2t_1)(3-2t_0)}
\]
to obtain Δ*=[w0w1/(w0+w1)]|\ell(t1)−\ell(t0)|=3|t1−t0|/[16(6−3t0−t1)].
The exact LR maximum is
\[
\sup_{LR}H_*=17/4-4\lambda_*+((t_0+3t_1)/8)(\lambda_*-1/2).
\]
The FULL maximum is this plus Δ*. Take the explicit FULL witness: early CONTINUE at both sources; time-3 CONTINUE for U=1 and for the one X with positive G_x0, STOP at the other U=0 history; time-4 STOP at V=0, CONTINUE at V=1,2. The dual norm inequality |H*(z)−H*(w)|≤(1+λ*)||z−w||∞ proves strict actual-image separation. If t0=t1, all conditional next-LR kernels at the shared U class agree; the predecessor's seedless occupancy construction matches all time observations, and all four when error rewards are LR-local. QED.

## Sharper exact certificate at the previously studied masses
For t0=1/16, t1=1/8: ell(t0)=39/46, ell(t1)=19/22, λ*=155/182,
\[
\sup_F H_*=1259/1456,\quad
\sup_{LR}H_*=157/182,\quad
\Delta_*=3/1456.
\]
Equivalently H'=182T_P−155T_Q has exact support gap 3/8; the infinity-norm distance bound is 3/2696. This improves the prior fixed direction 7T_P−6T_Q with bound 1/1664 in the same model. The raw gaps have different direction scales; the infinity-norm bounds are directly comparable.

## Typed BRC use and validation boundary
The carrier is the twelve positive, source-labeled P/Q branch masses (exact rational at rational parameters, symbolic positive real for the all-real family). LR compression at time 3 erases X. Before the future transition operation,
\[
K_{0u}-K_{1u}=(t_0-t_1)(1,-2,1),\quad
\|K_{0u}-K_{1u}\|_{TV}=2|t_0-t_1|.
\]
The exact support defect equals 3 TV/[32(6−3t0−t1)]. This is a positive-mass provenance/future-observer residual, not amplitude cancellation or a native X6/Heartbeat physics result. Ordinary exact finite P/Q arithmetic is applicable; native Heartbeat BRC-only arithmetic is not invoked.

The attached standard-library Fraction checker verifies conditional martingale identities, 12 positive P/Q masses and two measure normalizations, stage-3 gains, weighted cancellation and exact gap for 49 rational parameter pairs. It independently exhausts 262144 FULL and 128 LR deterministic policies at each of three parameter pairs (786432 FULL and 384 LR), and captures actual stdout. The all-real quantifiers rest on the analytic proof above. No independent acceptance or literature novelty priority is asserted.

## Actual authority and successor
At the read checkpoint the native directed context reported authority_granted=false and complete_task_packet=false; the active task-owner query returned CONTROL_QUOTA. This author-side work remains REGISTER_PENDING, UNREVIEWED, NOT_ADMITTED. The role ID does not assert Source ownership.

Next independent unit: vary the positive upstream Q(X,U) weights and the ratio grids while preserving exact collision identities and first certify 2D time-hull equality; or on diagonal t0=t1 search genuinely source-sensitive terminal rewards with exact 4D rational vertex containment/Farkas certificates. Only then test seedless LR real-image membership. Preserve strict positive branches, author provenance, source pins and complete exact evidence.