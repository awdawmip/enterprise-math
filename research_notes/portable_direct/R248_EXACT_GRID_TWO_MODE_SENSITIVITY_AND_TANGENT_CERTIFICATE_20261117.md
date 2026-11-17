# R248 — Certified positive two-mode sensitivity on the 21-point rational grid

Date: 2026-11-17 (Asia/Shanghai).
Evidence class: AUTHOR_DERIVED / EXACT_RATIONAL_CERTIFICATE_EXECUTED / NOT_REVIEWED.
Native BRC EffectHistogram: NOT_EXECUTED. Formal CLAIM, Result and Review: NONE.

## Provenance, scientific boundary and objective

This independent portable research continuation consumes R247's 21-point exact horizon theorem at scientific commit `c5fe805dba62a3a43c66fc033ed6b9a4f7368614` and its original frozen scientific input `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. It does not rebase the frozen input, alter P000 or claim a native X6/BRC source-integration result. The seven-source reversible sticky-reset chain here is an **auxiliary positive scalar observer**; labeled ports, signed branch provenance and cross-moment structure are outside its observation map.

The remaining R247 question is to determine whether the sharp finite-grid horizons 270 and 403 remain valid for **every real** `s` in the open interval `(39/100,41/100)`. R246 supplies a counterexample to general parameter monotonicity at event 126, so the derivative's sign needs an event-specific analysis rather than an assumption.

## Model and finite-grid theorem

Let `S21={j/1000:j=390,...,410}`, including the two analytic endpoint extensions. Use the unchanged R247 family

\[
t(s)=\frac{1691s-2615}{2615s-3539},\quad
a=(1/5,1/4,3/10,9/20,s,2/3,t(s)),\quad
b_0=13/60,\quad b_i=(5/18)|1/2-a_i|\ (i>0),
\]
\[
\pi_i=\frac{b_i}{1-a_i},\quad
Z=\sum_i\frac{b_i}{(1-a_i)^2},\quad
\rho_i=\frac{b_i}{Z(1-a_i)^2},\quad
P_{ij}=a_i\delta_{ij}+(1-a_i)\pi_j.
\]

For each of the 63 proper masks `m=0,...,62`, retain source 0 and the six other sources indicated by the bits. With `W=(144,576,1440,4320,17280,86400,518400)`, define

\[
\Phi_n(s)=\sum_{m=0}^{62}W_{\operatorname{popcount}(m)}\,
\rho_{D_m}^{\mathsf T}P_{D_m}^{n-1}\mathbf1.
\]

Let `r(s)` and `beta(s)` be the largest Perron eigenvalues for masks 59 and 55, and `A(s),B(s)` their positive spectral amplitudes as in R247. Define `X_n=A r^{n-1}+B\beta^{n-1}` and `E_n^{[2]}=\Phi_n/X_n-1`.

**Theorem R248 (exact finite-grid parameter sensitivities).** At each rational `s in S21`, the ordinary derivative with respect to real parameter `s` exists, and

\[
\boxed{\left.\frac{dE_{270}^{[2]}}{ds}\right|_s>\frac{63}{1000},\qquad
\left.\frac{dE_{403}^{[2]}}{ds}\right|_s>\frac1{100}.}
\]

At 39/100 and 41/100, "ordinary derivative" refers to the smoothly defined larger rational neighborhood (hence agrees with the one-sided derivative of the closed parameter restriction). This result is for 21 specified points; it does not establish positivity everywhere between them.

## Analytic derivative and certified interval proof

The rational function `t(s)` has derivative

\[
t'(s)=\frac{853776}{(2615s-3539)^2}.
\]

On the declared interval all seven `a_i,b_i,\pi_i,\rho_i` are differentiable, and the absolute-value branches of `b_i` are fixed. The transition derivative is exactly

\[
P'_{ij}=a_i'\delta_{ij}-a_i'\pi_j+(1-a_i)\pi_j'.
\]

For a mask `D`, write `z_0=\mathbf1,\;w_0=0` and iterate the **source-preserving tangent recurrence**

\[
z_{k+1}=P_D z_k,\qquad
w_{k+1}=P_D w_k+P_D' z_k.
\]

