# BRC N=4 — sharp unrestricted randomized five-code minimax theorem

**Author analytical proof, 2026-10-31; UNREVIEWED / NOT_ADMITTED.** Direct continuation of PR #1757, prior five-symbol bound 2/143 <= R5 <= 1/40 at commit 1b87b83880f4e5ce6060194b6f58b16e8e86338e and deterministic result fac6809b94daf139160872b10b3a3197f5bc0257.

## Exact question and result

Use the original P/Q strictly positive 16-leaf (S,J,K) experiment with K fair conditional on (S,J), each individual K leaf having mass numerator /240:

| S | Q:J0 | Q:J1 | P:J0 | P:J1 |
|---|---:|---:|---:|---:|
| AU | 10 | 10 | 9 | 11 |
| AV | 20 | 20 | 5 | 5 |
| BU | 15 | 15 | 3 | 27 |
| BV | 15 | 15 | 30 | 30 |

At stage two one prepared input x=(S,b), b in {P,Q}, enters a **common stochastic encoder E with at most five symbols** before J is generated and before future policy H is chosen. A stochastic decoder D_H can depend on H, but not directly on x, actual J or K. Score the statewise full marginal public terminal record O=(T,Decision,Z_BU), with BU-only Z=J XOR independent Bernoulli(epsilon), 0<=epsilon<=1/2, and a distinct absent symbol for non-BU. There is no requirement to reconstruct the same realized path.

For F=all lawful S23 or all lawful S2 causal stop/decision policies, define

R5(F;epsilon)=inf_{common stochastic E, |C|<=5} sup_{H in F} inf_{stochastic D_H} max_x TV(L_H(.|x), (E D_H)(.|x)).

**Theorem. For every real epsilon in [0,1/2], R5(all S23;epsilon)=R5(all S2;epsilon)=1/40.** No positivity, source-homogeneity, deterministic-encoder, or cross-source separation restriction is imposed.

## Lower bound valid for all randomized encoders

The contemporaneous third-stage P/Q likelihood-ratio classes AU0, AU1, AV, BU0, BU1, BV have distinct ratios 9/10, 11/10, 1/4, 1/5, 9/5, 2. For EACH subset A of these six classes, H_A is a genuinely lawful S23 and S2 policy: continue at stage two everywhere (AU/BU conditional continuation rates both 1), stop at stage three, choose public Decision=P exactly on A, Q otherwise. This respects equal-ratio actions at AV/BV, does not read future K, and supplies all 64 Boolean subset observers.

Discarding duplicate prepared rows AV_P=AV_Q and BV_P=BV_Q leaves six rows in order AU_Q, AU_P, AV, BU_Q, BU_P, BV. Their conditional distribution M over the six LR classes is

M=(1/20)*[
 [10,10, 0, 0, 0, 0],
 [ 9,11, 0, 0, 0, 0],
 [ 0, 0,20, 0, 0, 0],
 [ 0, 0, 0,10,10, 0],
 [ 0, 0, 0, 2,18, 0],
 [ 0, 0, 0, 0, 0,20]
].

For every five-column row-stochastic E restricted to these rows, rank(E)<=5 gives nonzero w with w^T E=0; row normalization gives sum_i w_i=0. Put r=w^T M, so sum_j r_j=0. Given full-public-record TV error <=delta for every H_A, its Decision=P event probability differs by <=delta at each state. Each policy-specific decoder supplies a vector d_A with

|M_i(A) - (E d_A)_i| <=delta.

Taking the w-linear combination gives |sum_{j in A} r_j| <=delta ||w||_1 for every subset A. Because r sums to zero, max_A |sum_{j in A} r_j| = ||r||_1/2; hence

(1) delta >= ||w^T M||_1/(2||w||_1).

Now establish a **sharp reverse-channel inequality on zero-sum signed input combinations**, with a constructive rational certificate rather than approximate rank arguments:

(2) ||w^T M||_1 >= (1/20)||w||_1.

