# D25/LIFT GH-7 and GH-8 — exact rational-Gosper obstruction and prime-cutoff boundary regularization

2026-10-28 Asia/Hong_Kong. Research logical lane: `chatgpt-research-hourly-enterprise-math-20260923`. Parent: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, D25/LIFT/JT2 remains OPEN. Frozen scientific Source pin: `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged).

**Evidence class:** AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. The two claims below are algebraic statements about auxiliary rational hypergeometric ranks, not new P000, native X6 operations, a native p=373 experiment, or a proof of the original W/S supercongruence. Inputs consumed, not recredited: GH-3/GH-4 (`29387582d6ea0be2c0f18ea1de49226cd5938090`), GH-5/GH-6 (`c0554de023ae6fea2b57fdaa0ffac7108013aa6b`). The single-sum vanishing conjecture remains unresolved.

## Exact carrier and declared observer

Put
\[
C_r=9^r\frac{(1/4)_r^3}{(1/2)_r(3/4)_r r!},\quad C_0=1,\quad
q(r)=\frac{C_{r+1}}{C_r}=\frac{A(r)}{B(r)},
\]
where \(A(r)=9(4r+1)^3\) and \(B(r)=4(4r+2)(4r+3)(r+1)\). For primes \(p\equiv19\pmod{24}\), \(d=(p-3)/4\), GH-3's exact residual question is \(T_p=\sum_{r=0}^{d}(8r+1)C_r\equiv0\pmod p\). Keep the original labelled MM/LH ports and finite cutoff: this scalar is only their stated auxiliary observer, not a permission to erase the original labelled pair or the next-digit GH-5 coordinates.

## GH-7. No prime-independent rational single-term Gosper antidifference

**Theorem GH7.1.** There is **no** rational function \(R(x)\in\mathbf Q(x)\) such that for all nonnegative ranks
\[
(8r+1)C_r=R(r+1)C_{r+1}-R(r)C_r.
\]
Equivalently \(A(x)R(x+1)-B(x)R(x)=B(x)(8x+1)\) has no rational solution. This does not exclude prime-dependent certificates, more elaborate WZ pairs, finite boundary terms, or multi-rank source transport.

**Proof.** Assume a rational solution. Partition its finitely many poles into integer-translation orbits. At the pole with smallest real part in any occupied orbit, say \(z_-\), the equation evaluated at \(x=z_--1\) forces \(A(z_--1)=0\) (otherwise the \(R(x+1)\) pole cannot cancel). Thus \(z_-=3/4\). At the pole with largest real part in the same orbit, \(z_+\), the equation at \(x=z_+\) forces \(B(z_+)=0\), hence \(z_+\in\{-1/2,-3/4,-1\}\). None of these differs from \(3/4\) by an integer, a contradiction. Therefore \(R\) is a polynomial. If its degree is \(n\), leading terms on the left are \(512\,\operatorname{lc}(R)x^{n+3}\); the right has degree 4, so \(n=1\). Setting \(R=ax+b\), coefficient comparison gives first \(a=1\), then \(b=11/16\), but the remaining coefficient of \(x^2\) in left minus right equals \(-342\ne0\). No solution exists. QED.

**Operational implication:** a characteristic-zero, rank-local rational Gosper antiderivative cannot be used as the missing proof of GH-3's vanishing. It is not legitimate to assume a universal exact boundary-free telescope exists, nor to infer that all more general telescopes fail.

## GH-8. Sharp cutoff valuation and two regularized Green-style ports

**Theorem GH8.1 (sharp endpoint cost).** Let \(p=4d+3>3\) be prime. The inputs \(C_0,\ldots,C_d\) are \(p\)-adic units, while
\[
v_p(C_{d+1})=-1,\quad B(d)=p(p^2-1),\quad
\frac{pC_{d+1}}{C_d}=\frac{9(p-2)^3}{p^2-1}\equiv72\pmod p.
\]
For a fixed nonzero rational polynomial \(R(x)=(x-1/4)^eU(x)\) with \(U(1/4)\ne0\), outside the finite set of primes dividing the rational numerator/denominator of \(U(1/4)\) and the coefficients used, the upper boundary has
\[
v_p\bigl(R(d+1)C_{d+1}\bigr)=e-1.
\]
Thus a naive nonvanishing gauge carries a pole, a simple zero at \(1/4\) makes the boundary integral but generally nonzero, and a double zero makes it vanish modulo \(p\).

**Proof.** In \(0\le r\le d\), none of the numerator or denominator Pochhammer factors is divisible by \(p\); at step \(d\to d+1\) exactly the denominator factor \((4d+3)/4=p/4\) contributes one \(p\). Substitution in \(q(d)\) gives the displayed identity. Since \(d+1=(p+1)/4\), \(R(d+1)=(p/4)^eU((p+1)/4)\) and \(U((p+1)/4)\equiv U(1/4)\not\equiv0\pmod p\) outside the declared exceptional primes. QED.

**Theorem GH8.2 (exact regularizing decomposition).** For every nonnegative integer \(r\), define
\[
R_1(r)=r-\tfrac14,\qquad
\rho_1(r)=\frac{3(160r^2+84r+5)}{32(r+1)(2r+1)},
\]
\[
R_2(r)=(r-\tfrac14)^2,\qquad
\rho_2(r)=\frac{-2048r^4-1152r^3+1552r^2+1008r+109}
 {128(r+1)(2r+1)}.
\]
For \(j=1,2\) the following is an **exact equality of rational numbers**:
\[
(8r+1)C_r=
  R_j(r+1)C_{r+1}-R_j(r)C_r+\rho_j(r)C_r.
\]
For every prime \(p=4d+3>3\), both residue moments are integral on \(0\le r\le d\), and the genuine upper and lower endpoints yield
\[
\boxed{T_p\equiv\tfrac14+18C_d+\sum_{r=0}^{d}\rho_1(r)C_r\pmod p,}
\]
\[
\boxed{T_p\equiv-\tfrac1{16}+\sum_{r=0}^{d}\rho_2(r)C_r\pmod p.}
\]
In particular the original conjecture \(T_p=0\) in the frozen 19-class is *equivalent* to the pole-free moment criterion
\[
\boxed{\sum_{r=0}^{d}\rho_2(r)C_r\equiv\tfrac1{16}\pmod p,}
\]
which is **not proved by this reduction**.

**Proof.** Substitute \(q(r)\) in \(\rho_j(r)=(8r+1)+R_j(r)-q(r)R_j(r+1)\). Because \(R_j(r+1)\) contains \((4r+3)^j/4^j\), the factor \(4r+3\) in \(B(r)\) cancels, leaving the displayed denominators \((r+1)(2r+1)\), all units on the stated window. Sum the exact identities from \(0\) to \(d\). The lower contributions are \(-R_1(0)=+1/4\) and \(-R_2(0)=-1/16\). The upper terms are \((p/4)C_{d+1}\equiv18C_d\pmod p\) and \((p^2/16)C_{d+1}\equiv0\pmod p\), respectively. QED.

This is a **BRC provenance/valuation-carrier application** rather than an alteration of original arithmetic sources. It retains the ordered rank population, finite endpoints, numerator/denominator \(p\)-valuation, and the exact next operation (cutoff summation). Suppressing the \(v_p(C_{d+1})=-1\) tail before multiplying by the gauge loses an actual unit boundary: \(18C_d\). The double-zero observer is the minimal polynomial order needed to remove that boundary modulo \(p\) without pretending the pole was absent.

## Author checks and current limit

The standard-library Python companion verifies the two rational decompositions at 45 consecutive ranks, the incompatible linear-coefficient certificate for GH-7, the two reduced finite-field formulas and endpoint normalization for all 154 primes \(7\le p<2001\) with \(p\equiv3\pmod4\), and exact rational finite sums for \(p=7,11,19,43,67\). Of those 154 primes, 37 are in the frozen \(19\pmod{24}\) class; their vanishing is observed, not proved by finite testing. These are author checks, not independent or formal verification.

**Next smallest science problem:** attempt to prove or refute \(\sum_{r=0}^{d}\rho_2(r)C_r=1/16\) in \(\mathbf F_p\) for every \(p\equiv19\pmod{24}\), using a true finite-field / geometric character sum or a p-dependent WZ certificate that retains both endpoint valuations. A useful first step is a finite-field recurrence or involution on the *regularized* integrand (not another unqualified Gosper ansatz). If successful, lift the *labelled* MM/LH ports with GH-5's \(C_p,K_p\), then connect GH-4, R23 and R36 without erasing original W/S, six Hasse J/E labels, two finite endpoints or the positive-infinity port. Native H0/B0, \([X]U\bmod p^2\), Frobenius \(\eta/\kappa\), native \(p=373\), canonical claim/checkpoint and independent Driver review remain open.

**Control:** current ordinary gateway 0.6.11 has \(research\_authority\_granted=false\), \(executor\_binding\_configured=false\), and native active-job quota at 5/5. No fresh winning own CLAIM, authorized OPEN or native Source checkpoint is established in this turn. The historical predecessor-claim issue remains tracked at enterprise-math#1558. Do not treat this portable artifact as a Source-authenticated completed predecessor or as a registered Research-Activity.
