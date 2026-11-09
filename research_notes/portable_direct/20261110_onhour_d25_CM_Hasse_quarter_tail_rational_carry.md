# D25 on-hour: quarter-length Hasse tail and rational signed CM carry

Date: 2026-11-10. TASK_RESEARCH. Logical Research lane: `chatgpt-research-onhour-enterprise-math-20260923` (not maintenance). Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen science `c47e13e4aba0e006366f989d6334d443f6333ae3`. Source checkpoint `b58330b74576153cdadde5d80a3d92df3a819a0e` unchanged. AUTHOR-SIDE / UNREVIEWED / NOT_ADMITTED / NON-NATIVE.

## Exact theorem: replace the full finite-log product by one quarter-length tail

Let p ≡ 13 (mod 24) be prime, q=(p-1)/4 (odd), d=1/36, R=F_p[t]/(t²-2),
s=1/2-t/3, s*=1/2+t/3, so ss*=d and s^p=s*. Define

G_p(X)=sum_{k=0}^{p-1}(1/4)_k(3/4)_k X^k/(k!)²,
L_p(X)=sum_{j=1}^{p-1}X^j/j (mod p),
A_p(X)=[(G_p mod p)L_p(X)]_{<p}.

Write C_k=(-1)^k binom(q,k)binom(q+k,k) for 0≤k≤q and
U_r=sum_{k=r+1}^q C_k/(k-r) in F_p, 0≤r<q.
Let T_0=2, T_1=1, T_n=T_{n-1}-d T_{n-2}.
Let D_0=0, D_1=-2/3, D_n=D_{n-1}-d D_{n-2}.

**Theorem.** Assuming the previously author-proved CM(-24) Hasse root G_p(s)=0 (mod p), the following are exact in F_p:

(1) G_p(X) mod p = P_q(1-2X) = sum_{k=0}^q C_k X^k.

(2) A_p(s) = s* U_0 + d sum_{r=1}^{q-1} U_r s^{r-1} in R.

(3) Tr(A_p(s)) = U_0 + d sum_{r=1}^{q-1} U_r T_{r-1}.

(4) Coeff_t(A_p(s)) = U_0/3 + (d/2) sum_{r=1}^{q-1} U_r D_{r-1}.

Thus BOTH the even trace and odd coordinate are preserved by a q-term signed boundary source. The derivation uses only coefficientwise finite polynomials, not an infinite-series interchange or unsigned norm projection.

**Proof.** Since p=4q+1, -q=1/4 (mod p), q+1=3/4 (mod p).
For k≤q the coefficients of G_p and P_q(1-2X) coincide modulo p; for q<k<p the factor (1/4)_k contains p/4. Therefore the reduction is exactly the degree-q Legendre polynomial, with coefficients C_k. The full product P_q(1-2X)L_p(X) has degree at most p+q-1. Its high-degree part is X^p H(X), with
[X^{p+r}]P_q(1-2X)L_p(X) = sum_{k=r+1}^q C_k/(p+r-k) = -U_r (mod p).
Hence P_q(1-2X)L_p(X)=A_p(X)-X^p sum_{r<q}U_r X^r. Evaluate at the previously proved root s, use s^p=s* and ss*=d, giving (2). Taking sum and difference of the two Galois conjugates yields (3) and (4). The recurrence for T and D follows from s+s*=1 and ss*=d. QED.

## Independent p² first-jet certificate, rational field only

Let y=2t/3 and let P_n(y)=y f_n(y²) for n=q and n=3q (both odd), with f_n in Z_(p)[Y]. The elementary polynomial Taylor cancellation
  4G_p(X) = 3 P_q(1-2X) + P_{3q}(1-2X) (mod p²)
holds coefficientwise: the Pochhammer parameters for the two Legendre terms differ from (1/4,3/4) by (-p/4,+p/4) and (+3p/4,-3p/4) respectively, and the 3:1 weighted first derivatives cancel. This identity includes the k>q boundary; it is not a truncated low-index approximation. At s the t-coordinate of G_p(s)=p g_p t (mod p²) thus gives
  6p g_p = 3 f_q(8/9)+f_{3q}(8/9) (mod p²).
Both sides use integral p-adic representatives with denominators prime to p. The open original CM carry identity is EXACTLY the single rational-field certificate

  U_0+d sum_{r=1}^{q-1}U_r T_{r-1}
     ?= (4/p)(3 f_q(8/9)+f_{3q}(8/9))    (mod p).

This is a shorter, signed, reproducible candidate for Jacobi/Legendre WZ research, not a proof that the question-marked equality holds for every target prime.

## Exact checks and provenance

The companion standard-library Python checker constructs original Gauss coefficients mod p², evaluates both Legendre polynomials mod p² in F_p², independently convolves Gbar with finite log, and compares the quarter-tail and rational trace, all with exact modular integers. All 22 primes p<1000 with p≡13 mod24 passed every *proved identity* check; the open equality also held on these 22 test cases. Examples (p, q, Tr(A), g, U_0, coefficient of t in A):
(13,3,7,3,5,11), (37,9,19,27,6,31), (373,93,149,115,105,174), (613,153,599,357,174,404), (997,249,799,241,422,931).
In particular p=373: Tr(A)=149=24·115 mod373. The odd value 174 is retained rather than erased by trace.

BRC COMPOSE_APPLIED: original signed C_k and U_r are the carrier; trace and odd coefficient are separate declared observers. The tail operation reconstructs BOTH observers at p precision under the stated root, with exact equality; it does not identify this auxiliary quadratic algebra with native six-axis space or the native H0/B0 crystalline operator.

## Frontier and next action

Reuse the exact raw coefficient/finite-log and Legendre identities above. Next target: construct a terminating Jacobi/Legendre telescoping identity for the rational certificate, possibly via the 3:1 p-shift of Legendre parameters or a second-kind polynomial. In parallel highest native experiment #1559 remains *NOT_RUN*: same-original-class p=373 [X]U mod 139129, rank, semilinear Frobenius direction/eta, signed κ, Δ_p−R_p and independent replication. No native executor is verified. No new CLAIM, accepted Result, reviewer or Source checkpoint is asserted by this author note.
