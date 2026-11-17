# R232 — Sperner-optimal spectral collision multiplicity and exact 231-mode observer

Date: 2026-11-17 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Native BRC EffectHistogram: NOT_EXECUTED.

## Source and mathematical scope

Continue R229, R230 and R231; immediate immutable predecessor: awdawmip/enterprise-math@f15c70f1ad510fa08387dd227177936ff9a2cd7e:research_notes/portable_direct/R231_MULTIPAIR_SOURCE_SPECTRAL_COLLISION_244_20261117.md. Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. P000 and ACTIVE six-axis Heartbeat World remain unchanged. The conclusions apply to the **derived scalar principal-ideal-cardinality observer** of the paired-source stochastic algebra, not physical BRC event laws; no native signs, port, branch, joint/provenance, multiplicity, rational weight or cross-moment carrier is compressed or discarded.

For k nonneutral source labels 1,...,k and neutral source 0, take the stationary sticky-reset Markov chain

\[
P_{ij}=\alpha_i\delta_{ij}+(1-\alpha_i)\pi_j,\quad 0<\alpha_i<1,\quad \pi_i>0,\quad \sum_{i=0}^k\pi_i=1 .
\]

Its stationary probabilities satisfy \(\rho_i\propto\pi_i/(1-\alpha_i)\).
For each proper nonneutral mask \(U\subsetneq[k]\), put \(D_U=\{0\}\cup U\) and \(b_i=(1-\alpha_i)\pi_i\). Assume all holding values \(\alpha_i\) distinct, and set

\[
C_D(x)=\prod_{i\in D}(x-\alpha_i)-\sum_{i\in D}b_i\prod_{j\in D\setminus\{i\}}(x-\alpha_j).
\]

By R229 the monic minimal recurrence polynomial of the stationary scalar expected ideal cardinality sequence \(f_n=\mathbb E[F_n]\) for \(n\ge L\) is the lcm of \(x-1\) and the 2^k-1 proper-block \(C_D\). The R215 fiber coefficients are strictly positive.

## Theorem 1: maximal multiplicity of a fixed non-pole observable mode

Fix a real \(\lambda\) distinct from **every** \(\alpha_i\), and define
\[
d_i=\frac{(1-\alpha_i)\pi_i}{\lambda-\alpha_i}\ne0\quad(i=1,\ldots,k).
\]
The number of proper blocks \(D_U\) having \(\lambda\) as a root of \(C_{D_U}\) satisfies

