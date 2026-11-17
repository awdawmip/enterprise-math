# R749STH — Exact six-phase tail-fiber diameter, strict six-step contraction, and asymptotic residual hierarchy

Date: 2026-11-17. Evidence: `AUTHOR_EXACT_NOT_REVIEWED`. Frozen scientific model: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Continuation: R749STF@eaca9aae and R749STG@a673e3aa. This is an auxiliary five-labeled-source scalar observation theorem, not a native X6/BRC Port realization or shared Task acceptance.

## Model and exact question

Five distinctly labeled sources have weights `w=(1,1,2,3,6)`. Define

\[
\Omega_n=\{k\in\mathbb Z_{\ge0}^5:k_1+k_2+2k_3+3k_4+6k_5\le n-1\},\quad C_n=|\Omega_n|,\quad T_n=\sum_{k\in\Omega_n}k_1.
\]

Let `S(n)=18n^4+54n^3-345n^2+2070n-16315` and, for `e,d in [-2,2]`,

\[
Y_n(e,d)=n^3\frac{T_n+e}{C_n+d}-\frac{S(n)}{108}.
\]

Each state retains `(e,d)` throughout six-step future observations `n=q+6j`.

## Theorem A — Exact diameter and monotone six-step contraction

For every integer `n>=73`,

\[
\boxed{D_n:=\sup_{e,d,E,D\in[-2,2]}|Y_n(e,d)-Y_n(E,D)|
=\frac{4n^3(C_n+T_n)}{C_n^2-4}.}
\]

The extremal states are `(e,d)=(2,-2)` and `(E,D)=(-2,2)`. Furthermore

\[
\boxed{D_{n+6}<D_n\quad\text{for every integer }n\ge73.}
\]

**Exact diameter proof.** Since `C_n>2` and `T_n>2`, `Y_n` increases strictly with `e` and decreases strictly with `d`. The maximum and minimum on the compact square occur at the opposite corners above. Their difference simplifies to the displayed rational expression.

**Infinite monotonicity certificate.** Generating functions:

\[
\sum_{n\ge1} C_nz^{n-1}=\frac{1}{(1-z)^3(1-z^2)(1-z^3)(1-z^6)},\quad
\sum_{n\ge1} T_nz^{n-1}=\frac{z}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)}.
\]

Rewrite these as `Q_C(z)/(1-z^6)^6` and `Q_T(z)/(1-z^6)^7`; the integral numerator polynomials arise by multiplying finite blocks `1+z^w+...+z^{6-w}` and an extra factor `z` for the marked `T`. For each residue `r=0,...,5`, coefficient extraction produces exact rational quasi-polynomials `c_r(n)` of degree 5 and `t_r(n)` of degree 6, valid at every `n>=29` with `n mod 6=r`.

Let `A_r(N)=N^3(c_r(N)+t_r(N))`, `B_r(N)=c_r(N)^2-4`, and first indices `b_r=(78,73,74,75,76,77)` in residue order `r=0,...,5`. Set

\[
F_r(J)=\left[A_r(N)B_r(N+6)-A_r(N+6)B_r(N)\right]_{N=b_r+6J}.
\]

The accompanying exact Python/SymPy verifier reconstructs all six polynomial pairs from the generating functions, cross-checks integer recurrence counts, and verifies that **all six `F_r` have degree 18 with all 19 rational coefficients strictly positive** (114/114 strictly positive coefficients). Therefore `F_r(J)>0` for each integer `J>=0`. Since `B_r(n)>0` for `n>=73`,

\[
D_n-D_{n+6}=\frac{4F_r(J)}{B_r(n)B_r(n+6)}>0.
\]

This is a proof covering **all** integer `n>=73`, not a numerical sample.

## Theorem B — Uniform sharp asymptotic tail rate

The leading coefficients on all six quasi-polynomial branches coincide:

\[
C_n=\frac{n^5}{4320}+\frac{n^4}{144}+\frac{95n^3}{1296}+O(n^2),
\quad
T_n=\frac{n^6}{25920}+\frac{11n^5}{8640}+\frac{155n^4}{10368}+O(n^3).
\]

The remainders are uniform over the six residues. Direct rational Laurent expansion gives

\[
\boxed{D_n=\frac{2880}{n}-\frac{60480}{n^2}+\frac{847200}{n^3}+O(n^{-4}),
\qquad \lim_{n\to\infty}nD_n=2880.}
\]

The constant 2880 is sharp since both corner states attain `D_n` at **every** `n`. In particular, for any declared absolute observer resolution `\epsilon>0`, all sufficiently late readings merge the permitted nuisance-parameter square within that resolution. The exact diameter still strictly decreases at every six-step advance.

## Theorem C — Injective exact tails and two-scale residual hierarchy

For any `(e,d),(E,D) in [-2,2]^2` with the same cutoff/residue sequence, let `\Delta_e=e-E`, `\Delta_d=D-d`. Then

\[
\boxed{Y_n(e,d)-Y_n(E,D)
=\frac{720\Delta_d}{n}
+\frac{4320\Delta_e-19440\Delta_d}{n^2}
+\frac{-129600\Delta_e+341400\Delta_d}{n^3}+O(n^{-4}).}
\]

This expansion is uniform over the entire compact parameter box. The exact fraction identity

\[
Y_n(e,d)-Y_n(E,D)=
\frac{n^3[\Delta_e C_n+\Delta_d T_n+eD-Ed]}{(C_n+d)(C_n+D)}
\]

and Theorem B's leading coefficients prove it; the bilinear constant `eD-Ed` only contributes from `n^{-7}`, while denominator perturbations first contribute from `n^{-6}`.

Thus

\[
\lim_{n\to\infty}n[Y_n(e,d)-Y_n(E,D)]=720(D-d).
\]

If this limit vanishes (equivalently `D=d`), then

\[
\lim_{n\to\infty}n^2[Y_n(e,d)-Y_n(E,D)]=4320(e-E).
\]

Hence two states whose sufficiently late exact six-step observations all coincide necessarily have identical nuisance parameters. Any two different fixed-parameter states are eventually strictly ordered: first by `D-d`, and when that vanishes by `e-E`. The exact infinite tail is injective even while the fixed-resolution late-time fiber has vanishing diameter.

The mathematical conclusion concerns the **auxiliary five-source scalar observer**. A provenance-preserving native X6/BRC Port or Cell lifting remains an independent objective.

## Validation, provenance and next problems

Reproduce with `python R749STH_TAIL_DIAMETER_CERT.py` (Python 3 + SymPy), which regenerates `R749STH_TAIL_DIAMETER_RESULTS.json` with every one of the 114 rational coefficients, and independently checks the six residue formulas against integer recurrences and the universal Laurent coefficients. Author-side execution: `PASS 114/114`. Status: `AUTHOR_EXACT_NOT_REVIEWED`. The original frozen science pin, P000 and prior R749STF/G scientific proofs remain unchanged.

Next scientific questions: a provenance-preserving BRC Port/Cell representation of this two-rate tail signature under explicitly allowed future operations; five-read exact collisions to advance `5<=m_*<=11`; and a sharp five-read finite-noise separation radius for the (602,604) candidate pair.
