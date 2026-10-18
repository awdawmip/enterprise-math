# Auxiliary BRC: sharp minimax subset rounding and uniform saturation bound 215

Date: 2026-10-18 (Asia/Shanghai).
State: UNREVIEWED / NO_NATIVE_CLAIM / NOT_ADMITTED.
This is a mathematical research handoff, not an admitted Enterprise Math Result. It does not supersede any active task owner.

## Source and scope

Verified GitHub source revisions:
- GLOBAL_KNOWLEDGE_V1: awdawmip/chatgpt-global-knowledge main@e2c99e7eeea5f67b9014b350fff8f8b35fe38d4c
- Enterprise Math: awdawmip/enterprise-math main@341ea3fb3b06d32b16208d523dd5b7fdf6037f39

The auxiliary model has n>=2 labelled sources with nonnegative integer masses. At each step a policy protects one label p, an adversary secretly resets some other label v to zero, and the policy observes one bit indicating whether the new total mass reaches the fixed integer threshold T. The policy may continue based on this bit. Initial observation is absent. Safety requires at least one positive source at every possible terminal leaf (Q=1). A_n(1,T) is the number of equivalence classes induced by all finite policies.

A previously derived but still independently UNREVIEWED dependency states: every realizable profile consisting of positive support and the threshold bits of all nonempty proper subsets has a positive-integer realization (q,w) with q<=(n+1)Delta_n, where Delta_n is the largest absolute determinant of an n-by-n binary matrix. Operations and terminal safety depend only on the profile, with threshold-independent transition rules. The following new minimax rounding theorem is proved independently; the BRC saturation inference is explicitly conditional on that dependency.

## Theorem 1: optimal simultaneous all-subset rounding

Let a_1,...,a_m be nonnegative reals. For each i choose y_i in {floor(a_i),ceil(a_i)}. Put e_i=y_i-a_i, P=sum max(e_i,0), N=sum max(-e_i,0). The best constant valid for all inputs is

  gamma_m = floor((m+1)^2/4)/(m+1).

For every input there is one y with max(P,N)<=gamma_m, so for every subset U, simultaneously:

  |sum_{i in U}(y_i-a_i)|<=gamma_m.

Moreover gamma_m cannot be reduced for this rounding problem.

### Constructive proof

Write a_i=floor(a_i)+r_i, 0<=r_i<1, sort r_1>=...>=r_m. Let R=sum r_i and H_j=sum_{i=1}^j r_i. If precisely j coordinates are rounded upward, the best choice is the j largest fractions; it simultaneously minimizes P_j=j-H_j and N_j=R-H_j. Their difference is P_j-N_j=j-R, while P_j is nondecreasing and N_j is nonincreasing in j. Thus only j=floor(R) and j=ceil(R) must be evaluated (one candidate if R is an integer).

When k<R<k+1, mean comparison of the k or k+1 largest fractional parts with the full mean gives H_k>=kR/m and H_{k+1}>=(k+1)R/m. Hence at j=k the cost equals N_k and is at most (m-k)R/m, and at j=k+1 the cost equals P_{k+1} and is at most (k+1)(1-R/m). The first affine bound increases and the second decreases with R; their intersection lies in [k,k+1] at R*=m(k+1)/(m+1). Consequently the lesser bound is no greater than (m-k)(k+1)/(m+1). Maximize over k=0,...,m-1 to get gamma_m. The R-integer case follows directly or by continuity.

For any subset U, the positive part of sum_U e_i is at most P and the negative part in absolute value is at most N, proving the simultaneous bound.

For sharpness choose j maximizing j(m+1-j) and set every fractional part to j/(m+1). If h coordinates are rounded upward, P=h(1-j/(m+1)), N=(m-h)j/(m+1). Their maximum is minimized at h=j-1 or h=j with exact value gamma_m. Thus no algorithm selecting coordinate-wise floors/ceilings can guarantee a smaller universal constant. For m=6, choose every fraction 3/7; the optimal unavoidable cost is 12/7, replacing the earlier 7/4 bound.

