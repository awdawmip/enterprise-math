# R762CN — Two marked X6 Port sources: adjacency-sensitive exact N-BRC quotient

Status: AUTHOR_PROVED_AND_AUTHOR_EXACT_CHECKED; independent review NOT_REVIEWED.
Task RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142; researcher EM-X6-3050F6; own SID MCP-4b2d70a97f594366a7c94a0f8b45df38.
Continuation: R762CM, Draft PR #2594@80ebec6ef5abc0e17d3bf26923c97230778824ff.
Frozen science: enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000 V5); taskbook/publication @e3f42efac29a2da2d95be391f3231a664e2fade0.
Scope: conditional K4 triad-incidence candidate on the six distinct signed-X6 axis token names. Neither TRIADIC_CLOSURE_E native event legality nor V17/V29/V39 transport is presumed.

## Typed model

Label six native-axis source tokens by K4 edges in the order 01,02,03,12,13,23. An unordered 3+3 partition of all six labels is one named candidate configuration. Exactly ten partitions exist. Four are star/face (F) and six path/path (P). Each configuration has nine *candidate* successors, one for every exchange of a token in one triple with a token in its complementary triple (R762CL).

Fix two distinct marked token names a,b and nonnegative integer source multiplicities λ,μ. A candidate exchange of tokens x,y has positive integer BRC weight

\[
w(x,y)=\lambda^{\mathbf1\{a\in\{x,y\}\}}\mu^{\mathbf1\{b\in\{x,y\}\}},
\]

with the convention that a nonselected factor is 1 (including when the corresponding parameter is zero). Equivalently, multiply λ if a is exchanged, μ if b is exchanged, and 1 otherwise. At zero, marked microbranches are absent. A joint exchange containing both tokens has multiplicity λμ. The observer reads the present F/P class and the exact **unnormalized** count of weighted positive source paths ending in each F/P class after any number of future swaps. Two states are equivalent iff these two integer counts agree for every t≥0. This is a stated positive-mass language, not signed force cancellation.

## Theorem 1: degree interaction obstruction

Let same(s) mean both marked tokens lie in the same triple. Then

\[
d_{\rm same}=3(\lambda+\mu+1),\qquad
d_{\rm split}=4+2\lambda+2\mu+\lambda\mu,
\quad d_{\rm split}-d_{\rm same}=(\lambda-1)(\mu-1).
\]

Exactly four of the ten partitions are same and six are split, regardless of whether a and b are adjacent or opposite K4 edges. Thus both relative mark geometries have the identical multiset of weighted row degrees.

**Proof.** In same-triple states, there are three λ-only exchanges, three μ-only exchanges and three unit exchanges. In split-triple states, there is one joint λμ exchange, two λ-only, two μ-only and four unit exchanges. To count same partitions choose the third token alongside a,b from the other four. This proves every formula. QED.

## Theorem 2: exact infinite-horizon minimal positive N-BRC observer quotient

The two K4 mark geometries are adjacent (share a vertex) and opposite (disjoint). For all λ,μ∈Z≥0, the exact number K of future-equivalence classes and minimum *additional fixed-length bits after the current F/P readout* are:

| Mark geometry | Parameters | K | Extra bits |
|---|---|---:|---:|
| Adjacent | λ=μ=1 | 2 | 0 |
| Adjacent | Exactly one parameter equals 1 | 3 | 1 |
| Adjacent | λ=μ≠1 | 5 | 2 |
| Adjacent | λ≠μ and neither equals 1 | 7 | 3 |
| Opposite | λ=μ=1 | 2 | 0 |
| Opposite | Every other pair | 3 | 1 |

**Stronger assertion:** present F/P together with the two F/P path counts after exactly one candidate exchange already separates all the classes in this table. The listed partitions are all strongly lumpable, hence preserve F/P source counts for arbitrarily long future runs. The upper and lower bounds match.

### Adjacent marks: explicit seven-state certificate

Take (a,b)=(01,02)=(0,1). Canonical three-index representatives denote unordered 3+3 partitions; edge indices run from 0 to 5. Set

A={012,013} F same; B={014} P same; C={015} P same; D={023} P split; E={024,034} F split; U={025,035} P split; G={045} P split.

With row sources and column targets in order (A,B,C,D,E,U,G), exhaustive nine-exchange counting gives the strongly lumpable transfer matrix

