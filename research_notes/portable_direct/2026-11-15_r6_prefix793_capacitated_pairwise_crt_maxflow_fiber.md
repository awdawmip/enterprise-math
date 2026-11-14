# PREFIX-793 / R6 — Capacitated max-flow theorem for the 2 × b × c joint CRT fiber

Date: 2026-11-15 (Asia/Shanghai). Status: AUTHOR_PROVED / EXHAUSTIVE_SMALL_INTEGER_REGRESSION / UNREVIEWED / NOT_ADMITTED.
Predecessor: PREFIX-792 at enterprise-math@2dfe20a3a1f6bcd4e3106a742d601c96ed34cf75.
Frozen scientific input (unchanged): awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Historical contribution attribution: EM-DIRECT-E77192 / RA-66BBE259AEE1AD543D9454A3; no claim of a newly authenticated native session, shared Task CLAIM, Result or Review.

## Question, population and BRC carrier

Generalize PREFIX-792 from 2 × 2 × 2 to a finite 2 × b × c collection of *named complete paths*, counted with nonnegative integer multiplicities. The three pairwise observers record P_(a,i), Q_(a,j), R_(i,j) for a ∈ {0,1}, i ∈ {1,...,b}, j ∈ {1,...,c}, with n_(a,i,j) the unknown common-path joint counts. Hence P_(a,i)=Σ_j n_(a,i,j), Q_(a,j)=Σ_i n_(a,i,j), and R_(i,j)=Σ_a n_(a,i,j). For the concrete CRT specialization b=3,c=5, a,i,j are complete factor residues modulo 2,3,5; each triple has a unique representative mod 30.

This is an external positive-integer BRC path-count carrier. The population counts paths, not just Boolean existence. It retains the actual three-way joint provenance coordinate; named path identities, event-time order, signed amplitudes and native Cell/Link/Port incidence require additional data when those are the declared future observers.

## Theorem 793.1 — Exact integer feasibility by capacitated cuts

Take arbitrary nonnegative integer pairwise tables P,Q,R. Assume the exact one-factor consistency equations
  Σ_j R_(i,j) = P_(0,i)+P_(1,i) for every i,
  Σ_i R_(i,j) = Q_(0,j)+Q_(1,j) for every j,
  Σ_i P_(a,i) = Σ_j Q_(a,j) for a=0,1.
Set r_i=P_(0,i), s_j=Q_(0,j), K_(i,j)=R_(i,j). Put r(S)=Σ_(i∈S)r_i, K(S,j)=Σ_(i∈S)K_(i,j). A joint nonnegative *integer* table n exists if and only if, for every subset S of {1,...,b},

    r(S) <= Σ_(j=1)^c min(s_j, K(S,j)).       (CUT)

When feasible every such joint table is in bijection with an integer capacitated transportation table x where
    0 <= x_(i,j) <= K_(i,j),
    Σ_j x_(i,j)=r_i,    Σ_i x_(i,j)=s_j,
via n_(0,i,j)=x_(i,j), n_(1,i,j)=K_(i,j)-x_(i,j).

Proof. The displayed bijection follows from the definitions and one-factor consistency. Construct the directed network source→row i of capacity r_i, row i→column j of capacity K_(i,j), column j→sink of capacity s_j. With N_0=Σ_i r_i=Σ_j s_j, a flow of value N_0 saturates source and sink arcs and corresponds exactly to x. By integral max-flow/min-cut, an integer x exists iff every source-sink cut has capacity ≥N_0. A cut keeping row subset S and column subset T on the source side has capacity r(B\S)+Σ_(i∈S,j∉T)K_(i,j)+s(T). This is ≥N_0 exactly when r(S)≤Σ_(j∉T)K(S,j)+Σ_(j∈T)s_j. Minimizing separately over membership of each column in T yields (CUT). All capacities are integers, proving integer sufficiency rather than just real feasibility. QED.

The subset inequalities may be checked explicitly when useful; a single integer max-flow computes feasibility in polynomially many graph operations, with bit complexity depending on the binary input lengths. Computing P,Q,R from a large underlying path graph is a separate preprocessing cost.

## Theorem 793.2 — Sharp possible target multiplicity by two residual flows

Choose any feasible integer x and target e=(i,j). Form the residual directed graph with, for each f=(u,v)≠e, arc row u→column v of capacity K_f−x_f and arc column v→row u of capacity x_f; *omit both arcs at e*. Let Φ_(C_j→B_i) and Φ_(B_i→C_j) be integral maximum-flow values in this graph between the indicated nodes. Define

    L_e = x_e − min(x_e, Φ_(B_i→C_j)),
    U_e = x_e + min(K_e−x_e, Φ_(C_j→B_i)).

