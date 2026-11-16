# JT2 UR — Universal spectral basepoint and first p-adic deformation

Date: 2026-11-17. Status: **PROVED COEFFICIENTWISE MOD-\(p^2\) THEOREM; CM-PORT RESIDUE REFORMULATION; FINITE EXACT CHECKS**.

## Scope and authorship

Author-side research extension by Driver EM-DVR-DEBB5E. Original JT2 UR source proofs and contributors, including EM-JT2-EF9380, are retained. The all-prime UR target is open. This note is not an independent Native review or acceptance.

Let \(p>3\) be prime with \(p=6m+1\), \(m\ge 1\), and work in \(R=\mathbb Z_{(p)}\). Define

\[
Q_m(Y)=P_{2m}(\sqrt Y)=c_0 H_m(C_*,Y),\qquad
c_0=(-1)^m\binom{2m}{m}4^{-m},\qquad C_*=m(2m+1).
\]

The **finite degree-\(m\) spectral polynomial** (not an untruncated analytic series) is

\[
H_m(C,Y)=\sum_{j=0}^{m}a_j(C)Y^j,\quad a_0=1,\quad
a_{j+1}(C)=\frac{j(2j+1)-C}{(j+1)(2j+1)}a_j(C)\quad(0\le j<m).
\]

Write \(Z_m(Y)=c_0\,\partial_C H_m(C,Y)|_{C=C_*}\), the earlier spectral derivative. At the universal rational basepoint \(C_0=-1/9\), put

\[
F_m(Y)=H_m(-1/9,Y)
=\sum_{j=0}^{m}\frac{(1/6)_j(1/3)_j}{(1/2)_j j!}\,Y^j.
\]

All displayed finite spectral coefficients are \(p\)-integral: in the recurrence \(j+1,2j+1\) are \(p\)-units for \(0\le j<m\), and \(2,3,6,9,18\) are units.

## Theorem A — Coefficientwise universal basepoint deformation

For **every** \(p>3\) prime satisfying \(p=6m+1\), in \(R[Y]/p^2R[Y]\):

\[
\boxed{Q_m(Y)\equiv c_0F_m(Y)+\frac{p}{18}Z_m(Y)\pmod {p^2}.}\tag{D}
\]

This is a polynomial identity, valid before imposing a CM port, CM0, or any special-value condition.

**Proof.** The exact spectral parameter relation is

\[
C_*=m(2m+1)=\frac{p^2+p-2}{18}
=-\frac19+\frac{p(p+1)}{18}=C_0+\delta.
\]

Each coefficient of \(H_m(C,Y)\) lies in \(R[C]\), since its recurrence denominators are \(p\)-units. Taylor expansion in \(C\) is therefore valid modulo \(p^2\):

\[
H_m(C_*,Y)\equiv H_m(C_0,Y)+\delta\,\partial_C H_m(C_0,Y)\pmod{p^2}.
\]

Here \(\delta\equiv p/18\pmod{p^2}\), and \(\partial_C H_m(C_*,Y)\equiv\partial_C H_m(C_0,Y)\pmod p\). Multiply by \(c_0\) and use the definitions. The coefficient ratio at \(C_0\) is

\[
\frac{a_{j+1}(C_0)}{a_j(C_0)}
=\frac{j(2j+1)+1/9}{(j+1)(2j+1)}
=\frac{(j+1/6)(j+1/3)}{(j+1)(j+1/2)},
\]

which identifies precisely the truncated series \(F_m\). QED.

**Independent coefficient-level proof/check.** Define

\[
T_j=\sum_{i=0}^{j-1}\frac{1}{(m-i)(2m+2i+1)},\qquad T_0=0,
\quad f_j=\frac{(1/6)_j(1/3)_j}{(1/2)_j j!}.
\]

For every \(0\le j\le m\), (D) asserts

\[
c_j\equiv c_0 f_j+\frac p{18}c_jT_j\pmod {p^2},
\quad Q_m(Y)=\sum c_jY^j,\quad Z_m(Y)=\sum c_jT_jY^j.
\]

Indeed,

\[
(i-m)(i+m+\tfrac12)
=(i+\tfrac16)(i+\tfrac13)-\frac{p(p+1)}{36},
\]

and modulo \(p\),

\[
T_j\equiv-\frac12\sum_{i<j}\frac1{(i+1/6)(i+1/3)}.
\]

Expanding the finite product through its first \(p\)-adic correction proves the same coefficientwise identity.

## Corollary B — The divided CM half-value

Now restrict to \(p\bmod24\in\{13,19\}\) and assume the inherited CM0 condition \(Q_m(1/2)\equiv0\pmod p\). Then (D) implies \(F_m(1/2)\equiv0\pmod p\). Thus both divisions by \(p\) are legitimate. Define

\[
u_m=\frac{Q_m(1/2)}p\pmod p,\quad
v_m=\frac{F_m(1/2)}p\pmod p,\quad
d_m=Q'_m(1/2)\pmod p.
\]

Then

\[
\boxed{u_m\equiv c_0v_m+\frac1{18}Z_m(1/2)\pmod p.}\tag{H}
\]