\[
\boxed{\#\{U\subsetneq[k]:C_{D_U}(\lambda)=0\}\le {k\choose\lfloor k/2\rfloor}.}
\]

**Proof.** With \(d_0=b_0/(\lambda-\alpha_0)\), the secular equation is \(\sum_{i\in U}d_i=1-d_0\). Let \(A=\{i:d_i>0\}\), \(B=\{i:d_i<0\}\) and \(w_i=|d_i|>0\). Under the bijection of subsets
\[
Y=(U\cap A)\cup(B\setminus U)
\]
the equation becomes
\[
\sum_{i\in Y}w_i=1-d_0+\sum_{i\in B}w_i.
\]
Any two distinct solutions \(Y_1\subsetneq Y_2\) would give strictly different positive weighted sums. Thus the solution family is an antichain in the Boolean lattice. A uniformly random maximal chain visits any fixed \(Y\) with probability \(1/{k\choose |Y|}\) and an antichain at most once, proving the LYM inequality \(\sum_{Y\in\mathcal F}{k\choose |Y|}^{-1}\le1\). Since the largest binomial coefficient is \({k\choose\lfloor k/2\rfloor}\), the family has at most that many members. The proper-mask subfamily has no more. QED.

This theorem bounds collisions of **one specified eigenvalue**; it does not bound all distinct-eigenvalue collision losses combined.

## Theorem 2: exact saturation at 20 blocks and scalar recurrence degree 231 for six sources

Take k=6, m=12 signed-direction labels, tail depth L=2 and the exact rational parameters

\[
\alpha=(1/5,\ 1/4,\ 3/10,\ 7/20,\ 2/5,\ 3/4,\ 4/5),
\]
\[
\pi=(687/2287,\ 455/6861,\ 130/2287,\ 105/2287,\ 455/13722,\ 455/2287,\ 1365/4574).
\]

All seven \(\alpha_i\) are distinct in (0,1); all \(\pi_i\) strictly positive and \(\sum\pi_i=1\). At \(\lambda=1/2\), putting \(c=455/2287\), direct exact substitution gives
\[
d_0=1-c;\quad d_1=d_2=d_3=d_4=c;\quad d_5=d_6=-c .
\]
The secular equation becomes
\[
|U\cap\{1,2,3,4\}|-|U\cap\{5,6\}|=1 .
\]
Under the preceding transformation \(Y=(U\cap\{1,2,3,4\})\cup(\{5,6\}\setminus U)\), this is exactly \(|Y|=3\). Hence there are precisely \({6\choose3}=20\) solutions and each is proper: the full mask has signed count 4-2=2. With source i encoded as bit i-1, the proper masks are

\`\`\`text
1,2,4,8,19,21,22,25,26,28,35,37,38,41,42,44,55,59,61,62
\`\`\`

The generic sum of all 63 proper-block polynomial degrees is 249, and the full source block contributes only the eigenmode 1, giving generic upper degree 250. The exact stdlib Fraction program accompanying this proof constructs every one of the 63 \(C_{D_U}\), verifies each is squarefree and that none has eigenvalue 1, and computes **all 1953** pairwise rational polynomial gcds. Its exact exhaustive result: precisely \({20\choose2}=190\) pairwise gcds are nonconstant, all equal \(x-1/2\), occurring exactly among the 20 displayed blocks. Every other gcd is 1. Thus exactly 19 duplicate degrees are eliminated:

\[
\boxed{d_{\min}=1+249-(20-1)=231.}
\]

No untested other inter-block collision is needed for this finite certificate.

To verify **minimality** rather than only annihilation, note P is reversible with \(\rho_i\propto\pi_i/(1-\alpha_i)\), and the symmetric similarity image of a proper killed block is
\[
K_D=\operatorname{diag}(\alpha_i)_{i\in D}+vv^\top,\qquad v_i=\sqrt{(1-\alpha_i)\pi_i}.
\]
With distinct holding values the secular eigenvalues are simple and a secular eigenvector has coordinates proportional to \(v_i/(\lambda-\alpha_i)\). Its scalar-observer overlap with \((\sqrt{\rho_i})_{i\in D}\) is proportional to
\[
\sum_{i\in D}\frac{\pi_i}{\lambda-\alpha_i}
=\frac{1-q_D}{1-\lambda}>0,\qquad q_D=\sum_{i\in D}\pi_i<1 .
\]
Here \(K_D\) is positive definite and proper-block stochastic killing makes \(\lambda<1\). Hence **every** proper-block eigenmode has nonzero, indeed positive, scalar spectral weight. Contributions of repeated modes from different blocks add, and the polynomial lcm has exactly the minimal scalar recurrence degree 231. This example is strictly positive, reversible and has positive spectrum; the observed sequence is completely monotone under stationary initialization. QED.

## Exact reproducibility and limits

Run Python 3 standard-library-only \`R232_sperner_spectral_collision_231_check.py\`. It performs all fraction arithmetic exactly, asserts the twenty source masks, verifies 63 block squarefreeness checks and all 1953 inter-block gcds, returns 190 nontrivial gcd pairs only at eigenvalue 1/2, and asserts degree 231. Its JSON result is \`R232_verification.json\`, status PASS.

General Sperner bound: symbolic author proof. Concrete 231-dimensional example: fully enumerated rational polynomial certificate for the declared 7-state source model. Independent review: NOT_REVIEWED. Native BRC EffectHistogram execution: NOT_EXECUTED. R231 rank 244 remains a separate correct but weaker explicit example.

## Open questions

Determine the **global smallest** scalar recurrence degree among all strictly positive 7-state sticky-reset models: one-mode Sperner bound does not settle simultaneous collisions at multiple distinct eigenvalues. Study collision variety codimensions and exact-bit time/space of 231-/250-mode minimal recurrences against the direct 256 reachable support/current-source states. Build a **read-only** scalar support-ideal observer on native BRC EffectHistogram with no loss of signed branches, ports, provenance, multiplicities, exact positive weights and joint/cross moments. No formal Task CLAIM, Result, Review or Foundation promotion is asserted by publication.
