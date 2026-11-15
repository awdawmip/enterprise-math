# R749SRU — Exact sharp adversarial noise radius for six-phase Walsh source recovery

Date: 2026-11-16 (Asia/Shanghai). Status: **AUTHOR_EXACT_NOT_REVIEWED**. Independent portable labeled-source study continuing [R749SRT@990a7324](https://github.com/awdawmip/enterprise-math/blob/990a7324b1950fd0d31ae3b07313c87e2c3e3303/research_notes/portable_direct/2026-11-16_R749SRT_MULTIREAD_SHARP_PHASE_THRESHOLDS.md); unchanged frozen auxiliary Walsh scientific pin: \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`.

## Exact model, observer and perturbation

Retain all five **labeled** positive integer sources with weights \((1,1,2,3,6)\), first source marked. For every integer \(r\ge1\), let
\[
\Omega_r=\{(k_1,\ldots,k_5)\in\mathbb Z_{\ge0}^{5}:
k_1+k_2+2k_3+3k_4+6k_5\le r-1\},\quad
C_r=|\Omega_r|,\quad T_r=\sum_{\Omega_r}k_1.
\]
Put \(E_r=T_r/(rC_r)\) and
\[
H_4(r)=\frac16+\frac1{2r}-\frac{115}{36r^2}
+\frac{115}{6r^3}-\frac{16315}{108r^4},
\qquad R(r)=r^4(E_r-H_4(r)).
\]
As previously established and independently recertified below, its ideal periodic component is
\[
P(a)=\frac1{36}(455,-295,-25,185,-25,-295)_a,\qquad a\bmod 6.
\]
For the three cutoff offsets \(A=\{0,1,5\}\), define ordered signatures and **actual** exact observations
\[
S_a=(P(a),P(a+1),P(a+5)),\qquad
Y(r)=(R(r),R(r+1),R(r+5)).
\]
Indices of \(P\) are reduced modulo six. For any measurement perturbation \(\eta\in\mathbb R^3\), decode by the unique minimizer of \(\|Y(r)+\eta-S_a\|_\infty\) over all six phases; **ties count as decoding failures**. Here noise acts on the three *scaled residual readings*, not the original count vector or the native Heartbeat time evolution.

## Theorem: all-integer sharp uniform noise tolerance

Let
\[
\boxed{\rho_*=\frac{1118645}{45039528}\approx0.0248369609912431.}
\]
**For every integer \(r\ge35\) and every real perturbation \(\eta\) with \(\|\eta\|_\infty<\rho_*\), the decoder returns the correct residue \(r\bmod6\) uniquely.** The bound is **sharp as a strict uniform guarantee**: at \(r=36\), a perturbation of norm exactly \(\rho_*\) produces a minimum-distance tie between phases 0 and 3. In particular the strong zero-noise recovery threshold 35 from R749SRT remains valid, but its worst-case near-threshold robustness is quantified exactly.

### Proof: rational finite bridge plus an infinite tail

Write the exact zero-noise gap
\[
m(r)=\min_{b\ne r\bmod6}\|Y(r)-S_b\|_\infty-\|Y(r)-S_{r\bmod6}\|_\infty.
\]
Every distance to a fixed site is 1-Lipschitz in the \(\ell_\infty\) perturbation. Thus under \(\|\eta\|_\infty<\tfrac12m(r)\), all competing phases remain strictly farther away. The positive gap theorem reduces robustness to an exact all-integer lower bound for \(m(r)\).

The strict-prefix count and marked count have generating functions
\[
\sum_{r\ge1} C_rz^r=\frac{z}{1-z}\prod_{w\in(1,1,2,3,6)}(1-z^w)^{-1},\quad
\sum_{r\ge1} T_rz^r=\frac{z}{1-z}\sum_{r\ge1} C_rz^r.
\]
The only poles are sixth roots of unity, with total pole orders at \(z=1\) equal to 6 for \(C\) and 7 for \(T\). Hence on each residue class modulo six, the two count functions are *exact* polynomials in the step index of degrees at most 5 and 6. The self-contained certificate reconstructs these from respectively 6 and 7 consecutive values, checks 8 further samples per class, and derives polynomial numerators \(B_a(n)\) and \(U_a(n)\) in ordinary powers of \(n\) satisfying
\[
R(r)-P(a)=B_a(n)/C_a(n),\qquad
35/12-(R(r)-P(a))=U_a(n)/C_a(n), \quad r=r_a+6n.
\]
All coefficients of \(B_a,U_a,C_a\) are *strictly positive* for each of the six classes; \(r_a\) is the first integer in \([512,517]\) in class \(a\). Therefore
\[
0<R(r)-P(r\bmod6)<35/12\quad\text{for all integers }r\ge512.
\]
The six ideal three-read signatures have minimum pairwise \(\ell_\infty\) distance \(15/2\), so
\[
m(r)>\frac{15}{2}-2\frac{35}{12}=\frac53\qquad(r\ge512).
\]
Consequently every noise vector of norm \(<5/6\) is harmless throughout the infinite tail.

For the finite bridge, exact integer coin-change dynamic programming computes \(C_r,T_r\), independently checked by direct recursive enumeration for \(1\le r\le24\). Exact \`fractions.Fraction\` evaluations of all five rival distances for **each \(35\le r\le511\)** (477 cutoffs, 2,385 rival comparisons) give the **strict** minimum
\[
\boxed{\min_{35\le r\le511}m(r)=\frac{1118645}{22519764}=2\rho_*,\text{ attained at }r=36.}
\]
Since \(\rho_*<5/6\), this is also the all-integer lower bound. The Lipschitz inequality proves correct unique decoding for all \(\|\eta\|_\infty<\rho_*\).

To establish sharpness, at \(r=36\) calculate
\[
Y(36)=\left(\frac{2144573}{56916},\frac{778682}{32049},
\frac{1028249}{50193}\right),\quad
S_0=\left(\frac{455}{36},-\frac{295}{36},-\frac{295}{36}\right),\quad
S_3=\left(\frac{185}{36},-\frac{25}{36},-\frac{25}{36}\right).
\]
Take \(\eta_*=(-\rho_*,+\rho_*,0)\). Direct rational comparison gives
\[
\|Y(36)+\eta_*-S_0\|_\infty
=\|Y(36)+\eta_*-S_3\|_\infty
=\frac{4393500977}{135118584},
\]
and the other four signatures are strictly farther. Thus the prescribed unique-decoder fails at noise norm exactly \(\rho_*\). \(\square\)

### Cross-check: exact competitor-cone distance

For arbitrary sites \(A,B\in\mathbb R^q\) and reading \(y\), the closest adversarial tie or defeat region is
\(V_B(A)=\{z:\|z-B\|_\infty\le\|z-A\|_\infty\}\).
Partition \(V_B(A)\) by a coordinate \(i\) and sign \(\sigma\) attaining \(\|z-A\|_\infty=\sigma(z_i-A_i)\). Feasibility requires \(\sigma(B_i-A_i)\ge0\). For such \((i,\sigma)\), the minimum \(\ell_\infty\) perturbation is
\[
\delta_{i,\sigma}=
\max\left\{0,\ \sigma\left(\frac{A_i+B_i}{2}-y_i\right),\
\max_{j\ne i}\frac{|y_j-B_j|-\sigma(y_i-A_i)}2\right\}.
\]
For equality \(A_i=B_i\), retain both signs. This follows by choosing \(z_i=y_i+\sigma\delta\) and intersecting each remaining coordinate's noise interval with the interval \([B_j-t,B_j+t]\) for \(t=\sigma(z_i-A_i)\). Taking the minimum over admissible coordinate/sign pairs yields the **exact** distance from \(y\) to the rival-error region. The certificate separately evaluates all 2,385 rival cones; its global optimum is again \(\rho_*\) at \(r=36\), against rival phase 3.

## Asymptotic contrast and information scope

For every phase \(a\), the nearest distinct ideal signature is at \(\ell_\infty\) distance \(15/2\). Since \(Y(r)\to S_{r\bmod6}\) along each residue class, and distance to the closed error region is continuous, the phase-specific robustness radius tends to \(15/4\) as \(r\to\infty\). The all-integer uniform threshold is governed by the exceptional finite cutoff \(r=36\), not by the asymptotic signature separation.

This is an **auxiliary positive labeled-source observer** calculation. The signature is a prospective compression under the declared cutoff-shift observations; it is not itself a signed native BRC port, an X6 state update, or a heartbeat-time parameter. A transfer needs a separately typed provenance-preserving observer/update map.

## Reproduction, provenance and remaining research

- Run the standard-library-only file \`R749SRU_SHARP_ADVERSARIAL_NOISE_CERT.py\` under Python 3; it emits \`R749SRU_SHARP_ADVERSARIAL_NOISE_RESULTS.json\`. Tested using exact Python integer and rational arithmetic with output \`PASS\`. The program also checks the complete rival-cone formula and reconstructs the six strictly positive tail polynomials; no floating arithmetic is used in the certificate.
- Finite domain: all \(r=35,\ldots,511\); infinite tail: every integer \(r\ge512\) by exact generating-function degree and coefficient positivity. Mathematical result is author-proved/author-exact-checked; **independent review pending**.
- Frozen scientific reference: \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Direct predecessor: [R749SRT scientific file](https://github.com/awdawmip/enterprise-math/blob/990a7324b1950fd0d31ae3b07313c87e2c3e3303/research_notes/portable_direct/2026-11-16_R749SRT_MULTIREAD_SHARP_PHASE_THRESHOLDS.md).

**Next:** Determine the sharp adversarial noise radius as a function of a higher minimum starting cutoff; optimize read-set size, shift horizon and a joint robustness/latency criterion. For native Enterprise Math, specify the labeled-source-to-BRC observer and preserved future operations before making any type-changing transfer assertion.
