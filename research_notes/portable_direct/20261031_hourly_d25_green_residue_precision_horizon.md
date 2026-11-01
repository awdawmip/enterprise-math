# D25/LIFT — p-local Green adjoint, residue gauge, first higher-jet resonance

Date 2026-10-31. Research logical conversation \`chatgpt-research-hourly-enterprise-math-20260923\`; research publication TP2-B6F4FC938FF94941C1B7, Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. P000 ACTIVE unchanged. Status AUTHOR-DERIVED / EXACT-RATIONAL-AND-MODULAR-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. The results concern external rational and p-local finite arithmetic, not original-class H0/B0 or native X6.

## Frozen first-jet input and exact question

The *other* Research lane established (see research_notes/portable_direct/20261031_onhour_d25_finite_rational_green_eval_terminal_punit.md) for p=6ell+1, M=3ell, the actual source polynomial F_p(1-y)=sum_(0<=k<=7ell) f_k y^k with **f_M=0 exactly** and its Green readout
\[
E_p=\sum_{k\ne M}f_k\frac{1-2^{M-k}}{k-M}.
\]
This input is consumed, not reproved. We determine the precise rational-primitive condition, finite adjoint recurrence, and p-local validity horizon of this Green interface.

## Theorem 1: necessary/sufficient rational primitive and p-local integrality

Fix integers M>=1, D>=0 and F(y)=sum_(k=0)^D f_k y^k over Q. Consider the Laurent rational differential omega_F=F(y)y^(-M-1)dy. A rational function Q(y) with dQ=omega_F exists **if and only if f_M=0** (interpret as zero if M>D); when it exists its nonconstant part is uniquely
\[
\boxed{Q_F(y)=\sum_{k\ne M}\frac{f_k}{k-M}y^{k-M}.}\tag{1}
\]
All other primitives differ by a constant. If p is an odd prime, f_k are p-local rationals, the primitive has coefficients in Z_(p)[y,y^(-1)] **if and only if** f_M=0 and
\[
\boxed{v_p(f_k)\ge v_p(k-M)\quad\text{for every }k\ne M\text{ with }f_k\ne0.}\tag{2}
\]
Proof: A derivative of a rational function has vanishing y^(-1) coefficient in its Laurent expansion at y=0. The omega residue is f_M. Vanishing residue makes the explicit finite sum (1) a primitive. Characteristic-zero uniqueness up to constant fixes all its nonconstant Laurent coefficients, giving precisely (2). The proof is exact for every finite D.

## Theorem 2: finite adjoint recurrence and gauge

For k!=M define
\[
h_k=(1-2^{M-k})/(k-M);
\]
let h_M be arbitrary. Then, including indices k=M-1 and k=M,
\[
\boxed{(k-M+1)h_{k+1}-(k-M)h_k=2^{M-k-1}.}\tag{3}
\]
The first-order adjoint has exactly one unconstrained coordinate h_M. It is invisible to the Green readout on the actual residue-free family:
\[
\boxed{Q_F(1)-Q_F(1/2)=\sum_{k\ne M}f_kh_k.}\tag{4}
\]
Proof: (k-M)h_k=1-2^(M-k); subtraction at adjacent indices yields (3). At k=M-1 and M the coefficient of h_M is identically zero; (4) follows by evaluating (1). This is a *finite*, algebraically defined Green primitive; no divergent formal integration or unverified substitution is used.

## Theorem 3: sharp p-local higher-jet degree wall

For actual D25 p=6ell+1>=7, M=3ell and D=7ell,
\[
-M\le k-M\le4\ell,\qquad 0<|k-M|<p\text{ for }k\ne M.
\]
Thus all nonzero denominators are p-units, and the inherited exact residue cancellation f_M=0 is sufficient for p-local integrality. If later jets extend the degree, the **first potentially nonunit positive denominator** appears at
\[
\boxed{k=M+p=9\ell+1.}\tag{5}
\]
The obstruction is sharp: F=y^(M+p) has zero residue, yet its only primitive modulo a constant is y^p/p, not in Z_(p)[y,y^(-1)]; F=p y^(M+p) has p-local primitive y^p. More generally modes k=M+tp require v_p(f_k)>=v_p(tp). For arbitrary new modes the full criterion (2) governs. Hence the older f_M=0 certificate must not be extrapolated beyond its actual degree wall.

## Composed two-port source-aware expression

The same logical Research lane previously proved the *separate* original signed-R adjoint \[R_p=-20\ell^3c_\ell\lambda_\ell\] modulo p (file 20261031_hourly_d25_signed_R_dual_green_telescope.md, commit 8f3ad2b9e2d3692f0f1b5e10a7ccdd8d12947a54). Combining this with the other Research lane's first-jet-only source identity, for frozen target primes p mod24 in {13,19}, gives exactly
\[
\boxed{\frac{A_p-p}{p^2}\equiv
\frac{L_0N_0-1}{p}+L_0N_1
-12\cdot2^{-3\ell}\sum_{k\ne M}f_kh_k
+20\ell^3c_\ell\lambda_\ell\pmod p.}\tag{6}
\]
This is a full algebraic *interface reduction*, not a proof of universal vanishing. The Green E and signed R belong to distinct original-source ports. Previously verified anchors (p,E,R): (19,12,12), (67,19,21), (373,1,196). A scalar coincidence at p19 cannot replace the independent provenance.

## Executed independent exact verification

The accompanying executable script d25_green_residue_precision_horizon_20261031.py uses Python Fraction and modular integer arithmetic. Rational ell=1..10: verified (3) including both sides of M, primitive coefficientwise, and endpoint identity (4) for arbitrary residue-free finite polynomials. For all 330 primes p=6ell+1 in [7,5000], independently compared finite kernel, dual recurrence, and Green endpoint evaluation modulo p. Every prime also checked the first extension k=M+p and the sharp F=y^(M+p), p*y^(M+p) distinction. Actual marker:
\`PASS_D25_GREEN_RESIDUE_PLOCAL_HORIZON rational_ell=1..10 primes=330 k_max=7ell first_extra_k=M+p\`.
This script **does not reconstruct the actual J0/J1 scientific source polynomial**, which is inherited from the other lane's existing proof. It is not a native p373 experiment, a universal cancellation test, or mathematical admission.

## Next precise problem, provenance and control

Construct a genuinely **coupled** finite WZ/CM telescoping relation linking the carry (L0N0-1)/p, the first-jet L0N1, the Green coefficients f_k/h_k and the distinct signed-terminal c_ell/lambda_ell. It must not become a block-diagonal restatement of (6); preserve original fixed 216 denominator and signed nonzero p19/p67/p373 anchors. If degrees grow, enforce criterion (2). The mother objective A_p=p mod p^3 for all frozen target primes remains OPEN; original-class H0/B0 experiment enterprise-math#1559 remains with its authorized owner. Current Gateway 0.6.11 at beginning of this run showed research_authority_granted=false, executor_binding_configured=false, active_jobs=5/5, CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED; exact continuation returned CONTROL_QUOTA. Controller support issue #1558 governs lawful service recovery. No native CLAIM/OPEN/checkpoint/Result/review is inferred from author-side GitHub publication.
