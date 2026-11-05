# D25 — Exact fourth-digit signed Clausen/216 interface samples

Date: 2026-11-05 (+08). Mother Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, immutable publication \`TP2-B6F4FC938FF94941C1B7\`, frozen scientific source \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. AUTHOR EXACT FINITE CERTIFICATE / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM.

## Distinct observer and finite exact result

For \(p=6n+1\), define the original signed 216 weighted series
\[
W_p=\sum_{k=0}^{p-1}(6k+1)\frac{(2k)!(3k)!}{216^k(k!)^5}
\]
and the terminating Clausen source
\[
G_p(z)={}_2F_1(-n,-2n;1-p/2;z),\qquad
\Psi_p(z)=G_p(z)\bigl(G_p(z)+12zG_p'(z)\bigr).
\]
Both are in \(\mathbb Z_{(p)}\). If \(W_p\equiv\Psi_p(1/2)\bmod p\), the **source-sensitive** quantity
\[
\boxed{Q_p=\frac{W_p-\Psi_p(1/2)}p\pmod{p^3}}
\]
is well-defined. It retains the difference of original signed 216 coefficients from the terminating Clausen observer at three p-adic digits (mod p^3), rather than conflating those observers.

This run computed these exact finite witnesses using independent modular factorial and coefficient-recursion implementations, both giving identical values modulo \(p^4\):

| p | \(W_p\bmod p^4\) | \(\Psi_p(1/2)\bmod p^4\) | \(Q_p\bmod p^3\) | three base-p digits of \(Q_p\) | \((W_p-p)/p^3\bmod p\) |
|---:|---:|---:|---:|---:|---:|
| 7 | 350 | 1246 | 215 | (5,2,4) | 1 |
| 13 | 19786 | 7761 | 925 | (2,6,5) | 9 |
| 19 | 82327 | 123158 | 4710 | (17,0,13) | 12 |
| 373 | 11832087049 | 14593651483 | 44491459 | (19,293,319) | 228 |

Here \(\mod p^3\) for \(Q_p\) uses the canonical representative of \((W_p-\Psi_p)\mod p^4\), divided by p. In particular \(\Psi\) and \(W\) generally have different signed internal digits even though \(W_p\equiv p\bmod p^3\) in all four cases.

## Link to the already published six-port identity

The inherited exact algebraic reduction
\[
W_p\equiv\Psi_p(1/2)+pF+p^2H\pmod{p^3}
\]
implies \(\boxed{Q_p\equiv F+pH\pmod{p^2}}\). Using the previously published six-port table (not independently rederived here),

- p=13: \(F=15\bmod169\), \(H=5\bmod13\). \(F+pH=80\bmod169\), while \(925\bmod169=80\).
- p=19: \(F=283\bmod361\), \(H=5\bmod19\). \(F+pH=17\bmod361\), while \(4710\bmod361=17\).
- p=373: \(F=130196\bmod139129\), \(H=317\bmod373\). \(F+pH=109308\bmod139129\), while \(44491459\bmod139129=109308\).

The third Q digit \((5,13,319)\) is **new finite precision data** for p=13,19,373 beyond this inherited p^3 interface. It is not yet an algebraically separated universal seventh/eighth source port, nor a native H0/B0 result. The distinct p^4 Clausen-root calculation in the preceding \`20261105_hourly20_d25_clausen_one_jet_hensel_p4.md\` can be paired with this vector without identifying the two coefficient populations.

## Verification, arithmetic, and next question

The companion \`d25_signed_fourth_digit_clausen_samples_20261105.js\` contains two independent exact routes: the original hypergeometric ratio for the full W sum and direct modular factorials; and the terminating G ratio and direct integer falling-products for \(\Psi\). For each listed p, factorial denominators use only k<p and powers of 216, hence are units modulo \(p^4\). No floating-point arithmetic enters the witness. A prior run compared the independent arithmetic for 7,13,19,373 exactly; the published code allows the comparison to be repeated.

Next proof obligation is a true **source-preserving symbolic expression** of \(Q_p\mod p^3\) in the signed 216 valuation layers and harmonic derivatives, enough to determine the new third digit, then test whether any finite telescope forces the second-digit LIFT cancellation across all \(p\equiv13,19\bmod24\). Retain the original frozen native p373 H0/B0, \([X]U\bmod139129\), semilinear \(\eta,\kappa\) and independent review obligations separately.
