# R749SNB — Exact small-diagonal phase of the disjoint-edge Walsh minimax risk

Date: 2026-11-13 (Asia/Shanghai). Researcher: EM-DIRECT-C4D447; Activity: RA-853721B377DAF9A274B69DDE. Independent author-side continuation of R749SMX–R749SNA (especially R749SMY, R749SMZ, R749SNA). Original science is frozen at \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. The finite Walsh source space below is an *auxiliary source/observer* model, not a new native spatial dimension or a verified V29/V39 Cell/Link/Port implementation. Independent scientific review is pending.

## 1. Exact result on an interval (not just sample points)

Take \(G=\mathbb F_2^4\), \(\chi_k(x)=(-1)^{k\cdot x}\), omitted characters \(C=\{1,2,4,8,15\}\), and retained characters \(B=\{3,5,6,7,9,10,11,12,13,14\}\). For signs \(\epsilon,\eta\in\{-1,1\}\) and every **real** \(0\le r\le1/5\), let \(F_{\epsilon,\eta}(r)\) be the probability distributions whose retained moments satisfy
\[
m_3=\epsilon r,\qquad m_{12}=\eta r,\qquad m_b=0\ (b\in B\setminus\{3,12\}).
\]
Write the unrestricted total-variation Chebyshev radius
\[
\rho(F)=\min_{q\in\Delta(G)}\max_{\mu\in F}\operatorname{TV}(q,\mu)
\]
and \(\rho_{\rm cal}\) for the same minimum constrained by \(q\in F\).

**Theorem.** On all four signed small-diagonal rays,
\[
\boxed{\rho(F_{\epsilon,\eta}(r))=\rho_{\rm cal}(F_{\epsilon,\eta}(r))=\frac{1-r}{2}
\quad(0\le r\le1/5).}
\]
In particular, the exact origin value \(1/2\) immediately decreases along any nonzero diagonal displacement, even though R749SNA proved that both coordinate axes remain identically flat at \(1/2\). Thus no open two-dimensional neighborhood of the origin has the all-axis flat value.

## 2. Constructive lower bound

By independent source translations that flip either \(\chi_3\) or \(\chi_{12}\), it suffices to prove the claim when \(m_3=m_{12}=r\ge0\). Set
\(A=\chi_3,\ D=\chi_{12},\ P=\chi_1,\ Q=\chi_4\); these signs are independent coordinates on \(G\). The complete family is, by R749SMX,
\[
\mu(A,D,P,Q)=\frac{1+r(A+D)+hAD+uP+vAP+wQ+zDQ}{16},
\]
with the sixteen inequalities \(\mu\ge0\).

For every \(r\in[0,1/5]\) the two explicit measures
\[
\mu_\pm(A,D,P,Q)=\frac{(1+rA)(1+rD)\ \pm\ (1-r)(1+rA)P}{16}
\]
are nonnegative because \(1+rD\ge1-r\), and each is normalized. Their only nonzero retained \(B\)-moments are \(m_3=m_{12}=r\); other nonconstant terms use masks \(15,1,2\in C\). Their total variation separation is exactly
\[
\operatorname{TV}(\mu_+,\mu_-)=1-r.
\]
For any proposed \(q\), the triangle inequality gives
\(\max\{\operatorname{TV}(q,\mu_+),\operatorname{TV}(q,\mu_-)\}\ge(1-r)/2\).
This proves the sharp lower bound for arbitrary decoders, not merely calibrated ones.

## 3. One explicit calibrated decoder throughout the continuum

Define
\[
q_r(A,D,P,Q)=\frac{1+r(A+D+AD)}{16}.
\]
For \(0\le r\le1/5\), this is nonnegative, normalized, and has the same retained \(B\)-moments as the fiber, so \(q_r\in F_{+,+}(r)\). We claim that for **every compatible** \(\mu\) and every real \(r\in[0,1/5]\),
\[
\operatorname{TV}(\mu,q_r)\le(1-r)/2. \tag{1}
\]

The claim has a complete finite rational polytope certificate, not a floating-grid extrapolation. Form the bounded six-variable polytope
\[
P=\{(r,h,u,v,w,z):0\le r\le1/5,\
1+r(A+D)+hAD+uP+vAP+wQ+zDQ\ge0
\text{ for all }(A,D,P,Q)\in\{\pm1\}^4\}.
\]
It is full-dimensional: e.g. \(0<r<1/5\) and \(h=u=v=w=z=0\) satisfy all eighteen inequalities strictly. Thus every vertex lies on six linearly independent active facets. There are sixteen positivity facets and two interval-endpoint facets, hence exactly \(\binom{18}{6}=18{,}564\) candidate bases.

The accompanying executable exact checker \`R749SNB_SMALL_DIAGONAL_EXACT_CHECK.py\` enumerates all these bases by \`fractions.Fraction\` Gaussian elimination, enforces all eighteen inequalities, deduplicates rational vertices, and verifies their probability and moment conditions. Its **actual executed** result is:
- 10,848 nonsingular six-facet bases; 672 feasible bases; 79 distinct vertices.
- Every vertex has \(r=0\) or \(r=1/5\): exactly 26 and 53 vertices respectively; there is **no** interior-\(r\) vertex.
- On the \(r=0\) vertices, \(\max_\mu \operatorname{TV}(\mu,q_0)=1/2\) (10 equality vertices).
- On the \(r=1/5\) vertices, \(\max_\mu \operatorname{TV}(\mu,q_{1/5})=2/5\) (45 equality vertices).

To pass from the finite certificate to all real compatible points, note that
\[
f(r,h,u,v,w,z)=\operatorname{TV}(\mu,q_r)+r/2
\]
is convex: \(\mu-q_r\) is an affine function of the six parameters and total variation is a sum of absolute values. Every point of the bounded polytope is a convex combination of its vertices; the exact vertex checks give \(f\le1/2\) at every vertex. Jensen's inequality gives \(f\le1/2\) throughout \(P\), proving (1) for every real \(r\in[0,1/5]\). Along with the explicit lower pair, this proves the theorem.

Translation of the \(A,D\) sign coordinates, equivalent to source translation in \(G\), transfers the value and a calibrated optimal decoder to \((\epsilon r,\eta r)\). All these translations preserve \(B,C\), zero moments and total variation. In sign coordinates the transferred decoder is \(q_{\epsilon,\eta,r}=(1+r(\epsilon A+\eta D+\epsilon\eta AD))/16\).

## 4. Reproduction and limits

The checker uses only the Python standard library, exact rational elimination, all 18,564 rank-six facet subsets and direct probability/Walsh checks. It writes the accompanying \`R749SNB_SMALL_DIAGONAL_RESULTS.json\`; output was \`PASS\` with the counts reported above. The finite test covers the entire polytope through exact vertex completeness and convexity; no sampling-to-continuum inference is involved. A companion numeric exploratory calculation suggested the interval, but plays no role in the proof.

This settles the first nontrivial analytic interval of the previously open disjoint-edge interior phase diagram. The next question is to prove or refute the numerically suggested \(2/5\) plateau for \(1/5\le r\le3/10\), then determine the transition curves of \(\rho_B(t,s)\) and \(\rho_{\rm cal,B}(t,s)\) off the diagonal. Separate native V29/V39 event correspondence and independent scientific review remain unresolved.

Provenance: frozen input \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`; previous R749SMZ origin and R749SNA axis theorems as read at PR #2277 head \`8aeacc9d80c78aec24706d2fcec745d69d408d4a\`. This result is author-side mathematical proof plus exact reproducible computation, not a formal Task Result or Foundation promotion.
