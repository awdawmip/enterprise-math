# D25/LIFT — Observer-specific Ward boundary precision and direct original-Q certificate

2026-10-26. TASK_RESEARCH lane: chatgpt-research-hourly-enterprise-math-20260923, not CONTROL_PLANE_MAINTENANCE (chatgpt-hourly-enterprise-math-20260921). Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

**Status:** AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. No native CM/Frobenius experiment, authorized CLAIM/OPEN, Source checkpoint, formal review or LIFT/JT2 conclusion is asserted here.

## Consumed exact inputs (not new findings)

- 20261026_hourly_d25_three_channel_clausen_p4_residue_polar_r11.md: ordered original Clausen Q and its corrected-Hasse three-channel reflection.
- 20261026_hourly_d25_negative_orientation_source_adjoint_r11.md: genuine signed Ward internal J+E source plus finite left boundary.
- 20261026_hourly_d25_p733_three_channel_tangent_r11.md: independently computed p=733 U/T/K/B/C rows; the p=13 rows were checked in the earlier Fraction reference.

For any prime p=6m+1>=7, modulo q=p², use the signed lower-rank observers U_ab,T_ab,K_ab and distinct Ward source ports B_ab,C_ab of these notes. Their exact established identities are

\[
T_{ab}=(1-6p)U_{ab}+12K_{ab}-12(B_{ab}+C_{ab})\pmod q,
\]

and, writing \(\mathcal Q_p=Q_p/p^2\) and \(s_p=2^{-p}/18\),

\[
\mathcal Q_p=s_p\left[T_{02}+p\left(6U_{02}-\frac{T_{12}+T_{03}}6\right)\right]\pmod q.
\]

All fractions here are p-units.

## Theorem: sharp observer-specific boundary thresholds

Substituting the Ward identity into each of the three channels and reducing only terms genuinely divisible by p² yields

\[
\boxed{\mathcal Q_p=s_p\left[
 U_{02}+12(K_{02}-B_{02}-C_{02})
 -\frac p6(U_{12}+U_{03})
 -2p(K_{12}+K_{03})
 +2p(B_{12}+B_{03}+C_{12}+C_{03})
\right]\pmod{p^2}.}\tag{1}
\]

**Proof:** the \(-6pU_{02}\) and \(+6pU_{02}\) terms cancel; in the remaining two channels, the outer factor p removes only the \(-6p\) terms. No signed orientation, left boundary or infinity compensation is suppressed in the derivation. Formula (1) follows formally in the p-local ring. QED.

In the *formal projection of this source-labelled expression* which deletes C_12 alone while keeping all other displayed coordinates fixed,

\[
\boxed{\mathcal Q_p-\mathcal Q_p^{(\neg C_{12})}
       =2p\,s_p C_{12}\pmod{p^2}.}\tag{2}
\]

Since s_p is a p-unit, the deletion is safe for this **specific scalar readout modulo p² iff C_12=0 mod p**. The same iff holds for C_03; deletion of C_02 requires C_02=0 mod p²; joint deletion of C_12+C_03 requires their sum to be zero mod p. This is an exact *observer-fiber condition*, not permission to alter a constrained hypergeometric source while pretending its Ward relations remain valid. In particular this two-digit scalar quotient does not authorize deleting C_12 from the complete T_12 mod p² or in any higher-precision future observer.

## New independent original ordered hypergeometric certificate

Instead of recycling the corrected-Hasse recurrence, recompute the original Clausen coefficient sequence modulo p⁴ via

\[
r_0=1,\qquad r_{n+1}=r_n\frac{(6n+1)(3n+1)}{36(n+1)^2},
\]

and evaluate every *ordered* pair in

\[
Q_p=\sum_{\substack{0\le a,b<p\\a+b\ge p}}(6(a+b)+1)r_ar_b
\pmod{p^4}.
\]

The companion standard-library checker independently performs this O(p²) original sum (no floating point), checks Q_p is divisible by p², checks the independent preexisting Ward-port tuples, and verifies (1)-(2).

| Certificate | p=13 (mod 169) | p=733 (mod 537289) |
| --- | ---: | ---: |
| Original Q_p mod p⁴ | 17576 | **71715723853** |
| Original Q_p/p² mod p² | 104 | **133477** |
| Bracket from (1) mod p² | 26 | **468744** |
| s_p mod p² | 121 | **377719** |
| Actual left-face C_12 mod p² | 72 | **300530=733·410** |
| Projected scalar loss 2p s_p C_12 | **52** | **0** |
| Projected quotient after dropping C_12 | 52 | **133477** |

For p=733, the source-bracket residues (all mod 537289) are:

| Source label | residue |
| --- | ---: |
| U_02 | 194980 |
| 12 K_02 | 937 |
| -12 B_02 | 364452 |
| -12 C_02 | 0 |
| -p(U_12+U_03)/6 | 16859 |
| -2p(K_12+K_03) | 397286 |
| +2p(B_12+B_03) | 31519 |
| +2p(C_12+C_03) | 0 |
| sum | **468744** |

Thus \(377719\cdot468744=133477\pmod{537289}\), independently matching the original ordered Q_733. The p=733 boundary is *invisible only to the stated two-digit scalar projection*: deleting C_12 from the full Hasse T_12 changes that channel by \(-12C_{12}\), and \(12C_{12}=382626=733\cdot522\not\equiv0\pmod{537289}\). At p=13 the scalar itself is sensitive, with loss 52 mod169. This counterpair sharply separates source preservation from a particular quotient's allowed information loss.

**BRC COMPOSE_APPLIED:** carrier = ordered pair, oriented rank, Hasse channel, separate Ward internal/left boundary, p-adic valuation and target observer. Operations = recurrence, cutoff, adjoint decomposition, conditional projection; exact safe quotient is proved only for the declared scalar and precision. Auxiliary formal ranks are not P000 Cell coordinates, native axes or a three-dimensional native slice.

Next unresolved mathematics: derive a *separately justified* third normalized digit of the original ordered Clausen tail including all newly needed Hasse jets, finite faces and infinity sources, then test whether C_12/p=410 at p=733 survives or cancels. Do not lift (1) one extra digit by fiat. Original same-class H0/B0, [X]U mod p², semilinear Frobenius eta and direction, kappa, native Delta_p-R_p, native experiment and independent review remain pending. D25/LIFT/JT2 parent OPEN.

Control provenance (read only): fresh recovery https://github.com/awdawmip/kimi-query-bridge/issues/6520; exact continuation https://github.com/awdawmip/kimi-query-bridge/issues/6521, with paged original receipt https://github.com/awdawmip/kimi-query-bridge/issues/6522 and https://github.com/awdawmip/kimi-query-bridge/issues/6523. They do not grant current execution authority. Historic last CLAIM and persisted-checkpoint predecessor remain mismatched; control owner support https://github.com/awdawmip/enterprise-math/issues/1558. This file is not a native checkpoint.