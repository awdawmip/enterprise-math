# R749STU — Exact initial four-read optimality for the 73/79 five-source scalar pair

Date: 2026-11-17. Status: **AUTHOR_EXACT_NOT_REVIEWED** (exact author-side computational and analytic certificate; not independently reviewed). Scientific input frozen at \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Predecessors: R749STR/STS, Draft PR #2653; R749STT, Draft PR #2656. Independent portable research; no Task CLAIM or native X6/Port/Cell equivalence is asserted.

## 1. Exact statement

Five distinct labeled nonnegative-integer source coordinates have weights \`(1,1,2,3,6)\`. Let \`C_n\` be the number of source tuples whose weighted sum is at most \`n-1\`, and \`T_n\` the sum of the **first** weight-one coordinate across this set. Define

\`\`\`
S(n) = 18*n^4 + 54*n^3 - 345*n^2 + 2070*n - 16315,
Y_n(e,d) = n^3*(T_n+e)/(C_n+d) - S(n)/108.
\`\`\`

For q=73 and p=79, let the independent candidate-specific parameter pairs \`(e,d)\`, \`(E,D)\` range over the **entire real** square \`[-2,2]^2\`, and remain fixed across observations. Compare the first m successive reads \`Y_(73+6j)(e,d)\` and \`Y_(79+6j)(E,D)\` for j=0,...,m-1.

**Theorem.** The exact smallest m for which the two candidate observation sets do not intersect is

\`\`\`
m_initial({73,79}) = 4.
\`\`\`

More precisely:

(a) There exists a legal real nuisance quadruple with all first **three** reads exactly equal. A constructive one-dimensional IVT certificate is given in §2.

(b) Put \`a=(9261513,-33843268,40729637,-16165583)\` and \`L_n(e,d)=sum(j=0..3) a_j Y_(n+6j)(e,d)\`. For every legal real quadruple,

\`\`\`
L_73(e,d) > 146200 > L_79(E,D)
L_73(e,d) - L_79(E,D) >=
  Δ = 722997167446021926834455947339144
      / 4444935850061982688915244893275 > 0.
\`\`\`

The stated Δ is a rigorous **conservative**, not sharp, bound from rational Bernstein coefficients. With absolute additive error at most η in **each** of the eight raw scalar readings (four per candidate), the separator stays positive for

\`\`\`
0 <= η < Δ/200000002
= 361498583723010963417227973669572
  / 444493589451134118953507178242744893275.
\`\`\`

No probabilistic assumptions are used.

## 2. Three-read exact collision: constructive IVT certificate

Fix \`E=1\` and allow \`D\` in the rational interval \`[-909/1000,-908/1000]\`. Define for i=0,1:

\`\`\`
r_i(D) = Y_(79+6i)(1,D),
x_i(D) = [r_i(D) + S(73+6i)/108] / (73+6i)^3,
v_i(D) = C_(73+6i)*x_i(D) - T_(73+6i),
d(D) = [v_0(D)-v_1(D)] / [x_1(D)-x_0(D)],
e(D) = v_0(D)+x_0(D)*d(D).
\`\`\`

The inversion identities imply \`Y_73(e(D),d(D))=Y_79(1,D)\` and \`Y_79(e(D),d(D))=Y_85(1,D)\` throughout the interval.

For the five rational functions \`x_1-x_0\`, \`e+2\`, \`2-e\`, \`d+2\`, \`2-d\`, the accompanying exact checker substitutes \`D=-909/1000+t/1000\`, writes each as a numerator divided by a denominator, and checks that its respective numerator and denominator have the **same strict sign at every degree-2 Bernstein coefficient** on \`0<=t<=1\`. Hence the inversion is continuous and \`e(D),d(D)\` remain strictly in (-2,2) on the whole interval. \`E=1\`, \`D in [-2,2]\` are automatically legal.

Define the third-read residual
\`\`\`
R(D) = Y_85(e(D),d(D)) - Y_91(1,D).
\`\`\`
Direct exact rational evaluation yields

\`\`\`
R(-909/1000) =
-285808956533718829371037284599568749942
/2407031270075883588016120924888968193259703277 < 0,

R(-908/1000) =
485024370753626417026051447398878
/476695740793968908390339941202433358357 > 0.
\`\`\`

The intermediate value theorem supplies a \`D_*\` strictly between these endpoints with \`R(D_*)=0\`, and the legal \`e(D_*),d(D_*)\` give **three simultaneous exact read equalities**. This existence argument does not assume the root is rational.

## 3. Four-read uniform separation: finite Bernstein certificate

An independent integer dynamic program gives

| n | C_n | T_n |
|---:|---:|---:|
| 73 | 707343 | 8931013 |
| 79 | 1020943 | 13914446 |
| 85 | 1436968 | 21025004 |
| 91 | 1978664 | 30933812 |
| 97 | 2672553 | 44459556 |

For \`n=73\` and \`n=79\`, let \`u=-2+4x\`, \`v=-2+4z\`, where \`x,z in [0,1]\`; let \`Q_n(v)=product(j=0..3)(C_(n+6j)+v)>0\` on this box, and set

\`\`\`
P_73(x,z) = 108*(L_73(u,v)-146200)*Q_73(v),
P_79(x,z) = 108*(146200-L_79(u,v))*Q_79(v).
\`\`\`

Each \`P_n\` is an exact polynomial, of bidegree (1,4). In the tensor Bernstein basis of bidegree (1,4), **all ten coefficients of each polynomial are strictly positive**. Their exact minimum coefficients are

\`\`\`
min Bernstein(P_73) =
  55532844424733753159041729352/3 > 0,

min Bernstein(P_79) =
  66343998071127222246484911864 > 0.
\`\`\`

Bernstein convex-hull positivity therefore proves \`P_n>0\` on the entire closed real box, establishing \`L_73>146200>L_79\` without numerical parameter optimization.

Using \`Q_n(v) <= product_j(C_(n+6j)+2)\` yields the exact positive rational bounds

\`\`\`
L_73(e,d)-146200 >=
  6941605553091719144880216169
  / 83158921894254424865255250,

146200-L_79(E,D) >=
  2764333252963634260270204661
  / 34910953008644867536077750.
\`\`\`

Their sum reduces to the stated Δ. The sum of the absolute values of the four integer contrast coefficients is \`100000001\`, so perturbing the eight candidate readings by at most η changes the inter-candidate contrast by at most \`200000002*η\`. This proves the noise statement.

## 4. Verification, inference boundary, future work

The accompanying Python 3/SymPy \`R749STU_FOUR_READ_73_79_CERT.py\` independently regenerates the five-source counts, checks both exact IVT endpoint signs, certifies whole-interval legality with 5 positive rational Bernstein ratios, certifies the 20 positive coefficients for the four-read separator and recomputes the uniform margin/noise bound. Author execution on 2026-11-17: **PASS**. The JSON machine result records exact values and all Bernstein coefficients. This is a proof by explicit rational polynomial identities and finite complete coefficient checks; no floating-point step is used.

Together with R749STR/STS for the fixed-base congruent family and R749STT for h=2, the initial minimum for \`q=73, p=73+6h, h>=1\` is now fully classified:

\`\`\`
h=1       => 4 reads,
h=2       => 3 reads,
3<=h<=129 => 2 reads,
h>=130    => 1 read.
\`\`\`

The scalar observer discards named joint-source/branch/provenance data, so it does not itself certify an X6/BRC Port/Cell state equivalence. The global unknown-q horizon \`5<=m_*<=11\` stays as previously established. The next independent research question is to construct an explicitly typed source/branch/future-operation preserving readout, or prove a minimal residual obstruction, under the native P000 and BRC contracts.