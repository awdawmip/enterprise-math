# Perfect Prime Beta–Bernstein Möbius quotient external prior-art audit — Research Return

Task: `RS-PERFECT-PRIME-BETA-BERNSTEIN-PRIOR-ART-AUDIT`  
Publication: `TP2-63813372F40BFF2A57BB`  
Researcher-ID: `EM-PPTBBPAUD-54C7E1`  
Claim: `chatgpt-pptbbpaud-20260830-1117-54c7e1`

## Terminal verdict

`SUCCESS / PARTIAL_ANTECEDENT_WITH_ACTIONABLE_THEOREM_FOUND`

No exact duplicate of the full AP operator statement was found in the audited external surfaces. This is **not** a novelty conclusion.

The audit did find two load-bearing existing theorem interfaces that can close the parent target if one precise AP-specific hypothesis is proved:

1. **GSTP / exterior-cone route.** Kushel's generalized strict total positivity theorem gives a positive simple spectrum once every exterior power preserves an appropriate proper cone. Therefore, if
   \[
   \mathcal T_m=R\widehat B R\widehat A
   \]
   can be proved GSTP in a task-specific cone family, the already-known fixed eigenvalue `1` is automatically simple and
   \[
   \det(I_{m-1}-Q_m)\ne0.
   \]

2. **Principal-angle / projection route.** Classical principal-angle theory identifies the singular values of a cross-Gram matrix with principal cosines, and products of two orthogonal projections encode squared principal cosines. Therefore, if `T_m` can be realized up to similarity as a projection/Gram product whose two subspaces intersect only in the fixed `e_0` direction, the quotient cannot contain eigenvalue `1`.

The standard Jacobi Bernstein–Durrmeyer theory supplies a third, narrower spectral model: it has Jacobi polynomial eigenfunctions and an explicit eigenvalue formula with `lambda_(n,0)=1` and all nonconstant eigenvalues below `1`. However, the AP operator is **not currently within that theorem's hypotheses** because its two half maps use the linked coordinates `u` and `u^m`, its common weight is `(1-u^(m^2))^(m-1) du` rather than the operative single Jacobi weight, and the signed non-orthogonal binomial Möbius involution `R` is inserted between the two positive transforms.

## Frozen internal target

The accepted parent frontier is

\[
\mathcal T_m=R\widehat B R\widehat A,
\qquad
\mathcal T_m e_0=e_0,
\qquad
\mathcal T_m=
\begin{pmatrix}
1&*\\
0&Q_m
\end{pmatrix},
\]

with

\[
\boxed{\det(I_{m-1}-Q_m)\ne0}
\]

required for every admissible `m`.

The two positive half maps arise from the same measure

\[
\rho_m(du)=(1-u^{m^2})^{m-1}\,du,
\]

with Bernstein coordinates linked by `u -> u^m`; `Ahat` and `Bhat` are already proved strictly totally positive. The exact `m=4` parent certificate gives a negative entry of `Q_4`, so direct entrywise Perron or direct ordinary total-nonnegativity/oscillation of `Q_m` is unavailable.

## Serious candidate sources and exact mapping

### S01 — Kushel: cone-theoretic generalized total positivity

Citation: O. Y. Kushel, *Cone-theoretic generalization of total positivity*, Linear Algebra and its Applications 436(3) (2012), 537–560, DOI `10.1016/j.laa.2011.07.003`.

Result: generalized strict total positivity is defined by strict preservation of proper cones in all exterior powers, and the resulting operator has a positive simple spectrum.

Mapping: apply the theorem to the **full** `T_m`, not merely `Q_m`. Since `T_m e_0=e_0`, simple spectrum would make eigenvalue `1` simple, which is equivalent to the quotient determinant target.

Missing hypothesis: construct explicit proper cones `K_j(m) subset wedge^j R^m` such that every `wedge^j T_m` is strongly positive on `K_j(m)`. Separate STP of `Ahat,Bhat` does not prove this after the two signed `R` factors.

Classification: `PARTIAL_ANTECEDENT` — **actionable**.

### S02 — principal angles and products of orthogonal projections

Citations: Z. Drmac, *On Principal Angles between Subspaces of Euclidean Space*, SIAM J. Matrix Anal. Appl. 22(1), 173–194, DOI `10.1137/S0895479897320824`; H. Klaja, *The numerical range and the spectrum of a product of two orthogonal projections*, JMAA 411(1) (2014), 177–195, DOI `10.1016/j.jmaa.2013.09.024`.

