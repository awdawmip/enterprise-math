# R731 — Exact multiedge BRC activation lattice and irreducible cooperation (X6 candidate incidence)

Date: 2026-11-12. Parent task locator from the R730 source: \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`, original publication \`TP2-8B7E13C5904A2D6F1142\`. Frozen scientific pin: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Direct sources: R728 Draft PR #2110 (\`b825881b426fbced70ea0c38ec6146ac7815f688\`) and R730 Draft PR #2113 (\`bce058506fca26817cfb2a4d7ee4fbed748f0e93\`). R729 #2112 is an independent line, not superseded here.

## 1. Precise BRC carrier and observational scope

At a selected native X6 Cell consider six original axis-family labels 0,…,5; their individual source IDs are distinguishable. Let \`a=(a0,...,a5)\` be nonnegative integer populations, \`Σa_i=3m\`. The *candidate* base hypergraph is
\[
H=\{T\subseteq\{0,\ldots,5\}:|T|=3,\ \{0,1\}\not\subseteq T\}.
\]
It contains 16 three-distinct-axis triples, excluding 012,013,014,015. In this candidate model, axes 0 and 1 share one exclusive port while 2,3,4,5 occupy independent ports.

For a nonempty \`S⊆{2,3,4,5}\`, open all types \`T_i={0,1,i}\` for \`i∈S\`. A branch is an unordered partition of **all labeled source IDs** into m valid triples. Let \`s_i\` count occurrences of \`T_i\` and define the exact positive-integer BRC *provenance histogram*
\[
F_{a,S}(\mathbf z)=\sum_{\text{valid labeled partitions }P}\prod_{i\in S}z_i^{s_i(P)}
=\sum_{\mathbf s} C_{\mathbf s}(a;S)\mathbf z^{\mathbf s}.
\]
Total \`F(1,…,1)\` forgets the counts of the individual new triple types. This is a combinatorial candidate-incidence model; no actual native \`TRIADIC_CLOSURE_E\`, V29 PASS/TRANSFER, V39 current \`j\`, or lawful physical port-open event is inferred.

## 2. Theorem A: exact integer lattice polytope of joint activation

For \`B=a0+a1\`, \`q=Σ_{i∈S}s_i\`, and \`m≥0\`, one has \`C_s(a;S)>0\` **if and only if** all of the following integer inequalities hold:
\[
0\le s_i\le a_i\quad(i\in S),\qquad
\max(0,B-m)\le q\le\min(a_0,a_1,m),
\]
\[
q-s_i\le m-a_i\quad(i\in S),\qquad
q\le m-a_j\quad(j\in\{2,3,4,5\}\setminus S).
\]
Thus support is exactly the integer points of the stated rational convex polytope. This is a finite combinatorial source support statement, not a continuity claim about physical updates.

**Proof.** Fix the use counts s. Remove q axis-0 IDs, q axis-1 IDs, and s_i axis-i IDs for each opened type. Remaining populations in the five exclusive base-port blocks are
\[
B-2q,\quad a_i-s_i\ (i\in S),\quad a_j\ (j\notin S,\ j\ge2).
\]
Exactly \`m-q\` base triples must be formed. The complete five-block three-distinct-block matching criterion says that all remaining labeled IDs admit such a partition iff each block contains at most \`m-q\` IDs; this follows by repeated selection of three highest nonzero block counts, as in R727/R728. Expansion gives \`B-2q≤m-q\`, \`a_i-s_i≤m-q\` and \`a_j≤m-q\`, which are precisely the last inequalities and q≥B−m. The other constraints are source availability and q≤m. Conversely, when these hold the selected new triples can be formed, and the remaining blocks pass that complete matching criterion. Every such integer point is therefore realized. QED.

## 3. Theorem B: exact labeled-source BRC multivariate transfer

Write \`(x)_{↓r}=x!/(x-r)!\` and
\[
a'=a-q(e_0+e_1)-\sum_{i\in S}s_i e_i.
\]
For every feasible s,
\[
\boxed{C_{\mathbf s}(a;S)
=\frac{(a_0)_{\downarrow q}(a_1)_{\downarrow q}
\prod_{i\in S}(a_i)_{\downarrow s_i}}
{\prod_{i\in S}s_i!}\ L_H(a').}
\]
All infeasible coefficients are zero. Here \`L_H(a')\` counts the unordered partitions of the *remaining labeled IDs* into base H triples.

**Proof.** Select q labeled 0 IDs, q labeled 1 IDs and s_i labeled outer IDs; pair the chosen 0 and 1 IDs, distribute the q pair-slots to the new types, and match selected outer IDs to slots of each type. Divide by the s_i! within-type permutations, since triples of the same type are unordered. The residual partition has L_H choices. Every full partition uniquely determines its new labeled triples and residual base triples; hence this is a bijective count, without overcount. QED.

This law reuses R728/R730's exact BRC labeled-branch multiplication and **extends** rather than replacing the single-edge formula.

## 4. Corollary: two-edge clipped rectangle with joint constraints

For two distinct outer axes \`k,l\`, writing \`s=s_k,t=s_l\`, the support is all integer points in
\[
0\le s\le\min(a_k,m-a_l),\quad
0\le t\le\min(a_l,m-a_k),
\]
\[
\max(0,a_0+a_1-m)\le s+t
\le\min(a_0,a_1,m,\{m-a_j:j\in\{2,3,4,5\}\setminus\{k,l\}\}).
\]
Any negative upper bound or inconsistent bounds mean empty support. This is a clipped integer rectangle/strip, not the Cartesian product of two independently valid single-edge intervals. It gives a practical exact support generator without enumerating all source partitions.

## 5. Theorem C: strictly cooperative activation of up to four new edge types

Let \`2≤d≤4\`, \`m≥d\`, and choose d distinct \`k_1,…,k_d ∈{2,3,4,5}\` and positive integers \`r_1,…,r_d\` with \`Σr_i=m\`. Set \`a_0=a_1=m\`, \`a_{k_i}=r_i\`, and all other outer populations zero. Let \`S=\{k_1,\ldots,k_d\}\`.

Then:
\[
\boxed{F_{a,S}(\mathbf z)=(m!)^2 \prod_{i=1}^d z_{k_i}^{r_i}.}
\]
Every proper subset of these d edge types, even if all other base types H remain enabled, admits **zero** valid partitions.

**Proof.** The m triples must jointly contain all 2m source IDs from axis families 0 and 1. A triple can contain at most two of these; therefore every triple has *both* 0 and 1, and is necessarily one of the new 01k_i types. Its type multiplicities are forced by outer stock r_i. Omitting a positive-stock type makes partition impossible. With all types available, choose an arbitrary bijection between labeled axis-0 and axis-1 IDs (m! choices), then an arbitrary allocation/matching of the m individually labeled outer IDs to the m pairs (m! choices). Thus (m!)² and the single provenance exponent vector. QED.

**Exact witnesses:** For \`m=2, a=(2,2,1,1,0,0)\`, individually opening 012 or 013 creates no branch, but opening both produces \`4 z_2 z_3\`. For \`m=4, a=(4,4,1,1,1,1)\`, opening all four new types produces \`576 z_2z_3z_4z_5\`; opening any strict subset gives zero. This is a rigorous example of *irreducible joint source activation* and an arbitrary-order (in m) factorial-square combinatorial branch count, with cooperation width 2..4 for the six-axis candidate model.

## 6. Verification

Two independent integer-counting implementations were executed with Python 3 standard library and no floating point:

* Two-edge test: all 8,709 occupation vectors with m=0,1,2,3,4, all six unordered pairs of outside axes: **52,254** candidate inputs; compare the polygon-point set to exact positive coefficient support and direct labeled pivot-source recursion to sum of coefficient transfer values. Exact marker: \`R731_TWO_EDGE_BRC_SUPPORT_AND_COOPERATION_EXACT_PASS\`.
* General nonempty opened-edge subsets: all 2,521 occupation vectors for m=0,1,2,3 and all 15 nonempty subsets of the four outer edges: **37,815** candidate inputs. Exact direct recursion equals multivariate coefficient sum. Additionally check 154 cooperative-family instances for d=2,3,4 and m≤8. Marker: \`R731_MULTI_EDGE_LATTICE_POLYTOPE_EXACT_PASS\`.

Executable scripts and result JSON are separate files in this research set; their finite coverage is explicitly narrower than the general theorem, which is supported by the preceding proofs.

## 7. Next discriminating native experiment

Read one *actual lawful* event under the frozen X6 Cell/Link/Port + \`TRIADIC_CLOSURE_E\` + V29/V39 sources. Extract exact signed force/port/branch identities and order, build \`E_native\` and test whether any local event supports one, two or more types 01i under a declared observer. If the candidate conflict hypergraph fails, preserve an exact native counterevent and retype the combinatorial interface; if it succeeds, test whether retaining the multivariate source-use histogram prevents a future observer mismatch that total F(1) would hide.

**Authority boundary:** This is an author-side candidate mathematical result. GitHub PR and local PASS do not confer live Task CLAIM, native checkpoint, independent Driver review, Working Truth/Foundation adoption or any P000 modification.
