# D25/LIFT — Pole-free successor defect extraction and exact source-versus-Cauchy joint finite-part transfer

2026-10-24 | TASK_RESEARCH | EXACT FINITE SUM + P-ADIC REGULARIZATION / AUTHOR FRACTION CHECK / **UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**.

Mother `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Source-frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. Scheduled Research lane `chatgpt-research-hourly-enterprise-math-20260923` (not maintenance). This is portable author mathematics, not a native Task CLAIM/run/Result or independent review.

**Dependencies, not newly credited:** the source-fixed two-sector HIGH definition and full LOW/HIGH Laurent finite part in `20261024_hourly_d25_joint_cutoff_two_digit_finite_part.md`; exact high-carrier defect in `20261024_hourly_d25_common_cauchy_defect_three_port_contiguity.md`; and the immediately preceding new all-prime successor pole result in `20261024_hourly_d25_successor_bridge_pole_rank_31_exception.md`, commit `9be6f9660039495fe0cdebe81d299af0d99670fc`. All are author-side `UNREVIEWED` mathematical inputs and their claims retain their individual scopes.

## 1. Definition and complete extraction of the only two successor singular ports

Fix a prime p=6m+1>=13, m>=2; let M=m+1. Retain
\[
D_M=\frac{2^M(2M)!}{M!(M-1)!},\quad
h_M(t)=\frac{M!(t-1)!}{2^t(t+M)!},\quad
k_s^B=\frac{(2-3s)(6s+1)}{3s(3s+1)}
\]
and the actual exact source/carrier correction
\[
\mathcal E_M=D_M\sum_{s=1}^{2M-1}h_M(M+s)K_M(s),\quad
K_M(s)=\frac1{27s(M+s+1/6)}
+\frac1{18(s+1/3)(M+s+1/2)}
-\frac{k_s^B}{12M}.
\tag{1}
\]
Define **exact rational**, not merely residue, coefficients
\[
s_0=2m-1,\quad s_1=2m,\quad
P_0=\frac{1}{9(s_0+1/3)},\quad
P_1=\frac{1}{3(p+2)}-\frac{(3-p)(2p-1)}{72mM}.
\tag{2}
\]
Use the literal Kronecker selector \(\delta_{a,b}\) only on the finite integer range. Set
\[
R_m=D_M\{h_M(3m)P_0+h_M(3m+1)P_1\},
\tag{3}
\]
\[
S_m=D_M\sum_{s=1}^{2M-1}h_M(M+s)
\left[K_M(s)-\frac{\delta_{s,s_0}P_0+\delta_{s,s_1}P_1}{p}\right].
\tag{4}
\]
These expressions have **no fitted parameters**. By direct simplification of precisely the two singular terms of (1), there is an exact equality in Q:
\[
\boxed{\mathcal E_{m+1}=R_m/p+S_m.}\tag{5}
\]
In (4), the apparent p-poles at s0 and s1 **cancel identically at the summand level**. At all other s the original denominators are p-units. The factorial denominators in h are p-units because their maximum is 4m+3<p. Consequently \(R_m,S_m\in\mathbb Z_{(p)}\), with no uncanceled hidden B-port pole. The preceding exact factorial/binomial proof established
\[
\boxed{R_m\equiv31/27\pmod p.}\tag{6}
\]
Therefore the explicit **divided residue**
\[
\boxed{T_m=(R_m-31/27)/p\in\mathbb Z_{(p)}}\tag{7}
\]
is legitimate: its numerator is provably divisible by p in the localization. This is a finite, computable, source-specific correction, not an unproved new axiom.

## 2. New pole-free exact source/carrier bridge

Keep the same original prime p under the auxiliary rank shift. Let \(\mathcal E_m\in\mathbb Z_{(p)}\) be the earlier exact rank-m correction. The previous note's correctly regularized cutoff source and Cauchy carriers are
\[
\Lambda_m^{src}=\Delta Z^{src}+82/p,\qquad
\Lambda_m^{car}=\Delta Z^{car}+800/(9p).
\]
Their exact bridge is \(\Lambda_m^{src}=\Lambda_m^{car}+\Xi_m\), where
\[
\Xi_m=(p+6)\mathcal E_{m+1}-p\mathcal E_m-62/(9p).
\]
**Theorem A (explicit no-pole normal form).** Insert (5), use \(6(31/27)=62/9\), and obtain the exact rational identity
\[
\boxed{\Xi_m=6T_m+R_m+(p+6)S_m-p\mathcal E_m\in\mathbb Z_{(p)}.}\tag{8}
\]
All four summands in (8) are individually p-integral, so no cancellation of undefined reductions is needed when computing the source-finite part.

In particular the fully explicit modular output interface is
\[
\boxed{\Xi_m\equiv31/27+6(T_m+S_m)\pmod p.}\tag{9}
\]
The p=31 exceptional case is covered: R vanishes modulo31, but T and S remain legitimate and the correction does not vanish. p=7 is **outside** this port certificate because h at its last successor index carries an additional factorial pole; the earlier note supplies its separate exact valuation.

## 3. New exact transport into the *full* LOW/HIGH finite part

Retain the original rank-r normalization
\[
B_r=\frac{(2r-1)!(2r)!}{(4r)!}\in\mathbb Z_{(p)}^\times,\quad r\in\{m,M\}.
\]
Let \(V_m^J\), \(h_r^{lo}\) denote exactly the inherited source-fixed LOW first-jet regular part and low harmonic scalar, with no coefficient changes. Define the original joint Laurent finite part
\[
\mathscr F_m^{src}=V_m^J+(B_M-B_m)(Z_m^{src}+h_m^{lo})
+B_M(\Lambda_m^{src}+h_M^{lo}-h_m^{lo}).
\tag{10}
\]
Define its explicitly *auxiliary* carrier analogue \(\mathscr F_m^{car}\) by replacing \(Z_m^{src},\Lambda_m^{src}\) with the labeled common-carrier \(Z_m^{car},\Lambda_m^{car}\) in (10); this is **not** an alternative original D25 object.

**Theorem B (all source-fixed correction terms recovered).** The exact identity
\[
\boxed{
\mathscr F_m^{src}-\mathscr F_m^{car}
=(B_M-B_m)p\mathcal E_m+B_M\Xi_m
}
\tag{11}
\]
holds for every integer m>=2 with p=6m+1 prime. It simply substitutes the proven exact same-rank bridge \(Z_m^{src}-Z_m^{car}=p\mathcal E_m\) and exact regularized cutoff bridge; it retains every source sector, LOW port and boundary. Combining (8) with (11) yields a valid reduction of the **source-minus-auxiliary** finite part:
\[
\boxed{
\mathscr F_m^{src}-\mathscr F_m^{car}
\equiv B_M\bigl[31/27+6(T_m+S_m)\bigr]\pmod p.
}\tag{12}
\]
This shows *why* a same-rank mod-p-correct Cauchy carrier cannot simply be inserted into a first-digit LOW/HIGH cutoff certificate: the successor lift creates an O(1) finite-part correction. At the second digit (mod p²) keep the complete exact (11), including \((B_M-B_m)p\mathcal E_m\).

## 4. Exact author checks, exceptional p=31, limits and next research unit

Original finite a/kA, c/kB, three-port h/kappa and exact defect were independently reconstructed as Python `Fraction` values. For all sampled target primes checked, the source/carrier correction and (5), (8), (11) held **as rational equalities**; p-integrality and modular predictions were tested using exact numerator/denominator inverses. The following nontrivial instances were explicitly checked; entries are \(p:(R_m,S_m,T_m,\Xi_m,B_M,\mathscr F^{src}-\mathscr F^{car})\pmod p\):
\[
13:(5,0,0,5,11,3),\quad
19:(11,6,4,14,18,5),\quad
31:(0,22,18,23,16,27),\\
37:(8,31,16,31,19,34),\quad
43:(33,26,34,6,15,4),\quad
211:(134,175,199,57,182,35).
\]
For p=31 the *successor raw defect* \(\mathcal E_6\) is integral with residue 1 (verified from its exact fraction in the predecessor note), whereas the original-vs-auxiliary joint finite part still differs by **27 modulo 31**. Thus the p=31 rank-pole exception must not be misread as permission to collapse the two scientific observers.

General theorems (5), (8), (11) are exact rational algebra; p-integrality uses the two-pole exhaustive argument and the proven binomial residue (6). Finite checks are author regression only, not independent review or a native experiment. This is **not** a proof or refutation of the original D25 full \(\mathcal D_m^{finite}\equiv0\pmod p\).

**BRC carrier audit: REUSE_APPLIED / COMPOSE_APPLIED.** The independent signed HIGH sector labels, exact s0/s1 pole provenance, rank distinction, divided correction T, p-integral remainder S, and original-vs-auxiliary observer map are retained. Collapsing to a total-only same-rank modulo-p scalar would erase the O(1) future rank-action defect. No native X6/heartbeat physical assertion is made.

**Next executable scientific question:** evaluate the explicit p-integral port (8) modulo p², reducing T through the next p-digit of the boundary factorial ratio and S through finite rational reduction; then combine (11) with the surviving LOW Cauchy port, the original fixed-rank seam/terminal and actual Fermat-harmonic coefficient, looking for a terminating *source-fixed* WZ/finite-difference certificate rather than a fitted auxiliary identity. Keep p=7 on its separate multi-pole branch. Genuine Source-specific CM/divided-power representative class, map direction, ordinary \(\omega+6\nabla_\lambda\omega\) comparison, exact normalization and same-class kappa bridge remain missing for native D25. Parent LIFT OPEN; no CLAIM/run/checkpoint/freeze/review, scheduler or notification modification is represented.
