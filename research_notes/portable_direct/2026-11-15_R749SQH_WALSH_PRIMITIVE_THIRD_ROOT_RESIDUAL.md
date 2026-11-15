# R749SQH — Exact primitive-third-root Walsh provenance oscillation

Date: 2026-11-15. Research status: **AUTHOR_EXACT_NOT_REVIEWED**.
Researcher-ID: **EM-DIRECT-5AD5C5**. Activity: **RA-23D649E29465155706DB0336**.

This is a continuation of **R749SQG** (Draft PR #2495; current scientific head initially \`8dc54db8472f9741761756d8fc060b3f092d745b\`) under the unchanged frozen science pin \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. All theorems apply only to the auxiliary 16-atom signed Walsh source alphabet, not to an admitted native X6 Port/Cell/Link law.

## Exact question and answer

The 23 labeled positive-slack sources have multiplicities \`(1:3,2:4,3:6,4:4,5:3,6:2,7:1)\` and integer count
\[
C_r=\#\{m\in\mathbb Z_{\ge0}^{23}:\sum_{i=1}^{23}s_im_i\le r-1\},\qquad r\ge1.
\]
R749SQG decomposed the exact period-420 quasipolynomial as
\[
C_r=P_{23}(r)+(-1)^{r-1}Q_9(r)+R_{420}(r)
\]
with \(\deg R_{420}|_{r\bmod420}\le7\), and fully specified \(P_{23}\), \(Q_9\).

**New theorem (all positive integer \(r\)).** The exact leading coefficient in the remaining root-of-unity sum is determined solely by \(r\bmod3\):
\[
\boxed{R_{420}(r)=
\frac{1-3\mathbf1_{\{3\mid r\}}}{4\cdot3^{16}\cdot7!}\,r^7+O(r^6).}
\]
Thus its leading coefficient is \(1/867821895360\) for \(r\equiv1,2\bmod3\), and \(-1/433910947680\) for \(r\equiv0\bmod3\). The remainder \(O(r^6)\) is uniform on positive integers. No other primitive-root order contributes to degree 7.

As an **exact, finite-difference identity**, let \(\Delta_{420}f(r)=f(r+420)-f(r)\). Then for **all \(r\ge1\)**
\[
\boxed{
\Delta_{420}^{\,7}\bigl(C_r-P_{23}(r)-(-1)^{r-1}Q_9(r)\bigr)
=\frac{1-3\mathbf1_{\{3\mid r\}}}{4\cdot3^{16}}\;420^7 .
}
\]
The identity removes all lower-degree periodic contributions even though the complete period remains 420.

## Proof by exact local root factors

Define
\[
F(z)=\frac1{1-z}\prod_{s=1}^7(1-z^s)^{-m_s}
=\sum_{r\ge1}C_rz^{r-1}.
\]
Let \(\rho\) be a primitive complex cube root of unity. Precisely the six weight-3 factors and two weight-6 factors vanish at \(z=\rho\), so the pole order is 8. The regularized leading Laurent coefficient for \((1-z/\rho)^{-8}\) is
\[
\begin{aligned}
B_\rho
&=\lim_{z\to\rho}(1-z/\rho)^8F(z)\\
&=\frac1{3^6\,6^2\,(1-\rho)^9(1-\rho^2)^7}\\
&=\frac1{4\cdot3^{15}(1-\rho)^2}
=-\frac{\rho^2}{4\cdot3^{16}},
\end{aligned}
\]
using \((1-\rho)(1-\rho^2)=3\) and \((1-\rho)^2=-3\rho\).

Its leading degree-7 coefficient contribution to \([z^{r-1}]F(z)\) is
\[
-\frac{\rho^2\rho^{-(r-1)}}{4\cdot3^{16}\cdot7!}\,r^7
=-\frac{\rho^{-r}}{4\cdot3^{16}\cdot7!}\,r^7.
\]
The conjugate pole contributes \(-\rho^{-2r}/(4\cdot3^{16}\cdot7!)\,r^7\). Their sum is
\[
-\frac{\rho^{-r}+\rho^{-2r}}{4\cdot3^{16}\cdot7!}
=\frac{1-3\mathbf1_{\{3\mid r\}}}{4\cdot3^{16}\cdot7!}.
\]
All primitive roots of orders 4, 5, 6 and 7 have pole orders at most 4 and hence degree at most 3. The order-3 subleading terms have degree at most 6. The exact 420-quasipolynomial decomposition established in SQG supplies uniformity. On each residue class modulo 420, the 7th forward difference with step 420 of a degree-7 polynomial equals \(7!\,420^7\) times its leading coefficient. This proves the stated exact difference identity. \(\square\)

## Exact computational evidence and continuation

The standard-library Python script \`R749SQH_WALSH_THIRD_ROOT_RESIDUAL_CERT.py\` imports the frozen R749SQG arithmetic certificate from the same directory, recomputes its \(C_r,P_{23},Q_9\), then checks the exact 7th forward 420-step difference against the theorem for **each of the 420 residue classes**, using \(r=1,\dots,3780\). All arithmetic is integer or \`fractions.Fraction\`. The result JSON \`R749SQH_WALSH_THIRD_ROOT_RESIDUAL_RESULTS.json\` is **PASS**; the result class counts are 140 in each of three mod-3 groups. An actual local re-execution provides finite consistency evidence; the preceding residue calculation proves all \(r\).

A meaningful next unit is to determine the exact degree-6 coefficient of the primitive-third-root component (also periodic modulo 3), and then quantify the sharp residue-dependent first-order correction to the SQF optional-source survival probability \(C_{r-3k}/C_r\). Maintain the author-level 23-source classification and await independent mathematical review before promoting to source-admitted native claims.
