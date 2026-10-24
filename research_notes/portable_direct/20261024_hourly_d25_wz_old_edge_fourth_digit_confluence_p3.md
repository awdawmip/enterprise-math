# D25/LIFT — original WZ old edge fourth digit and source-faithful confluence third digit

2026-10-24 | TASK_RESEARCH | portable author-level exact rational proof and 13-prime independent arithmetic reconstruction. **UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**. This is not a native Task CLAIM/run, CM benchmark, Result, or independent review.

**Lineage.** Parent Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; publication \`TP2-B6F4FC938FF94941C1B7\`. Frozen *scientific* Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\` is not changed. Research logical label \`chatgpt-research-hourly-enterprise-math-20260923\` is distinct from maintenance \`chatgpt-hourly-enterprise-math-20260921\`; these labels by themselves grant no authenticated research authority.

**Inputs consumed without renewed authorship credit.** Exact five-tail original WZ identity and factorial summand (c7fb90fd / a7f79955); exact original old-edge product and two-digit expansion (d1d7d345 / the preceding 20261024_hourly_d25_original_wz_confluence_third_digit.md); original HIGH-A/HIGH-B cutoff with pole \(-82/p\) (21c62ae4); exact source-versus-auxiliary Cauchy correction and \(\Xi_m\bmod p^3\) (28e35a1f); port-preserving \(\mathfrak R_m\bmod p^2\) from 20261024_hourly_d25_original_wz_confluence_third_digit.md; independent onhour LOW/Gosper work. The new unit is one additional genuine WZ old-edge digit and the resulting one-additional-digit **full confluence** transport, not a reproof of those sources.

## 1. Fourth-digit finite-product theorem

Fix a prime \(p=6m+1\ge13\), \(m\ge2\), and work in \(\mathbb Z_{(p)}\). Let \(H_n^{(r)}=\sum_{a=1}^n a^{-r}\), \(H_n=H_n^{(1)}\), and \(q=(108^{p-1}-1)/p\in\mathbb Z\). For \(r=1,2,3\), retain the **three distinct source ranges**
\[
h_r=H_{2m}^{(r)},\qquad \widetilde h_r=H_{2m-1}^{(r)},\qquad P_r=H_{p-2}^{(r)}.
\]
The inherited *exact rational* terminal product (the true old \(n=4m\) WZ boundary, not an auxiliary HIGH rank cutoff) is
\[
U_m=\frac{2m}{108^{p-1}}
\left(\prod_{k=2}^{2m}(1-p/k)\right)^2
\frac{\left(\prod_{j=1}^{p-2}(1+p/j)\right)^2}
{\prod_{j=1}^{2m-1}(1+p/j)}.
\tag{1}
\]
Define the following explicit \(p\)-integral finite harmonic coordinates:
\[
\begin{aligned}
\ell_1&=-q-2(h_1-1)+2P_1-\widetilde h_1,\\
\ell_2&=\frac{q^2}{2}-(h_2-1)-P_2+\frac{\widetilde h_2}{2},\\
\ell_3&=-\frac{q^3}{3}-\frac23(h_3-1)+\frac23P_3-\frac{\widetilde h_3}{3},\\
a_1&=\ell_1,\quad a_2=\ell_2+\ell_1^2/2,\quad
a_3=\ell_3+\ell_1\ell_2+\ell_1^3/6.
\end{aligned}
\tag{2}
\]

**Theorem A (all stated primes).**
\[
\boxed{U_m\equiv2m(1+pa_1+p^2a_2+p^3a_3)\pmod{p^4}.}
\tag{3}
\]
Every denominator in (1)–(3) is a \(p\)-unit. The new third correction \(a_3\) retains all three harmonic *ranges* and does **not** assume a Wilson or Wolstenholme quotient is zero. The \(a_i\) are allowed to depend on the fixed prime \(p\); (3) is a congruence of exact rationals, not a formal constant-coefficient series over varying primes.

**Proof.** Divide (1) by \(2m\); \(108^{p-1}=1+pq\) exactly. Apply \(\log(1+x)\equiv x-x^2/2+x^3/3\pmod{x^4}\) separately to each retained factor, legal because each factor is in \(1+p\mathbb Z_{(p)}\). Its coefficients of \(p,p^2,p^3\) are exactly \(\ell_1,\ell_2,\ell_3\) in (2). Then \(\exp(p\ell_1+p^2\ell_2+p^3\ell_3)\) has coefficients \(a_1,a_2,a_3\) shown in (2), proving (3) modulo \(p^4\). QED.

## 2. Fourth digit of the genuine old WZ edge

The **exact** original old WZ-edge coefficient from the inherited seam reduction, after substituting \(m=(p-1)/6\), is
\[
C(p)=\frac{(p+1)(2p-1)^2(30p^2+77p+40)}
{2(p+2)(2p+1)(4p-1)(4p+5)},\quad
\frac{E_0}{p}=U_m C(p).
\tag{4}
\]
Its finite rational expansion at \(p=0\), checked by multiplying both sides by the denominator, is
\[
C(p)\equiv c_0+c_1p+c_2p^2+c_3p^3\pmod{p^4},
\quad
(c_0,c_1,c_2,c_3)=
\left(-2,\frac34,-\frac{393}{40},-\frac{10051}{400}\right).
\tag{5}
\]
Set
\[
\begin{aligned}
d_0&=c_0,&d_1&=c_1+c_0a_1,\\
d_2&=c_2+c_1a_1+c_0a_2,&
d_3&=c_3+c_2a_1+c_1a_2+c_0a_3,\\
\theta_0&=(d_0-d_1)/3,&
\theta_1&=(d_1-d_2)/3,&
\theta_2&=(d_2-d_3)/3.
\end{aligned}
\tag{6}
\]

**Theorem B (fourth digit, all stated primes).** The *original* WZ old-rank edge satisfies
\[
\boxed{\frac{E_0}{p}\equiv
\frac23+p\theta_0+p^2\theta_1+p^3\theta_2\pmod{p^4}.}
\tag{7}
\]
Equivalently, with the uniquely source-normalized WZ edge,
\[
\boxed{\frac{E_0/p-2/3}{p}
\equiv\theta_0+p\theta_1+p^2\theta_2\pmod{p^3}.}
\tag{8}
\]
This is one additional normalized digit beyond the previously published \(J_m+pK_m\) comparison. Equation (8) uses **exact** finite \(P_r=H_{p-2}^{(r)}\), not an unrecorded replacement by a shorter harmonic range.

**Proof.** Multiply (3) by (5) and use \(2m=(p-1)/3\) *exactly*: the product is \((p-1)(d_0+pd_1+p^2d_2+p^3d_3)/3\). Its constant term is \(-d_0/3=2/3\), and its next three coefficients are exactly (6). All rational denominator factors are units for the stated prime class. QED.

## 3. Third-digit confluence certificate with all original ports

Preserve the **distinct** operations at the same fixed \(p\):
\[
\Delta_W=S_{m+1}^{WZ}-S_m^{WZ}=E_0+\sum_{j=1}^{4}E_j,\quad
E_j=W_{m+1,\,4m+j}\in p^2\mathbb Z_{(p)};
\]
\[
\Delta_H=Z_{m+1}^{src}-Z_m^{src}=-82/p+\Lambda_m,\quad
\Lambda_m\in\mathbb Z_{(p)};
\]
\[
\Omega_m=\frac{\Delta_W+(p^2/123)\Delta_H}{p^2},\quad
D_m=(B_{m+1}-B_m)p\mathcal E_m+B_{m+1}\Xi_m,\quad
\mathfrak R_m=\Omega_m-D_m.
\tag{9}
\]
Here \(B_r=(2r-1)!(2r)!/(4r)!\). The \(E_j\) are **actual** new WZ factorial tails, \(Z^{src}\) retains the original HIGH-A/HIGH-B source coefficients, and \(\mathcal E_m\) and \(G_m\) are inherited *different* Cauchy/source quantities.

For complete explicitness, use the previously proved cubic divided successor, with \(c'_0=31/27\),
\[
\Xi_m^{[3]}=c'_0+6t_0+6G_m
+p(t_0+6t_1+G_m-\mathcal E_m)
+p^2(t_1+6t_2),\qquad
\Xi_m\equiv\Xi_m^{[3]}\pmod{p^3}.
\tag{10}
\]
The source-defined \(t_0,t_1,t_2\) are exactly those from Theorem B, equations (9)–(11) of \`20261024_hourly_d25_third_digit_odd_product_source_transfer.md\`; no new approximation of \(G_m\) or \(\mathcal E_m\) is made.

**Theorem C (new full-confluence third digit).** For every prime \(p=6m+1\ge13\),
\[
\boxed{\begin{aligned}
\mathfrak R_m\equiv{}&
\theta_0+p\theta_1+p^2\theta_2
+\sum_{j=1}^{4}\frac{E_j}{p^2}+\frac{\Lambda_m}{123}\\
&-B_{m+1}\Xi_m^{[3]}
-(B_{m+1}-B_m)p\mathcal E_m
\pmod{p^3}.
\end{aligned}}
\tag{11}
\]
This is an **effective finite rational congruence**, not a conjectured cancellation: every term shown is separately \(p\)-integral, every \(E_j/p^2\) has its authentic factorial definition, and \(\Lambda_m\) is computed from the original fixed-coefficient HIGH sums. The newly required precision is \(E_0/p\bmod p^4\), true tails \(E_j/p^2\bmod p^3\), \(\Lambda_m\bmod p^3\), \(\Xi_m\bmod p^3\), \(\mathcal E_m\bmod p^2\), and the exact \(B\)'s. No auxiliary carrier is inserted for a WZ tail.

**Proof.** The five-tail identity and pole cancellation \(82/123=2/3\) give, over \(\mathbb Q\),
\[
\Omega_m=\frac{E_0/p-2/3}{p}
+\sum_{j=1}^{4}E_j/p^2+\Lambda_m/123.
\]
Apply (8), subtract the exact \(D_m\) in (9), and replace \(\Xi_m\) only by its already-proved congruent cubic jet (10). Multiplication by the \(p\)-integral \(B_{m+1}\) preserves the modulus. QED.

## 4. Author reconstruction with exact arithmetic

A focused standard-library \`Fraction\` computation separately reconstructed (i) the original factorial WZ summand
\[
W_{r,n}=
\frac{(6r)!(4r+2n)!(3n)!(6n+12r+1)}
{3^{6r}\,216^n\,(2r)!\,(n!)^2\,((2r+n)!)^2\,(4r+n)!},
\]
(ii) both true WZ sums and four new-rank tails, (iii) original HIGH-A/B finite sums, (iv) the predecessor/successor rational Cauchy correction \(R_m,G_m,\mathcal E_m,\Xi_m\), and (v) the **independently evaluated** product (1) and rational factor (4). For each tested prime, it asserted the **exact rational equality**
\(\Delta_W-\sum_{j=1}^{4}E_j=pU_mC(p)\), then separately verified (7) modulo \(p^4\) and (11) modulo \(p^3\), with modular inverses only for denominators prime to \(p\).

**All 13 author checks passed**, for \(p=13,19,31,37,43,61,67,73,79,97,103,127,211\). The following are numerical residues, *not* an infinite-prime argument or independent review:

| \(p\) | \(p\bmod24\) | \(E_0/p\bmod p^4\) | \(\Omega_m\bmod p^3\) | \(\mathfrak R_m\bmod p^3\) |
|---:|---:|---:|---:|---:|
| 13 | 13 | 1669 | 1093 | **1779** |
| 19 | 19 | 65633 | 410 | **120** |
| 31 | 7 (diagnostic) | 796060 | 14845 | **589** |
| 37 | 13 | — | 42130 | **34807** |
| 43 | 19 | — | 75264 | **10932** |
| 211 | 19 | 1603281883 | 6907656 | **6755912** |

The new third digits do not imply \(\mathfrak R_m=0\). At \(p=31\), the first-digit coincidence remains only an accidental comparison: \(\mathfrak R_m\equiv589=19\cdot31\not\equiv0\pmod{31^2}\). At actual H13/H19 primes \(13,19,43,211\), a nonzero residual rules out only the **uncorrected cross-observer substitution**, not the original LIFT statement.

**BRC/Enterprise coordinates:** \`COMPOSE_APPLIED\`. The typed carrier retains signed rational factors, p-valuation, the original old WZ terminal and four distinct new tails, HIGH-A/HIGH-B sector labels, Cauchy correction and separate future operators; (11) computes a coarse observer only *after* each provenance channel's p-adic jet is preserved. Positive branch mass cannot replace signed cancellation. No native X6 physical claim, P000 modification, CM experiment or Foundation admission follows.

## 5. Exact next unit and acceptance boundary

**New author increment:** the source-faithful fourth digit (3)/(7) and the genuine full-confluence third-digit transfer (11), with exact reconstruction over 13 primes. Previously published third-digit successor, WZ five-tail, original HIGH, LOW and \(\mathfrak R\bmod p^2\) are reused, not counted again.

**Smallest remaining mathematical question:** determine whether a *source-native, same-prime, same-primitive-class* CM/divided-power representative and an explicitly directed, semilinear comparison map send the original ordinary \(\omega+6\nabla_\lambda\omega\) observer to a candidate whose correction retains the full \(\mathfrak R_m\) in (11). A valid positive solution needs the actual primitive class, normalization, map direction, its first p-adic jet and the same-class \(\kappa\) bridge; the existing Source continuation says the concrete \([X]U\bmod p^2\) and fixed \(H_0/B_0\) data sufficient for the K-model \(\kappa\) observer have **not** been source-identified. Thus a true CM comparison or original native benchmark cannot be inferred from this finite transport identity. Use \(p=13,19,211\) first; no repeat of the completed 13-prime author regressions merely for control synchronization.

**Native control boundary:** this portable material does not create an authenticated CLAIM/open, publish a Source task checkpoint, freeze a Result, perform independent review, or change the frozen scientific source. Prior exact Source continuation \`rsch20-continuation-r13-20261024-1530-d25\` (#6262) reported \`execution_authorized=false\`, route \`REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION\`, and a genuine CM representative/normalization dependency; the latest same-lane recovery must be checked before any role-bound mutation. Existing support issue #1558 is the responsible path. D25/LIFT mother objective remains OPEN.
