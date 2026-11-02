# D25: uniform Gauss first carry proved; direct second carry

2026-11-03 (+08:00). AUTHOR-DERIVED / DEPENDENCY-PROVED / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. TASK_RESEARCH lane chatgpt-research-onhour-enterprise-math-20260923, not the separate hourly research or maintenance lane. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; immutable publication TP2-B6F4FC938FF94941C1B7; frozen science c47e13e4aba0e006366f989d6334d443f6333ae3.

## Theorem A: previously OPEN 12jh=1, now proved from inherited all-prime inputs

For p=6r+1 with p mod24 in {13,19}, z0=1/2, let G(z)=sum_{k=0}^{p-1}(1/6)_k(1/3)_k z^k/(k!)², F(z)=sum_{k=0}^{p-1}(1/2)_k(1/3)_k(2/3)_k z^k/(k!)³, W=[(1+6theta)F](z0), and ell(z)=sum_{k=0}^r binom(r,k)binom(2r,k)z^k, theta=z d/dz. This G is the **Gauss polynomial**, NOT the differently typed G_p in the frozen mother scalar.

Consume the previously accepted D24 first-digit W=p mod p², CM0 ell(z0)=0 mod p, G=ell mod p, and the previously proved finite Clausen theorem F=[G²]_{degree<p} with high-degree coefficients of G² divisible by p² (see 20261103_r11_d25_clausen_defect_low_high_prefix.md). Let A=G(z0)/p in Z_(p), D=G'(z0), h=A mod p, and j=(theta ell)(z0) mod p. Thus D=2j mod p.

The exact signed source congruence, retaining the finite Clausen high-index defect E, is

    W = G(z0)² + 6 G(z0)D + p² E (mod p³).                 (1)

Reduce (1) mod p², and substitute W=p mod p² and G(z0)=pA. Divide by p:

    6 h (D mod p) = 12 j h = 1 (mod p).                    (2)

Hence h,j,D mod p are units for **every target prime**, not merely the finite tests. Equation (2) DISCHARGES the OPEN first-carry condition and the equivalent H2-test in 20261103_r11_d25_gauss_hensel_root_second_carry.md and 20261103_hourly20_d25_gauss_edge_unit_one_tenth.md. The accepted first digit is a genuine logical input, not a new proof of D24.

The unique p² Gauss root beta reducing to 1/2 consequently satisfies by Hensel/Taylor

    beta = 1/2 - p h/(D mod p) = 1/2 - 6p h² (mod p²),       (3)

which equals 1/2-p/(24j²). Thus G(1/2-p/(24j²))=0 mod p² is proved for the target classes.

## Theorem B: direct one-quotient second-carry certificate

Divide (1) by p while retaining terms mod p²:

    W/p = 6 A D + p (A²+E) (mod p²).                       (4)

By (2), 6AD=1 mod p. Therefore the well-defined signed residual is

    (W-p)/p² = (6AD-1)/p + h² + E (mod p).                  (5)

Use the previously proved two-prefix source defect E=-S/5, with S=sum_{k=1}^r L_k 2^{-k}[(6k-5)Lambda_k-6Gamma_k] in F_p, as defined and independently sourced in 20261103_hourly20_d25_gauss_edge_unit_one_tenth.md. The full original-216 p³ target W=p is **exactly equivalent**, given the inherited first digit, to

    (6AD-1)/p + h² - S/5 = 0 (mod p).                      (OPEN)

This is a lower-complexity exact equivalent certificate on the W-side: unlike the inherited H3 second-Hensel formula, no root second digit epsilon is required. A=G(1/2)/p mod p², D=G'(1/2) mod p², and S mod p retain integer lifts, derivative, original coefficient band, valuation p² and signed source. The OPEN uniform second-carry cancellation remains the next true scientific obligation. Translation to the frozen Delta_p-R_p mother retains the previous exact original-W bridge; this author note does not establish new task admission.

## Independently executed exact arithmetic

The companion standard-library program calculates the original finite 216 series, Gauss value/derivative, and the signed two-prefix defect from distinct recurrences modulo p³, then checks (2),(3),(5). All eight samples p=13,19,37,43,181,373,1171,3019 PASS (finite regression only). At p=373: A=65672 mod139129, D=78545 mod139129, h=24, j=294, beta=32638 mod139129, E=177. The three-source residue is ((6AD-1)/373)=366, h²=203, E=177 modulo373, and 366+203+177=746=2·373. The original W(372)=373 mod373³. The finite computation does not prove OPEN.

## Durable frontier and rights

MOTHER: Delta_p-R_p=0 mod p for both target classes. PROVED/DON'T REPEAT: accepted D24 first digit and inherited Clausen/H3/H4/U1-U3; now (2),(3),(5). REMAINS: uniform signed cancellation (OPEN) and exact frozen scalar mapping when required by final admission; native original p=373 H0/B0 [X]U mod139129, rank, semilinear Frobenius, signed Green/Hesse/kappa and independent replay are NOT EXECUTED, existing support issue #1559 has no confirmed assignee. Control support #1558 remains distinct.

Read-only own onhour recovery Issue awdawmip/kimi-query-bridge#6632 was SUCCEEDED with no own run/claim and historical neutral staging; original request research-onhour-20261031-0205-dispatch-r15 at #6633 was definitive FAILED UPSTREAM_CODE_REVIEW_REQUIRED. No retry, no new session/CLAIM/OPEN/native Source checkpoint/Result/review, no staging merger, no maintenance identity. This is **author-side GitHub evidence**, not role-bound Source progress. Next action: seek a finite CM/WZ/contiguous relation cancelling the exact three-source (OPEN), with p=13,19,373 regression, while support #1559 pursues real native computation. BRC/Enterprise coordinates are used as p-adic ordered-index/valuation/source/observer preservation; no native X6 transfer is asserted.
