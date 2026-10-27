# R5 — Penultimate hinge family is complete for compulsory-arrival four-observer compression

2026-10-27. **Author-level finite BRC branch theorem; UNREVIEWED / NOT_ADMITTED.** No native CLAIM, formal Result, Driver acceptance, native X6 transfer or P000 change.

**Pinned inputs:** GLOBAL_KNOWLEDGE_V1 main@fd68f262d614470f7aaf2b03d1591656e0dc0373, with P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; Enterprise Math main@02ecc2acff48e05b3afba461d39aa8e970cdaf77; preceding R5 source research_notes/brc_n3_weak_strong_lumpability_gap_20261027_r5/NEXT_TASK.md. Actual em_control_tasks read returned CONTROL_QUOTA, so active Owner and a formal research CLAIM are not verified. This is an external positive rational two-measure tree, not a six-axis native physical model.

## Domain and definitions

Let finite strictly positive measures P,Q describe a finite observation tree. All paths are obliged to reach time T (no actions before T). At T, the observer may stop and label P or Q, or observe once more at T+1 and then label P or Q. Full-history behavioral policies may use independent randomized actions conditional on the complete path. Seedless likelihood-ratio (LR) behavioral policies may use independent randomized actions depending only on (t,L), with no persistent seed. Write O(pi)=(P(decide Q), Q(decide P), E_P tau, E_Q tau).

For each time-T full history h, put w_h=Q(h)>0, r_h=P(h)/Q(h), and K_h(y)=Q(Y=y|h), where Y=P(terminal)/Q(terminal). Then sum_y K_h(y)=1 and sum_y y K_h(y)=r_h. Fibers G_r collect histories with r_h=r. These are BRC-positive Q branch weights, with hidden predecessor labels retained until quotient safety is proved.

## Theorem (exact equivalence and quantitative certificate)

The following four statements are equivalent:

1. For every r, all K_h for h in G_r are identical as finite distributions on Y.
2. O_full=O_seedless as actual four-vector attainable sets, for arbitrary real local action probabilities.
3. Their minimum values agree for every signed linear functional on R^4.
4. Their minimum values agree for every u>0, s>=0 in the **nonnegative** restricted family J_(u,s)=e_P+u e_Q+s E_Q tau.

If 1 fails on rational tree data, a strictly positive **rational** gap in 4 is constructible using one terminal likelihood-ratio support knot u and rational s.

### Proof 1 -> 2

Fix an arbitrary full-history behavioral policy. At T, for history h with LR r, denote stop-P, stop-Q and continue probabilities by a_h,b_h,c_h. Define seedless actions at r as their Q-mass-weighted averages over G_r, dividing by W_r=sum_{h in G_r}w_h. The P and Q flows of stop decisions and continuation at each r agree because P(h)=rQ(h). Under 1, K_h=K_r in that fiber, so continued terminal Q mass at Y=y equals K_r(y)sum_h w_h c_h in either policy. Sum these flows over all r arriving at common y. Choose seedless terminal decision-Q probability as original Q mass deciding Q at y divided by the total original Q arrival at y (arbitrary if zero). Since every terminal branch with that y satisfies P=yQ, this matches both terminal error coordinates. Matching continuation masses under P,Q also matches E_P tau=T+P(continue) and E_Q tau=T+Q(continue). Hence every full four-vector has a seedless realization, and inclusion in the other direction is tautological.

### Proof 2 -> 3 -> 4

The policy domains are finite products of compact simplices and observer maps are continuous, so attainable sets are compact. Linear minima preserve equality of sets; 4 specializes the coefficients of 3.

### Proof 4 -> 1, and exact gap

Fix u>0 and s>=0. Define S_r=min(r,u), H_h(u)=sum_y K_h(y)min(y,u), d_h(u)=S_r-H_h(u)>=0 by concavity/Jensen using E(Y|h)=r. At h the optimal stop cost per Q mass is S_r; the optimal continue cost excluding compulsory baseline T*s is s+H_h. The full agent chooses separately per h, whereas a seedless agent shares its time-T action within G_r and may use one Bayes-optimal decision label at terminal Y=y. Thus:

C_full,r = W_r S_r + sum_h w_h min(0,s-d_h);
C_seedless,r = W_r S_r + min(0, sum_h w_h(s-d_h)).

Let A_r=sum_{h:d_h<s}w_h(s-d_h) and B_r=sum_{h:d_h>s}w_h(d_h-s). Rearranging positive and negative terms gives the **exact total optimum gap**

V_seedless(u,s)-V_full(u,s) = sum_r min(A_r,B_r).                     (★)

If there are histories i,j in one fiber with d_i(u)>d_j(u), choose s=(d_i+d_j)/2>=0; then A_r>0, B_r>0 and (★)>0.

If two K distributions differ, their hinge transforms H_h(u)=E min(Y,u) differ at some positive support knot u. Each H is continuous and affine between the common union of finite support knots. Equal knot values would force equal functions, hence equal right derivatives P(Y>u), and therefore equal atom masses—contradiction. For rational K,Y, that u and midpoint s and the (★) gap are rational. So agreement of all tests in 4 forces K homogeneity.

This proves the equivalence. (★) requires fixed compulsory time-T arrival masses: do **not** apply it unchanged to N=3 with freely chosen early stopping actions, where those masses depend on earlier policy.

## Exact six-leaf instance at T=2

At T=2 the two hidden histories have w_0=w_1=1/2, r_0=r_1=1. The final LR alphabet is Y=(1/2,1,3/2) with Q kernels K_0=(1/4,1/2,1/4), K_1=(1/8,3/4,1/8). All terminal P masses equal Y times Q masses and are positive. Earlier observations through T are compulsory; the two histories are distinguishable to the full agent but not to LR policy.

For u=1, s=3/32: H_0=7/8, H_1=15/16, d_0=1/8, d_1=1/16; the positive and negative masses in (★) are both 1/64.

Exact optima: V_full=75/64 with O_full,witness=(1/16,7/8,5/2,5/2), continuing first history and stopping second with label P. The seedless value is V_seedless=19/16: either stop both with O=(0,1,2,2), or continue both with O=(3/32,13/16,3,3). Gap = 1/64.

VERIFY.py enumerates exactly 3^2*2^6=576 full deterministic action descriptions and 3*2^3=24 seedless descriptions, evaluating all four coordinates with fractions.Fraction. Scalar optimality over arbitrary real local randomization follows by backward conditional linear minimization; the preceding symbolic proof establishes the universal statement within the declared model class. Captured output: EXACT_OUTPUT.txt.

## Prior art and limits

The classical strong-lumpability criterion (Thomas & Barr, Journal of the American Statistical Association 72(357), 1977, DOI 10.1080/01621459.1977.10479934) and Blackwell comparison of statistical experiments (Khan, Yu & Zhang, Economics Letters 247, 2025, DOI 10.1016/j.econlet.2024.112146) provide methodological context. This is a scoped self-contained sequential four-observer proposition; no broader novelty, peer review, general POMDP equivalence, Heartbeat physics or six-axis embedding is asserted.

**Consequence:** with only one optional final sample following compulsory observations, equality of all signed supports already guarantees actual four-observer equality. Thus this subclass cannot contain the mother-question equal-hull/nonconvex-image counterexample. The next unit removes compulsory arrival; see NEXT_TASK.md.
