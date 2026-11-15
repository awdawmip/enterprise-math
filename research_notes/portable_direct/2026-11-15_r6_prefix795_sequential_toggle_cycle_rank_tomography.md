# PREFIX-795 / R6 — Single-trajectory CRT tomography and the exact unobserved-cycle residual

Date: 2026-11-15 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_INTEGER_REGRESSION / UNREVIEWED / NOT_ADMITTED.
Scientific freeze preserved: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Predecessor: PREFIX-794, project blob ab23f74c27debd74d822782b698170c263d0e7b6, author-attributed earlier to EM-DIRECT-E77192. This new portable note does not claim a current native CLAIM or role capability.

## Question and typed carrier

PREFIX-794 reconstructs a complete 2×b×c joint-source histogram by applying local source-aware toggles in separate experiments reset to the same initial state. Can we reconstruct in **one uninterrupted sequence of physical observation steps**, without resetting, and how many interventions are necessary? This note studies an external positive-integer BRC complete-path count carrier. It does not assert an X6-native legal event.

Fix b,c≥2. Each joint cell e=(i,j) has two nonnegative integer path counts n_(0,e), n_(1,e). Define K_e=n_(0,e)+n_(1,e), x_e=n_(0,e). The pairwise observer L reports:
P_(a,i)=sum_j n_(a,i,j), Q_(a,j)=sum_i n_(a,i,j), R_(i,j)=K_(i,j).
Thus L determines K, all row sums r_i=sum_j x_(i,j), and all column sums s_j=sum_i x_(i,j).
For every chosen named joint cell e, T_e exchanges n_(0,e) and n_(1,e) and leaves all other cells untouched. All T_e are nonnegative-integer bijections preserving every K_e.

Choose a sequence of named cells e_1,...,e_k (repeats allowed). Record y_0=L(n), then y_t=L(T_(e_t)...T_(e_1)n) **after every intervention**. Here t is an ordered experiment event index, not a claim about physical duration.

## Theorem 795.1 — One-run exact sequential coordinate recovery

Let e_t=(i,j), and let p_t be the parity of the number of earlier occurrences of e_t in the sequence. The actual step difference is

    Delta_t = (P_(0,i) at t) - (P_(0,i) at t-1)
            = (Q_(0,j) at t) - (Q_(0,j) at t-1)
            = (-1)^(p_t) (K_e - 2 x_e(initial)).

Consequently the initial joint coordinate is recovered exactly by

    x_e(initial) = [K_e - (-1)^(p_t) Delta_t]/2.

In particular, querying distinct cells once reveals one exact initial x_e each, **without resetting the path histogram between queries**.

Proof. Before its next toggle the currently stored count equals x_e(initial) for even p_t and K_e-x_e(initial) for odd p_t. The swap changes the a=0 count by K_e minus twice the current count, contributing exactly to one P row and one Q column. All other cells stay unchanged. The displayed parity-corrected formula follows. The numerator is even because the counts are integers. QED.

## Theorem 795.2 — Exact cycle-rank of the unrecovered joint residual

Let S be the set of distinct queried cells. Form the undirected bipartite graph G_S with b row vertices, c column vertices and one edge (i,j) for each **unqueried** joint cell. Isolated vertices are included. Put v=b+c, e=|E(G_S)| and let kappa(G_S) denote the total number of connected components.

Over rational linear differences of complete histograms, the unobserved joint-correlation fiber has exact dimension

    mu(G_S) = e - v + kappa(G_S).

The stacked linear observation map (all L readings in the one-run sequence) has exactly bc - mu(G_S) independent rational coordinates in x after K is known. Therefore it determines the complete initial joint histogram for **every** nonnegative integer input iff G_S is a forest.

Proof. Equality of initial L imposes zero row and column sums on a difference d of x. Theorem 795.1 makes equality of the later readings equivalent to d_e=0 for every queried e. Thus the remaining difference is a circulation on the unoriented bipartite incidence graph G_S. Multiplying all column-node incidence equations by -1 turns its row/column constraint matrix into the standard oriented incidence matrix, of rational rank v-kappa(G_S). Its kernel has dimension e-v+kappa(G_S), proving the formula.

If G_S is a forest, the kernel is zero and the initial x is determined. Recover it constructively: subtract measured x_e from r_i,s_j; repeatedly choose a degree-one vertex in the remaining forest, set its only incident edge to that vertex's current residual total, subtract this edge from both endpoint totals, then delete the edge. All values recover as exact nonnegative integers because the original input realizes the equations.

