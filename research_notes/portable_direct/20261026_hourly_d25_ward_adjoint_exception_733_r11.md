# D25/LIFT — Central-binomial Ward-adjoint boundary and prime 733

2026-10-26; TASK_RESEARCH logical lane chatgpt-research-hourly-enterprise-math-20260923. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, science pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This is a new obstruction for one corrected-Clausen lower-adjoint *observer*, NOT a counterexample to the original-class LIFT/JT2 conjecture. Consume, do not re-credit, the earlier Ward lower-adjoint recurrence and Hasse-(1,2) source-face theorem.

Put p=6m+1 prime, N=2m-1, L=-N. The previously proved exact rational adjoint is
lambda_0=0; lambda_{k-1}=((p-2k)lambda_k-2^k)/(p-2k+1),
delta=2^(-N)-(p+2N)lambda_{-N}.
The exact lower-oriented source identity is
sum_{n=L}^0 2^n Y_n^{ab}=sum_{n=L}^{-1} lambda_n S_n^{ab}+delta Y_L^{ab}.
The genuine unweighted corrected-Hasse face obeys
Y_L^{12} = 4(-1)^m / [binom(2m,m)(2m+1)(m+1)] (mod p), a p-unit for EVERY target prime.

THEOREM (closed finite-field boundary criterion). For 1<=t<=N let
S_t=sum_{r=0}^{t-1} binom(2r,r)/8^r,
A_t=2^(2t-1)/(t binom(2t,t)).
Then lambda_{-t} = -A_t S_t (mod p), and
delta = 2^(-N) + [4^N/binom(2N,N)] S_N (mod p).
Therefore delta Y_L^{12}=0 mod p if and only if this explicitly stated truncated-binomial expression vanishes. That is a condition on this adjoint observer, not on raw Hasse source.

PROOF. With b_t=lambda_{-t}, the exact recurrence is
b_0=0, b_t=((p+2t-2)b_{t-1}-2^(1-t))/(p+2t-1).
Since 2N<p, all reduction denominators are p-units; mod p,
b_t=[2(t-1)b_{t-1}-2^(1-t)]/(2t-1).
A_1=S_1=1, so b_1=-A_1S_1. For t>=2 use
A_t/A_{t-1}=2(t-1)/(2t-1),
A_t [binom(2t-2,t-1)/8^(t-1)]=2^(1-t)/(2t-1)
and induction. At t=N use 2N A_N=4^N/binom(2N,N). Since Y_L^{12} is a p-unit, the vanishing equivalence follows. Over Q the same recurrence proves b_t<0 and delta>2^(-N)>0, but rational positivity does NOT forbid a finite-field zero. QED.

NEW EXACT COUNTEREXAMPLE. At p=733=6*122+1, m=122, N=243:
S_N=693, binom(486,243)=5, 4^243/binom(486,243)=110, 2^(-243)=2 (all mod733).
Since 110*693=731=-2 mod733, delta=0 mod733.
An independent direct backward recurrence gives lambda_{-243}=549 mod733.
The *raw* corrected Hasse face is Y_L^{12}=610 !=0 mod733, yet the *adjoint-weighted* face is delta Y_L^{12}=0 mod733.
The same unexpanded exact recurrence modulo 733^2 returns delta=176653=733*241 mod 733^2. Hence delta has exact 733-adic valuation one, and (delta Y_L^{12})/733=241*610=410 mod733. This is a sharply digit-dependent information-loss witness; a cancelled first-digit scalar still carries a nonzero second-digit residual.

AUTHOR CHECK. The original backward recurrence was compared against independently computed central-binomial partial sums at every t for all 80 primes p=6m+1, 7<=p<=997. The explicit bounded classification found only p=733 within that range; no claim of global uniqueness. Full standard-library checker: 12,287 exact assertions PASS including the p=733 p^2 lift and rational sign spot-checks. Finite samples do not replace the general induction; no original-class native CM or independent review was performed.

BRC observer: preserve (j,ell,Hasse channel,orientation,p-valuation) and the distinction between unweighted Y_L and its operator projection delta Y_L. The result refutes universal persistence of nonzero source through *this* scalar projection; it does not cancel original T12 or its separate infinity port. Next unit: compare p=733 second-digit repair against exact three-channel signed reflection and infinity, while separately pursuing the Source-identified original-class H0/B0/[X]U/Frobenius eta/kappa and Delta_p-R_p. Native Source checkpoint, Result, review and mathematical admission remain pending.
