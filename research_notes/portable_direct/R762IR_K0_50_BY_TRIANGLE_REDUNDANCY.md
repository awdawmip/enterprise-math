# R762IR — Fifty-event kernel for k=0 via Port-triangle redundancy

Date: 2026-11-22 (Asia/Shanghai).
Status: AUTHOR_PROVED / TWO_EXACT_FINITE_CHECKERS / CONSTRUCTIVE_WITNESS_TESTED / NOT_REVIEWED.
Frozen scientific source: a72226e2430ffa4786321ac86e7f0c599d5f0389.
Predecessor: R762IQ@1242433dd9ff8e123cb8d01936c1895d9d0110b9, R762IP@449ecf17d3407c86a18323288fa5972c742d6ab6, R762IM@b5e3a6073c54d1bbccd3a5d798887def7243a34c.
Scope: composite Port-Euler observer on six labeled axes, NOT native P000 signed triad dynamics. No change to task scientific pins, P000, ownership or review state.

## Definitions and theorem

Let A={0,...,5}. A Port is a two-element subset of A; there are 15 Ports. Each of the 20 three-element supports S contributes exactly the three possible edges between its contained Ports, forming a triangle. One named event of support S selects one of those three edges. A legal Port history is a connected, nonempty, all-even-degree multigraph on its actual active Port set V, with prescribed support counts n_S, hence admits an Euler circuit from every chosen p in V. Inactive Ports have degree zero. The observer retains V, p, the set of positive support types and each support count modulo two.

**Reduction theorem (arbitrary other counts).** Suppose a legal history exists and at least 11 of its support types have exactly three events. Then there exists a support j of count three which can be changed to count one, with all other counts unchanged, while retaining a legal Port-Euler history, the exact active set V, the chosen starting Port p, support positivity and per-support parity. In particular an event pair can be restored along the surviving edge of support j.

**Uniform k=0 theorem.** If all 20 counts satisfy 0 <= n_S <= 3, then for every legal Port history H there is a legal witness h with
  0 <= h_S <= n_S,  h_S > 0 iff n_S > 0,  h_S = n_S (mod 2),
  sum_S h_S <= 50,
with the same active Port set and any prescribed starting Port of H. Each reduction is constructive. No Claim/Result or independent review is asserted.

**High-tail corollary.** If 0 <= n_S <= 3, sum n_S is 54, 56, 58 or 60, and a legal history exists, then there is an *exactly 52-event* witness with the same preserved observer. This closes the coverage gap recorded for R762IM without enumerating all 14,260,096 (n,M) incidence candidates. The k=0 uniform upper bound improves the prior 53 to 50; the earlier whole-model 54-event bound, which also has four-event supports, is unchanged here.

## Exact finite hypergraph lemma

Call a family of support triangles connectivity-essential if removing any one triangle changes the partition of all 15 Ports into connected components of the union graph. In the fixed 20-triangle system, **no family of 11 triangles is connectivity-essential**. Indeed, the exhaustive independent C++17 enumerator checks all binomial(20,11)=167,960 labeled 11-subsets; for every subset it finds a triangle whose deletion leaves the same exact pairwise connectivity relation. Of binomial(20,10)=184,756 labeled 10-subsets, exactly six are entirely essential (integer support masks 1023, 64527, 466033, 746898, 895652, 971592). Thus the threshold 10 is sharp for this finite hypergraph lemma.

Proof that the 11-subset test bounds any larger family: if a triangle is essential in a family F, it stays essential in every smaller family containing that triangle, because a pair separated by deleting it in F remains separated when other edges are removed. If F had 11 essential triangles, those 11 alone would be an all-essential 11-subset, contradiction. The same argument works when restricted to any active Port set V, since triangles fully contained in V have the same connectivity comparison when the excluded Ports are adjoined as isolated vertices.

The test uses exact integer combinatorics, not floating point: enumerate every increasing 10/11-subset of the 20 support indices; for each, union the three vertices of each triangle in a disjoint-set graph; compare all 105 unordered vertex pairs before and after each candidate deletion. The 11-subset checker and a separate dynamic-partition implementation traversing all 2^20 support masks returned the same maximum essential count 10 and six all-essential 10-subsets. Source files and numerical outputs accompany this note. This is a finite computer-assisted lemma with its declared complete domain.

## Proof of the reduction theorem

