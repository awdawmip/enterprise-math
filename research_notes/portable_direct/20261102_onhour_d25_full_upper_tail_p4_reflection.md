# D25 — Original W216 whole upper-tail reflection modulo p^4

**2026-11-02 · AUTHOR-DERIVED / HAND-PROVED / EXACT FINITE REPLAY / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.**
Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen scientific input c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Logical Research lane chatgpt-research-onhour-enterprise-math-20260923; never the maintenance lane.

## Theorem: retain every omitted original high-band term

With the **original** D25 W216 coefficients and weights,

\[
a_k=\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3},\qquad
W_p(N)=\sum_{k=0}^N(6k+1)a_k2^{-k},
\]

define for each prime p>3
\(h=\lfloor2p/3\rfloor\), \(R=\lfloor(p-3)/3\rfloor\) and a finite-field sequence

\[
\boxed{d_0=1,\qquad
d_{r+1}=d_r\frac{36(r+1)^3}{(2r+3)(3r+5)(3r+4)}
\pmod p,\quad 0\le r<R.}
\]

The denominators in this range are all p-units. For **every** r=0,...,R,

\[
\boxed{\frac{(6(p-1-r)+1)a_{p-1-r}2^{-(p-1-r)}}{p^3}
\equiv(6r+5)d_r\pmod p.}
\]

Consequently,

\[
\boxed{W_p(p-1)-W_p(h)\equiv
p^3\sum_{r=0}^{R}(6r+5)d_r\pmod{p^4}.}\tag{T}
\]

This is an exact original-coefficient **whole terminal-band** reflection. In particular the cutoff reduction \(W_p(p-1)\equiv W_p(\lfloor2p/3\rfloor)\pmod{p^3}\) is valid, with the complete correction at the next p-adic digit displayed above. For r=0 it yields the direct original weighted terminal-term identity

\[
\boxed{W_p(p-1)-W_p(p-2)\equiv5p^3\pmod{p^4},}
\]

which has exact p-valuation 3 for primes p>=7 and is zero mod p^4 for p=5.

## Complete derivation and safe denominators

The p-divisible factors in (1/2)_k,(1/3)_k,(2/3)_k all enter by k=h+1, while the denominator (k!)^3 remains a p-unit for k<p. Therefore each term with h<k<p has valuation at least 3, and the upper-tail index map k=p-1-r is a bijection for r=0,...,R, because p-1-R=h+1.

The immediately preceding verified exact original-weight operator theorem (commit 519e114aa5c1f583d732b322851bb4701e756f20) proved by Wilson and Fermat that

\[
a_{p-1}/p^3\equiv-1\pmod p.
\]

Reverse the **original** rising-factorial recurrence, for k=p-1-r:

\[
\frac{a_{k-1}}{a_k}
=\frac{k^3}{(k-1/2)(k-2/3)(k-1/3)}
\equiv\frac{18(r+1)^3}{(2r+3)(3r+5)(3r+4)}\pmod p.
\]

For r<R, \(3r+5\le3R+2<p\), so no p-divisible factor is inverted. If \(c_r=-a_{p-1-r}/p^3\bmod p\), then c_0=1 and c_(r+1) follows the ratio 18. The original weight reduces to
\(6(p-1-r)+1\equiv-(6r+5)\pmod p\); also \(2^{-(p-1-r)}\equiv2^r\pmod p\). Hence the signed terminal term divided by p^3 equals (6r+5)*2^r*c_r. Setting \(d_r=2^r c_r\) doubles the ratio to 36 and proves the termwise identity. Summation proves (T); r=0 gives the terminal term 5. QED.

## Executed exact finite arithmetic

The same-commit standard-library Python reproducer compares the **entire direct original W216 k-index sum** against the reversed low-r sequence, term by term modulo p^4, for **all 428 primes 5<=p<=3000**, totaling **197723 tail indices**, and checks every signed sum. All assertions passed.

| p | h=floor(2p/3) | tail terms | exact tail mod p^4 | normalized tail / p^3 mod p |
|---:|---:|---:|---:|---:|
| 5 | 3 | 1 | 0 | 0 |
| 7 | 4 | 2 | 2058 | 6 |
| 13 | 8 | 4 | 10985 | 5 |
| 19 | 12 | 6 | 27436 | 4 |
| 373 | 248 | 124 | 14426842526 | 278 |

## BRC information preservation and remaining objective

This result is a **scope-specific information-preserving BRC cutoff certificate**: the original ordered indices, p-valuations, rational coefficients, signed weights and x=1/2 are retained. The reduction to h=floor(2p/3) is safe for the W mod-p^3 observer, while the future operation (W_full-W_short)/p^3 mod p requires the concrete repair coordinate \(\sum(6r+5)d_r\). It is an external p-adic observer computation and is not asserted as a new native X6 geometric theorem.

The frozen **D25 mother objective** remains: prove or refute Delta_p-R_p=0 mod p for all p=13,19 (mod24), equivalent under the accepted D24/CM0 original-cutoff bridge to W_p(p-1)=p mod p^3. The broader character candidate W_p(p-1)=p chi_-3(p) mod p^3 was finitely checked but not universally proved. A direct terminating WZ/contiguous certificate may now use the strictly shorter cutoff h without losing the p^3 target. If a candidate needs p^4 or a division by p^3, apply the exact signed tail (T). Tests at p13,p19,p373 and non-target p5,p7 are available.

**Native experiment:** authentic original p373 H0/B0 divided-power [X]U mod139129, module rank, semilinear Frobenius/eta, signed odd Green/Hesse/kappa and independent replay remain NOT_EXECUTED, with no confirmed executor at the 2026-11-02 read of issue #1559. These author-side symbolic and finite scalar calculations do not satisfy the native gate. The Site client's Researcher execution authority is unavailable; no authenticated session/claim/run/Source checkpoint/Result/admission is asserted. Original request preserved, not replayed. The Research automation and notification settings were not changed.
