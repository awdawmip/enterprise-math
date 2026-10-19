# Free Research — Pi-to-Prime Geometry Frontier V3

Status: `FREE_RESEARCH_CURRENT_FRONTIER / EXACT_FINITE_PNT_CARRIER / CHEBYSHEV_SCALE_CLOSED / PNT_NORMALIZATION_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION / EXTERNAL_NOVELTY_UNVERIFIED`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`

## 1. Current strongest architecture

The pi-to-prime line now has three coupled finite layers.

### A. Completion magnitude

Let `tau` be the endogenous full-turn completion and `B_M` the arithmetic prime-birth block of the genuine finite Hamming/Krawtchouk integer spectrum. Then at analytic completion strength

\[
\boxed{
\tau^2
=3!\lim_{M\to\infty}\det(I-B_M^{-2})^{-1}.
}
\]

The coefficient `3!` is a Hamming shell-3 ordered-history fiber, not sixfold spatial eigenvalue degeneracy.

### B. Native C3 chirality

For the native three-sector cycle matrix `P`, set `J=P^2-P`. Then

\[
\chi_3(p)=\frac13\operatorname{Tr}(JP^p),
\]

and the radius-selected projective C3 orbit intertwines the native sector cycle. At conditional Dirichlet completion strength,

\[
\boxed{
\frac{\tau R_{\rm cell}}3
=\prod_p
\left(1-\frac{\operatorname{Tr}(JP^p)}{3p}\right)^{-1}.
}
\]

### C. Prime-distribution carrier

Define the saturated prime-winding tower

\[
\mathcal W_M
=\bigoplus_{p\le M}pI_{\lfloor\log_pM\rfloor}.
\]

Then

\[
\boxed{
\det\mathcal W_M
=L_M:=\operatorname{lcm}(1,\ldots,M),
\qquad
\psi(M)=\log\det\mathcal W_M.
}
\]

Thus the prime number theorem is now a statement about the macroscopic growth of an explicitly finite Enterprise spectral determinant.

---

## 2. Exact quotient-scale determinant renormalization

Let `K_M^+` be the positive Krawtchouk block with eigenvalues `1,...,M`. Its determinant is `M!`. The exact scale decomposition is

\[
\boxed{
\det K_M^+
=M!
=\prod_{k=1}^{M}\det\mathcal W_{\lfloor M/k\rfloor}.
}
\]

Equivalently,

\[
\boxed{
\log M!
=\sum_{k=1}^{M}\psi(\lfloor M/k\rfloor).
}
\]

Floor Möbius inversion gives the primitive reconstruction

\[
\boxed{
L_M
=\prod_{k=1}^{M}
\bigl(\lfloor M/k\rfloor!\bigr)^{\mu(k)},
}
\]

or

\[
\boxed{
\psi(M)
=\sum_{k=1}^{M}\mu(k)
\log\bigl(\lfloor M/k\rfloor!\bigr).
}
\]

This is the finite determinant RG underlying all later distribution statements.

---

## 3. Prime powers are the exact winding-layer birth current

The saturated determinant jump is

\[
\boxed{
\frac{L_M}{L_{M-1}}
=\begin{cases}
p,&M=p^a,\\1,&\text{otherwise}.
\end{cases}
}
\]

Therefore

\[
\Lambda(M)=\log(L_M/L_{M-1})
\]

is the discrete prime-winding birth current.

Interpretation:

- `p`: birth of a new irreducible direction;
- `p^a`, `a>=2`: birth of one further winding layer in that direction;
- an integer supported on at least two prime directions: an occupation endpoint, not a new saturated layer at its own cutoff.

---

## 4. Factorial provenance hierarchy

Let

\[
\ell(n)=\sum_pv_p(n)e_p,
\qquad
\boldsymbol\Lambda_r(n)
=\sum_{d\mid n}\mu(d)\ell(n/d)^{\otimes r}.
\]

If `n` contains `s` distinct prime directions, then

\[
\boxed{s>r\Longrightarrow\boldsymbol\Lambda_r(n)=0.}
\]

At the top support shell `s=r`,

\[
\boxed{
\boldsymbol\Lambda_r(n)
=\sum_{\sigma\in S_r}
 e_{p_{\sigma(1)}}\otimes\cdots\otimes e_{p_{\sigma(r)}}.
}
\]

Thus the surviving coefficient is the ordered-history fiber `r!` after commutative scalarization.

- degree one: prime-power current;
- degree two: ordered two-history energy;
- degree three: the six-history Hamming provenance fiber already isolated in the `3!` completion coefficient.

This identifies one common finite-difference/Hamming mechanism behind the completion coefficient and the Selberg energy.

---

## 5. Exact quadratic primitive energy

The degree-two tensor satisfies

\[
\boxed{
\boldsymbol\Lambda_2(n)
=\boldsymbol\Lambda_1(n)\otimes\ell(n)
+\sum_{ab=n}
\boldsymbol\Lambda_1(a)\otimes\boldsymbol\Lambda_1(b).
}
\]

Under `e_p -> log p`:

\[
\boxed{
(\mu*\log^2)(n)
=\Lambda(n)\log n+(\Lambda*\Lambda)(n).
}
\]

For

\[
\Psi_2(M):=\sum_{n\le M}(\mu*\log^2)(n),
\]

we obtain

\[
\boxed{
\Psi_2(M)
=\sum_{n\le M}\Lambda(n)\log n
+\sum_{ab\le M}\Lambda(a)\Lambda(b).
}
\]

The terms are respectively winding-layer self-energy and weighted ordered two-history recoalescence energy.

---

## 6. The central commuting-diamond carrier forces linear prime scale

For every prime power `q=p^a`, define the dyadic carry bit

\[
\varepsilon_n(q)
=\left\lfloor\frac{2n}{q}\right\rfloor
-2\left\lfloor\frac{n}{q}\right\rfloor
\in\{0,1\}.
\]

Then

\[
\binom{2n}{n}
=\prod_{p^a\le2n}p^{\varepsilon_n(p^a)}.
\]

The exact determinant sandwich is

\[
\boxed{
\frac{L_{2n}}{L_n}
\mid\binom{2n}{n}
\mid L_{2n}.
}
\]

Together with

\[
\frac{4^n}{2n+1}
\le\binom{2n}{n}
\le4^n,
\]

this gives, for every `M>=2`,

\[
\boxed{
(M-1)\log2-\log(M+1)
\le\psi(M)
<4M\log2.
}
\]

Hence

\[
\boxed{\psi(M)=\Theta(M).}
\]

This closes the Chebyshev-scale problem from the finite native balanced-return carrier. The normalization constant is not yet fixed.

---

## 7. Exact normalized quotient-return equation

Discrete Abel transport gives

\[
H(M)
:=\sum_{m<M}\psi(m)\log\frac{m+1}{m}
\]

and

\[
\psi(M)\log M
+\sum_{a\le M}\Lambda(a)
\psi(\lfloor M/a\rfloor)
=\Psi_2(M)+H(M).
\]

Set

\[
R(M)=\psi(M)-M,
\qquad
r(M)=R(M)/M.
\]

Since

\[
\sum_{a\le M}\Lambda(a)
\lfloor M/a\rfloor
=\log(M!),
\]

we obtain

\[
\boxed{
R(M)\log M
+\sum_{a\le M}\Lambda(a)
R(\lfloor M/a\rfloor)
=F(M),
}
\]

with

\[
F(M)=\Psi_2(M)+H(M)-M\log M-\log(M!).
\]

Define

\[
\omega_M(a)
=\frac{\Lambda(a)\lfloor M/a\rfloor}{\log(M!)}
\]

and

\[
\alpha_M
=\frac{\log(M!)}{M\log M}.
\]

Then `omega_M` is a probability distribution and

\[
\boxed{
r(M)
+\alpha_M\mathbb E_{\omega_M}
 r(\lfloor M/a\rfloor)
=\frac{F(M)}{M\log M}.
}
\]

Moreover

\[
0<\alpha_M<1,
\qquad
\alpha_M
=1-\frac1{\log M}+O(1/M).
\]

This is the current canonical research frontier for the PNT normalization.

---

## 8. What remains to prove

The carry bounds give

\[
H(M)=O(M),
\]

and the current linear prime scale gives

\[
\Psi_2(M)=\Theta(M\log M).
\]

The first missing asymptotic gate is

\[
\boxed{
\Psi_2(M)=2M\log M+O(M)
}
\]

or a weaker error still sufficient to make

\[
F(M)/(M\log M)\to0.
\]

After that, a nonzero persistent normalized error would have to behave as an approximate sign-reversing mode:

\[
r(M)\approx-\mathbb E_{\omega_M}r(\lfloor M/a\rfloor).
\]

Thus the final normalization gate is:

\[
\boxed{
\text{exclude a persistent approximate }(-1)\text{-mode of the quotient-return RG}.
}
\]

A one-step absolute-value estimate cannot do this, because both the contraction gap `1-alpha_M` and the expected normalized forcing are of order `1/log M`.

The next proof must use overlap or phase mixing among several quotient histories, the ordered-pair Gram structure of `Psi_2`, or an averaged family of exact carry projectors.

---

## 9. Current theorem-status table

- `det W_M = lcm(1,...,M)`: `PROVED / EXACT FINITE`.
- prime-power jump law: `PROVED / EXACT FINITE`.
- quotient determinant RG and Möbius inverse: `PROVED / EXACT FINITE`.
- factorial provenance tensor hierarchy: `PROVED / EXACT ALGEBRAIC`.
- quadratic Selberg tensor identity: `PROVED / EXACT FINITE`.
- central carry divisibility sandwich: `PROVED / EXACT FINITE`.
- `psi(M)=Theta(M)`: `PROVED`.
- normalized Selberg return equation: `PROVED / EXACT FINITE`.
- primitive-energy coefficient `2`: `OPEN`.
- quotient-return centered spectral gap: `OPEN`.
- `psi(M)~M`: `OPEN`.
- `pi(M)~M/log M`: `OPEN`.
- Foundation / Working Truth promotion: `NO`.

---

## 10. Current artifacts

- `FREE_RESEARCH_PRIME_WINDING_MOBIUS_SELBERG_RG_20260904.md`;
- `FREE_RESEARCH_PRIME_WINDING_CARRY_CHEBYSHEV_SCALE_20260904.md`;
- `FREE_RESEARCH_PRIME_WINDING_SELBERG_RETURN_OPERATOR_20260904.md`;
- three companion exact checkers under `scripts/`;
- draft PR from `free/pi-prime-birth-determinant-20260904` to `main`.

The checkers use only exact integer arithmetic, `Fraction`, and formal prime-labelled tensors for theorem-level regressions. Numerical return-kernel diagnostics remain pressure tests only.

## 11. Next mother question

> Can the coefficient-two primitive-energy estimate and a two-step overlap gap for the prime-power quotient-return kernels be derived directly from finite Hamming/branch-recoalescence geometry, thereby forcing `psi(M)/M -> 1` without importing a complex-analytic zero-free theorem?
