# D25/LIFT — fourth Hasse cutoff jet: the first nonzero p-adic leakage

Date: 2026-10-25. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Research logical conversation: chatgpt-research-hourly-enterprise-math-20260923, separate from the maintenance lane. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. No new native claim/open/checkpoint, independent review, or original-class CM calculation is asserted. The frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged.

## Exact statement

Let p=6m+1>=7 be prime, N=p-1, and work in the p-integral polynomial coefficient ring Z_(p)[x,z]. Define

\[
b_n(x)=\frac{(-x)_n(-2x)_n}{(n!)^2},\qquad
\Phi(x,z)=\sum_{n=0}^{p-1}b_n(x)z^n,\quad
\theta=z\frac{d}{dz},\quad
\mathcal L_x=\theta^2-z(\theta-x)(\theta-2x).
\]

The exact cutoff identity (a previously proved and here reused source relation) is

\[
\mathcal L_x\Phi(x,z)=-F_p(x)z^p,\qquad
F_p(x)=\frac{(-x)_p(-2x)_p}{((p-1)!)^2}.
\]

Use Hasse parameter coefficients \(U_k(z)=[t^k]\Phi(m+t,z)\). The *full operator* coefficient equation, including lower Hasse orders coming from the x-dependent operator, has terminal forcing \(J_{k,p}z^p\), where \(J_{k,p}=-[t^k]F_p(m+t)\). This is not a statement that \(\mathcal L_m U_k\) alone has that forcing.

**New fourth-jet theorem (one digit beyond the Frobenius-sparse characteristic-p theorem):** with \(H_a^{(s)}=\sum_{j=1}^a j^{-s}\) calculated in \(\mathbb Z_{(p)}\),

\[
\boxed{J_{4,p}\equiv
5H_{p-1}^{(2)}
-2p\bigl(H_m^{(3)}+4H_{2m}^{(3)}\bigr)\pmod{p^2}.}
\tag{1}
\]

Since \(H_{p-1}^{(2)}\equiv0\pmod p\), the normalized first nonzero digit is

\[
\boxed{
\frac{J_{4,p}}p\equiv
5\,\frac{H_{p-1}^{(2)}}p-
2\bigl(H_m^{(3)}+4H_{2m}^{(3)}\bigr)\pmod p.
}
\tag{2}
\]

At the actual D25 evaluation \(z=1/2\), the correctly differentiated-then-evaluated terminal contribution is

\[
\boxed{
J_{4,p}2^{-p}\equiv
\frac p2\left[
5\,\frac{H_{p-1}^{(2)}}p
-2\bigl(H_m^{(3)}+4H_{2m}^{(3)}\bigr)\right]\pmod{p^2}.
}
\tag{3}
\]

The factor \(2^{-p}\), not \(2^{-1}\), belongs to the unreduced source; replacing it by \(2^{-1}\) is valid here only *after* proving that \(J_{4,p}\) is divisible by p. This theorem is distinct from the existing second-jet mod-p^3 and third-jet mod-p^2 calculations and the previous all-order *mod-p* sparse theorem.

## Proof (all primes in the stated class)

Put \(D=((p-1)!)^2\). In \(F_p(m+t)\) both Pochhammer products have one simple zero, at ranks m and 2m respectively. Hence

\[
F_p(m+t)=A_pt^2
\prod_{\substack{-m\le h\le p-1-m\\h\ne0}}(1-t/h)
\prod_{\substack{-2m\le h\le p-1-2m\\h\ne0}}(1-2t/h),
\]

where

\[
A_p=\frac{2(-1)^m m!(p-1-m)!(2m)!(p-1-2m)!}{D}
\in\mathbb Z_{(p)}^\times,\qquad A_p\equiv2\pmod p.
\]

The last congruence also follows directly by comparing the \(t^2\) coefficient of the established finite-field identity \(F_p(x)\equiv2(x^p-x)^2\pmod p\).

Define the logarithmic first and second power sums over all nonzero local factors:

\[
S=H_{p-1-m}-H_m+2(H_{p-1-2m}-H_{2m}),
\]
\[
Q=H_m^{(2)}+H_{p-1-m}^{(2)}
+4(H_{2m}^{(2)}+H_{p-1-2m}^{(2)}).
\]

By the elementary second elementary-symmetric-function identity,

