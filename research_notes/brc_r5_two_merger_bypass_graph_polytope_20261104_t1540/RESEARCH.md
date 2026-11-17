# R5: a two-merger bypass experiment with a nonconvex seedless-LR real image

Date: 2026-11-04. Scientific status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.
This is a finite two-law **controlled-action auxiliary BRC**, not yet an unrestricted terminal-declaration R5 model and not a mother-problem counterexample.

## Parent objective and frozen sources

R5 asks for a strictly positive source/route-sensitive P/Q BRC experiment with identical complete four-observer convex hulls for FULL and seedless likelihood-ratio policies, but different **actual real-policy** observation sets. The predecessor fixed four-parameter two-merger family was classified in commit 9497a99b4bbd2550dca6f3629a4e6d806bec4876, which excluded that fixed family.

The scientific input pins remain Global Knowledge a01383f825ef9d43b4b754254303298c64041568 and Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Current operating rules were read separately. P000 and ACTIVE worldview are unchanged; this finite P/Q experiment is an auxiliary mathematical model and asserts neither a native X6 embedding nor a physical realization.

## Fully specified model

Under both probability laws P and Q, three distinct histories begin at time zero: A1 and A2 have mass 1/4 each, and B has mass 1/2. All have likelihood ratio 1. Histories A1,A2 reach the **first merged information key** (time 1, r=1). History B follows a deterministic delay/bypass to time 2 without an action at time 1.

At the first key the allowed actions are STOP (declare Q at time 1) or CONTINUE to time 2. Under seedless LR they use the same probability x; FULL may choose independent x1,x2 by remembered history. At time 2, continuing A1/A2 and bypass B share the **second merged key** (time 2, r=1), with permitted STOP (declare Q) or CONTINUE to a time-3 terminal lottery. Seedless LR uses common continue probability y; FULL may use independent a1,a2,b. The two merges interact: the first decision changes the mixture reaching the second.

A1 and A2 each have, conditional on continuation from the second key, two terminal likelihood ratios (1/2,3/2) with Q probabilities (1/2,1/2) and P probabilities (1/4,3/4). B has ratios (1/4,7/4) with Q probabilities (1/2,1/2) and P probabilities (1/8,7/8). All listed source and terminal probabilities are **strictly positive**; P probability at each terminal equals r times Q probability and both per-source laws normalize to 1.

Terminal declaration is **prescribed**: declare P at the low-r terminal, Q at the high-r terminal. Early stopping declares Q. These are model assumptions, not optimized action choices; relaxing them is the next scientific check. The readout is
O4=(eP,eQ,TP,TQ) with eP=P[declare Q], eQ=Q[declare P], TP=E_P[t_stop], TQ=E_Q[t_stop].

## Exact all-real observation parameterization

Define x=(x1+x2)/2, z=(x1*a1+x2*a2)/2, and y=b for FULL. By direct summation over both laws,
  eP = 1 - y/16 - z/8,
  eQ = (y+z)/4,
  TP = TQ = 3/2 + (x+y+z)/2.                                (1)

For seedless LR, x1=x2=x and a1=a2=b=y, so z=xy. Conversely, every triple with 0<=x<=1, 0<=y<=1 and 0<=z<=x is attained by FULL: choose x1=x2=x, b=y, and a1=a2=z/x when x>0 (arbitrary when x=0).

Equation (1) is an injective affine map into R4, with exact inverse
  x = 2(TP-3/2) - 4 eQ,
  y = 8eQ - 16(1-eP),
  z = 16(1-eP) - 4eQ.                                        (2)

Hence the complete **actual behavioral** images, for arbitrary real probabilities, are:
  O4(FULL) = affine image of {0<=x,y<=1, 0<=z<=x},
  O4(LR)   = affine image of {0<=x,y<=1, z=xy}.
The FULL image is a convex three-dimensional polytope (in the TP=TQ affine subspace), while the seedless LR image is a nonconvex bilinear graph.

## Nonconvexity witness and complete convex-hull obstruction

The LR policies (x,y)=(0,0) and (1,1) give points whose midpoint has inverse coordinates (x,y,z)=(1/2,1/2,1/2), violating z=xy=1/4. Thus this midpoint lies in conv O4(LR), but not in the **actual real** O4(LR). This certifies nonconvexity without sampling or numerical tolerances.

Since z=xy on the unit square, its LR convex hull is exactly the McCormick tetrahedron
  0<=x,y<=1, max(0,x+y-1)<=z<=min(x,y).
By contrast the FULL image permits every 0<=z<=x without a z<=y restriction. In particular, x=1,y=0,z=1 is realized by FULL (all A histories continue at both keys; B stops at time 2). The corresponding actual FULL observation point is
  W=(7/8,1/4,5/2,5/2).
For direction n=(-8,-3,0,0), direct substitution in (1) gives
  n·O4 = -8 + (z-y)/4.
For LR, z=xy<=y, hence h_LR(n)=-8, achieved for y=0 or x=1. For FULL, z<=x<=1 and y>=0, hence h_FULL(n)=-31/4, achieved by W. Thus
  h_FULL(n)-h_LR(n)=1/4>0,
  dist_infinity(W,conv O4(LR)) >= (1/4)/(8+3) = 1/44.
This strictly rules out this controlled-action two-merger candidate as a solution to the FULL/LR convex-hull-equality mother target.

## Scientific significance and limits

The construction isolates a genuine mechanism for nonconvex **actual seedless LR observations**: a first merged decision controls the amount of one source reaching a later shared key, while a bypass source still reaches that key. In observer coordinates the seedless policy must obey the bilinear equation z=xy, whereas full-history action flows can vary z independently within [0,x].

A nonconvex LR image is therefore attainable in an explicit strictly positive P/Q two-merger experiment. Nevertheless the same model also has a strict *all-signed* convex-hull gap. Nonconvexity alone is insufficient for R5. The unrestricted terminal-declaration model, possible alternate branches that alter the hull without filling the actual image, and native X6 correspondence remain separate open questions; the present theorem does not negate them.

A compatible occupancy-measure result is Laroche & Tachet des Combes, ICML 2023, https://proceedings.mlr.press/v202/laroche23a.html, on history-to-Markov occupancy equivalence when the full Markov state is available. A relevant newer semi-algebraic perspective is Anderson & Montúfar (2026), https://arxiv.org/abs/2606.03048, on memoryless POMDP feasible value sets. Neither external paper is claimed to prove the present R5 model theorem.

## Exact check

VERIFY.py uses Python fractions.Fraction. It enumerates 4 seedless LR and 32 FULL deterministic policy tuples, verifies the signed support values, the exact midpoint and its inverse, 25 rational LR inversion tests and 243 full-history inversion tests. EXACT_OUTPUT.txt is the actual executed stdout. Finite checks support the explicit example; (1)-(2) and the domain arguments prove the all-real claim. No formal proof assistant or independent mathematical review is claimed.

## Next

Test unrestricted terminal P/Q decisions on this exact topology by all-signed deterministic-vector enumeration; seek a strict rational separating direction or, if none, full-vertex rational primal hull certificates. If unrestricted actions destroy the graph nonconvexity, identify the smallest source-sensitive terminal guard/branch modification that restores it without imposing forced declarations. Separately explore a compensating route that makes the FULL/LR hulls coincide while preserving some nonlinear actual-image obstruction. Do not infer R5 closure from this auxiliary result.
