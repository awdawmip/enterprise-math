# R5 — Exact 17-byte radius-cover rank for the original pinned wall corpus

Date: 2026-11-13. Status: author-side exact finite enumeration, reversible codec and cross-checked computation; not a formally accepted Source Result. This is an *auxiliary certificate-query index*, not a claimed native X6/Heartbeat dynamical law.

## Frozen inputs and non-repeated predecessor facts

Scientific input pin: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`. The independent 15-atom dual-zero coefficient fixture is reproduced in `VERIFY_R5_PINNED_RADIUS_COVER.py` from [the original exact two-coordinate census](https://github.com/awdawmip/enterprise-math/blob/eb3a80abe45ddd2305c7a0247a45eeba9bef04d3/research_notes/brc_r5_dual_zero_right_persistence_20261112/VERIFY_RIGHT_PERSISTENCE.py). The original 28-coordinate feasibility / canonical shortest legal-word witnesses were proved and executed there; this work **reuses** that vetted pair population rather than claiming a fresh independent proof of every legal path.

Original (K=213) checkpoint centers are decoded from the byte-exact 56B payload established by [Draft PR #2232](https://github.com/awdawmip/enterprise-math/pull/2232): SHA-256 `bf4f377e8a3b9823d589d0f5c5b0b5973f374a09aa986d5b729bc695c5de0326`. The prior [Draft PR #2253](https://github.com/awdawmip/enterprise-math/pull/2253) proved that radius-(R) covering sets are counted by paths in an exact directed graph; however its 17B example was **synthetic**, and its report explicitly left the original wall array and (T(E,2,213)) open. This note resolves that exact unfinished frozen-instance calculation.

## Exact independent reconstruction of the original event wall array

For a nonempty atom mask (m\subseteq\{0,\ldots,14\}), define integer weights
\[
n(m)=-\sum_{j\in m} W_j,\quad k(m)=-\sum_{j\in m}K_j,\quad
W=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80),
\]
\[
K=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0).
\]
Enumerate all (2^{15}-1) nonempty masks. Keep those with (n(m)\geq 3), (36\mid k(m)), and (q=k(m)/36\in\{3,12,15\}); deduplicate *pairs* ((q,n)) rather than masks. The `n>=3` condition is part of the frozen source fixture: it is **essential**. Omitting it adds five spurious pairs at n=1,2 and changes the radius calculation. The resulting pair counts are exactly `q=3:538, q=12:298, q=15:229`, hence 1,065 distinct original certificate activation events.

For each pair define the exact rational threshold
\[
\tau_{q,n}=\frac{1-36q/n}{23}.
\]
Sort all distinct rational thresholds and define
\[
E(0)=0,\qquad E(b)=\sum_{i=0}^{b-1}\#\{(q,n):\tau_{q,n}=\tau_i\}
\quad(1\le b\le953).
\]
This preserves tied-wall multiplicity. Actual event-group histogram: 869 singletons, 56 doubletons and 28 triples; 953 distinct walls, 954 boundaries, (E(953)=1065). Independently, exactly 605 events satisfy (\tau\le0), agreeing with the prior frozen root query at (r=0). The SHA-256 of the 953 one-byte event-group multiplicities, in increasing rational-wall order, is `c19d116b617a5197b76a00440b31f067fac0db3e743d38ae3208a533182c30f9`.

## Exact finite covering theorem and original-class computation

Let the 213 checkpoint indices be (S=(s_0<\dots<s_{212})) decoded from the immutable 56B fixture. Their first and last are 1 and 952, with index-gap histogram (3:16,4:77,5:119). For (R=2) and the actual rebuilt (E),
\[
\max_b\min_{s\in S}|E(b)-E(s)|=2,\qquad
\sum_{b=0}^{953}\min_{s\in S}|E(b)-E(s)|=1070.
\]
This reproduces both key guarantees of the previous optimally placed checkpoints, with true, not synthetic, event multiplicities.

Use the exact graph of #2253. Define
\[
u(p)=\max\{b:E(b)\le E(p)+2\},\quad
v(q)=\min\{b:E(b)\ge E(q)-2\}.
\]
There is a directed edge (p\to q) for (p<q) iff (v(q)\le u(p)+1); strict increase implies (q-p\le5). A start is admissible iff (E(p)-E(0)\le2), and a finish iff (E(953)-E(p)\le2). This concrete graph has **4,383 edges**, starts `[0,1,2]` and finishes `[951,952,953]`. The program verifies every constructed edge with a second, direct scan of the intermediate boundaries.

Let (F(1,p)=\mathbf1_{p\text{ admissible finish}}), (F(t,p)=\sum_{p\to q}F(t-1,q)), and
\[
T(E,2,213)=\sum_{p\text{ admissible start}}F(213,p).
\]
Every legal 213-center set corresponds to exactly one directed path of 213 vertices, so the recurrence enumerates **all** admissible sets exactly once, not merely those sharing the original gap histogram. For the original R5 pinned data:
\[
\boxed{T(E,2,213)=959842890872466279854034583824629760000.}
\]
Its minimum fixed-width rank index size for this **declared complete class**, assuming (E, K, R) known to the decoder, is
\[
\boxed{\lceil \log_2 T\rceil=130\ \mathrm{bits},\qquad
\left\lceil\frac{130}{8}\right\rceil=17\ \mathrm{bytes}.}
\]
This is an optimal capacity claim *within that class*, not a universal lower bound on encoding this particular already-known list, a full prefix data structure, or original certificate input.

Lexicographic rank (0-based) of the original 213 centers is
\[
\boxed{291259906744233319113441752826891487978}.
\]
The exact **17-byte big-endian** payload is `00db1e9e1b0580a2258635b9569ae84aea`. Its SHA-256 is `0f7e07e9ca919c50095777a9b9106f87b78d9dd617c4f80be1321ae9e4c42d65`. Inverse ranking restores all 213 original center indices exactly.

## Verification and total-cost interpretation

The provided standard-library program was executed against the declared frozen coefficients and byte-exact center seed. It (i) enumerated all 32,767 nonempty atom masks, (ii) checked q/n population, exact rational wall multiset and known root count, (iii) reconstructed all 954 cumulative event coordinates, (iv) independently checked every emitted graph edge, (v) computed (T) using *two independent dynamic programs*, suffix counting and forward propagation, and (vi) verified exact rank/unrank and all historical center residuals. All assertions passed. JSON output captures the exact integers, SHA-256, coverage, source scope and local resource figures. This is author-side exact finite computation, not a separate mathematical reviewer.

The optional center-list payload comparison is now on **the true pinned fixture**: 56B gap stream, 35B fixed-span multiset stream, 33B fixed-histogram stream, **17B full-radius-class rank**. The original 2,520-byte certified source seed and full prefix-query semantics remain unchanged. In the local Python 3.13 run, suffix DP alone took about 2.886 s with about 6.76 MB tracemalloc peak (run-specific, not a machine-independent bound). Reconstructing 953 walls from coefficients and computing the rank table costs time and memory; the 17B payload saves persistent bytes but **does not yet establish a cold-start or throughput advantage**. Production use must account for this preprocessing or reuse an exact cached rank table.

The previously completed 2,747,520 boundary-prefix comparisons belong to the predecessor, not to a new execution in this note. Their semantics are preserved because the center list and exact event counts are identical; a fresh byte-exact independent end-to-end query run remains useful validation.

## Recovery / next scientific question

The next discriminating unit is to find an exact lower-memory or linear-preprocessing algorithm for *unranking the pinned 17B center payload* without the (K\times W) arbitrary-precision suffix table, or to establish a sharp time/storage tradeoff and full cold-start break-even against 33/35/56B alternatives on the same original query distribution. Retain the current frozen 28-coordinate scientific input and certificate/provenance semantics. This author-side result does not assert formal task CLAIM, Result admission, independent review or P000 promotion; these have their own current native authority.

Artifacts: `VERIFY_R5_PINNED_RADIUS_COVER.py` and `EXACT_OUTPUT.json`. Source: prior PR #2253, PR #2232, original frozen coefficient fixture and the preserved 15-atom source pin.
