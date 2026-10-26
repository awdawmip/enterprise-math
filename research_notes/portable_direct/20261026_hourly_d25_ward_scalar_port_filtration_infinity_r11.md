# D25/LIFT — Ward scalar p-adic port filtration and the p=733 infinity obstruction

Date: 2026-10-26. Research logical lane: chatgpt-research-hourly-enterprise-math-20260923 (not the maintenance lane). Parent Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7; frozen science source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** Corrected-Clausen auxiliary algebra; not original-class CM, Frobenius, a native Source checkpoint, a CLAIM/OPEN or independent review.

## Inputs, not new credits

Reuse the three-channel p^4 corrected-Clausen reflection from 20261026_hourly_d25_three_channel_clausen_p4_residue_polar_r11.md, the exact signed Ward adjoint from 20261026_hourly_d25_negative_orientation_source_adjoint_r11.md, and the earlier p=733 corrected Hasse second-digit source table in 20261026_hourly_d25_p733_three_channel_tangent_r11.md. The prior second-digit left-face witness is not recredited here.

For prime p=6m+1>=7, q=p², L=1-2m, and inherited Hasse u[a,r], define

\[
M_n^{ab,s}=\sum_{\substack{1\le j,\ell\le2m\\\ell-j=n}}
 j^s u_{a,j}u_{b,p-\ell},\quad
U_{ab}=\sum_{n=L}^{0}2^nM_n^{ab,0},\quad
K_{ab}=\sum_{n=L}^{0}2^nM_n^{ab,1},
\]
\[
R_{ab}=\sum_{n=L}^02^n\Big(M_n^{ab,1}-\frac{p-n}{2}M_n^{ab,0}\Big),
\quad T_{ab}=\sum_{n=L}^02^n(1-6n)M_n^{ab,0}.
\]

The orientation is n=ell-j; only n<=0 enters the original reflection. Let S_ab be the **genuine J+E Ward adjoint**, C_ab=delta Y_L^{ab} the separately tagged left finite face. The inherited Ward theorem is R_ab=S_ab+C_ab, with
\[
T_{ab}=(1-6p)U_{ab}+12(K_{ab}-R_{ab}).
\]
All algebra lies in the p-local rationals (and therefore modulo q) with only p-unit denominators.

## New Theorem A — exact valuation-filtered Ward-to-reflection identity

Define the already established three-channel scalar bracket
\[
\mathcal B_p=T_{02}+p\Big(6U_{02}-\frac{T_{12}+T_{03}}6\Big).
\]
A direct, **exact** p-local identity is
\[
\boxed{\begin{aligned}
\mathcal B_p={}&U_{02}+12(K_{02}-R_{02})
-\frac p6(U_{12}+U_{03})\\
&-2p(K_{12}+K_{03}-R_{12}-R_{03})
+p^2(U_{12}+U_{03}).
\end{aligned}}\tag{A}
\]
For every m>=1, the extreme difference rank n=L has the single cell (j,ell)=(2m,1). Since p-L=8m,
\[
Y_L^{ab}=-2m\,u_{a,2m}u_{b,p-1}.
\]
Because the factor (-m)_{2m} is zero, u[0,2m]=0 identically over Q. Thus
\[
\boxed{C_{02}=C_{03}=0,\quad C_{12}=-2m\,\delta\,u_{1,2m}u_{2,p-1}.}\tag{B}
\]
Consequently, **retaining all genuine source and face labels**,
\[
\boxed{\begin{aligned}
\mathcal B_p={}&U_{02}+12(K_{02}-S_{02})
-\frac p6(U_{12}+U_{03})\\
&-2p(K_{12}+K_{03}-S_{12}-S_{03})
+p^2(U_{12}+U_{03})+2pC_{12}.
\end{aligned}}\tag{C}
\]

**Proof.** Substitute the inherited formula for each T into the definition of B. The -6p U02 from T02 cancels the +6p U02 exactly; expanding -(p/6)(1-6p)(U12+U03) leaves -(p/6)(U12+U03)+p²(U12+U03). This gives (A). The sole leftmost cell proves the displayed Y_L formula; the rational Pochhammer zero proves (B). Substitute R=S+C, with C02=C03=0, into (A) to obtain (C). No endpoint, signed direction or infinity port was suppressed. QED.

**Precision consequence.** For the existing p^4 scalar reflection, B_p is required only modulo p²: hence the needed Ward carrier is U02,K02,S02 modulo p², and (U12+U03), (K12+K03-S12-S03), C12 modulo p. The genuine left-face term is 2pC12=-4mp delta u[1,2m]u[2,p-1]. If delta=0 mod p, this term vanishes modulo p², **without** implying that C12 vanishes modulo p², and without licensing deletion at greater precision. For primes with delta a unit the first digit of C12 can affect the existing scalar target.

