# CLASSICAL_RERUN — faithful Lane A reconstruction

Task: `RS-RHR-CLAUDE-RH-RERUN-20260811`  
Researcher-ID: `RHR-9Q6M2K`

This lane uses the candidates' ordinary continuous/analytic mathematics. Enterprise-Math precision assumptions are deliberately not used to attack the classical proof.

## A. Claude V6 — regulated square-difference coupling

### A1. Hilbert–Schmidt threshold

Under the source's weighted-to-unweighted isometry, the off-diagonal kernel is

\[
T_{mn}=|m^2-n^2|^{-\sigma}, \qquad m\ne n.
\]

Its squared Hilbert–Schmidt norm is

\[
\sum_{m\ne n}|m^2-n^2|^{-2\sigma}.
\]

Write \(m=n+k\), \(k\ge1\). Then

\[
m^2-n^2=k(2n+k).
\]

Thus, up to a factor 2 for the two orderings,

\[
\sum_{k\ge1}\sum_{n\ge1}
k^{-2\sigma}(2n+k)^{-2\sigma}.
\]

For fixed \(k\), comparison with an integral gives

\[
\sum_{n\ge1}(2n+k)^{-2\sigma}
\asymp k^{1-2\sigma}
\]

when \(\sigma>1/2\). Hence the total behaves like

\[
\sum_{k\ge1}k^{1-4\sigma},
\]

which converges iff \(\sigma>1/2\).

**Result:** Theorem B is reproduced.

### A2. Spectral growth after bounded/compact coupling

Let

\[
D=\operatorname{diag}(d_n),\qquad
d_n=n^4-c(u)n^2,
\]

and

\[
H=D+\gamma K.
\]

For \(\sigma>1/2\), \(K\) is Hilbert–Schmidt, hence bounded and compact. A bounded self-adjoint perturbation shifts ordered eigenvalues by at most \(O(\|K\|)\) at fixed index in the min–max comparison. Therefore

\[
\lambda_n(H)=n^4+O(n^2),
\]

so

\[
N_H(\Lambda)\sim \Lambda^{1/4}.
\]

### A3. Target zero count in the same spectral variable

The intended target is

\[
\lambda_n=\gamma_n^2+\frac14.
\]

By Riemann–von Mangoldt,

\[
N_\zeta(T)
=
\frac{T}{2\pi}\log\frac{T}{2\pi}
-\frac{T}{2\pi}+O(\log T).
\]

Thus the number of target eigenvalues \(\le\Lambda\) would be

\[
N_{\rm target}(\Lambda)
=
N_\zeta(\sqrt{\Lambda-1/4})
\sim
\frac{\sqrt{\Lambda}}{4\pi}\log\Lambda.
\]

The ratio

\[
\frac{N_{\rm target}(\Lambda)}{N_H(\Lambda)}
\asymp
\Lambda^{1/4}\log\Lambda
\to\infty.
\]

Therefore no exact multiplicity-preserving bijection can exist for this bounded-coupling realization.

**Result:** the direct Hilbert–Pólya eigenvalue route is rigorously closed.

This does **not** prove that every conceivable trace-formula or unbounded/prime-carrying modification fails. It proves that the locked bounded square-difference-kernel route cannot have the claimed exact spectrum.

### A4. Determinant bridge

The identity

\[
\det_\zeta(H-(z^2+1/4))=C\Xi(z)
\]

requires much more than self-adjointness:

- determinant definition and admissible regularization;
- divisor/zero-set equality;
- multiplicity;
- no extra zeros/poles;
- growth/order normalization;
- completeness.

The locked Claude V6 source itself marks this bridge OPEN and later records the square-difference-kernel determinant lane as closed-negative.

**Lane A status for Candidate A:** `SOURCE_FOUND_NOT_FULL_RH_CLAIM`.

---

## B. Gershon TP∞ route

### B1. Honest surviving starting point

The manuscript distinguishes strict log-concavity / TP2 from TP∞ and states that TP2 alone is not sufficient for RH. That distinction is correct.

Finite interval certificates are also finite statements; they are not rejected merely because they are computational.

