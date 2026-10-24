# D25/LIFT — Successor HIGH bridge pole, universal 31/27 defect, exceptional rank p=31, and corrected finite-part port

2026-10-24 | TASK_RESEARCH | **EXACT RATIONAL DERIVATION + ALL-TARGET-PRIME MODULAR PROOFS / AUTHOR EXACT FRACTION CHECK / UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**.

Mother: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen **scientific** Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. Research lane specified by the scheduling task: `chatgpt-research-hourly-enterprise-math-20260923`, not control maintenance `chatgpt-hourly-enterprise-math-20260921`. This is mathematical author-side portable evidence. No assertion of current Source CLAIM, authorized run, native checkpoint, proof admission or independent review.

## 1. Exact carrier and the fixed-original-prime rank shift

Consume, without claiming as new, the exact coefficient-defect proof `20261024_hourly_d25_common_cauchy_defect_three_port_contiguity.md` and the original fixed-source HIGH pole certificate `20261024_hourly_d25_fixed_high_cutoff_shift_universal_pole_82.md`.

For every integer r>=1 define
```text
D_r = 2^r (2r)! / (r!(r-1)!)
h_r(t) = 2^{-t} r!(t-1)!/(t+r)!
kappa(t) = -2 + (2/3)/(t+1/6) + 1/(t+1/2)
kB(s) = (2-3s)(6s+1)/[3s(3s+1)].
```
The original signed source-fixed HIGH scalar is
\[
Z_r^{src}=\sum_{t=1}^{r-1} a_{r,t}k_t^A-\frac1{24}\sum_{s=1}^{2r-1}c_{r,s}k_s^B,
\]
where \(a_{r,t}=D_rh_r(t)\), \(c_{r,s}=2^{1-s}(2r+1)!(r+s-1)!/[r!(2r+s)!]\), and \(k_t^A=4(1-2t)(3t+1)/[(2t+1)(6t+1)]\). The *auxiliary*, only same-rank mod-p faithful, common carrier is
\[
Z_r^{car}=D_r\left(\sum_{t=1}^{r-1}h_r(t)\kappa(t)
+\frac13\sum_{t=r+1}^{3r-1}h_r(t)\kappa(t)\right).
\]
The inherited **exact rational** repair (all r, not just modulo a prime) is
\[
Z_r^{src}-Z_r^{car}=(6r+1)\mathcal E_r,
\]
\[
\mathcal E_r=D_r\sum_{s=1}^{2r-1}h_r(r+s)\left[
\frac1{27s(r+s+1/6)}
+\frac1{18(s+1/3)(r+s+1/2)}
-\frac{k_s^B}{12r}\right].\tag{E}
\]
For prime \(p=6m+1\) **hold p fixed**, and compare auxiliary rank r=m with r=M=m+1. Then
\[
\Delta Z^{src}=\Delta Z^{car}+(p+6)\mathcal E_M-p\mathcal E_m.
\tag{1}
\]
Unlike \(\mathcal E_m\), the successor \(\mathcal E_M\) need not be p-integral: its port labels are changed.

## 2. New theorem: the successor defect's principal residue

**Theorem 1.** For every prime \(p=6m+1\ge13\), \(M=m+1\),
\[
\boxed{p\mathcal E_M\equiv\frac{31}{27}\pmod p.}\tag{2}
\]
All relevant rational quantities \(p\mathcal E_M\) lie in \(\mathbb Z_{(p)}\). The exceptional small prime p=7 instead gives \(7\mathcal E_2\equiv1\pmod7\).

**Proof.** For m>=2, every factorial factor in \(D_Mh_M(M+s)\), \(1\le s\le2M-1\), is a p-unit, since the maximum denominator factorial index is \(4m+3<p\). In (E), the only p-poles are:
- \(s=2m-1\), where \(M+s+1/2=p/2\);
- \(s=2m\), where \(s+1/3=p/3\) and \(k_s^B\) has \(3s+1=p\).

