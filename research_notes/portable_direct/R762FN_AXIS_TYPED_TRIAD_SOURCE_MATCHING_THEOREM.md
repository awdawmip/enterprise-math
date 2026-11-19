# R762FN — Axis-typed X6 triad source matching: exact BRC observer fibers and minimal repair memory

Date: 2026-11-19 (Asia/Shanghai). Independent portable continuation of RS-X6-TRIADIC-CLOSURE-DYNAMICS. Mother-task frozen book: awdawmip/enterprise-math@857280d1012943290d141d1317179c40ec3cbdf8:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md. Frozen P000/X6 definitions: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Prior result R762FM in PR #2778, commit 356e3ee52a83270f39db13397cf941db4456ced1. Author-side proof and exhaustive checker k=1..5 PASS; independent review NOT_REVIEWED.

## Mathematical population and future operations

Fix one native X6 Cell c and three distinct signed *native axes* u,v,w from the existing six-axis affine torsor. On each of the three axes place k source-distinct equal-positive-quanta force tokens with positive direction: A_1,...,A_k on +E_u; B_1,...,B_k on +E_v; C_1,...,C_k on +E_w. For each k>=1 a candidate *triad incidence event* uses exactly one A, one B and one C token, all at c, and has incidence tag omega=+1, as in the R762FM candidate closure predicate. An incidence history is a set of k unordered such triads covering each original source token exactly once. Original legs, source names, multiplicities and signs are retained as named positive BRC branches.

Coarse observer O records the full labelled multiset of original primitive Cell legs, their signs and weights and the Cell, but *forgets which three tokens participate together in a triad event*. Thus O has the same output for every history of this stated population. Future operation Q_i asks for the two named source IDs B_j,C_l that share a triad with A_i; Q_I means these queries together for a declared subset I of the A labels.

This is a **typed candidate incidence model** compatible with P000 source/direction arity and the X6 coordinate carrier. It does not claim that its incidence rule has already been admitted as the native TRIADIC_CLOSURE_E Cell/Link/Port operation. The selected triple of X6 axes is a coordinate sub-selection, not a newly invented native three-dimensional world or an automatically realized FCC carrier slice.

## Theorem 1. Exact source family and full-reconstruction optimum

For every integer k>=1 the full grouping fiber above O contains exactly

    N(k) = (k!)^2

histories. The smallest possible deterministic fixed-length *additional grouping* code that preserves all Q_i contains

    b(k) = ceil(log_2((k!)^2))

bits, and a matching codec exists.

Proof. Every A_i belongs to one event with uniquely specified B_{sigma(i)} and C_{tau(i)}. Since all B and C tokens occur exactly once, sigma and tau are permutations of {1,...,k}. Conversely any (sigma,tau) in S_k x S_k defines precisely one unordered event set { (A_i,B_{sigma(i)},C_{tau(i)}) : i=1,...,k }. Distinct pairs yield distinct groupings but identical O outputs, so N(k)=(k!)^2. The combined outputs of all Q_i recover both permutations. Pigeonhole gives the lower bound. Rank sigma and tau lexicographically in {0,...,k!-1}; the integer k!*rank(sigma)+rank(tau) encodes the grouping in b(k) bits, and unranking recovers every event and future Q_i. QED.

The code size concerns *additional grouping state relative to the declared coarse O*, not storage of all tokens, source names, addresses, native coordinates or physical timing.

## Theorem 2. Exact limited-observer fibers

For any predeclared subset I of t distinct A labels, 0<=t<=k, the observer Q_I has exactly

    A(k,t) = (k!/(k-t)!)^2

distinct outputs, each of which has exactly

    F(k,t) = ((k-t)!)^2

compatible full histories. Therefore the sharp fixed-length grouping memory to support precisely Q_I is

    b(k,t) = ceil(log_2 A(k,t)) bits.

Proof. Answers for the t selected A labels choose an ordered injection into B tokens, in (k)_t=k!/(k-t)! ways, and independently an ordered injection into C tokens, also in (k)_t ways. The two remaining bijections from the k-t unused A labels to unused B and C labels may be completed in (k-t)! ways each. Each answer thus has exactly F(k,t) preimages, and all A(k,t) answers are attained. The information lower bound is the count of distinct outputs; an enumerative rank of two partial injections provides the corresponding upper bound. QED.

