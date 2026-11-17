# EC49FRJ — Direct exact native terminal-observer fiber proof of minimal root-query mass

Date 2026-11-17. Frozen scientific input fc0f038e7bfd12c886b4d37f900bfb770c0f61ab, original BRC class 16943. AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. This **strengthens** the companion full unbounded-price Bellman theorem by eliminating its dependency on two expensive high-price unrestricted Bellman anchors for the universal root-count lemma.

## Original physical observation fiber certificate

141 full named root-state profiles (all distinct) are indexed 0..140, with positive original configuration multiplicities m_i summing to 310. There are exactly 144 **named physical terminal** observations q=0,...,143 and 84 **named physical root** observations q=144,...,227.

Define for every original named profile i its complete original **terminal observer signature** T(i)=(response(q,i) for q=0,...,143). By exact exhaustive comparison of **all 144 original terminal responses across all 141 named profiles**, the signature map has exactly **139 fibers**, with precisely two nonsingleton fibers:

| full named profile pair | original representative configuration IDs | multiplicities | SHA256 of common 144-terminal signature JSON |
|---|---|---|---|
| P={8,139} | {17928,38165} | (1,1) | 459efc71c5edd35e17e4af59e04d6ded59fcdea3b2490b95e1707548cc691bd1 |
| Q={46,140} | {24541,38166} | (1,1) | 2422bf2e88480d75ca011075b53dc9a6829636ebefb2b585a482d31f2a4b690a |

The other 137 profiles are singleton fibers. A concrete **native named root physical observation** q=148 distinguishes P by response values (66,62) and Q by (66,64). Exactly the root physical IDs 148 through 163 inclusive give unequal responses for the two members of either pair. These physical IDs are retained independently of any coinciding response partition.

## Direct combinatorial theorem

For **every finite complete adaptive identifying decision tree Q** over the unchanged 228 physical actions, let r_i(Q) be the nonnegative integer number of original root observations on named profile i's path. Then:

**Ru(Q)=Σ_i r_i(Q) ≥4 and Rm(Q)=Σ_i m_i r_i(Q) ≥4.**

**Proof:** Consider any terminal-indistinguishable pair (i,j) above. As long as its two profiles have not been separated, their observations from **every terminal query** are identical. Thus no adaptive sequence of terminal observations can separate the pair. A complete identifying tree must ask at least one root query along their still-common path before their responses diverge. In particular r_i(Q)≥1 and r_j(Q)≥1. There are two disjoint pairs with exactly four distinct full named profiles, each having multiplicity one. Summing gives Ru≥4 and Rm≥4, with all remaining contributions nonnegative. The native complete physical trees D=(4,296,4,707) and E=(4,298,4,688) attain equality in **both** measures, so these global lower bounds are **sharp**. QED.

The proof applies to **all complete identifying adaptive trees**, including nonreduced trees and arbitrary positive real root/terminal prices; it does not use high-price numerical extrapolation, an aggregation that discards named states, or an extra hypothesis about terminal costs.

## Unbounded real-price Bellman corollary with just six price/prior anchors

For prior p_i(λ)=(1−λ)/141+λ m_i/310, the normalized cost of any tree Q as function of the real root price x has slope at least **4(1−λ)/141+4λ/310**. The same slope is attained by both D and E for every λ. The independently checked **six unrestricted exact Bellman anchors** at prices x=3 and x=20, priors λ=0, β=620/3299,1, together with the original separate-affinity interpolation proof, establish exact V=min(D,E) on the complete real rectangle [3,20]×[0,1]. For x≥20, any competitor's gap from its fixed interval winner D or E is an affine function with nonnegative value at x=20 and nonnegative slope, so it remains nonnegative for all real x≥20. Consequently **V(x,λ)=min(D,E) for every real x≥3 and 0≤λ≤1**. With the parent EC49FRI exact [1,3] theorem, **V=min(A,B,C,D,E) for every real x≥1**.

Thus **two explicit original terminal-observer fibers plus six exact finite Bellman anchors** suffice for this entire unbounded continuous problem. The independent native high-price x=100000 certificates already saved in EC49FRJ remain a separate computational corroboration rather than a load-bearing proof premise.

## Exact program and reproducibility

The companion source-linked verifier EC49FRJ_TERMINAL_FIBER_CHECK_20261117.py, run from the extracted full archive's code folder, reads the **unchanged original frozen BRC source/master and all 141 original named profile records**, checks both original source SHA256 values, enumerates every terminal signature and every root physical distinguisher, asserts the exact 139-class/two-pair fiber certificate and all original multiplicities, and writes EC49FRJ_TERMINAL_FIBER_CERTIFICATE.json.

The original generated witness file has SHA256 **f5140bee75a2ee8c5b2767183bf79f4d40cc6ab07223d8f631ddc6d16a978382**. Full actual source and certificate are in conversation-delivered archive **EC49FRJ_EXACT_ALL_PRICES_STRUCTURAL_FIBER_FULL_EVIDENCE_20261117.tar.xz** SHA256 **d40c092682a5fe1af7cc1229630af136305166314289f30aeac8eb64b914a46c**, fully re-opened with 33 manifest-listed files checked byte-for-byte. Archive is a conversation artifact, **not represented as a GitHub blob**.

This is an exact original BRC observer/fiber argument. Equal terminal observations do **not** erase either native named profile, composite/source provenance or the root observation necessary to distinguish them. Protected P000 and ACTIVE worldview unchanged; project admission remains NOT_REVIEWED.

**Next research**: a general dual/combinatorial minimum root-observation mass theorem for arbitrary finite terminal-signature fibers and positive multiplicities, accounting for shared root queries, adapted joint-composite observation families, and their future-operation preservation.
