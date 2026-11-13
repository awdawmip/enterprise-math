# R5: independent pre-J route and third kernel — exact signed-support theorem

**Research date**: 2026-11-02 (Asia/Shanghai). **Scientific status**: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## Provenance and mother objective

Frozen science: Global Knowledge main@a01383f825ef9d43b4b754254303298c64041568; Enterprise Math main@86149263e38c22292c9def1e0f69092efa1be77e. Direct predecessor: EM commit 105d4541610c9e310f8fba6d9e56bfe057c41f39, research_notes/brc_r5_upstream_two_kernel_diagonal_classification_20261102_t0040/RESEARCH.md, which classified the old two J-kernel mixture family (hull equality iff u=v; actual images also equal on the diagonal). Here the new C input is an independent pre-J source, whose downstream kernel is not a mixture of the previous two.

Current behavior rules verified separately at Global Knowledge main@f22d16f479f747cae6f44e7e09f3a3d66889dd95 and EM main@7c243c3b6558eb938c7ab3240fc91ee762a3a38f: global bootstrap/manual, EM researcher router, math/code/output/BRC rules, P000 startup projection and original, ACTIVE worldview, joint observer constraint, current continuation/portable research and research_method.json. Original P000 global blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matches the projection. This is a typed finite auxiliary two-law stopping model, not a native X6 theorem.

Mother problem: find a finite strictly positive two-law stopping model where FULL-history and seedless time/likelihood-ratio (LR) behavioral *convex hulls* agree in four observers but their *actual real policy images* differ. This new family gives a precise separation result on an open real parameter interval.

## Model and exact probability flows

Four initial labeled source masses (P,Q) are A1=A2=(1/8,1/8), B=(1/4,1/8), C=(1/2,5/8). P and Q each total one. Four genuine shared decisions: I=(time 1, P/Q=1), J=(time 2, P/Q=2), K=(time 3,P/Q=8/5), L=(time 4,P/Q=12/5); C first has its separate key (time 1,P/Q=4/5). A behavioral coin has the same probability under P and Q.

Each A_i at I either stops answer P at time1 (coin p), or nature answers Q at time2 with P/Q conditional probabilities (1/2,3/4), or enters J with (1/2,1/4). B enters J directly. C at its distinct initial key either stops Q at time1 (coin r), or nature sends it to J with P/Q conditional probabilities (tau/2,tau/5), or answers Q at time2 on the complement. Its J arrival ratio is exactly (4/5)*(tau/2)/(tau/5)=2. All nature edges and complements are strictly positive for 0<tau<1.

At J one may stop P at time2 (coin q), or continue. A1,A2,B continuing J use a law-independent 1/2 mixture of the previous A/B kernels: (A) terminate Q at time3 with P/Q conditional (3/5,1/2); on the residual terminate P at time3 with conditional (1/2,1/2), then send the remainder to K; (B) branch at time4 to a terminal with conditional (2/5,1/2), or to L with conditional (3/5,1/2); the B terminal answers P with law-independent probability 1/4, Q with probability 3/4. C instead uses a distinct post-J kernel: terminate Q at time3 with conditional (3/5,1/2), or send the residual (2/5,1/2) to K. At K stop answer P at time3 (coin k), or nature terminates Q at time4 with conditional (1/4,1/2) or sends its complement (3/4,1/2) to L. At L stop P at time4 (coin l), or Q at time5 otherwise.

Every arrival at each shared key satisfies P/Q exactly: J=2, K=8/5, L=12/5, as verified independently on all source paths in VERIFY.py. C's downstream **Q arrival at K conditional on J continuation** is 1/2; the A kernel's is 1/4 and B kernel's is zero. Therefore the C kernel is outside the typed future-process mixture convex hull [0,1/4] of the two old kernels. The C path creates a genuinely independent provenance-conditioned mechanism.

FULL policies can use source-dependent coins. The explicit admissible witness uses (p,q_N,q_C,r,k_N,k_C,l_N,l_C)=(1,0,1,0,0,0,1,0), with N={A1,A2,B}; an LR policy instead has five real coins (p,q,r,k,l) and requires q_N=q_C=q, k_N=k_C=k, l_N=l_C=l. The FULL witness belongs to the larger unrestricted FULL class.

