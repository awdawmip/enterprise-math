# PREFIX-1054 — Complete middle spectral positivity by two-scale residual transport

Date: 2026-11-24. Parent: PREFIX-1053. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_RATIONAL_CHECKED / NOT_REVIEWED.

## Scope and immutable sources

Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json, Stage46 signed W=J12−6I12, incoming −e1, bidirectional exclusion of Link {0,e1}, exactly one outgoing negative step, full native X6 Cell–terminal-port–grade, branch identity, sign, multiplicity and provenance retained. This is a certificate for the inherited auxiliary six-phase scalar ODE and its contrast, not a new native evolution, phase/pi evaluation or classical comparison run. NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION. Mother B_fix,odd(32) in {19,20} remains open.

Actual immutable reads:
- PREFIX-1052 de0250c78a0952c5b282623dacedce81c47bad90:research_notes/portable_direct/2026-11-24_r6_prefix1052_exact_critical_connection_and_middle_analytic_branch.md (ODE, physical/middle connection and removable singularities).
- PREFIX-1053 51e35cdfcf89ba7eca79bf00a0728f0c7f919631:research_notes/portable_direct/2026-11-24_r6_prefix1053_certified_middle_connection_data.md and checker 3e54f7c578aa433a43dc4b25ff7e5a3085d46a57 (initial intervals).
- PREFIX-1051 5df27cada185084996cab98b8736d5864e333d0f (inherited upper-band positivity, as used by PREFIX-1052/1053).

Let f=F/c, v=V/c denote the normalized analytic middle density and primitive of PREFIX-1052; c>0 is the inherited upper-edge coefficient. On [4,16], the physical contrast coincides with
5g/c=4(Hf)'−2Pf+12(11+y)v,
H=y²(36−y)², P=y(y−36)(17y−91), v'=(y−6)f.
At the endpoints, the one-sided 3/2 cusp and its first derivative vanish, so the contrast agrees there by continuity.

## Main result

Conditional on the cited analytic connection and initial interval proof, the following strict lower bounds hold at EVERY point of the indicated closed intervals:
| y interval | certified lower bound for 5g/c |
|---|---:|
| [15/2,16] | 2993000 |
| [23/4,15/2] | 18466000 |
| [39/8,23/4] | 17052000 |
| [4,39/8] | 15387000 |

Therefore g(y)>598600 c on [4,16]. With PREFIX-1051, g>0 on the whole [4,36), a connected interval of length 32. Only the lower regular interval (0,4) remains to be fully certified. This is a continuous interval proof, not sample-based sign inference.

## 1. Recurrences and two-scale residual lemma

Use the polynomial coefficients a_j of L in PREFIX-1052. At center y0 write A_j(t)=a_j(y0+t) and f(y0+t)=sum b_n t^n. For scale r>0 let d_n=r^n b_n. At a critical center 4 or 16 set m=4, width w=7; at ordinary centers set m=5,w=8. For n>=m, coefficient comparison in Lf=0 yields
W_k(n)=r^k sum_(j=0..5) [t^(k−m+j)] A_j(t) (n−k)_j,
sum_(k=0..w) W_k(n)d_(n−k)=0.
Negative coefficient indices are zero; the first m Taylor coefficients are free. W_0 is nonzero for integer n>=m (indicial divisor at critical centers; a_5(y0)(n)_5 at ordinary centers).

Let l_k=−LC(W_k)/LC(W_0). For center 16 the limiting polynomial is (1+r z/12)(1+r z/16)^5(1−r z/20); at 4 it is (1+r z/4)^5(1−r z/12)(1−r z/32); at an ordinary center it is a_5(y0+rz)/a_5(y0). All factors have absolute linear coefficient <1 for the scales used. Thus a causal inverse exists with absolute-sum bound K, the product of (1−|factor coefficient|)^(-multiplicity).

For any threshold N, coefficient comparison on the shifted polynomials W_k(N+u) gives bounds |−W_k(n)/W_0(n)−l_k|<=e_k for every real n>=N: sign-normalize W_0 so all coefficients are positive, then take the maximum absolute coefficient ratio for each numerator. The checkers verify K e<1 for e=sum e_k and all listed radii/thresholds.

The PREFIX-1053 inverse-convolution lemma extends to a forced recurrence with residual |eta_n|<=eta. With B=max of the preceding w absolute state values and L=sum|l_k|+e, the uniform tail bound is
sup_(n>=N)|d_n| <= K(LB+eta)/(1−Ke).
Proof: for any finite prefix of the tail, extend by zero before N, bound the forcing under the limiting convolution by LB+e M_tail+eta, and apply the causal inverse; solve the resulting scalar inequality. The same estimate holds uniformly on any finite prefix.