The quotient \(v_m\) is an explicitly defined **finite hypergeometric basepoint quotient**, with the same frozen polynomial cutoff \(m\).

## Corollary C — Spectral derivative and quadratic norm both cancel from UR

Use the already proved finite polynomial Lagrange identity

\[
2J_m(1/2)\equiv d_mZ_m(1/2)+2c_mS_p\pmod p,
\]

where

\[
J_m(Y)=\sum_{r=0}^{2m}\frac{[Y^r]Q_m(Y)^2}{2r+1}Y^r,\quad
S_p=\sum_{j=0}^{m}\frac{c_j\,2^{-(m+j)}}{2m+2j+1}.
\]

The existing scalar obstruction is

\[
\varepsilon_p\equiv18u_md_m-2J_m(1/2)-3\pmod p.
\]

Substitute (H) and the Lagrange identity to eliminate \(Z_m\) exactly:

\[
\boxed{\varepsilon_p\equiv18c_0d_mv_m-2c_mS_p-3\pmod p.}\tag{U}
\]

Thus the all-prime UR question is equivalently a congruence involving one \(p^2\)-level **truncated basepoint sum** and two \(O(m)\) coefficient sums. The representation needs neither spectral parameter differentiation nor a quadratic convolution. It retains the CM0 hypothesis and the original model/normalizations. **Uniform vanishing of (U) remains open.**

## Exact verification, coverage, and limits

An independent modular finite check covered all **148** primes \(p\le2000\) with \(p\bmod6=1\), verifying (D) coefficient by coefficient modulo \(p^2\). Among these, **77** primes have \(p\bmod24\in\{13,19\}\); the actual \(p\)-divisions and (H) matched. For the **15** qualifying primes \(p\le300\), a separately computed quadratic convolution for \(J_m(1/2)\) confirmed (U) against the original residual. These 15 residuals were zero. Arithmetic was exact, with all inverses taken only of \(p\)-units. These tests crosscheck the proof; finite enumeration alone is not the all-prime UR proof.

Verifier: experiments/jt2_ur_spectral_basepoint_padic_deformation_20261117.py.

## Source and contribution boundaries

- Frozen historical return: research_returns/EMW59A_JT2_UR_SUN_PARITY_DEFECT_RETURN_EF9380_20260910.md; immutable result RR-60983E048B55C2AC7F66; author EM-JT2-EF9380.
- Earlier Driver spectral/harmonic companion: research_notes/driver/2026-11-17_jt2_ur_spectral_logarithmic_harmonic_companion.md; author EM-DVR-DEBB5E.
- New polynomial deformation theorem, quotient reduction and crosscheck: Driver EM-DVR-DEBB5E; context shared, independence not asserted.
- Task/Result and mother-level completion are separate. The target \(\varepsilon_p=0\) for all the frozen prime classes remains open.


## Theorem D — Exact finite hypergeometric boundary-source equation

The degree-\(m\) basepoint polynomial \(F_m\) also satisfies an **exact rational inhomogeneous differential equation**, with the entire truncation error concentrated in its highest monomial. Define

\[
\mathcal L_C[G]:=Y(1-Y)G''+
\left(\frac12-\frac32Y\right)G'+\frac C2 G.
\]

Then, without reducing modulo \(p\),

\[
\boxed{\mathcal L_{-1/9}[F_m]=
-\frac{p(p+1)}{36}f_mY^m.}\tag{ODE-BOUNDARY}
\]

Equivalently, since \(C_*-(-1/9)=p(p+1)/18\),

\[
\boxed{\mathcal L_{C_*}[F_m]
=\frac{p(p+1)}{36}\left(F_m-f_mY^m\right),\qquad
\mathcal L_{C_*}[H_m(C_*,Y)]=0.}\tag{ODE-PAIR}
\]

**Proof.** The coefficient of \(Y^j\) in \(\mathcal L_{-1/9}[F_m]\), for \(j<m\), is

\[
(j+1)(j+\tfrac12)f_{j+1}
-(j+\tfrac16)(j+\tfrac13)f_j=0
\]

by the exact hypergeometric coefficient recurrence. At \(j=m\), the missing \(f_{m+1}\) term leaves only
\[
-(m+\tfrac16)(m+\tfrac13)f_m
=-\frac{p(p+1)}{36}f_m.
\]
This is the whole polynomial remainder. Adding the constant operator difference \((C_*-C_0)F_m/2\) proves the first relation in (ODE-PAIR). At \(C_*\), the degree-\(m\) spectral recurrence terminates exactly because the next numerator is \(m(2m+1)-C_*=0\), so \(\mathcal L_{C_*}[H_m(C_*,Y)]=0\). QED.

Consequently \(\overline F_m\) is an exact polynomial solution of the **homogeneous basepoint equation over \(\mathbb F_p\)**, although the rational truncated lift has the explicit boundary source above. This isolates the next arithmetic question: evaluate the divided special value \(v_m=F_m(1/2)/p\bmod p\) while respecting that top-coefficient source. The full uniform UR residual remains the equation (U), still open. The operator identity was additionally checked coefficientwise in exact rational arithmetic for \(m=1,\ldots,8\).
