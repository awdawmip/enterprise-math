# R5 — 第二门 Jensen 残差的早门解锁定理与最小有理证书

Date: 2026-11-05 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Mother question: find a strictly positive finite P/Q stopping BRC with conv O4(FULL)=conv O4(seedless LR) but O4(FULL)≠O4(seedless LR), O4=(eP,eQ,TP,TQ). This note proves a constructive exact obstruction for a two-gate family, and a forced-first-gate conditional-kernel classification. It does not decide the mother question.

Frozen science pins: GLOBAL a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e. Current normative rules are read separately. Direct predecessor: 78eaac089b30f2fee8c3397bb5146c71ee39688b:research_notes/brc_r5_two_face_overlap_20261105_t0640/RESEARCH.md.

## 1. Typed finite BRC and observer

Two hidden source histories h=A,B have positive shared P/Q mass w_h, sum w_h=1, likelihood ratio 1. At t=1, STOP/P, STOP/Q and CONTINUE are available. Conditional on CONTINUE, t=2 ratio r_j>0 has Q probability K_j>0, common to sources, with sum K_j=1 and sum r_j K_j=1. At t=2 all three actions remain available. Conditional on CONTINUE at (h,j), the t=3 Q distribution M_hj(s)>0 has sum 1 and sum s M_hj(s)=r_j, so its P conditional probability is (s/r_j) M_hj(s)>0. At t=3 both P/Q declarations are free. FULL observes h and history; seedless LR observes only (t,r). Real randomized behavioral policies are allowed.

For a normal n=(-1,-k,0,d), k>0, define C_k(r)=max(-r,-k), the optimal immediate declaration reward, and

G0(k)=sum_j K_j C_k(r_j)-C_k(1),
G_hj(k)=sum_s M_hj(s) C_k(s)-C_k(r_j).

Both quantities are nonnegative Jensen improvements; G0 concerns the immediately observed time-2 key, G_hj the source-dependent future experiment. Let x_+=max(x,0).

## 2. First-gate-unlocked second-gate separation theorem

For some j*=j0 and k>0 assume delta=|G_Aj0(k)-G_Bj0(k)|>0 and

G0(k) > m := (G_Aj0(k)+G_Bj0(k))/2.

Then, with the legal four-dimensional normal n=(-1,-k,0,-m), both histories strictly prefer time-1 CONTINUE, so the first-gate Jensen residual is exactly zero; nevertheless

h_FULL(n)-h_LR(n) >= K_j0 min(w_A,w_B) delta / 2 > 0.

PROOF. At the time-2 key j put V_hj=G_hj(k)-m. The time-1 CONTINUE advantage for h is

Y_h=G0(k)-m+sum_j K_j (V_hj)_+ > 0.

Consequently FULL and LR both continue at time 1 when maximizing n. Their support difference is exactly the sum of the nonnegative time-2 Jensen defects

D= sum_j K_j [sum_h w_h(V_hj)_+ - (sum_h w_h V_hj)_+].

At j0 the two V values are opposite with magnitudes delta/2, and the bracket equals min(w_A,w_B)delta/2. All other terms are nonnegative. This uses Bellman recursion for the finite tree and therefore optimizes over every real behavioral policy. QED.

The theorem is a sufficient separability test for this model family, not a universal obstruction for different topologies. It gives a testable design direction: early observation of the first kernel may activate the first continuation gate without absorbing all downstream source information.

## 3. Exact legal two-gate witness

Let w_A=w_B=1/2; r=(1/2,1,3/2) and K=(3/8,1/4,3/8) for both sources. At r=1/2 use terminal s=(1/4,3/4), Q weights (1/2,1/2); at r=3/2 use s=(5/4,7/4), weights (1/2,1/2). At r=1 set common terminal s=(1/2,1,3/2); use M_A=(1/4,1/2,1/4) and M_B=(3/8,1/4,3/8). All P and Q probabilities are strictly positive and normalized.