Result: for orthonormal bases `Q_X,Q_Y`, the principal cosines are the singular values of `Q_X^T Q_Y`; products of orthogonal projections have spectrum controlled by squared principal cosines, with eigenvalue `1` supported on the common subspace.

Mapping: an eigenvalue-preserving realization of `T_m` as an orthogonal-projection/Gram product would turn the parent theorem into the exact transversality statement

`intersection = span(e_0)`.

Missing hypothesis: produce the same-Hilbert-space orthonormal/Gram representation. `Ahat,Bhat` are row-normalized moment transforms rather than orthogonal projections, and `R` is non-orthogonal.

Classification: `PARTIAL_ANTECEDENT` — **actionable**.

### S03 — Jacobi Bernstein–Durrmeyer eigenstructure

Citation: *Bernstein–Jacobi-type operators preserving derivatives*, Computational and Applied Mathematics (2024), DOI `10.1007/s40314-024-02796-2`, especially Eq. (2.5) and Corollary 5.1, which recovers the classical Durrmeyer–Derriennic/Sablonnière theory.

Result: Jacobi polynomials diagonalize the Bernstein–Jacobi operator, with

\[
\lambda_{n,r}^{(\alpha,\beta)}
=
\frac{(n-r+1)_r}{(n+\alpha+\beta+2)_r}.
\]

Thus `lambda_(n,0)=1`, while for `alpha,beta>-1` and `1<=r<=n`, `0<lambda_(n,r)<1`.

Mapping: this is an exact external model showing how a normalized Beta/Bernstein integral operator can have the required simple constant fixed point.

Missing hypothesis: AP is not the same operator. The AP construction uses two different Bernstein variables linked by `u -> u^m`, a non-Jacobi common weight in the operative coordinate, and a signed Möbius transformation between the half maps.

Classification: `PARTIAL_ANTECEDENT`.

### S04 — arbitrary-weight Bernstein–Durrmeyer theory

Citation: E. E. Berdysheva and K. Jetter, *Multivariate Bernstein–Durrmeyer operators with arbitrary weight functions*, J. Approx. Theory 162(3) (2010), 576–598, DOI `10.1016/j.jat.2009.11.005`.

Result: the arbitrary-measure Bernstein–Durrmeyer theory exists, but the paper explicitly records that outside the Jacobi setting degree preservation and orthogonal-polynomial eigenspaces can fail.

Mapping: the AP measure belongs conceptually closer to the arbitrary-weight side than the pure Jacobi side.

Missing hypothesis: the general theory supplies no universal spectral formula excluding `1`, and it still does not contain the AP `u/u^m + R` product.

Classification: `ADJACENT_METHOD`.

### S05 — classical Bernstein operator as a negative control

Citation: S. Cooper and S. Waldron, *The Eigenstructure of the Bernstein Operator*, J. Approx. Theory 105(1) (2000), 133–165, DOI `10.1006/jath.2000.3464`.

Result: the classical Bernstein operator reproduces all linear polynomials, so eigenvalue `1` is already non-simple there.

Mapping: this directly kills any argument of the form “Bernstein + positivity/total positivity implies a unique fixed vector.”

Classification: `ADJACENT_METHOD / NEGATIVE_CONTROL`.

### S06 — Pascal/binomial Möbius factor

Citation: R. Brawer and M. Pirovino, *The linear algebra of the Pascal matrix*, Linear Algebra Appl. 174 (1992), 13–23, DOI `10.1016/0024-3795(92)90038-C`.

Result: the lower Pascal transform, its factorization and inverse/elimination structure are classical.

Mapping: if `L_(j,k)=binom(j,k)`, then the AP matrix `R_(j,k)=(-1)^k binom(j,k)` is a signed/checkerboard variant of the inverse Pascal transform. The Möbius factor itself is therefore not a missing literature object.

Missing hypothesis: no Pascal-matrix theorem found here controls the spectrum of `R Bhat R Ahat` from the shared Beta measure.

Classification: `ADJACENT_METHOD`.

### S07 — special sign regularity and oscillation

Citations: P. Koev and F. Dopico, *Accurate eigenvalues of certain sign regular matrices*, LAA 424(2–3) (2007), 435–447, DOI `10.1016/j.laa.2007.02.012`; classical Gantmacher–Krein oscillation theorem.