The residual hidden after Q_I consists exactly of a pair of permutations of the unqueried B/C partner labels; this is a source-typed repair coordinate, not an unspecified numerical error.

## Corollary. Exact query threshold

For k>=2, k-1 distinct A-token partner queries suffice to reconstruct *all* events, because the final unmatched B and C labels must partner with the remaining A. For any t<=k-2, each observation leaves at least (2!)^2=4 possible histories, so fewer than k-1 queries cannot reconstruct the full grouping in the worst case. This threshold holds for predetermined or adaptive A-token queries in this exact source population. For k=1 no query is required.

Theorem 2 gives an exact criterion for safely collapsing part of the source state: when the declared future interface is only Q_I, keep one of A(k,t) state codes and quotient precisely the F(k,t)-element fibers. Any later Q_j with j outside I requires retaining or recovering the missing relation information.

## Exact small cases

| k | source tokens | histories N(k) | full bits b(k) | one-A answer count / bits | full query threshold |
|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 1 | 0 | 1 / 0 | 0 |
| 2 | 6 | 4 | 2 | 4 / 2 | 1 |
| 3 | 9 | 36 | 6 | 9 / 4 | 2 |
| 4 | 12 | 576 | 10 | 16 / 4 | 3 |
| 5 | 15 | 14,400 | 14 | 25 / 5 | 4 |

For k=3, Q_1 leaves exactly four compatible groupings, while (Q_1,Q_2) distinguishes all 36. For k=4, (Q_1,Q_2) has 144 possible answers (8 bits), each with four compatible full groupings; Q_1,Q_2,Q_3 distinguish all 576 (10 bits).

This *does not contradict* R762FM's six-distinct-axis result of 10 source histories and four bits. R762FM used six tokens on six distinct native axes, whereas k=2 here uses two source-distinct tokens on each of three native axes, and every triad must select one from each axis. Without the axis-typing constraint, counting all partitions of 3k tokens would incorrectly overcount this X6 candidate family.

## Positive BRC observation and covariance

The exact path-formal positive source family is the sum over (sigma,tau) in S_k x S_k of separately named unit-weight branch elements [b_{sigma,tau}]. Under O all branches map to one common labelled-leg observation with total coefficient (k!)^2. Such positive recoalescence preserves total multiplicity, but not the grouping relations needed by Q_i. Nothing here converts positive BRC weight into signed-amplitude cancellation.

Permuting the six native positive axis labels by the established S6 skeleton transports the chosen three axes, Cell legs, source identities and grouped triads bijectively; every Q_i commutes with this relabelling. The conditional signed W6 candidate of R762FM likewise preserves the grouping counts *if* each sign reversal transports the incidence tag omega together with the relevant leg signs. This is only a covariance test, not admission of signed reversals as native rotations.

A naive lexicographic permutation rank/unrank uses O(k^2) selection steps, and data structures such as a Fenwick tree can improve selection work; integer bit-operation costs and base source-label storage are additional. The theorem is an exact *representation and future-query* bound, not a global execution-speed claim.

## Verification, evidence and next question

R762FN_VERIFY.mjs exhaustively enumerates every ordered permutation pair for k=1..5, including 15,017 distinct grouping histories. For each t=0..k it checks exact output cardinality A(k,t), exact equal fiber size F(k,t), mass identity A*F=N, and reconstruction from the first k-1 A queries. The raw machine result is R762FN_EVIDENCE.json; all checks PASS. Symbolic proofs above cover all integers k>=1; independent mathematical review remains NOT_REVIEWED.

The central open issue in the mother task is the legal *native* Cell/Link/Port admission predicate and update composition. Next: obtain the exact native licensed triad rule, apply it to these source-distinct candidate histories, count its surviving fibers and check whether Q_I commutes with consecutive event updates and actual licensed rotations. A separate extension would add time order and Cell-dependent incidence, which can require more state than the present unordered single-Cell model. Preserve the frozen P000/taskbook sources and R762FM provenance; do not claim a new CLAIM, PROGRESS, Result or Review through this portable note.
