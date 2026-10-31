# D25/LIFT — first-digit fixed-216 normalization sensitivity

2026-10-31; second portable, author-derived TASK_RESEARCH unit. Logical Research lane chatgpt-research-hourly-enterprise-math-20260923 (never the control maintenance lane). Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source c47e13e4aba0e006366f989d6334d443f6333ae3. P000 ACTIVE_LOCKED and all ACTIVE worldview records unchanged.

Status AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This is a conditional external p-adic/finite-field result, NOT an admitted native Enterprise X6 theorem.

## Original question and explicitly inherited hypothesis

The immediately preceding third-digit endpoint/mirror result shows that the Fermat quotient Q_p(216) contributes to a high-index normalized tail. Can the fixed original denominator 216 be freely shifted to 216(1+pt) without changing the first p-adic digit of the complete weighted sum? If not, which original valuation layer first detects the normalization change?

Let p=6\ell+1 be prime, \ell>=1, and

\[
 a_n=\binom{2n}{n}^2\binom{3n}{n}/216^n,\qquad
 F_p(X)=\sum_{n=0}^{p-1} a_n X^n,\qquad
 A_p(X)=\left(1+6X\frac{d}{dX}\right)F_p(X).
\]

Define
\[
 G_\ell(z)=\sum_{k=0}^{\ell}\binom{\ell}{k}\binom{2\ell}{k}z^k,\qquad z_0=1/2.
\]

Assume the **CM root**
\[
 G_\ell(1/2)\equiv0\pmod p. \tag{CM}
\]
This specific input is consumed from the existing D25 CM-root/Clausen line, including research_notes/portable_direct/20261031_hourly_d25_clausen_denominator_two_jet.md, not newly proved or independently accepted here. The theorem below is therefore conditional on (CM). All rational denominators used below are p-local units.

## Theorem — sharp original weighted observer response