There is no pole from \(r+s+1/6\), because \(6(r+s)+1\equiv1\pmod6\) and the allowed interval contains no t for which \(6t+1\) is a multiple of p. Therefore, with \(A=D_Mh_M(3m)\),
\[
p\mathcal E_M\equiv
D_M\left[-\frac{h_M(3m)}9+
\left(\frac16-\frac1{4M}\right)h_M(3m+1)\right]\pmod p.
\]
Here \(M\equiv5/6\), and
\[
\frac16-\frac1{4M}\equiv-\frac2{15},\qquad
\frac{h_M(3m+1)}{h_M(3m)}
=\frac{3m}{4(2m+1)}\equiv-\frac3{16}\pmod p.
\]
Thus
\[
\boxed{p\mathcal E_M\equiv-\frac{31}{360}A\pmod p.}\tag{3}
\]

We evaluate A **without assuming** the previously proved \(-82\) pole. Put \(B=D_Mh_M(m)\). Exact factorial cancellation yields
\[
B=\frac{4(m+1)}m\equiv-20\pmod p.
\]
A second exact ratio is
\[
\frac AB=4^{-m}\frac{2m+1}{3(4m+1)}
\frac{\binom{3m}{m}}{\binom{4m}{2m}}.
\tag{4}
\]
For each \(0\le n\le3m\), the elementary exact binomial polynomial identity
\(\binom{2n}{n}=(-4)^n\binom{-1/2}{n}\), together with \(-1/2\equiv3m\pmod p\), gives
\[
\binom{4m}{2m}\equiv16^m\binom{3m}{2m}
=16^m\binom{3m}{m}\pmod p.
\]
All displayed binomial denominators are p-units and the common numerator binomial is nonzero modulo p. Fermat then gives \(64^m=2^{p-1}\equiv1\), and \((2m+1)/(4m+1)\equiv2\), so (4) implies
\[
\boxed{A/B\equiv2/3,\quad A\equiv-40/3\pmod p.}\tag{5}
\]
Substituting (5) in (3) proves \((-31/360)(-40/3)=31/27\). QED.

**Sharp valuation classification.** For all target primes \(p\ge13\) other than p=31, (2) is nonzero and \(v_p(\mathcal E_{m+1})=-1\). For p=31 the principal pole vanishes. Direct exact rational evaluation at m=5, M=6 supplies the final (finite) case:
\[
\mathcal E_6=
\frac{15280005010940055686440885331}
{2486991386114635254532102656000}
\equiv1\pmod{31}.
\]
Its numerator and denominator are both congruent to 9 modulo 31, hence \(v_{31}(\mathcal E_6)=0\). For p=7, \(v_7(\mathcal E_2)=-1\), but the residue differs from (2) because the final r=2 denominator factorial reaches t+r=7 at t=5, introducing one **extra** p-pole into the last B-port; it must not be silently treated as a p-unit.

## 3. New theorem: corrected carrier principal pole and integral bridge

**Theorem 2.** For every prime \(p=6m+1\ge13\), the common-carrier fixed-p cutoff has the **different** universal principal residue
\[
\boxed{p(Z_{m+1}^{car}-Z_m^{car})\equiv-\frac{800}{9}\pmod p.}\tag{6}
\]
The true source-fixed HIGH cutoff retains \(p\Delta Z^{src}\equiv-82\pmod p\); their difference is precisely \(6(31/27)=62/9\).

**Independent proof of (6).** At successor M, every h-factor is p-integral (m>=2). The *only* common-carrier kappa p-poles are the new A-end t=m, with \(m+1/6=p/6\), and the high B-end t=3m, with \(3m+1/2=p/2\). Consequently,
\[
p\Delta Z^{car}\equiv4D_Mh_M(m)+\frac23D_Mh_M(3m)
=4B+\frac23A\pmod p,
\]
as the rank-m carrier is p-integral. Using (5), this equals \(-80-80/9=-800/9\). By (1)-(2), \(p\Delta Z^{src}\equiv-800/9+6(31/27)=-82\), independently recovering the old source-fixed theorem. The original -1/24 B-sector weight is respected; this is not an original fixed-rank LIFT result.

