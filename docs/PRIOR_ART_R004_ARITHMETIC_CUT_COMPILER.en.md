# Prior art — R004 arithmetic cut compiler

Status: `RESEARCH PRIOR-ART MAP / NOVELTY_UNVERIFIED`

Supplement 18 identifies carrier cuts in one weighted binary future-language family with support-minimal failures of subset-sum distinctness. The dissociated-set/subset-sum theory itself is established additive combinatorics.

## 1. Dissociated / subset-sum-distinct sets are prior art

Dutta defines a set of positive integers as subset-sum-distinct / dissociated when all finite subsets have distinct sums, and gives the equivalent condition that every relation with coefficients in `{-1,0,+1}` is trivial [SRC-DUTTA-2026-DISSOCIATED-GREEDY].

Mendoza-Smith and Tanner use the same operational condition in sparse recovery: a signal is dissociated when all `2^k` subset sums of its support are pairwise different [SRC-MENDOZA-SMITH-TANNER-2015-DISSOCIATED].

Older additive-combinatorics work also studies sumsets of dissociated sets [SRC-SHKREDOV-2007-DISSOCIATED-SUMSETS].

R004 therefore does not claim the notion of a dissociated set, distinct subset sums, or the `{-1,0,1}` relation characterization as new mathematics.

## 2. Project-local bridge under test

R004 Supplement 18 claims only this specialization:

1. exact binary state `x in {0,1}^d`;
2. current observation `L_a(x)=sum_i a_i x_i` with nonzero integer weights;
3. future generators are coordinate bit flips;
4. retained flip set `S` has exact safe quotient `q_S=(L_a,x|_S)`;
5. deleted coordinate set `H` breaks the full carrier iff the hidden weight subfamily on `H` is non-dissociated;
6. minimal carrier cuts are exactly support-minimal nontrivial `{-1,0,1}` relations among the observation weights.

The novelty claim, if any, is therefore the future-safe compiler reduction and its obstruction-cut interpretation, not additive-combinatorics dissociativity itself.

Historical novelty remains `NOVELTY_UNVERIFIED`.
