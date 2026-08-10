# Prior art — R004 typed relation compiler

Status: `RESEARCH PRIOR-ART MAP / NOVELTY_UNVERIFIED`

This note bounds the novelty claims for Supplement 13. Generic stable-partition and weighted-bisimulation mathematics is prior art. R004's research claim is only the typed Enterprise Math compiler placement, exact finite specializations, and the operation-versus-quotient-relative-relation composition boundary.

## 1. Coalgebraic partition refinement is prior art

Wißmann, Dorsch, Milius and Schröder give generic coalgebraic partition refinement covering classical relational systems, weighted systems, deterministic automata, Markov/Segala-style systems and color refinement [SRC-WISSMANN-DORSCH-MILIUS-SCHROEDER-2018-COALGEBRAIC-REFINEMENT].

Deifel, Milius, Schröder and Wißmann specialize/refine the generic method for weighted and weighted-tree-automata settings, including cancellative and non-cancellative monoid weights [SRC-DEIFEL-MILIUS-SCHROEDER-WISSMANN-2018-WEIGHTED-REFINEMENT].

R004 therefore does not claim generic partition refinement, behavioural minimization or monoid-weighted refinement algorithms as inventions.

## 2. Weighted transition/bisimulation semantics is prior art

Miculan and Peressotti formulate weighted labelled transition systems whose transition weights are drawn from a commutative monoid and develop weighted bisimulation machinery [SRC-MICULAN-PERESSOTTI-2013-WEIGHTED-BISIMULATION].

Thus the abstraction `source -> aggregate of weights into an equivalence block` belongs to an established family of weighted-transition semantics.

## 3. Monoid-weighted balanced network partitions are direct prior art

Sequeira, Aguiar and Hespanha use matrices of commutative monoids for weighted coupled-cell networks, carry invariant synchrony/balanced-partition results to the weighted setting, and give a coarsest invariant refinement algorithm [SRC-SEQUEIRA-AGUIAR-HESPANHA-2021-MONOID-NETWORKS].

This is especially close prior art to R004's finite block-aggregate implementation. The project must not claim "commutative monoid relation compiler" as a new abstract mathematical construction.

## 4. Balanced-equivalence lattices are prior art

Kamei and Cock compute balanced equivalence relations of coupled-cell networks and describe their hierarchy as a complete lattice [SRC-KAMEI-COCK-2012-BALANCED-LATTICE].

Therefore the fact that stable/balanced equivalences form a lattice and that a stable meet may require closure/refinement rather than naive set-partition intersection is not an Enterprise Math novelty claim.

## 5. Total-operation congruence intersection is prior algebra

For a total algebra, compatible equivalence relations are congruences and arbitrary intersections of congruences are congruences. R004's `raw meet` comparison uses this standard fact and delegates the mother operation-quotient interface to A2/P023.

## 6. Project-local addition under test

R004 Supplement 13 claims only the following project-local package:

1. make relation semantics explicit types in the existing future-language compiler: MAY, witness COUNT, witness LABEL-SET, and products;
2. use monoid factor maps as exact sufficient certificates that one compiled semantic quotient refines another;
3. exhibit equal-cardinality but incomparable COUNT/LABEL-SET safe partitions, showing that scalar class count is not a complete relation-precision coordinate;
4. distinguish total-operation composition (`raw meet` of congruences) from quotient-relative relation aggregation (`stabilize raw meet`);
5. provide a three-state two-channel semantic-activation cascade and a five-state same-channel raw-meet failure, with bounded minimality checks;
6. route the generic mother mathematics to P023/A4 rather than creating a duplicate Enterprise Math foundation.

Historical novelty of this exact packaging and these selected finite witnesses remains `NOVELTY_UNVERIFIED`.
