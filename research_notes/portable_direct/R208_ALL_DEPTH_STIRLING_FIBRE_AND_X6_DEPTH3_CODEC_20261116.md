# R208 — Source-conditioned Stirling fibres for every suffix depth; 26-bit exact X6 depth-three split

Date: 2026-11-16 (Asia/Shanghai).
Scientific status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Dependencies: R195 (source order), R200 (independent paired provenance/direction observation quotient), R206 (full-source-order Stirling fibre), R207 (depth-two split codec).
Independent portable research; no current CLAIM, Result, Review, Working Truth, or change to P000.

## Exact model

In the native Heartbeat World there are six spatial axes and twelve signed directions. This study uses a specified *observer* over them, not a replacement for X6. Let m>=1 count the distinguishable signed-direction symbols under study, k>=0 count selected source labels, plus an additional neutral source ⊥. An event is a complete paired symbol (direction,source) from the m(k+1)-letter alphabet. For any event history w let s(w) be the distinct selected sources in the order of their **last occurrence**, and t_L(w) its final min(L,|w|) complete paired events. The R200 quotient J_{m,k,L} retains (s,t_L) and is closed under chronological concatenation.

Let S(n,j) be the Stirling number of the second kind, with S(n,j)=0 for j<0 or j>n, S(0,0)=1. Let r=length(s), N_k=sum_{r=0}^k k!/(k-r)!.

## R208-A — All-depth conditional fibre cardinality

**Theorem.** For all integers m>=1, k>=0, L>=0, and every fixed reachable source order s of length r<=k, the number of distinct reachable complete-event suffix observations jointly compatible with s equals

F_{m,r,L}
  = m^L sum_{j=0}^{min(r,L)} S(L+1,j+1)
    + sum_{h=0}^{L-1} m^h S(h+1,r+1).

Empty sums are zero, and m^0=1. The total number of reachable joint states is

|J_{m,k,L}| = sum_{r=0}^k [k!/(k-r)!] F_{m,r,L}.

**Proof.** Split histories into full tails (length exactly L) and shorter complete histories (length h<L). For a full tail, let j be the number of distinct selected source labels that occur. The final source-order observation s uniquely forces these j labels to be its final j entries, in exactly their last-occurrence order. This permits precisely S(L+1,j+1) different provenance strings of length L, by the ordered-last-occurrence version of the Stirling/inclusion-exclusion identity: for j specified selected labels and the neutral symbol, provenance strings using every selected label and ending with any fixed relative last-occurrence order have

(1/j!) sum_{i=0}^j (-1)^i binom(j,i)(j+1-i)^L = S(L+1,j+1)

possibilities. This is also true at j=0. Each complete provenance string carries m^L independently chosen direction strings. Every such full tail can be realized after an earlier prefix containing the remaining selected sources in their designated order. This yields the first term.

For a shorter tail h<L there is *no omitted earlier prefix*: the entire history is of length h. It must have exactly r distinct selected labels, all present, in the prescribed last-occurrence order s, hence there are S(h+1,r+1) provenance strings. Each permits m^h direction strings. Summation yields the second term. Distinct tail lengths are disjoint. The formula depends only on r, not on source-label names. There are k!/(k-r)! ordered distinct selected source tuples of length r; summing proves the global formula. QED.

The total agrees with R200's alternate closed form (a=m(k+1)):

|J|=sum_{h=0}^{L-1} a^h+sum_{j=0}^k [k!/(k-j)!] (a-jm)^L.

Our exact checker verifies this independently for all listed finite models.

## R208-B — Constructive source/fibre rank and optimal 26-bit depth-three instance

The R207 partial-permutation source rank uses b_s=ceil(log2 N_k) bits. For any chosen source order s and length L, separately enumerate admissible complete paired-tail patterns in this order: short length h<L first, then full length L; within each length, lexicographic provenance pattern and base-m direction code. The explicit Stirling formula gives the exact number F_{m,r,L} of such patterns. Number them 0,...,F_{m,r,L}-1, defining a deterministic local rank f_s(t). A split integer code

C(s,t)=2^{b_f} source_rank(s)+f_s(t),
b_f=ceil(log2 max_{r<=k} F_{m,r,L})

has a direct two-field inverse by source unranking followed by local pattern/direction unranking. This preserves the full declared joint observation and is a finite monoid code via decode -> quotient product -> encode. No table of all |J| joint states is needed. For unbounded L, naive provenance-pattern enumeration can be exponential in L; this claim is an existence/construction, not a uniform polynomial-runtime bound.

For the original six-axis 12-direction observer with k=6 independent selected source labels, L=3, the seven fibre values for source-order lengths 0..6 are

F_{12,r,3} = [1885, 14268, 24336, 25920, 25920, 25920, 25920].

There are N_6=1957 source-order states. Therefore

|J_{12,6,3}|=50,583,973, b_s=11, b_f=15.

The split code uses **26 bits**. Because 2^25<50,583,973<=2^26, it is exactly optimal among *all fixed-width lossless* encodings of this observer. For full-length tails and at least three available sources, there are only

S(4,1)+S(4,2)+S(4,3)+S(4,4)=1+7+6+1=15

admissible provenance patterns for a fixed source order, independent of k once k>=3. Their direction strings contribute m^3; short histories are handled separately. This supplies a compact constructive codec without a global 50-million-state rank table or R199 prefix-count dynamic programming.

For L=4 with the same parameters, the split uses 11+21=32 bits, while |J|=2,095,910,437 needs only 31 bits. Thus split optimality at depths 2 and 3 does not extend uniformly to every depth. R199's global rank is an available exact optimal-width alternative.

## Validation and scope

Execute standard-library Python R208_stirling_fibre_exact_check.py to regenerate R208_verification.json. In 31 small combinatorial models (k=0..4, L=0..5, plus k=6,L=3), it exhaustively enumerates all provenance suffix patterns against all source-order prefixes and all short complete provenance histories, checking each fixed-source fibre. The identities are further independently cross-checked with direction multiplicities m in {1,2,3,4,12}, for **155 weighted model equalities**, all PASS. The full 50,583,973-state X6 L=3 cardinality is evaluated exactly by integer formulas, not enumerated as fifty million states. The general theorem follows from the combinatorial proof.

The 26-bit figure is a combinatorial observer *state identifier*, not a 26-dimensional affine action. The previously known F2 affine-orbit interval 31..35 applies to depth two of a different resource question. BRC physical affine effects, exact positive rational weights, multiplicities, branch identity, signed amplitudes, native X6 paths, ports, and time remain separately typed and must be retained where the future operation needs them. Independent mathematical review: NOT_REVIEWED. Native installed-package BRC integration: NOT_EXECUTED.

## Next scientific units

1. Construct an efficient direct source-conditioned Stirling rank/unrank algorithm at arbitrary L with clear time/bit-complexity accounting, exploiting last-occurrence ordered partitions instead of enumerating patterns.
2. Integrate the full paired observer code with native enterprise_math.brc_transport.EffectHistogram, including R203 joint physical–source cross moments, and compare end-to-end exact representation costs.
3. In parallel, study the open binary affine orbit dimension 31–35 at m=12,k=6,L=2; preserve the exact distinction between orbit dimension and cardinality coding.
