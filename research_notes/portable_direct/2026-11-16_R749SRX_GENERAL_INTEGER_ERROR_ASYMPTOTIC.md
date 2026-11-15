# R749SRX — Sharp square-root scaling for arbitrary integer marked-count errors

**Date:** 2026-11-16 (Asia/Shanghai). **Status:** AUTHOR_EXACT_NOT_REVIEWED.  
**Scientific input:** frozen Walsh auxiliary model \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`; exact predecessor R749SRV–SRW, including \`R749SRV_INTEGER_MARKED_COUNT_CERT.py\`. Independent positive labeled-source calculation; no native signed BRC, P000 force or X6 physical time is identified with the index r.

## The observer and the problem

Fix the five labeled positive source weights \`w=(1,1,2,3,6)\`; source 1 is marked. Put

\[
\Omega_r=\{k\in\mathbb{Z}_{\ge0}^{5}:\sum_iw_ik_i\le r-1\},\quad
C_r=\#\Omega_r,\quad T_r=\sum_{k\in\Omega_r}k_1\qquad(r\ge1).
\]

Use the same degree-four smooth subtraction as the frozen predecessor,

\[
H_4(r)=\tfrac16+\tfrac1{2r}-\tfrac{115}{36r^2}+\tfrac{115}{6r^3}-\tfrac{16315}{108r^4},\qquad
R(r)=r^3T_r/C_r-r^4H_4(r).
\]

The ideal six phases are \`P=(455,-295,-25,185,-25,-295)/36\`. For shifts \`J=(0,1,5)\`, define \`S_a=(P_a,P_{a+1},P_{a+5})\` (all indices modulo six).

For each integer \`M≥0\`, observe the vector
\[
Y_{r,\varepsilon}=\bigl(R(r+h)+\varepsilon_h (r+h)^3/C_{r+h}\bigr)_{h\in J},\qquad
\varepsilon\in([-M,M]\cap\mathbb Z)^3,
\]
with **exact denominator counts** \`C\`. Decode by the **unique** closest ideal \`S_a\` in the \(\ell_\infty\) norm; ties count as failures. Write \`N(M)\` for the least \`N≥1\` such that the decoder succeeds for **every** integer \`r≥N\` and **every** allowed error triple. It exists as proved below.

## Theorem (first general-M scaling law)

\[
\boxed{N(M)=24\sqrt{2M}+O(1)\quad\text{as integer }M\to\infty.}
\]
In particular,
\[
\boxed{\lim_{M\to\infty}N(M)/\sqrt M=24\sqrt2.}
\]
This assertion is specific to the stated source model, ideal signatures, exact denominators and maximum-norm nearest-signature rule. The historical exact results \`N(0)=35\`, \`N(1)=53\`, \`N(2)=65\` are retained.

### Proof

**1. Exact rational generating functions and residual rate.** For ordinary formal power series,
\[
\sum_{r\ge1}C_rz^r=\frac{z}{(1-z)^3(1-z^2)(1-z^3)(1-z^6)},\quad
\sum_{r\ge1}T_rz^r=\frac{z^2}{(1-z)^4(1-z^2)(1-z^3)(1-z^6)}.
\]
The first identity counts a marked-weight-one and four other unrestricted labeled variables under a strict cutoff; the second replaces the marked factor \((1-z)^{-1}\) with \(z(1-z)^{-2}\).

Every denominator zero is a sixth root of unity. Upon multiplying by \((1-z^6)^6\) and \((1-z^6)^7\), respectively, the numerators have degrees at most 23 and 29. Consequently, for each class \`r mod 6\` and all \`r≥36\`, \`C_r\` and \`T_r\` equal polynomials in \`r\` of degrees at most 5 and 6. The leading term at the unit root gives
\[
C_r=\frac{r^5}{4320}+O(r^4),\qquad T_r=\frac{r^6}{25920}+O(r^5).
\]

Exact rational interpolation of these residue-class polynomials, coupled with polynomial division, proves
\[
R(r)=P_{r\bmod6}+\frac{\gamma_{r\bmod6}}r+O(r^{-2}),
\]
where
\[
(\gamma_0,\ldots,\gamma_5)
=\left(\frac{3335}{3},\frac{13780}{9},\frac{12845}{9},
\frac{3740}{3},\frac{11485}{9},\frac{12980}{9}\right).
\]
The certificate establishes for each residue that the polynomial numerator of \(R-P_a\) has degree 4 in \`n=(r-r_0)/6\` while its denominator has degree 5, and computes the exact leading-coefficient ratio. In particular, there are constants \`A,B,r0\` such that, uniformly for \`r≥r0\` and \`h∈J\`,
\[
|R(r+h)-P_{(r+h)\bmod6}|\le B/r,\qquad
\left|\frac{(r+h)^3}{C_{r+h}}-\frac{4320}{r^2}\right|\le A/r^3.
\]

**2. Upper bound.** The six distinct ideal signatures have minimum pairwise maximum-norm separation \`d=15/2\`; direct rational enumeration verifies this. By the triangle inequality, correct decoding is unique whenever the distance of an observation from its true signature is strictly less than \`d/2=15/4\`.

For every admissible \(\varepsilon\),
\[
\|Y_{r,\varepsilon}-S_{r\bmod6}\|_\infty
\le B/r+M(4320/r^2+A/r^3).
\]
Put \(c=\sqrt{4320/(15/4)}=\sqrt{1152}=24\sqrt2\). Substitution of \(r=c\sqrt M+K\) gives
\[
B/r+M(4320/r^2+A/r^3)
=\frac{15}{4}+\frac{-2(15/4)K/c+B/c+A/c^3}{\sqrt M}
+O(M^{-1}).
\]
Choose a fixed \(K_+\) larger than the positive error-constant threshold. The displayed upper bound then falls below \(15/4\) for all \(r\ge c\sqrt M+K_+\) and sufficiently large \(M\): each term in the bound decreases with \(r\). Thus \`N(M)≤c√M+O(1)\`.

**3. Matching lower bound with integer errors, not a continuum relaxation.** The pair \`a=0,b=3\` satisfies
\[
S_3-S_0=\frac{15}{2}(-1,+1,+1).
\]
Choose \(r\equiv0\pmod6\) with \(r=c\sqrt M-K_-+O(1)\), choosing the lower multiple of six, and choose the admissible **integer** error triple
\[
\varepsilon=(-M,+M,+M).
\]
Write \`s=(-1,1,1)\`, \(e_h=R(r+h)-P_{(r+h)\bmod6}\), and
\(t_h=M(r+h)^3/C_{r+h}+s_he_h\). Then exactly
\(Y_h=(S_0)_h+s_ht_h\) and \((S_3)_h=(S_0)_h+s_h(15/2)\).
As \`M→∞\`, uniformly in the three shifts,
\[
t_h=\frac{15}{4}+\frac{2(15/4)K_-/c+O(1)}{\sqrt M},
\]
where the \(O(1)\) is bounded independently of fixed \(K_-\). A sufficiently large *fixed* \(K_-\) ensures
\(15/4<t_h<15/2\) simultaneously for all three coordinates. Therefore
\[
\|Y-S_3\|_\infty=\max_h(15/2-t_h)<15/4
<\max_h t_h=\|Y-S_0\|_\infty.
\]
The true phase zero cannot be decoded; at least one failure occurs at
\(r=c\sqrt M-O(1)\), yielding \`N(M)≥c√M-O(1)\`.

Combining 2 and 3 proves the two-sided \(O(1)\) theorem. \(\square\)

## Exact certificate, reproducibility and scope

The accompanying standard-library script \`R749SRX_GENERAL_COUNT_ERROR_ASYMPTOTIC_CERT.py\` reconstructs all six pairs of exact quasi-polynomials from integer coefficient recurrences. It checks twelve values in each residue class against interpolation, verifies the cancellation of high-degree terms and all six rational \(\gamma_a\), checks the minimal signature separation and the precise integer-error counterexamples inherited from R749SRV–SRW at \`r=52,64\`. Execute:

\`python3 R749SRX_GENERAL_COUNT_ERROR_ASYMPTOTIC_CERT.py > R749SRX_GENERAL_COUNT_ERROR_ASYMPTOTIC_RESULTS.json\`

The certificate reports \`PASS\`. Its 72 interpolation/sample confirmations are finite computational checks; the universal-in-\`r,M\` theorem follows from the generating-function degree argument and the two asymptotic norm estimates, not from finite enumeration. Proof and computed coefficients remain **author exact, not independently reviewed**.

## Open next questions

Find the optimal bounded oscillatory correction \`N(M)-24√(2M)\`, including residue-class competition and integer rounding; determine all finite \`N(M)\` without enumerating \((2M+1)^3\) error triples; extend the model to simultaneous errors in denominator \`C_r\` and numerator \`T_r\` while retaining the labeled-source information. A native signed/BRC bridge remains a separately typed future problem.
