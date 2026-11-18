# S23 n=3: certified near-optimal symmetric reconstruction

Date: 2026-11-07; author-side proof and exact integer verification, independent review pending.
Frozen scientific input: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Predecessor symmetry theorem: PR #1777 at c27d14427608cb3430d95e9876cca19bbd7e4838.

## Theorem

For all real a,c in [1/2,7/8] put z=(1-a)c, p=(a,z,(1-a)(1-c)), b=(z,1-z). The same pair (a,c) governs three conditionally independent observations. Define

δ₃ = inf over parameter-independent stochastic kernels K: {Y,N}³ -> {stop1,stop3,stop4}³ of sup_(a,c) TV(p^⊗3,b^⊗3 K).

The explicit rational K in VERIFY.py proves

5211/21952 <= δ₃ <= 8352195663312870519501 / 35184372088832000000000
                        = 0.2373836782485589...

The lower bound 5211/21952 is a *reused earlier exact-fiber result*; the upper bound here is newly and independently certified. The interval width is exactly

25566345946588188843 / 12068239626469376000000000 = 0.0000021184817950...

The previous continuous bound was f(α)=0.237838693711015430..., so this construction improves the upper bound by more than 0.000455.

## The 36-variable construction, preserving 27 ordered outputs

The input type k=0,1,2,3 counts the number of N positions. The output histogram h=(h0,h1,h2), with nonnegative entries summing to three, counts stop1/stop3/stop4. There are ten histogram types, indexed in lexicographic order. Let m(h)=3!/(h0!h1!h2!). The explicit nonnegative 4×10 integer matrix T=K in VERIFY.py has row sums M=10^9. For each *ordered* binary input word y of type k and each *ordered* ternary word x of histogram h define

K_full(y,x) := T[k,h]/(M m(h)).

This is a parameter-independent 8×27 Markov kernel. The 4×10 representation computes the exact marginal TV over all 27 tagged output words because both the truth law and reconstructed law are exchangeable and constant on each output orbit. It does not discard output order from the original observer specification.

## Exhaustive exact grid

Let N=512, D=8N=4096, a=(4N+3i)/D, c=(4N+3j)/D, for every 0<=i,j<=N. Put A=4N+3i, C=4N+3j,

q0=A D, q1=(D-A) C, q2=(D-A)(D-C), u=D²-q1.

The full histogram probability is m(h) q0^h0 q1^h1 q2^h2 / D^6. The compressed input-type probability is binom(3,k) q1^(3-k) u^k / D^6. The reconstructed histogram mass is the sum over k of these input probabilities times T[k,h]/M. Since the signed residuals sum to zero, their positive parts sum to exactly TV. The integer numerator at each grid point is therefore

Σ_h max(0, M m(h) q0^h0 q1^h1 q2^h2
           - Σ_k binom(3,k) q1^(3-k) u^k T[k,h]).

Divide by M D^6. VERIFY.py checks every one of 263169 grid pairs and all ten histogram types using unbounded integers (no floating-point certificate). It gives

max_grid TV = 8352131519952870519501 / 35184372088832000000000
            = 0.2373818551846190...

at indices (i,j)=(87,512), i.e. a=2309/4096, c=7/8.

## Analytic all-real extension

Let F(a,c)=p^⊗3-b^⊗3 K_full in R^27. The one-trial first derivative l1 norms obey ||p_a||=2, ||p_c||<=1, ||b_a||<=7/4 and ||b_c||<=1; all pure one-trial second derivatives vanish. Tensor product differentiation over the six ordered cross-factor terms and stochastic contraction imply

sup ||F_aa||₁ <= 339/8,   sup ||F_cc||₁ <= 12.

For a C² vector function on a grid cell of side h, endpoint-linear interpolation independently in a,c has l1 residual at most h²(||F_aa||_sup+||F_cc||_sup)/8. Dividing by two for TV and using convexity of the bilinear corner interpolation yields an all-real extension

sup_real TV(F) <= max_grid TV(F) + h²(339/8+12)/16
               = max_grid TV(F) + 3915/(8192 N²).

At N=512 the remainder is exactly 3915/2147483648. Adding to the exact grid maximum gives the theorem's upper bound, strictly below 23739/100000=0.23739.

## Provenance, verification and scope

The candidate 36-variable kernel was obtained by a numerical cutting-plane LP and rounded to the exact integer T. The executed VERIFY.py and its stdout RUN_EVIDENCE.txt are the independent acceptance certificate for the new upper bound; the numerical optimizer's convergence is not used in the proof. Earlier the independent-input/output S3×S3 twirl theorem justified the symmetry reduction. This is an auxiliary conditional-AV result; the original S23 six-source/ten-label R_beh(k,10) mother model requires a separate lawful encoder/decoder/source bridge. Tagged branch identities, multiplicities, and a single shared hidden parameter across three repetitions are retained. For any future *joint* (input,output) observer, a separate preservation proof would be needed.

The native service returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false, for session registration and task inventory in this run; this is an author-side research artifact, not a formally CLAIMed or accepted Task Result.

Next task: reduce or resolve the remaining 2.11849e-6 primal-dual gap with exact continuum primal or finite-support rational dual evidence.
