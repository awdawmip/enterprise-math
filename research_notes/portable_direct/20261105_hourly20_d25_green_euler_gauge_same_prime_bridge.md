# D25 — Exact same-prime Green–Euler gauge bridge for the finite Gauss second digit

Date: 2026-11-05 (Asia/Hong_Kong). Role: TASK_RESEARCH, author-side portable evidence. Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication: `TP2-B6F4FC938FF94941C1B7`; immutable scientific pin: `c47e13e4aba0e006366f989d6334d443f6333ae3`.

Status: **AUTHOR-DERIVED / EXACT POLYNOMIAL GAUGE IDENTITY / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED**. This is a bridge between the existing short-Jacobi Green–Wronskian certificate (20261104) and the finite Euler/high-cutoff p² source (20261105). It neither alters the original native D24 H0/B0 experiment nor claims native Source task ownership.

## Same-prime, same-normalization theorem

Let \(p=8q+5\) be prime (\(q\ge0\)), \(N=(p+1)/2\), and work coefficientwise in \(\mathbb Z_{(p)}[z]\) modulo \(p^2\). Let

\[
J_p(z)=\sum_{j=0}^q \binom qj\binom{3q+1}j(z/9)^j,\qquad
C_p(z)=\sum_{j=0}^q\frac{(5/8)_j(7/8)_j}{(j!)^2}(z/9)^j.
\]

Let (K_p^{\rm harm}(z)=\sum_{j=0}^q J_jh_jz^j), with the *previously fixed* short harmonic \(h_j=(H_q-H_{q-j})/8+3(H_{3q+1}-H_{3q+1-j})/8\). The existing exact short-kernel theorem gives \(C_p=J_p-pK_p^{\rm harm}\pmod{p^2}\). Define

\[
F_p^{\rm full}(x)=\sum_{k=0}^{p-1}\frac{(1/8)_k(3/8)_k}{(k!)^2}x^k,\quad
g(z)=(1-z/9)^N,\quad
V_p(x)=K_p^{\rm Euler}(x)+U_p(x).
\]

Here \(K_p^{\rm Euler}\) and \(U_p\) are precisely the lower Euler p-carry and upper cutoff p-tail of the preceding finite Euler note (they are different objects from \(K_p^{\rm harm}\)). Its identity is
\[
F_p^{\rm full}(z/9)=g(z)J_p(z)+pV_p(z/9)\pmod{p^2}.
\]

The older short Green note defines the *other normalization* (E_p(z)=[F_p^{\rm full}(z/9)-g(z)C_p(z)]/p\pmod p). Substitution yields the new explicit **coefficientwise gauge bridge**
\[
\boxed{E_p(z)=V_p(z/9)+g(z)K_p^{\rm harm}(z)\pmod p.}\tag{A}
\]