### B2. Lemma 8 cannot be accepted as written

The required uniform bound is obtained by asserting that every level-\(s\) tilted potential inherits at least the base curvature:

\[
W_p^{(s)''}\ge W_p''.
\]

No derivation establishing this inequality for all relevant levels is given. The numerical check only covers a finite cached range.

**Classification:** `UNPROVED_LEMMA`.

### B3. Lemma 10 contradicts the entire generating function

The source defines

\[
g(z)=\sum_{m=0}^{\infty}\gamma_m z^m
\]

and calls \(g\) entire.

Cauchy–Hadamard gives

\[
\frac1R=\limsup_{m\to\infty}|\gamma_m|^{1/m}.
\]

Since \(R=\infty\),

\[
\limsup|\gamma_m|^{1/m}=0.
\]

Lemma 10 claims, from Hadamard factorization,

\[
\gamma_m
=
R_1\rho_1^m
+
R_2\rho_2^m
+
O(\delta_3^m\rho_1^m),
\]

where \(\rho_1=1/|z_1|>0\), \(\rho_2<\rho_1\), and \(\delta_3<1\).
For a nonzero leading residue \(R_1\), this implies

\[
\limsup|\gamma_m|^{1/m}=\rho_1>0,
\]

contradicting entire-ness.

The conceptual source of the mistake is exact: zeros of an entire function enter a **product** representation. Exponential sums from inverse zero locations arise naturally in partial fractions / reciprocal or logarithmic-derivative expansions, not as the Taylor coefficients of the entire function itself.

A finite algebraic stress test:
\[
g(z)=(1-z/2)(1-z/3)
=1-\frac56z+\frac16z^2.
\]
All coefficients after degree 2 vanish, while
\(R_1 2^{-m}+R_2 3^{-m}\) cannot vanish for every \(m\ge3\) unless \(R_1=R_2=0\).

**Classification:** `FALSE_LEMMA`.

### B4. Consequence

Lemma 10 is used in the spectral-gap reduction feeding Proposition 22 and the universal unitarity claim. Once it fails, the claimed extension from bounded certificates to all `r,n` is not established.

**Candidate B status:** `FAIL_AT_EXACT_LEMMA`.

---

## C. Yamaguchi spectral determinant route

Define

\[
F(z)=\xi(1/2+iz).
\]

The paper's Hadamard-rigidity proof writes

\[
F(z)=\xi(0)\prod_k(1-z^2/\gamma_k^2)
\]

by pairing the nontrivial zeta zeros as \(1/2\pm i\gamma_k\).

This is exactly the target condition. In general, a zero
\(\rho=\beta+i\gamma\) maps to

\[
z=\gamma-i(\beta-1/2).
\]

Unless \(\beta=1/2\), the corresponding zero of \(F\) is not real.

The correct unconditional entire-function factorization must run over the actual complex zeros of \(F\), paired under the functional-equation symmetries. Replacing that divisor by the real list \(\{\pm\gamma_k\}\) assumes what RH asks to prove.

**Classification:** `CIRCULARITY`.

Self-adjointness of \(J_\infty\) cannot repair this: a self-adjoint operator only helps after an independently established exact spectral/divisor identity.

**Candidate C status:** `FAIL_AT_EXACT_LEMMA`.

---

## D. Negative control

The CIPHER/RTSG public archive says its functional bridge reduces to `1=1` at zeta zeros through the functional equation, and records multiple failed routes.

Our circularity scan independently rejects such a bridge because a tautological functional-equation identity supplies no new zero-location constraint.

**Negative-control result:** `PASS` — verifier does not falsely certify a publicly failed AI proof.

---

## Lane A final mathematical result

No full RH proof chain is reproduced.

- Candidate A: no full proof was claimed; its direct spectral route is provably incompatible with the target zero count.
- Candidate B: exact FALSE_LEMMA at Lemma 10; earlier Lemma 8 is already unproved.
- Candidate C: exact circularity at the Hadamard divisor parameterization.
- Candidate D: expected failure detected.

No appeal to “community acceptance”, Clay status, or generic LLM unreliability is used in these conclusions.
