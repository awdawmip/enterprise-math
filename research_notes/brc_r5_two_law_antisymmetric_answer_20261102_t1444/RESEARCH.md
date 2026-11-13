# R5 — Two-law antisymmetric source-answer perturbation: sharp all-real support gap and preserved 4D rank

Date: 2026-11-02 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This is an auxiliary finite two-law stopping graph; native X6 realization is not claimed.

## Continuation and source status

Direct predecessor: `enterprise-math@fcc49af33ca4df94f923e6a678b5837a5cd0e346:research_notes/brc_r5_answer_time_compensated_fiber_20261102_t1340/RESEARCH.md`. Its exact upper-face compensation and mixed-facet separation remain the established prior boundary. The task's **scientific input pin remains frozen** at Global Knowledge `main@a01383f825ef9d43b4b754254303298c64041568` and Enterprise Math `main@86149263e38c22292c9def1e0f69092efa1be77e`. The *separately read* 2026-11-02 normative snapshots were Global Knowledge `main@fc2394c4a3cc1409c03ae82e9f116f4dbd1d1b67` and Enterprise Math `main@1656181794935bb191381ba4b51a7941e80ffdca`. P000 and ACTIVE worldview are unchanged.

## Exact BRC source-labelled graph

Use the established I→J→K positive two-law stopping graph. Under **each** law, masses 1/2, 1/4, 1/4 initially enter I at time 1, J via B at time 2, and K via C at time 3, respectively. Continue I splits equally to J via I and K via I. At J, each origin B/I either stops at time 2 and answers P, or continues with equal branches to a direct time-3 answer and K via BJ/IJ. The direct J answer has P-law probability of answer P = 3/5 and Q-law probability of answer Q = 3/5. K stopping at time 3 answers P. K continuing terminates at time 4 or 5 and has independently specified terminal-answer kernels under the two laws.

Let `S=(C,I,BJ,IJ)`, seven independent FULL behavioral stop probabilities `(x,jB,jI,kC,kI,kBJ,kIJ)`, and LR stop probabilities `(x,y,z)` with `jB=jI=y` and all four K stops equal `z`. Every decision at the same time–likelihood-ratio key shares the same LR action; all natural branch probabilities are positive. The observation is `O=(eP,eQ,TP,TQ)`, with `eP=P(answer P)` and `eQ=Q(answer Q)`.

Fix **under the P law** K-continue answer-P probability `a_s=1/2` for all sources; **under the Q law** let answer-P probabilities `b_C=1/2-delta`, `b_I=1/2+delta`, `b_BJ=b_IJ=1/2`. Take common K-continue terminal time-5 probabilities `p_s=1/2` under P, `q_s=1/3` under Q, conditional on continuation (remaining terminals occur at time 4). Answer and delay events may be taken conditionally independent. The **probabilistic domain** is every real `-1/2 < delta < 1/2`, giving strictly positive terminal kernels.

## Theorem A (sharp all-real signed answer-sum gap)

Write `E=eP+eQ`. For every real `delta in (-1/2,1/2)`, the support maxima over all real stochastic behavioral policies satisfy

```
h_FULL(E) = 21/20 + |delta|/4.
h_LR(E)   = 21/20 + max(0, delta/4 - 1/40)   if delta >= 0,
            21/20                              if delta <= 0.
Delta_E   = h_FULL(E)-h_LR(E)
          = -delta/4                     if delta < 0,
             delta/4                     if 0 <= delta <= 1/10,
             1/40                        if 1/10 <= delta < 1/2.
```

Consequently the full four-dimensional convex hulls agree within this family **if and only if** `delta=0`. For `delta=0`, the actual real behavioral observation images also coincide.

**Complete proof.** The J direct mass is `D=[(1-jB)+(1-x)(1-jI)]/8`. Each unit of direct mass contributes `6/5` to answer sum, while every other unit contributes 1 before accounting for the shifted K Q-answer kernel. K-source arrival masses are `wC=1/4` and `wI=(1-x)/4`; continuing them adds `+delta` and `-delta` to the per-unit answer sum, respectively. Thus for every real FULL policy,

```
E_FULL = 1 + [(1-jB)+(1-x)(1-jI)]/40
           + (delta/4)(1-kC)
           - (delta/4)(1-x)(1-kI).
```