## Theorem 2: threshold-preserving integer lift

Let (q,w) be a positive integer threshold realization with w_i nonnegative integers; d=2q-1. To lift to target positive integer threshold t, form real masses a_i=2tw_i/d and apply the construction of Theorem 1. If

  t/(2q-1)>gamma_n,

then the resulting nonnegative integer vector y has precisely the original positive support and the same threshold bits for every nonempty proper subset.

Proof: for any winning subset U, sum_U w_i>=q, so sum_U y_i >= 2tq/d-gamma_n = t+t/d-gamma_n>t. For any losing subset, integer mass sum_U w_i<=q-1, hence sum_U y_i <=2t(q-1)/d+gamma_n=t-t/d+gamma_n<t. For zero source masses, a_i=0; the total fractional sum is smaller than the number of strictly positive fractions, so choosing floor/ceil(R) upward indices among the largest fractions never promotes a zero-fraction coordinate. For w_i>=1, a_i>=2t/d>2gamma_n>=1 for n>=2, hence y_i>=1. This completes the proof.

## Conditional corollary: stabilization by threshold 215 for six sources

Incorporate the previously derived bounded-integer-seed lemma q<=K_n=(n+1)Delta_n and its threshold-independent profile transition lemma. Let

  B_n=floor(gamma_n*(2(n+1)Delta_n-1))+1.

Every profile ever realizable at any integer threshold is realized at every integer t>=B_n by the integer lift. Since finite policy semantics on these profiles is independent of t, the minimal observational quotient stabilizes at t>=B_n.

The classical binary maximal-determinant value Delta_6=9 yields K_6=63, gamma_6=12/7 and

  B_6=floor((12/7)*125)+1=215.

Thus, conditional on the prior unreviewed seed lemma,

  A_6(1,T)=C_6 for all integers T>=215.

C_6 and the least possible stabilization threshold are not determined. The former sufficient bound was 219. The entirely self-contained binary Hadamard upper bound Delta_6<=14 gives K_6<=98 and B_6<=335 (previously 342) under the prior seed lemma. Other improved bounds: n=4 gives 35 instead of 37; n=2,3,5 are unchanged at 4,16,89 respectively.

## Evidence and verification scope

A locally executed exact-integer/Fraction verifier exhaustively checked 219,450 rational fractional vectors for m=1..6 and denominators 2..7, checked the sharp uniform witness for m=1..10 against all 2^m rounding choices, and checked 30,000 sampled seed/lift pairs across n=2..6 by replaying each nonempty proper subset threshold bit and positive support. All passed. These tests check finite domains only. Theorem 1 and the lift theorem have complete analytic arguments above, while the BRC corollary depends on the separately unreviewed small-seed lemma.

Bibliographic background for Delta_6=9: Weisstein, Hadamard's Maximum Determinant Problem, https://mathworld.wolfram.com/HadamardsMaximumDeterminantProblem.html ; OEIS A003432, https://oeis.org/A003432. This handoff does not claim priority for rounding in general.

## Authority, P000 boundary, and next question

The authenticated GitHub identity was awdawmip. Native control_tasks returned CONTROL_QUOTA; the Sites adapter exposed research_authority_granted=false and write_relay_enabled=false. No current task owner could be confirmed, no native CLAIM was acquired, and this unreviewed branch is NOT a canonical Source Result or mathematical acceptance.

P000 remains the user's locked 6D native discrete Cell/3D-slice/120-degree-enterprise-orthogonal worldview. The auxiliary threshold masses and secret resets have no established faithful embedding into P000 native Cell path and triadic balance operations; no native theorem is asserted.

Next: bound the *actual* smallest integer seed threshold q over six-source realizable profiles (rather than all binary active determinants), then use smaller seeds to sharpen 215 and identify C_6 plus the exact first stable threshold. Also seek an explicit native typed BRC correspondence before any P000 transfer.

Global-Knowledge-Sync: main@e2c99e7 / GLOBAL_KNOWLEDGE_V1
