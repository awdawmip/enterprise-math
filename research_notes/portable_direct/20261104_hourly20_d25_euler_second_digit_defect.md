# D25: exact second-digit Euler truncation-defect formula for the 2304 Gauss observer

Date: 2026-11-04. Parent task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / TP2-B6F4FC938FF94941C1B7. Frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. This is **AUTHOR-DERIVED / EXACT ALGEBRAIC PROOF IN DECLARED SCOPE / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**, not the formal native continuation/claim.

This unit consumes the preceding proof in 20261104_hourly20_d25_frobenius_euler_degree_descent.md: for p=8q+5, F_p(z)=g(z)^N C(z) modulo p, where g=1-z/9, N=(p+1)/2, and C is the degree-q truncated Gauss (5/8,7/8). Unlike that earlier first-digit factorization, the present result explicitly determines the full **second-digit discrepancy polynomial**.

## Theorem (mod p^2 Euler discrepancy in the truncated polynomial ring)

Let p=8q+5 be any prime >=5 and let
\[
F_p(z)=\sum_{k=0}^{p-1}\frac{(1/8)_k(3/8)_k}{(k!)^2 9^k}z^k,\qquad
c_j=\frac{(5/8)_j(7/8)_j}{(j!)^2 9^j},\quad C(z)=\sum_{j=0}^q c_jz^j.
\]
The first-digit congruence permits a coefficientwise p-division
\[
E_p(z)=\frac{F_p(z)-(1-z/9)^{(p+1)/2}C(z)}p\pmod p,
\]
a polynomial of degree <p. All coefficient denominators up to degree p-1 are p-units. Define in the finite ring \(A_p=\mathbb F_p[z]/(z^p)\)
\[
h(z)=\sum_{n=0}^{p-1}\binom{1/2}{n}(-z/9)^n,\quad
\ell(z)=-\sum_{n=1}^{p-1}\frac{z^n}{n9^n},
\]
and the explicit middle-carry polynomial
\[
R(z)=\sum_{j=q+1}^{3q+1} \overline{c_j/p}\,z^j.
\]
Then the **exact finite-field second-digit identity** is
\[
\boxed{E_p(z)=h(z)\bigl[R(z)-\tfrac12 C(z)\ell(z)\bigr]\quad\text{in }A_p.}
\]
The first nonzero middle-carry coefficient is fixed by the original Gauss recurrence:
\[
\boxed{[z^{q+1}]R=\gamma_p=\frac{\bar c_q}{288(q+1)^2}\in\mathbb F_p^\times.}
\]
For \(q+1<j\le3q+1\), its coefficients obey the ordinary reflected Gauss ratio
\[
R_j=R_{j-1}\frac{(8j-3)(8j-1)}{576j^2}\pmod p.
\]
For j>=3q+2 and j<p, c_j is divisible by p^2 and contributes no second-digit middle carry. This includes p=5, q=0: R has just the j=1 term.

### Exact proof

Euler's ordinary hypergeometric identity over Q gives, coefficientwise at indices below p,
\[
F_p(z)\equiv g(z)^{1/2}\sum_{j=0}^{p-1}c_jz^j\pmod{z^p}.
\]
The factor \(5/8+q=p/8\) occurs when creating c_{q+1}, and \(7/8+(3q+1)=3p/8\) occurs when creating c_{3q+2}. The integer factorial denominators stay prime to p for j<p. Consequently, modulo p^2 and z^p, the transformed coefficient sequence is \(C+pR\).

In the same finite-degree ring the formal logarithm is p-integral and satisfies
\[
g^{(p+1)/2}=g^{1/2}\exp\bigl(\tfrac p2\log g\bigr)
\equiv g^{1/2}\bigl(1+\tfrac p2\log g\bigr)\pmod{p^2,z^p}.
\]
All denominators needed for degrees <p are p-units; powers beyond degree p-1 are discarded *before* any evaluation. Subtract \(g^NC\), divide coefficientwise by p, and reduce modulo p to obtain the boxed formula. The displayed \(\gamma_p\) is the first-divisible-parameter step of the exact recurrence
\[
c_{q+1}=c_q\frac{p(p+2)}{576(q+1)^2}.
\]
This proves the formula for all p in the specified class.

## Observer consequences and exact execution

