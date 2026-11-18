# R5 — exact minimal future quotient for one named availability control

Date: 2026-11-15.
Frozen scientific input: \`435e77af0d180eac32bd1f9c4c464bc4010b7551\`.
Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Scope: the inherited cyclic-triangle **auxiliary** indexed-center radius-two observer, with \(\kappa_a=5k+q(u)\), \(q(u)=\sum_{i\bmod k}u_i u_{i+1}\); binary indices are not native X6 coordinates. This result restricts the **future operation alphabet**, rather than changing the frozen scientific input.

## Exact observer

Fix k≥3 and one named index j. Let the only permissible future operations be \(\operatorname{Set}_j(0)\) and \(\operatorname{Set}_j(1)\), setting u_j to the specified bit without changing any other coordinate. Let two masks be future-equivalent exactly when the current q, and q after **every finite word** of these two operations, agree. Distinct finite command words remain named and ordered.

Removing the two edges incident with j leaves a path on n=k−1 vertices. Write

\[
c(u)=\sum_{(i,i+1)\text{ not incident to }j}u_i u_{i+1},
\qquad t(u)=u_{j-1}+u_{j+1},
\qquad q_0=q(u)=c+u_jt.
\]

**Theorem.** The triple \((c,t,q_0)\) is a necessary and sufficient future-observer state. The exact number \(\mathcal N_k\) of equivalence classes is

\[
\boxed{\mathcal N_3=5,\qquad \mathcal N_k=5k-11\quad(k\ge4).}
\]

Thus a single controlled location admits only linearly many future-observation classes, whereas all k named Set locations require all \(2^k\) states once a horizon of two commands is allowed, by \`BRANCHING_CACTUS_AND_TWO_STEP_RESIDUAL_THEOREMS.md\` at this same R5 research frontier.

## Proof of sufficiency, necessity and the exact count

Every future operation sequence either is empty, in which case the observer returns \(q_0\), or ends with a known Set_j(b), in which case the observer returns \(c+bt\). Therefore the triple determines every finite readout sequence. Conversely, empty, Set_j(0) and Set_j(1) respectively reveal \(q_0,c,c+t\), so any future-equivalent masks must have exactly the same triple. This proves that the triple is the **minimal equivalence relation** for the stated observer and operation alphabet.

To count its attainable values, fix the path of n=k−1 remaining vertices and classify the endpoint sum \(t=u_{j-1}+u_{j+1}\).

If n≥3:

* t=0: both endpoints are 0. The possible numbers of adjacent 11 edges are exactly \(c=0,\ldots,n-3\), totaling n−2 possibilities; q_0=c, regardless of u_j.
* t=1: one endpoint is 1 and the other 0. The possible c are exactly \(0,\ldots,n-2\), totaling n−1 possibilities. Each allows both \(q_0=c\) and \(q_0=c+1\), depending on u_j.
* t=2: both endpoints are 1. If some interior vertex is 0 then at least two path edges are broken, so \(0\le c\le n-3\); all these values occur by placing a prefix of c+1 ones at one endpoint, one or more zeros, and a 1 at the other endpoint. If every path vertex is 1, \(c=n-1\). Hence this case has exactly n−1 possible c values, each giving the two values \(q_0=c\) and \(q_0=c+2\).

In the t=0 case, all c between 0 and n−3 occur using an interior run of c+1 ones (or the all-zero word for c=0); in the t=1 case, a prefix of c+1 ones works. There are thus

\[
(n-2)+2(n-1)+2(n-1)=5n-6=5k-11
\]

different future classes. Their triples differ by the labeled t or by c/q_0, so there is no overcounting.

For k=3, the remaining path has n=2 adjacent vertices. The feasible (t,c) pairs are exactly (0,0), (1,0), (2,1), giving respectively 1, 2 and 2 q_0 values: five classes. QED.

## Provenance and validation

This is a **readout quotient**. Returning source-labeled old libraries may require retaining further availability identities; no claim of source-witness factorization is made by this theorem.

The stored \`VERIFY_R5_ONE_VERTEX_OBSERVER.py\` exhaustively evaluates all \(2^k\) binary masks for k=3..14, computes every current/one-command observer triple, checks the formula and the range of t, and prints the exact per-k class counts. Local result: \`PASS_R5_ONE_VERTEX_FUTURE_QUOTIENT\`; full enumerated lengths and counts are preserved in \`EXACT_R5_ONE_VERTEX_OBSERVER.json\`. This finite check supplements the universal argument.

Next: extend the equivalence to an arbitrary fixed set J of controlled named vertices; identify the necessary edge-boundary coefficient residual, and measure when source-aware witness reconstruction forces a strictly finer quotient than future cardinality alone.
