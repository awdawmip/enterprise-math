# R762ID — Fifteen-mask Port obstruction certificate and bounded constructive signing

Date: 2026-11-21. Status: AUTHOR_PROVED / EXACT_FINITE_CERTIFICATE_CHECKED / NOT_REVIEWED.
Research lineage: R762IB@a3b465e76af541de223fcf7773477fbd224be8b4 and R762IC@40945d2ccef1d6d691ba88a85930e9d9276c9123. Frozen scientific input: RS-X6-TRIADIC-CLOSURE-DYNAMICS, science pin a72226e2430ffa4786321ac86e7f0c599d5f0389. This is a six-axis **composite Port/support/sign observer** theorem, not native P000 TRIADIC_CLOSURE_E.

## Result

Let T be the 20 unordered triples of X={0,...,5}, and let h_S be the 0/1 incidence vector of S in Z^6. A Port is a two-subset; a transition between two Ports sharing one axis has support their three-axis union. For any histogram n=(n_S) of named occurrences, write n_S=delta_S+2q_S, delta_S in {0,1}, and Q={S:q_S>=1}. Let H_i=sum_{S contains i} n_S. Let C(n)>0 mean that per-occurrence signs can be chosen with sum epsilon_t h_{S_t}=0. Let N_p(n)>0 mean that the named events admit a legal closed Port circuit starting and ending at p.

**Compact signability certificate:** If every H_i is even and the odd core delta is one of the three nonsignable S6-orbits in R762IB, then for each representative there is a finite list of maximal nonsignable Q-masks B. Precisely,

    C(delta+2*1_Q)=0  <=>  Q is contained in at least one B.

In lexicographic order T=binom({0,...,5},3), the 20-bit hexadecimal B masks are:

| Odd-core representative | Maximal bad B (hex) | Count |
|---|---|---:|
| 024,035,125,134 | 13301 19122 23222 2a121 42528 43114 5b525 63339 81524 83038 93336 ab52a | 12 |
| 012,015,025,034,123,124 | 6ccc9 80cc8 | 2 |
| 012,013,014,025,035,045,125,135,145,234 | 1d347 | 1 |

The inclusion-minimal signable sets Q form the hypergraph transversals of {T\B}. Their size distributions are:

| Odd-core size | Maximal bad B | Nonsignable Q | Minimal good Q | Sizes of minimal good Q |
|---:|---:|---:|---:|---|
| 4 | 12 | 3,824 | 48 | 4 of size 1, 12 of size 2, 24 of size 3, 8 of size 4 |
| 6 | 2 | 1,056 | 14 | 9 of size 1, 5 of size 2 |
| 10 | 1 | 1,024 | 10 | 10 of size 1 |

Thus any signable extension of a bad core has a signable subhistogram delta+2*1_U with U subset of Q and |U|<=4 (<=2 for six-event cores, <=1 for ten-event cores). The bound four is attained by inclusion-minimal signable Q in the unrestricted histogram class. For a bad core there are at most 12 occurrences in this essential signing template; the rest are assigned cancelling sign pairs.

**Compressed Port no-go certificate:** Of the 15 maximal bad masks, the four-core row has 8 with impossible even Port degree and 4 with core supports stranded in distinct components of the two-axis-overlap graph. The six-core row has 2 with separated core components; the ten-core row has 1. Consequently, no bad Q subset of any B can support a legal Port Euler circuit. Combined with the three-core completeness statement of R762IB, this yields a second, shorter certificate for the R762IC sufficiency implication:

    N_p(n)>0 and all H_i even  ==>  C(n)>0.

## Why the finite certificate proves all multiplicities

