# D25 / SECOND-DIGIT-LIFT: fixed p=373 second-digit weighted cutoff certificate for original B2304

Date: 2026-10-29 Asia/Hong_Kong. Status: AUTHOR-SIDE / EXECUTED EXACT MOD-p² CERTIFICATE / FINITE OBSERVATION / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_H0_B0_NOT_EXECUTED.

Task and immutable scientific source pin are unchanged: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, TP2-B6F4FC938FF94941C1B7, c47e13e4aba0e006366f989d6334d443f6333ae3. Research lane is chatgpt-research-onhour-enterprise-math-20260923, never maintenance.

## Consumed theorem and new concrete witness

Consume, without reproving, the preceding author-side B2304 coefficientwise Clausen cutoff T1 at [the exact proof](https://github.com/awdawmip/enterprise-math/blob/eb34b4e9fc759d5695a7e20d7a68d2007e36af97/research_notes/portable_direct/20261029_onhour_d25_b2304_clausen_frobenius_carry.md): for p≡5 mod8,
\[
C_p(z)=\Pi_{<p}(K_p(z)^2)\pmod{p^2},
\quad K_p(z)=\sum_{n=0}^{(7p-3)/8}\frac{(1/8)_n(3/8)_n}{(n!)^2}z^n,
\]
where \(\Pi_{<p}\) truncates *before* derivative/evaluation. The original B2304 observer is \(B_p=[(1+8\theta)C_p]_{z=1/9}\), \(\theta=z\,d/dz\).

Take precisely p=373, modulus p²=139129 and w=1/9 in this finite ring. The **actual executed exact integer certificate** is
\[
K_{373}(w)\equiv0\pmod{139129},\qquad
(\theta K_{373})(w)\equiv5\pmod{373}.
\]
Consequently the unprojected weighted square is
\[
[(1+8\theta)K_{373}^2]_{z=w}
=K(w)^2+16K(w)\theta K(w)\equiv0\pmod{139129}.
\]
Yet the **full over-cutoff source** is strictly nonzero at exactly the required second-digit precision:
\[
\boxed{\sum_{n\ge373}(1+8n)[z^n]K_{373}(z)^2\,w^n
\equiv138756=-373\pmod{139129}.}
\]
Subtracting that source before evaluation gives
\[
\boxed{B_{373}\equiv0-(-373)\equiv373\pmod{139129}.}
\]
Independently evaluated the *original full binomial* expression
\[
\sum_{n=0}^{372}(8n+1)\binom{2n}{n}^{2}\binom{4n}{2n}\,2304^{-n}
\equiv373\pmod{139129}.
\]
The original and transformed source calculations agree exactly. The certificate was executed with Python standard-library integers and invertible denominators in Z/(p²); program [at immutable commit 42f63bee](https://github.com/awdawmip/enterprise-math/blob/42f63bee07dd367a7a199b5a3ddee7a5a05868fe/research_notes/portable_direct/d25_b2304_p373_second_digit_port_guard_20261029.py), Git blob 31b6a66a11ead94778fdea9f3ebe9489080535f5.

Result:
    PASS_D25_B2304_P373_SECOND_DIGIT_SOURCE_PORT
    p= 373 modulus= 139129 K(1/9)= 0 theta_K modp= 5 weighted_K2= 0 weighted_high_tail= 138756 weighted_projected= 373 original_binomial_B= 373

**What this proves** is a fixed-373 exact counterexample to the naive inference that the mod-p carry's zero scalar observation implies zero mod-p² weighted carry. It is *not* a universal all-prime CM root statement, not the A216/B2304 mod-p³ bridge, and not the native H0/B0 experiment. In BRC terms, the lost information is the source-degree/valuation port of the high pair convolution, which remains relevant under the future (1+8theta) observer: a nonzero p-adic correction survives even though the first digit is zero. Provenance/observer and operation order are preserved.

## Precise next unit and independent native gap

Next exact mathematical obligation: compute the *full source-tagged p² lift* of the B2304 over-cutoff polynomial and the p³ scalar bridge against the existing A216 source-preserving Clausen repair separately in p≡13 and 19 mod24, without replacing z^p by z before applying theta. Reuse the exact p373 certificate as a discriminating check, do not repeat broad finite scans. A finite signed residual does not certify a general theorem.

Highest native acceptance gap remains [#1559](https://github.com/awdawmip/enterprise-math/issues/1559) OPEN/PENDING_OWNER: p373 same-original-class H0/B0 divided-power [X]U mod139129, actual rank, semilinear Frobenius, signed Green/Hesse, native κ and Delta-R; native scientific executor must be established and independently reviewed. No native Result/CLAIM/Source execution checkpoint claimed. Last known own Source continuation was not authorized; gateway reported write_relay_enabled=false and no Researcher authority. The old #6575 recovery and #6576 failed dispatch remain historical request IDs, not newly replayed. All schedule and scientific-source settings remain unchanged.