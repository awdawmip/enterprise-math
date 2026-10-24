# D25/LIFT — genuine original WZ five-port fifth digit modulo p^5

2026-10-25 · TASK_RESEARCH portable mathematical author result. **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT / NO_NEW_NATIVE_CLAIM / NO_SOURCE_CHECKPOINT / NOT_INDEPENDENT_REVIEW.** Source mother: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, **frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3**. This is an author-side, exact local p-adic calculation and is not a CM/DP experiment, Owner handoff, new service identity, native proof admission or completion of the parent Objective.

## 1. Exact inherited objects and the new gap

Fix a prime \(p=6m+1\ge13\); put \(n=2m=(p-1)/3\), and work in \(\mathbf Z_{(p)}\). Define
\[
V_{r,t}=\frac{(6r)!(4r+2t)!(3t)!}
{3^{6r}216^t(2r)!(t!)^2((2r+t)!)^2(4r+t)!},
\qquad W_{r,t}=(6t+12r+1)V_{r,t},\qquad
S_r=\sum_{t=0}^{4r}W_{r,t}.
\]
The existing authentic WZ telescoping identity gives **five distinct labeled ports**
\[
S_{m+1}-S_m=E_0+E_1+E_2+E_3+E_4,\quad
E_j=W_{m+1,4m+j}\ (1\le j\le4).
\]
The previous off-phase proof established \(E_0/p=U_m C_m\) modulo \(p^5\) from its **original** rational product, and another author had already established the genuine four-tail normalized jet modulo \(p^3\), hence the complete original WZ quotient modulo \(p^4\). Those are consumed inputs, not contributions of this note.

**New exact unit:** the first authentic four-tail factorial unit
\(\sigma_p=V_{m+1,4m+1}/p^2\) is now lifted to **modulo \(p^4\)**; the exact four-tail transfer coefficient is lifted by one digit; combining with the *inherited* old edge gives the **full original five-port quotient modulo \(p^5\)**. Neither source-specific CM/DP representatives nor a comparison between distinct primes is inferred.

## 2. New universal fourth normalized digit of the authentic factorial tail

Write \(H_N^{(s)}=\sum_{j=1}^N j^{-s}\), \(H_N=H_N^{(1)}\), and the exact integer Fermat quotients
\[
a=q_p(2)=\frac{2^{p-1}-1}{p},\qquad
b=q_p(3)=\frac{3^{p-1}-1}{p}.
\]
Define three **explicit p-integral** logarithmic coefficients
\[
\begin{aligned}
X_p={}&\frac{2567}{440}-2a-3b-H_{n+4}-2H_{n-1}+2H_{p-1},\\
Y_p={}&-\frac{10548779}{3484800}+a^2+\frac32b^2
+\frac12H_{n+4}^{(2)}-H_{n-1}^{(2)}-H_{p-1}^{(2)},\\
Z_p={}&\frac{4622489459}{766656000}-\frac23a^3-b^3
-\frac13H_{n+4}^{(3)}-\frac23H_{n-1}^{(3)}+\frac23H_{p-1}^{(3)}.
\end{aligned}\tag{1}
\]
With \(L_p=pX_p+p^2Y_p+p^3Z_p\), the **new all-prime theorem** is
\[
\boxed{\displaystyle
\sigma_p\equiv\frac3{220}
\left(1+L_p+\frac{L_p^2}{2}+\frac{L_p^3}{6}\right)
\pmod{p^4}.}\tag{2}
\]
Unlike truncating the old modulo-\(p^3\) result, (1) retains the full-block terms \(2H_{p-1}\) and \(-H_{p-1}^{(2)}\): the facts \(H_{p-1}\in p^2\mathbf Z_{(p)}\) and \(H_{p-1}^{(2)}\in p\mathbf Z_{(p)}\) make these **potentially nonzero third-digit contributions**, not optional errors.

### Proof from the authentic factorials

