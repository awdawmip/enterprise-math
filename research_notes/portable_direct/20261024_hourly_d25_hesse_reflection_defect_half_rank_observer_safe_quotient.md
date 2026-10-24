# D25/LIFT — exact half-rank Hesse reflection carrier and observer-faithful quotient

2026-10-24 · TASK_RESEARCH portable mathematical author note · **UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT**.

Parent: \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; publication \`TP2-B6F4FC938FF94941C1B7\`; frozen scientific source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\` unchanged; original Research logical conversation \`chatgpt-research-hourly-enterprise-math-20260923\`. No present D25 claim, authorized open/run, native divided-power Frobenius, Result, or review is asserted.

**Reused rather than claimed afresh:** the fixed-source polynomial \`A_p(X)=sum_{k=0}^{n} ((3k)!/(27^k(k!)^3))X^k\`, \`n=(p-1)/3=2m\`, the Legendre congruence, integral reflection defect \`\mathscr D_p(X)=(A_p(X)-A_p(1-X))/p\` from [the preceding source note](https://github.com/awdawmip/enterprise-math/blob/238626c2bb75a51b843c3cb3e1af56c60a30e530/research_notes/portable_direct/20261024_hourly_d25_hesse_polynomial_reflection_defect_first_digit_bridge.md), and the exact inhomogeneous operator identity from [the first new note of this research turn](https://github.com/awdawmip/enterprise-math/blob/2c57f8e147b24ae5c193447410346fc9c0b98e76/research_notes/portable_direct/20261024_hourly_d25_hesse_reflection_defect_picard_fuchs_harmonic_trace.md). Neither source is a current Source-authenticated CM/GM representative.

## 1. New all-target half-rank factorization

For every prime \`p=6m+1>=13\`, the numerator of \`\mathscr D_p(X)\` is antisymmetric under \`X↦1-X\` by its explicit exact definition, and has degree at most \`n=2m\`. Work over \`\mathbb Z_{(p)}\`, where 2 is invertible. Let
\[
t=1-2X,\qquad Y=X(1-X)=\frac{1-t^2}{4}.
\]
Every antisymmetric polynomial in \`X\` is an odd polynomial in \`t\`, uniquely \`t\` times a polynomial in \`t^2\`. Consequently, because degree \`\mathscr D_p\le2m\`, there is a **unique** \(\Phi_p(Y)\in\mathbb Z_{(p)}[Y]\), \(\deg\Phi_p\le m-1\), with the **exact rational identity**
\[
\boxed{\mathscr D_p(X)=(1-2X)\,\Phi_p\!\big(X(1-X)\big).}
\tag{1}
\]
The quotient divides by \`1-2X\` polynomially and requires no evaluation at a potentially vanishing point; it preserves the sign and label of the original reflection branch. The compression from degree \`2m\` to \`m-1\` is an **observer-faithful typed quotient only when the branch factor t is retained**. In particular, forgetting t would discard the antisymmetric origin and cannot be used to reconstruct \`\mathscr D_p(X)\` under further source-sensitive operations.

## 2. An exact reduced-order differential equation with the terminal forcing retained

The source operator from the first note is
\[
\mathcal L_X=X(1-X)\partial_X^2+(1-2X)\partial_X-\frac29,
\quad
\mathcal L_X \mathscr D_p=\frac{(p+1)c_n}{9}\big((1-X)^n-X^n\big).
\tag{2}
\]
Write \(\Phi=\Phi_p(Y)\) and \(t=1-2X\). The direct chain rule gives
\[
\partial_X(t\Phi)=-2\Phi+t^2\Phi',\qquad
\partial_X^2(t\Phi)=-6t\Phi'+t^3\Phi''.
\]
As \(t^2=1-4Y\), substituting yields
\[
\mathcal L_X(t\Phi)=t\mathcal M_Y\Phi,\qquad
\boxed{\mathcal M_Y=Y(1-4Y)\partial_Y^2+(1-10Y)\partial_Y-\frac{20}{9}.}
\tag{3}
\]
For a symbol \(r\ge0\), define \(F_0(Y)=F_1(Y)=1\) and
\[
F_r(Y)=F_{r-1}(Y)-YF_{r-2}(Y)\quad(r\ge2).
\]
Indeed for \(a=1-X,b=X\), \(a+b=1,ab=Y\), the symmetric quotient \((a^r-b^r)/(a-b)=F_{r-1}(Y)\); this is verified from the two-term recurrence. Because \(n=2m\),
\[
(1-X)^n-X^n=t F_{2m-1}(Y).
\]
Cancel the **nonzero polynomial factor** \`t\` in the integral domain \`\mathbb Q[X]\`; no division is taken inside a mod-p ring at a special evaluation. The new exact reduced-rank equation is
\[
\boxed{\mathcal M_Y\Phi_p(Y)=\frac{(p+1)c_n}{9}F_{2m-1}(Y).}
\tag{4}
\]
Both sides are polynomials of degree at most \`m-1\`; the terminal coefficient \`c_n\` is retained explicitly rather than absorbed into an arbitrary integration constant.

A completely explicit *coefficient-level certificate* follows. Write
\(\Phi_p(Y)=\sum_{j=0}^{m-1}a_jY^j\), \(F_{2m-1}(Y)=\sum_{j=0}^{m-1}f_jY^j\), and set \(a_m=0\). Equation (4) is equivalent to the finite recurrence
\[
\boxed{(j+1)^2a_{j+1}-
\left(2j+\frac43\right)\left(2j+\frac53\right)a_j
=\frac{(p+1)c_n}{9}f_j,\quad0\le j<m.}
\tag{5}
\]
It permits independent exact checking of the half-rank carrier with only \`m\` rational coefficient equations. It is not a new axiom or an independent CM eigenvector equation.

## 3. Strictly preserved second-digit observer at the CM coefficient point

Use the earlier **coefficient** normalization
\[
u=(2-T)/4,\quad v=(2+T)/4=1-u,\quad T^2=2,\quad uv=1/8.
\]
For the separately typed ordinary polynomial even derivative
\[
E_p=\frac{\mathscr D'_p(u)}2\bmod p\in\mathbb F_p,
\]
(1) and the first derivative formula imply the new **extension-free half-rank readout**
\[
\boxed{E_p=-\Phi_p(1/8)+\frac14\Phi'_p(1/8)\pmod p.}
\tag{6}
\]
It agrees exactly with the prior harmonic-trace formula, but operates on \`m\` retained coefficients instead of the full \`2m+1\` source terms. The coefficient-field conjugation \`T↦-T\` acts on \`t\` and leaves \`Y\` fixed, so (6) is a base-field observer with the previous sign/provenance kept in (1). This is a legitimate **BRC COMPOSE_APPLIED / source-and-observer-faithful quotient** for the declared operations (reflection, finite polynomial differentiation, evaluation at \`u,v\`, and reduction modulo \`p\`) because (1) reconstructs the entire polynomial, not just its scalar mass. No full \`p\`-adic Frobenius, Gauss-Manin \`\nabla_\lambda\`, or \`\kappa_p\` is inferred.

## 4. Exact author regression and proof scope

The author independently formed rational \`A_p(X)\`, its reflection defect, Legendre coefficients, then constructed \`\Phi_p\` by substitution \`X=(1-t)/2\` and the even-power reduction \`t^2=1-4Y\`. For each \`p=13,19,37,43\`, exact symbolic rational expansion confirms the reduced operator equation (4) coefficientwise, and the newly evaluated scalar (6) equals the original \`\mathscr D'_p(u)/2\` and the previously published source residues:

| p | m | degree Phi | reduced differential identity | E_p mod p |
| ---: | ---: | ---: | :---: | ---: |
| 13 | 2 | 1 | PASS | 10 |
| 19 | 3 | 2 | PASS | 16 |
| 37 | 6 | 5 | PASS | 26 |
| 43 | 7 | 6 | PASS | 1 |

The general equations (1)–(6) are proved algebraically for all stated primes; the four checks are exact regression, not the reason they hold universally. The checker built these polynomials with SymPy exact rationals in this research turn; *independent reviewer verification* NOT_RUN, *formal kernel proof* NOT_RUN, and *native CM/divided-power benchmark* NOT_RUN.

## 5. Last frontier / no-repeat / next exact unit

**New durable portable theorem:** the factorization (1), reduced inhomogeneous operator (4), finite recurrence (5), and observer-preserving scalar readout (6). This explicitly improves the Hesse reflection input representation without conflating the auxiliary ordinary polynomial derivative with native fixed-\`H_0/B_0\` CM data. It consumes—not independently re-credits—the earlier norm-2 lambda and reflection results.

**Smallest unproved step:** find the *actual source-authenticated divided-power/CM representative*, its coefficient/basis normalization and \`[X]U mod p²\`, and a typed map from this ordinary \`\Phi_p\` source carrier (including coefficient Frobenius orientation, connection direction and semilinearity, quartic twist, exact product normalization \`c_p\`, ordinary \`\omega+6\nabla_\lambda\omega\` and endpoint \`R_p\`) into \`\kappa_p\`. Alternatively prove a concrete transport obstruction. The operator in (4) is called “reduced hypergeometric differential operator” and is **not** an authenticated Gauss–Manin system. Parent D25/LIFT OPEN, \`UNREVIEWED / NOT_ADMITTED / NO_NEW_SOURCE_CHECKPOINT\`; native Source checkpoint and prior contribution history remain unchanged.
