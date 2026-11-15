# R749SRV — Sharp integer-count resolution threshold for six-phase Walsh recovery

Date: 2026-11-16 (Asia/Shanghai). Status: **AUTHOR_EXACT_NOT_REVIEWED**.
Independent portable positive labeled-source model, continuing [R749SRU](https://github.com/awdawmip/enterprise-math/blob/072fb45cf5193894a7c40dd8fe35b1eed378eda3/research_notes/portable_direct/2026-11-16_R749SRU_SHARP_ADVERSARIAL_NOISE_RADIUS.md). Scientific input pin unchanged: \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`. This is an observer-relative source-count theorem and does not assert a native signed X6 event.

## Exact model and new noise semantics

Five **labeled** independent nonnegative integer source multiplicities \(k_i\) have weights \(w=(1,1,2,3,6)\), with the first weight-one source marked. For every integer \(r\ge1\), let
\[
\Omega_r=\{k\in\mathbb Z_{\ge0}^5:k_1+k_2+2k_3+3k_4+6k_5\le r-1\},\quad
C_r=|\Omega_r|,\quad T_r=\sum_{k\in\Omega_r}k_1 .
\]
The unperturbed reading is \(E_r=T_r/(rC_r)\). Define
\[
H_4(r)=\frac16+\frac1{2r}-\frac{115}{36r^2}
+\frac{115}{6r^3}-\frac{16315}{108r^4},
\quad R(r)=r^4(E_r-H_4(r))=\frac{r^3T_r}{C_r}-r^4H_4(r).
\]
The ideal six-phase values are \(P_a=(455,-295,-25,185,-25,-295)_a/36\), with indices modulo 6. For read offsets \(J=(0,1,5)\), the six ideal signatures are
\[
S_a=(P_a,P_{a+1},P_{a+5})\in\mathbb Q^3,\quad a\in\mathbb Z/6\mathbb Z.
\]
Their minimum pairwise \(\ell_\infty\) distance is \(15/2\).

**Different from R749SRU:** retain the exact integer denominator counts \(C_{r+j}\), but allow **one unit of integer error in each marked total**, independently:
\[
\widetilde T_{r+j}=T_{r+j}+\epsilon_j,\qquad
\epsilon_j\in\{-1,0,1\}\quad(j\in J).
\]
The measured scaled residual becomes
\[
\widetilde R(r+j)=R(r+j)+\epsilon_j\frac{(r+j)^3}{C_{r+j}}.
\]
Choose the unique phase minimizing the \(\ell_\infty\) distance of the ordered triple \(\bigl(\widetilde R(r+j)\bigr)_{j\in J}\) to \(S_a\); ties count as failures. The error budget is **one integer in \(T\)**, not a fixed scaled-residual noise radius or a perturbation of the source weights.

## Theorem (sharp all-integer cutoff)

For every integer \(r\ge53\) and all \(3^3=27\) allowed independent integer-error triples, the decoder uniquely returns \(r\bmod6\). The all-integer uniform threshold **53 is least possible**: at \(r=52\), the error vector
\[
(\epsilon_0,\epsilon_1,\epsilon_5)=(-1,1,-1)
\]
makes phase \(3\) the unique nearest signature even though the true phase is \(52\bmod6=4\).

### Infinite tail proof, \(r\ge512\)

The strict-prefix generating functions for the marked weight-one source are
\[
\sum_{r\ge1}C_rz^r=\frac{z}{1-z}\prod_{w\in(1,1,2,3,6)}(1-z^w)^{-1},
\quad
\sum_{r\ge1}T_rz^r=\frac{z}{1-z}\sum_{r\ge1}C_rz^r .
\]
They have pole orders \(6,7\) at \(z=1\), and other poles among sixth roots of unity. Thus \(C_r,T_r\) are exact degree-\(\le5,\le6\) quasipolynomials, respectively, on residue classes modulo six. For each class \(a\), set \(r=r_a+6n\), where \(r_a\) is the unique member of \([512,517]\) in class \(a\). The accompanying certificate reconstructs both polynomials from \(6\) and \(7\) samples, verifies eight subsequent values per class, and forms the two exact rational numerator polynomials for
\[
R(r)-P_a=\frac{B_a(n)}{C_a(n)},\qquad
\frac{35}{12}-(R(r)-P_a)=\frac{U_a(n)}{C_a(n)}.
\]
Every ordinary-power coefficient of \(B_a,U_a,C_a\) is strictly positive in all six classes. Combined with the pole-degree theorem, these finite rational certificates establish the all-integer bound
\[
0<R(r)-P_{r\bmod6}<\frac{35}{12}\qquad(r\ge512).
\]

For each \(r\), restrict each \(k_i\) independently to \(0\le k_i\le\lfloor(r-1)/(5w_i)\rfloor\). Every resulting vector lies in \(\Omega_r\); therefore
\[
C_r\ge\prod_{i=1}^{5}\left(\left\lfloor\frac{r-1}{5w_i}\right\rfloor+1\right)
>\frac{(r-1)^5}{5^5\prod_iw_i}
=\frac{(r-1)^5}{112500}.
\]
It follows that each scaled-residual error is bounded in magnitude by
\[
\frac{r^3}{C_r}<\frac{112500r^3}{(r-1)^5}.
\]
The function on the right decreases strictly for \(r>1\), and at \(r=512\) equals the exact rational
\[
\frac{15099494400000}{34842114263551}<\frac56.
\]
Hence for every \(r\ge512\), every perturbed reading has coordinatewise deviation from its correct ideal signature strictly less than \(35/12+5/6=15/4\). As ideal signatures are separated by at least \(15/2\), the triangle inequality makes the correct one **strictly** closer than every competitor.

### Finite bridge and sharp witness

For every \(53\le r\le511\), compute \(C_r,T_r\) by exact integer coefficient recursion, generate all \(27\) error triples, and compare all six exact rational \(\ell_\infty\) distances. There are **459 cutoffs, 12,393 complete error vectors, and 74,358 signature-distance comparisons**. All decode correctly. The minimum strict rival-distance minus true-distance margin is
\[
\frac{211244629}{3408068268}>0
\]
at \(r=54\), error \((-1,1,-1)\).

At \(r=52\), with the stated error, the exact observed triple is
\[
\left(\frac{52293631}{2699676},\frac{46683721}{2941866},
\frac{283413083}{12270258}\right).
\]
The correct phase \(4\) has distance \(141581357/5883732\), while rival phase \(3\) has strictly smaller distance \(583868191/24540516\). The difference (rival minus true) is
\[
-\frac{60425304925}{222823795194}<0.
\]
Thus any purported smaller universal starting cutoff includes a failure at \(52\), proving sharpness.

For independent coefficient-recursion validation, the certificate also enumerates all labeled tuples directly for \(1\le r\le24\). All arithmetic is Python arbitrary-precision integer or exact \`fractions.Fraction\`; no floating point, heuristic sampling, or missing tail assumption is used.

## Meaning and scope

This result transfers the earlier **scaled-observer perturbation** calculation to a natural **integer count-resolution** model. Its sharp threshold is 53, while the prior unrestricted real scaled-noise uniform theorem at \(r\ge35\) had sharp radius \(1118645/45039528\). The two results have different quantified noise sets and therefore do not conflict.

A compact positive BRC histogram or a labeled integer-source enumeration may implement these counts; retaining the marked-source total and exact \(C_r\) is essential for the declared observer. A provenance-preserving transfer to signed BRC native Port dynamics would require an explicit source/branch/sign/update map. The number \(r\) here is a cutoff, not a physical heartbeat time coordinate.

## Reproduction and next questions

Run \`python3 R749SRV_INTEGER_MARKED_COUNT_CERT.py\` and compare JSON output to \`R749SRV_INTEGER_MARKED_COUNT_RESULTS.json\`. Full computed result is **PASS**. The author has checked the theorem and exact certificate; **independent mathematical review remains open**.

Next: determine optimal integer-error budgets \(M\ge2\) under the same three-read decoder and identify sharp thresholds as a function of \(M\); then extend to simultaneous count errors in \(C_r,T_r\), where the rational transformation is nonlinear, and test whether an observer-safe branch-provenance compression exists.
