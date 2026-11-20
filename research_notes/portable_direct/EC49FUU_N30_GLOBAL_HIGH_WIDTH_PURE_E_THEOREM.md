# EC49FUU — Complete high-width pure-E minimax theorem for the n=30 binary observer

**Date:** 2026-11-20 (Asia/Shanghai). **Evidence:** AUTHOR_PROVED / EXACT_FRACTION_BERNSTEIN_CERTIFIED / PARENT_DEPENDENT / NOT_REVIEWED.

## Frozen science and dependency boundary

This continues EC49FUT (PR #2854; immutable commit 328f9f87f928a3080c8df645693bacef2217cae3), with the unchanged BRC16943 scientific input pin **fc0f038e7bfd12c886b4d37f900bfb770c0f61ab**.

The reduction of the full-bit composite minimax problem to count thresholds and fixed nuisance endpoints is inherited from EC49FUO (8df5788adcd977cc809a0e27da180833317e3dfa) and EC49FUQ (96ad7a2c22c274446e74906c48bc6e3234a39436); EC49FUR (0ac1ef58d84517835260e4aefbe6d2c2b3a293c9) provides the convex total-variation dual. Those mathematical parents are author-proved and still NOT_REVIEWED.

The scientific object here is the **lossy binary clipped-price observer**, not a full or sufficient representation of the native X6 / Heartbeat World joint state. Signed residuals, source labels, paths, branches, and provenance are retained at their native upstream scope under P000, the ACTIVE worldview and joint-observer preservation.

Fix \(n=30\), a common nuisance \(\theta\in[0,E]\), and real width \(0<x<1\). Put

\[
E=\frac{31597745}{1653649},\quad \beta=\frac3{637},\quad
u_\theta=\frac{21829245984}{45529434409-456083905\theta},
\]
\[
T_\theta(x)=(1-x)(1-\beta x+\beta x\theta),\quad
p_\theta=1-T_\theta,\quad q_\theta=1-u_\theta T_\theta.
\]

Under equal-prior binary hypotheses, conditional on the same nuisance \(\theta\), the count \(K\) of 30 independent binary hits is binomial with parameters \(p_\theta\) or \(q_\theta\), respectively. Define the signed masses, tail advantage and endpoint advantage gap by

\[
\Delta_\theta(k;x)=\binom{30}{k}
[q_\theta^k(1-q_\theta)^{30-k}-p_\theta^k(1-p_\theta)^{30-k}],
\]
\[
D_\theta^{\ge j}(x)=\sum_{k=j}^{30}\Delta_\theta(k;x),
\qquad G_j(x)=D_E^{\ge j}(x)-D_0^{\ge j}(x).
\]

## Theorem (global closure of the n=30 upper tail)

For \(k=16,\ldots,29\), let \(c_k\) denote the unique root \(\Delta_E(k;c_k)=0\) in \((0,1)\), and set \(c_{30}=1\). Then:

1. **For every real \(x\in[c_{16},1)\), the unique least-favorable endpoint-prior weight is \(\lambda_E=1\).** There are no further forced two-support nuisance-mixing windows anywhere in this entire range.
2. For every \(j=17,\ldots,30\) and \(c_{j-1}<x<c_j\), the full composite minimax decision rule is the deterministic upper-tail threshold \(\phi(K)=\mathbf1\{K\ge j\}\). Its error probability is exactly
   \[
   \boxed{V_{30}(x)=\frac{1-D_E^{\ge j}(x)}2.}
   \]
3. At \(x=c_k\), \(17\le k\le29\), arbitrary randomization on the tie count \(K=k\) (left below \(k\), right above \(k\)) remains minimax; its unique least-favorable endpoint-prior weight is \(1\). At \(x=c_{16}\) the pure-E threshold \(K\ge17\) is minimax; the larger tie-rule set is already specified in EC49FUT.
4. At \(x=1\) both binary laws coincide and the minimax error is \(1/2\); the prior is not unique there. The preceding uniqueness statement is on the stated half-open interval.

**New scope:** EC49FUT had established pure E in 13 separate neighborhoods around \(c_{17},\ldots,c_{29}\). Here every gap between those neighborhoods and the final \(K\ge30\) tail is closed on the full continuum of real widths, starting immediately at the last mixed-window exit \(c_{16}\).

## Exact proof

### 1. E-Bayes root partition

For \(1\le k\le29\), since \(q_E>p_E\), the sign of \(\Delta_E(k;x)\) is the sign of

\[
\left(\frac{1-u_ET_E}{1-T_E}\right)^k u_E^{30-k}-1.
\]

The function \(T_E(x)=(1-x)[1+\beta(E-1)x]\) is strictly decreasing on \(0<x<1\), because \(\beta(E-1)<1\). The ratio \((1-u_ET)/(1-T)\) strictly increases with \(T\) for \(u_E<1\). Hence this signed expression strictly decreases in \(x\). Each verified opposite-sign rational bracket below contains exactly one root. Their strict ordering, together with the binomial monotone likelihood ratio, implies that \(K\ge j\) is E-Bayes on the whole interval \((c_{j-1},c_j)\), \(j=17,\ldots,30\); at a crossing adjacent count thresholds tie.

All root brackets below are strict, and each integer denotes its value divided by \(10^{12}\). The standalone verifier independently evaluates the exact signed mass on both ends.

| k | strict lower integer | strict upper integer |
|---:|---:|---:|
|16|433405288408|433405288409|
|17|474356338011|474356338012|
|18|515357839408|515357839409|
|19|556358678282|556358678283|
|20|597318517188|597318517189|
|21|638205356397|638205356398|
|22|678993711821|678993711822|
|23|719663237873|719663237874|
|24|760197675211|760197675212|
|25|800584038553|800584038554|
|26|840811983841|840811983842|
|27|880873310863|880873310864|
|28|920761569134|920761569135|
|29|960471743261|960471743262|

### 2. Positive Bernstein certificates on the *entire* threshold intervals

Denote the strict brackets of \(c_k\) by \((\ell_k,r_k)\). Every threshold interval \([c_{j-1},c_j]\) is contained in a single rational interval

\[
I_j=[\ell_{j-1},r_j]\quad(17\le j\le29),\qquad
I_{30}=[\ell_{29},1].
\]

The four probability functions \(p_0,q_0,p_E,q_E\) are quadratic polynomials in \(x\) over \(\mathbb Q\). Therefore \(G_j(x)\) is a rational polynomial of degree at most 60. The companion script builds all binomial mass polynomials using exact polynomial convolution and proves the following stronger statements:

- For every \(j=17,\ldots,29\), the **61 coefficients** of the degree-60 Bernstein representation of \(-G_j\) on \(I_j\) are **strictly positive**.
- For \(j=30\), the exact polynomial \(-G_{30}\) has zero remainder on division by \(1-x\), and **all 60 Bernstein coefficients** of the degree-59 polynomial \(-G_{30}/(1-x)\) on \(I_{30}\) are strictly positive.

There are therefore exactly \(13\cdot61+60=\boxed{853}\) positive exact rational coefficient inequalities, covering **14 entire real-width intervals** without sampling. Each Bernstein basis function \(\binom dkt^k(1-t)^{d-k}\) is nonnegative on \(t\in[0,1]\) and the basis sums to one. Positive coefficients yield

\[
\boxed{G_j(x)<0\quad\text{on }I_j\cap(0,1),\ j=17,\ldots,30.}
\]

For the last interval, use \(1-x>0\) before \(x=1\). The checker also verifies the polynomial transformation at both interval endpoints, checks all 14 exact root brackets, recomputes a representative point per interval from the independent original binomial formula, and verifies the exact divisibility at \(x=1\).

### 3. Composite optimality and uniqueness

On \(x\in[c_{j-1},c_j]\), choose the E-Bayes threshold \(\phi_E(K)=\mathbf1\{K\ge j\}\). The certificate gives

\[
D_0(\phi_E)>D_E(\phi_E).
\]

Every candidate rule \(\phi\) satisfies

\[
\min(D_0(\phi),D_E(\phi))
\le D_E(\phi)\le D_E(\phi_E)
=\min(D_0(\phi_E),D_E(\phi_E)).
\]

Thus \(\phi_E\) attains the finite-endpoint minimax upper bound. For prior uniqueness, the convex dual is

\[
f(\lambda)=\sum_{k=0}^{30}[(1-\lambda)\Delta_0(k)+\lambda\Delta_E(k)]_+.
\]

At an ordinary E-Bayes threshold, its left derivative at \(\lambda=1\) equals \(G_j<0\). At a tie, its left derivative is the gap of **one of the two** adjacent E-Bayes thresholds; both adjacent gaps are strictly negative by the certificates. Convexity forces the unique minimizing endpoint weight \(\lambda_E=1\). The count-threshold and endpoint-only parent theorems lift this to the full-bit composite nuisance game. The point \(x=c_{16}\) is included by using the E-Bayes rule \(K\ge17\), for which \(G_{17}<0\).

This completes the claimed high-width theorem, conditional on the explicitly named parent reductions.

## Exact reproducibility

The companion standalone Python 3 standard-library program is:

EC49FUU_N30_GLOBAL_HIGH_WIDTH_PURE_E_VERIFY.py

Run it from the enterprise-math repository root with:

    python3 research_notes/portable_direct/EC49FUU_N30_GLOBAL_HIGH_WIDTH_PURE_E_VERIFY.py

**Executed locally on 2026-11-20:** 14 root/interval checks PASS, 853 strictly positive exact-rational Bernstein coefficients, 14 exact midpoint crosschecks and terminal output:

    ALL PASS: 14 complete rational intervals; 853 strictly positive Bernstein coefficients; roots 16..29 independently bracketed

No floating-point or unbounded numerical search is used for the certificate. The output's mathematical strength is precisely the polynomial signs plus the named author-proved parent reductions; independent mathematical review remains NOT_REVIEWED.

## Next research and identity

The next valuable work is to certify the **lower-width gaps** for \(n=30\) and the onset/order of the early two-support windows, then analyze how the number of mixed windows depends on \(n\). A separate BRC/X6 observer-fiber comparison should quantify the precise information lost under binary count compression.

Prior note lineage includes Researcher EM-DIRECT-8454C6, SID MCP-44cfc4e6f2094f96861854ebefc77e84. These IDs are historical provenance; this independently published portable theorem neither claims that SID as a current capability nor changes any canonical CLAIM, RUN, Result, Review, Activity or protected worldview. Activity association is pending verification of the present logical session identity and permitted CAS path.
