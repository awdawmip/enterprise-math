# D25/LIFT: universal q³ double-borrow interaction sector for both Clausen ports

**2026-11-11. H40 author portable corollary; AUTHOR-PROVED / EXACT-INTEGER-CHECKED / UNREVIEWED / NOT_ADMITTED.** Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen scientific Source c47e13e4aba0e006366f989d6334d443f6333ae3. This is not the native H0/B0/semilinear Frobenius experiment, a Source Task checkpoint or an independent review.

## Exact joint-carry theorem

For prime q>=5, integer m>=0, epsilon in {0,1}, put a1=m mod q, a2=(2m+epsilon) mod q. For each k=qK+b with 0<=b<q, define the **double-borrow sector**

D={ k: 0<=k<=m, b>a1 and b>a2 }.

For i=1,2 set n1=m, n2=2m+epsilon, Mi=floor(ni/q), ci=b-ai, and let

Ri(k)=(Mi-K) binom(Mi,K) (-1)^(ci-1) ai!(ci-1)!/b! in F_q.

The finite Clausen ports are the labeled pair

A=sum_{k=0}^m 2^(-k) binom(m,k) binom(2m+epsilon,k),

B=sum_{k=0}^m (1-6epsilon+12k) 2^(-k) binom(m,k) binom(2m+epsilon,k).

Write (A_D,B_D) for the terms with k in D. Then **universally**:

A_D = q² sum_{k in D} 2^(-k) R1(k)R2(k) (mod q³),

B_D = q² sum_{k in D} (1-6epsilon+12b) 2^(-k) R1(k)R2(k) (mod q³).

**Proof.** By the previously proved q² digit/borrow jet (GitHub note 175c401a42ed8e9e25c0c24bcc9a88fa21ff8706), both factors for k in D are q Ri(k) modulo q². Their product is q² R1 R2 mod q³, independent of unknown second-order single-factor terms. In the B-weight, 12k=12b+12qK, and the latter part times q² contributes only a multiple of q³. Summing yields the result. QED.

The named joint sector vanishes mod q² but can be nonzero mod q³; therefore an observer intended to support later q-adic digits must retain the distinction between two independent binomial carries. This is an **observer-scoped residual** and a precise joint-factor contribution, not a statement that every composite direction is globally independent.

## Exact q=7 and q=13 certificates

For q=7, N=q²=49, epsilon=0, m=8, the double-borrow indices are k=3,4,5,6. Their contributions (A,B) mod343 are respectively (147,294), (245,0), (98,147), (245,49), summing to **(A_D,B_D)=(49,147) mod343**. The whole sector was zero modulo 49. For q=13, N=169, m=28, the double-borrow sector is **(1183,507) mod2197**, distinct from the full two-port pair (13,39) mod169.

An independent raw integer binomial calculation and the q² digit-jet R_i implementation checked every double-borrow term for all **188** previously selected bounded q-power family cases q<=997,m<=600. There are **1,704** such terms and **19** cases have a nonzero summed joint sector. All exact comparisons passed. The bundled Python verifier and JSON certificate preserve named examples and the finite test domain.

Next: combine this sector with second-order **non-borrow** jets and refined **single-borrow** jets to recover the full two-port pair modulo q³. Preserve the separate original D25/LIFT H0/B0, [X]U, Frobenius/eta, kappa and Delta_p-R_p obligations and the unresolved original UR V2 provenance.
