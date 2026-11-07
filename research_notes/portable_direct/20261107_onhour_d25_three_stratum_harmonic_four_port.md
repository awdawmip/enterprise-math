# D25 — Three-stratum harmonic lift and four-port finite-cutoff certificate

2026-11-07 · Author-side TASK_RESEARCH; exact algebraic coefficient theorem, finite exact regression, **UNREVIEWED / NOT_ADMITTED**. Research lane: chatgpt-research-onhour-enterprise-math-20260923 (maintenance lane excluded). Mother task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Consumes the published p³ projected Clausen–Euler theorem and normalized factorial tail (commit 50346cde208fb05673de7e7ed367f4998f200a1b). Scientific inputs have not been repinned.

## Theorem 1 — A general three-stratum p³ formula

Let p>3 be prime, 0<=u<v<p, c1,c2 belong to Z_(p), and set a=-u+c1*p, b=-v+c2*p and g_n=(a)_n(b)_n/(n!)² for 0<=n<p. Write H_j^(r)=sum_{i=1}^j i^{-r}, H_0^(r)=0. Define three degree <p polynomials F0, F1, F2 by their coefficients as follows.

For 0<=n<=u, put B_n=binom(u,n)binom(v,n),
L_n=c1(H_u-H_{u-n})+c2(H_v-H_{v-n}),
T_n=c1²(H_u^(2)-H_{u-n}^(2))+c2²(H_v^(2)-H_{v-n}^(2)), and set
[z^n](F0,F1,F2)=(B_n,-B_n*L_n,B_n*(L_n²-T_n)/2).

For u<n<=v, put
R_n=(-1)^(u+n)*c1*u!*(n-u-1)!*v!/((v-n)!*(n!)²),
S_n=c1*(H_{n-u-1}-H_u)-c2*(H_v-H_{v-n}),
and set [z^n](F0,F1,F2)=(0,R_n,R_n*S_n).

For v<n<p, put
J_n=(-1)^(u+v)*c1*c2*u!*v!*(n-u-1)!*(n-v-1)!/(n!)²
and set [z^n](F0,F1,F2)=(0,0,J_n).

Then coefficientwise over Z_(p)[z]/(p³,z^p),

    sum_{n=0}^{p-1} g_n z^n = F0(z)+p*F1(z)+p²*F2(z).       (1)

The three valuation strata are generically 0,1,2 when c1,c2 are p-units. Without that hypothesis these are only lower bounds.

**Proof.** For n<=u, factor each numerator term j-u+c1*p or j-v+c2*p by its unit -u+j or -v+j. The remaining product consists of (1-p*c1/(u-j)) and (1-p*c2/(v-j)). Its first two elementary symmetric sums are -L_n and (L_n²-T_n)/2. For u<n<=v, remove the one factor c1*p at j=u. The constant product of the surviving factors is R_n/c1 and its first relative correction equals S_n; this yields p*R_n*(1+p*S_n). For n>v remove both factors c1*p and c2*p; the surviving constant product equals J_n/(c1*c2) and its p-adic correction is irrelevant modulo p³. All denominators n! are p-units. QED.

## Corollary 2 — Exact source-preserving four-port weighted identity

For the 216 Gauss series, take (u,v,c1,c2)=(m,2m,1/6,1/3), p=6m+1. For the 2304 Gauss series, take (u,v,c1,c2)=(k,3k+1,1/8,3/8) for p=8k+3 or 8k+5. The latter two classes have the same three-stratum coefficients but distinct Euler multiplier C_B=1 or 1-z, respectively.

Let Pi_p retain degrees <p and D=z*d/dz. Define O_A(f)=[(1+6D)Pi_p(f)](1/2) and O_B(f)=[(1+8D)Pi_p(C_B*f)](1/9). The exact Clausen and Euler identities plus (1) give, for either respective original weighted sum modulo p³,

    Weighted(p) = T0 + p*T1 + p²*(T11+T02),             (2)
    T0=O(F0²),  T1=O(2F0F1),  T11=O(F1²),  T02=O(2F0F2).

The four ports preserve the zeroth source, first-order source, first-order self-composition, and zeroth/second-order cross-composition. In particular T02 includes low/mid harmonic corrections as well as the high-index factorial tail: it is NOT only a tail statistic. The original 216 and 2304 index/valuation/Euler/cutoff/signed-difference observers are kept separate. BRC tool resolution: COMPOSE_APPLIED, actual typed signed source ports and arithmetic, not a positive-mass cancellation claim.

For p=373 the exact certificate (T0 mod p³, T1 mod p², T11 mod p, T02 mod p) is:

    216:  (25720961, 64951, 198, 189)
    2304: (16706670, 63754, 188, 267)

The signed difference of all four ports is the literal integer equality

    9014291 + 373*1197 + 373²*(10-78) = 0.             (3)

This independently recovers W_373=V_373=373 modulo 373³. The prior two-component split ((G_A-G_B)/p², E_A-E_B)=(219,154) is now refined by explicitly separating first-order self-composition and the full second-order cross-port. This numerical certificate is not a universal proof or the separately required native H0/B0 experiment.

## Executed checks, sources and open frontier

The companion standalone standard-library script d25_three_stratum_harmonic_four_port_check_20261107.py checks **every coefficient** of both Gauss series modulo p³ against independent original recurrences for 37 primes p<=401 in the 216 class and 41 primes p<=401 in the 2304 classes. It also reconstructs all original integer-binomial weighted sums via exact finite convolution and validates the four-ports at p=13,19,43,67,373, retaining the Euler factor for p=8k+5. All executed checks PASS; no floating-point approximations were used.

Smallest open scientific unit: a symbolic finite-field Cartier/telescoping identity for the *signed four-port* difference simultaneously for p≡13 and 19 (mod24). The five specified primes discriminate the two Euler branches and nontrivial cancellation. Continue from (2) and the prior Fricke-Hasse frontier; do not repeat the p² or p³ fold or the factorial-tail proof.

Native original-class H0/B0 [X]U modulo 139129, semilinear Frobenius/eta, odd Hesse/Green κ and independent replication remain pending at https://github.com/awdawmip/enterprise-math/issues/1559, with no assignee as of this run. On 2026-11-07 around 13:29 UTC, em_status and original-request em_control_reconcile both returned BACKEND_IDENTITY_OR_VERSION_MISMATCH with fixed subreason UPSTREAM_STATUS_TOOL_ERROR, underlying STATUS_DATABASE_UNAVAILABLE and operation_sent=false. Site phase CONFIGURED_NOT_LIVE_VERIFIED, research_authority_granted=false. Original request onhour11-20261106-1400-exact-research-lane-continuation is retained, not replayed; previous receipt was QUEUED / EVENT_COLLECTION_IO / Error. No valid Source session/CLAIM/run/checkpoint/Result/admission is asserted.

This note is durable author-side scientific evidence only: AUTHOR_SIDE_PROVED / FINITE_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED.
