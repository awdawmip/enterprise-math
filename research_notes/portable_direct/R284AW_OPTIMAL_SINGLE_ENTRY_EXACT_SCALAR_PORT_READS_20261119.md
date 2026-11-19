# R284AW — n−1 exact scalar readings are sufficient and (on the stated classes) optimal

Date: 2026-11-19. Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.
Source lineage: R284AT spanning-tree formal Port observation and R284AU-PACK bounded-height scalar encoding (source blob b35245c3a39e67069f8be192d970dfb61427b1bd).
Frozen scientific baseline: R284AT source pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Object: auxiliary independently named Port-channel determinant observers, not native X6 heartbeat dynamics. All signed cofactor and joint-path coefficients retain names and direction. Neither P000 nor frozen inputs change.

## Exact measurement model

Fix integers n>=2 and H>=1. An unknown matrix C=(c_ij) has all entries in {1,...,H}, and H is known to the observer. One scalar measurement consists of a freely programmable nonnegative integer diagonal D, a single ordered off-diagonal entry (u,v), and a nonnegative integer strength z, producing the **exact integer** det(D-C-zE_uv). One diagonal-only reading may be allowed but also costs one read. All input and output bits count, and adaptive choice is permitted.

## AW1 (constructive n−1 upper bound)

For every n>=2,H>=1, exactly n−1 individually edited **scalar** determinant readings suffice to reconstruct C entrywise, using only polynomially many input/output bits and polynomial-time exact integer arithmetic. The scheme is nonadaptive. This improves the n scalar readings of R284AU-PACK by encoding the formerly separate baseline into the first edited reading.

### Proof

Set F(d)=det(diag(d)-C) and G_v(d)=det(diag(d)-C-E_{0v})-F(d), v=1,...,n−1. Linearity of the determinant in one matrix entry gives
det(diag(d)-C-zE_{0v})=F(d)+z G_v(d).

Use the positive 3-separating weights w_0,...,w_{n−1} constructed in R284AU-PACK §AU2. For k=1,2,3, all distinct k-subsets have distinct sums of w_i, and w_i=O(n^6). Put W=1+sum_i w_i and e(S)=|S|W+sum_{i∈S}w_i. Because W exceeds the total weight, the different subset cardinalities occupy disjoint exponent bands. Among the complements of cardinality 1,2,3 all monomials have distinct e(S). Let E=e([n]), A=2^n n! H^n, choose a power of two B>2A, set D_i=B^(W+w_i), and R=E+1.

Every multiaffine coefficient of F or G_v is an integer of magnitude <=n!H^n. Even if some irrelevant monomials collide after diagonal substitution, the resulting aggregate coefficient at each exponent has magnitude <=A<B/2. Thus F(D) and each G_v(D) admit unambiguous **balanced signed base-B expansions**, with exponents in [0,E]. All signs and named high-degree coefficients are preserved.

Make precisely the following measurements:
(1) y_1=det(D-C-B^R E_{0,1});
(2) y_v=det(D-C-E_{0,v}) for v=2,...,n−1.
There are n−1 readings (one if n=2). The first reading is y_1=F(D)+B^R G_1(D). Since the low and high exponent supports [0,E] and [R,R+E] are disjoint and individual coefficients are <B/2 in absolute value, the balanced-base expansion separates the entire F(D) digit sequence from the shifted G_1(D) sequence. Reconstruct y_0=F(D) from low digits **without an additional observation**, and recover G_1(D) from the high digits. For v>=2, y_v-y_0=G_v(D), so all G_v(D) follow.

For each named subset T with |T|<=3, write f_T for the coefficient of ∏_{i∉T}d_i in F and g_{v,T} for that coefficient in G_v. The 3-separating property recovers all the required f_T,g_{v,T} as exactly one balanced digit of the relevant substituted polynomial. Determinant/cofactor expansion gives:
a_i := c_ii = −f_{ {i} };
p_ij := c_ij c_ji = a_i a_j − f_{ {i,j} };
c_{v0} = −g_{v,{0,v}};
c_{0v} = p_{0v}/c_{v0};
c_{ij} = (a_j c_{i0} − g_{i,{0,i,j}})/c_{j0} for 1<=i<j<n;
c_{ji}=p_ij/c_ij.
These are R284AT's exact pair/path identities. Every divisor is strictly positive, so the reconstruction is defined and unique.

