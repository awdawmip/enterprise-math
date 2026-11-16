# R209 — Direct Stirling rank/unrank for complete paired-event observers

Date: 2026-11-16 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Frozen scientific pin: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Dependencies: R200, R206, R207, R208. Independent portable research; no CLAIM or Result/Review.
Scope: a declared finite source-order/full-paired-tail *observer* of six-axis Heartbeat World, not a replacement for native X6, path, time, full provenance, port identities, physical BRC affine effects or signed amplitudes.

## The new problem and result

R208 proves every-depth source-conditioned Stirling tail-fibre counts, but its explicit local-pattern enumerator can be exponential in tail depth L. The open question was a direct efficient no-enumeration rank/unrank. R209 provides one using a backwards restricted-growth automaton. It is a constructive, globally optimal fixed-width code for **independent** direction and source labels, including cases where source/fibre split codes waste a bit.

Let m>=1 count direction symbols, k>=0 count selected provenance labels, L>=0 count final paired events, and let 0 be a neutral provenance label. The event alphabet is pairs (d,p) with 0<=d<m and 0<=p<=k, of size a=m(k+1). A history w has source order s(w), the list of distinct selected p>0 in last-occurrence order, and full paired tail t_L(w), the final min(L,|w|) pairs. The R200 quotient J=(s,t_L) respects concatenation.

Write P(k,r)=k!/(k-r)!, S(n,j)=Stirling second-kind, and

C(r,L) = sum_{j=0}^{min(r,L)} S(L+1,j+1).

**Theorem A (complete disjoint blocks).** All J states partition into:
1. short histories of exact length h=0,...,L-1, each with a^h possible complete event words (the source order is determined by the word); and
2. full-length tails, stratified by source-order length r and the partial permutation s of r out of k labels, each source block containing m^L C(r,L) tails.

Within a full-tail source block, group by j, the number of selected labels appearing in the tail. Exactly the final j labels of s appear, in the required last-occurrence order, giving S(L+1,j+1) provenance words and m^L independent direction words. Consequently:

N(m,k,L) = sum_{h=0}^{L-1} [m(k+1)]^h + m^L sum_{r=0}^k P(k,r) C(r,L).

Proof: A short tail is the entire history. In a full tail the j distinct selected labels must be a final segment of the final source order, and each legal tail may be prefixed with the earlier selected labels in their desired order. For a prescribed last-occurrence order of j distinct selected symbols, the number of length-L strings using those symbols and neutral zero is exactly S(L+1,j+1), by the R206/R208 inclusion-exclusion identity. Each direction is independently chosen. The blocks are disjoint and exhaustive. The formula includes L=0 (only source orders) and k=0. This is a constructive reindexing of R208's exact count, not a new total-state theorem.

## Backwards rank/unrank without pattern enumeration

Fix a source order s and one j-block. Read the provenance word right-to-left. Let h=0,...,j be how many distinct selected symbols have been encountered so far in this backward scan. These symbols must be s[-1], ..., s[-h], in that first-seen order. The next backwards symbol may be: neutral zero; any of these h seen labels; or, when h<j, exactly the next new label s[-h-1]. The next-new option advances h by 1.

Let F_j(t,h) count admissible completions with t positions left and current state h. The exact recurrence is

F_j(0,h) = [h=j],
F_j(t,h) = (h+1) F_j(t-1,h) + [h<j] F_j(t-1,h+1).

Thus F_j(L,0)=S(L+1,j+1). To rank a word, at each backwards step enumerate the allowed symbols in increasing numeric order, add the completion counts for those preceding the actual symbol, and update h. To unrank, subtract completion-block counts until the chosen symbol's block is reached.

**Theorem B.** The backwards rank and unrank give inverse bijections between provenance words in a fixed s,j block and integers 0,...,S(L+1,j+1)-1.