For any t in the p-local integers set X_t=(1+pt)^{-1}. Then
\[
 \boxed{A_p(X_t)-A_p(1)\equiv -3pt\,G_\ell'(1/2)^2\pmod{p^2}.}
 \tag{1}
\]
If (CM) holds then G_\ell'(1/2) is NONZERO modulo p. Consequently, if t is a p-adic unit, the original weighted difference has exact p-adic valuation 1:
\[
 \boxed{v_p(A_p(X_t)-A_p(1))=1.} \tag{2}
\]
Moreover, the first derivative is carried entirely by the lowest valuation band:
\[
 \boxed{
 \sum_{n=0}^{2\ell} n(6n+1)a_n\equiv3G_\ell'(1/2)^2\pmod p.
 }
 \tag{3}
\]
These claims do not justify discarding higher valuation bands at the frozen target modulus p^3.

### Proof A: finite Clausen polynomial reduction and derivative

The classical Clausen identity as applied to the original truncated coefficients by the predecessor gives the coefficientwise identity
\[
 F_p(X)\equiv G_\ell(X/2)^2\pmod p. \tag{4}
\]
The parameters 1/6 and 1/3 reduce to -\ell and -2\ell modulo p, respectively; the finite Gauss series terminates before p-denominator problems. Since the original coefficient valuation is positive after n=2\ell, (4) holds at the full original degree p-1. This is an application of a known identity, not a claim of inventing the classical Clausen transformation.

Write z=X/2. Apply the **original weighted differential observer** before specializing the parameter:
\[
 A_p(X)\equiv G_\ell(z)^2+12z G_\ell(z)G_\ell'(z)\pmod p.
\]
Differentiating with respect to X, using dz/dX=1/2, and evaluating z=1/2 under (CM) gives
\[
 A_p'(1)\equiv \tfrac12[14GG'+12z((G')^2+GG'')]_{z=1/2}
 =3 G_\ell'(1/2)^2\pmod p. \tag{5}
\]
Because X_t=1-pt (mod p^2), exact polynomial Taylor expansion about X=1 gives (1).

### Proof B: the CM root is necessarily simple

As a terminating hypergeometric polynomial G_\ell={}_2F_1(-\ell,-2\ell;1;z), it satisfies
\[
 z(1-z)G_\ell''+[1+(3\ell-1)z]G_\ell'-2\ell^2 G_\ell=0
\tag{6}
\]
over F_p. The point z_0=1/2 is ordinary, with z_0(1-z_0)=1/4 invertible. Were both G_\ell(z_0) and G_\ell'(z_0) zero, expanding at z_0 in powers of (z-z_0) and comparing coefficients successively would force each coefficient up to degree \ell to vanish: the leading multiplier at derivative order j is j(j-1)/4 and is invertible for 2<=j<=\ell<p. This contradicts G_\ell(0)=1. Hence (CM) implies G_\ell'(z_0) ≠0 modp. If t is a p-unit, (1) has nonzero coefficient at p and therefore implies (2). No finite scan is used for this simplicity proof.

### Proof C: identify the exact valuation band

For 0<=n<p, Legendre's factorial formula gives
\[
 v_p(a_n)=\left\lfloor\frac{2n}{p}\right\rfloor+
          \left\lfloor\frac{3n}{p}\right\rfloor.
\]
For p=6\ell+1 this valuation is zero precisely at 0<=n<=2\ell; after that it is >=1. Consequently
\[
 A_p'(1)=\sum_{n=0}^{p-1}n(6n+1)a_n
 \equiv\sum_{n=0}^{2\ell}n(6n+1)a_n\pmod p.
\]
Combine this with (5) to obtain (3), completing the proof.

## Exact independent check against ORIGINAL 216 coefficients

The actually executed self-contained standard-library program at research_notes/portable_direct/d25_cm_normalization_sensitivity_20261031.py has SHA256 c2d9a44c5df4e26a6ed7935550e73dcf4edb5663ec365ba9f2eb8aa0f20dd2af, Git blob 7ec1386eb585c603cf49632b0470229e208d9635. It computes (G,G') from integer binomials; it computes original a_n separately from the exact recurrence modulo p^2; and it evaluates the full original weighted polynomial A_p(X_t), not the RHS polynomial, for t=-2,-1,0,1,2.

Observed all 166 target-class primes p<=5000 with p mod24∈{13,19}, 830 exact finite-difference checks, all PASS. Marker PASS_D25_CM_FIXED_NORMALIZATION_FIRST_DIGIT_SENSITIVITY_EXACT; actual execution-log SHA256 d441381807fc04f4efc41468a621292fa2f29b0560fd40db3ad498843be8123d. Anchors (p,G'(1/2) modp,A_p(1) modp^2,(A_p(X_1)-A_p(1))/p modp):
(13,1,13,10), (19,2,19,7), (37,11,37,7), (157,118,157,147), (373,215,373,81).

These finite tests confirm the implementation and tested CM inputs, but do not prove (CM) for the infinite prime class; the mathematical derivation of (1)-(3) explicitly depends on (CM).

## Observer, consequences, and next unit

BRC COMPOSE_APPLIED: carrier includes p, original n and signed weight 6n+1, fixed normalization 216, valuation band, base observer A_p(1), perturbation t and derivative. Normalization sensitivity proves that collapsing fixed-normalization and variable-normalization ports is mathematically unsound: a unit-sized p-adic change in normalization changes the *complete* weighted sum at valuation exactly 1. The first variation is low-band, unlike the high-order endpoint of the preceding reciprocal mirror. This external finite-field result does not establish a native P000 X6 correspondence.

The frozen objective remains, for p mod24 in {13,19},
\[
 A_p(1)\stackrel{?}{\equiv}p\pmod{p^3},
\]
equivalently the existing scoped complete second-digit four-port obstruction C+L-J+I=0 (modp). This paper supplies a sharp obstruction to treating Q_p(216) as a freely movable normalization gauge, but NOT a proof of that remaining cancellation. Next exact science unit: derive a finite WZ/CM bridge for the original *fixed* denominator 216, preserving the lowest-band 3G'(1/2)^2 response, middle/high signed valuation walls and endpoint Fermat quotient; seek a genuine joint cancellation identity. Do not rerun finite scans as a substitute for proof.

Native gateway observation on 2026-10-31: 0.6.11, research_authority_granted=false, executor_binding_configured=false, quota 5/5, CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED. Historical original research-lane recovery and continuation receipts from kimi-query-bridge #6424/#6425 do not authorize a current run. Control support enterprise-math #1558 and native 373 experiment #1559 unchanged. No new CLAIM, OPEN, native Source checkpoint, Result, review, P000/worldview modification, session/staging transition, maintenance identity use or scheduler action.