The BRC source-resolved second-digit port is the ordered pair \((E_p(1),(\theta E_p)(1))\in\mathbb F_p^2\), computed **after taking the degree-<p quotient**, never by applying an infinite analytic logarithm at z=1. In particular, the complete vector provides exactly the two p-adic correction coordinates needed to compare F_p(1) and its weighted derivative with \(g(1)^NC(1)\) and the first-digit formula involving C'(1). The separate contributions are middle carry \(hR\) and binomial exponent deformation \(-\frac12hC\ell\).

The accompanying code independently constructs original and reflected Gauss coefficients modulo p^2, the finite half-power and logarithm modulo p, and checks every coefficient of E_p against the boxed convolution. It tests the first carry \(\gamma_p\) and the two observer values. Executed: **PASS all 79 primes p<=2000 with p mod8=5; 72,931 coefficient checks**.

Representative exact results \((p,q,E_p(1),\theta E_p(1))\) modulo p:
\[
(5,0,3,0),\ (13,1,9,6),\ (29,3,5,24),\ (37,4,12,31),\
(53,6,23,9),\ (61,7,34,41),\ (373,46,119,71).
\]

## Next smallest question and preserved control status

Use the two **separate** correction sources to derive a class-selected finite identity at z=1, showing that the original selected factor \(S=F_p(1)\) (p mod24=13) or \(Y=(1+16\theta)F_p(1)\) (p mod24=5) vanishes modulo p^2. The present identity proves the exact discrepancy for all p=8q+5 but does not itself prove that class-specific cancellation. Compare the resulting criterion with earlier Jacobi harmonic/one-seam and native original-class D24 evidence without copying those completed proofs.

Canonical native continuation rhourly20-20261104-1923-cont-read: SUCCEEDED at Source 3645861db6452777b473a94c7938cc903a962a89; preserved SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED native frontier, route REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION, execution_authorized=false. Protected old session/staging was not changed. Native p373 H0/B0, [X]U and Delta-R are pending in their exact earlier roles. This author artifact is not a native checkpoint, Result or mathematical admission.


## Corollary: exact scalar certificate for the selected second-digit zero

All C-values in this paragraph are taken from their **original p-adic rational coefficients modulo p^2**, while E-observations are the finite-polynomial residues just proved. Set \(u=(8/9)^N\), with \(N=(p+1)/2\), and let \(e_0=E_p(1)\), \(e_1=(\theta E_p)(1)\) modulo p. For the previously observed p mod24 class selector, the following are **if-and-only-if arithmetic certificates**, not assumptions of their own vanishing:

If \(p\equiv13\pmod{24}\) and \(C(1)\equiv0\pmod p\), then
\[
\boxed{F_p(1)\equiv0\pmod{p^2}\ \Longleftrightarrow\
u\,\frac{C(1)}p+e_0\equiv0\pmod p.}
\]

If \(p\equiv5\pmod{24}\) and \(C'(1)\equiv0\pmod p\), then
\[
\boxed{(1+16\theta)F_p(1)\equiv0\pmod{p^2}\ \Longleftrightarrow\
u\left(16\frac{C'(1)}p-C(1)\right)+e_0+16e_1\equiv0\pmod p.}
\]

Proof: at z=1, \(F_p=g^NC+pE_p\) modulo p^2. The first statement follows by evaluation. For the second, apply \(1+16\theta\) **before** evaluating at z=1: since \(1-16N/8=1-2N=-p\) exactly, the transformed term is \(u(16 C'(1)-pC(1))\). Subtract and divide by p. Both equivalences preserve all exact divisibility hypotheses. They reduce the selected second-digit question to a single, explicit finite-field cancellation.

Exact evaluated source pairs (baseline term, discrepancy term), whose sum is 0 modulo the displayed p, are: p=5 (2,3), p=13 (4,9), p=29 (17,12), p=37 (25,12), p=53 (45,8), p=61 (27,34), p=373 (254,119). These are examples, not a uniform proof of class selection or cancellation.

Next proof target is now sharply stated: prove the boxed right-hand sides vanish on their specified residue classes using a finite Jacobi/CM/WZ symmetry of C, R and the truncated logarithm. Do not replace this exact arithmetic identity by an analytic logarithm evaluated at z=1 or by a bare scalar total that loses its two BRC source ports.
