# PREFIX-615-R2 — 1+2+4 exact splitting and one-residue phase-3 closed form

Date: 2026-11-09 Asia/Shanghai. Status: AUTHOR-SIDE EXACT PROOF + EXECUTED ORIGINAL 48-PHASE CHECKER; INDEPENDENT REVIEW PENDING.
Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Dependency: PREFIX-613–614, commit 4d276201aec4e8c0dc578d15ac0e0df66c23b47f.

## Scope and question

For the original typed positive-branch-sum X6 STAR 48-phase matrix Q(g) with six-axis weights (1,1,1,1,0,0), g>=0, set d=e4+e11+e14+e32 (zero-based original phase indices). The original 96 ports and 576 tagged actions remain upstream provenance. Let a,b>=0 be the first two chronological gates, q1,...,qt>=0 later gates, lambda>0 the known paired-input difference scale, and h=e3^T the original phase-3 *sum* observer. Study

X_t = h Q(q_t)...Q(q_1)Q(b)Q(a)(lambda d), t>=0.

This is an exact observer-specific quotient; it does not reconstruct tagged path histories or preserve arbitrary future per-port measurements. The prior PREFIX-614 7-state carrier DOES reconstruct the complete original 48-phase sum vector for the same input family.

## Theorem 615.1 — Exact simultaneous 1+2+4 direct sum

Reuse the previous original-phase 48x7 E, and 7x7 T0,T1, satisfying Q(g)E=E(T0+gT1). Columns of E are (A^2d, DAd, ADd, A^3d, A^2Dd, A^4d, A^3Dd) with A=Q(0), D=Q(1)-Q(0). Their previously proved pivot minor is -16384. Define the *explicit fixed rational* 7x7 basis change S with rows:

    1/2, 1/2,-1,     0,0,0,0
     -3,   0, 0,     1,0,0,0
   -9/4,-3/4,3/2,    0,1,0,0
      0,   0, 1,     0,0,0,0
   -7/8,-1/8,-5/4,   0,0,1,0
    1/8,-1/8,-1/4,   0,0,0,0
   -5/8, 1/8, 1/4,   0,0,0,1

Direct exact multiplication certifies det(S)=-1/8 and, for *symbolic g*,

S^{-1}(T0+gT1)S = diag( [2], [[0,-4],[1,0]], B(g) ),

    B(g)=[ [0,0,0,4(g+3)],
           [1,0,0,0],
           [0,1,0,0],
           [0,0,1,0] ].

The one-dimensional and two-dimensional summands are independent of the gate; the four-dimensional summand carries the entire dependence. Therefore

charpoly(T0+gT1)=(x-2)(x^2+4)(x^4-4g-12).

More specifically, the *original* phase-3 output row and a two-gate state are

(hE)S=(2,-2,4,1,0,0,0),
S^{-1}(1,b,a,0,0,0,0)^T=(1,1,0,3+b,3+a,1,1/2)^T.

This gives a complete symbolic proof of the split; it is stronger than characteristic-polynomial factorization alone because the similarity and readout identities are proved in the original 48-phase embedding.

## Theorem 615.2 — Every prefix uses exactly one gate residue class

For t>=0, put r=t mod4, k=floor(t/4), j=(-t) mod4, and define

    beta_t = 16^k * [0,8,16,0][r],
    w=(3+b,3+a,1,1/2),
    P_t=product(4(q_s+3): 1<=s<=t and s mod4=r),

where an empty product is 1. Then for ALL a,b,q_s>=0 and lambda>0,

    X_t = lambda*(beta_t + w[j]*P_t).

Proof: The 1D block contributes 2^(t+1). The 2D block R satisfies R^2=-4I and, with input (1,0) and readout (-2,4), contributes -2(-4)^m at t=2m and 4(-4)^m at t=2m+1. Combining the contributions by t mod4 yields beta_t. In B(g), a coordinate rotates forward one slot; the only multiplying edge is slot3->slot0 with factor 4(g+3). To land in slot0 at time t, its unique source is slot j; the multiplying edges occur precisely at steps s congruent to t mod4. Hence the contribution w[j]*P_t. Sum the two readout contributions and multiply by lambda. QED.

Examples: X_0=lambda*(3+b); X_1=lambda*(8+2(q1+3)); X_2=lambda*(16+4(q2+3)); X_3=lambda*4(3+a)(q3+3); X_4=lambda*4(3+b)(q4+3). beta_t vanishes for t mod4=0 or 3. One final phase-3 scalar depends on one residue class of later gates, while the full prefix sequence observes all four classes: observer-specific factorization is not a claim that the other gate positions or tagged histories are redundant.

## Algorithmic accounting and tests

To obtain ALL t=1,...,n phase-3 prefix readings, keep 4 exact running products p[0..3]=1. At step t update p[t mod4] <- p[t mod4]*4(q_t+3), maintain one exact power 16^floor(t/4), and output lambda*(beta_t+w[(-t)mod4]*p[t mod4]). This performs O(n) scalar arithmetic operations and holds O(1) live scalar registers, rather than updating the 48-phase vector or even the 7-state carrier for this single observer. Reading all n gate inputs already requires Omega(n) input inspections. Arbitrary rational numerators/denominators and final product bit lengths remain a separate exact bit-complexity cost; no general bit-time speedup is asserted. Q(0) has 96 nonzeros; the previous T0,T1 have 13 and 4.

Standalone exact checker PREFIX615_R2_phase3_closedform_checker.py reconstructs the original STAR/48-phase Q, re-derives E, T0, T1, verifies S^{-1}(T0+gT1)S symbolically, the readout row, initial tail, and characteristic polynomial; then checks four independent integer/rational/zero gate-word families: 2880 individual original 48-phase equalities, 60 closed-form phase3 equality checks, and 56 streaming-prefix checks, all passed. The universal result follows from the displayed block identity, not the finite tests. See PREFIX615_R2_phase3_closedform_results.json.

Research status: AUTHOR-SIDE PROOF; EXACT TESTS EXECUTED; NO INDEPENDENT DRIVER REVIEW, NATIVE RESULT OR FOUNDATION PROMOTION.

Next discriminating unit: construct the frozen original 96-port to 48-phase output interface and test, one chosen port-specific readout at a time, whether it factors through this 7D embedding and then 1+2+4. When it does not, exhibit an exact tagged two-source counterexample and compute the smallest repair coordinate. Compare preparation, input bit-length, prefix cost and port reconstruction end to end before claiming a full native 96-port speedup.