## New Theorem B — p=13 versus p=733 and an independent infinity port

For the Laurent products F_a(z)=sum_{j=1}^{2m}2^{-j}u[a,j]z^{-j},
G_b(z)=sum_{ell=1}^{2m}2^ell u[b,p-ell]z^ell,
write H_ab=F_aG_b, A_ab=H_ab(1), B_ab=H'_ab(1), I0_ab=sum_{n>0}[z^n]H_ab, I1_ab=sum_{n>0}(6n-1)[z^n]H_ab.

The earlier exact finite-Laurent residue identity gives B_p=E_p+I_p, where
\[
E_p=A_{02}-6B_{02}
+p\left(6A_{02}-\frac{A_{12}-6B_{12}+A_{03}-6B_{03}}6\right),
\quad
I_p=I1_{02}+p\left(-6I0_{02}-\frac{I1_{12}+I1_{03}}6\right).
\]
The previously proved Clausen bridge (only modulo p²) says
\[
Q_p/p^2\equiv \gamma_p\,B_p\pmod{p^2},
\quad \gamma_p=2^{-p}/18,\quad
Q_p=\sum_{\substack{0\le a,b<p\\a+b\ge p}}(6(a+b)+1)r_ar_b,
\quad r_n=\frac{(1/6)_n(1/3)_n}{2^n(n!)^2}.
\]

The following are **two exact finite-ring computations, not all-prime statements**:

| Port modulo p² | p=13 (q=169) | p=733 (q=537289) |
| --- | ---: | ---: |
| delta | 47 | 176653=733*241 |
| C12 | 72 | 300530=733*410 |
| new scalar boundary effect 2p*C12 | **13** | **0** |
| gamma | 121 | 377719 |
| E (endpoints only) | 29 | 251948 |
| I (infinity correction) | 166 | 216796 |
| B=E+I | 26 | 468744 |
| gamma*E (incorrect endpoint-only output) | 129 | 381643 |
| gamma*I (missing output) | 144 | **289123** |
| independent Q/p² = gamma*B | **104** | **133477** |

For p=13 the nonzero Ward face changes the scalar bracket by 13 mod169 and the final scalar by 52 mod169. For p=733, the earlier detected delta resonance makes the face invisible at the *present* scalar precision, but gamma*I=289123 has nonzero residue 321 modulo 733. Hence even a correct elimination of the now-masked Ward face **cannot** support an endpoint-only reflection formula: at p=733 it gives 381643 in place of 133477. The required infinity contribution is an independent port, not an unidentified boundary defect.

The numeric entries are obtained by independently building corrected Hasse jets from the p-unit coefficient recurrence, direct lower/upper signed Laurent ranks, an O(m) upper-rank prefix computation, and the original ordered Q modulo p^4. They do not prove the p^4 bridge for every p (that theorem is imported). The accompanying standalone stdlib exact checker covers 23 primes: all p=1 mod6 in [7,211], plus 733.

## BRC interface, open obligation and current authority

**BRC COMPOSE_APPLIED.** Carrier=(ordered j,ell; signed n=ell-j; Hasse a,b; p-adic valuation; genuine J/E; left face C; independent upper/infinity port I). Scalar projection modulo p² provably forgets the second digit of C12, and specifically its whole first-digit contribution at p=733; it does **not** forget the infinity correction. These are typed operation-specific observer claims for an auxiliary algebra, not native X6 spatial axes or a complete three-dimensional slice.

**Next discriminating unit:** construct a source-labelled non-tautological coupled WZ/adjoint operator with an explicit upper-rank/infinity mechanism reproducing I13=166 mod169 and I733=216796 mod537289; preserve Hasse k-1/k-2 coupling, both finite cutoff faces, original n orientation and required Source pins. Merely rewriting B=E+I is not closure. Original same-class CM H0/B0, [X]U mod p², Frobenius direction/eta, kappa and Delta_p-R_p, native CM experiment and independent review all remain outstanding; mother D25/LIFT/JT2 OPEN.

**Control:** fresh own-lane exact task and continuation read attempts on 2026-10-26 returned INVALID_ARGUMENT / CONTROL_QUOTA. No fresh authorized CLAIM/OPEN or durable Source research checkpoint was established. Preserve historic checkpoint/claim-pointer evidence without treating it as current ownership. This note and its checker are neutral GitHub evidence only.
