# D25 — Weighted Picard–Fuchs CM jet forcing (2026-11-02)

**Status: AUTHOR-DERIVED / EXACT ALGEBRAIC PROOF / 11 FINITE EXACT TESTS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_EXPERIMENT.** Neutral source evidence only; NOT a Source checkpoint, role/session, CLAIM, run, Result or formal review.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research lane reference chatgpt-research-onhour-enterprise-math-20260923 remains distinct from the maintenance lane.

## 1. Exact weighted-operator commutator

For a prime p>3, in p-local rationals, put theta=z*d/dz and

a_k=(1/2)_k(1/3)_k(2/3)_k/(k!)^3
    = binom(2k,k)^2 binom(3k,k)/108^k,

F_p(z)=SUM(k=0..p-1) a_k z^k,  Y_p(z)=(1+6 theta)F_p(z).

At z=1/2, Y_p is exactly the original weighted-216 W_p (no source or weight modification). Define

P_A(theta)=(theta+1/2)(theta+1/3)(theta+2/3)
          =theta^3+(3/2)theta^2+(13/18)theta+1/9,

L_A=theta^3-z P_A(theta).

The coefficient recurrence gives the exact finite polynomial identity L_A F_p=-p^3 a_p z^p. Since [L_A,theta]=z P_A(theta), the new **exact all-p identity** is

**L_A Y_p = 6z P_A(theta) F_p - (1+6p)p^3 a_p z^p.** (1)

Thus the full-period *unweighted* homogeneous PF equation mod p^3 does not imply that the original *weighted* Y_p itself obeys that scalar homogeneous equation.

## 2. Exact all-target CM jet and nonzero weighted forcing

Now p=6m+1, p mod24 in {13,19}. Let ell_m(z)=SUM(k=0..m) binom(m,k)binom(2m,k)z^k. **Consumed accepted predecessor** (not newly proved here): CM0 ell_m(1/2)=0 modp, from research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md (CM0/SIMPLE).

In F_p[z], the finite Clausen identity is

**F_p(z) = ell_m(z)^2 (mod p), coefficient by coefficient.** (2)

Explanation: for every k<p the factorial denominators are p-units, parameters 1/6 and 1/3 reduce to -m and -2m, and the terminating 2F1 polynomial ell_m has degree m; its square has degree 2m<p, and the formal Clausen identity identifies every coefficient below p. This is not a limit or an unsafe truncation exchange.

Write z0=1/2, u=ell_m'(z0). The terminating hypergeometric polynomial solves

z(1-z)ell''+[1+(3m-1)z]ell'-2m^2 ell=0.

At z0 the leading coefficient is a unit. If ell and ell' both vanished, repeated differentiation would force all Taylor coefficients through degree m<p to vanish, contradicting ell(0)=1. Therefore u!=0 modp from CM0. The double root F_p=ell_m^2 yields

F_p(z0)=theta F_p(z0)=0;
theta^2 F_p(z0)=u^2/2 !=0 (mod p). (3)

As L_A F_p=0 modp, theta^3F_p(z0)=(3/2)theta^2F_p(z0)=3u^2/4. Substituting into (1) proves for **every target prime**

**Y_p(z0)=0,  theta Y_p(z0)=3u^2 !=0,  L_A Y_p(z0)=(9/2)u^2 !=0 (mod p).** (4)

