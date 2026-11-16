# R207 — Depth-two source-fibre stratification and an optimal split code for X6

Date: 2026-11-16 (Asia/Shanghai)
Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED
Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34
Dependencies: R195, R197, R198–R200, R206. Independent portable research; no CLAIM, Result, Review, Working Truth or P000 change.

## Exact observation model

The Heartbeat World has six native spatial axes and twelve signed directions (not twelve axes). Here m>=1 is the number of distinguishable direction symbols, k>=0 the number of selected provenance symbols, and ⊥ one neutral provenance symbol. Each event is a pair (d,p), with 0<=d<m and p in {⊥,0,...,k-1}. The selected observer J(w) consists of s(w), the ordered list of distinct selected provenance labels in last-occurrence order, and t₂(w), the suffix of at most two complete paired events. Concatenation induces the R200 quotient monoid.

Let r=|s| and N_k=Σ_{r=0}^k k!/(k-r)! (partial permutations).

## R207-A — Exact conditional fibre theorem

For every fixed source-order state s, the number of attainable depth-two tails is

F_r(m) = 1+m+m²  if r=0;
F_r(m) = m+4m² if r=1;
F_r(m) = 5m²    if r>=2.

Consequently, for every m>=1 and k>=0,

|J_{m,k,2}| = 1+(k+1)m+(5N_k-k-4)m².

Proof. With r=0, the full history has no selected provenance, and the empty, singleton and two-event tails contribute 1,m,m². With r=1, let j be the last source. A singleton history must have selected provenance j. A complete two-event tail can have only the provenance patterns (⊥,⊥), (⊥,j), (j,⊥), (j,j), each with m² direction pairs. For r>=2, write j=s[-1], i=s[-2]. The four patterns remain, and the only additional pattern is (i,j): distinct selected labels in the final two events must be the final two labels of s in this order. Every listed pattern is attainable by prepending a suitable ordered source prefix. No history shorter than two events can contain r>=2 distinct selected sources. Sum over 1 empty source order, k singleton orders and N_k-1-k longer orders. Direct algebra gives the closed formula, also for k=0,1 by direct evaluation. QED.

## R207-B — Explicit no-DP split rank/unrank

Rank a source order of length r as a length-stratified partial permutation, giving src_rank(s) in [0,N_k). First add the length offset Σ_{j<r} k!/(k-j)!; then rank the distinct ordered labels lexicographically, using at position j the stride (k-j-1)!/(k-r)! and removal from the sorted available list.

For fixed source s, assign fibre rank f_s(t) as follows (d,d0,d1 are direction indices):

* r=0: empty tail -> 0; singleton neutral direction d -> 1+d; neutral-neutral directions d0,d1 -> 1+m+m*d0+d1.
* r=1: singleton selected provenance j=s[-1], direction d -> d. For length-two patterns (⊥,⊥), (⊥,j), (j,⊥), (j,j), indexed a=0..3, rank = m+a*m²+m*d0+d1.
* r>=2: five patterns (⊥,⊥), (⊥,j), (j,⊥), (j,j), (i,j), indexed a=0..4, rank = a*m²+m*d0+d1.

Put b_s=ceil(log₂ N_k), b_f=ceil(log₂ max_{0<=r<=k} F_r(m)) and define

C(s,t) = 2^{b_f} src_rank(s)+f_s(t).

This is a bijection from valid joint states into a subset of [0,2^{b_s+b_f}). The inverse splits the high and low fields, un-ranks the partial permutation, and then decodes the indicated fixed-source pattern plus base-m directions. The globally smallest fixed-width state code has ceil(log₂ |J|) bits by cardinality, so this split code is optimal whenever the two widths coincide. The general R199 algorithm remains appropriate when they differ.

Proof. Partial-permutation ranking is a bijection within each length class, and the disjoint tail patterns from R207-A exhaust exactly the F_r(m) local ranks. The high and low fields recover the source state and its complete paired tail. The product can be implemented by decode -> (s∘s',suffix₂(t t')) -> encode. This is conjugation of the established R200 finite quotient and preserves associativity, identity and all declared future observations. A BRC joint histogram can use this integer as the observer key while independently retaining physical affine action, exact positive rational weights, multiplicities and other required branch/provenance keys. QED.

## Exact X6 example and limits

At m=12, k=6, N_6=1957 and the fibre sizes by r=0..6 are [157,588,720,720,720,720,720]. Thus

|J|=1,407,685; b_s=11; b_f=10; split width=21 bits.

Because 2^20 <1,407,685<=2^21, the independent 11+10 split is **globally minimum fixed-width** for this observer. It needs no full-state table and no R199 prefix-count DP; ranking the source costs O(k²) elementary comparisons with a simple ordered-array implementation and O(k) source-symbol storage, and ranking the length-two fibre uses constant-time pattern/direction arithmetic.

This is a 21-bit combinatorial identifier, not a 21-dimensional affine representation. The unrelated F₂ affine-orbit problem from R205–R206 still has the currently established bounds 31..35 for m=12,k=6,L=2.

The split code is not universally optimal. For k=m=1, N_1=2, F_0=3, F_1=5, |J|=8: the split uses 4 bits while global ranking needs 3.

The R200 quotient retains selected-source order plus the last two **paired** events; it does not independently subsume native X6 paths, full time relations, physical effects, signed amplitudes, port identity or unselected hidden provenance. Positive-weighted BRC and signed/phase carriers retain their separate algebraic types.

## Validation, reproducibility and next questions

Exact pure-Python checker: R207_depth2_split_codec_check.py; preserved result: R207_verification.json. The deterministic test exhausts 1,407,685 X6 joint source/tail states and 1,407,685 reconstructed representative histories; verifies 20 additional parameter models (k=0..4,m=1..4); and tests 8,947 ordered compositions against concatenated actual history representatives. All PASS. General m,k statements are established by the proofs above. No installed native enterprise_math.brc_transport integration or independent mathematical review was executed.

Continue with (1) an explicit depth-three split code using source-conditioned Stirling/ordered-partition fibres and exact optimality conditions; (2) actual installed native EffectHistogram integration with R203 cross moments and total conversion/storage costs; and (3) the independent open 31..35 F₂ affine-orbit dimension question. Preserve the task's scientific input pin and shared active owners.