At k=1: G0=3/16, G_A,mid=1/8, G_B,mid=3/16, m=5/32, delta=1/16. Set n=(-1,-1,0,-5/32). The exact time-2 advantages (low,mid,high) are

V_A=(-5/32,-1/32,-5/32),
V_B=(-5/32,+1/32,-5/32).

The time-1 continuation advantages are Y_A=1/32, Y_B=5/128; their Jensen defect is zero. The only nonzero second-gate defect is at mid r=1:

D_mid=K_mid min(w_A,w_B) delta/2=1/256.

Explicit Bellman supports:

h_FULL(n)=-287/256,
h_LR(n)=-9/8=-288/256,
gap=1/256.

A FULL witness: both sources CONTINUE at time 1. At time 2 declare P at r=1/2 and Q at r=3/2; at middle r=1 source A STOP/Q and source B CONTINUE, then declare P if s<1 and Q otherwise. Its exact observation is

W=(eP,eQ,TP,TQ)=(27/128,37/64,17/8,17/8).

Then n·W=-287/256. With ||n||_1=69/32, the separation implies

dist_infinity(W,conv O4(seedless LR)) >= 1/552.

No terminal declaration is restricted, and early stopping remains available in the full policy sets. Source history and every path Q mass are retained until the observer is evaluated.

## 4. Conditional-kernel rigidity in the forced-first-gate slice

Consider the same finite two-stage model but require CONTINUE at time 1 for both policy classes; allow source-dependent strictly positive K_hj instead of common K, with the same shared ratio r_j at each j. In this conditional submodel the following three statements are equivalent:

(i) conv O4(FULL)=conv O4(seedless LR);
(ii) O4(FULL)=O4(seedless LR) for all real behavioral policies;
(iii) for every shared j, all conditional terminal Q laws M_hj are identical across h.

PROOF OF (iii) => (ii). For every time-2 j, replace source-dependent actions by their Q-occupancy-weighted conditional average; identical M_j preserves the resulting time-3 (t,s) occupation. At terminal ratio s average P/Q declaration probabilities among histories arriving at s. Because P=sQ on each such fiber, the four O4 coordinates are unchanged. Reverse inclusion is immediate since LR is a subclass of FULL.

PROOF OF (i) => (iii). If M_hj differ at some shared j, the finite stop-loss transforms G_hj(k) differ at some k>0: the slopes/jumps of the function k -> E[max(-S,-k)] determine the law, with shared total mass and mean. Pick d strictly between -min_h G_hj(k) and -max_h G_hj(k). At this j, V_hj=d+G_hj(k) has strictly positive and strictly negative values. With time 1 forced CONTINUE, the local Jensen defect is strictly positive and the other j defects are nonnegative. Thus there exists n=(-1,-k,0,d) with h_FULL(n)>h_LR(n), contradicting (i). QED.

This classification concerns the forced-continue submodel. The preceding theorem separately supplies an explicit criterion for lifting a conditional difference into the original legal model where time-1 stopping is optional.

## 5. Actual computation, scope and next unit

Executed Python 3 standard-library Fraction verification (VERIFY.py), checking strict Q/P kernel normalization and conditional mean, the analytic Bellman formulas, an explicit FULL witness and independent exhaustive enumeration of 3,458 deterministic seedless LR policies (2 direct time-1 labels plus 3^3 second-gate action configurations times 2^7 terminal declarations). Every assertion passed; stdout is in EXACT_OUTPUT.txt. The general theorems are proved analytically; finite enumeration verifies the specified rational instance.

BRC reuse: explicit positive rational branch masses, source provenance, conditional P/Q likelihood ratios and retained (time,ratio) observer; no untyped reduction to total-only carrier. P000/ACTIVE WORLDVIEW unchanged. No independent review or Foundation admission is asserted.

Next: locate a two-gate family where every full-direction Jensen defect is zero but source-conditional history coupling survives, then test exact four-dimensional convex-hull equality by rational finite-fan or convex-membership certificates. If found, test real-image inequality semialgebraically. Also investigate whether terminal path overlap and additional stop resources permit cancellation beyond the sufficient-separation regime here.