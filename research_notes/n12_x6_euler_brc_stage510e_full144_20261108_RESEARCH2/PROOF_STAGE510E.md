# Stage510-E — Exact Euler–BRC rank/unrank with all 144 native ordered relations active

Date: 2026-11-08 (Asia/Shanghai).
Status: independently written mathematical argument and author-side exact integer execution; independent Driver review / formal native Source acceptance pending.

## Source and target

This independent unit directly addresses the long-open 12-direction/144-ordered-relation Euler–BRC *random-access ranking*, distinct from Euler-trail enumeration. The current X6 native alphabet has exactly 12 **signed directions** \(\{\pm E_1,\ldots,\pm E_6\}\), not 12 axes; all remain within six native spatial coordinates and are merely names for combinatorial steps. A directed adjacent-pair inventory \(m=(m_{ij})_{0\le i,j<12}\) has nonnegative **integer** multiplicities. The resulting BRC observer keeps all 144 ordered pair coordinates, including loops, not a support-only or total-only projection. Word \(w_0,\ldots,w_N\) has a designated start \(s\), end \(t\) and exactly \(m_{ij}\) occurrences of adjacency \(i\to j\). Identical parallel edges are indistinguishable in the word. This is a static native-X6 combinatorial word model, not a physical heartbeat or a new equation of motion.

