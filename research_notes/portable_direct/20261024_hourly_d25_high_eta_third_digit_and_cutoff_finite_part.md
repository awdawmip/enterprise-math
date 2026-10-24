# D25/LIFT — Exact reflected HIGH boundary factorization, third p-adic digit, and cutoff finite part

2026-10-24 | TASK_RESEARCH, portable exact-rational proof | **TWO NEW ALL-TARGET-PRIME CERTIFICATES / AUTHOR EXACT CHECKS / UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**.

Mother: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin **c47e13e4aba0e006366f989d6334d443f6333ae3** remains unchanged. Research provenance is the logical conversation **chatgpt-research-hourly-enterprise-math-20260923**, separate from the control-maintenance logical conversation and from the onhour Research lane. This is author-side reusable proof evidence, not a native claimant execution, result, independent review or mathematical admission.

**Exact inherited inputs, not new claims:** the original fixed HIGH sectors, signed \(-1/24\) bridge and their two incoming boundary coefficients are in 20261024_hourly_d25_source_fixed_high_beta_euler_transport.md. The preceding 20261024_hourly_d25_fixed_high_cutoff_shift_universal_pole_82.md proved \(p(Z_{m+1}-Z_m)\equiv-82\pmod p\). The other Research lane independently combined that leading residue with LOW and introduced a surviving LOW Cauchy port in 20261024_onhour_d25_joint_low_high_cutoff_pole_one_port.md. **New here** is the exact reflected product for the previously first-digit-only coefficient \(\eta_m\), its full third-digit lift, and the previously unknown first *two integral digits* of the Source-fixed HIGH cutoff shift after removing the \(-82/p\) pole.

## 1. Exact all-m rational factorization

Let \(m\ge1\), put \(p=6m+1\), and for p-adic congruences require \(p\) prime. The fixed HIGH-B incoming coefficient is

\[
\eta_m=c_{m+1,2m}=
\frac{(2m+3)!(3m)!}{2^{2m-1}(m+1)!(4m+2)!}
=\frac{2(2m+3)}{(4m+1)4^m}\,
Q_m,\quad
Q_m=\frac{(2m)!(3m)!}{m!(4m)!}.
\]

Define the **labeled finite multiset** (the two index classes are disjoint)
\[
\mathcal U_m=\{1,3,5,\ldots,2m-1\}
\ \sqcup\ \{2m+1,2m+2,\ldots,3m\}.
\]
Every element is a p-unit when \(p=6m+1\) is prime.

**Theorem 1 (exact rational identity, no primality needed).**
\[
\boxed{\displaystyle
\frac{Q_m}{4^m}=
\prod_{u\in\mathcal U_m}\left(1-\frac pu\right)^{-1},
\qquad
\eta_m=\frac{2(p+8)}{2p+1}
\prod_{u\in\mathcal U_m}\left(1-\frac pu\right)^{-1}.}
\tag{1}
\]

**Proof.** In the denominator of \(Q_m=\prod_{j=1}^m(m+j)/(3m+j)\), use the exact reflection
\(3m+j=p-(3m+1-j)=-(3m+1-j)(1-p/(3m+1-j))\).
After multiplying the finite factors,
\[
Q_m=(-1)^m\frac{\binom{2m}{m}}{\binom{3m}{m}}
\prod_{u=2m+1}^{3m}(1-p/u)^{-1}.
\]
Independently use \(3m=(p-1)/2\) **as an exact integer identity** to expand
\[
\binom{3m}{m}
=(-1)^m\frac{\binom{2m}{m}}{4^m}
\prod_{j=0}^{m-1}\left(1-\frac p{2j+1}\right).
\]
Substitution proves the first identity in (1). The exact formula for \(\eta_m\) and \(m=(p-1)/6\) give the second. These are identities in \(\mathbb Q\), not fitted modular relations. QED.

Let \(H_r^{(s)}=\sum_{j=1}^r j^{-s}\), \(H_r=H_r^{(1)}\), and define the two explicit p-integral sums
\[
S_m:=\sum_{u\in\mathcal U_m}\frac1u
=\boxed{H_{3m}-\tfrac12H_m},
\qquad
T_m:=\sum_{u\in\mathcal U_m}\frac1{u^2}
=\boxed{H_{3m}^{(2)}-\tfrac14H_m^{(2)}}.
\]

