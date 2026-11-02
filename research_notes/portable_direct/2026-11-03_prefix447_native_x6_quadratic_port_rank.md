# PREFIX-447 — Sharp native-X6 quadratic control-port rank and a mixed-axis marginal counterexample

**Date:** 2026-11-03 (Asia/Shanghai). **Lineage:** PREFIX-446 (`1e8eb17db167847c7ad7fc179cb0ce892d7c9fb2`). **Scientific input frozen:** `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. **Author-level status:** analytic proof + exact independent certificate, not independently reviewed or admitted. **Control:** GitHub login `awdawmip` with repository push permission; native Site research authority unavailable and active Owner unconfirmed (`CONTROL_QUOTA` during this run). No formal CLAIM is asserted.

## Question and typed setting

PREFIX-446 proved a `q(d+1)`-coordinate completion for degree-`d` moments on the explicit **first-axis signed path subfamily**. What is the exact full-six-axis quadratic information requirement of a history-typed BRC port? Here the mother problem is minimum future-sufficient observation of positive branch families without erasing six-axis interaction directions.

Fix a chosen native Cell and use chart-relative displacement in the locked P000 `X6` torsor, with six independent signed native axes. A primitive word is an ordered sequence of steps `±e_i` (`1<=i<=6`), of a common prescribed length `N`; time, final Cell address and history are separate types. For fixed `q>=2`, its auxiliary history sector is `r(w)=#(-e_1) mod q`, not an extra spatial coordinate. A source is a finite positive-rational weighted bag of words. We observe **per-sector full quadratic X6 moments**:

\[
T_{r,\alpha}=\sum_{w:r(w)=r}c_w\,x(w)^\alpha,\quad \alpha\in\mathbb N^6,\quad|\alpha|\le2.
\]

The monomial family has `binom(6+2,2)=28` elements: mass, six first moments, six coordinate squares and fifteen mixed products. The allowed future BRC operations are finite positive-rational weighted alternatives and state-conditioned six-axis affine effects `x -> A x+b` on each `(source r,target s)` control transition. An affine effect is a **typed algebraic observer/transport**; an individual native step remains `±e_i`.

## Theorem 447.1 — sharp 28q-dimensional quadratic observation rank, at one native duration

**Statement.** For every `q>=2`, at the single common native word length

\[
\boxed{N=4+2(q-1)=2q+2,}
\]

there exist **28q distinct ordered valid X6 words**, partitioned equally into `q` history sectors, whose positive-rational branch weights yield an observer of exact linear rank

\[
\boxed{\operatorname{rank}=28q.}
\]

Consequently, for this source population the minimum number of independent *linear rational coordinates* that determine all sector-labeled X6 quadratic moments is exactly `28q`. For `q=3`, length `N=8`, the rank is **84**. The value is attained by the existing `q`-indexed `MomentState` layout (28 packed homogeneous symmetric-matrix entries per state), with a `ControlPacket` retaining the control sector.

**Proof.** Build the set of 28 endpoints

\[
P=\{0\}\cup\{2e_i,-2e_i:1\le i\le6\}\cup\{2e_i+2e_j:1\le i<j\le6\}.
\]

Every point is reachable by a word of exactly four native signed steps: two cancelling pairs for zero; the two repeated `±e_i` steps plus one cancelling pair for `±2e_i`; two positive `e_i` and two positive `e_j` steps for the mixed point. Choose axis 2 for the cancelling pair so that all base words have `#(-e_1)=0`, except the `-2e_1` point, which has `#(-e_1)=2`.

For each chosen base word `w` and target sector `r`, let `t=(r-#(-e_1 in w)) mod q`, using `0<=t<=q-1`. Append `t` cancelling ordered pairs `(-e_1,+e_1)` and `q-1-t` pairs `(+e_2,-e_2)`. The resulting word has length `2q+2`, the same endpoint as `w`, and history sector precisely `r`. Hence every sector contains the full endpoint set `P` at the common duration. The `(r,P)` pairs give 28q distinct legal words.

Order the degree-at-most-two monomials as

\[
1;\quad x_1,x_1^2,\ldots,x_6,x_6^2;\quad (x_i x_j)_{i<j}.
\]

Order points as `0`, then `+2e_i,-2e_i` for each axis, then `2e_i+2e_j`. The 28-by-28 integer evaluation matrix `V` has exact determinant

\[
\boxed{\det V=16^6 4^{15}=2^{54}=18014398509481984.}
\]

Indeed the zero row isolates the constant coefficient. The two `±2e_i` rows supply the six invertible 2-by-2 blocks `[[2,4],[-2,4]]`, each of determinant 16; after eliminating their contributions, every mixed-point row isolates its `x_i x_j` coefficient with diagonal entry 4. Thus the 28 monomials are independent on P. The sector-labeled matrix has q diagonal copies of V; its determinant is `2^(54q)` and its rank `28q`. Rational positive branch weights contain an open positive orthant of this coefficient space, so lower-dimensional linear statistics cannot distinguish all possible quadratic observations. The existing symmetric homogeneous (7-by-7) matrix has precisely 28 independent entries, proving attainment. QED.