For bit complexity: w_i=O(n^6), sum w_i=O(n^7), E=O(n^8), log_2 B=O(n(log n+log(H+1))), and R=E+1. The diagonal entries, first edit strength, and scalar outputs have at most O(n^9(log n+log(H+1))) bits (conservative). Generating weights, exact integer determinants by Bareiss, centered-digit extraction, and divisions use polynomial bit complexity. QED.

## AW2 (matching lower bounds; distinguish the finite-domain cases)

(i) For every H>=2 and n>=2, **any nonadaptive** scheme with fewer than n−1 single-entry measurements fails to identify every matrix in {1,...,H}^{n×n}.

(ii) For every H>=4 and n>=2, **any deterministic adaptive** scheme with fewer than n−1 single-entry measurements fails on that same bounded integer class. Thus n−1 is the exact adaptive optimum for H>=4.

(iii) On the class of strictly positive rational matrices (no fixed height bound), even adaptive single-entry determinant measurements require at least n−1 readings.

### Lower-bound proof

Given any transcript with q<n−1 readings, form the undirected graph G of its q queried off-diagonal edges. G is disconnected. Choose a nonconstant positive diagonal T=diag(t_i) constant on each component. Since T commutes with D and also with every queried E_uv (because t_u=t_v),
det(D-TCT^(−1)-zE_uv)
=det(T^(−1)(D-TCT^(−1)-zE_uv)T)
=det(D-C-zE_uv)
for every diagonal D, strength z and sampled edge (u,v). All signed measurements coincide.

For (i), take any componentwise t_i∈{1,2} using both values. Choose positive integer entries C_ij=1 when t_i=2,t_j=1; C_ij=2 when t_i=1,t_j=2; and C_ij=1 otherwise. The distinct matrix C'=TCT^(−1) also has all entries in {1,2}. Hence every fixed scheme with q<n−1 has an indistinguishable pair already at H=2.

For (ii), run the proposed adaptive scheme on the **fixed** matrix C=2J (all entries 2). Its realized graph after q<n−1 queries is disconnected. Set t_i=2 on one proper union of its components and t_i=1 elsewhere. Then C'=TCT^(−1) has entries in {1,2,4}, is distinct from C, and is valid for every H>=4. By induction, each answer on C' equals the corresponding answer on C; therefore the deterministic adaptive scheme issues the same next query and remains unable to distinguish them. This proves the adaptive claim.

For (iii), perform the same transcript-based argument on an all-ones positive rational matrix using any nontrivial rational componentwise scaling T. It remains within the positive rational class and generates an indistinguishable adaptive transcript. QED.

The singleton alphabet H=1 has a known matrix and requires zero readings. For the bounded integer adaptive cases H=2,3, the upper bound remains n−1 while a matching general adaptive lower bound is left open. The bound applies to an instrument changing **at most one** off-diagonal entry per scalar reading; simultaneous edits are a different measurement model.

## Reproduction and exact finite evidence

Companion script: R284AW_single_entry_scalar_optimal_checker.py. Companion result: R284AW_single_entry_scalar_optimal_verification.json. Use Python standard-library exact integers and Bareiss fraction-free determinants. Seed: 2842719.

Completed checks: 590/590 matrix reconstructions, comprising 78 seeded positive integer instances of n=2,...,6 and **all 512** positive 3×3 binary matrices. Additionally, 75 exact comparisons tested disconnected-support indistinguishability witnesses at sizes n=3,...,7, with varied diagonal settings and edited strengths. Every test passed. Maximum observed diagonal bit length 1393; maximum observed scalar response bit length 11718. Finite tests check the implementation on this stated domain; the universal claims are proved above. No independent mathematical review is recorded.

## Next research questions

1. Settle the adaptive single-entry lower bound for the remaining integer alphabets H=2,3, or construct exact counterexamples.
2. Improve the **total transmitted bits and instrument dynamic range** at exactly n−1 scalar readings; benchmark against R284AU-PACK and the differently scoped R284AV readout design.
3. If simultaneous independently weighted star edits are explicitly allowed in one scalar reading, encode all cofactor channels in disjoint digit blocks and test the resulting one-reading construction as a separate scoped observation theorem, including noise sensitivity.

Provenance status: independent portable scientific artifact; no new formal CLAIM, no result freeze or independent review asserted.