**Corollary 1 (third-digit lift, every prime \(p=6m+1\ge7\)).**
\[
\boxed{\displaystyle
\eta_m\equiv16\left[
1+p\left(S_m-\frac{15}{8}\right)
+p^2\left(\frac{S_m^2+T_m}{2}
-\frac{15S_m}{8}+\frac{15}{4}\right)
\right]\pmod{p^3}.}
\tag{2}
\]
Consequently its second-digit formula is
\(\eta_m\equiv16[1+p(H_{3m}-H_m/2-15/8)]\pmod{p^2}\),
strictly strengthening the inherited \(\eta_m\equiv16\pmod p\).

**Proof.** For a finite set of p-units,
\[
\prod_u(1-p/u)^{-1}
\equiv1+pS_m+\tfrac{p^2}{2}(S_m^2+T_m)\pmod{p^3};
\]
this follows by finite multiplication or expansion of the formal logarithm over \(\mathbb Z_{(p)}\), with p odd. Also
\(2(p+8)/(2p+1)\equiv16[1-15p/8+15p^2/4]\pmod{p^3}\).
Multiply and collect terms. Every harmonic denominator is less than p, so this works for p=7 as well. QED.

## 2. Two integral digits of the source-fixed HIGH cutoff shift

Retain the Source-imposed HIGH scalar and both independently labeled sectors:
\[
Z_m=\sum_{s=1}^{m-1}a_{m,s}k_s^A
-\frac1{24}\sum_{s=1}^{2m-1}c_{m,s}k_s^B,
\]
\[
a_{m,s}=2^{m-s}\frac{(2m)!(s-1)!}{(m+s)!(m-1)!},\qquad
c_{m,s}=2^{1-s}\frac{(2m+1)!(m+s-1)!}{m!(2m+s)!},
\]
\[
k_s^A=\frac{4(1-2s)(3s+1)}{(2s+1)(6s+1)},\qquad
k_s^B=\frac{(2-3s)(6s+1)}{3s(3s+1)}.
\]

At fixed \(p=6m+1\), the previously established exact cutoff transport is
\[
Z_{m+1}-Z_m = D_m+W_m,
\quad D_m:=\gamma_m k_m^A-\frac{\eta_m}{24}k_{2m}^B,
\quad\gamma_m=\frac{4(m+1)}m,
\tag{3}
\]
where the complete old-index/last-endpoint remainder, not a fitted constant, is
\[
\begin{aligned}
W_m={}&\sum_{s=1}^{m-1}(\rho^A_{m,s}-1)a_{m,s}k_s^A
-\frac1{24}\sum_{s=1}^{2m-1}(\rho^B_{m,s}-1)c_{m,s}k_s^B\\
&-\frac{\theta_m}{24}k_{2m+1}^B,\qquad
\theta_m=\frac{3m+1}{2(4m+3)}\eta_m,\\
\rho^A_{m,s}&=\frac{4(2m+1)(m+1)}{m(m+s+1)},\\
\rho^B_{m,s}&=\frac{2(2m+3)(m+s)}
{(2m+s+1)(2m+s+2)}.
\end{aligned}
\tag{4}
\]
For every prime \(p=6m+1\ge7\), \(W_m\in\mathbb Z_{(p)}\). For \(m\ge2\), each denominator in (4) is a p-unit. For exceptional \(m=1,p=7\), \(\theta_1=1/14\) is not a 7-unit but its product with \(k_3^B\) is integral; its full contribution is retained.

**Theorem 2 (new finite part, all target primes).** With the same \(S_m,T_m\) as above, define
\[
C_m=-S_m^2-T_m+\frac{77}{12}S_m-\frac{607}{6}.
\]
Then the **unmodified, source-fixed** two-boundary contribution satisfies
\[
\boxed{\displaystyle
pD_m\equiv-82-p\left(\frac{1315}{12}+2S_m\right)
+p^2C_m\pmod{p^3}.}
\tag{5}
\]
In particular
\[
\boxed{\displaystyle
\Lambda_m:=Z_{m+1}-Z_m+\frac{82}{p}\in\mathbb Z_{(p)},
\qquad
\Lambda_m\equiv W_m-\frac{1315}{12}-2H_{3m}+H_m
+pC_m\pmod{p^2}.}
\tag{6}
\]

