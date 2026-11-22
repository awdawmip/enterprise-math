# R5 | exact second-threshold period at O(N) precision

Date: 2026-11-22. Scientific status: **AUTHOR_EXACT_PROOF / EXACT_INTEGER_CROSSCHECKED / NOT_REVIEWED**. Independent portable-research result, not an authenticated Task CLAIM, Result, Review or Foundation theorem.

Frozen scientific provenance: original true-event correction at enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15; predecessor m=1 theorem at enterprise-math@c27732cc27700ab4e65268acdf4a285cbdf910f6, research_notes/portable_direct/r5_m1_o1_exact_period_20261122/RESEARCH.md. Frozen model and event supports unchanged; the m=2 proof has its own witness computations.

## New exact theorem

Let a_p be nonnegative integers indexed by p=214,...,314, with total cost N=sum(p a_p). The frozen supports are

- S0={214,215,216,217,218};
- S1={214,216,217,218,219,220,221};
- S2={215,216,217,218,219,220,221};
- S3={223,...,290};
- S4={296,...,312}.

Define f_2(N) to count assignments of total cost N satisfying **at least one** event E_i: sum_{p in S_i} a_p < 2. Let M_2(O(N)) be the least common coefficient period of the quasipolynomial terms of degree >= 2, i.e. modulo a remainder O(N). Then

\[
\boxed{M_2(O(N))=229\,746\,052\,653\,717\,600.}
\]

Thus raising the failure threshold from m=1 to m=2 does not shrink the sharp period at this precision.

## Exact intersection generating functions (overlap preserved)

For each nonempty set I of events, write U_I=union_{i in I} S_i. For each p in U_I, define \sigma_I(p)={i in I : p in S_i}; this is the **exact joint-event membership signature**. For every nonempty B subset of I define

\[
h_{I,B}(q)=\sum_{\substack{p\in U_I\\\sigma_I(p)=B}}q^p.
\]

Let \Pi(H) denote the set partitions of the labeled set H. The polynomial enumerating the bounded variables on U_I under simultaneous conditions E_i, i in I, is precisely

\[
Q_{I,2}(q)=\sum_{H\subseteq I}\sum_{\pi\in\Pi(H)}
          \prod_{B\in\pi}h_{I,B}(q).
\]

The empty partition contributes 1. **Proof:** Each E_i permits at most one selected item among all prices in S_i. Hence every selected price p has a_p=1, and the nonempty signatures of selected prices are pairwise disjoint. They partition the exact activated-event set H; conversely, one price of exact signature B for each block in a partition gives exactly one admissible assignment. This bijection preserves all overlaps (including E0/E1/E2) and each monomial's total cost.

For D(q)=prod_{p=214}^{314}(1-q^p), exact inclusion-exclusion gives

\[
F_2(q)=\sum_{N\ge0}f_2(N)q^N
      ={R_2(q)\over D(q)},\qquad
R_2(q)=\sum_{\emptyset\ne I\subseteq\{0,1,2,3,4\}}
(-1)^{|I|+1}Q_{I,2}(q)\prod_{p\in U_I}(1-q^p).
\]

This is a polynomial numerator with all event intersections represented faithfully.

## Matching upper and lower bounds

At a primitive d-th root of unity, d>=2, D has zero order n_d=# {p in [214,314]:d divides p}. A pole contributing to degree >=2 must have order >=3. Enumeration gives exactly 39 candidate d with n_d>=3:

2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,43,44.

Their lcm is L=229746052653717600; all other d give at most O(N), so M_2(O(N)) divides L.

For each row below, expand R_2(zeta_d(1+t)) at a primitive d-th root. The two independently constructed full integer vectors (occupancy-bit DP and exact-signature set-partition sum) agree after reduction modulo Phi_d. The first nonzero coefficient is t^j; the table displays its first nonzero power-basis coordinate (zero-based). For d=7,9,27,31 the t^0 vector is identically zero.

| d | n_d | j | surviving pole | coordinate | exact coefficient |
|---:|---:|---:|---:|---:|---:|
| 7 | 14 | 1 | 13 | 0 | 2387 |
| 9 | 11 | 1 | 10 | 0 | 648 |
| 11 | 9 | 0 | 9 | 0 | 3 |
| 13 | 8 | 0 | 8 | 0 | 1 |
| 17 | 6 | 0 | 6 | 0 | 4 |
| 19 | 5 | 0 | 5 | 0 | -4 |
| 23 | 4 | 0 | 4 | 0 | -2 |
| 25 | 4 | 0 | 4 | 0 | 3 |
| 27 | 4 | 1 | 3 | 0 | -2646 |
| 29 | 3 | 0 | 3 | 0 | -164042 |
| 31 | 4 | 1 | 3 | 0 | 713 |
| 32 | 3 | 0 | 3 | 0 | -682804 |
| 37 | 3 | 0 | 3 | 0 | -3 |
| 43 | 3 | 0 | 3 | 1 | -1 |

Each coefficient is a nonzero exact algebraic integer; its pole order n_d-j is >=3. By partial fractions, any period T of the degree >=2 quasipolynomial must be divisible by every such d: a primitive d-frequency of polynomial growth at least N^2 cannot be absorbed into O(N) nor expressed by frequencies of orders dividing T when d does not divide T. The 14 orders' lcm equals L, proving L divides M_2(O(N)). Together with the upper bound this proves equality.

## Reproduction and scope

Run Python 3 standard library: python3 VERIFY_R5_M2_O1.py. The program independently constructs all 31 event intersections by (A) bitmask occupation dynamic programming and (B) the labeled set-partition identity, evaluates exact zero- and first-order jets in Z[q]/(q^d-1), compares **entire** cyclotomic-reduced vectors at all 14 witness orders, checks the 39-order ceiling and witness lcm, and emits R5_M2_O1_CERTIFICATE_FULL.json. Expected terminal output ends ALL CHECKS PASS. All arithmetic is integral, with no floating approximation.

Author execution on 2026-11-22: ALL CHECKS PASS, including full-vector independent comparison at 14 root orders. Local script SHA256 e762b9609eec9df7b8f9e9851d462570db5fac7866a2d7f967cd6a806c7d6564, full generated JSON SHA256 b0d8c7ac143af4774089cb3fc2211b67c7e62a082fd1f61baf82d695d1f7a9d5. Separate project independent mathematical review: NOT_REVIEWED.

The signed cyclotomic residue/jet carrier preserves cancellation; positive-only BRC mass is insufficient for the t^0 / t^1 distinction. This is a frozen scalar partition-counting readout, with no claim that native X6 dynamics were proved or P000 changed.

## Next scientific frontier

Investigate m>=3 with exact simultaneous event capacities m-1 using a five-counter DP or signature partition generating functions. Test whether L persists and classify real phase-dependent cancellations. Seek independent review of the m=1 and m=2 O(N) proofs.

## Control provenance

The bounded native owner request r5-20261122-0843-owner-onebounded-v1 concluded FAILED / SOURCE_TREE_TRUNCATED. Current owner and live CLAIM were therefore unverified. This independent GitHub portable artifact asserts no formal CLAIM/RUN, Activity mutation, Result freeze, or mathematical review. Original authorship and immutable scientific pins remain preserved.
