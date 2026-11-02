# D25 — Original W216 value-level p^3 Cauchy transport with high-index and logarithmic source corrections

2026-11-02. **AUTHOR-DERIVED / PROVED EXACTLY / EXACT FINITE REPLAY / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.** Research object: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific input \`c47e13e4aba0e006366f989d6334d443f6333ae3\`, unchanged. Logical historical Research lane \`chatgpt-research-onhour-enterprise-math-20260923\`; no maintenance-lane identity, claim or native run is asserted.

## Why this is the next mother-goal unit

The accepted D24/finite-Clausen reduction makes the D25 original signed second-digit obligation equivalent in p≡13,19 (mod24) to the **original value**, not its derivatives:
\[
W_p(1/2)=\sum_{k=0}^{p-1}(6k+1)\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3\,2^k}\equiv p\pmod{p^3}.
\]
The prior Cauchy lane proved a signed first-jet correspondence and its p^2 repair, but its derivative readout did not directly determine this scalar value. The present theorem instead gives an **exact value-level transport at all precisions** with the otherwise missing upper boundary and a computable p-adic logarithmic deformation. No external conjecture is assumed.

## Original objects and provenance

Let \(p=6m+1>3\) be prime; work in \(\mathbf Z_{(p)}\), and write \(\theta=z\,d/dz\), \(z_0=1/2\). Define the original unweighted polynomial
\[
F(z)=\sum_{i=0}^{p-1}a_i z^i,\qquad
a_i=\frac{(1/2)_i(1/3)_i(2/3)_i}{(i!)^3}
=\frac{\binom{2i}{i}^{\,2}\binom{3i}{i}}{108^i}.
\]
Keep the **ordered** source indices \((i,j)\) in the separate finite binomial Cauchy convolution
\[
E(z)=\sum_{j=0}^{p-1}\frac{(1/2)_j}{j!}z^j,\qquad C(z)=[E(z)F(z)]_{<p}.
\]
This is the same outer Cauchy polynomial defined in the preceding Le Lan-source note; its exact formal-series identity with \((1-z)^{-1/2}F\) is established there, with Roman Le Lan's Euler/Clausen identity identified as published prior art (arXiv:2604.03327v2). This paper is not claimed to prove the present p^3 result. Put
\[
e(z)=(1-z)^{3m},\quad P(z)=e(z)F(z),\quad
A(z)=[P(z)]_{<p},\quad H(z)=P(z)-A(z),\quad D(z)=C(z)-A(z).
\]
The high polynomial \(H\) is **not evaluated after setting \(z^p=0\)**: the target \(z_0\) is a p-adic unit, so all its high terms may survive. Define the four separate typed observers
\[
W=[(1+6\theta)F]_{z_0},\quad L=[(3\theta-1)C]_{z_0},\quad
U=[(3\theta-1)H]_{z_0},\quad T=[(3\theta-1)D]_{z_0},\quad f=F(z_0),\quad e_0=2^{-3m}.
\]

## Theorem A — exact value-level signed transport

For every prime \(p=6m+1>3\), there is an equality in \(\mathbf Z_{(p)}\), with no CM hypothesis:
\[
\boxed{\displaystyle W=2e_0^{-1}(L+U-T)+3pf.}\tag{A}
\]
Consequently the original D25 target in its two selected residue classes is *equivalent* to this new, source-preserving Cauchy condition:
\[
\boxed{\displaystyle L+U-T\equiv\frac{pe_0}{2}(1-3f)\pmod{p^3}.}\tag{B}
\]
If a separately authenticated source establishes \(f\equiv0\bmod p^2\) for the selected classes, (B) specializes to \(L+U-T\equiv pe_0/2\bmod p^3\). The unconditional criterion (B) preserves the scalar correction \(3pf\).

**Proof.** By exact coefficient-truncation definitions, \(C=P-H+D\), hence \(P=C+H-D\). At \(z_0=1/2\),
\[
\frac{\theta e}{e}=-3m\frac{z}{1-z}=-3m,\qquad
(3\theta-1)(eF)=e(3\theta-9m-1)F
=\frac e2[(1+6\theta)F-3pF].
\]
Apply \(3\theta-1\) to the polynomial identity \(P=C+H-D\), evaluate at \(z_0\), and solve for \(W\). All terms are rational with denominators prime to p; no limit or untruncated analytic series is substituted into the finite equality. This proves (A) and (B).

## Theorem B — exact p^3 logarithmic deformation and upper-boundary valuation

Define \(Q(z)=\sum_{n=1}^{p-1}z^n/n\) and \(H_n=\sum_{r=1}^{n}1/r\), \(H_0=0\). Then in \(\mathbf Z_{(p)}[z]/(p^3,z^p)\):
\[
\boxed{\displaystyle
D(z)\equiv\left[
e(z)F(z)\sum_{n=1}^{p-1}
\left(\frac{p}{2n}+\frac{p^2 H_{n-1}}{4n}\right)z^n
\right]_{<p}\pmod{p^3}.}\tag{C}
\]
Moreover \(H\in p^2\mathbf Z_{(p)}[z]\) and \(H\bmod p^3\) receives contributions only from the exact original source indices \(3m+1\le i\le4m\); the indices \(i\ge4m+1\) contribute multiples of \(p^3\).

**Proof.** In formal series,
\[
E=(1-z)^{-1/2}=e(z)(1-z)^{-p/2}
=e(z)\exp\left(\frac p2\sum_{n\ge1}\frac{z^n}{n}\right).
\]
Coefficientwise through degree <p the denominators n and all factorial coefficients are p-units. Expanding the exponential mod p^3 and using \([z^n]Q^2=2H_{n-1}/n\) yields (C). For a coefficient of \(H=[eF]_{\ge p}\), each original convolution pair obeys \(i+j\ge p\), \(0\le j\le3m\), hence \(i\ge3m+1\). Legendre's formula for \(i<p\) gives
\[
v_p(a_i)=\left\lfloor\frac{2i}{p}\right\rfloor+\left\lfloor\frac{3i}{p}\right\rfloor.
\]
It is \(\ge2\) for \(i\ge3m+1\) and \(\ge3\) for \(i\ge4m+1\). Preserve the first band and all ordered convolution indices. This proves the valuation assertion.

## Exact computational certificate, independent observers

The accompanying standard-library Python checker constructs \(a_i\) by the original factorial-ratio recurrence; constructs C from *direct E*F ordered convolution; constructs P and H from a distinct finite \((1-z)^{3m}F\) convolution; constructs D **independently a second time** from (C); and checks equality (A) against the directly computed weighted W modulo p^3. It checked 18 primes \(7,13,19,31,37,43,61,67,73,79,97,109,139,157,181,229,373,1171\), all exact source/transport/log identities passing. The previously observed original W supercongruence is checked only as a finite diagnostic, not used as the proof of (A)-(C).

At p=373, the modulus is 51,895,117, and the independently calculated raw observers are:
\[
W=373,\quad f=9\,878\,159,\quad L=8\,487\,242,\quad U=19\,060\,673,\quad T=46\,400\,081\quad(\bmod p^3).
\]
Here \(U/p^2\equiv137\bmod373\); the high boundary is a real nonzero second-digit correction. After the exact \(2e_0^{-1}\) prefactor, the four source contributions to W are
\[
6\,538\,317\quad(\text{Cauchy}),\quad
13\,773\,771\quad(\text{high boundary}),\quad
31\,583\,402\quad(\text{minus logarithmic deformation}),\quad
0\quad(3pf).
\]
Their integer sum is 51,895,490, giving \(W=373\bmod51\,895\,117\). At p=7 the \(3pf\) port is 133 mod343, confirming why its retention is mathematically necessary outside special CM hypotheses.

The finite checks corroborate the algebraic theorem. They do not prove the distinct universal congruence \(W\equiv p\chi_{-3}(p)\bmod p^3\) or classify its novelty.

## Frontier, BRC observer and native benchmark

The scientific frontier is now a directly weighted, p^3-precision, **value-level** decomposition (A)-(C), with traceable original index pairs, source coefficients, exact valuations, signed readouts and the future operation evaluation at a p-unit. This gives an exact factorization of the declared W-observer; it is not a claim of full joint-state equivalence. A useful next discriminating step is to prove the right-hand condition (B) by a finite creative-telescoping identity for the complete original 216-Cauchy pair, explicitly tracking the p^2 upper tail \(U\) and the p, p^2 logarithmic defect \(T\), or locate a rigorously matching published p^3 original W theorem. Do not repeat first-jet-only work or numeric W stress.

The same-original-class p373 native H0/B0 divided-power [X]U mod139129, module rank, semilinear Frobenius eta, odd Green/Hesse κ and independent reproduction remain NOT_EXECUTED/PENDING_OWNER in issue #1559. This scalar theorem is not that native experiment. Current Sites status 0.6.11 (fresh 2026-11-02): Research authorization false, queue admission limit active; no native session/claim/run/checkpoint is asserted. The existing author-side artifact is UNREVIEWED/NOT_ADMITTED; staging is independent; historical unknown/rejected requests are not replayed. Existing scheduler/notifications untouched.
