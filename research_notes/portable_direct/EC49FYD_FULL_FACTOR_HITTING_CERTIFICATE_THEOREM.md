# EC49FYD — Full-factor Farey–CRT certificate = 11 + strict-supermask transversal number

Date: 2026-11-23. Frozen scientific pin: \`BRC16943\`.
Parents: EC49FYC @ \`41ec11bb67668ba560c9e22948330451699b2ef3\` and EC49FYA @ \`19a04cf3410c979ceb6502eae1fdbaba84ec5b68\`.
Mode: informed independent portable research; no native CLAIM or mathematical Review. Status: **AUTHOR_PROVED / EXACT_EXHAUSTIVE_FINITE_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED**.

## Exact problem and definition
Let \(\mathcal F\) be the frozen collection of 50 nonzero ten-bit P10 masks. The 600 normalized states are \((U,z)\), where \(U\in\mathcal F\) and \(z=-1,0,\ldots,10\). An indexed physical read is

\[
W_{(U,z)}(t,j)=\mathbf1_{t\in U}\mathbf1_{z\ne j},\quad 0\le t<10,\quad0\le j<11.
\]

Here \(z=-1\) means the full factor (no missing column). A target-state certificate is a nonadaptive set of physical sites whose readout vector for the *known* target is different from each of the other 599 states. Let \(C(U,-1)\) be its minimum cardinality; this is not the worst-case depth of an adaptive decision tree.

For a fixed support mask \(U\), construct the strict-upper-set difference hypergraph

\[
\mathcal E_U=\{\,V\setminus U:V\in\mathcal F,\ U\subsetneq V\,\}.
\]

Define \(\tau(U)\) to be the minimum size of a row set \(T\subseteq\{0,\ldots,9\}\setminus U\) meeting every edge of \(\mathcal E_U\), with \(\tau=0\) if \(\mathcal E_U\) is empty.

## General theorem and proof
**Theorem.** Let \(\mathcal F\) be *any* finite family of nonempty subsets of an \(n\)-row universe, and form full and one-hole states with \(m\ge n\) physical columns under the same Boolean product readout. For every \(U\in\mathcal F\),

\[
\boxed{C(U,-1)=m+\tau(U)}.
\]

**Lower bound.** For each column \(j\), the target \((U,-1)\) differs from the state \((U,j)\) only at *positive* sites in column \(j\). Thus a valid certificate contains at least one positive query in each of the \(m\) columns. Against every strict-full-supermask rival \((V,-1)\) with \(U\subsetneq V\), only a negative query in a row of \(V\setminus U\) distinguishes the target. These negative rows must hit all hyperedges and require at least \(\tau(U)\) distinct sites. Positive and negative sites cannot coincide, proving \(C(U,-1)\ge m+\tau(U)\).

**Upper bound.** Select exactly one positive query per column, with the selected rows together covering *every row in \(U\)*. This is possible because \(m\ge n\ge|U|\). Add \(\tau(U)\) negative queries, one in each row of a minimum hitting set, in any physical column. For every rival \((V,z)\):
- if \(U\not\subseteq V\), choose a selected positive row in \(U\setminus V\);
- if \(U\subseteq V\) and \(z\ne-1\), the positive site in the omitted column \(z\) has target value 1 and rival value 0;
- if \(U\subsetneq V\) and \(z=-1\), a chosen negative row in \(V\setminus U\) separates the states.
These cases exhaust all rivals. The \((U,-1)\) state itself is excluded. Hence \(C(U,-1)\le m+\tau(U)\), completing the proof.

**Rigidity of equality.** Every minimum certificate has exactly one positive site per column and exactly \(\tau(U)\) negative sites at distinct rows forming a minimum transversal; in addition, its selected positive rows must separate all masks missing some support of \(U\). The existence of such a certificate is established by the construction above.

## Exact frozen P10/C11 classification
For the frozen 50-mask family, set \(m=11\). Exhaustively enumerate \(r=0,\ldots,1023\) and test \((r\ \&\ (V\setminus U))\ne0\) for every strict supermask. This is exhaustive because a transversal is a subset of the ten rows. Results:

| \(\tau(U)\) | \(C(U,-1)\) | Count | Masks |
|---:|---:|---:|---|
| 0 | 11 | 22 | 123,243,245,346,367,371,447,486,491,567,599,602,615,701,718,753,828,857,867,949,980,1005 |
| 1 | 12 | 17 | 86,91,157,175,203,211,287,327,410,412,457,460,646,697,721,789,965 |
| 2 | 13 | 8 | 23,281,299,301,389,394,613,673 |
| 3 | 14 | 3 | **101,788,833** |

For each of the three hardest full-factor states, the complete lists of minimum negative-row transversals have respectively **6, 4, 8** members. They are emitted in the JSON evidence. The mask 788 has support rows \(\{2,4,8,9\}\), and all four minimum transversals require row 0, one of \(\{3,5\}\), and one of \(\{6,7\}\). Hence a length-14 target certificate for \((788,-1)\) cannot query row 1, independently recovering EC49FYC's path restriction from a general exact characterization.

## Computation and limits
The accompanying standalone JavaScript reconstructs all 72 primitive representatives and 50 masks using the frozen P10 formula, forms all 600 states, enumerates all 1024 row subsets for every \(U\), outputs explicit minimum transversals and a constructed minimal 11+\(\tau\) certificate for every full state, and verifies the readout distinction against each of the other 599 states (**29,950 exact pair checks**). All checks use integers and Boolean logic; there is no rounding. The published JSON is generated by the same source and is independently consistent with an exploratory Python integer-MILP comparison. The mathematical proof above does not depend on solver optimality.

**Scope.** This classifies the **50 full-factor target-state certificates**. It does not classify the 550 one-hole target certificates or settle the global adaptive tree optimum \(Q\in\{14,15\}\). The all-600 genuine-anchor realizability is inherited from pinned EC49FXU; this remains an auxiliary normalized Farey–CRT observer claim, without native X6 dynamics transfer.

**Next open problem.** Exploit the exact minimum certificates and their 6/4/8 hypergraph-transversal patterns to impose branch-and-bound restrictions on all ten possible root rows. Seek a depth-14 tree or a finite exhaustive obstruction over all root classes, preserving column-translation symmetry and allowing different queries on different branches.
