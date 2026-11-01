# D25 / SECOND-DIGIT-LIFT — exact divided-Frobenius coefficient transport

Date: 2026-11-01 09:00 Asia/Hong_Kong. **AUTHOR-SIDE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_NOT_RUN.** This is not a native Source Result, review, CLAIM, or executed H0/B0 benchmark.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3. Research logical lane: chatgpt-research-onhour-enterprise-math-20260923 (not CONTROL_PLANE_MAINTENANCE). The exact Jacobi two-shift congruence in 20261101_onhour_d25_jacobi_two_shift_p13.md is reused, not reproved or claimed anew.

## Exact new two-port Frobenius-carry theorem

For any prime \(p>7,\;p\equiv5\bmod8\), write

\[
a=\frac{5p-1}{8},\qquad b=\frac{7p-3}{8},\qquad \lambda=\frac19,\qquad0<a<b<p.
\]

Define the finite **single source polynomial**

\[
P_p(t)=(1+t)^a(t+\lambda)^b,\qquad J=[t^b]P_p(t),
\]

with coefficient extraction \([t^r]\). For nonnegative integer arguments, let

\[
K_n(x)=\sum_{k=0}^n\binom nk\binom xk\lambda^k.
\]

The binomial theorem directly gives the exact rational identities

\[
\begin{aligned}
J&=K_a(b)=K_b(a),\\
K_b(a+p)&=[t^b]P_p(t)(1+t)^p,\\
K_a(b+p)&=[t^{b+p}]P_p(t)(t+\lambda)^p.
\end{aligned}\tag{1}
\]

The **different extraction indices \(b\) and \(b+p\)** are essential to retaining the two original parameter/source ports.

The divided Frobenius polynomials are

\[
E_1(t)=\frac{(1+t)^p-1-t^p}{p},\qquad
E_\lambda(t)=\frac{(t+\lambda)^p-t^p-\lambda^p}{p}.
\]

Both belong to \(\mathbb Z_{(p)}[t]\) because \(\binom pk\) is divisible by \(p\) for every \(1\le k<p\); division by \(p\) occurs in the integer/p-local coefficient ring, **not inside \(\mathbb F_p\)**. Keep the two signed provenance ports

\[
C_1=[t^b]P_p(t)E_1(t),\qquad
C_\lambda=[t^{b+p}]P_p(t)E_\lambda(t).
\]

Using \(b<p\) and \(\deg P_p=a+b<b+p\) in (1) establishes the **exact equalities in \(\mathbb Z_{(p)}\)**

\[
\boxed{K_b(a+p)=J+pC_1,\qquad K_a(b+p)=J+pC_\lambda.}\tag{2}
\]

The exactness (rather than just equality modulo \(p^2\)) is this unit's useful new coefficient/Frobenius interface. It requires no conjectural CM input or new axiom.

Consume the **earlier author-derived** Jacobi two-shift relation, retaining its exact proof level:

\[
8G_{\beta,p}\equiv20J-5K_b(a+p)-7K_a(b+p)\pmod{p^2},
\quad
G_{\beta,p}=\sum_{k=0}^{p-1}\frac{(1/8)_k(3/8)_k}{9^k(k!)^2}.
\]

It follows that

\[
\boxed{8G_{\beta,p}\equiv8J-p(5C_1+7C_\lambda)\pmod{p^2}.}\tag{3}
\]

Equivalently the *terminal scalar only* has a one-coefficient representation:

\[
\boxed{
8G_{\beta,p}\equiv[t^{b+p}]P_p(t)
\left[20t^p-5t^p(1+t)^p-7(t+\lambda)^p\right]\pmod{p^2}.}\tag{4}
\]

Modulo \(p\), the two different Frobenius sources reduce to a pair of finite-log kernels:

\[
E_1(t)\equiv\sum_{k=1}^{p-1}(-1)^{k-1}\frac{t^k}{k},\quad
E_\lambda(t)\equiv\lambda\sum_{k=1}^{p-1}(-1)^{k-1}\frac{(t/\lambda)^k}{k}.
\]

This is the **p13 Jacobi parameter-shift coefficient transport**, distinct from GH98/GH99's previously recorded, differently sourced reflected-Green finite-log trace; no duplicate discovery or claim of their approval is made.

## The exact remaining p13 cancellation