Hence Y_p has a simple zero at the CM point (ordinary derivative Y_p'(z0)=6u^2 !=0), while unweighted F_p has a double zero. The weighted original model has strictly nonzero scalar PF forcing already mod p.

This is a scoped obstruction to an **unmodified scalar-PF transfer**. It does not obstruct derivative-coupled 3-state transport or the D25 original supercongruence.

## 3. Exact provenance-preserving 3-jet connection

With X=(F_p,theta F_p,theta^2F_p)^T, over p-local rational functions away from z=1,

theta X = A(z)X - p^3 a_p z^p/(1-z) * (0,0,1)^T,

A(z)=[[0,1,0],
      [0,0,1],
      [z/(9(1-z)),13z/(18(1-z)),3z/(2(1-z))]].

Original weighted readout Y_p=(1,6,0)X. The 3-state system is homogeneous modulo p^3 at z=1/2; its scalar weighted readout is not itself a solution of the original scalar homogeneous PF equation. This **separates full-period endpoint defect from derivative-coupling source**, and retains information the original weighted observer needs. The jet is a classical auxiliary algebraic representation, NOT a native H0/B0/X6 operator.

## 4. Independent original 2304 fixed-prime discriminator

Set b_k=(1/4)_k(1/2)_k(3/4)_k/(k!)^3, H_p(z)=sum(k<p)b_k z^k,
Z_p=(1+8theta)H_p, L_B=theta^3-z(theta+1/4)(theta+1/2)(theta+3/4).

All p>3 satisfy the analogous exact commutator:
L_B Z_p=8z(theta+1/4)(theta+1/2)(theta+3/4)H_p-(1+8p)p^3 b_p z^p.

**Fixed p=373 direct exact original-coefficient witness (all mod 373):**

- At z=1/2, 216 theta-moments 0,1,2,3: **0,0,173,73**; ell_m'(1/2)=**215**; weighted first jet **292**; weighted scalar PF forcing **65**.
- At z=1/9, 2304 theta-moments 0,1,2,3: **0,0,336,63**; weighted scalar PF forcing **131**.

Even when the original weighted values agree at this point, their separately typed scalar PF residuals differ: 65!=131 (mod373). This is a fixed-prime exact counterexample to the method claim that equality of values automatically transports scalar PF operator residuals; it is NOT a counterexample to D25. In the finite check, these two PF forcing values actually coincide at p=67; no all-prime inequality is claimed.

## 5. Executed exact finite tests, mathematics scope

The author executed Python standard-library integer checker d25_weighted_pf_cm_jet_forcing_20261102.py on the target primes
13,19,37,43,61,67,109,139,211,373,1171.

All **11/11** cases passed two independent coefficient constructions (4486 integer mod-p direct-binomial/recurrence comparisons), full finite Clausen coefficient comparison (2243 checked coefficients), CM root/slope, theta jets, nonzero 216 forcing and both weighted commutator evaluations. No floating point or p-divisible modular inverses. Exact tabulated results and full checker were generated as author-side files in the same run; this note contains the complete theorem and dependency proof. Computational checks do not substitute for the all-prime algebra.

## 6. Next exact work and remaining native experiment

Mother task **OPEN**: Delta_p-R_p=0 modp for p≡13,19 mod24, equivalently original W_p=p modp^3 under accepted first digit and signed cutoff R=Q/p². Next discriminating mathematical unit: construct a **legitimate source-typed finite 3x3 weighted/jet 216-to-2304 transfer through p²** at z=1/2,1/9, with normalization, twist and derivative ordering; test its first nontrivial 373 row and original signed cutoff before claiming the original mod p³ equality. Alternate valid direct LIFT proofs remain open.

Existing original p=373 same-class native H0/B0 divided-power [X]U mod139129, module rank, true semilinear Frobenius/eta, odd signed Hesse/Green, kappa and independent replica remain **PENDING_OWNER / NOT_EXECUTED**, under existing support awdawmip/enterprise-math#1559 (not replaced by auxiliary jets). No new Task/CLAIM/native completion asserted.

Old Research dispatch research-onhour-20261031-0205-dispatch-r15 had final FAILED / UPSTREAM_CODE_REVIEW_REQUIRED receipt at awdawmip/kimi-query-bridge#6633. No duplicate write/control request; native recovery_status and own session/claim/run not authenticated this turn. The note is neutral GitHub evidence, REGISTER_PENDING / SYNC_DEBT for formal activity/Source checkpoint, NOT_ADMITTED for scientific review. Frozen scientific pin, P000 and schedule/notification configuration unchanged.
