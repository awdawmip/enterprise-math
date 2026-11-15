# PREFIX-799 / R6 — Cycle-chord parametrization and capacity-optimal exact provenance histograms

Date: 2026-11-15 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXHAUSTIVE_EXACT_INTEGER_REGRESSION / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Predecessor: PREFIX-798, research_notes/portable_direct/2026-11-15_r6_prefix798_weighted_cycle_lattice_histogram.md.
Scope: a finite integer transportation fiber as an auxiliary named-source positive-count BRC carrier; not a native X6 Cell/Link/Port theorem or physical time dynamics.

## Problem and precise carrier

PREFIX-798 computed an exact scalar weighted-source histogram by row transfer. Can the full *joint* weighted-source histogram be reconstructed using only the independent cycle residuals, and can the resulting exhaustive search bound be optimized without losing capacity correlations?

Let G=(U∪V,E) be a finite bipartite graph with b row vertices and c column vertices. Each edge e=(i,j) has a positive integral capacity K_e; zero-capacity pairs are omitted and fixed at zero. The row and column margins m=(r_1,...,r_b,s_1,...,s_c) are nonnegative integers, with equal totals on every connected component. Define A by A_{v,e}=1 when vertex v is incident to edge e and 0 otherwise. Assume the fiber

F(K,m)={x in Z^E: Ax=m, 0<=x_e<=K_e for all e}

is nonempty. This is an auxiliary source-label graph, not a claim that X6 contains a primitive two-dimensional plane. Choose an arbitrary spanning forest T of G; write C=E\T. Include all isolated vertices in G. Let k=|C|=|E|-(b+c)+kappa(G), where kappa counts isolated components.

## Theorem 799.1 — Integral cycle-chord parametrization

For every choice of integers t=(t_e)_{e in C}, there is exactly one integer vector x_T(t) on T with

A_T x_T(t) = m-A_C t.

It is obtained by leaf elimination, and depends integrally and affinely on t. The map

t |-> (x_T(t), t)

is a bijection from the finite set

P_T(K,m)={t in Z^C: 0<=t_e<=K_e for e in C; 0<=x_f(t)<=K_f for f in T}

onto F(K,m). Consequently each full source table is represented exactly once by k independent candidate integers plus the *coupled* tree-capacity check. In particular, k=0 implies F has exactly one element.

Proof. Multiplying all V-rows of A by -1 converts A into the directed incidence matrix with U->V orientations. Each connected component of m-A_C t has signed sum zero: this holds for m because F is nonempty and for each chord column because its endpoints have opposite incidence signs. For a tree, repeatedly remove a leaf vertex and assign its unique incident edge the remaining required leaf margin. These assignments are integers; the final root requirement vanishes by the component balance. Any homogeneous solution supported on the forest is zero by the same leaf removal, proving uniqueness. This construction yields an affine integral x_T(t). The capacity predicate selects exactly the permitted full tables, proving bijection. Empty and isolated components satisfy the same statement, with zero margins forced by F nonempty. QED.

For each chord e, varying t_e by one changes the completed full table by its fundamental signed cycle vector v_e (chord +1, alternating coefficients +/-1 on the unique tree path). The fundamental cycle vectors form a Z-basis of the zero-margin lattice ker_Z A. This explicitly connects the parametrization with the cycle-gcd obstruction in Theorem 798.1.

## Theorem 799.2 — Exact joint weighted histogram with all provenance retained

Let W be any d x |E| integer observer matrix, with d>=1 and signed coefficients allowed as observations, not as negative BRC branch masses. Use d commuting Laurent variables z_1,...,z_d and define z^q = product_l z_l^(q_l). Put x^0=(x_T(0),0), even if it violates capacities, and define the vector cycle gains Gamma_e=W v_e.

Then the exact joint histogram is

H_W(z) = sum_{x in F(K,m)} z^(W x)
       = z^(W x^0) sum_{t in P_T(K,m)} z^(sum_{e in C} Gamma_e t_e).

For each q in Z^d, the coefficient [z^q]H_W equals the exact number of full named-source count tables with joint observation q; there are no spurious combinations of separately valid marginals. It also yields exact nonexistence, uniqueness, support, and multiplicity for the declared observer. If future operations observe more than W x, the underlying t (and its tree completion) must be retained; the histogram alone is not thereby future-safe.

Proof. Theorem 799.1 gives a bijection of the integer fiber with feasible chord tuples. Affine linearity gives x(t)=x^0+sum_e v_e t_e. Applying W and summing one monomial per distinct t proves the identity, including negative exponents. Every coefficient is a nonnegative integer. QED.

