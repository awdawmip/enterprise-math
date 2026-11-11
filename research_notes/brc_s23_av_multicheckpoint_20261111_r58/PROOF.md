# R58 — Multi-checkpoint labelled source reconstruction and deletion-depth retention

Date: 2026-11-11. Status: author proof + exact finite tests, independent review pending. Frozen S23/AV source commit: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. R57 predecessor: 710a2d1d4dd9689e163543b6663b10ce4bc6164f, path research_notes/brc_s23_av_phase_batch_20261111_r57/PROOF.md. This is an auxiliary irrational circle-rotation observer, not a native P000/X6 dynamics law.

## Definitions and imported R57 lemma

Fix irrational 0<θ<1 and integers m,H≥1; K=m+H−1. Original historical boundary z=0,...,m−1 has circular phase {zθ}; B is the ascending circular permutation of these original labels. At observer phase x, the source of age r=1,...,H has phase {x−rθ}; its interval label is L_r(x). Define youngest per original label by τ_z(x)=min{r:L_r(x)=z}, or EMPTY.

The R54 Farey-successor enumeration s_1,...,s_K orders the K cuts by decreasing positive phase {sθ}. Checkpoint k lies just after the kth cut (0≤k≤K), with endpoints strictly between cuts. R52/R57 give the exact age interval affected by cut s:

I_s = [max(1,s−m+1), min(H,s)].

Every affected source moves one original circular historical label backward. The exact count of crossed boundaries for source age r at checkpoint k is

C_r(k) = #{t : 1≤t≤k and r∈I_{s_t}}.

Hence, preserving full original labels, R57 proves

(1) L_r(k)=B[(rank_B(L_r(0))−C_r(k)) mod m].

The integer C_r(k), not merely its residue mod m, also retains the number of crossed micro-events.

## Theorem R58-A: optimal explicit-output offline checkpoint batching

**Statement.** Given B, the initial full labelled source ownership and the R54 cut generator, for any Q≥0 requested checkpoint ranks in [0,K] (unordered and possibly repeated), exact full owner arrays of length H and youngest-age arrays of length m for every checkpoint can be generated in

O(k_max + Q(H+m) + Q)

word operations with O(H+m+Q) workspace excluding the returned arrays, where k_max is the maximum requested rank or 0 if Q=0. The initial state plus the R54 cut tape retains every individual original-labelled event for exact path reconstruction.

**Algorithm.** Bucket each requested checkpoint index under its integer rank k (so no comparison sorting is needed). Maintain an integer difference array D[1..H+1]. For each generated cut s_t, write D[lo]+=1 and D[hi+1]−=1 for the inclusive event interval I_s=[lo,hi]. At each requested checkpoint, prefix sum D in age order to obtain C_r, apply (1) for all r, then scan increasing ages and write the first age assigned to every original label. Empty labels retain EMPTY. Return requested answers in the original query order.

**Proof.** By the difference-array identity, the prefix sum of D after k cut updates equals the number of its processed intervals containing each r; this is exactly C_r(k). Each such boundary moves the source one predecessor label, so induction proves (1), including circular wrap-around and m=1. The increasing age scan emits the minimal age for each original label. Each cut costs two integer updates, and each explicit checkpoint costs H owner entries and O(H+m) youngest-label recovery. Buckets cost O(k_max+Q) indexing space and time, and k_max≤K=m+H−1. The initial labelled state and cut tape encode every original (r,z=s−r) event on demand. QED.

When the interface explicitly requires QH+Qm literal array entries, output itself costs Ω(Q(H+m)) word writes. The theorem matches this full-output lower bound up to constants. A compressed or youngest-only interface has different bounds.

**Optional online route.** A persistent lazy range-add/point-query segment tree can retain a version per cut. It allocates O(k_max log H) new nodes, permits an individual arbitrary checkpoint crossing-count query in O(log H), and recovers Q full vectors in O(QH log H+Qm), while preserving the same label transformation (1). The offline bucketing route is preferable for a finite known collection of full-vector queries.