\[
T_{\rm adj}=
\begin{pmatrix}
1&1&1&\mu&\lambda+\mu&\lambda+\mu&\lambda\\
2&0&1&\lambda&2\mu&2\lambda&\mu\\
2&1&0&\lambda&2\lambda&2\mu&\mu\\
2\mu&\lambda&\lambda&0&2&2&\lambda\mu\\
\lambda+\mu&\mu&\lambda&1&1&\lambda\mu+1&1\\
\lambda+\mu&\lambda&\mu&1&\lambda\mu+1&1&1\\
2\lambda&\mu&\mu&\lambda\mu&2&2&0
\end{pmatrix}.
\]

The exact one-step (F,P) source-output signatures of its rows are:

| Group | F | P |
|---|---|---|
| A | λ+μ+1 | 2(λ+μ+1) |
| B | 2(μ+1) | 3λ+μ+1 |
| C | 2(λ+1) | λ+3μ+1 |
| D | 2(μ+1) | λμ+2λ+2 |
| E | λ+μ+1 | λμ+λ+μ+3 |
| U | (λ+1)(μ+1) | λ+μ+3 |
| G | 2(λ+1) | λμ+2μ+2 |

**Minimality.** Current F/P separates F from P. A and E are distinguished when (λ−1)(μ−1)≠0 because their outgoing P counts differ by that product. Same versus split P groups have degrees differing by the same product. Within the two same P groups, B and C have F counts differing by 2(μ−λ). Within the three split P groups D,U,G the respective F counts are 2(μ+1), (λ+1)(μ+1), 2(λ+1). Their pairwise equalities occur only when λ=1, μ=1, or λ=μ. This gives all seven distinct groups for nonneutral unequal parameters. For equal nonneutral parameters B/C and D/G merge: five groups. If exactly one mark is neutral (parameter 1), the weights become the single-mark problem of R762CM, with three observer classes. Both neutral return the homogeneous R762CL two-class F/P chain. In every case direct row aggregation of T_adj verifies the stated coarsening, proving all-future sufficiency.

### Opposite marks: explicit three-state certificate

Take (a,b)=(01,23)=(0,5). The three permanent strongly lumpable groups are

H={012,013,024,034} F split; I={014,023} P split; J={015,025,035,045} P same.

Their exact row-transfer matrix is

\[
T_{\rm opp}=
\begin{pmatrix}
\lambda\mu+2&2&2\lambda+2\mu\\
4&\lambda\mu&2\lambda+2\mu\\
2\lambda+2\mu&\lambda+\mu&3
\end{pmatrix}.
\]

The two current P groups I and J have one-step F counts 4 and 2(λ+μ). These differ unless λ+μ=2. Under λ+μ=2, if (λ,μ)≠(1,1), their total row degrees differ by (λ−1)(μ−1)≠0. Thus every parameter except (1,1) needs three classes; at (1,1) the two P groups merge into the homogeneous two-class quotient. Strong lumpability of the displayed matrix proves the upper bound.

For a known F/P readout, the largest hidden class count is in P: 5,3,2 or 1 in the adjacent regimes, and 2 or 1 in the opposite regimes. The minimum fixed repair is respectively ceil(log2 of this hidden count), attained by an index within the known F/P class. Full named triad membership is a stronger language retaining 10 states (4 fixed bits).

## New exact joint-observer witness

At (λ,μ)=(2,3), **both** geometries have four states of weighted outdegree 18 and six states of outdegree 20, but their true F/P future quotients have **7 versus 3 states**. In this family the global BRC source-degree histogram, the marginal mark values and the F/P class counts do not determine all future F/P source counts. The relative joint K4 incidence must be retained or supplied through an exact observer-safe repair.

## Finite verification, source and remaining problem

The accompanying Python standard-library program enumerates 10 named partitions and 9 swaps per state, checks weighted symmetric transfer, group lumpability, degree formulas and one-step versus nine-step future equivalence in *both* geometries for all 169 pairs 0≤λ,μ≤12. It independently checks both symbolic quotient matrices on 81 parameter pairs and exact future count preservation for six depths. Integer arithmetic only; 7,598 assertion groups passed. The combinatorial argument and the displayed all-parameter matrices prove the theorem for all nonnegative integer λ,μ. Independent review NOT_REVIEWED.

The frozen P000 V5 signed X6 Cell torsor, all-six-axis PERP_E and three-force minimum are unchanged. The named K4 token carrier is a candidate incidence representation. The actual TRIADIC_CLOSURE_E Cell/Link/Port event predicate and V17/V29/V39 transport are the next input needed: restrict these candidate swap edges to real permitted typed events and test whether the observer equivalences survive. R762CH/CK signed path-area/provenance and even-modulus torsion data are separately retained until an exact future-observer descent theorem permits compression.
