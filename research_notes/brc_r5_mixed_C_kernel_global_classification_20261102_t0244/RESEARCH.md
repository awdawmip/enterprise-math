# R5 — global mixed-third-kernel two-parameter classification

**Date:** 2026-11-02 Asia/Shanghai. **Status:** AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

**Frozen scientific pins:** GLOBAL_KNOWLEDGE_V1 main@a01383f825ef9d43b4b754254303298c64041568; Enterprise Math main@86149263e38c22292c9def1e0f69092efa1be77e. **Direct predecessor:** Enterprise Math commit 0a9c093d7a310e392277e832e19829e8de83a3de, research_notes/brc_r5_independent_prej_C_kernel_20261102_t0140/RESEARCH.md and VERIFY.py. **Current rules consulted separately:** Global Knowledge main@6b5d2c73ada20c88f781d4566dedc66d8fff3286; Enterprise Math main@f405a1a6a4e402219fb01f60014bc0db6e935585. Original P000 global Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matched the P000_STARTUP projection; ACTIVE worldview unchanged. Native research_authority_granted=false and active-owner read returned CONTROL_QUOTA.

## Question and exact finite positive-flow model

The mother question is whether a finite strictly positive two-law stop/continue experiment can have equal FULL-history and seedless (time,likelihood-ratio) LR four-observer convex hulls but unequal *actual real* behavioral observer images. A strict all-signed support gap rejects one candidate topology, not the mother objective.

Initial labeled masses (P,Q) are A1=A2=(1/8,1/8), B=(1/4,1/8), C=(1/2,5/8), each law totaling 1. Decisions use I=(time 1, P/Q ratio 1), J=(2,2), K=(3,8/5), L=(4,12/5), and the distinct C key (1,4/5). At I, A1/A2 may stop answer P at time 1; otherwise nature terminates Q at time 2 with conditional (P,Q)=(1/2,3/4), or sends (1/2,1/4) to J. B enters J directly. C at its separate key may stop Q at time 1; otherwise nature sends (tau/2,tau/5) to J or terminates Q at time 2 on the complement. These J arrivals have ratio 2.

J stops P at time 2 or continues. The A1/A2/B post-J kernel is the law-independent half-mixture N=(A+B)/2. Kernel A terminates Q at time 3 with (3/5,1/2), then of the remainder (2/5,1/2) terminates P at time 3 with half or sends half to K. Kernel B terminates P at time 4 with (1/10,1/8), Q at time 4 with (3/10,3/8), and sends residual (3/5,1/2) to L. Kernel C terminates Q at time 3 with (3/5,1/2), and sends residual (2/5,1/2) to K. **New parameter:** the C-source post-J kernel is the law-independent mixture C_s=(1-s)N+sC. At K, stop P at time 3 or continue: nature terminates Q at time 4 with (1/4,1/2) or sends (3/4,1/2) to L. At L, stop P at time 4 or answer Q at time 5. All specified natural branches and mixture weights are strictly positive for 0<tau,s<1, and all shared (time,LR) keys have the claimed ratios.

Observer O=(e_P,e_Q,T_P,T_Q) records P(final answer P), Q(final answer Q), and expected integer terminal times under P/Q. LR uses five real behavior coins (p,q,r,k,l). FULL may use source/history dependent coins. An explicit admissible FULL strategy (p,q_N,q_C,r,k_N,k_C,l_N,l_C)=(1,0,1,0,0,0,1,0) has, for all s,

W(tau)=(61/160+tau/4, 11/16-tau/8, 43/20, 125/64).

The C source stops at J for this witness, so C_s never affects W.

## Theorem (complete classification in this family)

Let t=tau, and define the parameter-dependent signed four-normal

n1=-15(8*s*t^2+75*s*t-24*t^2-134*t-110);
n2=-24*t(10*s*t+69*s-30*t-30);
n3=-15(5*s*t^2-15*s*t-37*t^2-92*t-55);
n4=6(32*s*t^2+3*s*t-184*t^2-294*t-110).

For **every real** 0<=t,s<=1, if V_10001 is the deterministic LR observation for (p,q,r,k,l)=(1,0,0,0,1), then

max over all real LR policies [n(t,s)·O] = n(t,s)·V_10001,

