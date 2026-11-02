# D25 — original 216 high-band p^4 reflection and exact C1 beta-integral reduction

Date: 2026-11-02. Author-side TASK_RESEARCH logical lane: chatgpt-research-hourly-enterprise-math-20260923 (not maintenance chatgpt-hourly-enterprise-math-20260921).
State: AUTHOR-DERIVED / ALGEBRAICALLY PROVED (W4, C1-BETA) / EXACT FINITE CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. No native Source completed_units, Result, or H0/B0 experiment.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. P000 / ACTIVE X6 Heartbeat worldview and observer preservation unchanged.

## Theorem W4: fourth-digit exact reflection of the original 216 high-index tail

For any prime p=6r+1>=7 define in Z_(p)
  B_k = (2k)!(3k)!/[216^k (k!)^5] = C(2k,k)^2 C(3k,k)/216^k,
  W(N) = sum_{k=0}^N (6k+1)B_k,
  q_p(216)=(216^(p-1)-1)/p, w_p=((p-1)!+1)/p,
  H_n=sum_{h=1}^n 1/h, H_0=0.

Write k=p-j, partitioning the high-index population k=3r+1,...,p-1 into the middle band 2r+1<=j<=3r (valuation exactly 2) and ultrahigh band 1<=j<=2r (valuation exactly 3). In the middle band let d_j=3j-p,
  alpha_j=-216^(j-1) ((j-1)!)^5/[(2j-1)!(d_j-1)!],
  C_j=w_p+2H_(2j-1)+2H_(d_j-1)-5H_(j-1)-q_p(216).
Then term by term:
  B_(p-j)/p^2 = alpha_j(1+p*C_j)                (mod p^2).     (W4-M)

In the ultrahigh band let
  upsilon_j=-2*216^(j-1)((j-1)!)^5/[(2j-1)!(3j-1)!].
Then term by term:
  B_(p-j)/p^3 = upsilon_j                        (mod p).       (W4-U)

The exact source-separated weighted-tail formula is
  T_p := [W(p-1)-W(3r)]/p^2
      = M0 + Mw + Mc + U                          (mod p^2),    (W4-T)
  M0=sum_{j=2r+1}^{3r}(1-6j)alpha_j,
  Mw=6p*sum_{j=2r+1}^{3r}alpha_j,
  Mc=p*sum_{j=2r+1}^{3r}(1-6j)alpha_j*C_j,
  U=p*sum_{j=1}^{2r}(1-6j)upsilon_j.
Equivalently W(p-1)-W(3r)=p^2*T_p (mod p^4). All denominators are p-units. No CM0 or conjectural character identity is required.

### Proof

For k<p, v_p(B_k)=floor(2k/p)+floor(3k/p), yielding valuations 2 and 3 in the two indicated bands. For 0<=a<p the factorial decomposition is exact:
  (p+a)!/p=(p-1)!a! prod_{h=1}^a(1+p/h).
The Wilson reflection holds modulo p^2:
  (p-a)!=(-1)^a/(a-1)! * [1+p(H_(a-1)-w_p)].
It follows by dividing (p-1)!=-1+p*w_p by prod_{h=1}^{a-1}(p-h). Also H_(p-a)=H_(a-1) (mod p).

In the middle band 2(p-j)=p+(p-2j), 3(p-j)=p+(p-d_j). Apply the exact decomposition to each numerator factorial, reflect (p-2j)!, (p-d_j)!, and (p-j)!, and insert 216^(-(p-j))=216^(j-1)(1-p*q_p(216)) mod p^2. The first-order contributions are
  -2w_p +(H_(2j-1)+H_(d_j-1)-2w_p)
  +(H_(2j-1)+H_(d_j-1))-5H_(j-1)+5w_p-q_p(216)
  = C_j.
The leading sign is negative because d_j-j=2j-p is odd. This proves W4-M.

For 1<=j<=2r, 3(p-j)=2p+(p-3j), while 2(p-j)=p+(p-2j). The leading relations (2p+a)!/p^2=2a! (mod p) and (p+a)!/p=-a! (mod p) for a<p, combined with Wilson reflection, give precisely the stated -2 and upsilon_j, proving W4-U. Multiply the original term by 6(p-j)+1=1-6j+6p and sum over both disjoint bands. This proves W4-T.

### Exact finite evidence and BRC scope