**Proof.** Substitute \(m=(p-1)/6\) into the *actual* rational boundary weights, without modifying either source-fixed K coefficient:
\[
p\gamma_m k_m^A=
\frac{8(p+5)(4-p)(p+1)}{(p-1)(p+2)}
\equiv-80-116p-90p^2\pmod{p^3},
\tag{7}
\]
\[
p k_{2m}^B=\frac{(3-p)(2p-1)}{p-1}
\equiv3-4p-2p^2\pmod{p^3}.
\tag{8}
\]
Multiply (8) by \(-\eta_m/24\), inserting the independently derived exact-product expansion (2):
\[
-\frac{\eta_m}{24}(pk_{2m}^B)
\equiv-2+p\left(-2S_m+\frac{77}{12}\right)
+p^2\left(-S_m^2-T_m+\frac{77}{12}S_m-\frac{67}{6}\right)
\pmod{p^3}.
\]
Adding (7) gives (5), including the integer constant \(-607/6=-90-67/6\). The exact SHIFT (3) and p-integrality of \(W_m\) imply
\(\Lambda_m=W_m+D_m+82/p\), which yields the p-integrality and the two integral digits (6). For p=7 the apparently nonunit last endpoint is handled as a *product*, never discarded termwise. QED.

This is stronger than the prior \(-82\) principal-pole theorem: it isolates a **canonical, fixed-coefficient p-integral regularized HIGH cutoff observable** and supplies its residue modulo \(p^2\), while retaining all old A and B branches and the last endpoint. The \(m\to m+1\) cutoff is auxiliary at fixed p, not the original D25 forcing at a new prime.

## 3. Executed exact rational checks and scope

Independently implemented in the present author environment using Python integers, factorials and Fraction:
(i) exact equality of the two formulas in (1) for m=1,2,3,5,6,7,10,11,12,35;
(ii) (2) modulo \(p^3\);
(iii) both Taylor expansions (7),(8);
(iv) (5) modulo \(p^3\);
(v) exact two-sector \(Z_{m+1}-Z_m=D_m+W_m\);
(vi) (6) modulo \(p^2\).
All enumerated target-prime instances passed. Sample independently computed residues are:

| p | \(\eta_m\bmod p^3\) | \(\Lambda_m\bmod p^2\) |
|---:|---:|---:|
| 7 | 86 | 24 |
| 13 | 1602 | 133 |
| 19 | 4804 | 192 |
| 31 | 23576 | 247 |
| 37 | 11782 | 1032 |
| 43 | 60216 | 1268 |
| 61 | 184663 | 2880 |
| 211 | 873345 | 22874 |

These finite checks do not establish the all-prime theorems: the exact double-reflection product and finite p-adic expansions prove them. This is an author's independent arithmetic reconstruction, **not** an independently organized Driver review or native Enterprise/X6 experiment.

**BRC use: REUSE_APPLIED / COMPOSE_APPLIED.** The carrier keeps the two signed Source-fixed HIGH branch sets, the incoming \(s=m\) and \(s=2m\) poles, the \(s=2m+1\) last endpoint, exact integer/factorial provenance and \(p\)-valuation. The fixed-p cutoff is the observer; (6) preserves two previously erased integral digits after lawful cancellation of the principal pole. No positive-mass substitution, scalar-only shortcut or native-space transfer is asserted.

**Next uncompleted exact science:** insert (6) into the already derived full LOW/HIGH cutoff Laurent transport (other lane's one-surviving-LOW-port result); determine whether its finite-part remainder admits a terminating rational/harmonic telescoper with explicit LOW Cauchy port and original seam/terminal. Separately the original \(\mathcal D_m^{finite}\equiv0\bmod p\) and the native same-class CM/divided-power comparison, semilinear direction, leading normalization and kappa bridge remain open. Do not claim that fixed-p auxiliary cutoff regularity is the original LIFT proof.

**Publication classification:** portable GitHub evidence only; UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT. The own ordinary-control recovery was read-only SUCCEEDED (request rsch20-recovery-20261024T0823-r09), with no current winning CLAIM/run or unpublished upload. The exact D25 continuation rsch20-d25-cont-20261024T0832-r09 was read-only SUCCEEDED, route REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION, execution_authorized=false; its Source-native parked scientific frontier is preserved. No re-registration, claim, open, checkpoint/freeze/review or scheduler modification has been performed.
