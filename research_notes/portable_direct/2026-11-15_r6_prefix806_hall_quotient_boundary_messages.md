# PREFIX-806 — Exact Hall-filtered observer-sufficient boundary messages

Date: 2026-11-15 (Asia/Shanghai). Enterprise Math / BRC auxiliary named-source integer model. Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Continues PREFIX-805. Historical Researcher-ID `EM-DIRECT-4660FF`, Activity `RA-63E1066C3056A93898BE8E18`.

Status: AUTHOR_PROVED / EXACT FINITE REGRESSION / NOT INDEPENDENTLY REVIEWED.

## Scope and question

Take a finite bipartite graph G with named source edges e, integer capacities K_e >= 0, nonnegative integer row and column demands d_v and signed integer additive observer weights w_e in Z^q. A table x is legal if 0<=x_e<=K_e and each vertex demand equals the sum of its incident named edge counts. Partition vertices into components A and B after removing a named crossing edge set X.

PREFIX-805 groups crossing assignments t by their residual vertex-demand vectors rho_A,rho_B and crossing observer exponent omega. The present question is whether *entire infeasible signature classes* can be removed before computing any internal observer histogram, with an exact finite certificate and no change in the final Laurent histogram.

## Theorem 806.1 — Local Hall certificate commutes with observer-sufficient quotient

For C=A or B, let R_i^C,S_j^C be the residual demands and K_ij^C the internal-edge capacities. The component admits an integer completion if and only if

(1) all its residual demands are nonnegative;
(2) sum_i R_i^C = sum_j S_j^C; and
(3) for every subset I of its row vertices,

    sum_(i in I) R_i^C <= sum_j min(S_j^C, sum_(i in I) K_ij^C).

Let s=(rho_A,rho_B,omega) be the PREFIX-805 observer-sufficient signature and m_s the number of distinct named crossing assignments having s. Write f_C(rho_C) for the preceding finite Hall predicate. Then

    H_G(d;z) = sum_(s: f_A(rho_A,s) & f_B(rho_B,s))
                  m_s z^(omega_s) H_A(rho_A,s;z) H_B(rho_B,s;z).

This is an exact identity in Z[z_1^+-1,z_1^-1,...,z_q^+-1,z_q^-1] (multivariate Laurent notation). The Hall checks may be cached *once per signature*, even if multiple distinct crossing assignments induce the same signature.

**Proof.** In each component construct the finite flow network source -> rows with edge capacities R_i^C, rows -> columns with capacities K_ij^C, and columns -> sink with capacities S_j^C. Total demand balance is necessary. For any row set I, min cut requires sum_(i in I) R_i^C <= sum_j min(S_j^C,sum_(i in I)K_ij^C); conversely, all such inequalities ensure an s-t flow of value sum_i R_i^C by max-flow/min-cut. Integral capacities admit an integer maximum flow, hence a legal component table. The joint source table decomposes uniquely into its crossing allocation and its two legal component tables, as in PREFIX-804/805. Component feasibility depends only on its residual demands, which are included in s. Consequently, all allocations sharing s either have zero valid completions or have the same two component histograms; discard exactly the zero classes, retain multiplicity m_s for every surviving class. Integer Laurent coefficients and signed exponents are preserved. QED.

## Corollary 806.2 — Exact reuse and work bound

For fixed internal capacities, one Hall decision per distinct residual-demand pair suffices; quotienting before evaluation never increases the number of internal histogram messages relative to evaluating every signature without the Hall filter. Let M be the number of distinct signatures and a,b the numbers of row vertices in the two internal components. A direct subset implementation requires O(M (2^a a c_A + 2^b b c_B)) integer operations for checking the necessary and sufficient Hall conditions, in addition to crossing enumeration and histogram evaluation. This is an observer-relative complexity bound, not an overall running-time improvement guarantee. Infeasible signatures incur no internal histogram evaluation.

The signature is sufficient only for the *declared* additive observers. Adding a new named-edge observer may split old classes, precisely as PREFIX-805 demonstrated.

## Checker and verified finite scope

The self-contained Node/JavaScript checker implements:
1. Independent direct enumeration of every legal full named table and its exact signed two-observer Laurent histogram.
2. Separator allocation with exact single-crossing-variable elimination from cut conservation and signature grouping.
3. The same separator computation with full integer Hall feasibility for both internal components before their histogram messages.

It executes the exhaustive 2x2 capacities in {0,1,2} and 2x3 capacities in {0,1}, **every achievable row/column margin** for each capacity vector; it then checks three fully specified 4x4 witnesses. All counts and coefficients are exact safe integers on the declared finite test range.

Results: **145** capacity patterns, **1919** margin fibers, **2025** counted full named table occurrences and **5769** exact assertions. Result: `ALL_EXACT_CHECKS_PASS`.

Across the exhaustive finite families, the unfiltered separator performed 4871 component-histogram computations and 2025 nonzero coefficient products; Hall-filtered separator performed 4041 component computations and 2025 coefficient products, with 444 rejected crossing allocations.

For 4x4 named-crossing witness: 16 legal named tables and 4 signed two-observer outcomes; 6 unfiltered component computations versus 6 filtered computations, 0 rejected crossing allocations. Full coefficient evidence appears in the JSON.

For 4x4 dense unit: 90 legal named tables and 9 signed two-observer outcomes; 38 unfiltered component computations versus 30 filtered computations, 8 rejected crossing allocations. Full coefficient evidence appears in the JSON.

For 4x4 stressed boundary: 18 legal named tables and 5 signed two-observer outcomes; 11 unfiltered component computations versus 11 filtered computations, 0 rejected crossing allocations. Full coefficient evidence appears in the JSON.

The implementation intentionally does not claim a wall-clock improvement; Hall tests have their own cost. Its exact pruning counters and independent histogram agreement measure the proved change. Larger-graph performance remains open.

## Position and next problem

PREFIX-805 introduced observer-sufficient signatures; PREFIX-806 proves a complete finite feasibility predicate on those signatures and certifies exact zero-message pruning. It reuses the integer-capacity Hall machinery of PREFIX-800/801 while retaining the provenance and signed observers of PREFIX-804/805. These are auxiliary source-flow theorems, not native X6 event-time theorems.

Next: cache Hall signatures and component suffix messages incrementally when neighboring crossing assignments differ at one edge; evaluate complete time, peak memory and observer-support growth against the unfiltered and memoized suffix baselines on explicit larger sparse/dense models. Separately establish a typed, operations-preserving native Cell/Link/Port/event-time readout before interpreting these results as X6 dynamics.

No shared CLAIM, Result, Review, P000 alteration or new authority is asserted.