For s_i=sign(w_i) (choose either sign at a zero entry), let lambda=s_1 when s_1 != s_2, otherwise lambda=0. Define f on the six LR output classes by

f_AU0=11s_1-10s_2-lambda;
f_AU1=-9s_1+10s_2-lambda;
f_AV=s_3-lambda;
f_BU0=s_4-lambda-(5/4)(s_5-s_4);
f_BU1=s_4-lambda+(5/4)(s_5-s_4);
f_BV=s_6-lambda.

Direct row multiplication verifies **M f = s-lambda*1**. If s_1 and s_2 disagree, f_AU0 and f_AU1 equal +/-20; otherwise both equal s_1. The BU components have magnitude at most 2+5/2=9/2 and AV/BV at most 2. Therefore ||f||_infinity<=20. Using sum w_i=0,

||w||_1 = w^T s = w^T M f <=20 ||w^T M||_1,

which proves (2). The constant is sharp at w=(1,-1,0,0,0,0): ||w||_1=2 and ||w^T M||_1=1/10. Substitute (2) in (1): **delta>=1/40 for every possible randomized five-symbol E**, independent of sensor noise.

The quantifiers are preserved: E is common, each D_H may change with H, and the maximizing H_A is allowed to depend on E. There is no assumption of a single joint decoder of all policies or of deterministic source coding.

## Matching constructive upper bound for all lawful policies

Five codes are AU*, AV, BU_Q, BU_P, BV. Both prepared AU rows map deterministically to AU*; the other rows map to their exact code (AV/BV combine the identical b laws). The decoder at AU* samples J with success probability 21/40, precisely the midpoint between AU_Q's 1/2 and AU_P's 11/20. On all other codes it samples the exact conditional J probabilities (AV/BV 1/2, BU_Q 1/2, BU_P 9/10), independently samples fair K when reached, draws the BU sensor with its declared epsilon and executes the selected H.

At the two AU preparations, TV of the actual J law versus Bernoulli(21/40) is 1/40; all other preparations are exact. The complete lawful public record is a common Markov readout of this sampled future, so total-variation data processing bounds its error by 1/40 for **every** stochastic/adaptive S23 or S2 policy and every real epsilon. The legal H_{AU1} Decision=P event attains exactly 1/40 for this encoder.

Thus the all-real **unrestricted stochastic optimum is exactly 1/40**, closing the previous interval 2/143 <= R5 <= 1/40. A cross-source randomized improvement is impossible under this stated preparation/observation interface. The previous rank-based lower bound remains valid but is strictly weaker.

## Evidence scope and BRC/native interpretation

VERIFY.js was actually evaluated in a JS V8 runtime using exact integer arithmetic; RUN_EVIDENCE.txt holds the actual output. The program verifies both complete 16-leaf normalized positive laws; the distinct likelihood ratios; all 64 sign assignments and 384 rational dual identities (using integral 4f); the sharp reverse witness; and 1536 **full terminal output** comparisons for 64 legal S23 decisions, six prepared rows and epsilon in {0,1/8,1/4,1/2}. The maximal L1 numerator on denominator-320 distributions is 16, giving TV=16/640=1/40. The continuum and arbitrary stochastic encoder/adaptive-policy claims follow from the analytic proof, **not** finite enumeration.

The BRC carrier retains labeled branches, preparation provenance and the admissible future observer family. One less preparation state causes a strictly positive observer-relative statistical reconstruction residual. No result here assigns it native force, energy, physical time or an empirically calibrated Heartbeat mechanism. P000 V5's six native space axes plus separately typed time, three-dimensional slices and the protected ACTIVE residual-fidelity worldview are unchanged. A native dynamical correspondence remains a separate proof obligation.

Classification: AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_EXECUTED / PORTABLE_SOURCE / UNREVIEWED / NOT_ADMITTED; no native Task CLAIM, Result, independent review or Foundation promotion.
