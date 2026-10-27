# R5 — A complete parametric ten-leaf BRC hull-exclusion theorem

Date: 2026-10-27. **PORTABLE AUTHOR / UNREVIEWED / NOT_ADMITTED**. This concerns an external finite positive two-measure decision tree, not native heartbeat dynamics, a P000 theorem, a formally claimed Task, a Result, or independent review.

Frozen inputs: GLOBAL_KNOWLEDGE_V1 main@d9c91d03eff26a0dfeb2bba85ce7d0a467f35c23 (bootstrap, manual, P000 projection matching original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE worldview, math and code rules); enterprise-math main@d8b1a8272420500b67ddc04033ca9577f7c1f3f8 (portable and autonomous research protocols). Predecessors: research_notes/brc_lr_affine_circuit_duality_20261027_r5/PROOF.md and research_notes/brc_n3_optional_early_stop_activation_masking_20261027_r5/PROOF.md. Native owner lookup returned CONTROL_QUOTA. The contributor uses an explicitly local author activity without a native CLAIM.

## Positive BRC branch model

Let rational parameters satisfy 0<c<1, 0<delta<1, 0<eps<1, 0<p_B<p_A<1/2. At time 1 histories A,B each have P=Q=1/2 and likelihood ratio 1. Conditional on either history, time 2 branches C,L,H with Q probabilities (c,(1-c)/2,(1-c)/2) and likelihood ratios (1,1-delta,1+delta). Conditional on C, the time-3 likelihood ratios are (1-eps,1,1+eps); the Q kernels after A and B are respectively K_A=(p_A,1-2p_A,p_A) and K_B=(p_B,1-2p_B,p_B). L and H have one last leaf retaining their time-2 likelihood ratio.

The ten terminal Q masses are products of the stated positive factors. Each terminal P mass is its terminal likelihood ratio times the corresponding Q mass. Every kernel has mass one and the expected child ratio equals its parent ratio. Consequently all ten P and Q leaf masses are positive and normalized. Retain hidden path identities until observer safety has been proved; this is T0 positive-weight BRC and T6 observer-safe quotient reuse (REUSE_APPLIED). Signed support defects are not positive BRC masses.

A full-history behavioral policy may stop and classify at times 1 or 2, and must classify at 3. A seedless LR policy conditions its independently sampled local actions only on (time, LR). The observer is O=(P(declare Q),Q(declare P),E_P tau,E_Q tau). Both strategy classes allow every real local action probability in [0,1].

## Theorem: rational positive-price separator for every unequal pair

Let b=(1-c)*delta/2, d_A=eps*p_A, d_B=eps*p_B and dbar=(d_A+d_B)/2. Set J_s(O)=O_1+O_2+s*O_4 for real s>=0, and let V_full and V_LR be the minimum over the respective entire behavioral-policy spaces.

For EVERY real s>=0, define
  h_s(d)=min(0, s-b+c*min(0,s-d)).
Then the exact Bellman formulas are
  V_full(s)=1+s+(h_s(d_A)+h_s(d_B))/2;
  V_LR(s)=1+s+h_s(dbar).

An explicit positive rational witness and its exact strict optimum gap are:

* If b<=d_B, choose s=(b+c*dbar)/(1+c). Then
  V_LR(s)-V_full(s)=c*(d_A-d_B)/4>0.
* If b>d_B, put m=min(b,d_A) and s=(d_B+m)/2. Then
  V_LR(s)-V_full(s)=c*(m-d_B)/4>0.

Thus conv(O_LR) is a proper subset of O_full for EVERY positive rational member of this family with p_A != p_B, including arbitrary voluntary stopping at time 1. Interchange A and B if p_B>p_A. Conversely, if p_A=p_B, all identical time/LR hidden histories have identical next-LR kernels; full-history occupancy-flow Markovization preserves (tau,R_tau,D), so O_full=O_LR. In this family the following are equivalent: equal terminal kernels; all s>=0 price-direction optimal values equal; all signed four-dimensional support functions equal; equality of the full and seedless-LR reachable four-observer sets.

## Proof: exact Bellman recursion over all real strategies

