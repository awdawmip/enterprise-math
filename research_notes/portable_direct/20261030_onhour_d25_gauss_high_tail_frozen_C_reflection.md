# D25 / SECOND-DIGIT-LIFT — source-indexed Gauss high-tail / frozen reflection identity

2026-10-30 Asia/Hong_Kong. **AUTHOR-SIDE / PROVED COEFFICIENTWISE REFLECTION / EXACT FINITE EXECUTION / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.** This is not the native p=373 H0/B0 divided-power experiment and not a proof of the all-prime LIFT.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). Logical Research lane: chatgpt-research-onhour-enterprise-math-20260923; no maintenance-lane identity, session, claim or run was adopted.

## Exact original object and result

Let p=6m+1>=7 be prime, and retain the ORIGINAL Gauss coefficients and high valuation-two source

\[
c_n=\frac{(1/6)_n(1/3)_n}{(n!)^2},\qquad
F_p=\frac1{p^2}\sum_{n=2m+1}^{p-1}c_n\,2^{-n}\pmod p.
\]

Retain the original frozen reflected coefficient family, originally used only for 1<=a<=m in the signed observer R_p:

\[
C_1=\frac1{10},\qquad
\frac{C_{a+1}}{C_a}=\frac{36a^2}{(6a+5)(3a+2)}.
\]

**Theorem (source-indexed high-tail reflection).** The SAME rational recurrence extends without a p-divisible denominator to every 1<=a<=4m, and for each such a

\[
\boxed{\frac{c_{p-a}\,2^{-(p-a)}}{p^2}\equiv C_a\pmod p.}\tag{R}
\]

Consequently, without losing index/provenance information,

\[
\boxed{F_p\equiv\sum_{a=1}^{4m}C_a\pmod p.}\tag{F}
\]

This is a full-prime algebraic statement for all p≡1 (mod 6), stronger than an equality of total sums. The frozen R_p observer continues to use only its original range 1<=a<=i<=m and original signed weights. Extending the C recurrence is an auxiliary computation, not a redefinition or replacement of R_p. The high tail and the reflected cutoff remain separately labeled sources even though their arithmetic carriers coincide.

## Proof

The already established three-stratum coefficient identity gives, for 2m<n<p,

\[
\frac{c_n}{p^2}\equiv
\frac{(-1)^m m!(2m)!(n-m-1)!(n-2m-1)!}{18(n!)^2}\pmod p.\tag{S2}
\]

For any 0<=r<=p-2, Wilson's theorem gives the exact residue

\[
(p-2-r)!\equiv\frac{(-1)^r}{(r+1)!}\pmod p.
\]

Set n=p-1-b=6m-b, 0<=b<=4m-1, in (S2). Apply the complement formula to the two upper factorials and to the denominator (n!)^2. The signs cancel, yielding

\[
V_b:=\frac{c_{p-1-b}}{p^2}\equiv
\frac{m!(2m)!(b!)^2}{18(m+b+1)!(2m+b+1)!}\pmod p.
\]

In particular

\[
V_0=\frac{1}{18(m+1)(2m+1)}\equiv\frac1{10}\pmod p
\]

because m+1≡5/6 and 2m+1≡2/3 (mod p). For 0<=b<=4m-2,

\[
\frac{V_{b+1}}{V_b}
=\frac{(b+1)^2}{(m+b+2)(2m+b+2)}
\equiv
\frac{18(b+1)^2}{(6b+11)(3b+5)}
=\frac12\,\frac{C_{b+2}}{C_{b+1}}\pmod p.
\]

All factors inverted here are p-units: the integer arguments m+b+2 and 2m+b+2 remain in [1,p-1]. Since V_0=C_1, induction gives V_b=2^{-b} C_{b+1}. Fermat's theorem gives 2^{-(p-1-b)}≡2^b (mod p). Multiplication proves (R), with a=b+1. Summing over this exact bijection of indices gives (F). QED.

## Corollary: universal nonhomogeneous Gauss differential endpoint

The last source coefficient satisfies

\[
\boxed{\frac{c_{p-1}}{p^2}\equiv\frac1{10}\pmod p.}\tag{E0}
\]