**Fixed length versus general length.** The construction proves full rank at `N=2q+2` and at any larger even-increment `N+2m` by appending m cancelling pairs on axis 2. It does not invoke a global origin or change the native six-axis ontology.

## Theorem 447.2 — closure under exact state-conditioned affine BRC

Write `Q_r = sum_{w:r(w)=r} c_w z_w z_w^T` with `z_w=(x_1,...,x_6,1)^T`. For every finite positive-rational control kernel with transition atoms `(r,s,weight=\lambda,H)` where `H=[[A,b],[0,1]]`, the target per-sector moment is exactly

\[
\boxed{Q'_s=\sum_{(r,s,\lambda,H)}\lambda H Q_r H^T.}
\]

This follows by distributing each atom over the words and interchanging finite sums. Positive alternatives add these matrices; serial composition uses affine matrix multiplication and repeated application of this formula. It therefore closes for every finite sequence of kernels in this declared language. This is precisely the symbolic operation of the frozen `EffectHistogram.moment_action`, and the `ControlPacket.moment_action` dispatches those matrices by control `(source,target)`; `MomentState` stores the 28 upper-triangular entries. **Reuse resolution:** `COMPOSE_APPLIED` for frozen `brc_transport.py` blob `be1debe367263931bd5e93fd750be3ed54624fe1` and `brc_control_port.py` blob `44def6b8ac787e798d3cc2c6be16f873f91bdb8` at the frozen source pin. The upstream classes were inspected; their direct-import runtime check is a separate pending test.

## Proposition 447.3 — exact mixed-axis loss with only two words per bag

Within `q=3`, length `N=8` and **one fixed history sector** `r=0`, construct sources A and B with respective endpoints (coordinates 3 through 6 are zero):

\[
A=\{(2,2),(-2,-2)\},\qquad
B=\{(2,-2),(-2,2)\}.
\]

Each endpoint has an exact signed-axis four-step word, followed by the above sector-targeted cancelling-pair padding. Each word has weight 1. Every one-axis **complete endpoint marginal histogram** is identical for A and B, on all six axes. Nevertheless,

\[
\boxed{T_{0,x_1x_2}(A)=8,\quad T_{0,x_1x_2}(B)=-8.}
\]

Under the invertible six-axis affine shear `x'_1=x_1+x_2`, with other coordinates unchanged, the sum of squared first readouts is respectively **32 versus 0**. Thus preserving only individual-axis marginal distributions (even without finite moment truncation) is insufficient for the declared affine-effect BRC language. The mixed quadratic coordinate detects the exact difference. This is an algebraic `Affine` effect, not an assertion of a primitive mixed-axis movement.

## Relation to PREFIX-446 and resource consequences

For the frozen first-axis-only path family at `q=3,d=2,N=8`, the sector quadratic row rank is **9** (`3` one-variable moments per residue; three available endpoints per residue). On the **full native six-axis path family at the same duration**, the rank is **84**, proved above. The 75 additional independent directions comprise first moments/squares in the other axes and genuinely mixed moments. This identifies a concrete source/observer scope change where replacing the full quadratic port by the nine-coordinate axis specialization erases independently observable X6 information.

For a general six-axis quadratic observation, `q` existing `MomentState` values (28 rationals each) achieve the exact linear-information lower bound. For the first-axis-only language, a sparse port can carry three live entries per sector; the fixed `MomentState` representation still allocates 28 per sector. These are **rational-coordinate counts**, not measured bytes or total execution complexity; exact numerator/denominator bit lengths and kernel representation costs matter for engineering comparisons.

## Exact evidence and remaining work

The executable standard-library certificate `prefix447_x6_quadratic_port_certificate.py` uses integer Bareiss elimination for `det V`, constructs the 28q actual native signed-step words for `q=2,3,4,5`, verifies the two-word marginal counterexample, and checks the full homogeneous moment update against direct rational-weight branch propagation for three serial conditional affine BRC steps at `q=3` (84 initial weighted branches). The companion `PREFIX447_EXACT_EXECUTION.log` is the verbatim locally executed result. Checks use exact `int`/`Fraction` arithmetic. The general `q` and arbitrary-serial result is proved above; the executed cases are finite checks.

**Next PREFIX-448:** Run a source-version-matched direct upstream class-level test with `ControlPacket.from_edges`, `then`, `alternatives`, `evaluate`, and `moment_action` on the same 84-word `q=3,N=8` source and the two-word mixed-axis witness; confirm the per-sector 28-entry matrix and affine shear values, then compare real serialized byte sizes, execution time, full `EffectHistogram` and a sparse nine-moment axis specialization over an explicitly declared length window. The direct class import is the remaining native execution unit. Formal live CLAIM, independent review and mathematical admission remain governed by the Source task authority.
