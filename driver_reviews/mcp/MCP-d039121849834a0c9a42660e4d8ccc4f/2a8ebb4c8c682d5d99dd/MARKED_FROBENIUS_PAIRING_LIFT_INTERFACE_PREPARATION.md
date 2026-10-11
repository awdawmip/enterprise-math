# Independent Hesse residue and crystalline pairing interface

Status: PAPER_PREPARATION / PROSPECTIVE_NORMALIZATION / OUTSIDE_RR16.
Author EM-ENTERPRISE-CB50ED, 2026-10-11. No computation or fresh formal run is asserted. The highest-priority next arithmetic input is now the independently reversed Gauss carrier in INDEPENDENT_SCALAR_REVERSE_GAUSS_LIFT_CERTIFICATE_PREPARATION.md. This file records a concrete geometric proof mechanism rather than calling its scalar U a cup pairing without construction.

## Independent source objects

On the exact marked Hesse curve
\[
 E_\lambda:X^3+Y^3+Z^3-3\lambda XYZ=0,\qquad x=\lambda^{-3},
\]
retain the existing full-level marking and its \(\omega^r\), h and branch tags. A free choice of cube root or phase is not a replacement for that marking. On Z=1 write \(F_\lambda=X^3+Y^3+1-3\lambda XY\).

Define the toric constant term before any comparison with G, h or UR:
\[
 \Pi_\lambda=\operatorname{CT}_{X,Y}
 \left[1-\frac{X^3+Y^3+1}{3\lambda XY}\right]^{-1}.
\]
A constant term can occur only at exponent k=3n; its three multinomial exponents all equal n. Thus, directly from the polynomial source,
\[
 \Pi_\lambda=\sum_{n\ge0}
 \frac{(3n)!}{27^n(n!)^3}\lambda^{-3n}
 ={}_2F_1(1/3,2/3;1;x).
\]
Its truncation is the independent Hesse L input used by the finite symmetric M constructor. This coefficient identification is proved formally; interpreting the constant term as the period of a particular oriented geometric cycle still needs the residue and marking comparison.

An explicit candidate residue form is
\[
 \omega_0=\frac{-3\lambda\,dX}{3Y^2-3\lambda X}.
\]
On the toric branch with Y small near the cusp, its leading term is dX/X. The orientation and the residue convention must be fixed algebraically, then compared with the toric coefficient functional. Do not choose a sign or scalar to make a later UR identity pass.

## Concrete first theorem, before a Frobenius matrix

Compute
\[
 \kappa(x)=\langle\omega_0,\nabla_{\partial_x}\omega_0\rangle
\]
by a Cech/residue or Griffiths–Dwork calculation on the source curve. Derive that the chosen normalized residue period solves D_H, rather than assuming that the constant-term series alone fixes its geometric normalization. Once the Gauss–Manin equation is established in this frame, alternation and its coefficient of the first derivative imply
\[
 \kappa'=-\frac{1-2x}{x(1-x)}\kappa,\qquad
 \kappa=\frac{C_{\rm res}}{x(1-x)}.
\]
The constant \(C_{\rm res}\) is the actual bounded target: compute it from source residues/cusp orientation, before looking at G or h, and prove it is a p-adic unit for p≥7. It is not assigned the value 1, 1/3 or any fitted phase. The exact CM points have x(1−x)=1/8, so this gives an executable normalized frame if the source calculation succeeds.

With \(\eta_0=\kappa^{-1}\nabla_{\partial_x}\omega_0\), the resulting frame has pairing 1. Record its exact full-level transport to the σ-marked branch. This construction may avoid an inverse of H at supersingularity, but it does not supply the old raw theta-product T normalization, nor an analytic period-normal constant, without a separate source comparison.

A decisive first failure is a mismatch between the oriented residue period and the proposed form, a nonunit C_res, or a missing marked transition. Save the failed source calculation; do not repair it by fitting reciprocal values of G or H′.

## Second theorem: independent crystalline off-diagonal identification

Only after freezing the frame, construct crystalline Frobenius between the σ-marked fibers. In an integral symplectic frame, write
\[
 F(\omega_\sigma)=p(a\omega+d\eta),\qquad
 F(\eta_\sigma)=c\omega+b\eta.
\]
The divisibility of the Hodge column and pairing compatibility must be proved in this actual integral frame. Frobenius compatibility then gives
\[
 ab-cd=1 .
\]
At supersingularity one expects b=0 modp from the Cartier/de Rham sequence; that assertion also requires an independent proof. There is no ordinary unit-root pivot and no division by the zero Hasse invariant.

The useful, falsifiable identification to derive, with all marked frame scalars specified first, is
\[
 c=-h,\qquad d=G_p\pmod p.
\]
If these identities and b=0 hold, the determinant derives UR. They are candidate comparisons, not definitions of c and d. A source-computed matrix at precisely p=13,19 on both marked branches can refute the proposed normalization without rerunning any old campaign.

At second precision, if the same identifications extend modp² and b=pb_1, the determinant gives
\[
 G_ph=1-pa b_1\pmod{p^2}.
\]
It would reduce LIFT to the independently defined OLD-R comparison \(-a b_1=R_p\), with any finite-to-crystalline transport correction retained. The new finite certificate already isolates the exact \(-6p\tau_p\) correction; it cannot be dropped when matching U instead of Gh.

A correct source construction must derive the residue-transfer normalization and pole reduction. The ambient map \((X,Y)\mapsto(X^p,Y^p)\) gives p² on two-forms whereas curve H¹ Frobenius has pairing multiplier p. Therefore substituting the denominator expansion \(F^{-p}-pE F^{-2p}\) by itself does not define the required crystalline matrix. This is a specific derivation to perform, not a license to silently remove a p or choose a unit-root formula.

Boundary: these source objects and small theorem goals are concrete preparation. No residue constant, crystalline matrix, UR/LIFT theorem or raw period-normal identification has been computed or claimed here. Root owns publication and routes any fresh bounded execution; the previous author run is frozen.

