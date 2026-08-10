# Prior art — R004 joint witness coupling / marginalization gate

Status: `RESEARCH PRIOR-ART MAP / NOVELTY_UNVERIFIED`

Supplement 30 must not be read as claiming relational projection, multivalued dependencies, lossless joins, or contingency-table coupling ambiguity as new mathematics.

## 1. Relational projection and lossless reconstruction are prior art

Ronald Fagin's 1977 work on multivalued dependencies and fourth normal form is a classical source for dependencies under which a relation can be decomposed into projections and recovered without information loss by joins [SRC-R004-JWC-FAGIN-1977]. The two-target Boolean rectangularity/lossless-marginalization gate used here is a very small finite specialization of this broad database-theory lineage.

## 2. Weighted/count marginals and joint tables are prior structures

Contingency tables, marginal sums and the fact that margins generally do not determine the joint table are standard combinatorics/statistics. R004 does not claim generic marginal ambiguity.

## 3. Project-local addition under test

R004 Supplement 30 only claims the following compiler placement:

1. common fine witnesses for several target channels must first form a typed **joint weighted coupling** on the product target;
2. marginals are exact pushforwards and hence safe erasures when the remaining future uses only marginal semantics;
3. coupled future predicates witness that joint coupling remains live;
4. MAY rectangularity/lossless join is an explicit reconstruction certificate, not something inferred from nontrivial marginals after coupling has been erased;
5. the joint-coupling table itself becomes another certificate carrier subject to the existing backward future-safe quotient/liveness compiler.

Historical novelty of this exact Enterprise Math packaging remains `NOVELTY_UNVERIFIED`.