1. **One-way pair reduction.** If delta+2*1_Q is signable, all larger n with that delta and presence set Q are signable: assign cancelling (+,-) signs to every extra pair. Thus C(n)=0 implies C(delta+2*1_Q)=0. All six coordinate parities are unchanged.
2. **Exact finite sign test.** For each odd core, enumerate the vector targets A_delta={-sum_S epsilon_S h_S/2}, where epsilon_S in {+1,-1}. For a pair-presence set Q, compute R_Q={sum_{S in Q} z_S h_S : z_S in {-1,0,+1}}. Then C(delta+2*1_Q)>0 iff A_delta intersects R_Q. Integer six-tuples (no floats) verify every listed B is nonsignable and every derived minimal good U is signable. Proper immediate subsets of every minimal good U are nonsignable.
3. **Combinatorial coverage without assuming a result.** For a finite universe, a set Q is not contained in any B exactly when it hits every complement T\B. Every such Q contains an inclusion-minimal transversal U. Enumerating these transversals gives the stated 48+14+10 positive templates, and the checker independently compares both classifications across all 3*2^20 Boolean Q masks. All Q are thereby classified without doing an exponential signed search per Q.
4. **Port obstruction inheritance.** The boundary mask of each candidate triangle edge is the XOR of its two Port endpoints. Odd-core edges contribute one boundary each; two available occurrences from a support in Q contribute the GF(2) span of its three edges. If even degree is infeasible for B, it remains infeasible for every subset Q of B. If the original odd core occupies two distinct connected components of the support-overlap graph even after adding B, no Q subset of B can join these components. In either case a closed Euler circuit is impossible. A legal Port circuit always has even vertex degrees and connected used edges.
5. **Three-orbit prerequisite.** Every even-incidence odd core is either signable or, by R762IB's independent finite census, belongs to one of exactly three S6 orbits. Axis relabeling preserves the signability and Port predicates. For signable cores, cancelling pairs suffice. For bad cores with a genuine Port circuit, the previous step excludes every bad maximal B, so Q contains a positive template U.

The proof uses only the stated finite signed-incidence and Port interfaces. The 15-mask certificate plus transversal tests independently re-check the central Boolean classification of R762IC; the R762IB odd-core orbit completeness remains a named load-bearing dependency awaiting independent theorem review. The composite sign result does not assert a native-force, time or rotation realization.

## Constructive algorithm and complexity

Input: one actual legal named Port circuit (or separately established N_p(n)>0) with H even. Count the 20 support multiplicities. If delta is signable, choose a core witness epsilon and cancel all q_S pairs. Otherwise find one of the three bad representatives and a mapping from its axes to the actual six axes (720 possibilities maximum); map Q to representative coordinates. Select a positive template U subset Q from the 48/14/10 finite precomputed tables. Use its exact stored (epsilon_S,z_S) witness; for each S in U, assign signs (++), (+,-), or (--) to one pair according to z_S=+1,0,-1; all remaining pairs cancel. Attach the signs to the original named events without modifying Port order.

For the fixed six-axis universe and a fixed precomputed certificate/witness table, this takes O(m) time to ingest and output signs for m named events and O(20) histogram cells (O(log m) bits per count); offline table construction and its verification are fixed finite costs. This is output-sensitive, not an assertion of polynomial complexity in the bit length of binary-encoded huge multiplicities, nor an algorithm for variable numbers of axes.

**An explicit size-four template:** odd core (024,035,125,134), all core signs -1; U=(012,024,045,234), with pair coefficients z=(+1,-1,+1,+1). The odd core contributes (-2,-2,-2,-2,-2,-2), and 2*sum(z_S h_S)=(+2,+2,+2,+2,+2,+2). Therefore the signed sum is exactly zero.

## Reproducibility and boundary

Run: python3 research_notes/portable_direct/R762ID_CHECK.py

The checker uses six-coordinate integer tuples for sign reachability, direct 15-bit GF(2) Port-edge boundaries for parity, the support-overlap graph, transversal duality, and complete Boolean mask coverage. Actual local output:

- core 4: bad=3824, minimal-good=48, Port negative masks: even degree impossible 8 / core components separated 4;
- core 6: bad=1056, minimal-good=14, separated core components 2;
- core 10: bad=1024, minimal-good=10, separated core components 1;
- PASS R762ID exact six-axis finite certificate.

No independent human review or formal proof-assistant acceptance. The code is a finite certificate for exactly six axes and its declared composite observables; it does not evaluate P000's primitive triadic balance or physical state propagation. The positive-weight Port path and signed return witnesses remain distinct BRC carriers. Any later coarsening must preserve the actual observer and event identity needed for the claim.

## Next unresolved scientific unit

Derive a conceptual graph/orbit explanation of the 15 maximal bad masks and the 8 Pasch Port parity failures without exhaustive classification, and test whether the construction lifts to P000-native force, Link, Cell, time and rotation constraints. Native extension requires an explicit typed embedding and preservation of the relevant Port/sign observers; it cannot be inferred from this composite theorem.

EM-Source-Status: Source research artifact only; native CLAIM/PROGRESS and Activity are distinct operations requiring their own live authority.