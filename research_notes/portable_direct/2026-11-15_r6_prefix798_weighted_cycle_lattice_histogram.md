# PREFIX-798 / R6 — Weighted provenance observers: cycle-lattice congruence and exact histogram transfer

Date: 2026-11-15 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_INTEGER_REGRESSION / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Predecessor: PREFIX-797, research_notes/portable_direct/2026-11-15_r6_prefix797_multi_cell_integral_cut_projection.md.
Scope: finite bounded integer transportation fibers as auxiliary labeled positive-path-count BRC carriers. No native X6 dynamics claimed.

## The research question

PREFIX-797 gives a sharp integer max-flow/min-cut decision for simultaneous specified cell counts. Consider instead an aggregate weighted observation Q_w(x). Its scalar extremal interval and its residue classes may retain information that differs from the actual finite attainable set. What is the precise lost residual, and how can it be computed without treating independent cells as independent?

Fix positive integers b,c, capacities K_ij in nonnegative integers, row margins r_i, column margins s_j with equal total, and the nonempty fiber

F(K,r,s) = { x in Z^(b*c): 0 <= x_ij <= K_ij; sum_j x_ij = r_i; sum_i x_ij = s_j }.

Let w_ij be any integer weight and Q_w(x)=sum_ij w_ij*x_ij. Cells label distinct source-provenance classes; counts are nonnegative integers, and w is an observation coefficient (not a negative branch mass). Let G_K be the bipartite graph on row and column vertices containing exactly edges with K_ij>0.

For an even simple cycle C in G_K define its alternating integer gain gamma_w(C)=sum_(alternating + edges)w_e - sum_(alternating - edges)w_e, up to overall sign. Let g_w be the nonnegative gcd of all gamma_w(C), with gcd of the empty set and of all zeros defined to be zero.

## Theorem 798.1 — Universal structural residue obstruction

For any x,y in F(K,r,s):

Q_w(x)-Q_w(y) belongs to g_w*Z.

When g_w=0 the observation Q_w is constant on the entire fiber. When g_w>0 the attainable values all lie in one congruence class modulo g_w.

Proof. Orient each graph edge from row to column. The integer difference d=y-x has zero incidence at every vertex, since the margins agree. On a spanning forest of G_K, sequential elimination of non-tree edge coefficients expresses every integer zero-incidence vector as an integer linear combination of fundamental simple-cycle signed incidence vectors. This follows integrally: remove the chosen integer coefficient along each chord's unique fundamental cycle, leaving a zero-incidence vector on a forest, which must vanish by leaf elimination. Therefore Q_w(d) is an integer linear combination of fundamental-cycle gains. Every such gain is divisible by g_w, proving the assertion. If g_w=0 all cycle gains vanish and Q_w(d)=0. QED.

This is a necessary structural congruence for the specified fiber. It need not describe every feasible residue, since margins and capacity saturation can suppress cycle moves.

## Theorem 798.2 — Characterization of weights with zero structural residual

The following are equivalent on every connected component of G_K:

(i) g_w=0.
(ii) Each simple-cycle alternating weight sum is zero.
(iii) There exist vertex potentials alpha_i on rows and beta_j on columns such that w_ij=alpha_i+beta_j on every edge of G_K.

Consequently Q_w(x)=sum_i alpha_i*r_i+sum_j beta_j*s_j for every x in F(K,r,s). In particular, total-sum row/column observers are structurally sufficient for exactly these potential-type weighted queries, even before inspecting capacity saturation.

Proof. (i) and (ii) are the definition of gcd zero. For (ii) to (iii), fix an arbitrary row/column vertex potential at one root of each graph component and propagate the equation w_ij=alpha_i+beta_j along a spanning tree. The equation on any chord is consistent exactly when the corresponding fundamental-cycle alternating sum vanishes. Conversely an alternating cycle telescopes the vertex potentials, proving (iii) implies (ii). Summing the edge equations over x establishes the formula. QED.

## Theorem 798.3 — Exact weighted BRC histogram by provenance-preserving transfer

Define the polynomial (Laurent polynomial for signed weights)

H_w(z)= sum_(x in F(K,r,s)) z^(Q_w(x)).

Its coefficient at exponent q equals the exact number of full named-source count tables realizing q; hence the support is the exact attainable query-value set, including gaps.

Set D_0(0,...,0;z)=1 and other D_0(d;z)=0. For row i=1,...,b, define

D_i(d;z) =
  sum_{t in Z^c: 0<=t_j<=K_ij, sum_j t_j=r_i, t_j<=d_j}
    D_(i-1)(d-t;z) * z^(sum_j w_ij*t_j),

