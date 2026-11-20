# X6 R65 — Universal half-radius onset for common-bias positive-BRC star-moment tomography

Date: 2026-11-21 (Asia/Shanghai)  
Line: RS-X6-NATIVE-TIME-DYNAMICS (historical provenance; current native owner authority must be checked independently)  
Scientific status: CONDITIONAL_AUTHOR_PROOF / EXACT_INTEGER_AUTHOR_CHECK / NOT_INDEPENDENTLY_REVIEWED  
Project substrate: frozen P000 V5 at \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\`; ACTIVE six-axis Heartbeat World and joint-observer preservation. This result concerns only the explicitly declared conditional positive-weighted AB observer, not an established native \`TRIADIC_CLOSURE_E\` reset process.

Predecessor: R64, \`research_notes/portable_direct/2026-11-21_x6_r64_shared_bias_minimax_star_moment_radius.md\` at commit \`bc1955b3c5471b1e3262f7b24d6c5e36ae511521\`. Reuse its exact pairwise common-bias distance and its integer-lattice feasibility result.

## R65 theorem: exact onset of the universal \`1/2\` accuracy plateau

Fix integers \`p >= D >= 2\`. A labelled binary \`p x p\` success-incidence table has row-success-degree histogram \`c=(c_0,...,c_D)\`, with nonnegative integer entries, \`sum c_d=p\`, and all degrees bounded by \`D\`. Each repeated-A, independently reset positive-BRC star observation, after normalization by known strictly positive branch weights, is

\[
m_t(c)=\sum_{d=0}^{D}c_d d^t,\qquad
y_t=m_t(c)+b+e_t,\quad t=1,\ldots,D,
\]
where \`b\` is one unknown real additive offset, \`|e_t|<=eta\`, and \`m_0=p\` is known separately. The target is the high-degree subhistogram \`(c_2,...,c_D)\`. Every such histogram is realizable as a named binary relation because \`D<=p\`.

Define \`eta*_(p,D)\` to be the largest strict uniform uniqueness threshold: for \`eta<eta*\`, every pair of compatible candidates has the same target; at \`eta=eta*\`, some pair with different target is compatible.

**Theorem (all \`D>=2\`, all \`p>=D\`):**

\[
\boxed{\eta^*_{p,D}=\frac12\quad\Longleftrightarrow\quad p\ge 2^D-D-1.}
\]

If \`D<=p<2^D-D-1\`, then \`eta*_(p,D)>=1\`. At the exact plateau onset, the two minimal competing high-degree difference vectors are opposite signs of

\[
\boxed{a_d=(-1)^d\binom{D+1}{d+1},\qquad d=2,\ldots,D.}
\]

Their minimum necessary Port population is exactly \`2^D-D-1\`. Apart from exchanging the two models, these are the **only** differences attaining oscillation \`2\` in the normalized positive-moment model.

Thus the previously finite D=3 and D=4 onset values (4 and 11 Ports) and the newly solved D=5 onset (26 Ports) are instances of one exact all-D law.

### Proof

**(1) R64 minimax reduction and parity lower bound.** Write \`a_d=c_d-c'_d\` for \`d>=2\`, and

\[
z_1=0,\qquad z_t=\sum_{d=2}^{D}a_d(d^t-d),\quad 2\le t\le D.
\]

The unknown common offset removes the constant direction, and R64 proves that a nonzero integer vector \`a\` is feasible at population \`p\` if and only if
\[
\max(P_+(a),P_-(a))\le p,\qquad
P_\pm(a)=\sum_{d=2}^{D}\max(\pm a_d,0),
\]
and its pairwise observation ambiguity starts at \`osc(0,z_2,...,z_D)/4\`.

For every integer \`d\` and \`t>=2\`, \`d^t-d\` is even. Therefore all \`z_t\` are even integers. The matrix
\[
M_{t,d}=d^t-d=d(d-1)(1+d+\cdots+d^{t-2})
\]
for \`t,d=2,...,D\` is invertible: after dividing each column by nonzero \`d(d-1)\`, the rows are evaluations of monic polynomials of successive degrees \`0,...,D-2\` at distinct integers \`2,...,D\`, hence a nonsingular Vandermonde transform. Consequently a nonzero \`a\` yields nonzero \`z\`. Since \`z_1=0\`, its oscillation is a positive even integer, at least \`2\`; thus \`eta*>=1/2\`.

**(2) Classification of every oscillation-2 possibility.** Replace \`a\` by \`-a\` if necessary. At oscillation \`2\`, each \`z_t\` belongs to \`{0,2}\`. For any integer \`d\` and \`t>=2\`,
\[
d^{t+2}-d^t=d^t(d^2-1)\equiv0\pmod4.
\]
For even \`d\`, \`d^t\` is divisible by \`4\`; for odd \`d\`, \`d^2-1\` is divisible by \`8\`. Hence \`z_{t+2}\equiv z_t\pmod4\`. Since both are \`0\` or \`2\`, they must be equal. For \`D>=3\`, only three nonzero patterns remain: E = \`z_t=2\` on even \`t\` and \`0\` on odd \`t\`; O = the converse; A = \`z_t=2\` at every \`t\`. (For \`D=2\`, E is the only nonzero pattern.)

**(3) An exact integrality obstruction eliminates O and A.** Let \`s(D,t)\` be signed Stirling numbers of the first kind:
\[
x(x-1)\cdots(x-D+1)=\sum_{t=1}^{D}s(D,t)x^t.
\]
Because this polynomial vanishes at \`x=1\`, it is also \`\sum_{t=2}^{D}s(D,t)(x^t-x)\`. Its value at \`d=2,...,D-1\` is zero and at \`D\` is \`D!\`. Thus
\[
D!a_D=\sum_{t=2}^{D}s(D,t)z_t.
\]
Using \`s(D,1)=(-1)^{D-1}(D-1)!\`, the polynomial values at \`x=1,-1\`, and the three patterns gives
\[
a_D(E)=(-1)^D,\qquad
a_D(O)=(-1)^{D+1}\frac{D-2}{D},\qquad
a_D(A)=(-1)^D\frac2D.
\]
For every \`D>=3\`, the latter two are not integers; only E can be produced by an integer histogram difference.

**(4) Unique feasible vector and exact Port threshold.** The vector
\[
a_d=(-1)^d\binom{D+1}{d+1}
\]
satisfies \`z_t=1+(-1)^t\` for \`2<=t<=D\`. Indeed, the \`(D+1)\`st alternating finite difference of \`g(x)=x^t-x\` is zero for \`t<=D\`; the omitted \`x=-1,0,1\` contributions yield exactly \`1+(-1)^t\`. Invertibility of \`M\` proves that this solution is unique. Its positive and negative high-degree masses are
\[
P_+=\sum_{\substack{2\le d\le D\\ d\ \mathrm{even}}}\binom{D+1}{d+1}
=2^D-(D+1),
\]
\[
P_-=\sum_{\substack{2\le d\le D\\ d\ \mathrm{odd}}}\binom{D+1}{d+1}
=2^D-1-\binom{D+1}{2}\le P_+.
\]
The R64 feasibility criterion therefore gives exactly \`p_min=max(P_+,P_-)=2^D-D-1\`. At and above this population, the explicit models reach oscillation \`2\`, and the lower bound shows \`eta*=1/2\`. Below this population, oscillation \`2\` is impossible; every nonzero feasible difference has even oscillation at least \`4\`, giving \`eta*>=1\`. This proves the theorem. \`QED\`.

### Explicit D=5 equality witness

At \`D=5\`, \`p_min=26\`, \`(a_2,a_3,a_4,a_5)=(20,-15,6,-1)\`. Two feasible histograms (ordered by degrees \`0,...,5\`) are
\[
c=(0,0,20,0,6,0),\quad c'=(10,0,0,15,0,1).
\]
Their moment differences for \`t=1,...,5\` are exactly \`(14,16,14,16,14)\`; the unknown-bias-adjusted oscillation is \`2\`, and the sharp error radius is \`1/2\`.

### Executed verification and evidence scope

The companion standard-library Python verifier checks all explicit binomial vectors for \`D=2,...,12\`, including histogram feasibility, all moment coordinates and oscillation. It exhausts all \`2^(D-1)-1\` nonzero one-sided width-two patterns per \`D\` (4,083 patterns in total), checking a necessary exact signed-Stirling divisibility condition. It also exhausts 50,154 feasible nonzero integer-lattice candidates over the separately declared small ranges \`D=2,p=2..4;\ D=3,p=3..5;\ D=4,p=4..11;\ D=5,p=5..8\`. All checks PASS, with \`D=5,p=5..8\` giving oscillation \`30\` and \`D=4,p=11\` giving oscillation \`2\`. These computations reproduce the stated finite ranges; the all-D theorem relies on the mathematical proof above, not a finite extrapolation.

Companions:
- \`research_notes/portable_direct/x6_r65_universal_half_radius_plateau_verify.py\`
- \`research_notes/portable_direct/x6_r65_universal_half_radius_plateau_results.json\`

### Remaining scientific questions and status

1. Determine the exact intermediate staircase \`eta*_(p,D)\` for \`D>=5\` below \`2^D-D-1\`; the theorem now gives the exact final onset and a strict integer-lattice gap.
2. Establish which typed native \`TRIADIC_CLOSURE_E\` whole-triad reset/Port identities actually realize the conditional BRC repeated-A observer, without discarding Cell, Link, source or path provenance.
3. Generalize the minimax calculation to unequal channel budgets and unnormalized positive masses, for which common raw offset becomes a nonconstant direction after normalization.

The observations are a conditional positive BRC quotient for a declared histogram target only. Raw Cell/Link incidence remains retained for future native dynamics; no independent proof review or formal Task Result admission is asserted.
