# BRC-X6：二阶矩完全相同、最少八项的连续保真策略族

Status: AUTHOR_PROVED / EXACT_INTEGER_AND_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED. Researcher-side portable mathematics; not a native Source Result, CLAIM, independent review or Foundation promotion. Frozen scientific input pin: f42f2906d77f24085c123f3ccfe9667d41caa96d. Original 96 ports, six labeled actions, nine frozen roots, full next-port and seven-component reward observer (R1,...,R6,K). Source ports are (6,7,28,29), with signed coefficients (+,-,-,+).

## Theorem A: source-row multiset-overlap lower bound

For a four-source stochastic policy x, suppose all six action masses at each source are strictly positive. Let x be a convex combination of m>0 native preserving deterministic action quadruples, with m positive coefficients w_1,...,w_m. For sources p,q, let I_pq be the multiset intersection cardinality of their six action probabilities, counting repeated equal values with multiplicity.

Then m>=6 and I_pq >= max(0,24-3m). In particular I_pq<=2 certifies that m>=8.

Proof: At each source, the m indexed convex weights are partitioned among six nonempty action groups. If k groups contain at least two weight indices, m>=6+k, hence k<=m-6. At most m-6+k<=2(m-6) indices belong to nonsingleton groups. For two sources, at least m-4(m-6)=24-3m indices are singleton at both sources. Each such index contributes an equal individual weight to one separate action coordinate of each source. Even when numerical weights repeat, matching these indexed weights injectively gives at least that many entries in the multiset intersection. Negative lower bounds are replaced by zero. This proves the assertion for arbitrary positive convex weights and any set of deterministic four-source policies.

## Theorem B: a continuous sharp eight-term family invisible to M2 differences

The following eight original action tuples are each preserving for every frozen root in the signed full joint output and next-port atom dictionary:

v0=(5,5,0,0), v1=(5,5,4,4), v2=(1,1,3,3), v3=(0,0,2,2),
v4=(2,2,5,5), v5=(3,3,1,1), v6=(4,4,1,1), v7=(0,0,5,5).

For every real s>=2, take convex coefficients proportional to

(1,1,1,2s-1,s,1,s,1), with total mass S=4s+4.

The four exact source-row probability vectors of their mixture are (A,A,B,B), where

A=(2s,1,s,1,s,2)/S,
B=(1,s+1,2s-1,1,1,s+1)/S.

All 24 action masses are positive. Each row has sum 1 and identical second marginal moment

M2 = 6(s²+1)/S² = 3(s²+1)/(8(s+1)²).

The two multisets of unnormalized values share exactly two elements: the two copies of 1. Indeed A's remaining multiset is {2,s,s,2s}, and B's is {s+1,s+1,2s-1}; for every real s>=2 they are disjoint. Consequently I(A,B)=2, and Theorem A excludes every preserving convex representation of at most seven deterministic policies. The displayed eight valid policies realize the upper bound. Therefore

minSupport(x_s)=8 for every real s>=2.

This is an unbounded continuous parameter family. Rational s gives exact rational certificates. Its first moments and all four marginal second moments agree; the complete source-action multiplicity observer distinguishes a decomposition obstruction that the second-moment difference test misses.

### Small rational example

s=2 yields eight positive coefficient numerators (1,1,1,3,2,1,2,1), denominator 12. The six action probability numerators are

at ports 6 and 7: (4,1,2,1,2,2);
at ports 28 and 29: (1,3,3,1,1,3).

Both rows have squared numerator sum 30, hence M2=30/144=5/24, but their numerical multiset intersection contains only the two copies of 1/12. The exact minimum is eight.

## Evidence and verification

Original fixed-source kernel frozen_native_kernel_prefix577.py has SHA-256 d2b84a22928e8160315e8578ea99a62f91b8688462d2b6451a71eef871df88b0. The new author-side verifier verify_eight_family.py checks all eight action tuples against the full signed (next_port,R1,...,R6,K) integer atom dictionary for each of nine roots, selected rational parameters with exact fractions, and the row formula for integers 2..199. A second implementation independently enumerates all 6^4=1296 possible pure actions for each root, recovers 38 preserving actions, and checks the eight witnesses, four rational parameters and complete signed output. Both programs pass. The proof for all real s>=2 is the algebraic argument above, not an extrapolation of finite tests.

Observer and operations: retain original source ports, labeled actions, full reward and successor port; deterministic policies are valid exactly when the four signed original output atoms cancel. The convex mixture preserves that declared observer by linearity. No quotient of branch provenance or signed atoms is used.

Theorem contributes to the earlier BRC-X6 38-vertex signed-policy polytope, previously proved uniform minimum six and an explicit minimum-seven example. Next mathematical question: use the multiset overlap lower bound as a cheap certificate/pruning step in a general rational minimum-support solver, then seek higher-order/combined-source certificates for exact minima nine and above.

Parent Source D25 native original-class H0/B0, Frobenius, kappa/Delta-R and CM experiment remain unfinished under their own ownership and execution rights; UR V2 four-file original provenance still requires 94687-byte SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76. This author's portable result has no Source CLAIM or review admission.