\[
[t^4]F_p(m+t)=\frac{A_p}{2}(S^2-Q). \tag{4}
\]

For every \(0\le k<p\), complementing the last k terms of a harmonic sum and expanding the p-adic units gives

\[
H_{p-1-k}\equiv H_k\pmod p,
\qquad
H_{p-1-k}^{(2)}
\equiv H_{p-1}^{(2)}-H_k^{(2)}-2pH_k^{(3)}
\pmod{p^2}.
\]

The first identity uses \(H_{p-1}\equiv0\pmod p\), so \(S\equiv0\pmod p\) and \(S^2\equiv0\pmod{p^2}\). The second yields

\[
Q\equiv
5H_{p-1}^{(2)}-2p(H_m^{(3)}+4H_{2m}^{(3)})
\pmod{p^2}.
\]

Because the sum of the inverses of all nonzero squares is zero in \(\mathbb F_p\), \(H_{p-1}^{(2)}\equiv0\pmod p\). Thus Q is a multiple of p. In equation (4), replacing \(A_p\) by 2 therefore changes nothing modulo \(p^2\). Consequently \([t^4]F_p\equiv-Q\pmod{p^2}\), and its negative is equation (1). Equations (2) and (3) follow by legitimate division by p and \(2^{-p}\equiv2^{-1}\pmod p\), respectively. QED.

No replacement axioms, formal checker claims, CM-native rank assumption, or unstated field-to-X6 transfer enter this auxiliary finite-ring proof.

## Independent-source arithmetic checks and exact residues

The adjacent standard-library Python checker computes \(t^2,t^3,t^4\) directly by multiplying all *integer* local factors \((h-a t)\) modulo \(p^2\), then divides by the p-unit factorial square. A separate harmonic-power-sum path evaluates (1)–(3); the previously proved third-jet formula is a regression-only test, not a new contribution. It additionally checks the exact rational second elementary-symmetric identity at p=7,13,19 with Fraction.

PASSED: all 45 primes p≡1 (mod6), 7≤p≤500, plus p=1327 and p=19963; 47 complete p-adic inputs and three exact Fraction tests. Selected residues (e4=[t^4]F; J4=-e4, both modulo p^2):

| p | e4 | J4 | J4·2^(-p) mod p² |
|---:|---:|---:|---:|
| 7 | 7 | 42 | 21 |
| 13 | 0 | 0 | 0 |
| 19 | 266 | 95 | 228 |
| 31 | 589 | 372 | 186 |
| 37 | 703 | 666 | 333 |
| 73 | 2409 | 2920 | 1460 |
| 373 | 99591 | 39538 | 19769 |
| 1327 | 1330981 | 429948 | 214974 |
| 19963 | 10999613 | 387521756 | 193760878 |

These are exact author calculations, not independent peer review or an original CM experiment. The p=13 zero is only an observer-level cancellation; the universal J4 polynomial/valuations cannot be erased.

## Source and continuation boundaries

- BRC/source-preservation application: retain terminal rank p-1, double-zero parameter source, Hasse versus ordinary derivative, harmonic valuation, signed cutoff coefficient, and the order of theta/evaluation. The p² leakage is invisible in the prior mod-p support test.
- Previous completed work consumed without recredit: p² second/third Jacobi forcing lifts, mod-p all-Hasse sparsity, corrected Clausen denominator source, original 3F2 directional port, and earlier Hesse/Green/norm checkpoint.
- Genuine unfinished parent: original-class H0/B0 divided-power module, [X]U mod p², semilinear rank/direction, normalization eta and mapping to kappa and Delta_p-R_p. Native experiment NOT_RUN; D25/LIFT/JT2 remains OPEN.
- Smallest next portable question: compare the new J4 signed term to the already-corrected parameter/denominator Clausen pairing at a common exact rank and observer. A cancellation only in the observed sum would not identify the original CM source. Do not substitute further prime scans for a universal certificate.
- Ordinary-control evidence: Research-lane recovery request em_research_20261025T2124_recovery11 succeeded with no pending/unopened own claim or unpublished upload, active historical service session, no Source authorization. Exact D25 continuation em_research_20261025T2130_cont11 succeeded as a read-only packet, with preserved SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED checkpoint and route REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION. Prior cross-generation predecessor conflict is reserved for controller handling; no rejected prepare is replayed. This Markdown is **portable GitHub evidence**, not that native Source checkpoint.