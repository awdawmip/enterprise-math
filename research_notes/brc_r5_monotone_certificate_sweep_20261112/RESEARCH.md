# R5 — monotone certificate activation, exact update budget, and indexed storage tradeoffs

Date: 2026-11-12 (Asia/Shanghai). Research status: author-side theorem and an executable regression protocol; formal native Source Result and independent review are separate operations.

## Frozen model and scientific dependencies

We work **only** in the external 28-coordinate, 15-labeled-operation P/Q–BRC Blackwell auxiliary model, not in native X6 dynamics. Frozen fixture: awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551, research_notes/brc_r5_sharp_nonlocal_fifteen_ray_20261111/VERIFY_R5_SHARP_RAY.py; original science pins: Global a01383f825ef9d43b4b754254303298c64041568, EM 86149263e38c22292c9def1e0f69092efa1be77e.

Direct inputs are the collision/legality results in Draft PR #2149 at f40960e285be90937aad827ce46446a1f777f1bc, and the interval + minimal-cover + exact LOUDS results in Draft PR #2152 at ad7013218d0474e1e942906e3beadec1eccb9213. We preserve their precise hypotheses, frozen input bytes, mathematical status and source attribution. This note does not alter them or any Task CLAIM.

Let I=[L,U], U=1/23, L=-427508577031693280/628800490619, x=155682221/25142124560000000, and u_q(r)=x(1-23r)/q for q in {15,12,3}. The cited exact census supplies 1,065 distinct admissible pairs i=(q_i,n_i), one chosen shortest ordered word w_i per pair, lengths at most 10 with total label occurrences 6,379, and exact threshold

\[
\tau_i=\frac{1-36q_i/n_i}{23}.
\]

It also supplies a prefix trie with N=2,880 nodes, E=2,879 edges, and exactly 1,065 terminal words, stored in 20,155 bits (2,520 bytes). These numerical inputs are **inherited from the frozen source computation**; the present theorem is conditional on that verified corpus and its right-persistence lemma.

## Theorem 1: exact monotone activity, not merely a sufficient activation test

For each selected i, define A_i(r)=1 when its **same** labeled word w_i is legal, at its **own** moving time u_{q_i}(r), for every 28-coordinate prefix of the word. For r in I with r<U, one has exactly

\[
A_i(r)=\mathbf{1}_{\{r\ge\tau_i\}}.
\]

If zero operation scale is explicitly admitted, this remains true at r=U.

Proof. The preceding right-persistence theorem shows legality for all r in [tau_i,U]. For r<tau_i, the final k0 mass of this fixed word/mask is

\[
\frac{23xn_i}{36q_i}(r-\tau_i)<0,
\]

with x,n_i,q_i positive. Thus no ordering of that mask can be legal at its moving time to the left of tau_i. The two implications are exact, including the activation equality. At r=U, u_q(U)=0 and X(U) is nonnegative; use the zero-scale convention. QED.

For any fixed q, tau_(q,n) is strictly increasing with n>0. Hence **at most three pairs** can have the same activation parameter (at most one per q). There may be fewer, including zero, at any of the previously classified 2,905 collision parameters. Only the selected 1,065 pairs are activated here; the other collision events are not fictitiously assigned certificates.

## Theorem 2: monotone, exactly auditable prefix-aggregate sweep

Build the rooted labeled trie on the selected words. Each node v represents one complete labeled prefix p(v), including the empty root. Define

\[
C_v(r)=\sum_{i=1}^{1065} A_i(r)\,
   \mathbf{1}_{\{p(v)\text{ is a prefix of }w_i\}}.
\]

Sort the 1,065 exact rational thresholds tau_i, grouping equal thresholds. Initialize every C_v to zero and every chosen terminal's active flag to false. Upon crossing tau_i from the left (or arriving at equality), set that word's flag and add one to C_v for the root and all nodes along w_i. When several pairs have the same tau, process their updates as one atomic event.

**Claim.** After each threshold group, every stored counter equals its defining sum. It also stays correct throughout the following open parameter interval. No deletions or re-solving of the 28-coordinate legality system occur.

Proof. The counters are initially correct because each tau_i lies to the right of the parameter-domain left endpoint in the preceding admissible interior-collision census. At a threshold, Theorem 1 changes precisely the corresponding A_i from 0 to 1; all other indicator values remain fixed. The algorithm adds their prefix incidence vectors, exactly the change in C. Induction over the sorted threshold groups proves the claim. Every update is irreversible on the increasing sweep. QED.

The exact worst-case cumulative counter-increment budget over the **entire** sweep is