For nonnegative error weights the optimal stopping declaration at likelihood ratio r has Q-weighted loss S(r)=min(r,1). At time 2 C, stopping costs 1, while one final sample adds time price s and Bayes risk 1-d_h, since K_h puts probability p_h on the left LR 1-eps. Therefore C's continuation advantage is min(0,s-d_h). On L,H the final observation preserves the LR, and extra sampling cannot lower classification loss for s>=0.

The expected Bayes risk after obtaining the time-2 branch but before any time-3 continuation is
  c*1+((1-c)/2)*(1-delta)+((1-c)/2)*1=1-b.
Relative to stopping at time 1, continuing after hidden history h incurs incremental optimum h_s(d_h). The initial Q masses of A and B are each 1/2, yielding V_full.

A seedless LR policy must share both its time-1 action and time-2 C action across A and B. Averaging their positive C kernels gives gain dbar and yields V_LR. Finite-tree objective functions are multiaffine in all local behavioral probabilities. Optimizing one probability at a time at an endpoint produces a deterministic global minimizer. Hence the Bellman formulas are valid for every real local randomization, without any finite-grid extrapolation.

## Proof: strict gaps and hull geometry

The algebraic identity
  h_s(d)=min(0,s-b,(1+c)*s-b-c*d)
makes h_s a concave piecewise-affine function of d, so Jensen gives V_LR>=V_full.

If b<=d_B, choose s=(b+c*dbar)/(1+c). It satisfies s>b and s<dbar. Directly,
  h_s(d_B)=h_s(dbar)=0,
  h_s(d_A)=-c*(d_A-dbar).
The gap is c*(d_A-d_B)/4. This is the early Bellman-action conflict mechanism.

If b>d_B, let m=min(b,d_A)>d_B and s=(d_B+m)/2. Then
  d_B<s<=dbar, s<b,
  h_s(d_B)=s-b,
  h_s(d_A)=s-b-c*(d_A-s),
  h_s(dbar)=s-b-c*(dbar-s).
Subtracting gives the gap c*(s-d_B)/2=c*(m-d_B)/4. Here both histories continue at time 1 and the loss is incurred by merging their time-2 C actions.

For any chosen s, the rational vector lambda=(1,1,0,s) is an exact strict linear separator. Since every LR behavioral strategy is a full-history strategy, their reachable sets satisfy O_LR subset O_full. Full-history action/occupancy flows form a finite system of linear mass-conservation inequalities; any convex combination of feasible flows can be implemented by dividing outgoing flow by positive alive mass at each full history. Thus O_full is a convex polytope, and strict support separation shows conv(O_LR) is a PROPER subset. If p_A=p_B, the strong kernel-constancy condition at every time/LR fiber makes the exact occupancy-flow average seedless LR and preserves the terminal observer distribution. This gives the equality direction and finishes the proof.

## Two checked rational instances and verification scope

Fix c=1/2, eps=1/2, p_A=1/3, p_B=1/8. Then d_A=1/6, d_B=1/16, dbar=11/96.

* With delta=3/4, b=3/16, s=11/96, V_full=395/384, V_LR=25/24, gap=5/384. This is a reached time-2 C-action conflict.
* With delta=1/8, b=1/32, s=17/288, V_full=1205/1152, V_LR=305/288, gap=5/384. This is a time-1 action conflict.

Adjacent VERIFY.py is the actually executed Python Fraction rational checker: it constructs and normalizes all ten positive P/Q leaves, exhausts 256 full-history and 16 seedless LR deterministic continue/stop patterns (classification Bayes-optimal for these positive-price directions) for BOTH examples, and checks 108 rational parameter tuples against the closed formulas. EXACT_OUTPUT.txt is its execution output. The whole-family quantifier follows from the symbolic proof above, not from the 108 tests.

**Research conclusion:** this infinite strictly-positive rational ten-leaf family cannot host the stronger mother problem conv(O_LR)=O_full but O_LR!=O_full. The equal-kernel subfamily already has equal attainable sets.

**Next:** consider models with DISTINCT time-1 likelihood ratios merging later, or genuinely history-dependent intermediate kernels; do an exact full-vector versus LR-deterministic hull gate before real semialgebraic nonattainability. See NEXT_TASK.md.