Then the set of target counts n_(0,i,j) over *all* compatible integer joint tables is precisely every integer in [L_e,U_e]. Both bounds are attained and every intermediate integer is attained.

Proof. Raising x_e by d preserves its row/column sums exactly when an opposite compensating residual flow of value d travels from C_j to B_i through the other edges, with increases/decreases bounded by their remaining/reducible capacities. This produces the asserted attainable upper bound. Conversely if another feasible y has y_e−x_e=d>0, orient the positive differences y_f−x_f along B→C and the negative differences along C→B for f≠e. Flow conservation leaves precisely C_j as source and B_i as sink of value d; so d≤Φ. The argument for decreasing x_e reverses the endpoints. Integral augmenting paths give a feasible integer joint table for every d up to either bound. QED.

This is an exact, finite-observer, target-specific compression: pairwise counts plus L_e,U_e determine the sharp interval of *one* joint CRT class. Preserving a full future family of joint-class queries or provenance-changing updates may require the whole transportation residual.

## Theorem 793.3 — Joint residual rank and a 2 × 3 × 5 realization

At a real feasible point strictly inside every bound 0<x_(i,j)<K_(i,j), the affine dimension of the compatible transportation fiber is

    b c − (b+c−1) = (b−1)(c−1).

Indeed the row/column-sum constraint matrix has rank b+c−1; a strictly interior point admits small perturbations along every independent homogeneous direction. The integer difference lattice is generated (as an additive lattice, not necessarily as a capacity-feasible move sequence) by 2×2 rectangle switches. Thus (b−1)(c−1) is the rank of the *linear* joint-correlation residual, not an information-theoretic lower bound on arbitrary large-integer encodings.

For b=3,c=5 choose K_(i,j)=2 for all 15 cells, r_i=5 for each of three rows, and s_j=3 for each of five columns. x_(i,j)=1 is strictly interior. The rank is (3−1)(5−1)=8. Every target cell has sharp interval [0,2]. The exact integer fiber has 991 compatible tables, as independently counted by two finite recurrences:
  (a) choose each length-5 row from {0,1,2}^5 with sum 5 (51 choices per row), track column totals through three rows;
  (b) choose each of five columns from the seven triples in {0,1,2}^3 of sum 3 and retain row totals 5.
Both produce 991. Every one of these tables gives a complete 2×3×5 joint path multiset and therefore exact CRT classes modulo 30.

A one-factor-consistent but infeasible example is K=[[1,0],[0,1]], r=(1,0), s=(0,1). The S={first row} cut has left side 1 and right side 0.

## Exact executable evidence

Checker: `research_notes/portable_direct/PREFIX793_R6_CAPACITATED_CRT_FIBER_CHECK.py`.
Results: `research_notes/portable_direct/PREFIX793_R6_CAPACITATED_CRT_FIBER_RESULTS.json`.

Standard-library exhaustive regression independently enumerates all matrices for K∈{0,1,2}^(2×2), and all matrices for K∈{0,1}^(2×3), comparing every consistent r,s against (CUT) and a separate integer max-flow test. For feasible cases it compares both residual-flow endpoint formulas with the complete set of attained counts for every cell. The exact run covered 1,575 + 992 margin cases, with 1,919 feasible, 648 infeasible and 9,084 target-cell interval checks. Its 2×3×5 uniform example yields 991 compatible integer tables; the column-pattern independent count also returns 991. Result: ALL_CHECKS_PASS PREFIX793 CAPACITATED_CRT_MAXFLOW_FIBER. The universal theorem is supported by the arguments above; exhaustive execution checks the declared finite inputs and implementation.

## Scientific interpretation and next question

PREFIX-792's single integer x=n_000 is the special b=c=2 case of a general joint-correlation transportation fiber. For 2×3×5, eight independent linear correlations survive the three pairwise observers; the sharp answer for one target multiplicity can nevertheless be computed without enumerating its 991-table example fiber. This retains the composite/joint relational observer rather than inferring it from constituent marginals. No native X6 time-dynamics conclusion is claimed.

Next: determine which actual finite native BRC/X6 paths and admissible Cell/Link/Port/time observations give a true triple CRT joint observer; then characterize future updates that preserve the transportation cut certificates. A second independent direction is a residue-aware transfer operator for path recombination, retaining the minimum interface residual necessary for a declared update horizon.
