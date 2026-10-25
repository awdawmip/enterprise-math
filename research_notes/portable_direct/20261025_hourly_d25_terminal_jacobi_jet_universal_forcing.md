# D25/LIFT — universal terminal forcing of the second Jacobi parameter jet

Date: 2026-10-25. Research lane: TASK_RESEARCH; portable author derivation, exact author check, UNREVIEWED / NOT_ADMITTED / NO_NATIVE_CHECKPOINT. Mother objective D25/LIFT/JT2 remains OPEN. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 **unchanged**. Do not reinterpret the plain Hesse input as authenticated CM/Frobenius data.

## Exact question and contribution

The previously established same-source Jacobi translation bridge [20261025_hourly_d25_jacobi_translation_second_digit_bridge.md](20261025_hourly_d25_jacobi_translation_second_digit_bridge.md) reduces the hard target to a terminating second-parameter-jet identity. Its differential equation has a nonzero cutoff forcing term. This note determines that forcing's exact universal residue, rather than deleting it as a formal truncation artifact. The result holds for **every** prime p=6m+1>=7, not only the target classes p=13,19 (mod 24).

Let N=p-1=6m and

\[
b_n(x)=\frac{(-x)_n(-2x)_n}{(n!)^2},\qquad
\Phi(x,z)=\sum_{n=0}^{N}b_n(x)z^n,\qquad
F_i(z)=\partial_x^i\Phi(m,z)\quad(i=0,1,2).
\]

Write \(\theta=z\,d/dz\), \(\mathcal L_x=\theta^2-z(\theta-x)(\theta-2x)\), and \(w_n=b_n''(m)/2\).

**Theorem (universal endpoint-jet anomaly).** In the p-local polynomial ring, the exact identities are

\[
\mathcal L_m F_0=0,\qquad
\mathcal L_m F_1=-z(3\theta-4m)F_0,
\]
\[
\boxed{\ \mathcal L_m F_2
=-2z(3\theta-4m)F_1+4zF_0-40m^2w_Nz^p.\ }
\]

The **exact rational** terminal coefficient is

\[
\boxed{\
w_N=
\frac{2(-1)^m\,m!(2m)!(5m-1)!(4m-1)!}{((6m)!)^2}.
\ }
\]

Its residue is **independent of p**:

\[
\boxed{\quad w_{p-1}\equiv\frac{18}{5}\pmod p,\qquad
-40m^2w_{p-1}\equiv-4\pmod p.\quad}
\]

Consequently the nonhomogeneous identity in \(\mathbb F_p[z]\) is

\[
\boxed{\
\mathcal L_mF_2+2z(3\theta-4m)F_1-4zF_0=-4z^p.
\ }
\]

At **every** \(z_0\in\mathbb F_p\) the residual observer is \(-4z_0\); in particular the D25 evaluation at \(z_0=1/2\) sees the universal nonzero value

\[
\boxed{\quad -4(1/2)^p\equiv-2\pmod p.\quad}
\]

The equality \(z^p=z\) is only an evaluation identity on \(\mathbb F_p\), **not** a polynomial identity in \(\mathbb F_p[z]\). Preserve both representations if further differentiation, coefficient extraction, or different observer fields are allowed.

## Proof (all primes in the stated class)

The coefficient ratio is
\[
(n+1)^2b_{n+1}(x)=(n-x)(n-2x)b_n(x).
\]
Direct coefficient comparison up to degree N+1 gives the **exact truncated equation**
\[
\mathcal L_x\Phi(x,z)=-z^{N+1}(N-x)(N-2x)b_N(x).
\]
At x=m the two numerator Pochhammer products of \(b_N\) have distinct simple zeros (at indices m and 2m). Thus \(b_N(m)=b_N'(m)=0\), but \(b_N''(m)=2w_N\). Because
\(\mathcal L_x'=z(3\theta-4x)\) and \(\mathcal L_x''=-4z\), differentiating this exact equation twice yields the three displayed jet equations. In the second derivative, the surviving endpoint contribution is
\(-2(N-m)(N-2m)w_Nz^{N+1}=-40m^2w_Nz^p\).

For the exact coefficient, differentiating the two factors \((-x)_N\) and \((-2x)_N\) at their simple zeros gives, respectively,
\[
(-1)^{m+1}m!(5m-1)!,\qquad -2(2m)!(4m-1)!.
\]
Their product divided by \(((6m)!)^2\) is precisely \(w_N\). Wilson's theorem gives \(((p-1)!)^2\equiv1\pmod p\), while
\[
(5m-1)!(m+1)!\equiv(-1)^{m+2},\qquad
(4m-1)!(2m+1)!\equiv1\pmod p.
\]
Therefore \(w_N\equiv 2/((m+1)(2m+1))\). Since \(6m\equiv-1\), these two factors reduce to \(5/6\) and \(2/3\), giving \(18/5\). Also \(40m^2\equiv10/9\), so their product is 4. Finally, Fermat's identity at any field point yields \(z_0^p=z_0\). Every denominator above is a p-unit, because p>=7.

**Scoped no-go for a shortcut.** Dividing the endpoint term by z gives \(-4z^{p-1}\) in the normalized differential equation. No polynomial \(G\in\mathbb F_p[z]\) satisfies \(G'=-4z^{p-1}\): the coefficient of \(z^{p-1}\) in a polynomial derivative is \(p[z^p]G=0\). Thus the standalone endpoint input cannot be discarded by pretending it has a polynomial primitive. This **does not** exclude a signed telescoper involving the other jet and reflected-corner terms, or a differently typed rational/function-field mechanism.

## Evidence and precise limitations

The adjacent reproducer \`20261025_hourly_d25_terminal_jacobi_jet_universal_forcing_check.py\` computes p-local Taylor jets via an **exact rational recurrence** (not floating point), checks the **entire** differential polynomial degree by degree, and separately verifies the factorial residue, the \(-4z^p\) coefficient and the \(z=1/2\) observer. All 35 primes p=1 (mod 6) with 7<=p<=373 passed. These are author checks; the quantified result rests on the algebraic proof above; no independent review, Lean formal check, original CM experiment, or native Source checkpoint is claimed.

BRC resolution: **COMPOSE_APPLIED** at the exact source rank/parameter-jet/valuation carrier. The polynomial coefficient \(z^p\), the finite-field point observer, and the signed inhomogeneous boundary are deliberately not merged. The source polynomial's double zero preserves a second-derivative residual when both the value and first derivative vanish.

## Continuation (smallest open unit)

Use the genuine inhomogeneous second-Jacobi-jet equation with the explicit terminal port \(-4z^p\) (or \(-2\) at z=1/2), and the prior exact reflected-corner pairing to search for a **signed, all-target-primes** telescoper of
\(B_{01,p}+A_2H_0/72-T_{\mathrm{jet},p}\).
A homogeneous-Jacobi-only cancellation does **not** close this obligation. Still outstanding: uniform proof of the hard congruence, authenticated same-original-class CM/divided-power \(H_0/B_0,[X]U\bmod p^2\), Frobenius normalization and kappa map, independent review and canonical authorization. Earlier Source checkpoint/contribution history and do-not-repeat remain owned by native Source. This artifact is portable evidence only and is not predecessor completed research or a new claim.