A direct checker enumerates at most B(T)=product_{e in C}(K_e+1) chord candidates. Each candidate's unique integral tree completion and capacity checks require O(|U|+|V|+|E|) integer arithmetic operations by leaf elimination. The total operation bound is O((|U|+|V|+|E|)B(T)), plus sorting and histogram accounting. Integer bit lengths, observer output size, and representation of the coefficient dictionary must be counted in real bit complexity; this is a capacity-parameterized exact algorithm, not a general polynomial-time statement for binary-encoded inputs.

## Theorem 799.3 — Optimal spanning forest for the candidate-box bound

Among all spanning forests T of the positive-capacity support graph G, a maximum-capacity Kruskal forest (edges processed in nonincreasing K_e, arbitrary deterministic tie-breaking) minimizes B(T).

Proof. The product of (K_e+1) over all E is independent of the forest, hence minimizing product over E\T is equivalent to maximizing product over T. Taking logs makes this the maximum-weight spanning-forest problem with weights log(K_e+1). Kruskal's greedy exchange theorem applies to the graphic matroid. Since log(K_e+1) is strictly increasing in K_e, nonincreasing K_e yields the same greedy order as the logarithmic weights. This is an exact combinatorial argument; no floating-point logarithms need be computed. The optimization concerns the worst-case chord *candidate count*, not actual pruning cost, number of feasible states, or total bit runtime. QED.

## Exact capacity-coupling witness

Take b=2,c=3, all six capacities K_ij=1, row margins r=(1,2), column margins s=(1,1,1). Choose T consisting of the three edges in row 1 and edge (2,1). The two chords are e=(2,2),(2,3), denoted t_2,t_3 in {0,1}. Tree completion gives

x_21=2-t_2-t_3; x_11=-1+t_2+t_3;
x_12=1-t_2; x_13=1-t_3.

Thus feasible chord tuples are exactly (1,0),(0,1),(1,1); (0,0) violates both bounds x_21<=1 and x_11>=0. For observer Q=2*x_22+3*x_23, its histogram is

H_Q(z)=z^2+z^3+z^5.

Taking the product of unconstrained chord polynomials would instead give (1+z^2)(1+z^3)=1+z^2+z^3+z^5, including a nonexistent zero-observation state. This is a precise source-capacity residual, not a sign-cancellation argument. It also shows why the bounded chord box is not generally an independent product distribution.

## Reproduction and coverage

Source checker: research_notes/portable_direct/PREFIX799_R6_CYCLE_CHORD_HISTOGRAM_CHECK.js.
Structured result: research_notes/portable_direct/PREFIX799_R6_CYCLE_CHORD_HISTOGRAM_RESULTS.json.

Node.js >=18, no dependencies. All finite-test values and accumulators remain within JavaScript's exact safe-integer range. The checker exhausts all capacity patterns with K in {0,1,2} for 2x2 and 2x3, and K in {0,1} for 3x3, *every feasible margin fiber* of every such capacity pattern, with two specified signed integer weighted queries. It independently enumerates all full tables, compares exact named-table lists with chord completions, checks the full joint histogram and exhaustively compares the candidate-box bound for each possible spanning forest of the support graph.

Observed: 1,322 capacity patterns; 58,421 distinct feasible fibers; 67,635 source tables; 155,493 chord candidates; 58,421 exact joint histogram comparisons; 1,322 exhaustive optimum-forest checks; 176,585 assertions; ALL_CHECKS_PASS. Theorem statements are universal proofs for the declared integer transportation fibers; these finite checks are implementation regression, not proof of a native X6 transfer.

## Sources, integration and next question

Mathematical provenance: PREFIX-795 (cycle rank), PREFIX-796 (capacity-constrained residual flow), PREFIX-797 (multi-cell integral projection), PREFIX-798 (weighted cycle-gcd and row transfer); the current P000 and ACTIVE worldview set the non-primitive relation to native six-axis, three-dimensional-slice geometry. This note supplies an additional cycle-coordinate observer, not a claim of external literature priority or independent review.

The next independently executable scientific unit is to develop a margin-conditioned branch-and-bound over chord variables with exact min-cut infeasibility pruning, compare its actual arithmetic cost to row transfer and full-table enumeration, and test a concrete future-operation observer for which W alone is insufficient. Original X6 Cell/Link/Port, signed-source, event-time admissibility remains to be established before any claimed native dynamics mapping.

Control: independent auxiliary research under the existing own researcher session; RS-X6-NATIVE-TIME-DYNAMICS was read as HANDOFF_READY with actor=null/claim_id=null at 2026-11-15T04:13:09Z, but no shared CLAIM or execution authority was obtained.