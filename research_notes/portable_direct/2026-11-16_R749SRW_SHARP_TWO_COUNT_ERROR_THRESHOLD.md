# R749SRW — Sharp two-integer marked-source error threshold

Date: 2026-11-16 (Asia/Shanghai). **AUTHOR_EXACT_NOT_REVIEWED.**
This extends the exact labeled-source integer-resolution theorem [R749SRV](./2026-11-16_R749SRV_INTEGER_MARKED_COUNT_RESOLUTION.md) using the same original frozen Walsh auxiliary science \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Source weights, observer, and three-read shift set remain unchanged.

## Problem and theorem

The five **labeled** positive integer source weights are \((1,1,2,3,6)\); the first source is marked. At integer cutoff \(r\ge1\), let
\[
\Omega_r=\{k\in\mathbb Z_{\ge0}^{5}:\sum_iw_ik_i\le r-1\},\quad C_r=|\Omega_r|,\quad T_r=\sum_{k\in\Omega_r}k_1.
\]
Define
\[
R(r)=\frac{r^3T_r}{C_r}-r^4H_4(r),\quad
H_4(r)=\frac16+\frac1{2r}-\frac{115}{36r^2}+\frac{115}{6r^3}-\frac{16315}{108r^4}.
\]
The six period-six ideal phase values are \(P=(455,-295,-25,185,-25,-295)/36\) and three-read ideal signatures are \(S_a=(P_a,P_{a+1},P_{a+5})\), indices reduced modulo six. Their smallest pairwise \(\ell_\infty\) separation is \(15/2\).

**Two-integer measurement errors** mean that denominators \(C_{r+h}\) are exact while the three marked integer totals have independent errors \(\epsilon_h\in\{-2,-1,0,1,2\}\), for \(h\in\{0,1,5\}\). The measured vector is
\[
Y_\epsilon(r)=\left(R(r+h)+\epsilon_h\frac{(r+h)^3}{C_{r+h}}\right)_{h=(0,1,5)}.
\]
Decode by the unique nearest \(S_a\) under maximum norm; a tie is a failure.

**Theorem.** For every integer \(r\ge65\) and every one of the \(5^3=125\) allowed error vectors, the decoder uniquely returns \(a=r\bmod6\). The least all-integer threshold is exactly **65**: at \(r=64\), error \((-2,+2,-2)\) produces a unique false phase \(3\) rather than the true phase \(4\).

## Proof and reproducible certificate

**Infinite tail.** The marked-weight-one generating functions are
\[
\sum_{r\ge1}C_rz^r=\frac z{1-z}\prod_{w\in(1,1,2,3,6)}(1-z^w)^{-1},
\quad\sum_{r\ge1}T_rz^r=\frac z{1-z}\sum_{r\ge1}C_rz^r.
\]
Their rational denominators have poles only at sixth roots of unity, with pole orders 6 and 7 at 1. Consequently \(C_r,T_r\) are degree-\(\le5,\le6\) exact quasipolynomials in each of six residue classes, respectively. The fully reproduced R749SRV six-polynomial certificate constructs these by exact rational interpolation and verifies the positive coefficients of two numerator polynomials, proving for every integer \(r\ge512\):
\[
0<R(r)-P_{r\bmod6}<35/12.
\]

The fully explicit integer grid injection from R749SRV supplies
\[
C_r>\frac{(r-1)^5}{112500},\quad
\left|\epsilon_h\right|\frac{(r+h)^3}{C_{r+h}}
<\frac{225000(r+h)^3}{(r+h-1)^5}.
\]
The function \(225000u^3/(u-1)^5\) strictly decreases for \(u>1\); at \(u=523\) its exact value is
\[
\boxed{\frac{447048959375}{538294594356}<\frac56}.
\]
Thus all three perturbed coordinates for \(r\ge523\) lie within \(35/12+5/6=15/4\) **strictly** of the correct signature. As the other five signatures are separated by at least \(15/2\), the triangle inequality guarantees strict unique decoding for every integer \(r\ge523\).

**Exact finite bridge.** For all \(65\le r\le522\), iterate **458** cutoffs, **125** integral errors at each cutoff and all **six** phase sites. The accompanying Python certificate carries out **57,250 complete exact-error-vector tests** and **343,500 rational signature-distance comparisons**, using arbitrary-precision integers and \`fractions.Fraction\`. Every competitor minus true distance is positive; the minimum is
\[
\boxed{\frac{456681943}{13305600828}}
\]
at \(r=66,\ \epsilon=(-2,2,-2)\), rival phase \(3\). It recomputes the six residue-class positivity certificates from the unchanged original data, rather than inferring an infinite claim from the finite search.

**Sharpness.** At \(r=64\), \(\epsilon=(-2,2,-2)\), the three exact perturbed readings are
\[
\left(\frac{5756801}{371844},\frac{70116085}{5589837},\frac{145922869}{7358715}\right).
\]
The correct phase \(4\) has max distance \(463686775/22359348\); rival phase \(3\) has strictly smaller distance \(604132351/29434860\). The rival-minus-correct gap is
\[
\boxed{-\frac{216897888749}{1015654750110}<0}.
\]
A successful universal starting threshold cannot be smaller than 65, since it would include this failure at 64. The bridge and tail establish that 65 suffices. \(\square\)

## Interpretation and next work

R749SRV handled one-count errors with exact minimum threshold 53. R749SRW handles two-count errors and raises the sharp threshold to 65. Both are unconditional *within this positive labeled-source observer* and the specified maximum-norm nearest-signature rule. No identification of the cutoff \(r\) with heartbeat time, native signed BRC port or P000 force event has been made.

**Reproduction:** Execute \`python3 R749SRW_TWO_COUNT_ERROR_CERT.py\` in the directory containing the existing \`R749SRV_INTEGER_MARKED_COUNT_CERT.py\`; compare exact JSON with \`R749SRW_TWO_COUNT_ERROR_RESULTS.json\`. This is a dependency on the specific previously authored algorithm; all source code is preserved in the same branch/PR. Author exact arithmetic passed; independent review remains pending.

**Next research:** Establish a formula/asymptotic for sharp integer count-error threshold \(N(M)\) for general \(M\), find the first nontrivial simultaneous \(C_r\) and \(T_r\) error class, and investigate source- and sign-preserving typed maps to native BRC observations.