\[
\sum_i (|w_i|+1)=6379+1065=\boxed{7444},
\]

including one root increment per word. Exactly 1,065 terminal flags are set once, for 8,509 total elementary counter/flag mutations. These are finite **aggregate operation counts**, not measured CPU timings. If the root count is instead derived from the number of activated words, only 6,379 nonroot counter increments are needed.

Sorting the 1,065 rational thresholds takes conventional O(T log T) exact rational comparisons; constructing the trie from the words takes O(6,379) labeled traversals. Given the sorted event list and trie, applying all changes costs O(7,444) counter increments plus 1,065 flags; optional merger with the full 2,905 collision-parameter grid costs O(2,905+1,065) event comparisons. This avoids rescanning 32,768 operation masks **per event**. All rational comparisons retain numerator/denominator bit-cost semantics rather than being labeled constant-time machine arithmetic.

## Theorem 3: precise packed-bit tradeoffs for three interfaces

We distinguish (a) bulk sequential decoding, (b) indexed retrieval by a **pre-agreed sorted pair ordinal**, and (c) in-memory prefix-count queries. The same external pair-key to ordinal mapping is excluded from both compared formats; no free arbitrary (q,n) dictionary lookup is claimed.

(A) The original static LOUDS payload uses 20,155 bits, or 2,520 bytes; the comparator's length-prefixed flat words use 29,776 bits, or 3,722 bytes. This is the already published PR #2152 result.

(B) For an *explicit fixed-width ordinal index*, a trie terminal node ID in [0,2879] takes 12 bits, and a bit offset into the flat comparator's 29,776-bit stream takes 15 bits. With T=1,065 entries and one dynamic activation flag per pair, concatenate and bit-pack the fields:

\[
B_{\rm trie,indexed}=20155+12(1065)+1065
 = \boxed{34000\text{ bits}=4250\text{ bytes}},
\]

\[
B_{\rm flat,indexed}=29776+15(1065)+1065
 = \boxed{46816\text{ bits}=5852\text{ bytes}}.
\]

The trie variant saves exactly 1,602 packed bytes (approximately 27.38% of this indexed flat comparator) under these **declared** index conventions. The 12- and 15-bit tables represent fixed-width offsets/IDs, not entropy-optimal encodings. All pair-ordinal tables are read in the same pair order. Retrieval of a word from its trie terminal requires a parent/rank-select facility: the stored ID alone is not an O(|w|) decoder. Without that facility, complete LOUDS decoding can be used first; its preprocessing time and RAM must be counted by an end-to-end benchmark.

(C) Keeping all N=2,880 prefix counters in fixed 11-bit fields suffices because 0<=C_v<=1065<2048. These counters add 31,680 bits (3,960 bytes). Static LOUDS + counters + active flags alone uses exactly

\[
20155+31680+1065=\boxed{52900\text{ bits}=6613\text{ bytes}}
\]

when globally bit-packed; adding the 12-bit terminal index gives 65,680 bits = 8,210 bytes. This larger interface supports incremental prefix aggregates and does **not** improve upon the earlier static payload-size metric. In a real implementation, parent arrays, pair dictionaries, rational event keys, bit packing, cache behavior and CPU costs must be reported separately.

## Exact verification and next scientific unit

The accompanying VERIFY_MONOTONE_CERTIFICATE_SWEEP.py consumes the **actual** predecessor's fixed 1,065-word dictionary via the sibling VERIFY_TRIE_CODEC.py, recomputes every rational activation threshold, replays the update schedule, and independently reconstructs prefix counters from active terminal words after every event. It also checks the tight 7,444/8,509 work counts and all packed-bit equalities. This verifies the new incremental algorithm on the frozen selected-word corpus; the load-bearing full 28-coordinate legality proof is inherited from the cited immutable R5 right-persistence theorem. The current author performed a separate arithmetic cross-check for all fixed-width formulas, not a clean-room re-execution of the predecessor program.

To reproduce, on this branch run Python 3 standard library: python3 research_notes/brc_r5_monotone_certificate_sweep_20261112/VERIFY_MONOTONE_CERTIFICATE_SWEEP.py. The script imports the existing source in research_notes/brc_r5_dual_zero_right_persistence_20261112 by explicit local import-path insertion.

Next: measure startup decode time, parent/rank-select memory, exact-key lookup cost, and per-event update latency on the actual corpus; then enlarge the labeled atom family while tracking certificate eligibility and full input-to-output resource cost. No formal Result, independent review or native X6 theorem is implied by this model-internal result.