The J term is at most `1/20`. For positive delta, the last two contributions together are at most `delta/4`, attained by `(x,jB,jI,kC,kI)=(0,0,0,0,1)`. For negative delta, their sum is at most `-delta/4`, attained by `(0,0,0,1,0)`. So the stated FULL maximum is exact. With LR tying `jB=jI=y` and `kC=kI=z`,

```
E_LR = 1 + (1-y)(2-x)/40 + (delta/4)x(1-z).
```

When delta<=0, the last term is nonpositive and max is `21/20` at x=y=0. When delta>=0, the maximum uses y=z=0 and maximizes the affine function `1+(2-x)/40+delta*x/4` over x in [0,1]; the two endpoints give the displayed expression. These are all-real behavioral maxima, without discretization: the formula itself is exact for real actions, and independently the finite graph observation is multi-affine in its behavioral parameters. Subtracting proves the gap. As LR is a subclass of FULL, positive gap means strict hull inclusion for any nonzero delta.

At delta=0, all K answer/time kernels coincide under each law. For an arbitrary FULL policy choose the same x and let
`y=[jB+(1-x)jI]/(2-x)`. The full K source masses are
`w=(1/4,(1-x)/4,(1-jB)/8,(1-x)(1-jI)/8)`; put `z=(sum_s w_s k_s)/(sum_s w_s)`. Both denominators are strictly positive for x in [0,1]. These choices preserve total J stopping flow, K arrival flow, and K stopping flow under BOTH laws. Thus all four observation coordinates agree exactly, establishing FULL actual-image inclusion in LR. Reverse inclusion is tautological. QED.

## Theorem B (full-dimensionality survives every nonzero perturbation)

For the LR corners ordered lexicographically `(x,y,z)`, form a 4x4 matrix whose columns are the four differences from corner (0,0,0) to corners `(0,0,1),(0,1,0),(1,0,0),(1,0,1)`. Exact symbolic expansion gives `det_LR=3*delta/1280`. At the all-1/2 interior FULL behavioral point, the 4x4 Jacobian minor in variables `(x,jB,kC,kI)` equals `det_JFULL=delta/2560`. Both are nonzero for every nonzero real delta in the domain. Hence the LR convex hull has affine dimension four, and the FULL real behavioral image contains a four-dimensional open set (by the submersion/inverse-function theorem).

Both identities follow by substituting the explicit flow equations in VERIFY.py and expanding; a separate SymPy exact symbolic calculation verified these formulas. This is rank evidence for the auxiliary graph, not an external geometry/native-X6 promotion.

## Exact positive example

At `delta=1/8`, choose FULL deterministic actions `(x,jB,jI,kC,kI,kBJ,kIJ)=(0,0,0,0,1,0,0)`. Then
`W=(13/20,69/160,15/4,11/3)`,
`h_FULL(E)=173/160`, `h_LR(E)=169/160`, `gap=1/40`.
The support normal is `N=(1,1,0,0)`, with `||N||_1=2`; thus
`dist_infinity(W,conv O(LR)) >= 1/80`.
An example on the negative side is delta=-1/8, where LR support remains 21/20 and FULL support is 173/160 (gap 1/32).

## Computation and status

`VERIFY.py` was run using Python's standard-library `Fraction`. It enumerates all 128 FULL and eight LR deterministic behaviors at eleven rational values of delta (including both signs, zero and 1/10), checks the exact global maxima, witnesses, and the delta=0 aggregation, and checks four-dimensional affine/Jacobian minors. The saved stdout concludes `PASS_EXACT_R5_TWO_LAW_ANTISYMMETRIC_K_ANSWER 1680 exact assertions`. The all-real statements are proved algebraically above; finite checks are consistency certificates. No native CLAIM/Result/Driver-review/admission or owner confirmation is claimed: actual authenticated service presently reports `research_authority_granted=false`, and a bounded dispatch query returned `CONTROL_QUOTA`.

Next: characterize more general two-law source-specific answer kernels, including independent P and Q perturbations and changes at J. For each candidate, first use exact answer-projection support to distinguish trivial separation, then solve four-dimensional convex inclusion for 128 FULL vertices against eight LR vertices with rational convex/Farkas certificates; retain nonzero rank if a genuine equality candidate is found. The original four-dimensional mother objective remains open.