The exact block decomposition
\[
\frac{(kp+s)!}{p^k}=
k!((p-1)!)^k s!
\left(\prod_{h=0}^{k-1}\prod_{j=1}^{p-1}(1+hp/j)\right)
\prod_{j=1}^{s}(1+kp/j),\quad k=0,1,2,\ 0\le s<p,
\]
applied to the seven original factorial arguments in \(V_{m+1,4m+1}\) first proves \(\nu_p(V_{m+1,4m+1})=2\). The exact Wilson-reflection product
\[
\frac{(p-1)!}{(4m+1)!}
=(-1)^{n-1}(n-1)!\prod_{j=1}^{n-1}(1-p/j)
\]
removes both uncancelled factorial blocks without discarding Wilson-quotient corrections. In particular, it yields the following **exact equality in \(\mathbf Q\)** (not merely a congruence):
\[
\begin{aligned}
\frac{\sigma_p}{3/220}={}&
\prod_{\substack{c\in\{-1,2,5,8,11\}}}
(1+p/c)^{-e_c}\ (1+pa)^{-2}(1+pb)^{-3}\\
&\times
\left[\prod_{j=1}^{n-1}(1-p/j)\right]^2
\left[\prod_{j=1}^{p-1}(1+p/j)\right]^2
\frac{\displaystyle
\prod_{j=1}^{5}(1+p/j)
\prod_{j=1}^{4}(1+2p/j)(1+2p)}
{\displaystyle
\left[\prod_{j=1}^{2}(1+p/j)\right]^2
\prod_{j=1}^{n+4}(1+p/j)},
\end{aligned}\tag{3}
\]
where \((e_{-1},e_2,e_5,e_8,e_{11})=(2,2,2,1,1)\).
Indeed, the source normalization before division by \(\sigma_p/(3/220)\) is
\[
\frac{2880}
{3^{p+5}216^{4m+1}\,n^2(n+1)^2(n+2)^2(n+3)(n+4)},
\]
and \(3^{p+5}216^{4m+1}=3^6\cdot216(1+pa)^2(1+pb)^3\);
also \(3^8n^2(n+1)^2(n+2)^2(n+3)(n+4)=(p-1)^2(p+2)^2(p+5)^2(p+8)(p+11)\). These equalities explain every rational factor and the constant \(3/220\).

Every factor of (3) is a \(p\)-unit with p-adic normalization \(1+O(p)\). Expand \(\log(1+z)\) through degree three. Collecting the coefficient of \(p^s\), \(s=1,2,3\), gives exactly (1): the constant rational parts are respectively
\[
\frac{2567}{440},\qquad
-\frac{10548779}{3484800},\qquad
\frac{4622489459}{766656000}.
\]
The remaining terms are the corresponding \(H^{(s)}\) and Fermat-quotient powers. Thus
\(\log(\sigma_p/(3/220))\equiv L_p\pmod{p^4}\); expanding the exponential through degree three yields (2). No asymptotic fit, CM correspondence, analytic logarithm or non-\(p\)-unit inverse was used. \(\square\)

## 3. Exact new source-ratio transfer and full five-port formula

The unchanged **three original consecutive factorial ratios** are
\[
R_k(p)=\frac{V_{m+1,4m+k+1}}{V_{m+1,4m+k}}
=\frac{(2p+2k+3)(2p+3k-1)(2p+3k)}
{4(2p+3k+1)(p+k+2)(4p+3k+11)},\quad k=1,2,3.
\]
Let
\[
B(p)=\sum_{j=1}^{4}(6p+6j+7)\prod_{k=1}^{j-1}R_k(p).
\]
Exact rational differentiation at \(p=0\), retaining the third logarithmic derivative of **each individually labeled original port**, gives
\[
\boxed{\begin{aligned}
B(p)&\equiv A_0+pA_1+p^2A_2+p^3A_3\pmod{p^4},\\
A_0&=\frac{250809}{17920},\
A_1=\frac{466056841}{63974400},\
A_2=\frac{22193173931}{114194304000},\\
\boxed{A_3}&=\boxed{-\frac{98135062039471}{1630694661120000}}.
\end{aligned}}\tag{4}
\]
Here \(A_0,A_1,A_2\) are inherited; **only \(A_3\) is new**. One source-exact check independent of the Taylor coefficients is
\[
B(p)=\frac{
16320p^9+541568p^8+7893680p^7+66286656p^6+
353196580p^5+1237592632p^4+2850111825p^3+
4157826064p^2+3485426095p+1279125900}
{256(p+2)(p+3)(p+4)(p+5)^3(2p+7)(4p+17)}.\tag{5}
\]
The new accumulated third derivatives \(d^3(\log \prod_{k<j}R_k)/dp^3\vert_{0}\), for \(j=1,2,3,4\), are
\[
(0,\ 10881079/4630500,\ 454017795407/181997172000,\
1548984075869/614240455500).
\]
All denominators of (1)–(5) are \(p\)-units for the stated primes (factors \(2,3,5,7,11,17\), with \(7<13\) and \(17\not\equiv1\pmod6\)).

From exact Source labels, \(\sum_{j=1}^{4}E_j/p^2=\sigma_p B(p)\). Hence (2)+(4) gives the **complete four-tail source sum modulo \(p^4\)**; the vector ports themselves remain distinguishable. Consuming (not re-proving) the original old edge \(E_0/p=U_m C_m\), where
\[
U_m=\frac{2m}{108^{p-1}}
\left[\prod_{k=2}^{n}(1-p/k)\right]^2
\frac{\left[\prod_{j=1}^{p-2}(1+p/j)\right]^2}
{\prod_{j=1}^{n-1}(1+p/j)},\
C_m=\frac{(p+1)(2p-1)^2(30p^2+77p+40)}
{2(p+2)(2p+1)(4p-1)(4p+5)},
\]
yields the **new complete original five-port theorem**
\[
\boxed{\displaystyle
\frac{S_{m+1}-S_m}{p}\equiv U_m C_m+
\frac{3p}{220}
\left(1+L_p+\frac{L_p^2}{2}+\frac{L_p^3}{6}\right)
(A_0+pA_1+p^2A_2+p^3A_3)\pmod{p^5}.
}\tag{6}
\]
The exact \(U_m C_m\) in (6) may instead be evaluated using the already-proved off-phase old-edge fifth-digit formula. Formula (6) is **not** a same-prime CM/DP class match, not a claim about \(\kappa_p\), and not the entire D25/LIFT objective.

