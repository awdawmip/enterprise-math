# EC49FYE — Exact one-hole target certificates by a two-multicover integer theorem

Date: 2026-11-23. Frozen scientific input: **BRC16943**.
Parent: EC49FYD, immutable scientific source \`7454e769679058baf19b5c922ae0543fa5407076:research_notes/portable_direct/EC49FYD_FULL_FACTOR_HITTING_CERTIFICATE_THEOREM.md\`.
Mode: informed independent portable research. Status: **AUTHOR_PROVED / EXACT_EXHAUSTIVE_INTEGER_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED**.
Author lineage: Research 4 / prior activity \`RA-0F8055ACDE0F5F6A97CA5D6D\`, previous historical researcher \`EM-DIRECT-48E619\`; this file creates no native CLAIM or review.

## Problem

Fix a family \(\mathcal F\) of nonempty subsets of \(R=\{0,\ldots,n-1\}\), with \(m\ge n+1\) columns \(J\).
For \(U\in\mathcal F\) and \(z\in \{-1\}\cup J\), define the Boolean product state
\[
 W_{U,z}(t,j)=\mathbf1_{t\in U}\mathbf1_{z\ne j}.
\]
Here \(z=-1\) denotes a complete factor; \(z=h\in J\) denotes one missing column.
The target-state certificate cost \(C(U,h)\) is the minimum number of **fixed physical positions** whose response vector uniquely identifies this *known target* against all other \((V,z)\). This is not the minimax depth of a single adaptive decision tree.

## Two-multicover theorem (arbitrary row family)

For any \(U\in\mathcal F\) and missing column \(h\), introduce \(a_t\in\{0,1\}\) and \(x_t\in\{0,1,2\}\) for each row \(t\in R\). Define \(D(U,V)=U\triangle V\). Then the exact certificate cost is
\[
\boxed{
C(U,h)=\min\Big\{\sum_{t\in R}(a_t+x_t):
 \sum_{t\in U}a_t\ge1,\;
 \sum_{t\in D(U,V)}x_t\ge1,\;
 \sum_{t\in D(U,V)}x_t+\sum_{t\in V}a_t\ge2
 \quad\forall V\in\mathcal F\setminus\{U\}
\Big\}.}
\]
It is independent of the hole index \(h\).

**Necessity.** For a certificate \(S\), let \(a_t=1\) if \(S\) reads \((t,h)\); let \(x_t\) be the number of distinct non-hole columns read in row \(t\), truncated at two. Rival \((U,-1)\) requires a reading \((t,h)\) with \(t\in U\).
For \(V\ne U\), rival \((V,h)\) differs only on the outer-column rows \(D(U,V)\); hence \(\sum_D x\ge1\).
If no \(h\)-column read lies in \(V\), i.e. \(\sum_V a=0\), then every outer-column hole rival \((V,k)\), \(k\ne h\), must be excluded: at least two distinct outer columns of the difference rows must be read, forcing \(\sum_Dx\ge2\). Thus \(\sum_Dx+\sum_Va\ge2\) whether the latter sum is zero or positive. The objective does not exceed the number of physical reads in \(S\), establishing the lower bound.

**Sufficiency (constructive).** Choose \(A=\{t:a_t=1\}\), read \((t,h)\) for every \(t\in A\). For each row with \(x_t\ge1\), read one outer position whose column is unique to that row; because there are \(m-1\ge n\) outer columns, assign them injectively. If \(x_t=2\), additionally read a *different* outer column in the same row (its choice may coincide with another row's first column). This uses precisely \(\sum(a+x)\) distinct physical positions.

The missing-column target \((U,h)\) is separated from each rival:
- If the rival mask is \(U\) and its factor is complete or misses another column, a target-zero read in \(A\cap U\) at column \(h\) separates them.
- If the rival is \((V,h)\), the first inequality for \(D(U,V)\) supplies a separating outer read.
- For \(V\ne U\) and rival \((V,k)\), \(k\ne h\), or \((V,-1)\), if \(A\cap V\ne\varnothing\), a read at column \(h\) separates them. Otherwise \(\sum_Dx\ge2\): either two different rows contribute (their assigned first columns are different) or one row contributes twice (its two columns are different). The rival can erase only one outer column. A separating difference read survives.

Thus these integer constraints are necessary and sufficient. In particular the argument justifies the two-multicover integer reduction without a floating-point optimizer.

## Exhaustive frozen P10/C11 census

Use exactly 10 rows, 11 columns and the 50 frozen P10 supports generated from 72 primitive representatives. Column translation makes every missing-column index equivalent, so compute the representative \(h=0\) for each \(U\).

| Exact minimum \(C(U,h)\) | Number of supports \(U\) | Supports |
|---:|---:|---|
| 5 | 13 | 86, 175, 394, 460, 486, 602, 646, 673, 753, 788, 828, 833, 867 |
| 6 | 34 | 23, 101, 123, 157, 203, 211, 243, 245, 281, 287, 299, 301, 327, 346, 367, 371, 389, 410, 412, 447, 457, 491, 567, 599, 613, 615, 697, 718, 721, 789, 857, 949, 980, 1005 |
| 7 | 3 | **91, 701, 965** |

Consequently **all 550 one-hole states** have minimum target-certificate costs 5, 6 or 7, in counts \(143,374,33\). Combining with EC49FYD's 50 full-factor states yields the **complete 600-state target-certificate census**:
\[
\begin{array}{c|rrrrrrr}
\text{cost}&5&6&7&11&12&13&14\\\hline
\text{states}&143&374&33&22&17&8&3
\end{array}
\]
Hence \(\max_s C(s)=14\) is attained **only** at the three full-factor targets \(U=101,788,833\). A known one-hole target requires at most seven reads.

## Exhaustive integer certificate and reproduction

The companion \`EC49FYE_ONE_HOLE_CERTIFICATE_VERIFY.js\` reconstructs the 72 primitive directions and exact 50 P10 masks from the pinned P10 predicate; enumerates **every** ten-row pair of decisions \((a_t,x_t)\) with \(a_t\in\{0,1\}\), \(x_t\in\{0,1,2\}\), objective \(\le7\); tests the exact two-multicover constraints for each support; constructs the matching physical observation positions; and directly compares each representative target with its other 599 states.

There are exactly **351,240** cost-bounded candidate assignments. Every support has a feasible assignment of cost at most 7, so exhaustive comparison over all assignments with cost at most 7 proves the exact minima—no assignment of cost greater than 7 can improve an exhibited minimum. The checker independently performs **29,950** target-versus-rival Boolean readout comparisons, all passing. Arithmetic consists of integer bit operations. Run: \`node EC49FYE_ONE_HOLE_CERTIFICATE_VERIFY.js > EC49FYE_ONE_HOLE_CERTIFICATE_OUTPUT.json\`.

This is an auxiliary normalized Farey–CRT observer claim. Genuine anchor realizability is inherited from the pinned EC49FXU source. The theorem does not assert transfer to native X6 time dynamics.

## Remaining question

The global single-decision-tree optimum under the same frozen no-free-spectrum observer remains \(Q_{\mathrm{adaptive}}\in\{14,15\}\). This full **target-certificate** census narrows potential 14-depth bottlenecks to three complete-factor states, although coordinating a single decision tree may still create additional constraints. Next: use exact branch-specific residual candidate sets to decide whether a uniform depth-14 tree exists, retaining the three hard-state certificate hypergraphs and column-translation symmetry.
