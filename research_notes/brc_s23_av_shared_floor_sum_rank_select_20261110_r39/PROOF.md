# R39 — Shared cutpoint Floor Sum and batched last-source selection

Date 2026-11-10. Status: author-side exact derivation and eleven computed regression cases. Frozen S23/AV scientific pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Prior scientific frontier: R36–R38, especially PR #1965 commit 9e4ae500a16d4c808b6501d86c069b7c99d66361.

## Precise question and observer
Fix an irrational 0<theta<1. The m historical phases {z theta}, z=0,...,m-1, form m cyclically ordered half-open arcs. Retain the original label of every arc. For an integer window [J-N,J), find the largest source index tau_i whose phase belongs to historical arc i, or bottom when no such source exists. This is an auxiliary circle-rotation observation with a declared labelled readout; no native X6 dynamics are inferred. R38's direct q-lane selector covers wide arcs and leaves narrow arcs for exact Floor Sum rank/select. We investigate shared computation of narrow-arc last sources.

## Theorem R39.1 — Common endpoint count formula
Let a,b be historical *indices* of adjacent arc cutpoints in increasing circular-phase order, and let w=1 for the unique arc crossing zero and w=0 otherwise. For L<J, define

S_z(L,J)=sum_{t=L}^{J-1} floor((t-z)theta).

Then the number C_(a,b)(L,J) of sources t in [L,J) whose phases belong to that arc is EXACTLY

C_(a,b)(L,J) = S_a(L,J)-S_b(L,J)
             + (J-L)(floor(a theta)-floor(b theta)+w).

Proof: For each t the half-open circular membership indicator is
floor((t-a)theta)-floor((t-b)theta)
+floor(a theta)-floor(b theta)+w.
Substitute integer/fractional parts of t theta, a theta and b theta to check the two cases (nonwrapping and wrapping). Summing over integer t proves the equality. Adjacent arcs share their historical endpoint indices; consequently, for any set Q of arcs tested at one common L, their entire *labelled* count vector needs one S_z per distinct z in their endpoint union E(Q), rather than separate 2|Q| shifted sums. For the complete m-arc partition |E(Q)|=m. QED.

## Lemma R39.2 — Enclosure-wide certification
Suppose theta lies in a rational interval [ell,u], historical order is fixed (floor(d ell)=floor(d u) for all 1<=d<m), and L>=m-1. Each t-z in S_z(L,J) is nonnegative. Thus floor((t-z)x) is nondecreasing for x in [ell,u]. If exact rational endpoint sums S_z(L,J;ell) and S_z(L,J;u) agree, *every individual summand* agrees throughout the interval; therefore S_z(L,J;theta) is that fixed integer. Applied to every z in E(Q), this certifies every query count at once for all enclosed theta.

Proof: A finite sum of nondecreasing integer-valued functions can have equal endpoint values only when every component has equal endpoint values. Constancy of each term gives the required statement. Historical cutpoints retain their order by the fixed-floor hypothesis, and R39.1 transfers the result to arc counts. The returned last-source candidate additionally receives endpoint membership checks. QED.

## Theorem R39.3 — Adaptive multi-owner rank/select
For any owner i, the suffix-hit predicate H_i(L)=[C_i(L,J)>0] is monotone when L moves left. For a source window [J-N,J), test suffix lengths 1,2,4,... until each owner first has a hit or N is exhausted. If a hit first appears at length h following a zero suffix of length h_prev, the latest hit is in [J-h,J-h_prev). Group owners with identical binary-search midpoints and compute the whole group count vector using shared S_z endpoints. The monotone predicate maintains the bracket; a one-integer bracket returns exactly tau_i. A full-window zero count returns bottom. Optionally, when N is small, one full-window batched check eliminates all absent owners before bisection.

For each source threshold L queried for owner subset Q_L, the number of unique shifted Floor Sum values needed is bounded by
SUM_over_distinct_L |E(Q_L)|,
and by 2 SUM_over_L |Q_L| without sharing. A memo keyed by (L,z) avoids repeated endpoint evaluation. Each owner incurs O(log N) suffix and bisection tests. The total bit complexity must additionally count Euclidean Floor Sum integer divisions with the actual rational denominator and input precision, preprocessing historical cutpoints, caching, source recovery and verification.

Proof: Doubling finds a zero/positive bracket (or certifies emptiness); binary-searching the monotone hit predicate finds the largest integer source with a hit. By R39.1 a grouped count equals its independently computed value at each midpoint, so grouping changes no label or branch. Each (L,z) key is computed at most once; summing unique keys gives the bound. QED.

## Exact tests and provenance
VERIFY_R39.py implements a distinct-cutpoint cache and grouped rank/select, with integer Euclidean Floor Sum and strict algebraic sqrt2/sqrt3 enclosure checks, comparing every selected label with R38/R36's independent per-arc oracle in eleven cases. Two short windows also have brute-force phase reconstruction. On theta=1/3+sqrt2/1000, m=257, J=10^9, N=10^8, the 45 narrow arcs require 1,230 unique shifted sums against 2,490 unshared evaluations (50.6% reduction); all 45 labels agree with the independent oracle. The 212 wide arcs retain R38's exact q-lane route. On a different m=128 input, the batch uses 2,104 shifted sums versus 7,084 unshared (70.3% reduction). Results, scope and arithmetic costs appear in EVIDENCE.md.

This is a BRC-compatible *owner/provenance-preserving observation*: no future-needed label is collapsed into a scalar total. BRC interface resolution = REUSE_APPLIED to the branch-provenance discipline; there is no claim of native typed BRC arithmetic, native X6 reconstruction or a re-run of the S23 trillion-step 298-run table. Independent mathematical review and shared task admission remain pending.

## Next mathematical unit
Develop an Ostrowski/Euclidean-digit block service to reuse shifted Floor Sum quotient/remainder work **across distinct thresholds as well as across owner endpoints**. Benchmark q-growth, large continued-fraction quotients, exact bit cost and cache memory, preserving owner-labelled results and independent source certificates.
