# R762HZ — Exact relative second correction for signed Port/BRC zero returns

Date: 2026-11-21. Scope: the frozen six-axis **composite Port candidate** of R762HX/R762HY, not native `TRIADIC_CLOSURE_E` admission. Frozen scientific input: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Status: `AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / NOT_REVIEWED`. The six dominant saddle classification and spectral separation from R762HX remain an **unreviewed antecedent**.

## New theorem

Write `K_m(p)` for the number of ordered, rooted, signed Port walks of length `m` returning to the initial Port `p` with zero signed X6 Cell displacement, each ordered edge transition and sign retained. For odd `m`, `K_m(p)=0`. Along even `m → ∞`, conditional on the R762HX six-saddle/spectral-gap lemma,

\[
\boxed{K_m(p)=\frac{10\sqrt5}{27\pi^3}\frac{16^m}{m^3}
\left(1+\frac{19}{6m}+\frac{9209}{360m^2}+O(m^{-3})\right).}
\]

The new coefficient `9209/360` is an exact rational number and independent of the root `p`. The preceding `19/6` is reproduced independently by the present rational-Gaussian computation. These are *asymptotic* corrections; the finite-`m` error constant and a uniform finite-`m` application threshold have not been certified.

## Derivation

The fifteen Ports are the two-element subsets of `{0,...,5}`. Adjacent Ports meet in exactly one axis. For adjacent `p,q`, let `h_{p∪q}` be their three-axis incidence vector. Set
\[
B(u)_{pq}=\begin{cases}\frac18\cos\langle u,h_{p\cup q}\rangle,&|p\cap q|=1,\\0,&\text{otherwise},\end{cases}
\quad A=B(0),\quad J=\tfrac1{15}{\bf1}{\bf1}^{T}.
\]
This real Fourier observer is derived from the positive, source-labeled BRC count; it is not a signed-weight primitive. The adjacency spectrum is `1` (one), `1/4` (five), `-1/4` (nine), hence the reduced resolvent
\[
R=(I-A)^{-1}_{\mathbf1^\perp}=\frac{16}{15}(I+A-2J).
\]
Writing `s=t²` and `x_{pq}=⟨u,h_{p∪q}⟩`, expand `B(tu)=A+sC+s²D+s³E+O(s⁴)`, with adjacent-edge entries `C=-x²/16`, `D=x⁴/192`, `E=-x⁶/5760` (zero elsewhere). Let `f=1/√15·1` and `λ=1+sλ₂+s²λ₄+s³λ₆+O(s⁴)` be its simple leading eigenvalue. Ordinary eigenvector perturbation with `fᵀv=1` gives the exact polynomial identities
\[
\begin{aligned}
\lambda_2&=f^TCf,\\
\lambda_4&=f^TDf+f^TCRCf,\\
\lambda_6&=f^TEf+2f^TDRCf+f^TCRCRCf-\lambda_2f^TCR^2Cf.
\end{aligned}
\]
All are homogeneous symmetric polynomials in the six components of `u` of degrees 2, 4, 6 respectively. The finite S6 action permutes Ports, so the corresponding invariant spaces have dimensions 2, 5, 11. The checker obtains their coefficients in the power-sum partition basis from exact full-rank rational evaluation matrices; this is a **complete polynomial identity reconstruction**, not a fit to an asymptotic sequence.

The covariance from R762HX is `Σ=(3/10)I+(1/5)11ᵀ`, with `Σ^{-1}=(10/3)I-(4/9)11ᵀ` and `Q(u)=uᵀΣu=-2λ₂(u)`. Put
\[
T_4=\lambda_4-\frac{Q^2}{8},\qquad
T_6=\lambda_6+\frac{Q\lambda_4}{2}-\frac{Q^3}{24}.
\]
Then
\[
m\log\lambda(m^{-1/2}u)
=-\frac{Q}{2}+\frac{T_4}{m}+\frac{T_6}{m^2}+O(m^{-3}\|u\|^8),
\]
and the integrand's relative second coefficient is `T₆+T₄²/2`.

Let `U~N(0,Σ^{-1})`. Exact multivariate Wick recurrence (implemented in the checker, no sampling) gives:

| Exact Gaussian expectation | Value |
|---|---:|
| `E[λ₆]` | `-1921/90` |
| `E[Q λ₄]` | `275/3` |
| `E[Q³]` | `480` |
| `E[λ₄²]` | `13631/60` |
| `E[λ₄ Q²]` | `1100` |
| `E[Q⁴]` | `5760` |
| `E[T₄]` | `19/6` |
| `E[T₆]` | `202/45` |
| `E[T₄²]` | `2531/60` |

Consequently
\[
\boxed{\mathbb E[T_6+T_4^2/2]
=\frac{202}{45}+\frac{2531}{120}
=\frac{9209}{360}.}
\]

R762HX identifies exactly six maximal-modulus saddle points on the six-torus with a spectral gap outside their neighborhoods. Near any one the simple branch is analytic and even, while the global Port-root permutation symmetry makes its trace amplitude exactly one. Standard local Gaussian rescaling with the uniform eighth-order analytic expansion, plus the gap on the complement, yields the stated relative `O(m^{-3})` remainder. For even `m`, the six saddle contributions agree. The leading constant is exactly the previously proved R762HX value.

## Reproducibility and evidence boundary

`R762HZ_CHECK.py` reconstructs all perturbation coefficients from the actual fifteen-state Port matrix, proves full rank of the 2-, 4- and 6-degree symmetric power-sum evaluation systems, checks four additional independent test directions per degree, expands the resulting six-variable polynomials, and applies a memoized multivariate Gaussian Wick recursion over rational arithmetic. Execution returned `PASS R762HZ` with the rational values above. Numerical eigensolver spot checks in three directions also agreed with the sixth-order eigenvalue series within floating-point rounding; those checks do not replace the exact certificate.

The infinite-length conclusion depends on R762HX's continuous six-saddle classification and gap, which this unit has not independently proved or reviewed. The new rational coefficient and perturbation identities have a standalone reproducible algebraic certificate. No finite-data regression was used and no original P000 native triadic force event is claimed.

## Continuation

A worthwhile next unit is either (a) independently audit the six-saddle spectral classification and the analytic remainder at the degree-eight expansion, or (b) develop the unresolved *single-histogram* Port Euler/sign-balance problem: find a legitimate `N_p(n)>0` and coordinate-even `H(n)` with `C(n)=0`, or prove no such source exists. Retain Port order, source multiplicity, observer limitations, the current owner boundary, and the frozen P000 pin.