Inherited frozen scientific pins: Global Knowledge \`bf84bd7c61a2444b59b1da96be57df0e9ae47e53\`; Enterprise Math \`2af3fc484eb11060b69e0afc1b562bcaf5ad1419\`; P000 immutable blob \`bcc2590d3168a28f72e8b9f0f9b1f76faadcd488\`. Current behavioural method and P000 were independently read at the current main snapshot. Related source Stage509-B \`94f52374ed15a2a8cb41a7bf8b5aca163e8c1370\`; Stage510-B in sibling research folder.

## Theorem 510-E.1 — Exact number of Euler words with repeated heterogeneous directed relations

Let \(n_{ij}=m_{ij}\), \(d_i^+=\sum_jm_{ij}\), \(d_i^-=\sum_jm_{ji}\). Let \(N=\sum m_{ij}\), and let \(V\) be vertices of positive total incidence. If \(N=0\), the number of words is 1 for \(s=t\) and 0 otherwise. For \(N>0\), if \(s,t\notin V\), or some balance constraint
\[
d_i^+-d_i^- = [i=s]-[i=t]
\]
fails, the count is zero. Otherwise let \(\tau_t(m)\) be the weighted directed-in-arborescence count rooted at \(t\), computed as the determinant of the directed out-degree Laplacian's minor after deleting root \(t\). For all \(i\in V\), form \(L_{ii}=\sum_{j\in V,j\ne i}m_{ij}\), \(L_{ij}=-m_{ij}\) for \(j\ne i\); **loops are omitted only from the tree Laplacian, not from degree/factorial inventories**. Then:
\[
\boxed{C(m;s,t)=\frac{\tau_t(m)\prod_{i\in V}\left(d_i^+-1+[i=t]\right)!}{\prod_{i,j}m_{ij}!}.}
\]
The formula is exact for directed multigraphs with loops and parallel edges; \(\tau_t=0\) covers disconnected/non-Euler inventories. It counts *vertex-direction words*, not labeled edge permutations. All divisions are exact integers on valid inputs.

**Proof.** First distinguish every individual edge occurrence, including every parallel copy. For a fixed end \(t\), choose the last outgoing edge for each active vertex other than \(t\). In every valid Euler traversal these chosen edges constitute an in-arborescence toward \(t\); otherwise a last-exit directed cycle prevents completion. Conversely an in-arborescence and an independent ordering of other outgoing edges at each vertex (all \(d_i^+-1\) non-tree exits for \(i\ne t\) and all \(d_t^+\) exits for \(t\)) generate one edge-labeled Euler trail by following each vertex's next unused exit. There are \(\tau_t\prod_i(d_i^+-1+[i=t])!\) such labeled trails. For each resulting *vertex word*, permuting the labels of its \(m_{ij}\) identical \(i\to j\) edge occurrences yields exactly \(\prod_{ij}m_{ij}!\) labeled trails, independent of the word. Dividing gives the asserted formula. Exact \(\tau_t\) follows from the directed matrix-tree determinant. QED.

## Theorem 510-E.2 — Exact lexicographic rank and unrank

Order the 12 signed native direction symbols as indices \(0,\ldots,11\); declare this index order, not an external spatial orientation. At each current symbol \(v\), any next symbol \(j\) with \(m_{vj}>0\) defines a branch: consume one copy \(m_{vj}\gets m_{vj}-1\) and its exact count of suffix completions is \(C(m';j,t)\). These branches partition the word set disjointly by its next symbol.

Therefore:
- **rank**: along an existing Euler word, sum all completion counts for smaller candidate next symbols \(j\) before taking the observed symbol.
- **unrank**: for an integer \(r\) with \(0\le r<C(m;s,t)\), scan the next symbols in order; subtract each rejected branch count until choosing the first branch containing \(r\).
- continue until the inventory is exhausted; the chosen endpoint must equal \(t\).

Induction on remaining edge count proves rank/unrank are mutually inverse and cover precisely the integer interval \([0,C)\); no enumeration of all Euler words is required. The same inventory, start/end and lex ordering are used for both directions, so these are **random access** operators.

## Exact executed experiment — full 144-active heterogeneous inventory

The bundled executable \`EULER_BRC_RANK.py\` uses Python standard-library arbitrary-precision integers, exact Bareiss determinants, factorial quotients, a count-cache, actual lex rank/unrank loops, and an independent tiny-instance brute enumerator. Set
\[
m_{ij}=1+\big((ij+i+j)\bmod 3\big),\quad 0\le i,j<12,\quad s=t=0.
\]
This **fully specified** 12×12 matrix is symmetric and connected, has all 144 directed relation types active, and contains 32 entries of multiplicity 1, 32 of multiplicity 2 and 80 of multiplicity 3, totaling \(N=336\) relation edges, hence length-337 direction words. No symmetry/regularity assumption is imposed on the *general* theorem; the chosen benchmark is heterogeneous (entries vary), balanced and strongly connected.

The exact total is 943 bits (284 decimal digits):
\`\`\`text
53271093223387672856479764664324348051167466104686151416103605397498437808338783727599072854714814222355611853137594447151673274798895696918964596339896902595060121189987309218284251010655677266875465822865172764095938560000000000000000000000000000000000000000000000000000000000
\`\`\`

Executed checks: **4,838** independent exhaustive small-matrix/start-end comparisons of matrix-tree formula against edge-consuming recursion; for the 336-edge graph, first and final lex words, the middle exact rank, and a reproducible 940-bit random rank all satisfy \`rank(unrank(r))=r\` and a generated word satisfies \`unrank(rank(w))=w\`. All assertions passed. Full actual machine output is \`EULER_BRC_EXECUTED.json\`, which includes random rank, random word SHA256, timings, cached states and memory. One Python-process observation: cold random rank about 0.1247 seconds; cold random unrank about 0.1618 seconds; peak \`ru_maxrss\` 103576 KiB (process-wide, not algorithm-only). These are sample timings in the actual run, not a comparison to a different algorithm.

**Bit-cost accounting:** the input has 144 integer multiplicities and a total of 336 directed relations; \`C\`, candidate ranks and factorial/determinant intermediates are large integers, with at least 943-bit final counts. A call to \(C\) uses a directed 11×11 matrix-tree minor and big-integer Bareiss elimination, factorial products/division, and the full 144-integer inventory. A full rank or unrank traverses 336 edges and up to 12 candidate branches per step, with cache reuse. The source \`EULER_BRC_RANK.py\` is the actual measured implementation and supplies an operational cost baseline, not a proven asymptotic speedup. A complete same-input comparison with alternative exact rankers and resource bounds remains open.

## Applied BRC interface and proof status

BRC carrier: 12-symbol native-X6 ordered-direction adjacency inventory, retaining **all 144 directed multiplicity coordinates**. Serial composition of direction words uses the complete joint edge accounting; the Euler rank/unrank operators invert the path-to-inventory fiber for a chosen \(s,t\), via exact integer arborescence counts. Source identities for individual parallel edge copies are quotient-safe only because the declared observer and future language concern *direction words* and exact counts; if an application later needs separately labeled edge provenance, the fiber would need enrichment.

This stage provides a self-contained combinatorial theorem and exact finite execution evidence. The theorem is an author-side proof and awaits independent Driver review. It does not change P000, project promotion state, native runtime authority or physical dynamics.

## Next

Compare against a second independently implemented exact rank/unrank algorithm **on the identical 144-active heterogeneous inventory**, including initialization, representation and preprocessing, bigint operations, output recovery, wall-clock and peak RSS. Test nonsymmetric balanced / open Euler inventory families and confirm matrix-tree/root boundary cases. Continue Stage511-B exact direct-touch-mask synthesis and gap-local public-rank quotient as a separate line.
