# OAI7-090: exact atomic factorization and independently certified \(Q,D\) bounds

**Source review / new mathematical bridge, 2026-11-15.** Reviewer/contributor: \`EM-DVR-DEBB5E\` (RESEARCH_DRIVER). The triangular-lattice construction and checker are credited to the original \`openai/math\` authors. This note independently proves an exact algebraic interpretation of the **intended** finite source coefficients and obtains rational, outward-rounded bounds. It is *not* a claim that the original checker was rerun or a Native OAI7 Result accepted.

## Frozen source and exact objects

Source: \`openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a\`, \`preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/verification/check_certificate.py\`, blob \`23768a5c2d88e100399bb5c4347447e86a7160cb\`. The source's \`R\`, \`ph\`, \`Pfull\`, \`PJ\`, \`U\`, \`Q\` and \`D\` definitions are being checked.

Write
\[
A=\{0,1,3,4,7,9,12,13,16,19,21,25,27,28,31\},
\quad \alpha=\pi/18,\quad e_a=e^{i\alpha a},\quad z_s=e^{i\alpha s}.
\]
Define the **exact target coefficients** \(c_j\) by
\[
P(z)=\prod_{a\in A}(2z-e_a-\overline{e_a}z^2)
=\sum_{j=0}^{30}c_jz^j,\qquad p_j=c_{15+j}\ (0\le j\le15).
\]
These are the ideal mathematical objects enclosed by the fixed-grid implementation; computed \`IQ\` intervals are not presumed literally equal to exact complex numbers.

## Exact factorization, self-inversive fold, and double zeros

For \(|z|=1\), each factor satisfies
\[
z^{-1}(2z-e_a-\overline{e_a}z^2)
=2-e_a\overline z-\overline{e_a}z=|z-e_a|^2.
\]
Consequently
\[
F(s):=z_s^{-15}P(z_s)
=\prod_{a\in A}|z_s-e_a|^2
=\prod_{a\in A}4\sin^2\!\frac{\alpha(s-a)}2\ \ge0. \tag{1}
\]
Each quadratic has coefficient symmetry \(c_j=\overline{c_{2-j}}\), so the product has \(c_{30-j}=\overline{c_j}\), including real \(c_{15}\). Therefore, with \(u_0=p_0\), \(u_j=2p_j\) for \(1\le j\le15\),
\[
F(s)=\operatorname{Re}\sum_{j=0}^{15}u_j e^{i\alpha js}. \tag{2}
\]
This is the exact meaning of the source's \`PJ=Pfull[15:]\` and \`U=[p*(2 if j else 1)...]\` fold. It is a **nonnegative trigonometric polynomial**, not an assumed positivity of each coefficient.

All elements of \(A\) are distinct modulo \(36\). At each \(n\in A\), \(F(n)=F'(n)=0\), the zero has exactly multiplicity two in the real variable \(s\), and \(F\) is strictly positive at all other real \(s\) except the periodic translates of those roots. In particular no division by a vanishing exact curvature at a listed root is needed.

## \(Q(n)\) and \(D(n)\) admit closed product/cotangent formulae

The checker's exact intended definitions, with \(\alpha=\pi/18\), are
\[
Q(n)=\operatorname{Re}\sum_{j=0}^{15}p_j(i\alpha j)^2 e^{i\alpha jn},
\quad
D(n)=\frac{\operatorname{Re}\sum_{j=0}^{15}p_j(i\alpha j)^3e^{i\alpha jn}}{3Q(n)}.
\]
By differentiating (2), \(Q(n)=F''(n)/2\) and \(D(n)=F'''(n)/(6Q(n))\). Isolate the unique zero factor in (1), writing
\(F(s)=4\sin^2(\alpha(s-n)/2)H_n(s)\) where
\(H_n(s)=\prod_{a\ne n}4\sin^2(\alpha(s-a)/2)\).
The first factor equals \(\alpha^2(s-n)^2+O((s-n)^4)\), hence
\[
\boxed{Q(n)=\alpha^2\prod_{\substack{a\in A\\a\ne n}}4\sin^2\!\frac{\alpha(n-a)}2>0},\tag{3}
\]
\[
\boxed{D(n)=\frac{H_n'(n)}{H_n(n)}
=\alpha\sum_{\substack{a\in A\\a\ne n}}\cot\!\frac{\alpha(n-a)}2}.\tag{4}
\]
Thus \(Q\) measures the positive quadratic curvature of the root, whereas \(D\) is the cubic-to-quadratic coefficient ratio. The exact Taylor expansion is
\(F(n+\delta)=Q(n)\delta^2+Q(n)D(n)\delta^3+O(\delta^4)\).
These identities also show that the source's \`q(n)=Q[n%36]\` and \`d(n)=D[n%36]\` are compatible with the \(36\)-periodicity of the intended functions.

## Independent all-rational enclosure verification

Companion executable (standard-library \`fractions.Fraction\` only):
[\`2026-11-15_oai7_090_atomic_qd_rational_certificate.py\`](2026-11-15_oai7_090_atomic_qd_rational_certificate.py).
It was run independently in the working environment and every assertion succeeded. It derives a strict interval for \(\pi\) using the \(41\)-term alternating Machin series, then evaluates sine and cosine at rational \(x_k=k\pi_0/36\) for \(1\le k\le31\), outward rounding all enclosures to a \(10^{-10}\) grid. The truncation errors are bounded by \(x_k^{29}/29!\) for the 14-term sine polynomial and \(x_k^{30}/30!\) for the 15-term cosine polynomial, plus \(|x-x_k|\) from \(\pi\)'s interval and the 1-Lipschitz property of sine/cosine. At these orders the omitted alternating terms decrease (all \(x_k<2.71\)). All sine lower bounds are strictly positive; \(\cot=\cos/\sin\) is enclosed by checking the four rational endpoint quotients. Equations (3) and (4) are then evaluated using outward interval arithmetic for **every one of the 15 roots**.

The script checks strict rational inequalities, not decimal floating-point approximations:
\[
\boxed{0.157<\min_{n\in A}Q(n)},\qquad
\boxed{\max_{n\in A}Q(n)<40},\qquad
\boxed{\max_{n\in A}|D(n)|<2.83}. \tag{5}
\]
Illustrative outward six-decimal intervals (all 15 are printed by the script):

| \(n\) | certified \(Q(n)\) interval | certified \(D(n)\) interval |
|---:|---:|---:|
| 0 | [1.096622, 1.096623] | [-2.821466, -2.821465] |
| 1 | [0.324679, 0.324680] | [0.328512, 0.328513] |
| 3 | [0.157467, 0.157468] | [-1.074198, -1.074197] |
| 19 | [20.797184, 20.797185] | [-0.263013, -0.263012] |
| 31 | [39.879534, 39.879535] | [0.488492, 0.488493] |

The exact inequalities in (5) correspond to the source's \`envtable\` checks \`lt('.157',imin(Q.values()))\`, \`lt(imax(Q.values()),40)\`, \`lt(imax(abs(x) for x in D.values()),'2.83')\`; the \(n=1\) intervals also support the separate \`near(q(1),'.32468')\` and \`near(d(1),'.32851')\` target values. This establishes the bounds of the **ideal analytic quantities independently** of the recursive numerical coefficient generation.

## Precisely preserved proof boundary

The original source uses outward intervals for \(\pi\), \`expo\`, complex phases, coefficient multiplication, and division; this note establishes exact identities and an **independent rational certificate of the target inequalities**, not that the source's particular computed interval widths satisfy the same assertions. The latter still requires actual original checker execution or a separate propagation proof. This note does not independently establish the manuscript's universal-energy implication, Lean build/axioms, upstream geometry, Native Result acceptance, Task completion or mother-objective completion. Any formal review must retain original contributor credit and the genuinely independent Researcher/Driver roles.

The only new contribution here is the explicit exact factorization-to-\(Q,D\) mathematical bridge plus a separately executed all-rational 15-root inequality certificate. It reuses, rather than repeats, the prior OAI7 Python–Lean crosswalk, \(\pi\)/exponential enclosure, Bernstein/polytope, and two-wave Taylor-tail audits.
