# S23/AV two-trial reverse deficiency: a certified joint-kernel bound of 947/5000

2026-11-06 | AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Predecessor: draft PR #1777 at `38dfc779fae5cdedc2285d8b317fb798af39b85b`. This conditional AV observation is extracted from the full tagged S23 law; six tags AU0, AU1, AV, BU0, BU1, BV and shared b are preserved in the mother model.

## Question and theorem

For all real a,c in [1/2,7/8], with b fixed arbitrarily in its original legal interval [1/8,1/2], define the full AV stop law on labels (1,3,4) and the binary stop-3 projection on (Y,N):

```
z=(1-a)c; A(a,c)=(a,z,1-a-z); B(a,c)=(z,1-z).
delta2 = inf_{L in Stoch(4,9)} sup_{(a,c) in [1/2,7/8]^2}
          TV( A(a,c) tensor A(a,c), (B(a,c) tensor B(a,c)) L ).
TV(P,Q) = sum_k |P_k-Q_k|/2.
```

Two trials are conditionally independent given the SAME unknown (a,c); the single 4-by-9 stochastic kernel L is independent of a,b,c and may make joint randomization decisions. A reverse Blackwell kernel need not reproduce the original Y/N observation when its output is projected back to bits.

**New theorem: 423/2468 <= delta2 <= 947/5000.** The exhibited L has EXACT maximum error 947/5000, attained at a=c=1/2. This improves the previous explicit-joint-kernel upper 235/1144 by exactly 5727/357500 (>0), a 7.80% relative reduction. The exact minimax value delta2 remains open.

## Rational reconstruction kernel

Rows: YY, YN, NY, NN. Columns: 11,13,14,31,33,34,41,43,44. Every integer below is a numerator over 10000.

| input/output | 11 | 13 | 14 | 31 | 33 | 34 | 41 | 43 | 44 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| YY | 0 | 0 | 0 | 0 | 10000 | 0 | 0 | 0 | 0 |
| YN | 0 | 239 | 0 | 5881 | 0 | 0 | 2436 | 1111 | 333 |
| NY | 0 | 5881 | 2436 | 239 | 0 | 1111 | 0 | 0 | 333 |
| NN | 7534 | 321 | 912 | 321 | 0 | 0 | 912 | 0 | 0 |

All entries are nonnegative; each row sums to 10000. The kernel commutes with trial exchange, although trial exchange invariance is not needed for the abstract minimax definition.

## All-real proof: ten signed symmetrized corner vectors

Let the four corners be theta0=(1/2,1/2), theta1=(1/2,7/8), theta2=(7/8,1/2), theta3=(7/8,7/8), and write Ai=A(thetai), Bi=B(thetai). Every coordinate of A and B is separately affine in a and c. Consequently the usual nonnegative product-barycentric corner weights lambda_i(a,c), summing to one, satisfy *exactly for every real parameter pair*:

```
A(a,c) = sum_i lambda_i Ai,   B(a,c) = sum_i lambda_i Bi.
```

Define signed output error vectors F_ij = Ai tensor Aj - (Bi tensor Bj)L; put G_ii=F_ii and G_ij=(F_ij+F_ji)/2 for i<j. The SAME parameters are used on both trials, so the joint reconstruction error is

```
sum_i lambda_i^2 G_ii + sum_{i<j} (2 lambda_i lambda_j) G_ij .
```

The ten coefficients are nonnegative and sum to (sum lambda_i)^2=1. The convexity of half the l1-norm therefore bounds TV on the entire continuum by the largest of the ten exact numbers below.

| (i,j) | half-l1(G_ij) |
|---|---:|
| 0,0 | **947/5000** |
| 0,1 | 32873/320000 |
| 0,2 | 5903/64000 |
| 0,3 | 95473/1280000 |
| 1,1 | 163319/1280000 |
| 1,2 | 1183/8000 |
| 1,3 | 60571/320000 |
| 2,2 | 13243/128000 |
| 2,3 | 139843/1024000 |
| 3,3 | 242263/1280000 |

These are exact rational calculations from the integer kernel, reproduced in VERIFY.py. The maximum is 947/5000. At theta0, lambda0=1, so its actual TV is 947/5000. This establishes the EXACT supremum for the displayed kernel over all lawful real a,c, rather than only a finite mesh.

## Universal lower witness and scope

Reuse the predecessor's two lawful hypotheses theta0 and theta3, prior P(H1)=256/617. Their two-trial Bayes binary-classification risks are RA=601/2468 on the complete observations and RB=256/617 on their binary projections, with gap RB-RA=423/2468. If a common reverse kernel achieves worst TV <= e, composing the full-observation Bayes rule with that kernel yields a binary rule with Bayes risk <=RA+e. The [0,1]-valued-loss TV inequality gives RB-RA<=e, proving delta2 >=423/2468. VERIFY.py independently repeats this exact risk arithmetic.

This work reuses the prior AV source law and the symmetrized-corner interpolation argument (REUSE_APPLIED); it supplies a new rational kernel witness, not a new general-purpose BRC method. The target output is the full stop-pair distribution, and this TV bound concerns two conditionally iid AV observations only. Application to the frozen ten-label S23 encoder/decoder minimax game requires a separate legal mapping. The current proof is author-side and has no independent mathematical admission.

Exact execution: 45 assertions using Python standard-library Fraction. VERIFY.py and RUN_EVIDENCE.txt preserve the runnable certificate and actual stdout. The continuum result follows from the algebraic interpolation above, not from checking a grid.

Next: optimize the 4x9 rational kernel further, derive an exact lower dual/decision witness (possibly multi-hypothesis), and independently check the bridge to original R_beh(k,10) for k=4,6.