Let (u=g(1)=(8/9)^N), (V_0=V_p(1/9)), (V_1=\(x\partial_xV_p\)(1/9)), (H_0=K_p^{\rm harm}(1)), and (H_1=\(z\partial_zK_p^{\rm harm}\)(1)). Then for the *older* (e_0=E_p(1)) and (e_1=\(z\partial_zE_p\)(1)):
\[
\boxed{e_0=V_0+uH_0,\qquad
e_1=V_1+u\(H_1-NH_0/8\)\pmod p.}\tag{B}
\]
The derivative coefficient is (N/8), because (z g'(z)|_{z=1}=-Nu/8). Retain \(x\partial_x\) versus \(z\partial_z\), and \(U_p\) versus the lower carry; no change of truncation is hidden in this map.

For \(q\ge1\), the established Green Wronskian is (W_1=J_p(1)H_1-H_0J_p'(1)\pmod p); at \(q=0\) all three \(H_0,H_1,W_1\) are zero.

## Green-source cancellation at the selected second digit

The previous Wronskian note's selected Green formulas were conditional on the mod-(p) first-digit selector. Formula (B) identifies their *exact* normalization relation. Write (j_0=J_p(1)), (j_1=J_p'(1)) in \(\mathbb Z_{(p)}/p^2\) and let \(j_i/p\) mean the actual mod-(p) quotient when \(p\mid j_i\).

If \(j_0=0\pmod p\), \(j_1\ne0\pmod p\), then \(H_0=-W_1/j_1\). Hence the Green equation
\[
u\(j_0/p+W_1/j_1\)+e_0=0\pmod p
\]
reduces **exactly** to
\[
\boxed{u\(j_0/p\)+V_0=0\pmod p.}\tag{C}
\]
This is precisely ((F_p^{\rm full}(1/9)/p)\pmod p), provided its numerator is divisible by (p).

If \(j_1=0\pmod p\), \(j_0\ne0\pmod p\), then \(H_1=W_1/j_0\). Since \(1-2N=-p\), the other Green equation
\[
u\(16j_1/p-j_0-16W_1/j_0\)+e_0+16e_1=0\pmod p
\]
reduces **exactly** to
\[
\boxed{u\(16j_1/p-j_0\)+V_0+16V_1=0\pmod p.}\tag{D}
\]
This is the directly observable \((F_p^{\rm full}(1/9)+16\(x\partial_xF_p^{\rm full}\)(1/9))/p\pmod p\).

Thus the Green \(W_1\) contribution is absorbed by the finite Euler gauge change; this **reconciles** the two previously different e0 normalizations. The proof is substitution in the two established coefficientwise identities and elementary differentiation. The *vanishing* of (C)/(D) on every prime is a separate problem: the displayed equivalences do not use such a universal assertion.

## Exact witnesses and coverage

Companion standard-library checker independently constructs full Gauss and short ((5/8,7/8)) coefficients modulo \(p^2\), finite Jacobi coefficients modulo \(p^2\), and harmonic \(K^{\rm harm}\) modulo (p); calculates lower Euler and upper cutoff scalar ports separately; checks (B), both selected Green-to-Gauss reductions, and independently the two original \(p^2\) Gauss observables. **PASS 168/168 primes \(5\le p\le5000, p\equiv5\pmod8\)**. For all 9 primes \(p\le149\) in this class, also PASS *every coefficient* of (A) in degrees \(0,\ldots,p-1\). All 168 selected second digits were zero (finite exact evidence).

At \(p=373\) (the inert auxiliary Jacobi class), \(u=82\), \(H_0=332\), \(H_1=372\), \(W_1=189\), \(V_0=124\), \(V_1=176\). Therefore
\[
e_0=124+82\cdot332\equiv119,\qquad
e_1=176+82\(372-187\cdot332/8\)\equiv71\pmod{373}.
\]
This resolves the previously open numerical mismatch \(124\ne119\) by its **missing harmonic gauge term**, without changing either underlying observation. At \(p=29\) (split auxiliary class), (\(V_0,V_1,H_0,H_1,W_1,e_0,e_1\)=(2,27,22,12,26,5,24)\pmod{29}). At \(p=5\), \(q=0\), \(U_5=K_5^{\rm harm}=W_1=0\), and the bridge remains valid.

The BRC typed source is \(\(p,q,\text{original coefficient index},\text{lower Euler carry},\text{upper tail},\text{Jacobi harmonic deformation},\text{value},\theta\text{-derivative},W_1,\text{branch/normalization}\)\). Formula (A) is an exact, observer-preserving change of coordinates in this auxiliary classical model; it is not a native P000 six-axis construction.

## Current frontier / next executable unit

Highest author-side frontier: equations (A)–(D), source-separated normalizations and 168-prime exact check. Prior Green and finite Euler proof statements are consumed, not re-proved or re-registered. A next precise unit is to compare the *same-prime original 216–2304 signed second digit* with this normalized Gauss observable, including its quadratic observer and original 373 H0/B0/Frobenius direction. First obtain the original signed observer's authoritative definition/pin and test \(p=13,19,373\); an auxiliary equality cannot stand in for native \([X]U\bmod p^2\) data.

Native service continuation, new session/CLAIM/OPEN, Source checkpoint, formal Result and independent admission remain separate. The existing Source durable checkpoint must be preserved; this artifact is author-side evidence only.
