# Prior art — R004 typed generator basis

Status: `RESEARCH PRIOR-ART MAP / NOVELTY_UNVERIFIED`

Supplement 15 studies a task-relative generator-basis problem after the full typed Representation Compiler has already produced a target safe carrier. Generic minimum generating sets, semigroup rank, hitting set/set cover, term generation and semiring generation are prior mathematics.

## 1. Finite semigroup rank and minimum generating sets are prior art

Gray studies the minimal number of generators of finite semigroups and applies the theory to natural transformation-semigroup families [SRC-GRAY-2013-FINITE-SEMIGROUP-RANK].

Araújo, Bentz, Mitchell and Schneider determine the rank/minimum generating-set size for transformation semigroups stabilising a finite partition [SRC-ARAUJO-BENTZ-MITCHELL-SCHNEIDER-2014-PARTITION-SEMIGROUP-RANK].

R004 therefore does not claim the notion of a minimum transformation generating set, semigroup rank, or partition-stabilising transformation semigroup as new.

## 2. Hitting set and algebraic generation are generic priors

The reduction “choose a minimum subset of generators that hits every forbidden object” is a direct finite hitting-set/set-cover formulation. Generic exact/approximate algorithms and complexity theory for hitting set are established combinatorics/computer science and are not novelty claims here.

Likewise, checking whether a quotient operation lies in a generated transformation monoid, or whether a relation matrix lies in a generated semiring subalgebra, is ordinary algebraic generation. Supplement 15 only uses those mature notions as reconstruction certificates inside the Enterprise Math compiler.

## 3. Project-local additions under test

R004 claims only the following integrated finite package:

1. after full compilation to `Q*`, characterize carrier-preserving generator subsets by hitting every strictly coarser forbidden partition between `Q*` and the initial observation;
2. show local pairwise merge tests are insufficient, so activation-aware basis synthesis is globally partition-structural;
3. distinguish carrier bases from semantic reconstruction bases;
4. prove a coarsening-natural reconstruction criterion: quotient-level reconstructibility of omitted typed generators implies their carrier redundancy;
5. specialize that criterion to unary operation-term/transformation-monoid generation, semiring relation generation and semantic factor maps;
6. provide exact integer inclusion-minimal/private-world and generator-disjoint packing certificates;
7. preserve the prior R004 rule that class/basis cardinalities are derived statistics, not complete typed-precision coordinates.

Historical novelty of this exact Enterprise Math placement and selected finite reduction/counterexample package remains `NOVELTY_UNVERIFIED`.
