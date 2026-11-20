# Stage470-B — Exact full-fiber positive BRC transfer for h=0 (2026-11-06)

Status: AUTHOR_SIDE_EXACT_DP / INDEPENDENT_COMBINATORIAL_CROSSCHECK / UNREVIEWED.

Parent Stage469-B: b91752cfeb32355746453fdec3f945d1a9dc9cc7, with frozen scientific global main bf84bd7c61a2444b59b1da96be57df0e9ae47e53, EM main 2af3fc484eb11060b69e0afc1b562bcaf5ad1419, and P000 Git Blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Current normative policy read separately. This is an independent author-side research unit, not a formal Source Result.

## Domain and exact theorem

Original histories P,Q have fixed first step A=+E1 and subsequent symbols in Sigma={A=+E1,B=+E2,C=+E3}; 2<=m=|P|<n=|Q|. Every original step is a native signed X6 step, and the full initial observer Phi consists of both lengths, signed six-component displacements, all 12x12 ordered adjacent-direction counters separately for P and Q, and K=sum_{i=1}^m [P_i=Q_i]. Each original ordered pair (P,Q) has positive integer BRC mass one. For future equivalence use exactly the Stage469-B labeled future-operation language: POP_P<=1, APPEND_P<=1, POP_Q=0, APPEND_Q<=1; every APPEND uses any of the twelve native signed X6 directions.

Stage469-B identifies the exact future repair in this h=0 case as R=(Q_n,P_{m-1},Q_m,Q_{m+1}) on each fixed Phi fiber. In particular Q_n is computable from the initial directed-edge imbalance; at most 3^3=27 repair classes can occur.

**Theorem 470.1 (constructive exact positive BRC transfer).**
For every feasible fixed full initial observer fiber Phi, the memoized pair-prefix transfer in STAGE470B.py computes all 27-or-fewer positive integer repair populations M(r), the exact support count q_F, and support-lexicographic rank/unrank, without listing original P or Q histories. Its state comprises position, last original P and Q directions, the two residual ordered edge-count vectors (nine coordinates each), and the remaining positional-match target. Its transitions consume one original P/Q edge of the required type (only Q once i>m), and consume a match count when i<=m and current directions agree. At the last position all remaining counters must be zero. The tags P_{m-1},Q_m,Q_{m+1} are emitted during these transitions.

The input observer's three direction-population counters for each original word are exactly reconstructible from first letter A and incoming directed edge counts:
  N_j = [j=A] + sum_i E_{ij}.
The corresponding signed six-component displacement is reconstructed using A=+E1,B=+E2,C=+E3 and zero in axes 4,5,6. Hence on this precise original-history domain the original 25 nonnegative counters (3+3 direction counts, 9+9 directed edges, 1 positional K) reduce to 19 (9+9 edges plus K) without erasing any component of Phi. The last letters are recovered from outdegree-in-degree=[first=A]-[last=j]. This is a source/observer-specific exact redundancy certificate.

**Proof.** Starting at (A,A), every original path realizing Phi has one and only one sequence of choices at each position; each choice consumes exactly one required directed edge per active source. The recursion branches over all such choices and no others. The remaining-match counter makes the terminal criterion equivalent to the original K. Directed-edge exhaustion at the prescribed lengths, the fixed start and the incoming-count identity force the entire signed X6 displacement and 12x12 adjacency fields. Thus every accepted recursion path gives one original history in the complete fiber, and every original history is accepted exactly once. By induction on the number of positions left, summing nonnegative child weights gives the exact number of completions for each repair-tag suffix. At the end the key includes Q_n from edge imbalance and all three emitted tags, so the returned dictionary equals the full repair-class population function. Under the Stage469-B future-equivalence theorem, its positive support is exactly q_F, and sorting a set of at most 27 keys gives exact rank/unrank. This establishes the theorem.

A conservative state-count bound is 9*n*(m+1)*(n+1)^18 = O(n^20) for fixed three-letter Sigma (with overhead for small tag vectors). Each transition performs additions on nonnegative integers of at most O(m+n) bits since the full population is at most 3^(m+n-2). The bound is intentionally conservative; observed state count is recorded below. No full-fiber history enumeration is performed by the large-instance transfer.

## Large unrestricted initial-observer fiber

Choose m=35, n=56 and P=A^35. Fix the complete Q observer by the directed edge counts AA=3, AB=BA=14, AC=CA=12, with every other directed edge zero; first/last Q directions A, six-dimensional displacement determined from the edge counts. Fix K=18. All Q words in this entire Phi fiber consist of k=26 A-X-A excursions, exactly b=14 with X=B and 12 with X=C, plus L=3 AA loops distributed among the 27 available A gaps. This structural statement follows from the absence of BB/CC/BC/CB edges and the balanced AB/BA,AC/CA edge counts. It is not a restricted-subfamily approximation.

The exact original population is 11,154,643,500 and q_F=5. The five repair keys (Q_n,P_{m-1},Q_m,Q_{m+1}) and their integer masses in lexicographic order are:
  (A,A,A,A) : 531,173,500
  (A,A,A,B) : 858,049,500
  (A,A,A,C) : 735,471,000
  (A,A,B,A) : 4,862,280,500
  (A,A,C,A) : 4,167,669,000
They sum exactly to 11,154,643,500. Without conditioning on K, the same fixed P and Q adjacency data give binom(26,14)*binom(29,3)=35,289,235,800 possible Q words.

Independent combinatorial validation enumerates only the 3 identical loop placements among 27 A gaps (binom(29,3)=3,654 candidate allocations), retaining the 1,155 allocations whose first 35 letters have exactly 18 A. At fixed allocation, Q_m,Q_{m+1} are either both A or one is an excursion variable X_i; B/C assignment multiplicity is binom(26,14), binom(25,13), or binom(25,14) respectively. This yields the same five exact masses, without enumerating the binom(26,14) colorings. It is a genuinely independent coefficient-counting check of the large transfer.

## Actual finite verification and provenance

STAGE470B.py and STAGE470B_EXECUTED.json contain the exact runnable Python 3 standard-library implementation and its actual output. The test fully enumerates original ternary initial-observer fibers at (m,n)=(2,3),(3,5),(4,6), compares the memoized BRC transfer's complete mass dictionary to brute-force raw history counts for every fiber, and verifies each supported rank. Totals: 5,866 distinct full initial fibers, 7,317 histories, 7,155 repair-class assertions, and 68,603 cumulative memoized states. All assertions passed.

The large instance used only 2,132 memoized transfer states and matched the independent loop-placement combinatorics exactly. The full future-tree equivalence relation is inherited from the Stage469-B theorem/finite test; this run independently verifies exact population and rank under that relation. Its formal Source Result and independent Driver review remain pending.

## Smallest next unit

Stage471-B: implement deterministic Boolean support and rank for h>0, where Lambda_h includes a growing ordered word; establish a polynomial bound or construct a state-complexity obstruction for the necessary determinization. Independently test P budgets (2 POP,2 APPEND) for new Q probes at positions m-1 through m+2, with all 12 native directions and interleavings. Continue using frozen scientific pins and current normative rules.