New application: compute d_n at the desired radius r by directed integer fixed point, with scale M, exact free coefficients, and per-step residual strictly less than 1/M. Rather than propagate absolute errors at radius r (which discards signed cancellations), rescale the error to radius r0<=r, obtaining a residual <=1/M. Bound the first N0 errors in units 1/M by direct absolute recurrence plus 1; use the forced inverse-convolution estimate at r0 from N0 onward. Let E0 be the maximum of those two bounds. Returning to scale r gives
|d_n−dhat_n| <= (E0/M)(r/r0)^n.
Choose M to certify a uniform bound delta through the desired finite index N−1. At the larger radius r, apply the homogeneous inverse-convolution estimate at N using the certified terminal state. For n>Dcut=200, use the maximum T of that infinite-tail bound and all finite coefficient envelopes from Dcut+1 through N−1. This controls the signed recurrence at two different scales while preserving rounding error as a distinct representation residual.

Actual rational settings:
| center | r,N | r0,N0 | finite delta bound |
| 16 | 9,30000 | 5,300 | 10^-100 |
| 15/2 | 21/8,3000 | 7/8,100 | 10^-80 |
| 23/4 | 21/16,300 | 7/16,100 | 10^-80 |
| 4 | 3/2,300 | 3/2,300 | 10^-80 |

At center 16 use M=10^10000, at the other centers M=10^5000. These are sufficient fixed-point precisions, not claimed optimal. All conditions and rounding bounds are checked with exact integer/rational operations. The large scale is used only inside the inherited scalar ODE certificate.

## 2. Whole-interval polynomial and six-state transport

For a band y=y0+s ell x, 0<=x<=1, s=±1, q=ell/r<1, let u(x) be the degree-200 Taylor polynomial in x obtained by rounding each fixed-point scaled coefficient again on the 10^-50 grid. Let eta=delta+10^-50. For derivatives of order k=0,...,4, the uniform error is bounded by
E_k=[eta(Dcut+1)^(k+1)+T q^(Dcut+1)(Dcut+1)^k/(1−q((Dcut+2)/(Dcut+1))^k)] / ell^k.
The denominators are checked positive. This follows by the falling factorial bound n^k and a geometric ratio for the weighted tail. The primitive change is computed by polynomial integration of s ell (y0+s ell x−6)u(x); its error is at most ell(|y0−6|+ell)E_0. The first checker uses an equivalent tighter geometric-sum bound for k=0,1.

For each Taylor basis polynomial form its contrast polynomial, including the primitive change. The separate primitive constant contributes 12(11+y)v(y0). Convert every polynomial p(x)=sum a_i x^i of degree d to its exact Bernstein coefficients beta_k=sum_(i<=k) a_i binom(k,i)/binom(d,i). Since the Bernstein basis is nonnegative and sums to one, min beta and max beta bound the polynomial over the entire closed unit interval. Use the midpoint of the current coefficient box and add the basis-function uncertainty with absolute Bernstein maxima. Bound the analytic remainder using |H|<=36^4, |H'|<=4*36^3, |P|<=36²(17*36+91), |11+y|<=47. All these bounds apply on the present physical bands.

For the first band, start with the exact rational PREFIX-1053 initial box, and compute four separate analytic basis polynomials at 16. The resulting polynomial Bernstein minimum is approximately 2993305.31617, total error approximately 59.25398; the exact assertion is lower>2993000.

