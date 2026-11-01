# D25 — Pfaff–Saalschütz collapse of the terminal Green normalization (all p-adic jets)

2026-10-31. Author-side TASK_RESEARCH, logical lane \`chatgpt-research-hourly-enterprise-math-20260923\`; parent \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; task publication \`TP2-B6F4FC938FF94941C1B7\`; frozen scientific Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. P000 ACTIVE unchanged. **AUTHOR-DERIVED / EXACT-FINITE-HYPERGEOMETRIC-PROOF / EXACT-INTEGER-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.** This is classical finite-hypergeometric algebra applied to the inherited D25 Green terminal source, not a claim of first discovery of Pfaff–Saalschütz or a proof of the final D25 supercongruence.

## Reused theorem, not claimed as new

The hourly signed-residue note at Enterprise Math commit \`5a19591c6841efd21acd1bba1b123d2d90ab66ff\` established for all positive \(\ell\):
\[
S_\ell=\sum_{i=0}^{\ell}\binom{\ell}{i}\binom{2\ell}{i}\binom{6\ell+i}{3\ell},\qquad
\Gamma_\ell=\frac{(-1)^\ell}{18S_\ell}.
\tag{0}
\]
The independent on-hour note \`20261031_onhour_d25_terminal_gamma_second_digit_harmonic.md\` (commit \`cfa1e3fd82e2780a8aefe2ff0414e6bfaf15fc55\`) gave a nontrivial finite-harmonic first correction \(\mathcal H_\ell\) and \(\Gamma_\ell\bmod p^2\), \(p=6\ell+1\). The preceding *same hourly lane* new note \`20261031_hourly_d25_frobenius_plateau_green_scalar_defect.md\` gives the distinct regularized scalar and logarithmic repair observers, re-used below. This note **does not reattribute** those earlier results.

## Theorem 1 — exact balanced terminating binomial collapse

For **every** integer \(\ell\ge1\) and indeterminate \(N\), with generalized binomial coefficients regarded as polynomials in \(N\),
\[
\boxed{\sum_{i=0}^{\ell}\binom{\ell}{i}\binom{2\ell}{i}\binom{N+i}{3\ell}
=\binom{N}{\ell}\binom{N}{2\ell}.}
\tag{1}
\]
In particular, setting \(N=6\ell\) gives the entirely explicit terminal scalar
\[
\boxed{S_\ell=\binom{6\ell}{\ell}\binom{6\ell}{2\ell}.}
\tag{2}
\]

**Proof.** It suffices to prove (1) for integers \(N\ge3\ell\), since both sides are degree-\(\le3\ell\) polynomials. Set \(M=3\ell\), use
\[
\frac{\binom{N+i}{M}}{\binom{N}{M}}=
\frac{(N+1)_i}{(N-M+1)_i},\qquad
\binom{\ell}{i}\binom{2\ell}{i}=
\frac{(-\ell)_i(-2\ell)_i}{(i!)^2}.
\]
The left side divided by \(\binom{N}{M}\) is
\[
{}_3F_2\left[\begin{matrix}-\ell,-2\ell,N+1\\1,N-M+1\end{matrix};1\right].
\]
Apply the *standard, independently existing* terminating balanced Pfaff–Saalschütz identity with \(n=\ell,\ a=-2\ell,\ b=N+1,\ c=1\):
\[
{}_3F_2[-n,a,b;c,1+a+b-c-n;1]
=\frac{(c-a)_n(c-b)_n}{(c)_n(c-a-b)_n}.
\]
Its second denominator is exactly \(N-M+1\). Thus the sum becomes
\[
\binom{N}{M}
\frac{(2\ell+1)_\ell(-N)_\ell}{\ell!(2\ell-N)_\ell}
=\frac{(N!)^2}{\ell!(2\ell)!(N-\ell)!(N-2\ell)!}
=\binom{N}{\ell}\binom{N}{2\ell}.
\]
The identity extends polynomially to all \(N\). QED. Classical identity reference: https://mathworld.wolfram.com/SaalschuetzsTheorem.html .

## Theorem 2 — exact terminal normalization and arbitrary-order p-adic jets

For a formal variable \(x\), define
\[
P_\ell(x)=(-1)^{3\ell}\sum_{i=0}^{\ell}
\binom{\ell}{i}\binom{2\ell}{i}\binom{x-1+i}{3\ell}.
\]
By (1) with \(N=x-1\),
\[
\boxed{P_\ell(x)=
\prod_{r=1}^{\ell}\left(1-\frac{x}{r}\right)
\prod_{r=1}^{2\ell}\left(1-\frac{x}{r}\right).}
\tag{3}
\]
Equivalently, using the exact \(\,q_j=[y^j]G_\ell(1-y)\) from the preceding note,
\[
P_\ell(x)=[y^{3\ell}](1-y)^{x-1}G_\ell(1-y)
=\sum_{j=0}^{\ell}q_j\prod_{r=1}^{3\ell-j}(1-x/r).
\tag{4}
\]
This is an exact equality of **degree-\(3\ell\) rational polynomials**. At the special prime \(p=6\ell+1\), \(P_\ell(p)=(-1)^\ell S_\ell\); thus the *inherited* \(\Gamma_\ell\) satisfies
\[
\boxed{18\Gamma_\ell=
\left[
\prod_{r=1}^{\ell}\left(1-\frac{p}{r}\right)
\prod_{r=1}^{2\ell}\left(1-\frac{p}{r}\right)
\right]^{-1}.}
\tag{5}
\]
Every factor and inverse is a \(p\)-adic unit since \(2\ell<p\); (5) determines **all finite \(p\)-adic digits**, not merely the previously published first or second digit.

Let \(A_\ell=H_\ell+H_{2\ell}\) and \(B_\ell=H_\ell^{(2)}+H_{2\ell}^{(2)}\), with \(H_m^{(s)}=\sum_{r=1}^m r^{-s}\). From (3), the *exact formal expansion* is
\[
\boxed{\log(18\Gamma_\ell)=
\sum_{s\ge1}\frac{p^s}{s}
\big(H_\ell^{(s)}+H_{2\ell}^{(s)}\big),}
\tag{6}
\]
where the logarithm means the standard convergent \(p\)-adic logarithm of \(1+p\mathbb Z_p\), or equivalently a formal \(x\)-series evaluated at \(p\). In particular,
\[
\boxed{
\Gamma_\ell\equiv\frac1{18}
\left[1+pA_\ell+\frac{p^2}{2}(A_\ell^2+B_\ell)\right]
\pmod{p^3}.}
\tag{7}
\]

This also proves an **exact rational simplification** of the on-hour first-jet harmonic expression, for each positive integer \(\ell\):
\[
\boxed{
-H_{3\ell}+
\sum_{i=1}^{\ell}\frac{(-1)^i
\binom{\ell}{i}\binom{2\ell}{i}}{i\binom{3\ell}{i}}
=-H_\ell-H_{2\ell}.}
\tag{8}
\]
**Proof of (8).** Differentiate both forms of \(P_\ell(x)\) at \(x=0\). The coefficient expansion from the sum on the left is exactly the expression on the left of (8), while the logarithmic derivative of the product (3) is \(-H_\ell-H_{2\ell}\). QED.

A second derivative produces the finite second-jet identity
\[
\boxed{
\frac{H_{3\ell}^2-H_{3\ell}^{(2)}}2+
\sum_{i=1}^{\ell}
\frac{(-1)^i\binom{\ell}{i}\binom{2\ell}{i}}
{i\binom{3\ell}{i}}
(H_{i-1}-H_{3\ell-i})
=
\frac{A_\ell^2-B_\ell}{2}.}
\tag{9}
\]
**Proof.** Expand the i=0 factor and the single-root i>=1 factors of the left form of \(P_\ell(x)\) to order \(x^2\); expand the product form (3) to the same order. Every displayed denominator is nonzero in \(\mathbb Q\) and a \(p\)-unit for prime \(p=6\ell+1\). QED.

## Consequence for the separate Green residual

The previous hourly note proved \(\mathcal T_\ell\bmod p\) as a finite symmetrized Frobenius plateau observer and
\((E_\sharp-E)/p\equiv-\mathcal H_\ell\mathcal T_\ell/18\pmod p\). Equation (8) immediately upgrades the **interface expression** to
\[
\boxed{\frac{E_\sharp-E}{p}
\equiv \frac{(H_\ell+H_{2\ell})\mathcal T_\ell}{18}\pmod p.}
\tag{10}
\]
The independent logarithmic residue is \((r_\sharp/p)\equiv (H_\ell+H_{2\ell})/18\pmod p\). The exact source requires **both** the low and terminal components for zero logarithmic residue; these are NOT equivalent to the regularized scalar at higher precision.

More generally, retaining the exact \(p\)-local rational \(\mathcal T_\ell\) from the preceding note, (7) gives
\[
\boxed{
E_\sharp-E\equiv
\frac{pA_\ell\mathcal T_\ell}{18}
+\frac{p^2(A_\ell^2+B_\ell)\mathcal T_\ell}{36}
\pmod{p^3}.}
\tag{11}
\]
Here \(A_\ell,\mathcal T_\ell\) are taken to their actual \(p\)-adic precision, rather than truncated prematurely. This is a **source/observer repair**, not the missing four-port D25 cancellation.

## Independent exact verification

Executed standard-library integer/Fraction program \`d25_terminal_saalschutz_collapse_check_20261031.py\`: exact evaluation of (1) at seven integer \(N\) for each \(\ell=1,\dots,14\); exact rational verification of (8) for those same \(\ell\); direct original terminal sum versus the product (2) for every prime \(p\equiv1\bmod6,\ 7\le p\le1200\) (94 primes); independent modular inversion of exact \(\Gamma_\ell=(-1)^\ell/(18S_\ell)\) versus (7), and the normalized \(S_\ell\) second-jet expansion, modulo \(p^3\). All checks PASS.

Selected exact modular witnesses \((p,\ell,A_\ell\bmod p,B_\ell\bmod p,\Gamma_\ell\bmod p^3)\):
\[
(19,3,16,1,759),\quad
(67,11,2,6,226702),\quad
(373,62,181,298,4162162).
\]
The \(373\) result reduces to \(\Gamma_{62}\equiv127421\bmod373^2\), in agreement with the previously independent on-hour report. Finite checks corroborate the program; the general identity follows from (1), itself a specialization of the established Pfaff–Saalschütz theorem.

## Remaining science and control scope

The frozen D25/LIFT objective remains
\[
\sum_{n=0}^{p-1}(6n+1)
\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n}
\stackrel{?}{\equiv}p\pmod{p^3},\qquad p\bmod24\in\{13,19\}.
\]
Its current four-port Green/first-jet/integer-carry/signed-\(R\) joint cancellation remains **OPEN**. The new exact closed form (2) and all-order gamma (5) may eliminate an auxiliary terminal-normalization unknown from candidate joint certificates; they do not individually cancel \(R_p\), prove the original congruence, or constitute native H0/B0 evidence.

Next precise step: substitute the binomial-product gamma and harmonic collapse directly into the original *full* finite Green/adjoint WZ system (retaining original 216, exact \(\pm1/18\) internal residues, and the separate signed \(R_p\)). Seek a single telescoping certificate for the full four-port cancellation. Validate nonzero boundary examples \(p=19,67,373\), distinguish mod-\(p\) scalar quotient from mod-\(p^2\) source equality, and preserve P000/Source pins.

At this run, Gateway 0.6.11 reported \`research_authority_granted=false\`, \`executor_binding_configured=false\`, \`CODE_REVIEW_REQUIRED/UPSTREAM_CODE_REVIEW_REQUIRED\` and five active control jobs at its quota. The connector has no callable \`recovery_status\` entry and no new native authorized run/claim/Source checkpoint is asserted. #1558 remains the control repair path. Author-side Git source only; formal task Result and independent mathematical admission remain pending.