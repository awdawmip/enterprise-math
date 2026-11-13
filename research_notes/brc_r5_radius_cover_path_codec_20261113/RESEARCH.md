# R5 — Exact radius-cover path enumeration and reversible center coding

Date: 2026-11-13. Status: author-side exact combinatorial proof and executed finite calculations; **not** an accepted Source Result. Frozen scientific input remains `435e77af0d180eac32bd1f9c4c464bc4010b7551`. This research changes only the *optional derived center-list representation* of the R5 auxiliary certificate-query data structure.

## Prior frontier and question

Draft PR [#2245](https://github.com/awdawmip/enterprise-math/pull/2245) establishes a 35-byte fixed-span multiset-rank code with a faster histogram ratio-chain decoder, while [#2239](https://github.com/awdawmip/enterprise-math/pull/2239) establishes a 33-byte fixed-histogram code. Both encode wider word classes using the observed 213 checkpoint centers (first=1, last=952, 212 gaps, histogram `{3:16, 4:77, 5:119}`). The original exact 56-byte center payload in [#2232](https://github.com/awdawmip/enterprise-math/pull/2232) has SHA-256 `bf4f377e8a3b9823d589d0f5c5b0b5973f374a09aa986d5b729bc695c5de0326`.

The new question is whether the **actual radius-2 coverage requirement**, not just a gap alphabet/span/histogram, defines a smaller rankable finite class. The answer is yes as an exact theorem. The number of legal sequences depends on the full cumulative wall-event array `E`; its value for the *original pinned rational R5 corpus* has **not** yet been computed in this work.

## Theorem: admissible center sets are directed graph paths

Let `x[0]<x[1]<...<x[W]` be strictly increasing **integers**, `R>=0` an integer, and `1<=K<=W+1`. We consider strictly increasing checkpoint indices `S=(s_0,...,s_{K-1})` with `max_b min_j |x[b]-x[s_j]|<=R`. Define:

- an admissible start `s` by `x[s]-x[0]<=R`;
- an admissible finish `s` by `x[W]-x[s]<=R`;
- a directed edge `p -> q` for `p<q` if the interval of integer boundary indices `[p,q]` is covered by these two endpoints alone.

Set `u(p) = max{b : x[b] <= x[p]+R}` and `v(q)=min{b : x[b]>=x[q]-R}`, with usual array bounds. Then **edge(p,q) iff `v(q)<=u(p)+1`**. Because the `x[b]` are strictly increasing integers, every valid edge satisfies `q-p<=2R+1`.

**Proof.** At a boundary `b` between `p,q`, its nearest center among any increasing center set with adjacent centers `p,q` is one of `p,q`; earlier or later centers are farther away. The left endpoint covers exactly boundary indices through `u(p)`; the right endpoint covers those from `v(q)`. Their union covers every integer boundary index of the interval exactly when there is no integer gap between the two index intervals: `v(q)<=u(p)+1`. Separately the first and final tails must be covered by the first and last center. Thus a K-center radius-R covering is exactly a path of K vertices with admissible endpoints and these legal edges. For `q-p>=2R+2`, boundary `p+R+1` is at index distances at least `R+1` from both endpoints, hence event distances also exceed R. Such an edge cannot be legal. QED.

The index-gap inequality is necessary but **not sufficient**: `x=[0,3,6]`, `R=2`, `S=[0,2]` obeys the gap and tail bounds but leaves boundary 1 uncovered. The graph enforces the exact event metric and avoids that false inference.

## Exact combinatorial ranking

Let `F[t,p]` count legal paths of exactly `t` centers that begin at p and end at an admissible finish. Define `F[1,p]=1` for admissible finishing p, else 0, and

`F[t,p] = sum_{q: edge(p,q)} F[t-1,q]`.

Then the exact finite-class cardinality is

`T(x,R,K)=sum_{p: admissible start} F[K,p]`.

The lexicographic enumeration of start choices and successive edges, weighted by these suffix counts, gives mutually inverse rank and unrank on `[0,T)`, with no hidden tie rule. Provided `T>0` and `x,R,K` are available at decoding, `ceil(log2(T)/8)` bytes (equivalently `ceil(bit_length(T-1)/8)` for `T>1`) is an optimal **fixed-width byte payload size for this exact class**. Dynamic programming takes `O(K(W+1)(2R+1))` additions with integer arbitrary-precision counts; ranking/unranking each uses at most `O(K(2R+1))` suffix-count selections after the DP. The event-coordinate array itself and all certificate/event provenance remain separate; this encoding is reversible only for the declared checkpoint-center observer.

## Executed exact verification

`VERIFY_RADIUS_COVER_CODEC.py` exhaustively enumerates every strictly increasing integer array with 0..6 increments, each increment in {1,2,3} (1,093 arrays). It tests 28,432 `(x,R,K)` instances with `R=0..3` and every permitted `K`, comparing DP counts to every explicit K-subset and checking lexicographic rank/unrank on all **104,566** admissible sequences. No mismatches; out-of-range ranks rejected. The explicit counterexample above is checked.

`SYNTHETIC_FROZEN_DIMENSIONS.py` *reads the real published 56-byte center payload* (SHA-256 above), recovering the 213 exact historical centers and gap histogram. It then creates a **new synthetic** 953-increment event array with integer frequencies `{1:858,2:78,3:17}` and total 1,065 events, constructed so that precisely those historical centers give radius-2 coverage. This synthetic array has the same counts and maximum multiplicity as the R5 problem but is **not asserted to equal the pinned rational event array**.

For this declared synthetic E, the DP reports

`T = 4366610165786408069188153688125015683600`, needing **132 bits / 17 bytes** to index all exact radius-2 K=213 coverings. The historical center list's rank is `4320653095406908733124959812907791083778`, and unranking exactly restores its 213 indices. By contrast the previous 33/35-byte codecs address larger specified classes. Thus the 17-byte result is a concrete **constructed-instance capacity result**, not a claim of 17-byte R5 production storage.

A second deterministic synthetic example (50 increments of 3, 12 of 2, 891 of 1, permuted by seed 2026111313) shares 954 boundaries and 1,065 events but has `T=0` for `R=2,K=213`. Hence the aggregate dimensions and gap-count theorem alone do not determine feasibility or codec capacity.

## What is preserved; next discriminating experiment

The original scientific pin, certificate seed, event ordinal identities, 953 rational activation walls, tied-event multiplicities, 2,880 prefix nodes, and all future operations are unchanged. Any exact code must decode back to the identical center indices; the existing directory/masks and signed event corrections then operate unchanged.

**Next**: independently rebuild the pinned original exact `E[0..953]` from its published 2,520-byte BP/labels/terminals seed; compute `T(E,2,213)` and rank/unrank the original 213 centers, test all 2,747,520 boundary-prefix counts or establish exact representation substitutivity against an already verified query implementation, then compare *full* cold-start time, peak RSS and query costs for the 17-byte-type path code (with its actual pinned width), 33B, 35B and 56B. The DP itself costs O(KWR) in preprocessing, which may outweigh the storage saving unless its count table is cached or the query life is long. Formal task owner/CLAIM, Result, review and actual Source activity must be checked separately.

Evidence: `VERIFY_RADIUS_COVER_CODEC.py`, `SYNTHETIC_FROZEN_DIMENSIONS.py`, `EXACT_OUTPUT.json`, `SYNTHETIC_OUTPUT.json`. Python standard-library exact integer arithmetic; no approximate or floating-point mathematical oracle.