At y=15/2, transport all six state entries (f,f',f'',f''',f'''',v) by evaluating the corresponding basis jets and integrating the primitive. If a coefficient lies in Q_j±epsilon_j and a basis value lies in z_j±d_j, its uncertainty is bounded by |Q_j|d_j+epsilon_j(|z_j|+d_j). The sum yields a certified box. Round each new midpoint downward on 10^-30 grid and the error upward, including the rounding. At each ordinary center use all five initial derivatives divided by their factorials, and keep v separately. This retains the full scalar ODE state rather than replacing it by just the current contrast. Two ordinary steps reach y=39/8 from 15/2 via 23/4. The lower bounds on both bands are computed by the same Bernstein certificate.

## 3. Exact critical connection at 4 and lower-branch starting data

PREFIX-1052 proves that the middle branch is analytic through 4. Write f(4+t)=sum_(j=0..3) Q4_j R4_j(t) with R4_j normalized to initial Taylor coefficient delta_ij. Compute these four basis functions at r=3/2, match derivative orders 0..3 at t=7/8, using the state box from section 2. A fifth derivative is not required for this solve because the existence of the analytic branch is inherited; it was transported but not independently used to verify the matching theorem.

Let Ahat and D be the finite 4x4 matching matrix and componentwise absolute error matrix, xhat=Ahat^-1 bhat, C=|Ahat^-1|, and b_err the state error vector. Put K=||C D||_infty<1, u=C(b_err+D|xhat|). The Neumann bound proves componentwise
|x−xhat| <= u + K ||u||_infty/(1−K) 1.
This follows by first bounding the infinity norm of the error by ||u||/(1−K) and then substituting it in the componentwise inequality. The exact inverse and K<1 are checked. Subtract the integrated basis contributions from the transported primitive at 39/8 to enclose v(4), propagating both coefficient and integration errors. Use these parameters in the Bernstein contrast certificate on [4,39/8].

The following exact closed intervals (not floating-point rounded diagnostics) are printed by the checker, numerators divided by 100:
| quantity | lower | upper |
|---|---:|---:|
| Q4_0 | 235698 | 235702 |
| Q4_1 | -44062 | -44059 |
| Q4_2 | 6845 | 6848 |
| Q4_3 | -1244 | -1242 |
| v(4) | -5241077 | -5241068 |

These are directly usable connection data for the remaining lower physical branch:
rho(y)/c = f(y)−135(4−y)^(3/2) C4(y−4) for 0<y<4,
and U(y)/c is the corresponding integral with initial value v(4). Retain the cusp contribution separately; the analytic background alone is not the physical lower density. For future tight cancellation near 0, the narrower PREFIX-1053 initial enclosure can be propagated if needed.

## 4. Actual execution and immutable replay

Two checkers ran locally (Python/SymPy/Fraction, exact integer and rational arithmetic):
- 1a28e880d3a6224247694b947779c239ffab4ea7:research_notes/portable_direct/PREFIX1054_R6_MIDDLE_SUBBAND_CHECK.py, Git blob c85bfb4e3a054d7efd2ba46cdd0d19a8b7e2f619.
- bda07a82cf7828d43f041f14b00ef3d2a9b1cbf1:research_notes/portable_direct/PREFIX1054_R6_MIDDLE_COMPLETION_CHECK.py, Git blob 67c0ac428143fb4db1cd7a4665c2665feeef47a6.

Both immutable GitHub readbacks exactly matched the executed local bytes. Put the two files in the same directory and run the second; it imports and executes the first. The final executed output included:
```
PREFIX1054_MIDDLE_SUBBAND_CERTIFICATE_PASSED
band 7.5 5.75 lower 18466497.957567886 error 278.4397199829283
band 5.75 4.875 lower 17052430.31877272 error 502.8556838654073
local4 exact hundredth box [(235698, 235702), (-44062, -44059), (6845, 6848), (-1244, -1242), (-5241077, -5241068)]
band 4.0 4.875 lower 15387939.06492301 error 4506.335702817863
PREFIX1054_MIDDLE_COMPLETION_CERTIFICATE_PASSED
```
Decimal diagnostics are explanatory only. Exact strict integer inequalities for the four interval bounds and all tail/inverse conditions are asserted. No independent review, Lean formalization, new BRC native propagation, or attribution of the scalar result to native signed X6 is claimed.

## 5. Control and next

Owner read r6-20261124-1250-leased-observe-v1 SUCCEEDED/error=null; fixed as-of 2026-11-24T04:51:56.108788Z, Source 213c3ec64486ac904789902cd4c13481b881fffd, LEASED filter empty, 534 total tasks. Original registration r6-20261123-2358-session-start-own-v1 SUCCEEDED. Recovery metadata identifies open historical session MCP-f6d93209fc8e4c5bb2c3b44f69a47174, no runs, execution_authorized=false; Source Activity RA-0ABD84561C86E53067DB0322 is EM-DIRECT-780BBE/TASK_RESEARCH, checkpoints empty on actual readback. Current logical-session authority not established; no new CLAIM, protected Activity write, PROGRESS or formal completion. Material is preserved in independent portable notes.

Next: certify the lower physical branch on (0,4) by the new critical connection data and explicitly retained −135 cusp. Start with a rational square-root coordinate near y=4 to retain signed cusp and derivative/integral terms; approach y=0 with the inherited lower-edge expansion from PREFIX-1044 and a verified remainder. Once all three intervals are proved positive, combine with the existing Hausdorff difference equivalence, and separately resolve the native observer correspondence. Do not repeat the middle proof.