For the ORIGINAL truncated Gauss polynomial G_p(z)=sum_(n=0)^(p-1)c_n z^n, put

\[
\mathcal L=z(1-z)\partial_z^2+(1-\tfrac32z)\partial_z-\tfrac1{18}.
\]

The exact hypergeometric coefficient recurrence implies the polynomial identity

\[
\mathcal L G_p(z)=-(p-\tfrac56)(p-\tfrac23)c_{p-1}z^{p-1}.
\]

The coefficient of p^2 on the right is -[(5/9)(1/10)] = -1/18. Therefore in the p-local polynomial ring

\[
\boxed{\mathcal L G_p(z)\equiv-\frac{p^2}{18}z^{p-1}\pmod{p^3}.}\tag{E1}
\]

In particular, at z=1/2,

\[
\boxed{G_p''(1/2)+G_p'(1/2)-\tfrac29G_p(1/2)
\equiv-\tfrac29p^2\pmod{p^3}.}\tag{E2}
\]

This is a nonzero order-p^2 **truncation/source defect**. A homogeneous Gauss differential equation is valid for the infinite hypergeometric series but CANNOT be applied to this finite G_p modulo p^3 without retaining (E1). For the original LIFT only the separately established lower-precision differential identities may be reused at their genuine precision; (E2) does not prove LIFT.

## Executed evidence and BRC scope

The exact Python standard-library file d25_gauss_tail_reflection_ode_guard_20261030.py independently constructed the original Gauss coefficients modulo p^3 and the frozen C recurrence modulo p, then verified **each** of the 4m individual index-paired (R) identities, (F), (E0), the exact finite polynomial differential boundary, and (E2). It completed all 330 primes p≡1 mod6 in [7,5000), including 166 of the two frozen target residue classes.

| p | m | F from original high tail | extended sum C_1..C_4m | original-prefix sum C_1..C_m | normalized ODE defect (E2)/p^2 |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 13 | 2 | 8 | 8 | 0 | 7 |
| 19 | 3 | 10 | 10 | 5 | 4 |
| 157 | 26 | 0 | 0 | 106 | 87 |
| 373 | 62 | 252 | 252 | 45 | 207 |

At p=373 the original Gauss G_p(1/2) modulo 373^3 remains 24495656 and its original first derivative modulo 373^2 remains 78545; this is consistent with prior independent three-stratum evidence. Previously frozen signed R_373 remains 196, not the high-tail value 252. No identification F_p=R_p is asserted.

BRC: **COMPOSE_APPLIED** to the existing signed rational, source-indexed, p-valuated coefficient carrier. Population: original Gauss high stratum 2m+1<=n<=p-1 and original reflected C indexing a. Bijection n=p-a, exact weights/valuation, additive observer F_p, and the nonlinear downstream observer 6(M/p)g+p((M/p)^2-R_p)-1 are retained. Mod-p source equality does not license replacing native H0/B0, original odd Green/Hesse, or the signed R observer by this scalar high-tail sum.

## Unfinished frontier and next action

LIFT remains the original all-prime target Delta_p-R_p=0 (mod p) for p≡13,19 (mod24), equivalently A_p≡p (mod p^3) at the previously verified original interface. **Next mathematical unit:** insert (R) termwise into the original three-stratum LIFT harmonic-port expansion and the separately frozen R double sum; attempt an exact finite hypergeometric telescoping identity on the now SHARED C carrier, with the original i/a indices and signs retained. Do not treat the nonhomogeneous ODE as a completed second-digit proof.

The original native p=373 H0/B0 divided-power [X]U mod 139129, rank, genuine semilinear Frobenius/eta, signed odd Green/Hesse and kappa remain NOT_EXECUTED and on support issue #1559 with PENDING_OWNER. The available Site is read-only (research_authority_granted=false, write_relay_enabled=false). No Source session/CLAIM/run or formal Source checkpoint was created. This author-side note and executed code are not mathematical admission or independent review.

Source dependencies: prior original-R-corrected low-root and Gauss three-stratum notes in research_notes/portable_direct/, especially 20261030_onhour_d25_gauss_three_stratum_harmonic_jet_p3.md, and the frozen scientific taskbook at c47e13e4aba0e006366f989d6334d443f6333ae3.