**Corollary (exact p-integral repair coordinate for the *next* WZ step).** Define
\[
\Lambda_m^{src}=\Delta Z^{src}+\frac{82}{p},\qquad
\Lambda_m^{car}=\Delta Z^{car}+\frac{800}{9p}.
\]
Then each is p-integral, and the **exact**, not merely modular, equality
\[
\boxed{
\Lambda_m^{src}=\Lambda_m^{car}+\Xi_m,\quad
\Xi_m=(p+6)\mathcal E_{m+1}-p\mathcal E_m-\frac{62}{9p}
\in\mathbb Z_{(p)}
}\tag{7}
\]
holds for all target primes p>=13. The integrality of Xi follows directly from (2) and \(\mathcal E_m\in\mathbb Z_{(p)}\). The term \(\Xi_m\) is a **genuine surviving correction port**; discarding it loses the original source's mod-p and mod-p² finite part. At p=31 its numerator pole cancels separately, not through a new owner or a different prime.

For p=7, exact Fraction evaluation yields \(p\Delta Z^{car}\equiv3\), \(p\mathcal E_2\equiv1\), and \(p\Delta Z^{src}\equiv2\pmod7\), consistently satisfying (1). Neither (6) nor (7) is claimed at p=7.

## 4. Actual author verification, attribution, limitations, continuation

Using standard-library Python `Fraction` and factorial integers, **independently reconstructed** each original a/kA and c/kB finite sum, the auxiliary Cauchy h/kappa sum and the rational correction (E). Checked the exact equality \(Z_r^{src}-Z_r^{car}=(6r+1)\mathcal E_r\), then evaluated p-adic residues of all three fixed-p successor differences for all **80 primes p≡1 (mod 6) with p<1000**. All passed the stated formulas, with the p=7 separate case. Checks are author regression only; proofs of the universal modular statements are in Sections 2-3.

Sample values, each tuple \((p;\;p\Delta Z^{src},\ p\Delta Z^{car},\ p\mathcal E_{m+1})\bmod p\):
\[
7:(2,3,1),\quad13:(9,5,5),\quad19:(13,4,11),\quad31:(11,11,0),\quad211:(129,169,134).
\]
In particular p=31 is the **unique target-prime p>=13 with no first-order singularity in the successor bridge defect**. At this one prime it remains a nonzero integral correction, rather than a zero expression.

**BRC information interface: REUSE_APPLIED / COMPOSE_APPLIED.** Preserve the signed original HIGH-A and HIGH-B provenance; keep rank m vs M, the t=m and t=3m Cauchy pole orbits, s=2m-1 and s=2m defect ports, exceptional p=7 terminal, p=31 valuation, and exact rational correction Xi. Observing only the mod-p same-rank carrier erases rank-transport information; Xi repairs that loss. No positive-mass BRC arithmetic, native X6 experiment or independent review was performed.

**Next minimal scientific action:** insert \(\Lambda_m^{car}+\Xi_m\), NOT \(\Lambda_m^{car}\) alone, into the existing full LOW/HIGH Laurent finite part \(\mathscr F_m\) from `20261024_hourly_d25_joint_cutoff_two_digit_finite_part.md`. Derive \(\Xi_m\bmod p^2\) from the exact labeled ports, including p=31 and separate p=7 handling, then attempt source-fixed coupled terminating finite-difference/WZ certificate with both seams, n=4m terminal, LOW first jet, genuine Fermat/harmonic correction and full \(\mathcal D_m^{finite}\). Do not change original source coefficients to fit auxiliary cancellations.

Native D25 additionally still requires real source-specific divided-power/CM representative class, map direction and semilinearity, comparison to ordinary \(\omega+6\nabla_\lambda\omega\), exact leading normalization and same-class bridge/kappa. No such input is asserted here. Parent LIFT remains OPEN. Official status **UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**, and last known ordinary-control canonical dispatch returned `FAILED: TimeoutExpired` (not NO_DISPATCH). No session mutation, CLAIM, open, freeze, review, scheduler or notification mutation is claimed.