## 4. Executed arithmetic falsification

Reproducible standard-library checker:
[original five-port fifth-digit checker](20261025_offphase_d25_original_five_port_fifth_digit_check.py).
It uses exact Python fractions and original factorials, with \(p\)-unit modular inverses; no floats, fitted constants or external algebra CAS are required. Actually executed in this author environment:

* **79/79 PASS** for every prime \(13\le p<1000,\ p\equiv1\pmod6\): sigma formula (2) vs unchanged factorials modulo \(p^4\); \(B(p)\) formula (4) vs the three original ratios modulo \(p^4\); and the total of all four separate original factorial ports modulo \(p^4\).
* **14/14 PASS** for \(p=13,19,31,37,43,61,67,73,79,97,103,109,127,211\): original **complete** \(S_{m+1}-S_m\), independently rebuilt term-by-term as exact fractions, divided by \(p\) and checked against (6) modulo \(p^5\).

| p | sigma mod p^4 | B(p) mod p^4 | (S_{m+1}-S_m)/p mod p^5 |
|---:|---:|---:|---:|
| 13 | 17703 | 3640 | 184865 |
| 19 | 25785 | 66864 | 2080127 |
| 31 | 856221 | 191233 | 13701143 |
| 211 | 1538350290 | 138055265 | 86047380883 |

These are **author-side** exact regression checks, not independent review or a native CM/DP benchmark; the all-prime theorem is (3)–(6), not extrapolation from 79 tests.

## 5. Observer, provenance and succession boundary

**BRC COMPOSE_APPLIED at the labeled external p-adic observer:** carrier \((p,m,\nu_p;\ E_0,E_1,E_2,E_3,E_4;\ \sigma_p,R_1,R_2,R_3;\ L_p,A_0,\ldots,A_3)\), preserving branch provenance, signed rational port values and exact valuation. Summation to (6) is authorized only as that named scalar readout, not a safe quotient for selective CM/DP, HIGH, native X6 or future path operations. The ACTIVE P000 seven-dimensional Heartbeat worldview, six native spatial axes, three-dimensional research slices and residual-fidelity constraint are unchanged; this exact external \(p\)-adic arithmetic is not a native-world realization.

Consumed provenance without contribution transfer:
* [previous old-edge fifth-digit result](https://github.com/awdawmip/enterprise-math/blob/7c783f61dce5b4442b1b45cbe70e4ab399a653ce/research_notes/portable_direct/20261025_offphase_d25_original_terminal_fifth_digit_exact_harmonic_observer.md);
* [other Research lane's original four-tail third jet and complete fourth digit](https://github.com/awdawmip/enterprise-math/blob/60be3714d51d1adb717d5d834f5b92e45f254d2e/research_notes/portable_direct/20261024_hourly_d25_genuine_four_tail_third_jet_full_wz_fourth_digit.md).
The current other-owner Hesse Green descent is a different source/observer and is not duplicated.

**Native status:** service 0.6.11 status was read this turn, but the Site-bound identity has research_authority_granted=false, static_machine_readonly, write_relay_enabled=false, no executor binding. Historical same-lane recovery request d25-r11-recovery-20261024-2144-01 and continuation request d25-r11-continuation-20261024-2149-01 were consumed as read-only historical evidence, not live current authorization. No session/CLAIM/open/publish_checkpoint/Result/freeze/review/release or independent contribution assertion is made; the Source-native mother remains **OPEN**. Existing support owner path: Enterprise Math issue #1558 / actual Source control maintainer.

**Separate UR preservation debt:** the already-completed UR mathematics is not re-proved. The original reported four-file V2 bundle with 94,687 bytes and SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76 still lacks byte-identical recoverable material. Existing neutral staging inventories are not the four-file original. Only a true original 94,687-byte payload with matching digest may receive lawful writer/provenance/checkpoint, after actual Source authority and request reconciliation.

**Next scientific step:** consume any genuinely newer cross-lane checkpoint; the inherited Source-parked core D25/LIFT still needs a same-prime, same-original-primitive-class \(H_0/B_0\) divided-power representative, fixed [X]U mod \(p^2\), specified semilinear map/direction and lawful \(\kappa\)-comparison. The new p^5 WZ formula supplies a complete additional external scalar digit, **not** that missing class bridge. Deliverable remains UNREVIEWED / NOT_ADMITTED; no scheduler or notification settings changed.
