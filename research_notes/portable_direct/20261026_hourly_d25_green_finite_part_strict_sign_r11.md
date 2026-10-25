# D25/LIFT — Exact alternating sign of the critical Green finite part

Date: 2026-10-26. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. Frozen science source pin: c47e13e4aba0e006366f989d6334d443f6333ae3, unchanged.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** This rational auxiliary-model statement is not a native CM/Frobenius experiment, canonical Research checkpoint, independent review or all-prime LIFT theorem.

## Input (not recredited)

Reuse the corrected-Clausen rational factorials and the finite-part identity proved in the preceding critical-point result, now stored at research_notes/portable_direct/20261026_hourly_d25_critical_point_residue_r11.md. For an integer m>=1 put L=m+1 and U=2m, and set

\[
a_j=(-1)^{j-L}\frac{m!(j-m-1)!(2m)!}{(2m-j)!(j!)^2},\quad L\le j\le U,
\qquad
h_\ell=\frac{2\,m!\,(2m)!\,((\ell-1)!)^2}{(\ell+m)!(\ell+2m)!}>0.
\]

The Laurent finite part of the reciprocal Green–Wronskian transfer at z=1/2 was established as

\[
\operatorname{FP}_m=
\frac{(-1)^{3m}}{2^{3m}}
\sum_{j=L}^{U}\sum_{\ell=j}^{U}
(j+\ell)\binom{3m+\ell-j}{3m}a_jh_\ell. \tag{I}
\]

This uses the complementary upper triangle, not the original signed Clausen lower triangle. The Toeplitz infinity-boundary identity is separately established in research_notes/portable_direct/20261026_hourly_d25_toeplitz_infinity_compensation_r11.md.

## New theorem: strict sign for every integer m>=1

Define the rational positive quantities

\[
B_j=\sum_{\ell=j}^{U}(j+\ell)\binom{3m+\ell-j}{3m}h_\ell,
\qquad b_j=|a_j|B_j.
\]

Then

\[
\boxed{b_L>b_{L+1}>\cdots>b_U>0} \tag{S1}
\]

and, for every m>=1,

\[
\boxed{(-1)^m\operatorname{FP}_m>0.} \tag{S2}
\]

For m>=2 we also obtain the exact rational bounds

\[
\boxed{
\frac{b_L-b_{L+1}}{2^{3m}}
\le (-1)^m\operatorname{FP}_m
<\frac{b_L}{2^{3m}}.
} \tag{S3}
\]

The lower bound is an equality when m=2. For m=1 only the first summand exists; FP_1=-1/144.

**Proof.** Let w(j,l)=(j+l) binom(3m+l-j,3m)>0 for l>=j. For j<U and l>=j+1,

\[
\frac{w(j+1,\ell)}{w(j,\ell)}
=\frac{j+\ell+1}{j+\ell}\frac{\ell-j}{3m+\ell-j}<1,
\]

since \(\ell-j<3m(j+\ell)\) for the specified integer ranges. Thus every summand shared by B_j and B_{j+1} strictly decreases, and B_j additionally contains its positive diagonal summand. Hence B_j>B_{j+1}>0. Meanwhile

\[
\frac{|a_{j+1}|}{|a_j|}
=\frac{(j-m)(2m-j)}{(j+1)^2}<1
\qquad (L\le j<U).
\]

This proves S1. Because \(a_j=(-1)^{j-L}|a_j|\) and \((-1)^{3m}=(-1)^m\), equation I becomes
\[
(-1)^m\operatorname{FP}_m=
2^{-3m}(b_L-b_{L+1}+b_{L+2}-\cdots).
\]
A finite alternating sum of a strictly decreasing sequence of positive rationals, starting positive, is strictly positive. Pairing adjacent terms proves S2, and pairing all terms after the first or first two gives S3. QED.

## Independent exact author checks and interpretation

The proof is general over Q; additional exact Fraction tests passed for 1<=m<=30, checking S1–S3 and the original double sum. For 1<=m<=12 they also match the independently derived high-order Taylor-jet extraction in the preceding checker. Exact examples: FP_1=-1/144, FP_2=23/115200, FP_3=-4273/729907200. Standalone reproducible implementation: research_notes/portable_direct/20261026_hourly_d25_green_finite_part_strict_sign_check.py.

This is a new nonvanishing and sign conclusion for the **specific characteristic-zero finite-part observer**, not for its leading Laurent pole and not for the original reflection-tail observer. Rational positivity/nonvanishing does **not** imply nonvanishing modulo p (in particular no uniform mod-p unit assertion is made). The auxiliary complex z plane is not a native X6 plane. Preserve signed source ranks and observer direction under any BRC compression.

## Next precise action

Combine the two distinct critical-point observers (positive leading pole and sign-alternating finite part) with the Toeplitz infinity two-moment compensation; seek a source-faithful coupled certificate in the full corrected Clausen operator. The parent LIFT/JT2 target remains OPEN. The official canonical next action still requires real same-class H0/B0, divided-power [X]U mod p², native semilinear Frobenius direction/normalization, kappa mapping and independent review. No winning CLAIM, authorized OPEN, native checkpoint or native CM computation follows from this portable publication.
