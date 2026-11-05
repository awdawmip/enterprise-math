# R5 — Exact all-normal two-gate sign-compatibility criterion and source-dependent-kernel certificate

Date: 2026-11-05. Scope: finite strictly-positive two-source/finite-source P/Q stopping BRC, unrestricted P/Q declarations, FULL history-sensitive versus seedless LR (time, likelihood-ratio) behavioral policies. Status: AUTHOR_DERIVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

Frozen scientific pins: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`; EM `86149263e38c22292c9def1e0f69092efa1be77e`. Current behavioral rules read independently. The R5 mother target is equal full four-observer convex hulls with unequal actual real-policy images; it remains open.

## 1. Exact domain and observation

At time 1 a finite hidden source h has Q and P weight w_h>0, sum_h w_h=1, likelihood ratio 1. At time 1 a policy may STOP and declare P or Q, or CONTINUE. Continuation reaches a common finite set of time-2 likelihood ratios r_j>0 with source-dependent Q kernels K_h(j)>0, sum_j K_h(j)=1, sum_j r_j K_h(j)=1. At time 2 the policy may STOP/P, STOP/Q or CONTINUE. Continuation reaches time-3 terminal ratios s_l>0 with source-dependent, strictly positive Q kernels M_{h,j}(l), sum_l M=1, sum_l s_l M=r_j. All terminal labels P/Q are allowed. The corresponding P transitions are exactly ratio-weighted and normalized. FULL may observe h; LR observes only (t,r). Source-dependent M is new relative to the previous full-epsilon family.

Define O4=(e_P,e_Q,T_P,T_Q), with e_P=P(declare Q), e_Q=Q(declare P), and T_P,T_Q the expected stopping time. Real stochastic behavioral actions are arbitrary probabilities at every allowed information key.

## 2. Theorem: exact support and both information-loss terms for ALL real normals

For an arbitrary n=(a,b,g,d) in R^4, maximize n·O4. The Q-scaled optimal declaration payoff and per-step cost are

  L(r)=max(a*r,b),       c(r)=-(g*r+d).

Here declaration Q pays a*r (P error), declaration P pays b (Q error). Define

  A_h = sum_j K_h(j)L(r_j) - L(1),
  B_hj = sum_l M_hj(l)L(s_l) - L(r_j),
  D_hj = B_hj - c(r_j),
  X_h = A_h - c(1) + sum_j K_h(j)[D_hj]_+,
  mu = sum_h w_h X_h,
  eta = sum_j {sum_h w_h K_h(j)[D_hj]_+ - [sum_h w_h K_h(j)D_hj]_+},

where [x]_+=max(x,0). Then for the ENTIRE real behavioral policy classes

  h_FULL(n) = L(1)-c(1) + sum_h w_h[X_h]_+,
  h_LR(n)   = L(1)-c(1) + [mu-eta]_+,

and hence the exact support gap is

  Delta(n) = {sum_h w_h[X_h]_+ - [mu]_+} + min(eta,[mu]_+) >= 0.

The decomposition is valid for every n in R^4 (including zero/positive/mixed error coordinates and arbitrarily signed time coefficients), without restricting n to (-1,-k,-u,-v).

Proof. Terminal declaration optimization gives L(s). The time-2 STOP payoff is L(r_j)-2c(r_j), and CONTINUE payoff is L(r_j)-2c(r_j)+D_hj. FULL takes [D_hj]_+ separately for each h,j, then takes the positive-part first-gate advantage for each h. Because LR's time-1 continue action is common to all h, the conditional source mass at its time-2 key j is proportional to w_h K_h(j). LR therefore optimizes one common time-2 action, giving the pooled positive part [sum_h w_h K_h(j)D_hj]_+. The pooled time-1 advantage equals mu-eta. Behavioral randomization cannot improve a linear directional objective over the corresponding deterministic local action and, in this acyclic finite-time setting, an optimum exists at deterministic information-key actions. Finally eta>=0 by convexity of positive part, and [mu]_+-[mu-eta]_+=min(eta,[mu]_+) for eta>=0. QED.

## 3. Exact zero-gap sign compatibility

For strictly positive w_h and K_h(j), Delta(n)=0 if and only if either:

  (S) X_h<=0 for every source h (first gate may optimally STOP everywhere), or

  (C) X_h>=0 for every source h AND, for every time-2 key j, the D_hj across all h do not have both a positive and a negative value (one common optimal continue/stop choice).

Proof. A Jensen gap sum_h w_h[X_h]_+-[mu]_+ is zero exactly when the X_h have one weak sign. If all X_h<=0 then mu<=0 and the second term vanishes. If all X_h>=0 and at least one is positive, mu>0, so the second term vanishes exactly if eta=0. Each eta_j is nonnegative and zero exactly when all D_hj have one weak sign under the strictly positive weights w_h K_hj. If all X_h=0, condition (S) already holds. This covers all boundary/zero cases. QED.

For two sources with p_j=w_A K_A(j) and q_j=w_B K_B(j), whenever D_Aj*D_Bj<0,

  eta_j = min(p_j*abs(D_Aj), q_j*abs(D_Bj)),

otherwise eta_j=0. Thus a single opposite-sign second-gate pair, combined with X_A,X_B>0, certifies STRICT full-four-dimensional convex-hull separation. This is a finite exact sign certificate, not merely one approximate observation residual.

The full hulls are equal exactly when this zero-gap criterion holds for every n in R^4. Because L and all nested hinges are piecewise-linear homogeneous in n, finite rational support-fan/cell feasibility checks are available when all probabilities are rational. Implementing and verifying such a complete cell enumeration for new equal-hull candidates remains a next unit.

## 4. New rational instance: BOTH the first and second kernels depend on source

Let w_A=w_B=1/2, time-2 ratios R=(1/2,1,3/2), and

  K_A=(1/4,1/2,1/4),  K_B=(3/8,1/4,3/8).

Terminal ratios S=(1/4,1/2,1,3/2,7/4). Use the common low and high kernels

  M_low =(11,1,1,1,1)/15,   M_high=(1,1,1,1,11)/15,

and different time-2 midpoint kernels

  M_A,mid=(1/10,1/10,3/5,1/10,1/10),
  M_B,mid=(1/8,3/16,3/8,3/16,1/8).

All kernel entries are strictly positive; E_Q[S|h,j]=r_j, E_Q[R|h]=1; therefore all induced P transition probabilities are strictly positive and normalized.

Choose n=(-1,-1,-1,27/32), so L(r)=-min(r,1), c(r)=r-27/32. The exact ingredients are

  A=(1/8,3/16),
  B_A=(1/12,1/8,1/12), B_B=(1/12,3/16,1/12),
  D_A=(41/96,-1/32,-55/96), D_B=(41/96,+1/32,-55/96),
  X_A=29/384, X_B=51/256, mu=211/1536, eta=1/256.

Both first gates strictly CONTINUE. The only disagreeing second gate is r=1; the two source weighted advantages there have opposite signs. It contributes eta=1/256. Thus

  h_FULL=-1565/1536, h_LR=-1571/1536, Delta=1/256>0.

An explicit FULL witness continues at time 1 for both sources. At time 2: low ratio continues for both, high ratio stops/P for both, mid ratio stops/P for source A and continues for source B. At time 3 declare Q if s<1, otherwise P. Its observation is

  W=(1/12,91/128,73/32,39/16);  n·W=-1565/1536.

For the LR hull, every support value is at most -1571/1536; hence W is outside it, and by Hölder duality

  dist_infinity(W,conv O4(LR)) >= (1/256)/(1+1+1+27/32) = 1/984.

## 5. Verification, prior science and exact scope

`VERIFY.py` executes the above Fraction arithmetic, checks each P/Q kernel and ratio martingale identity, builds W by direct trajectory integration, and INDEPENDENTLY enumerates all 3*3^3*2^5=2592 deterministic seedless LR policies for this 3-time-key/5-terminal-key model. It verifies the maximum support is exactly -1571/1536. The actual output is in `EXACT_OUTPUT.txt`, ending `PASS_EXACT_R5_TWO_GATE_SIGN_COMPATIBILITY`.

The general all-real-normal formula and exact zero-gap statement are analytic proofs. The finite exhaustive check covers this specified rational instance. Related established contexts: David Blackwell, "Equivalent Comparisons of Experiments" (1953), DOI 10.1214/aoms/1177729032; Laroche & Tachet Des Combes, "On the Occupancy Measure of Non-Markovian Policies in Continuous MDPs," ICML/PMLR 202 (2023), https://proceedings.mlr.press/v202/laroche23a.html. These are contextual predecessors, not claims of independent origin for the general information/occupancy ideas.

The statistical BRC model declares exactly its observer/time/history projection, retains hidden-source provenance for FULL, and tests loss of future-observer information through that projection. It is a finite typed observation model, not an alteration of P000's six-axis native ontology.

## 6. Next discriminating unit

Use the zero-gap sign criterion to search a new **source-dependent K and M** positive rational family for which the condition holds over every normal cone, rather than checking isolated normals. Start with the finite arrangement of declaration breakpoint hyperplanes L(s), L(r), then second-gate D_hj=0, then first-gate X_h=0 and mu-eta=0; obtain exact rational feasibility/violation certificates. Only after an exact equal-hull certificate search for a real-policy point outside LR using polynomial elimination or Jacobian-rank/dimension separation. Maintain current owner/CLAIM boundaries; these author-side materials are portable evidence, not an admitted R5 Result.