where 0<=d_j<=s_j, with any out-of-range state zero. Then H_w(z)=D_b((s_1,...,s_c);z).

Proof. A table of the first i rows has a unique last-row vector t and a unique preceding (i-1)-row table with column load d-t. The exponent is additive and the number of completions multiplies by one for this uniquely chosen row. Conversely each summand constructs a distinct integer table respecting its capacities and row margins; column-load cutoffs enforce the final s. Induction in i proves the equality, with nonnegative integral coefficients and no cancellation. QED.

This is an exact finite algorithm. For fixed c and bounded margins it is a pseudo-polynomial dynamic program in the column-load state space product_j(s_j+1), row-choice count product_j(K_ij+1), and represented polynomial support size; it is not asserted to have polynomial bit complexity in unrestricted c or binary-encoded margins.

If the attainable exponents have minimum L and maximum U, reduction of H_w modulo z^m-1 for m>U-L is injective on the exponent support (with the known shift L): q in [L,U] is determined by q modulo m. For smaller m, the coefficients become exact residue counts but can merge different exponent values. This follows because two distinct integers in [L,U] have difference strictly between -m and m.

## Counterexample A — A genuine gcd-1 observer gap

Take b=c=4, capacities K=1 on the edges of two disjoint complete 2x2 blocks (rows/columns {1,2} and {3,4}), and K=0 elsewhere. Every row and column margin equals one. Set w_11=2, w_33=3, all other weights zero. Each block has precisely two 0-1 permutation tables. Consequently

H_w(z)=(1+z^2)(1+z^3)=1+z^2+z^3+z^5.

The two fundamental cycles have gains 2 and 3; hence g_w=gcd(2,3)=1. The attainable set is {0,2,3,5}, despite its convex interval being [0,5] and its structural gcd being 1. In particular values 1 and 4 are absent. Thus gcd-1 congruence is not a sufficient accessibility certificate. Each table's provenance correlation is retained in the exact polynomial.

## Counterexample B — A nontrivial congruence gap

Take b=c=2 with K_ij=1, r=s=(1,1), and w=(1,0,0,1) in row-major order. The only two feasible tables are the two permutation matrices, yielding H_w(z)=1+z^2. The alternating cycle gain is 2, so g_w=2 and the intermediate value 1 is ruled out by the cycle congruence.

## Reproducibility and verification scope

Checker: research_notes/portable_direct/PREFIX798_R6_WEIGHTED_PROVENANCE_HISTOGRAM_CHECK.py
Results: research_notes/portable_direct/PREFIX798_R6_WEIGHTED_PROVENANCE_HISTOGRAM_RESULTS.json

Pure Python 3 standard-library exact integers. The checker enumerates every capacity assignment and feasible table in 2x2 with K<=2 and 2x3 with K<=1; in 3x3 with K<=1 it selects capacity masks with enumeration index divisible by seven. For each distinct (K,r,s) fiber it compares row-transfer polynomial coefficients against directly enumerated tables for four explicitly defined weight patterns, computes a spanning-forest gcd independently, and checks injective modulus m=U-L+1. It also verifies both exact counterexamples. Output: 53,980 exact assertions, ALL_CHECKS_PASS. Enumeration validates the stated finite domains; the preceding arguments establish the three general mathematical statements.

## BRC / Enterprise Math interpretation, sources, and next unfinished question

BRC carrier is a named-cell positive integer multiplicity histogram. Q_w is a typed scalar observer; H_w retains exact multiplicity and correlated provenance. The bipartite indexing grid is a mathematical source table, not a native X6 geometric plane or replacement for the P000 six spatial axes / three-dimensional slice / independent ordered time. The underlying count tables themselves remain available when future source-level updates require more than Q_w or H_w.

Source basis: PREFIX-795 graph cycle-rank, PREFIX-796 capacity-sensitive residual flow, PREFIX-797 multi-cell integral cut projection; current P000 and BRC Foundation typing. Theorem and code here are original author derivations, not presented as external priority or an accepted Foundation theorem.

Next research: (1) characterize when capacity-saturated fibers exhibit observer invariants not captured by the full cycle lattice; (2) construct a practical cut-conditioned transfer for multiple simultaneous weighted queries and derive minimal future-safe residuals; (3) obtain and verify an actual native Cell/Link/Port, signed-source, event-time observer map before transferring any theorem to an X6 dynamical claim.

Control: independent auxiliary Source research under registered historical current-session source, pending source-checked Activity association; no shared RS-X6-NATIVE-TIME-DYNAMICS CLAIM, Result, or Review is implied.
