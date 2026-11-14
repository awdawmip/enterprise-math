# R147 — Exact CRT joint-residue law and second moments for tied-phase Sturmian fibers

Date: 2026-11-14 (Asia/Shanghai). Scientific pin: \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\` (unchanged).
Researcher: EM-DIRECT-DAF2F3, session MCP-fa6cae44b88546f9a2079bdd4adcad23; independent author-side mathematics, NOT_REVIEWED.
Scope: external scalar S23 tied-phase observer, not an asserted native X6 embedding or formally adopted shared Task Result.
Exact prerequisites: R143 projection, R146.1 closed phase-index fiber formula and R146.2 affine periodicity, committed at \`b02b0c242b274bc6a82111dbd3600126a2867319\` and its cited predecessors.

## 1. Definitions and arithmetic carrier

Let \`m>=1\`, let \`w\` be a finite Sturmian binary word with strict free-intercept slope-support endpoints \`alpha=a/b < beta=c/d\`, in lowest terms, \`0<=alpha<beta<=1\`, \`b,d>=1\`.
For prefix counts \`s_j\` put

\`\`\`
u_alpha = min_{0<=j<=m}(s_j+1-j alpha) = U/b,
ell_beta = max_{0<=j<=m}(s_j-j beta) = V/d,
h = u_alpha - ell_beta,  delta = beta - alpha,
L = K-1 >= 1.
A_L=(La-U)/b, B_L=(Lc-V)/d,
C_w(L+1) = ceil(B_L)-floor(A_L)-1.
\`\`\`

The last equality is the exact R146 phase-index fiber theorem. It counts distinct integer phase indices of the fixed *word*; it does not discard multiplicity by converting to Boolean support. Define

\`\`\`
x_L = (La-U) mod b,       0 <= x_L < b,
y_L = (Lc-V) mod d,       0 <= y_L < d,
eta_d(y) = 0 if y=0, else 1-y/d.
e_w(L) = C_w(L+1)-L*delta.
\`\`\`

Here \`mod\` always means the least nonnegative integer residue. Let \`g=gcd(b,d)\`, \`B=b/g\`, \`D=d/g\`, \`P=lcm(b,d)=gBD\`. Denominator 1 and endpoint slopes 0,1 are included.

**Identity.** For every \`L>=1\`:

\`\`\`
e_w(L) = h - 1 + x_L/b + eta_d(y_L).                 (R147.1)
\`\`\`

Indeed, \`floor(A_L)=A_L-x_L/b\`, \`ceil(B_L)=B_L+eta_d(y_L)\`, and \`B_L-A_L=L*delta+h\`.

## 2. Exact CRT joint-population theorem

Over any \`P\` consecutive integers \`L\`, each ordered pair \`(x,y)\` occurs **exactly once** if and only if

\`\`\`
a^(-1)*(x+U) == c^(-1)*(y+V) (mod g),               (R147.2)
\`\`\`

with the congruence vacuous for \`g=1\`. The modular inverses exist for \`g>1\`, because \`g\` divides \`b,d\` and both endpoint fractions are reduced.

**Proof.** The congruences defining the pair are
\`aL == x+U (mod b)\` and \`cL == y+V (mod d)\`.
Multiply by inverse units, then apply the generalized Chinese Remainder Theorem. A solution exists precisely for the compatibility condition modulo \`g\`, and then the solution class is unique modulo \`P\`. Thus the joint histogram is the exact finite polynomial

\`\`\`
H_w(X,Y) = sum_{0<=x<b, 0<=y<d, CRT-compatible} X^x Y^y.   (R147.3)
\`\`\`

If \`g=1\`, every pair occurs and \`H_w(X,Y)=(sum_{x=0}^{b-1}X^x)*(sum_{y=0}^{d-1}Y^y)\`.
When \`g>1\`, the \`g\`-class compatibility carries a genuine joint residue constraint. Raw factor data alone do not justify replacing that constrained population by independent marginals.

## 3. Exact period mean and variance

Take averages uniformly over any \`P\` consecutive \`L\`. Both \`x_L\` and \`y_L\` are individually uniform on their full residue ranges. Consequently,

\`\`\`
mean(e_w) = h - 1/(2b) - 1/(2d).                    (R147.4)
\`\`\`

The individual variances of \`x/b\` and \`eta_d(y)\` are respectively
\`(b^2-1)/(12b^2)\` and \`(d^2-1)/(12d^2)\`.

Here is a *g-term* exact covariance formula (no need to enumerate the full \`P=bd/g\` joint population). For \`t=0,...,g-1\` write

\`\`\`
r_x(t) = (at-U) mod g,           r_y(t) = (ct-V) mod g,
mu_x(t) = (B-1)/(2B) + r_x(t)/b,
mu_eta(t) = (D+1)/(2D) - r_y(t)/d - 1_{r_y(t)=0}/D,
bar_x = (b-1)/(2b),             bar_eta = (d-1)/(2d),
Gamma = (1/g) * sum_{t=0}^{g-1} (mu_x(t)-bar_x)*(mu_eta(t)-bar_eta).
\`\`\`

Then

\`\`\`
Var_P(e_w) = (b^2-1)/(12b^2) + (d^2-1)/(12d^2)
             + 2*Gamma.                              (R147.5)
\`\`\`

**Proof.** Conditional on \`L mod g=t\`, the eligible \`x\` residues are
\`r_x(t)+gj\`, \`j=0,...,B-1\`, and eligible \`y\` residues are
\`r_y(t)+gk\`, \`k=0,...,D-1\`. They form their full Cartesian product once,
because \`gcd(B,D)=1\`. Therefore the two terms of (R147.1) are conditionally independent. Their conditional means are the displayed \`mu_x(t)\` and \`mu_eta(t)\`; the extra indicator accounts for the single \`y=0\` case where \`ceil(B_L)-B_L=0\`. By total covariance,
\`Cov(x/b,eta_d(y))=Cov_t(mu_x(t),mu_eta(t))=Gamma\`. The standard uniform-residue variances give (R147.5). All operations are exact rational arithmetic.

**Coprime simplification.** If \`g=1\`, then \`Gamma=0\` and

\`\`\`
Var_P(e_w) = (b^2-1)/(12b^2)+(d^2-1)/(12d^2).     (R147.6)
\`\`\`

For noncoprime denominators, \`Gamma\` must be retained unless independently proved zero. Mean (R147.4) holds in either case.

**Affine-cycle corollary.** Because R146 proves \`C_w(L+P+1)=C_w(L+1)+P*delta\`, the sequence \`e_w(L)\` is exactly periodic (period dividing \`P\`). Thus (R147.3)–(R147.6) describe its complete discrepancy distribution and moments on *every* future period, including arbitrarily large \`K\`; no sampling-limit argument is used.

## 4. A minimal joint-residue witness

For \`m=4\`, word \`w=0101\`, exact prefix inequalities give

\`\`\`
alpha=1/3, beta=2/3, u_alpha=2/3, ell_beta=0,
b=d=g=P=3, U=2, V=0.
\`\`\`

As \`L\` traverses a period, \`(x_L,y_L)\` takes precisely
\`(1,0),(2,2),(0,1)\`; its discrepancy values are \`0,2/3,1/3\` in that order.
Therefore \`mean(e)=1/3\`, \`Var(e)=2/27\`, and \`Gamma=-1/27\`.
The independence-based variance would have been \`4/27\`, so ignoring the joint CRT residue changes a quantitatively observable statistic by a factor of two. This is an explicit exact failure of an unlicensed product-of-marginals approximation for the declared observer.

## 5. Exact verification, reuse, open question

The accompanying \`check_r147.py\` exhausts all 636 finite Sturmian word records of lengths \`1..11\` (full binary candidate space at each length) with Python \`Fraction\` and integer arithmetic. For each, it enumerates all \`P\` residue positions, verifies CRT support bijection, the exact discrepancy formula, mean and variance, and the \`g\`-term conditional covariance expression. The run checked **12,732 period/residue positions**; 534 words had coprime endpoints, while 102 had nonzero joint covariance. All checks passed: \`R147_CRT_FIBER_FLUCTUATION_PASS\`. This is a finite implementation crosscheck; the universal result rests on the above CRT and conditional-expectation proof.

Reuse: \`H_w\`, \`Gamma\` and the exact two-residue carrier support future BRC-style joint-fiber analysis while preserving multiplicity and composite-modulus coupling. Next: derive whether the CRT phase alignment near the conjectural permanent saturation boundary \`E(m)\` can sharpen R146B's per-word disappearance criterion for the remaining Farey-avoidant word family. The all-length \`T(m)=E(m)\` conjecture is still open.

No native CLAIM, review or P000 alteration is asserted.