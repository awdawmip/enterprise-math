# R284BT — Two frozen star-Port leaves: an exact alias strip, a one-free-leaf noise ceiling, and a sharp 4×4 binary certificate

Date: 2026-11-20 (Asia/Shanghai).
Scientific status: AUTHOR_PROVED / EXACT_EXHAUSTIVE_CERTIFICATE_PASSED / NOT_REVIEWED.
Research line: R284BS @ immutable source commit \`3e97c6471e6b8e5caa2e0eeb5ae15c5eef8d2937\` (single frozen leaf). No change to that source, to P000, or to any formal task, owner, Result or Review. Historic R1 portable lineage: EM-DIRECT-E6B1DD; this note does not claim a currently authenticated research session.

## Observer and theorem A: a universal exact alias strip

For integers \(n\ge3\), \(H\ge2\), let \(C\in\{1,\ldots,H\}^{n\times n}\) and
\[
 F_C(d,z)=\det\left(\operatorname{diag}(d)-C-\sum_{i=1}^{n-1}z_i E_{0i}\right).
\]
Freeze two *distinct leaves* \(j,k\) to integers \(d_j=t,d_k=s\), retaining all other controls free. If
\[
                         |t-s|\le H-1, \tag{A}
\]
then there exist distinct \(C,D\) in the full alphabet with **identical restricted response polynomials** for all remaining controls. No number of adaptive observations with these frozen diagonal values can distinguish the pair, even with zero noise. This holds for arbitrarily large \(|t|\) and \(|s|\).

**Proof.** Select \(c_j,c_k\in\{1,\ldots,H\}\) such that \(c_j-c_k=t-s\). Start with the all-ones matrix, change only \(C_{jj}=c_j,C_{kk}=c_k,C_{0j}=2,C_{0k}=1\). Let \(D\) be identical except \(D_{0j}=1,D_{0k}=2\). Put \(B=\operatorname{diag}(d_1,\ldots,d_{n-1})-A\), where \(A\) is the leaf block, and \(v=(C_{10},\ldots,C_{n-1,0})^T=\mathbf1\). The two frozen diagonal entries of \(B\) are equal (\(t-c_j=s-c_k\)); all off-diagonal entries are \(-1\). Hence the simultaneous permutation \(j\leftrightarrow k\) preserves \(B\) and \(v\), and therefore \(g=\operatorname{adj}(B)v\) has \(g_j=g_k\) as polynomial functions of every remaining control. In the block determinant identity
\[
 F_C=(d_0-C_{00})\det B-(b+z)^Tg,\qquad b_i=C_{0i},
\]
the sole change \(b_j-b_k\mapsto b_k-b_j\) contributes \(g_j-g_k=0\). Thus \(F_C=F_D\) identically. QED.

The strip (A) is a **sufficient exact-collision region**; this theorem does not classify every other resonant pair \((t,s)\).

## Theorem B: a finite noise ceiling when one leaf remains free

Let \(n\ge3\), freeze **all but one** leaf-diagonal controls to finite integers \(t_i\), and leave only leaf \(\ell\) unfrozen (besides \(d_0\) and all star controls \(z_i\)). For every \(H\ge2\), there is a pair of distinct candidate matrices such that the observation difference is the control-independent integer
\[
                   F_D-F_C=-\prod_{i\ne\ell,\ i\ge1} t_i. \tag{B}
\]

**Proof.** Let \(C\) be the all-ones matrix \(J_n\), and obtain \(D\) by increasing only \(C_{0\ell}\) from \(1\) to \(2\). With \(m=n-1\), the leaf block is \(B=\operatorname{diag}(d_1,\ldots,d_m)-\mathbf1\mathbf1^T\), \(v=\mathbf1\). The polynomial identity
\[
 [\operatorname{adj}(\operatorname{diag}(d)-\mathbf1\mathbf1^T)\mathbf1]_\ell
       =\prod_{i\ne\ell}d_i
\]
follows from the matrix determinant lemma on the open set where all \(d_i\) are invertible and then by polynomial identity. Since only \(b_\ell=C_{0\ell}\) changes, the block determinant formula gives (B). QED.

For a real-circle residue observation modulo any prime \(p\), the circular separation of these two candidates is at most \(\left|\prod_{i\ne\ell}t_i\right|\), independent of the remaining controls. Thus if the adversarial circular error radius satisfies
\[
          2\rho\ge\left|\prod_{i\ne\ell}t_i\right|, \tag{C}
\]
the two closed error balls intersect, and no one-reading controller can guarantee recovery. In fact, even adaptive repetitions under the same fixed frozen controls cannot distinguish against an adversary that returns the midpoint on each observation. If the product is zero, the pair has identical responses already at zero noise.

For \(n=4\), freezing two leaves \(d_1=t,d_2=s\) leaves exactly one free leaf \(d_3\); (C) becomes \(2\rho\ge|ts|\). Unlike the single-frozen-leaf result R284BS in \(n\ge4\), **no fixed finite pair \((t,s)\)** here can support uniform recovery for *every* finite noise radius merely by enlarging \(p\) and changing the remaining free controls. One may instead select new frozen settings as a function of the desired radius; that is a distinct quantifier order.

## Theorem C: sharp radius at an explicit four-dimensional binary setting

Take \(n=4,H=2\), freeze \(d_1=5,d_2=50\), leave \(d_0,d_3,z_1,z_2,z_3\) free. The complete exact integer coefficient census of all \(2^{16}=65{,}536\) candidates establishes:

- The **full** response polynomials are pairwise distinct: 65,536 signatures.
- After dropping *only* the coefficient constant in all free controls, there are 32,768 signature classes, each of size two; every doubleton differs **only** in the entry \(C_{03}\).
- The absolute constant differences inside these doubletons lie between **195** and **612**; the minimum **195** is attained.

Consequently, for this fixed frozen setting and the single finite-field real-circle observation model, the exact existence criterion is
\[
 \boxed{\text{there exist a prime }p\text{ and fixed free controls correcting all errors }|\varepsilon|\le\rho
        \iff 0\le\rho<195/2.} \tag{D}
\]
Here the control choice may depend on \(\rho\), the candidate table is finite, and the decoder can use table lookup. No efficient decoder or small modulus is asserted.

**Sharp negative direction.** Two matrices with row-major binary mask IDs \(1640,1632\) are identical except for \(C_{03}=2\) versus \(C_{03}=1\):
\[
 C=\begin{pmatrix}1&1&1&2\\1&2&2&1\\1&2&2&1\\1&1&1&1\end{pmatrix},
 \quad
 D=\begin{pmatrix}1&1&1&1\\1&2&2&1\\1&2&2&1\\1&1&1&1\end{pmatrix}.
\]
For every free-control setting, their response difference has absolute value 195. Any circle distance is at most 195, so \(2\rho\ge195\) makes robust unique decoding impossible.

**Positive direction.** Write the response, using \(x=d_3\), as
\[
 F_C=d_0(L_0+xL_1)
 -\sum_{i=1}^3 z_i(g_{i,0}+xg_{i,1})
 +(f_0+xf_1).
\]
These ten integer coefficients are determined by evaluating the three-by-three leaf determinant and adjugate vector at \(x=0,1\). The exact census reports all full signatures distinct and identifies every possible *constant* difference as an integer of magnitude at least 195. For \(m=\lfloor2\rho\rfloor\le194\), these constant pairs already have separation \(>2\rho\) whenever \(p>612+m\). Every remaining candidate-pair difference is a **nonconstant** integer polynomial \(Q\) in the five free controls, of total degree at most two. For every integer \(e\in[-m,m]\), \(Q-e\) is nonzero. Take a prime \(p\) large enough that all of their nonzero coefficients remain nonzero modulo \(p\) and
\[
               \frac{2(2m+1)\binom{65536}{2}}p<1.
\]
Schwartz–Zippel and the union bound show that some common assignment of the five free controls avoids all distances \(0,\ldots,m\) around the circle. Hence every candidate has disjoint closed error balls of radius \(\rho\). This proves (D), conditional only on the *exhaustive exact-integer certificate* described below.

## Reproducible exact certificate and scope

Companion artifacts:
- \`research_notes/portable_direct/R284BT_double_frozen_port_checker.py\`: standard-library Python, complete enumeration of all 65,536 binary matrices, ten-coefficient signatures and constant-gap grouping.
- \`research_notes/portable_direct/R284BT_double_frozen_port_verification.json\`: counts, exact minimum/maximum, witness matrices and the mask convention.

The checker also compares its coefficient evaluation with an independently formulated \(4\times4\) permutation-expansion determinant on **256** deterministic masks and free-control settings. All integers are exact; no floating-point computation or Monte Carlo inference enters the certificate. The exhaustive claim is limited to \(n=4,H=2,t=5,s=50\). Theorems A and B are algebraic for the stated general domains. The circle-noise existence statement follows from the finite certificate plus the algebraic union-bound argument. Independent mathematical review: \`NOT_REVIEWED\`.

The zero-noise aliases in A are exact observer fibres. They are not certified to remain equivalent if the frozen controls are later released, or if a different Port geometry/native BRC/X6 operation is admitted; provenance and directional residuals must therefore be retained under the project's observer-fidelity rule. These determinant calculations are an auxiliary algebraic model, not a native Heartbeat World computation.

## Next mathematical frontier

Classify the remaining exact-collision locus for two frozen leaves outside the difference strip \(|t-s|\le H-1\) (the finite census at some distant pairs shows additional resonances); derive the best attainable finite noise radius as a function of \((t,s)\), \(n\) and \(H\); look for explicit, low-modulus controls or an algebraic decoder avoiding the \(H^{n^2}\) candidate table. Preserve existing frozen source pins and the independent authorship/review boundaries.

Source publication is independent of Research Activity association; no current formal CLAIM/RESULT/REVIEW is established by this note.