n(t,s)·W(t) - max_LR n(t,s)·O = **(33/4)*s*t*(t+15)**.    (1)

Thus for every s*t>0, FULL and LR four-observer convex hulls differ. A conservative uniform bound ||n||_1 <= 13869 gives

dist_infinity(W(t),conv(LR)) >= **11*s*t*(t+15)/18492** >0.      (2)

If s*t=0, the **actual real observer images are equal**, so in this two-parameter family both convex-hull equality and actual-image equality hold **iff s*t=0**. Boundary cases with a zero edge are statements about the closed mathematical family, not strictly-positive interior models.

### Proof and exact global certificate

Every finite path visits each LR decision key at most once, so the four-observer map is multi-affine in the five LR behavior coins. Expansion by product Bernoulli weights shows that every real LR observer lies in the convex hull of the 2^5=32 deterministic LR vertices; conversely deterministic vertices are LR. All-signed LR maxima therefore occur at these vertices.

For fixed LR deterministic bits, each observation coordinate is bilinear in (t,s): the C pre-J natural split involves t only once and the C post-J mixture involves s only once on a path. Compute its four corner values in exact rational P/Q source flow. Multiplying by the displayed n yields for each of 32 LR bits b a polynomial S_b=n·(V_10001-V_b) of degree <=3 in t, <=2 in s. In the tensor Bernstein basis B_{i,3}(t)B_{j,2}(s), **all 384 exact rational coefficients of these 32 slack polynomials are nonnegative (264 strictly positive)**. Since each Bernstein basis term is nonnegative and the basis sums to one on [0,1]^2, S_b>=0 at every real parameter, proving the exact LR maximum. This is a finite universal coefficient certificate, **not sampling-based extrapolation**. The zero-slack deterministic bits are 10001,10011,10101,10111,11000,11001,11010,11011.

Exact observation of the displayed FULL witness and polynomial multiplication give the identity n·(W-V_10001)=(33/4)*s*t*(t+15) with no omitted terms, proving (1). Hölder gives (2). Componentwise bounds |n1|<=4020, |n2|<=3336, |n3|<=2985, |n4|<=3528 justify the norm bound.

At s=0, all J arrivals have the same conditional future kernel N, and the K,L natural kernels are also source-blind. At t=0, C never reaches J, so every genuinely shared key likewise has a common conditional future kernel. In either boundary case, for any FULL policy aggregate its Q stop/continue flow at each (time,LR) key, choose the LR stop coin as the Q stop flow divided by total Q occupancy (arbitrary at zero occupancy), and note that P action flow is LR-key-ratio times Q action flow. Because the next-key kernels are source-blind, induction over the finite acyclic graph exactly matches both law flows, terminal answers and stopping times. Every FULL real observer has an actual real LR representative; the reverse inclusion is trivial. This proves the boundary statement, completing the classification. QED.

## Evidence and limits

Run the accompanying standalone Python 3 standard-library Fraction verifier: it computes both-law positive source flows, checks shared LR-key ratios and normalization at each exact evaluation, reconstructs all 32 LR deterministic observations bilinearly, checks the exact witness polynomial, verifies all 384 tensor Bernstein coefficients, and executes 198 additional noncorner exact observation evaluations. Its captured output ends PASS_EXACT_R5_MIXED_THIRD_KERNEL_GLOBAL_CLASSIFICATION. The universal signed statement relies on the analytic multi-affinity and Bernstein argument; the software gives an independently rerunnable finite rational algebra certificate.

BRC reuse is **typed positive dual-law branch/source mass**, with origin and destination provenance preserved through terminal readout. The signed four-normal applies only to the observer, not to the positive BRC carrier. No native X6/three-dimensional slice bridge, physical prediction, Lean proof, independent Driver review, formal Result, or Foundation admission is claimed. Active owner remains unconfirmed because the current native read returned CONTROL_QUOTA; GitHub PR preservation is author-side only.

**Next:** leave this fully classified family. Seek a two-sided pre-J source topology with genuinely independent conditional kernels whose observer residuals can counteract one another; reject a candidate by an exact signed normal if possible, otherwise require complete rational four-hull membership (<=5 LR vertices per FULL deterministic point) before studying actual real observer-image nonmembership. The mother question remains open.