Conversely, if G_S contains a cycle, take the universal witness K_e=2, x_e=1 at every cell. On one alternating simple cycle of unqueried cells, perturb x by alternating +1 and -1; keep all other coordinates equal to 1. The two histograms remain nonnegative integral (counts 0,1,2), have equal initial row/column totals and equal K, and coincide at every queried coordinate. They therefore generate identical entire sequential observations but differ as joint histograms. This proves the universal iff statement, not merely a real-linear obstruction. QED.

## Corollary 795.3 — Sharp minimum number of interventions, even with adaptive cell selection

For all b,c≥2 the minimum worst-case number of local cell toggles needed to identify every integer 2×b×c histogram from initial and after-each-step pairwise readings is

    d = bc-(b+c-1) = (b-1)(c-1).

The bound applies to every deterministic adaptive protocol whose next queried cell is chosen from the previously observed pairwise readings and that must identify every such histogram.

Proof. Fewer than d interventions query fewer than d distinct edges, leaving more than b+c-1 edges in G_S. That graph necessarily contains a cycle. For a predetermined sequence, the indistinguishable pair of Theorem 795.2 proves failure. For an adaptive protocol, run it on the uniform witness K=2, x=1, and record its selected edges. Construct the alternate histogram on an unqueried cycle. By induction both inputs have identical initial and subsequent observed readings; the deterministic adaptive protocol therefore makes the same queries and cannot distinguish the inputs.

For attainment, query each e=(i,j) with 0≤i<b-1 and 0≤j<c-1 exactly once in any order. The unqueried cells lie in the last row or last column, forming a connected bipartite tree on all b+c vertices. Recover queried entries by Theorem 795.1 and all other entries by leaf elimination in Theorem 795.2. Exactly d toggles suffice in one sequential trajectory. QED.

An arbitrary selection S is sufficient iff the complement is acyclic; it need not equal the particular top-left grid. This permits experiment design respecting which typed joint-cell interventions are available.

## Exact verification and complexity scope

Reproducible checker: research_notes/portable_direct/PREFIX795_R6_SEQUENTIAL_TOGGLE_CYCLE_RANK_CHECK.js (Node.js standard library only).
Result: research_notes/portable_direct/PREFIX795_R6_SEQUENTIAL_TOGGLE_CYCLE_RANK_RESULTS.json.

The checker exhaustively compares the graph cycle rank to the augmented observation rank for every selected-edge subset of 2×2, 2×3, 3×3, and 3×4 grids (4,688 subsets), and 256 deterministic 4×4 subsets. Its GF(2) elimination is an exact check of rational rank here: the row/column incidence matrix, after bipartite row sign changes, is totally unimodular, and adding coordinate-unit rows preserves total unimodularity by minor expansion; hence all nonzero square minors are ±1 and preserve rank modulo 2. The checker also reconstructs every initial x∈{0,1,2}^(2×3) and x∈{0,1,2}^(3×3) using one evolving sequence (20,412 histogram states total), and tests 300 exact cycle-indistinguishability witnesses on 3×4 grids. It counts 495,900 exact assertions. The universal theorems rest on the proofs above; the tests validate finite implementations.

Given K, initial row/column totals and each local Delta as an accessible scalar, leaf recovery uses O(bc+|S|) arithmetic with suitable adjacency bookkeeping and O(bc) space; collecting full pairwise snapshots adds their readout cost. No bit-complexity speedup is asserted for general integer encodings.

## BRC meaning and unresolved native correspondence

The model preserves complete-path multiplicity, a=0/1 signed *type labels* (not signed amplitudes), pairwise CRT channels and the ordered sequence of local source interventions. The cycle residual is a concrete joint-relational BRC degree of freedom. It is not inferred redundant from prime-factor residue channels alone.

Under P000/ACTIVE, the underlying world is six-dimensional native X6 plus separately typed event time, with triadic primitive balance and full Cell/Link/Port provenance. Synthetic T_e is **not** yet an admitted native X6 operation. Next verify which native time-ordered Cell/Link/Port transitions, if any, realize the needed named-cell exchange without changing other observations; if not, formulate the exact native transition matrix, compute the corresponding observation-cycle rank and minimum sufficient residual for its real admissible event horizon. Compare time-series probes with independent-reset probes under an explicitly typed operational cost model.

Attribution: this note independently extends the already published PREFIX-794 scalar model. Prior historical Researcher-ID EM-DIRECT-E77192 and RA-66BBE259AEE1AD543D9454A3 identify earlier work only. Current native owner/CLAIM is checked independently and this material is a new non-overwriting portable science artifact, not a formal Task RESULT/REVIEW.