Proof: Induct on t. At t=0 precisely h=j accepts one empty completion. At t>0, first-symbol choices partition accepted continuations into disjoint blocks of sizes F_j(t-1,h') by the recurrence. The lexicographic rank and inverse block-subtraction traverse the same partition. Hence both procedures are exact inverses.

## Global optimal code

Rank the short histories by h then by the event digits d(k+1)+p in base a. For a full tail with source order s of length r:

O_short = sum_{h=0}^{L-1} a^h.
O_r = m^L sum_{u=0}^{r-1} P(k,u) C(u,L).
O_s = partial_perm_rank(s) m^L C(r,L).
P_code = sum_{v=0}^{j-1} S(L+1,v+1) + backwards_provenance_rank.
D_code = base_m_rank(direction_tail).

The full index is O_short + O_r + O_s + P_code m^L + D_code.

The partial-permutation rank uses sorted remaining source labels and step-size P(k-i-1,r-i-1) after i labels have been selected. The inverse first locates the short or full region; for a full state it locates r, decodes s, chooses j by Stirling block subtraction, reconstructs the provenance tail by the backwards DP, and decodes the directions.

**Theorem C (exact minimality).** For every m>=1,k>=0,L>=0, the global rank/unrank are mutual inverses between the reachable quotient J and the *consecutive* interval [0,N(m,k,L)). Hence exactly ceil(log2 N(m,k,L)) fixed bits suffice (zero bits for the singleton case), matching the counting lower bound. The quotient product implemented as rank(unrank(x) * unrank(y)) is associative and has the same declared future observer semantics as R200.

Proof: Theorem A supplies the exhaustive disjoint blocks and exact cardinalities; base-a/base-m digit ranks and partial permutations are bijective within their blocks; Theorem B is bijective in each provenance subblock. The consecutive offsets therefore have neither gaps nor collisions. The representation has exactly N images, so fewer than ceil(log2 N) bits cannot injectively encode it. The quotient product is transported through a bijection, hence remains associative and observer-preserving.

## Cost

After Stirling and source-length offset preprocessing (O(L min(k,L)+k min(k,L)) integer operations), each relevant backwards DP table has O(L(j+1)) exact integer entries and arithmetic steps, where j<=min(k,L). A direct sorted-array partial-permutation rank/unrank costs O(k^2) elementary operations. Scanning up to j+2 candidate symbols over L positions gives O(L(j+1)+k^2+L) additional integer operations. No enumeration of all provenance words or all N states is used. These are arithmetic operation counts; integers and offsets can require B=ceil(log2 N) bits, so physical bit complexity and actual BRC end-to-end runtime depend on exact-integer algorithms and conversion/storage.

## X6 consequences and validation

For m=12,k=6, (L, N, minimum bits) is:

- (0, 1,957, 11)
- (1, 46,957, 16)
- (2, 1,407,685, 21)
- (3, 50,583,973, 26)
- (4, 2,095,910,437, 31)
- (5, 97,426,560,037, 37)

For L=4, the new direct globally packed code uses **31 bits**, while R208's simple two-field split uses 32. This is the depth-four one-bit gap resolved by a direct polynomial-arithmetic-step construction. Combinatorial identifier bits are not F_2 affine-orbit dimensions: the separate R205–R206 X6 L=2 interval remains 31..35 dimensions.

The standard-library integer checker tests 27 complete small parameter models (m=1..3, k=0..2, L=0..2) with exhaustive history images to length k+L; 514 exhaustive state rank/unrank checks, 10,803 actual-word checks, 2,835 one-event update checks, 1,658 ordered composition checks, 50 provenance-fibre checks, and another 50 exact X6 rank/unrank samples at depths 1..5. All assertions PASS. The symbolic proofs cover general m,k,L; arithmetic checks establish the declared finite instances. Independent review is NOT_REVIEWED. Native installed enterprise_math.brc_transport tests remain NOT_EXECUTED.

Reproduce with R209_direct_stirling_rank_check.py and compare R209_verification.json.

**Next science:** integrate a pinned real EffectHistogram and measure input-conversion, exact rational growth, mixed physical-source moments and serialized storage; examine online updates without full key decoding; separately study the unresolved 31..35 binary affine-orbit dimensional interval at X6 tail depth two.
