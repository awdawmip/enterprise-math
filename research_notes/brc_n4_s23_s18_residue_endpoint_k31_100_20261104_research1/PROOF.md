# BRC N=4 / S23 — residue-class endpoint theorem and certified K=31..100 optimum at s=1/8

Date: 2026-11-04. Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Model: source-tagged classical statistical observation, not native BRC-Shor physical dynamics. The observer erases a source tag only in the declared future Chernoff-discrimination experiment; P000 and joint-provenance requirements are unchanged.

## Model and claim

Fix s=1/8, h=1/42, v=2h=1/21. Set a=s(1+v)/2=11/168 and b=s(1-v)/2=10/168.
Full source observation T has P_T=(a,1-s,b), Q_T=(b,1-s,a); Bernoulli coarse observation B has P_B=(a,1-a), Q_B=(b,1-b). Costs are c_T=15/8 and c_B=1. Independent observations share ONE Chernoff exponent:

f_X(t)=-log(sum_y P_X(y)^t Q_X(y)^(1-t)),  C(m,n)=max_{0<=t<=1}{m f_T(t)+n f_B(t)}.

A budget-K allocation has integers m,n>=0 and 15m+8n<=8K. No separate optimizer values are added as an equality.

**Result 1 (general rational-cost residue endpoint reduction).** Suppose observation types T and B have costs p/q and 1, with p,q positive coprime integers and f_B(t)>0 for 0<t<1. For every nonnegative integer K, an optimum can be selected from at most 2q allocations. For each feasible remainder r in 0,...,q-1, let

a_r=ceil(pr/q), J_r=floor((K-a_r)/p).
Candidate endpoints are (m,n)=(r,K-a_r) and (r+q J_r, K-a_r-p J_r).

Proof. Each m has a unique decomposition m=r+qj; its maximum feasible B count is n=K-a_r-pj, where 0<=j<=J_r. Taking an available extra B strictly raises positive-information Chernoff performance for this nontrivial experiment (the common maximizing t lies inside (0,1)). For fixed r and K,

C_r(j)=max_t {j[q f_T(t)-p f_B(t)] + r f_T(t)+(K-a_r)f_B(t)}.

This is a pointwise supremum of functions affine in j and hence convex. For j in [0,J_r], C_r(j)<=max{C_r(0),C_r(J_r)}. Thus a maximizer is among the endpoints, with at most two per residue. This theorem holds for every K; it does not rely on the efficiency ranking and does not assert a constant-bit-cost algorithm.

**Result 2 (complete K=31..100 unique optima at s=1/8).**

| K | Unique optimal (m,n) |
|---|---|
| 31..39 | (16,K-30) |
| 40..44 | (0,K) |
| 45..59 | (24,K-45) |
| 60..74 | (32,K-60) |
| 75..89 | (40,K-75) |
| 90..100 | (48,K-90) |

In combination with the separately preserved K=1..30 certificate (immutable predecessor at 9b2a85e7248c47c82d25e64d85ad872aa59e8c69), this supplies a complete author-side classification through K=100.

## Proof for Result 2

Write C_T=max f_T=f_T(1/2), C_B=max f_B, and E=C_T-(15/8)C_B. The exact rational verifier establishes

0<E<191/10^11;  53 E<C_B/8.

For any feasible pair let u=K-(15/8)m-n>=0. Using the valid upper bound C(m,n)<=m C_T+n C_B,

C(m,n)-K C_B <= m E-u C_B.

For K<=100, m<=floor(8K/15)<=53. If 8 does not divide m, u>=1/8 (fractional cost slack), so this value is strictly negative. Thus every non-multiple-of-eight m is worse than pure B. For m=8j, the best n is K-15j, with j=0,...,L=floor(K/15).

The function j -> C(8j,K-15j) is convex by Result 1 and therefore only endpoints j=0 and j=L can win. Set K=15L+r, 0<=r<=14, and compare the last endpoint with pure B by

H_L(r)=C(8L,r)-(15L+r) C_B.

Because f_B(t)<=C_B, one has C(8L,r+1)<=C(8L,r)+C_B, hence H_L(r+1)<=H_L(r).

The executed rigorous rational enclosures give four decisive inequalities:

H_2(9)>1706/10^12; H_2(10)<-691/10^12;
H_3(14)>1339/10^12;
32 C_T+14 f_B(1/2)-74 C_B >2772/10^12.

The last expression is a lower bound on H_4(14), achieved by the common exponent t=1/2. Write g=8 C_T-15 C_B>0 and d=C_B-f_B(1/2)>=0. For L>=4 and r<=14,

H_L(r)>=L g-r d>=4g-14d>0.

For L=2, monotonicity and the certificates at r=9 and r=10 yield a last-endpoint winner precisely at r=0..9 and pure-B winner at r=10..14. For L=3, H_3(14)>0 gives last-endpoint winners for all r=0..14. For L>=4, the center-probe lower bound proves last-endpoint winners at every r<=14. Here L>=2 throughout K=31..100. In each case the endpoint comparison is strict; convexity then makes every intermediate j strictly suboptimal. Non-multiple-of-eight m were eliminated strictly above. Therefore the table gives the unique global maximizer for each integer K=31..100. QED.

## Certified calculation / coverage

Set delta=2t-1, k=s/(2-s)=1/15, R=sqrt(1-v^2), R_B=sqrt(1-k^2 v^2), alpha=atanh(v), gamma=atanh(kv). The exact Chernoff coefficients are

Z_T(delta)=1-s+s R cosh(alpha delta);
Z_B(delta)=(s R/2)exp(alpha delta)+((2-s)R_B/2)exp(-gamma delta).

For F_{m,n}(delta)=-m log Z_T(delta)-n log Z_B(delta), the true optimized value is max_delta F_{m,n}(delta). Throughout delta in [-1,1], curvature bounds follow from the tilted-distribution variances:

(log Z_T)'' >= v^2[s(1-v^2)-v^2]>1/5000;
(log Z_B)'' >= b(1-a)v^2>1/10000.

Thus F''<=-mu with mu=m/5000+n/10000. Any rational probe d in [-1,1] gives an exact lower bound F(d) and upper bound F(d)+F'(d)^2/(2mu). The validator encloses every term with Fraction rational intervals and applies this inequality for C_B and the three mixed comparisons.

Rational probes d_B=7412849/10^9, d_2,9=1710806/10^9, d_2,10=1853374/10^9, d_3,14=1759134/10^9. Its positive square roots use an integer-square-root 10^30 grid. atanh is a positive 12-term series with upper tail x^25/[25(1-x^2)]; exp is a 10th-degree Taylor polynomial with geometric upper bound on positive input and reciprocal interval for negative input; -log z uses nine positive odd powers of w=(1-z)/(1+z), with remainder <=2w^19/[19(1-w^2)]. The program's inequalities are exact Fraction assertions; float conversion occurs only to print human-readable decimal approximations after all assertions. No gridded search or approximate real optimizer participates in the proof.

Executed local script: VERIFY.py; captured output: RUN_EVIDENCE.txt; reproducibility uses Python 3 standard library only. Curvature reasoning above supplies the proof not contained in the finite exact program. Only K=31..100 classification is newly established here; the general residue theorem is valid for arbitrary rational trial cost and integer K under its displayed conditions.

The original ten-label decoding minimax mother objective remains at the previously recorded open interval [1/2,2/3]. No native CLAIM, Result, independent review or mathematical admission is claimed by this author-side note.
