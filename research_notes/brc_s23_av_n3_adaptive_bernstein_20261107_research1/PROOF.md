# S23 n=3: exact adaptive Bernstein certificate for the 36-variable kernel

Date: 2026-11-07. Status: author-side mathematical proof and executed exact-arithmetic verifier. Independent review pending.
Frozen scientific input: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Fixed kernel: PR #1777 @72c42391354a2decdacca583134e8f1f97130dc0, 36-variable near-optimal kernel, unchanged.

## Theorem (full ordered-output observer, all lawful real parameters)

For real a,c in [1/2,7/8], set z=(1-a)c, p=(a,z,(1-a)(1-c)), b=(z,1-z). The same pair (a,c) governs three conditionally independent observations.

The explicit rational 4×10 matrix T in VERIFY.py defines a full 8×27 stochastic kernel: for a binary input y having k N labels and an ordered ternary output x with histogram h=(h0,h1,h2),

K_full(y,x) = T[k,h] / (10^9 m(h)), where m(h)=3!/(h0!h1!h2!).

For every lawful real parameter pair,

TV(p(a,c)^⊗3, b(a,c)^⊗3 K_full) ≤ 23738203887/100000000000 = 0.23738203887.

Combining the existing exact-fiber minimax lower bound gives

5211/21952 ≤ delta_3 ≤ 23738203887/100000000000.

The new certified minimax interval width is 16433241/34300000000000 ≈ 0.0000004791032362. The preceding upper bound was 8352195663312870519501/35184372088832000000000 ≈ 0.2373836782485589.

There is also a rational witness for this *fixed* kernel: its TV at (a,c)=(141/250,7/8) equals exactly 1899056310874087867/8000000000000000000 ≈ 0.2373820388592610. Hence the fixed kernel's continuous maximum is enclosed within approximately 1.08e-11, whereas the remaining minimax gap is about 4.791e-7.

## Proof

1. The histogram orbit set H={h∈{0,1,2,3}^3: sum(h)=3} has 10 elements and total ordered-output multiplicity sum_h m(h)=27. Every row of integer T is nonnegative and sums to M=10^9. Spreading each histogram mass uniformly over its m(h) ordered words defines a parameter-independent Markov kernel with 27 distinct ordered outputs. Both true and rebuilt output measures are exchangeable within each orbit. Therefore their full ordered-tag total variation is precisely

E(a,c) = sum_h max(0,R_h(a,c)),

R_h(a,c) = m(h) a^h0 z^h1 ((1-a)(1-c))^h2
         - (1/M) sum_(k=0)^3 binom(3,k) z^(3-k)(1-z)^k T[k,h].

The signed residuals sum to zero. Since the one-trial probabilities are of separate polynomial degree at most one in each of a,c, each R_h is of bidegree at most (3,3).

2. On the original box put a=1/2+(3/8)u, c=1/2+(3/8)v, with u,v∈[0,1]. There is a unique exact tensor cubic Bernstein representation R_h=Σ_(i,j=0)^3 beta_(h,i,j) B_i^3(u)B_j^3(v). The rational evaluations at u,v∈{0,1/3,2/3,1} determine those coefficients via the inverse Bernstein evaluation matrix with rows

(1,0,0,0)
(-5/6,3,-3/2,1/3)
(1/3,-3/2,3,-5/6)
(0,0,0,1).

The verifier constructs this tensor inverse using Fraction, scales to common-denominator integers, and checks three separate off-node interpolation identities.

3. Every tensor Bernstein weight is nonnegative, and the sixteen weights sum to one. Since the positive-part function is convex, on any rectangle with beta coefficients,

E(a,c) ≤ max_(i,j) Σ_h max(0,beta_(h,i,j)).

The same index (i,j) is used for all signed histogram residuals; the inequality therefore remains valid even across residual sign changes.

4. Split rectangles alternately along the a/c axis at their midpoint. For one cubic coefficient vector P0,P1,P2,P3, de Casteljau's exact midpoint rule gives child controls (numerators over a common denominator multiplied by eight):

L = (8P0, 4(P0+P1), 2(P0+2P1+P2), P0+3P1+3P2+P3);
R = (L3, 2(P1+2P2+P3), 4(P2+P3), 8P3).

Apply to each tensor slice and all 10 histograms. These transformations exactly preserve every residual polynomial on each child, and the children cover their parent. The verifier accepts a rectangle only if its exact rational Bernstein hull does not exceed 23738203887/10^11, using integer cross multiplication. Otherwise it splits that rectangle again.

The executed verifier terminates after 59 splits with 60 accepted leaves, maximum depth 31. Its greatest accepted rational hull is about 0.2373820388630728, strictly less than the declared upper bound. This finite exact certificate covers the entire initial continuum, including boundaries. The verifier separately evaluates the stated rational witness. The theorem follows.

## Evidence, scope and next research

VERIFY.py is a self-contained standard-library Python checker with the complete fixed stochastic kernel. RUN_EVIDENCE.txt is its actual execution result. The previous 263169-point grid was not rerun: only 60 adaptive leaves are needed. All certificate decisions are exact Fraction/unbounded-integer comparisons; floating point is used solely to print decimal approximations.

This is an auxiliary conditional-AV theorem preserving the shared hidden parameter, ordered ternary output observer and branch multiplicities. Transfer to the original six-source/ten-label S23 mother R_beh(k,10) requires a separate lawful encoder/decoder/source observation map.

The native Source service returned BACKEND_IDENTITY_OR_VERSION_MISMATCH (operation_sent=false); formal task CLAIM and active Owner were unconfirmed. Mathematical authoring, independent review and formal acceptance remain separate.

Next: isolate the exact algebraic maximizer of this fixed kernel on the boundary c=7/8 near a=0.564, then seek a stronger 36-variable primal kernel or a finite-support minimax dual lower bound. See NEXT_TASK.md.