Thus \(\Phi_n'=\sum_DW_D\{(\rho_D')^{\!T}z_{n-1}+\rho_D^{T}w_{n-1}\}\) is rational at rational `s`. No numerical finite-difference approximation is needed. The executable uses the diagonal-plus-rank-one structure with integer-cleared denominators to compute both vectors in parallel, retaining all 63 mask contributions.

For either Perron root `lambda`, put

\[
f_D(\lambda,s)=\sum_{i\in D}\frac{b_i}{\lambda-a_i}-1=0,\quad
Q_D=\sum_{i\in D}\frac{b_i}{(\lambda-a_i)^2}>0,
\]

so implicit differentiation yields

\[
\lambda'=
\frac{\sum_{i\in D}\left[b_i'/(\lambda-a_i)+b_i a_i'/(\lambda-a_i)^2\right]}{Q_D}.
\]

Set \(S_D=\sum_{i\in D}b_i/[(1-a_i)(\lambda-a_i)]\). Then

\[
A_D=\frac{W_D S_D^2}{ZQ_D},\qquad
A_D'=A_D\left(2S_D'/S_D-Z'/Z-Q_D'/Q_D\right).
\]

These identities determine `X_n'`. Finally,

\[
\frac{dE_n^{[2]}}{ds}=\frac{\Phi_n'X_n-\Phi_nX_n'}{X_n^2}.
\]

At every grid point, the executable brackets each Perron root by **100 exact rational bisections** with checked opposite secular signs. It then evaluates `X_n` and `X_n'` using rational outward interval arithmetic, while `\Phi_n,\Phi_n'` are exact rational quantities. With `N=[\Phi_n'X_n-\Phi_nX_n']` the computed interval and `X^+` its positive upper bound, it verifies the strict exact inequalities

\[
\boxed{N^- - \frac{63}{1000}(X^+)^2>0\quad(n=270),\qquad
N^- - \frac1{100}(X^+)^2>0\quad(n=403)}
\]

for each of the 21 rational parameters. All **42 integer/rational comparisons PASS**. Since `X_n>0`, these prove the theorem.

## Reproducibility, evidence and scope

- [Executable exact certificate](R248_exact_two_mode_sensitivity_grid.py). Python 3 standard library only, `Fraction` interval endpoints, no floating point in PASS decisions. The local run completed 21/21 parameters, 42/42 derivative-floor inequalities, `PASS` in approximately 23 seconds.
- [All 42 margin digests](R248_verification_digest.csv). Each row gives the SHA-256 of the exact positive fraction written as `numerator/denominator` and numerator/denominator bit lengths. These digests are evidence fingerprints, not independent mathematical review.
- Full deterministic local verification JSON SHA-256: `5969e1817e8df48673844a477fc299f421afd0c01053062df62ee110d610ffc0` (regenerate by running the script in a writable working directory). Exact published script SHA-256: `8c5c790e26e0b8b7cf4e51573c69a85167234ab8cec4c8295adbb76f4773902f`.

For orientation only, the grid's *certified lower bounds* for the derivative range numerically from approximately 0.063669 to 0.090606 for event 270 and from 0.010700 to 0.025727 for event 403. The theorem uses the weaker rational lower bounds, not rounded diagnostics. The analytic identities apply across the real parameter interval, whereas the positivity checks only cover the 21 grid points.

## Remaining questions and owner boundary

**Next discriminating goal:** certify positivity of these same derivative expressions over the continuum, or rigorously bound the errors `E_270` and `E_403` by adaptive parameter intervals without assuming monotonicity. The 21 rational derivative certificates supply positive anchor witnesses and exact tangent machinery for Taylor/interval subdivision; they do not fill the gaps. A continuous-interval certificate, if obtained, could combine with R245's endpoint lower-threshold witnesses to prove the optimal **uniform real-parameter** horizons 270 and 403.

The complete exact output remains reproducible from the published script; its JSON has been retained as a run artifact, but only the digest certificate and program are GitHub-published here. This independent research note makes no formal Task CLAIM, PROGRESS, Result, Review or source-level BRC integration claim. Existing owners and their frozen pins are unchanged. Mathematical review remains NOT_REVIEWED.