## Exact all-real theorem

Let O=(e_P,e_Q,T_P,T_Q), where e_P=P(final answer P), e_Q=Q(final answer Q), and T_P,T_Q are expected integer stopping times under the two laws. Set the signed normal

    n=(11480,-1856,9320,-9392),       ||n||_1=32048.

For every real tau in [0,1], the above FULL witness has the exact observation

    W(tau)=(61/160+tau/4,11/16-tau/8,43/20,125/64),
    n·W(tau)=4795+3102*tau.

The exact maximum over **all real seedless LR policies** is

    max_LR n·O = max(6005,4454+3102*tau).

Hence the exact signed witness-to-LR-hull gap is

    D(tau)=min(3102*tau-1210,341).

For **every strictly positive** 55/141<tau<1 we obtain D(tau)>0 and

    dist_infinity(W(tau),conv(LR(tau))) >= D(tau)/32048.

At tau=1/2, W=(81/160,5/8,43/20,125/64) and the exact signed gap is 341 (distance >=341/32048). The same direction does not decide hull equality for tau<=55/141.

### Complete proof and arithmetic certificate

Every finite trajectory visits each shared key at most once. Therefore the LR four-observer readout is multi-affine in its five real behavior coins. It equals a convex combination of all 2^5=32 deterministic LR vertices with product-Bernoulli coefficients. So the LR signed support over all real coins equals the maximum of those 32 vertices.

For each of the 32 fixed deterministic LR policies, the signed score is an AFFINE function of tau: only C's pre-J natural split depends on tau, and no path visits this split twice. The FULL witness score is affine for the same reason. The attached standalone Python 3 standard-library Fraction program computes and independently checks all P/Q terminal masses and exact shared LR keys, and enumerates all 32 LR vertices at tau=0,1/2,1. The minima of n·(W−O_LR_vertex) at the three interpolation values are precisely -1210,341,341. Corresponding n·W scores are 4795,6346,7897, hence LR support values are 6005,6005,7556. Affinity bounds every LR vertex by 6005 on [0,1/2], and by 4454+3102*tau on [1/2,1]. These bounds are ATTAINED by the deterministic LR bits (p,q,r,k,l)=(1,0,1,0,1), which has constant score 6005, and (1,1,0,0,0), which has score 4454+3102*tau. Thus the displayed support formula holds for all real tau, and by multi-affinity all real seedless LR behavioral policies. Subtract the explicit witness score and simplify the strict threshold 1210/3102=55/141. Finally for every Y in conv(LR), Hölder gives D<=n·(W−Y)<=||n||_1 ||W−Y||_infinity, proving the distance bound. QED.

The three-point finite enumeration is universal here because the polynomial degree was independently established as at most one in tau, not because sampled points alone prove arbitrary real identities. The fractional computation also executes five extra rational regression values. EXACT_OUTPUT.txt is the captured local execution output; the program itself is the exact verifiable certificate.

## BRC reuse, status, follow-up

Positive rational dual-measure mass is carried with full initial source, natural-kernel, branch, answer, time and action provenance until the four-observer readout. The dual signed normal acts on final observations; it is not a signed mass in the positive BRC carrier. No native spatial coordinates, BRC–Shor dynamics, physical model, unbounded horizon, mathematical acceptance or independent review is claimed.

The authenticated GitHub user awdawmip has repository push rights. The current native service version 0.6.11 reports research_authority_granted=false and static read-only access; current owner listing returned CONTROL_QUOTA. No CLAIM, Result or Driver review receipt was obtained. This is author-proved, exactly computed, portable research only.

Next discriminating experiment: replace the third C kernel with C_s=(1-s)*(A+B)/2+s*C using a law-independent nature coin 0<=s<=1, preserving shared LR keys. At s=0 the conditional continuation kernel is source blind and actual real FULL/LR images can be matched by Q/P-mass Markovization. At s=1, tau>55/141 this note certifies a strict hull gap. Determine the exact (s,tau) separation region, check any candidate hull-equality point with complete rational four-dimensional convex decompositions or Farkas separators, and then analyze actual real-policy image membership.
