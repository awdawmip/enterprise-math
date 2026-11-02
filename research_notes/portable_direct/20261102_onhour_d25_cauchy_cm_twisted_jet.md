# D25 — A genuine finite Cauchy/216 CM bridge: exact polynomial square and twisted first jet
2026-11-02. **AUTHOR-DERIVED / ALGEBRAICALLY PROVED (using accepted CM0) / FINITE EXACT REPLAY / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_SOURCE_SYNC_DEBT.**
Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific source c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged. Declared research logical lane chatgpt-research-onhour-enterprise-math-20260923, not the maintenance conversation.

## Exact external source, without novelty misattribution
Roman Le Lan, *Series for 1/pi arising from Cauchy product*, arXiv:2604.03327v2 (10 April 2026), Lemma 1 and Eq. (3.2), https://arxiv.org/pdf/2604.03327. His Euler/Clausen Cauchy-product identity is **prior art**. This note derives a new finite characteristic-p CM specialization and a correctly signed derivative observer, retaining the different original sums and cutoffs. The paper's stated Sun mod-p² conjecture about the Cauchy-weighted sum is not used as a theorem.

Let p=6m+1>3 be prime, let theta=z*d/dz, and define the **original 216 unweighted source**
\[
F_p(z)=\sum_{k=0}^{p-1} a_kz^k,\quad a_k=\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3}
=\frac{\binom{2k}{k}^2\binom{3k}{k}}{108^k}.
\]
Define the Le Lan outer Cauchy source by
\[
c_n=\sum_{r=0}^n \binom{-1/3}{r}\binom{-1/6}{r}
\binom{-2/3}{n-r}\binom{-5/6}{n-r},\quad C_p(z)=\sum_{n=0}^{p-1}c_nz^n.
\]
This ordered convolution is retained in provenance; C_p is a separate observer, NOT the original H0/B0 native class. Define
\[
\ell_m(z)=\sum_{j=0}^m\binom mj\binom{2m}jz^j,\quad
E_p(z)=\sum_{j=0}^{p-1}(1/2)_jz^j/j!.
\]

## Theorem 1 — all-p exact finite convolution and full polynomial mod-p identity
Over Q[[z]], the published Euler and Clausen identities give
\[
\sum_{n\ge0}c_nz^n=(1-z)^{-1/2}\sum_{n\ge0}a_nz^n.
\]
Therefore, **exactly in Q[z] through every coefficient n<p**,
\[
\boxed{C_p(z)=[E_p(z)F_p(z)]_{<p}.}\tag{1}
\]
The truncation operation retains total index n and ordered component indices r,n-r. Since p=6m+1,
\[
E_p(z)\equiv(1-z)^{3m},\qquad F_p(z)\equiv\ell_m(z)^2\pmod p.
\]
The second congruence is the exact finite Clausen reduction (previously established); both are polynomial coefficient identities. Their product has degree 3m+2m=5m<p. Hence
\[
\boxed{C_p(z)\equiv(1-z)^{3m}\ell_m(z)^2\pmod p}\tag{2}
\]
**as a full polynomial, not only modulo z^p**, for all primes p≡1 (mod6). In particular, every original outer Cauchy coefficient c_n with 5m<n≤6m has p-valuation at least one. The next p-adic digit of those coefficients is not discarded when division by p may follow.

## Theorem 2 — target-class CM double root and signed first-jet transport
For p≡13,19 (mod24), consume the accepted CM0 input \ell_m(1/2)≡0 (modp), and its already-proved simple-root property \ell'_m(1/2)≠0 (modp). Consequently F_p and C_p both have a **double**, not higher, root at z0=1/2 mod p. Since
\[
(1-z_0)^{3m}=2^{-3m}\equiv(2/p)=-1\pmod p
\]
by Euler's criterion in exactly these residue classes, their second Euler jets satisfy
\[
\boxed{(\theta^2 C_p)(z_0)\equiv-(\theta^2 F_p)(z_0)\pmod p.}\tag{3}
\]
Preserve the distinct signed original weighted readouts
\[
W_p(z)=(1+6\theta)F_p(z),\qquad L_p(z)=(3\theta-1)C_p(z).
\]
At a double root, their first Euler jets obey
\[
\boxed{2(\theta L_p)(1/2)+(\theta W_p)(1/2)\equiv0\pmod p.}\tag{4}
\]
This is an **all-target-prime first-jet identity** with exact source and Frobenius quadratic-character twist; it makes no claim that W_p(1/2)=L_p(1/2) modulo p² or p³. The actual mother obligation W_p(1/2)=p (modp³) remains open.

## Exact replay and p=373 certificate
A Python standard-library modular checker, using the original 216 coefficient recurrence and **two independent Cauchy constructions** A(z)B(z) and E_p(z)F_p(z), passed 53 primes: 45 targets p≤1000, five non-CM controls 5,7,11,17,23 and two further controls 31,47, plus 1171. It compared 22,507 coefficient positions at mod p², all full mod-p polynomial coefficients, source CM0 and the signed jet. Independent arithmetic contains no p-divisible modular denominator.
At p=373: m=62, c_n≡0 mod373 for 311≤n≤372, \ell_m'(1/2)=215, (\theta W_p)(1/2)=292 and (\theta L_p)(1/2)=227 modulo373. Thus 2*227+292=746=2*373, exactly. p=13: slopes 3,5; p=19: slopes 12,13, all with signed formula (4).
Further observed (not a theorem): the signed first-jet congruence generally acquires a nonzero **next-digit repair** after division by p; this is the next local scientific unit.

## BRC observer and native/source boundaries
Carrier is the original ordered convolution (r,n-r), coefficients a_k,c_n, their p-valuations and source model tags, and the evaluated theta-jets. The operation that follows is evaluation at the p-unit z0 followed by division by p or higher; formal truncation z^p cannot be evaluated at z0 and silently discarded. This is a source-preserving external p-adic scalar algebra bridge, not a native X6 embedding or the pending fixed-p373 H0/B0 native [X]U experiment.

Source p373 same-class divided-power [X]U modulo 139129, module rank, semilinear Frobenius/eta, odd signed Green/Hesse/kappa and independent replay remain NOT_EXECUTED/PENDING_OWNER under existing #1559. Current native Site gateway has no Research write authorization, so this is only author-side GitHub evidence, not session/CLAIM/run, Source checkpoint, Result, mathematical review or admission. No maintenance ID used.

## Next exact action
Derive and verify the p² correction to the signed first-jet transport, preserving the full <p truncation and the CM root's p-adic quotient; then assess whether the resulting correction can help the original weighted W_p=p (modp³) or is only a first-jet tool. Preserve the exact 2026 cited source and original frozen pin.