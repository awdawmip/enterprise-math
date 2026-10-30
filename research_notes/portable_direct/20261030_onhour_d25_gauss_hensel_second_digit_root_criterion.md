# D25 / SECOND-DIGIT-LIFT — Gauss–Hensel root and signed second-digit residual transport

2026-10-30, Asia/Hong_Kong. AUTHOR-SIDE / EXACT ALGEBRAIC EQUIVALENCE / EXECUTED FINITE CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING. Research-onhour logical lane: chatgpt-research-onhour-enterprise-math-20260923 (distinct from maintenance). Mother: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin **c47e13e4aba0e006366f989d6334d443f6333ae3**; P000/ACTIVE worldview unchanged. No assertion of Source session, CLAIM, Result admission or native H0/B0 execution.

## Exact original interface consumed

For each prime p=6m+1 with p≡13 or19 (mod24), use the original coefficients, weight and **frozen signed reflected** scalar R_p:

\[
a_n=\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n},
\quad A_p=\sum_{n=0}^{p-1}(6n+1)a_n,
\quad G_p(z)=\sum_{n=0}^{p-1}c_nz^n,
\quad c_n=\frac{(1/6)_n(1/3)_n}{(n!)^2}.
\]

Set z_0=1/2, M=G_p(z_0), g=G'_p(z_0), h=M/p. Existing accepted CM0/first-digit UR and the previously proved finite Clausen source alignment give M≡0 modp, g a p-unit, p² | Q, Q/p²≡R_p modp and the **exact finite identity**

\[
A_p=M(M+6g)-Q.
\]

Thus original LIFT is equivalent to

\[
6hg+p(h^2-R_p)\equiv1\pmod{p^2}. \tag{A}
\]

The antecedents and original definition of R are consumed at their existing proof strength, not rediscovered; the source-port alignment is the 2026-10-26 project note, commit 2d7bdfd7821d3afac8eaefb4b88bfedca8ff46be. This author's later CM proof is an author-side supporting derivation, not independent admission.

## New exact all-target-prime theorem (equivalence, NOT completed LIFT)

Hensel's lemma yields a **unique** zero ζ_p of the finite polynomial G_p over Z_p with ζ_p≡z_0 (modp): indeed modulo p, G_p(z) equals the finite polynomial P_m(z)=∑_(k≤m)binom(m,k)binom(2m,k)z^k and z_0 is a simple zero by the existing CM/Hasse antecedent. Let d_p=(z_0−ζ_p)/p and t_p=g^(−2), both p-local.

**Theorem.** For every stated target prime, with fractions interpreted as p-unit inverses,

\[
\boxed{A_p\equiv p\pmod{p^3}
\iff (6d_p+4pd_p^2)g^2\equiv 1+pR_p\pmod{p^2}.} \tag{B}
\]

Equivalently, the *necessary and sufficient unique second-displacement digit* is

\[
\boxed{d_p^*=\frac{t_p}{6}
+p\left(\frac{R_pt_p}{6}-\frac{t_p^2}{54}\right)\pmod{p^2},
\quad A_p\equiv p\pmod{p^3}\iff d_p=d_p^*\pmod{p^2}.} \tag{C}
\]

So a potentially independent p-adic CM/Gauss–Manin argument could prove the **explicit root-location prediction**

\[
\boxed{\zeta_p\equiv\frac12-\frac{pt_p}{6}
-p^2\left(\frac{R_pt_p}{6}-\frac{t_p^2}{54}\right)\pmod{p^3}.} \tag{D}
\]

### Proof

The Gauss finite polynomial satisfies the **exact endpoint differential equation** (a=1/6, b=1/3, N=p−1):

\[
[z(1-z)\partial_z^2+(1-\tfrac32 z)\partial_z-\tfrac1{18}]G_p(z)
=-(p-1+\tfrac16)(p-1+\tfrac13)c_{p-1}z^{p-1}. \tag{E}
\]

Each of (1/6)_(p-1) and (1/3)_(p-1) has a p-factor and (p−1)! is a p-unit. Thus p²|c_(p-1) in the p-local sense. At z_0=1/2, (E) gives

\[
G_p''(z_0)+g-\frac29G_p(z_0)\equiv0\pmod{p^2},
\quad\text{hence }G_p''(z_0)\equiv-g\pmod p. \tag{F}
\]

Taylor expansion of the **actual Hensel zero**, ζ_p=z_0−pd_p, yields