Let t be the number of supports with n_S=3. For each such support that has all three Ports active, form its full triangle. Let G_3 be the union of these triangles on V. The finite lemma says that at most 10 full-triangle supports in any such family are essential for G_3 connectivity. If t>=11, choose an exactly-three support j which either has only two active Ports, or has three active Ports and is non-essential in G_3.

If j has two active Ports, all three original events must use their unique allowed edge. Replacing them by one event on the same edge preserves parity, positive incidence, and the connectivity relation.

Otherwise j has three active Ports a,b,c and the other three-event full triangles still connect a,b,c inside one G_3 component after its removal. Fix the allocation of every support other than the full-three-event triangles, and replace j by one edge, say ab. Every full-three-event support i has the complete GF(2) boundary choice set {0, e_ab, e_ac, e_bc} on its own triple: boundary zero is attained by its three distinct triangle edges; a prescribed edge boundary is attained by one copy of that edge and two copies of a DIFFERENT triangle edge. Each such realization connects all three of its Ports. This is the n_S=3 case of the exact quotient lemma R762IP.

The difference delta between the old boundary of j and the chosen one-edge boundary is either zero or a two-vertex boundary on {a,b,c}; these vertices lie in one component of the other full triangles. Along a path between them in that graph, XOR the edge-boundary corrections into their unique supporting triangles. The path telescopes to delta; each triangle's accumulated correction is again zero or a pair boundary on its own three vertices. Re-realize the remaining full-three-event supports with the resulting desired boundaries and three-edge connected local realizations. The total Port parity remains even.

Connectivity also survives. Every unchanged non-three-event support keeps its old edges. Every re-realized full-three-event triangle connects all three of its active Ports, so no old connectivity carried by it is lost. The old j triangle's three vertices are already mutually connected through the remaining full triangles, so replacing it by ab cannot disconnect the total union. Every initially active Port remains active. Hence the resulting graph is connected and even-degree, with the claimed counts. An Euler circuit from p follows.

The induction uses no fixed sign, time, rotation, Cell address, or physical BRC arithmetic: it is a typed observer-level Port graph argument. A native TRIADIC_CLOSURE_E lift still requires its separate map and residual-fidelity proof.

## Counting consequences

Repeatedly apply the reduction theorem while t>=11. Each step changes exactly one three-event count to one, preserving positive support types and count parity. At termination t<=10. Every other count in the k=0 domain is <=2; therefore
  sum h_S <= 3t + 2(20-t) = 40+t <= 50.

For N in {54,56,58,60}, define the deficit D=60-N in {6,4,2,0}. Each non-three-event support has deficit at least one, so initially t>=20-D, respectively 14,16,18,20. To reach exactly 52 events needs (N-52)/2 reductions, respectively 1,2,3,4. At each such step the current t is at least 14,15,16,17 respectively before the last reduction, so the >=11 criterion remains satisfied. All 52-event outcomes preserve the specified V and p, establishing the high-tail corollary.

## Independent validation and example

C++17 subset checker actual output:
  ten=184756 allessential10=6 eleven=167960 allessential11=0
  sharp masks: 1023,64527,466033,746898,895652,971592.

Independent dynamic-partition C++17 check over 1,048,576 masks:
  max-essential=10; essential-only-count=77310 (all mask sizes);
  min redundant at size 11 = 4; size 14 = 10;
  exactly six 10-subsets are all essential.

Python exact integer constructive test:
  choose two-event supports indexed (0,1,2,4,5,7) and three events on each of the other 14 supports, all 15 Ports active;
  start with full triangles and doubled two-event edges, giving a connected even-degree 54-event graph;
  choose successive removable three-event supports (10,11,13,16), reassign triangle edges by path-boundary corrections;
  verified event totals 54->52->50->48->46, with every support count, active Port, connectedness and even degree checked after each step.

The finite census establishes the structural bound, while the Python construction tests a concrete boundary case; the latter is not a substitute for the general proof.

## Unresolved and next step

The 50 upper bound may not be optimal. The six 10-support extremal hypergraphs are the right next finite family: incorporate the other ten supports' parity and connectivity to test whether all actual Euler realizations can be reduced further. The whole-model absolute bound still depends on the four-event bridge cases (k>0); treat them separately. For the model's native P000 dynamics, the signed Cell/Link/force/rotation/time lift and future-observer preservation remain open.

Control provenance: new independent portable research; prior R762IQ author context is historical scientific provenance, not a current authenticated CLAIM. Source publication, Activity, canonical progress and mathematical admission are independent states.
