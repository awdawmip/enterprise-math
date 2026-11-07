# S23/AV: sharp uniform error of an explicit two-trial joint reconstruction kernel

Date: 2026-11-06. Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED. Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34; exact source research_notes/brc_n4_s23_asymmetric_hull_gap_sqrt43_20261101_research1/PROOF.md. Immediate predecessor: draft PR #1777, commit 54670d366c139a6ab5310e12c1e1838f52ea7a20 (two-iid-trial bounds).

## Theorem and quantifiers

Retain original six S23 source tags AU0, AU1, AV, BU0, BU1, BV, and one lawful common b in [1/8,1/2]. Only the conditional AV row is read here. For a,c in [1/2,7/8], set z=(1-a)c, A(a,c)=(a,z,1-a-z) on full stops (1,3,4), and B(a,c)=(z,1-z) on binary outcomes (Y,N), where Y is stop 3. Both conditionally independent trials use the SAME unknown parameter (a,c). Put A2=A tensor A, B2=B tensor B. A reconstruction is ONE 4-by-9 stochastic kernel L, independent of a,b,c, permitted to use both binary outcomes jointly.

Let delta2=inf_L sup_(a,c) TV(A2(a,c),B2(a,c)L), TV(P,Q)=sum_k |P_k-Q_k|/2.

**Result: 423/2468 <= delta2 <= 235/1144.** More precisely, the constructed L below satisfies the *exact*, attained equality sup_(a,c) TV(A2,B2 L)=235/1144. The value of delta2 itself remains open.

The former universal product-kernel upper was 18549/78400. Our sharp explicit-joint-kernel upper improves it by 349507/11211200 (~0.0311748073, 13.18% relative).

## Constructive kernel

Use binary input order (Y,Y),(Y,N),(N,Y),(N,N), and full output order (1,1),(1,3),(1,4),(3,1),(3,3),(3,4),(4,1),(4,3),(4,4). Put v=8/11, t=10/13, u=9/80, w=3/520. The rows of L are:
- (Y,Y): (3,3) with probability 1;
- (Y,N): (3,1) with v and (3,4) with 3/11;
- (N,Y): (1,3) with v and (4,3) with 3/11;
- (N,N): (1,1) with t, each of (1,4),(4,1) with u, and (4,4) with w.

All other entries vanish. The rows are nonnegative and sum to 1: t+2u+w=10/13+9/40+3/520=1. The (N,N) row can correlate the reconstructed output stops, so this kernel is not a product of two identical one-trial kernels.

## Full-continuum proof: ten symmetrized corner vectors

Index the four parameter corners as theta0=(1/2,1/2), theta1=(1/2,7/8), theta2=(7/8,1/2), theta3=(7/8,7/8); write Ai=A(thetai), Bi=B(thetai). Since each component of A and B is separately affine in a and c, there exist four nonnegative product-barycentric weights lambda_i(a,c) with sum lambda_i=1 and A(a,c)=sum lambda_i Ai, B(a,c)=sum lambda_i Bi for *all real legal parameters*.

Define signed nine-vectors F_ij=Ai tensor Aj-(Bi tensor Bj)L. Then because the same parameter controls both trials,

A(a,c) tensor A(a,c) - [B(a,c) tensor B(a,c)]L
= sum_i lambda_i^2 F_ii + sum_(i<j) (2 lambda_i lambda_j) G_ij,
where G_ij=(F_ij+F_ji)/2.

Every coefficient is nonnegative and they sum to (sum lambda_i)^2=1. Convexity and homogeneity of half the l1 norm thus give
TV(A2(a,c),B2(a,c)L) <= max_(0<=i<=j<=3) ||G_ij||_1 / 2.

The ten exact rational values are:

| (i,j) | half-l1 of G_ij |
|---|---:|
| (0,0) | **235/1144** |
| (0,1) | 177/2288 |
| (0,2) | 681/4576 |
| (0,3) | 1173/9152 |
| (1,1) | 9939/112640 |
| (1,2) | 2769/22528 |
| (1,3) | 1075/6656 |
| (2,2) | 2081/18304 |
| (2,3) | 5809/36608 |
| (3,3) | 60089/292864 |

The exact Fraction checker verifies each entry and its comparison to 235/1144. For theta=theta0 only lambda_0 is nonzero, so the actual error equals 235/1144. This establishes the exact supremum for this L on the complete continuum. Symmetrizing ordered mixed-corner vectors exploits the actual shared parameter; independently parameterized trials would yield a different and weaker upper certificate.

## Universal lower bound (reused and independently rechecked)

Fix lawful b=1/8. Compare H0=(a,c)=(1/2,1/2) and H1=(7/8,7/8), with P(H1)=256/617. Two-trial Bayes-optimal binary 0-1 risks (sum of per-outcome minima) are RA2=601/2468 for the full observation and RB2=256/617 for the binary projection. Their difference is 423/2468. For ANY joint kernel L with both TV reconstruction errors <=e, compose the full-observation optimal decision rule with L to obtain a binary-observation rule. The difference of expected loss, bounded in [0,1], is <=e under each hypothesis; hence RB2<=RA2+e. Therefore e>=423/2468, and delta2>=423/2468.

## Verification, provenance and next question

Actually executed Python 3 standard-library Fraction verifier: 45 exact assertions over all 16 ordered corner reconstructions, kernel stochasticity, trial-exchange covariance, ten symmetrized rational bounds, attainment at theta0, inherited Bayes witness and improvement arithmetic. The algebraic interpolation, rather than finite sampling, establishes real-continuum coverage. Program and stdout are in VERIFY.py and RUN_EVIDENCE.txt.

This is a source-conditional S23 statistical result with explicit observer scope and preserved source provenance, not a statement about native X6 rotational dynamics. The original ten-label legal policy/encoder/decoder and minimax loss remain the separate bridge to R_beh(k,10) at k=4,6. Next: optimize general joint kernels for a still smaller upper and derive a matching lower, potentially via multi-hypothesis Blackwell decision certificates. Independent proof review, formal claim and project admission remain pending.