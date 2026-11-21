# X6 R75 — 全维奇偶精度分组的正权 BRC 星形矩：锐性临界半径、Port 门槛和唯一竞争结构

Date: 2026-11-21 (Asia/Shanghai)
Scientific status: CONDITIONAL_AUTHOR_PROOF / EXACT_INTEGER_AUTHOR_CHECK / NOT_INDEPENDENTLY_REVIEWED
Scope: conditional positive-count BRC degree-histogram observer, not native X6 Cell/Link/Port dynamics
Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json (P000 V5)
Predecessors: R64 common-bias collision law, R65 uniform all-D threshold, R68 heterogeneous weights, R72 D=4 all-weight atlas, R74 two-noisy-middle-channel case.

## Problem, observer and provenance

Fix integers \(p\ge D\ge2\). Each of \(p\) named A Ports has a conditional positive-count success degree \(d\in\{0,\dots,D\}\), with integer counts \(c_0,\dots,c_D\ge0\) summing to \(p\). An independently reset second source gives the declared conditional observation

\[
Y_t=m_t(c)+b+e_t,\qquad m_t(c)=\sum_{d=0}^D c_d d^t,\quad
|e_t|\le\eta w_t,\quad 1\le t\le D,
\]

where \(b\in\mathbb R\) is one unknown common additive offset. The recovery target is the high-degree histogram \((c_2,\ldots,c_D)\). Fix arbitrary **positive** real numbers \(x,y\) and put

\[
w_t=\begin{cases}x,&t\text{ odd},\\y,&t\text{ even}.\end{cases}
\]

Thus the odd-indexed measurement channels share one error weight and the even-indexed channels share another; **there is no bound on \(x/y\)**.

This is an observer-specific, positive-count, finite-histogram result. Original named-port identity, full joint relation, branch multiplicity, signed/phase data, Cell/Link incidence, independently typed time, and the whole TRIADIC_CLOSURE_E reset event remain in the project substrate, outside this quotient. The present proof does not assert an actual X6 physical reset implementation or infer a native residual from ordinary moment arithmetic.

For \(a=(a_2,\ldots,a_D)\in\mathbb Z^{D-1}\setminus\{0\}\), define

\[
q(a)=\max\Big(\sum_{d=2}^D(a_d)_+,\sum_{d=2}^D(-a_d)_+\Big),
\quad z_1=0,\quad
z_t=\sum_{d=2}^D a_d(d^t-d)\;(t\ge2).
\]

A difference is realizable at population \(p\) if and only if \(q(a)\le p\), using degree-zero/one filler counts. The R68 exact common-bias pair-collision formula is

\[
\eta_{\rm pair}(a;w)=\frac12\max_{1\le i<j\le D}
\frac{|z_j-z_i|}{w_i+w_j}.
\]

The sharp histogram recovery radius \(\eta^*_{p,D}(w)\) is the minimum of \(\eta_{\rm pair}\) over all nonzero feasible integer differences. Strictly below the radius the high-degree histogram is identifiable; at the radius two different targets admit a shared noisy observation.

## Theorem R75: cross-parity rigidity

Put \(Q_D=2^D-D-1\), and define the alternating binomial vector

\[
a_d^*=(-1)^d\binom{D+1}{d+1},\qquad d=2,\dots,D.
\]

Define the *cross-parity integer gap* \(C_D(a)=\max_{i\ {\rm odd},\,j\ {\rm even}}|z_i-z_j|\), where \(1\le i,j\le D\).

**Rigidity.** For every \(D\ge2\), \(C_D(a)\) is a positive even integer, and

\[
\boxed{C_D(a)=2\quad\Longleftrightarrow\quad a=\pm a^*.}
\]

Every other nonzero integer difference satisfies \(C_D(a)\ge4\).

**Sharp heterogeneous precision plateau.** For every \(x,y>0\), \(p\ge D\ge2\),

\[
\boxed{
\begin{aligned}
p\ge Q_D &: \quad \eta^*_{p,D}(x,y)=\frac1{x+y},
\quad\operatorname{argmin}=\{\pm a^*\},\\
D\le p<Q_D &: \quad\eta^*_{p,D}(x,y)\ge\frac2{x+y}.
\end{aligned}}
\]

The smallest admissible population at which the \(1/(x+y)\) radius is reached is \(\max(D,Q_D)\). In this entire two-weight family this is also the sharp all-\(x,y\) saturation population; **the optimizer remains unique up to sign at arbitrarily large precision anisotropy**.

The table of first admissible populations is \(D=2:2\), \(D=3:4\), \(D=4:11\), \(D=5:26\), \(D=6:57\), \(D=7:120\), \(D=8:247\). For \(D=2\), \(Q_2=1\) but the model separately imposes \(p\ge D\).

## Proof

**1. Evenness and injectivity.** For every integer \(d\) and \(t\ge2\), \(d^t-d\equiv0\pmod2\), so all \(z_t\) are even. The square matrix \(M_{t,d}=d^t-d\), \(t,d=2,\dots,D\), is nonsingular over \(\mathbb Q\): divide column \(d\) by the nonzero \(d(d-1)\); the remaining entries are evaluations at the distinct nodes \(2,\dots,D\) of the monic consecutive-degree polynomials \(1,1+d,\ldots,1+d+\cdots+d^{D-2}\). The determinant is a nonzero Vandermonde determinant. Thus \(a\ne0\) implies some \(z_t\ne0\).

The graph of all odd-to-even index pairs is complete bipartite and connected, including index \(1\) with \(z_1=0\). If all its gaps vanished, all \(z_t=0\), contradicting injectivity. Hence \(C_D(a)\) is a positive even integer.