The independent integer-only verifier reconstructs every original B_k by its factorial-ratio recurrence modulo p^4, and separately reconstructs the reflected source from integer factorials, Wilson/Fermat quotients and harmonic inverses. It checks every middle/ultra coefficient and the four-port signed tail at all 611 primes p<=10000, p%6=1. All pass. Selected exact certificates:

| p | T mod p^2 | first tail digit | new next digit | (M0,Mw,Mc,U) mod p^2 |
|---:|---:|---:|---:|---|
| 13 | 140 | 10 | 10 | (49,39,156,65) |
| 19 | 237 | 9 | 12 | (199,190,133,76) |
| 373 | 33463 | 266 | **89** | (137157,62664,8206,103694) |
| 1171 | 546734 | 1048 | 466 | (1214204,38643,539831,125297) |

At 373 the four values sum to 311721=33463 (mod139129). The previous mod p observer saw 266; the next digit is 89. The three new source ports repair fourth-digit information for this exact signed observer, with no global minimality claim.

## Theorem C1-BETA: exact finite beta integral for the existing character-kernel target

For every integer r>=1 set n=3r and for 0<=m<=2r define
  v_s=(-1)^(s+1)*2^s/[4s*C(n,s)] (1<=s<=m),
  V_m=sum_{s=1}^m v_s; V_0=0,
  T_m=(-1)^m 2^(-m) C(3r,m)C(2r,m)C(4r,m),
  P_r(x)=sum_{m=0}^{2r}(6m+1)T_m*x^m,
  Hbin(r)=sum_{m=0}^{2r}(6m+1)T_m*V_m.

Then the following are **exact rational identities**:
  V_m=1/2*integral_0^1 [(1-t)^n-(-2t)^m(1-t)^(n-m)]/(1+t) dt,   (B1)
  Hbin(r)=1/2*integral_0^1 (1-t)^n [P_r(1)-P_r(-2t/(1-t))]/(1+t) dt. (B2)

Proof. The finite beta integral
  1/[s*C(n,s)]=integral_0^1 t^(s-1)(1-t)^(n-s) dt
followed by the finite geometric sum of (-1)^(s+1)2^s/4 gives B1. Multiply by (6m+1)T_m and sum over m to obtain B2. In B1 the numerator vanishes at t=-1, so division by 1+t is exact in Q[t], and the quotient has degree <=n-1. B2 is a finite sum of these polynomial quotients. Integration denominators are 1,...,n; when p=6r+1 they are p-units and mod-p reduction is valid.

A separate exact Fraction/polynomial-long-division program verified every m and the final aggregate for r=1,2,3,4,6,8. Examples: Hbin(1)=-14, Hbin(2)=-48559/96, Hbin(3)=-8114143/960. The universal previous C1 character conjecture
  Hbin(r) ?= 3*((2/p)-1) (mod p), p=6r+1
is **still open**. B1/B2 provide an exact alternative polynomial-integral / creative-telescoping target with no assumption of C1.

## Source interfaces and next

W4 carrier: exact original indexed high-band coefficients, valuations, signed weights and origin tags; observer: original tail modulo p^4. Four repair ports are sufficient for this observer and horizon (BRC COMPOSE_APPLIED). C1-BETA carrier: original ordered (m,s) pairs and beta moments, final observer Hbin modulo p; the integral factors exactly through this aggregate and original provenance remains available in U3/U4/V1/V2 (BRC EXTEND_EXISTING_TOOL). No unproved quotient of arbitrary future observers is used.

The frozen D25 mother objective is Delta_p-R_p=0 mod p for p=13 or19 (mod24), equivalent **under previously established D24/CM0 and original-cutoff reductions** to original full W(p-1)=p mod p^3. A separate onhour lane has finite exact W character tests through p<=10000 and targets to p<=20000; these are not universal proofs and are not recredited. Next small units: seek exact terminating WZ/contiguous/integral certificate for C1 or original W full p^3 character (weight, coefficient and cutoff exactly as stated); test p=13,19,373 plus p=5,7 controls; combine a valid identity with signed D25 residual. Original p373 native H0/B0, semilinear Frobenius, signed Green/Hesse/kappa and independent replay remain NOT_EXECUTED (previous support issue #1559).

Native gateway live-read 2026-11-02 ~11:11 UTC: v0.6.11, UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false; active job quota 5/5. #6637 and #6638 are **historical**, not independently re-read in this turn. No new service session, claim, open, Source checkpoint, Result or independent mathematical admission. Existing service identity/staging preserved. Activity REGISTER_PENDING. Existing control support #1558 is historical routing. Scheduler and notification settings unchanged.