Result: the minor signature `(-1)^(k(k-1)/2)` is equivalent to a nonsingular TN matrix with reversed columns; oscillatory matrices have distinct positive eigenvalues.

Mapping: if an AP Möbius-transformed **full product** can be converted, without changing eigenvalues, to an oscillatory matrix, the required simplicity follows.

Missing hypothesis: the frozen parent only establishes STP for the positive half maps, not for the signed normalized full product. Moreover `Q_4` itself has a negative entry, so direct TN of `Q_m` is impossible.

Classification: `PARTIAL_ANTECEDENT` — actionable only after a full-product sign/ordering theorem.

### S08 — Karlin basic composition / TP kernel theory

Citation: S. Karlin, *Total Positivity*, Vol. I, Stanford University Press, 1968.

Result: the classical basic composition formula explains why suitable positive-kernel compositions/integrals preserve total positivity.

Mapping: this is a classical antecedent of the Andreief/generalized-Vandermonde mechanism already used to prove the half-map STP statements.

Missing hypothesis: it does not cross the two signed Möbius factors to prove the full-product fixed-point theorem.

Classification: `ADJACENT_METHOD`.

## Exact duplication test

The audit required a source to cover, jointly rather than separately:

1. the common AP measure `(1-u^(m^2))^(m-1) du`;
2. the paired Bernstein coordinate systems `u` and `u^m`;
3. the AP row normalizations defining `Ahat,Bhat`;
4. two insertions of the binomial Möbius involution `R`;
5. the quotient/fixed-point conclusion `det(I-Q_m) != 0`.

No audited source matched this joint package. Exact-combination searches including `Beta-Bernstein + Möbius quotient + eigenvalue`, `Bernstein + Pascal/Möbius + eigenvalue`, `u^m + Bernstein + total positivity`, the literal AP weight, and `Bernstein-Durrmeyer + Pascal matrix + Mobius` returned only adjacent material or no mathematical match.

Verdict for exact duplication: `NO_EXACT_DUPLICATE_FOUND_IN_AUDITED_SURFACES`.

Guard: `NO_EXACT_DUPLICATE_FOUND != NOVELTY`.

## Strongest research consequence

The literature search does **not** justify restarting from generic total positivity. It sharpens the next mathematical work to two exact interface lemmas:

### Interface A — exterior-cone theorem

Construct cones `K_j(m)` for `j=1,...,m` such that

\[
\wedge^j \mathcal T_m
\]

is strongly positive on `K_j(m)`. Kushel then gives simple spectrum and the parent target immediately.

This route is attractive because it naturally allows signed coordinate changes and does not demand entrywise positivity of `Q_m`.

### Interface B — strict transversality theorem

Construct a Hilbert-space realization in which `T_m` is similar to a product/compression of two orthogonal projections, and prove that their common subspace is exactly one-dimensional. Principal-angle theory then gives the quotient exclusion.

This route is sharper geometrically but has a harder normalization obstacle: the row normalizers and the non-orthogonal `R` must be absorbed into a legitimate Gram/projection model.

## Recommendation to Driver / sibling mathematical lanes

1. Do **not** spend a successor task re-proving generic Bernstein total positivity, Pascal inversion, the Karlin composition formula, or the ordinary oscillatory-matrix theorem.
2. For the exterior-power lane, test whether the shared measure can manufacture the required proper cones after transporting the standard TP cones through `R`; the theorem to target is GSTP of the **full** `T_m`.
3. For the principal-angle lane, formulate the missing theorem as an exact Gram-normalization/similarity construction followed by `dim(U_m cap V_m)=1`, rather than as a vague “principal-angle analogy.”
4. The Jacobi Bernstein–Durrmeyer spectrum is a useful model/check, not a valid direct proof; arbitrary-weight theory explicitly warns that the special eigenspaces need not persist.
5. Preserve the existing negative controls: generic Bernstein structure can have repeated eigenvalue `1`; direct TN/entrywise-PF on `Q_m` is already blocked.

## Frozen artifacts

- `research_artifacts/PERFECT_PRIME_BETA_BERNSTEIN_PRIOR_ART_AUDIT/source_ledger.json`
- `research_artifacts/PERFECT_PRIME_BETA_BERNSTEIN_PRIOR_ART_AUDIT/claim_map.json`

No novelty, Working Truth, Foundation, or canonical-promotion authority is asserted by this audit.
