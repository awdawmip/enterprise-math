# PREFIX-797 / R6 — Exact simultaneous-cell residual projection by integral cut certificates

Date: 2026-11-15 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_INTEGER_REGRESSION / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Predecessor: PREFIX-796 at f72cf08ae29de5a227b477179f77962390642807.
Scope: positive-integer complete-path histograms with named BRC provenance cells; abstract auxiliary observer, not a native X6 update or a validated heartbeat trajectory.
Carrier: two path types per named source cell of a b x c rectangular indexing table, with exact counts, not signed amplitudes.

## Question and setup

PREFIX-796 obtained sharp one-coordinate integer ranges from residual max flow. These ranges do not describe the feasible *joint* uncertainty of two or more unobserved provenance coordinates, because source-cell counts share row/column constraints.

Let b,c >=1, E={1,...,b} x {1,...,c}, integer capacities K_ij>=0, and row and column supplies r_i,s_j>=0 with sum_i r_i=sum_j s_j. Assume the full integer fiber

  F(K,r,s)={x in Z^E: 0<=x_ij<=K_ij,
             sum_j x_ij=r_i, sum_i x_ij=s_j}

is nonempty. The second path type has multiplicity K_ij-x_ij. A known coordinate may be removed from the unknown cell set by adjusting the corresponding supplies; equivalently keep it as one of the fixed target entries below.

Choose ANY finite set S subseteq E and integer proposed counts t=(t_e)_(e in S). Let U=E\S, and set

  R_i(t)=r_i - sum_{j:(i,j) in S}t_ij,
  D_j(t)=s_j - sum_{i:(i,j) in S}t_ij.

## Theorem 797.1 — Exact multi-coordinate feasibility and min-cut dual certificate

There exists x in F(K,r,s) satisfying x_e=t_e for ALL e in S if and only if:

1. t_e is integer and 0<=t_e<=K_e for e in S;
2. all R_i(t),D_j(t) are nonnegative, and sum_i R_i=sum_j D_j; and
3. for every subset I of row vertices and subset J of column vertices,

   sum_(i in I) R_i(t)
   <= sum_(j in J) D_j(t)
      + sum_(i in I,j notin J,(i,j) in U) K_ij.                  (CUT)

The conditions are sharp for arbitrary finite b,c, capacities and selected cells. A feasible assignment has an integer witness; if conditions fail, either a local bound or an explicit violated cut is a certificate of failure.

**Proof.** Remove the fixed cells S and construct the standard directed bipartite network: source -> row i with capacity R_i; row i -> column j for every (i,j) in U with capacity K_ij; column j -> sink with capacity D_j. When condition 2 holds, an integer max flow of value T=sum_i R_i provides an integer filling y on U with exactly the required row and column sums; append the fixed t to obtain x. Conversely every such x defines an integral flow of value T.

A source-side cut containing source, exactly the row set I and column set J has outgoing capacity

  sum_(i notin I) R_i + sum_(i in I,j notin J,(i,j) in U)K_ij
      + sum_(j in J)D_j.

Its capacity is at least T if and only if (CUT) holds. All cuts have this form. Max-flow/min-cut makes the conditions necessary and sufficient. All network capacities are integers; augmenting-path integral max flow supplies the required integer solution. QED.

## Theorem 797.2 — Hole-free integer projection of the bounded transportation fiber

Let Q_S subseteq R^S be the real polytope described by the inequalities of Theorem 797.1, with the requirement 't is integer' removed. Then

  projection_S F(K,r,s) = Q_S intersect Z^S.                   (LATTICE)

**Proof.** Any integer source table belongs to the real polytope by necessity. Conversely an integer point t in Q_S passes all real feasibility cuts. After fixing its integer entries, the residual network has integer capacities and integer supplies. The integrality of max flow produces an integer table x with projection t. Hence every integer point in the continuous projection is attainable, with no additional lattice holes. QED.

This is an exact statement about coordinate projections of bounded integral bipartite-flow fibers; it is not asserted for arbitrary integer polytopes.

**Algorithm and certificates.** Membership of any proposed simultaneous target t is decided by one integral max-flow on b+c+2 vertices and at most |U|+b+c edges, after linear-size bookkeeping. A maximum flow supplies a positive certificate; a deficient minimum cut supplies a violating (I,J) certificate. Thus the exponentially many written inequalities admit polynomial-time separation by the ordinary max-flow algorithm (with the usual input bit-cost qualifications).

## Theorem 797.3 — Individual sharp intervals can be jointly inconsistent

Use b=c=2, capacities K_ij=2 for all four cells, and row/column counts r=(2,2), s=(2,2). The full fiber is exactly

  x(z) = [[z,2-z],[2-z,z]],  z in {0,1,2}.

Thus each of x_11 and x_12 separately has the full sharp range {0,1,2}, while their joint projection is

  {(0,2),(1,1),(2,0)}.

For example the proposed pair (x_11,x_12)=(0,0) satisfies BOTH marginal coordinate intervals but is impossible: the fixed first row totals 0 instead of r_1=2. More generally, the sum x_11+x_12=2 is an exact coupling residual. The minimal repair for this two-coordinate question is one constraint, not an independent interval per coordinate.

## Reproducible exact verification

Checker: research_notes/portable_direct/PREFIX797_R6_MULTI_CELL_CUT_CERTIFICATE_CHECK.py
Results: research_notes/portable_direct/PREFIX797_R6_MULTI_CELL_CUT_CERTIFICATE_RESULTS.json

The standard-library Python checker (no floating point or randomness) directly enumerates the entire feasible fiber for every covered (K,x) state. For every pair of chosen cells and EVERY pair of proposed integer counts 0<=t<=K, it compares membership in the brute-force fiber projection with BOTH an independently computed integer max-flow test and direct enumeration of ALL row/column cuts.

Complete domains:
- 2x2 with each 0<=x_e<=K_e<=2 (1296 states);
- 2x3 with each 0<=x_e<=K_e<=1 (729 states).
An additional deterministic stride-41 subfamily of the 2x3 K_e<=2 domain contributes 1138 states. Total 331328 exact assertions including six explicit witness assertions; ALL_CHECKS_PASS. The theorems are proved generally above; finite computation is a reproducible implementation check only.

## Relation to BRC, P000 and open frontier

The count carrier retains path type and source-cell identity, and uses exact nonnegative integer arithmetic; row/column readouts are partial observers of a joint source relation. The (b,c) grid indexes a provenance correlation table. It is **not** a two-dimensional native geometric plane, does not change the six native X6 spatial axes or the three-dimensional slice convention, and adds no seventh spatial axis. Time is independent if native temporal events are later typed.

A future native X6 transfer requires an explicit mapping from actual Cell/Link/Port, signed source and event-time operations into this count carrier, with a proof that its K, row/column constraints and allowed coordinate observations are preserved. Synthetic cell swaps from PREFIX-795/796 remain auxiliary.

Next concrete questions:
1. Obtain the exact native allowable event/readout map, if authorized, and identify genuine conserved integer capacities and admissible partial queries.
2. For a chosen family of future operations, characterize which CUT inequalities remain observable and whether they form a smaller minimal sufficient residual quotient.
3. Determine optimal multi-cell measurement selection under a declared cost budget; a sum of independent PREFIX-796 interval widths is not the correct joint objective.

Attribution: Current independent researcher session source must be verified separately. Prior activity RA-63E1066C3056A93898BE8E18 belongs to recorded identity EM-DIRECT-4660FF; shared Task RS-X6-NATIVE-TIME-DYNAMICS requires its own winning CLAIM and separate review. The exact transport of this article is evidence preservation, not Foundation admission.