For \(p\equiv13\bmod24\), consume the prior *mod-p only* CM selector \(J\equiv G_{\beta,p}\equiv0\bmod p\). Then (3) yields the proven equivalence

\[
\boxed{G_{\beta,p}\equiv0\pmod{p^2}
\iff8(J/p)\equiv5C_1+7C_\lambda\pmod p.}\tag{5}
\]

The all-prime vanishing on either side **is not proved**. It is now a coefficient-symmetry/CM problem involving one finite polynomial \(P_p\) and **two** Frobenius defect ports, not a requirement to recompute the existing Jacobi Taylor or three-source harmonic decomposition. The quotient \(J/p\) is p-integral only in the stated p13 class, not for all p≡5 mod8.

## Actual exact independent checks

Executable standard-library source: research_notes/portable_direct/d25_p13_frobenius_coefficient_port_20261101.py, Git blob **04c859cec358b33eb55de0c91c505172b3565096**. Executed code independently uses (i) original beta Pochhammer recurrence, (ii) integer-binomial Jacobi shifts, (iii) unshifted polynomial coefficient convolution, and (iv) exact divided-binomial Frobenius extraction. All **23 primes \(p\le500,\;p\equiv5\bmod8\)** passed (3); all six selected primes \(13,29,37,61,109,373\) passed both exact independent coefficient ports.

The source readouts are p-local integers reduced modulo \(p^2\), and \(C_1,C_\lambda\) reduced modulo p.

| p | J | K_b(a+p) | K_a(b+p) | C1 | Cλ | Gβ mod p² |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 104 | 91 | 39 | 12 | 8 | 0 |
| 29 | 403 | 780 | 26 | 13 | 16 | 287 |
| 37 | 555 | 740 | 666 | 5 | 3 | 0 |
| 373 | 27975 | 30586 | 77957 | 7 | 134 | 0 |

At p13, \(8(J/p)=64\equiv12=5\cdot12+7\cdot8\pmod{13}\). At p373, \(8(J/p)=600\equiv227=5\cdot7+7\cdot134\pmod{373}\). **p29 is a negative control**: \(J\bmod29=G_{\beta,29}\bmod29=26\ne0\); J/p is not valid there. These finite results are NOT a proof of (5) for infinitely many p13.

BRC resolution: **COMPOSE_APPLIED** on exact integer/rational coefficient carriers, separately labeled \(C_1,C_\lambda\), p-adic valuations, and the declared terminal mod-\(p^2\) Gauss observer. Scalar (4) is not a lossless quotient for future derivative, signed cutoffs or provenance observations. Ordinary polynomial Frobenius is **not** native Heartbeat X6, H0/B0 semilinear Frobenius or the missing original p373 divided-power experiment.

## Unfinished mother and recovery packet

Original LIFT mother is \(\Delta_p-R_p=0\bmod p\), equivalent to \(A_p\equiv p\bmod p^3\) for primes \(p\equiv13,19\bmod24\). This remains OPEN; so does the stronger experimental p4 affine bridge. The exact next mathematical operation is a genuinely CM-compatible coefficient symmetry proving/refuting (5), with both \(C_1,C_\lambda\) protected, followed by the original 216 signed cutoff \(R_p\). Do not repeat D24 UR, the earlier Jacobi two-shift, p19 Hensel digits, or completed high-valuation port reflections.

**Native benchmark remains an independent higher-priority debt:** existing issue #1559 requires at \(p=373\) the same-original-class H0/B0 divided-power \([X]U\bmod139129\), module rank, true semilinear Frobenius direction/normalization eta, original signed odd Hesse/Green, same-definition κ and independent reproduction. PENDING_OWNER/NOT_RUN. Responsible path is the authorized canonical Source Task/native evaluator owner or implementation maintainer. Acceptance requires actual raw reproducible original data and independent validation; this polynomial checker is not a substitute.

Current Gateway 0.6.11 reports no Source Research write authority or executor binding for this client. Own checkpoint read: ACCESS_DENIED. Original request research-onhour-20261031-0205-dispatch-r15 lookup: CONTROL_REQUEST_NOT_FOUND in this client's scope; no replay, new CLAIM/session/open/run, Source checkpoint, freeze, review or admission claimed. Three prior staging sources remain independent. Preserve scientific Source pin, P000/ACTIVE worldview, scheduling and notification settings. **REGISTER_PENDING / SYNC_DEBT until separately authorized Source execution path is real.**