**2. A cross gap at most 2 forces all odd moments to vanish.** Assume \(C_D(a)\le2\). Every even-indexed \(z_t\) differs from \(z_1=0\) by at most 2, hence belongs to \(\{-2,0,2\}\). For odd \(t\ge3\), every integer \(d\) satisfies \(d^t-d\equiv0\pmod6\): modulo 2 the difference is zero, and modulo 3 any odd power is congruent to the base. Therefore each such \(z_t\) is divisible by 6. It differs by at most 2 from \(z_2\), and \(|z_2|\le2\), so \(|z_t|\le4\); therefore \(z_t=0\) for all odd \(t\).

**3. All even moments must agree.** For even \(r,s\ge2\), \(d^r-d^s\equiv0\pmod{12}\): modulo 3 the even powers are equal, and modulo 4 both are zero for even \(d\), one for odd \(d\). Hence \(z_r\equiv z_s\pmod{12}\). Each lies in \(\{-2,0,2\}\), so all even-indexed \(z_t\) equal a single \(u\in\{-2,0,2\}\). Nonzero \(a\) and invertibility force \(u=\pm2\). For \(D=2\) or \(3\), the comparison between distinct even indices is vacuous; the same conclusion follows directly.

Thus \(C_D(a)\le2\) forces exactly one of the two signatures \(z_t=1+(-1)^t\) and \(z_t=-1-(-1)^t\).

**4. Identify the unique integer solution.** Let \(N=D+1\) and \(f_t(k)=(k-1)^t-(k-1)\). Since \(\deg(f_t)\le D<N\), its \(N\)-th alternating binomial finite difference is zero:
\[
\sum_{k=0}^{N}(-1)^k\binom Nk f_t(k)=0.
\]
Here \(f_t(1)=f_t(2)=0\) and \(f_t(0)=1+(-1)^t\). Moving the \(k=0,1,2\) terms and substituting \(d=k-1\) gives
\[
\sum_{d=2}^{D}(-1)^d\binom{D+1}{d+1}(d^t-d)
=1+(-1)^t.
\]
So \(a^*\) has exactly the \(+2\)/zero parity signature. Matrix injectivity gives uniqueness, and negation produces the other signature. This completes the rigidity theorem.

**5. Radius and sharp Port threshold.** Every odd-to-even measurement pair has the same denominator \(w_i+w_j=x+y\), hence
\[
\eta_{\rm pair}(a;w)\ge \frac{C_D(a)}{2(x+y)}.
\]
For \(a\ne\pm a^*\) this is at least \(2/(x+y)\). For \(a=\pm a^*\), all equal-parity gaps vanish and every cross gap is exactly 2, so \(\eta_{\rm pair}(a^*;w)=1/(x+y)\), with equality for every \(x,y>0\).

The even-indexed \(d\)'s contribute positive entries to \(a^*\), whose total is
\[
P_+=\sum_{\substack{d\ge2\\d\,{\rm even}}}\binom{D+1}{d+1}=2^D-(D+1).
\]
The negative mass at odd \(d\ge3\) is
\[
P_- = 2^D-1-\binom{D+1}{2}\le P_+.
\]
Consequently \(q(a^*)=P_+=Q_D\). This gives both the exact onset and the factor-two lower bound below onset. At and above onset all other candidates have strictly larger radius, proving uniqueness. QED.

## Research significance

R68's generic sufficient stability condition \(w_{\max}<2w_{\min}\) permits only moderate anisotropy. R75 supplies a distinct **exact structural stability** family with unbounded ratio \(x/y\): the two parity classes may have precision ratios of one to a million, yet the same alternating binomial integer difference remains uniquely hardest to distinguish. The mechanism is the complete cross-parity gap graph plus its congruence rigidity modulo 6 and 12.

Examples: for D=4 and \((w_1,w_2,w_3,w_4)=(1,1000,1,1000)\), \(p=11\) gives exactly \(\eta^*=1/1001\), while \(p\le10\) yields \(\eta^*\ge2/1001\). For D=6, \(p=57\), odd weights 17 and even weights 101 give \(\eta^*=1/118\). These results concern the declared histogram observer and require no approximation or ordinary-trigonometric calculation.

## Reproducibility, evidence and remaining work

The accompanying standard-library Python program computes integer moment differences and exact Fraction radii. It checked explicit \(a^*\), Port population and every parity moment at \(D=2,\dots,12\), across five positive integer weight pairs including 1:1000 and 1000:1. Complete bounded signed integer enumeration at \((D,q_{\max})=(2,2),(3,5),(4,11),(5,8)\) covered 4, 90, 5082 and 15420 feasible nonzero vectors respectively, total 20,596; the only vectors with cross gap 2 in the covered ranges are the two signs of \(a^*\) when \(q_{\max}\ge Q_D\). The finite checks are author verification; the all-dimensional claim is supported by the symbolic proof above.

Published companion paths:
- research_notes/portable_direct/x6_r75_parity_block_exact_verify.py
- research_notes/portable_direct/x6_r75_parity_block_exact_results.json

Scientific input P000 V5 and current ACTIVE worldview/joint-observer rule are preserved. No source-native Cell/Link/Port fidelity theorem, signed/phase recovery, or physical-time interpretation is claimed. Next scientific questions: (i) characterize exact arbitrary-four-weight chambers and strict winners of R72's 28-vector atlas; (ii) determine native whole-triad provenance-preserving maps to the positive BRC observer and which future operations genuinely descend through it.

Historical line: RS-X6-NATIVE-TIME-DYNAMICS; historical provenance EM-X6-214D9C, RA-545183ADD4EF71C3E4698AEE. Historical identities are not live session capabilities. Formal control ownership and source Activity mutation are separately checked, and this portable result is not a CLAIM, PROGRESS, Result acceptance or independent review.