## Theorem R58-B: sharp deletion-depth retention

**Statement.** For a fixed label and sources with distinct ordered integer timestamps, allow arbitrary insertions and at most d total *arbitrary individual deletions* before queries of the latest surviving timestamp. Initially retain its latest min(d+1,N) timestamps. After t deletions, maintain only the latest at most d−t+1 retained timestamps, including any new insertions. This summary answers all subsequent latest-timestamp queries exactly. On unrestricted populations, retaining merely the top d initial timestamps is insufficient.

**Proof.** With e deletions remaining, an element below the (e+1)th greatest current timestamp can become greatest only after at least e+1 newer elements have been deleted, which exceeds the budget. On insertion, keep the new top e+1. If a stored element is deleted, the e remaining stored elements are the required top e with e−1 deletions left. If an unstored element is deleted, the top e are the first e of the former summary. By induction all latest queries remain correct. Conversely, choose two populations sharing their d greatest values but with distinct (d+1)th values; deleting the common d greatest leaves different maxima. QED.

Minimal witness: source sets {1,2} and {2} have identical latest timestamp 2; delete timestamp 2 and the two outputs are 1 and EMPTY. Therefore R56 single-latest T_z suffices for the chronological rolling-window updates covered by R56, while nonchronological deletion requires a deeper stack or a reversible event tape.

## Exact validation and bit cost

CHECK_R58.py is a runnable, deterministic integer-only rational phase checker. For rational p/q tests, the reduced denominator q/gcd(p,q)>K ensures the relevant finite cut phases are distinct. At every requested checkpoint it compares all labelled owners and all youngest ages against independent rational-phase direct classification and, separately, replays every individual original-labelled event.

Small cases: m=1..12, H=1..15, eight deterministic seeded fractions p/1009 for each pair, totaling **1,440 cases**, **8,640 unordered/duplicate checkpoint queries**, **74,880 individual replayed source moves**, and **38,880 difference-array endpoint updates**. Both m=1 and H=1 are covered.

Frozen S23 endpoints: m=128,H=225,K=352, p in {262204504569236716045286, 262204504569236716045287}, denominator 10^24. The Farey neighbour denominators are (164,225) at both ends. For each endpoint, 17 nonchronological requests output 3,825 owner entries and 2,176 youngest-age entries; only **704 difference updates** represent **28,800** original-labelled micro-events across the entire tour. Checkpoints 0 and 352 have exactly matching full owner and youngest vectors, while retaining the 28,800-event cut tape. Physical time rephasing is checked exactly for j in {−10^18, 10^12+128, 10^18}, all 225 ages, k=0,176,352 and both endpoints.

The operation counts above refer to grouped updates and full-vector readout, not total bit cost. The remaining total costs include the b-bit rational parameter enclosure and exact stability, Farey bracket construction, initial B ordering and H source classifications, modular operations with indices up to K, remote timestamp arithmetic with O(log(|j|+1)) index bits, actual emitted Q(H+m) outputs, and independent validation. R49 two-state caching and R56 split-block direct endpoint classification remain valid competitors. BRC observer/provenance audit: no scalar-count quotient is used; original labels, path multiplicity and reversible tape are preserved, and no positive-weighted BRC arithmetic is assumed for this auxiliary model.

Author proof and exact finite checks are reported separately from independent review and formal project admission. Existing frozen R55/R56 298-segment data are historical inputs; R58 does not claim to rerun the entire 298-segment compilation.

## R59 next unit

Build a checkpoint-sparse youngest-only query algorithm preserving all original labels, with a bound that may improve upon QH explicit full-owner scanning when only Qm youngest values are required. Measure its precise bit cost against R49 two-state caching and R56 split-block direct classification. Test equal latest vectors with distinct future arbitrary-deletion observations. Preserve the frozen science pin and check actual shared-task owner before any CLAIM/Result/Review.