\[
0=G_p(\zeta_p)\equiv M-pd_pg
+\tfrac12p^2d_p^2G_p''(z_0)\pmod{p^3},
\]

so h≡d_pg−(p/2)d_p²G_p'' (modp²), h²≡d_p²g² (modp). Substituting into the old interface (A), and using (F),

\[
6hg+p(h^2-R_p)\equiv
g^2(6d_p+4pd_p^2)-pR_p\pmod{p^2}.
\]

This proves (B); the derivative of 6d+4pd² is 6+8pd, a p-unit. Solving first modulo p and then modulo p² gives the **unique** solution (C), hence (D).

**Stronger signed-residual transport corollary.** The already accepted first digit implies d_p−d_p*∈pZ_p. Linearizing the same polynomial at d_p* gives the precise residual, not just a zero test:

\[
\boxed{\Delta_p-R_p=\frac{A_p-p}{p^2}
\equiv6(g\bmod p)^2\,\frac{d_p-d_p^*}{p}\pmod p.} \tag{G}
\]

The multiplier 6g² is invertible modp: any nonzero source-observer residue corresponds to a nonzero error in the **second** Hensel root digit, with the same original sign/provenance. The explicit R_p term is essential: dropping R changes the target digit by p·R_pt_p/6.

## Executed exact finite certificates

The separately published Python-standard-library checker below computes c_n modulo p³, the finite polynomial and derivatives, Newton's unique root modulo p³, **original R_p by its frozen C_a double sum**, and independent original 216/2304 weighted recurrence sums modulo p³. It also compares full integer-binomial sums independently for 13, 19 and 373. All 60 primes 13≤p<1500 with p≡13,19 mod24 passed exact (E)–(G) and original A_p≡B_p≡p modp³. It performs a **labeled counterfactual negative control** R→R+1, observing the transported residual −1 modp without changing frozen R in the true source. This is finite exact verification, not proof of a universal LIFT claim.

| p | frozen R_p | g mod p² | actual ζ_p mod p³ | d_p mod p² | predicted d_p* |
|---:|---:|---:|---:|---:|---:|
| 13 | 0 | 1 | 449 | 50 | 50 |
| 19 | 12 | 344 | 4798 | 289 | 289 |
| 37 | 11 | 862 | 39313 | 991 | 991 |
| 43 | 15 | 1287 | 22941 | 391 | 391 |
| 211 | 119 | 35743 | 8649840 | 25787 | 25787 |
| 373 | 196 | 78545 | 18815053 | 19122 | 19122 |

For 373, h=65672 (mod139129) and R_373=196 (mod373): neither is silently replaced by zero. BRC resolution COMPOSE_APPLIED: carrier is source-indexed, signed p-local Gauss coefficients and frozen Q/R with valuation and Hensel derivative ports; authorized future observer is Δ−R at precision p³. The p-adic scalar root is an external arithmetic coordinate and has no native H0/B0 or X6 operator identity.

## Next scientific action and current bounded gate

**Unfinished proof:** establish (D) for both infinite target classes using a deformation-sensitive CM/Gauss–Manin comparison or original finite hypergeometric/WZ transformation preserving the actual signed R_p; (G) will then give original LIFT. Do not count this equivalent root criterion as the proof itself. The native highest frontier #1559 separately requires fixed p373 **same-original-class H0/B0 divided-power** [X]U mod139129, rank, genuine semilinear Frobenius/eta, signed odd Green/Hesse, κ, and independent replication. No portable scalar computation satisfies that benchmark.

During this run Site reported research_authority_granted=false, executor_binding_configured=false and em_checkpoint_list ACCESS_DENIED; ordinary-chat recovery_status is listed in status but has no exposed direct method on this client. No self-owned Source session/claim/run/target_request_id was recovered, and another lane's identity was not used. If a prior request exists, reconcile its original ID after legitimate access, rather than duplicating writes. Leave the scheduled lane enabled, Source pin unchanged, and this artifact as AUTHOR-SIDE / NOT_ADMITTED.

Prior project evidence: research_notes/portable_direct/20261026_onhour_d25_native_lift_source_port_identity.md (2d7bdfd); research_notes/portable_direct/20261030_onhour_d25_A216_CM_Deuring_Hasse_uniform_zero.md (5da4867); research_notes/portable_direct/20261030_onhour_d25_A216_B2304_fourth_digit_restoration_and_fifth_digit_obstruction.md (6e8b41e); GitHub Issue #1559.
