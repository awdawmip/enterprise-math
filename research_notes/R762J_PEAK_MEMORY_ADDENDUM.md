# R762J addendum — exact minimal history-memory repair for triadic co-presence

Date: 2026-11-13 Asia/Shanghai. Status: AUTHOR-SIDE EXACT PROOF + EXACT FINITE VERIFIER; NOT_REVIEWED.

Continuation of the proven source-tagged U/A/C N-BRC carrier in `R762J_TYPED_BRC_TRISTATE.md` (same Draft PR #2295), in turn based on R762I PR #2292. Parent Task `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, publication `TP2-8B7E13C5904A2D6F1142`, frozen scientific source `a72226e2430ffa4786321ac86e7f0c599d5f0389`. The carrier is combinatorial, not a native force-law construction.

## 1. History-sensitive observation

Take n independently named sources. A source has state U (not yet outbound), A (at assigned signed X6 port), C (returned, no further move). Exactly one named `O_i: U→A` and `I_i: A→C` is allowed. Global events occur sequentially. Write `s∈{U,A,C}^n`, `a(s)=#{i:s_i=A}`, `c(s)=#{i:s_i=C}`; `P` is the maximum value of a(s) attained **so far** (including the initial state).

The earlier theorem proved that `s` alone is minimal for every *future named-event legality*. The new observation asks to preserve both that legality and the **historical peak co-presence** `P` (or the boolean `H=[P=n]` meaning all n assigned ports were simultaneously occupied at some past/current state).

## 2. Exact reachability of each peak

**Theorem A.** For any reachable ternary vector s, precisely the following peaks occur among its source-named histories:

- if `a+c=0`, only `P=0`;
- otherwise every integer `P` in the closed interval `max(1,a) ≤ P ≤ a+c` occurs, and no other peak occurs.

**Proof.** At any current state, `a` sources are present, so peak ≥a. Once any source has gone outbound, peak ≥1. At most `a+c` sources have ever gone outbound, so peak ≤a+c. For each integer `p` in this interval, construct a history. If `a>0`, choose exactly `p-a` of the `c` completed sources; process the other completed sources as individual O/I pairs, then open all a future-active sources and the selected p−a future-completed sources (attaining occupancy p), finally close the selected completed ones. If `a=0` and `c>0`, process c−p completed sources as pairs, then open p completed sources simultaneously and close them; peak is p. Each source status and its named provenance are maintained. Hence the stated bounds are exact.

## 3. Minimum complete observer and closed cardinality

**Theorem B.** For the observer consisting of current named-event future legality **plus** historical peak P (queriable now and propagated by P' = max(P,a(s')) for any future allowed event), `(s,P)` is a minimal sufficient deterministic state. Its exact reachable-state count is

```text
K_n = (n+3) 3^(n-1) - 2^n + 1   for all n≥1.
```

In particular, n=3 has precisely **47 distinguishable states**, requiring **6 fixed-width bits** instead of the 27 states/5 bits needed when only named future-event permission is observed.

**Proof.** Theorem A enumerates all reachable (s,P). The update depends only on s and P, hence is sufficient. If s differs, the source-name-specific one-letter legal continuation set differs in some coordinate (U permits O_i, A permits I_i, C permits neither); if P differs, the current historical peak readout differs. Therefore no two distinct pairs can be merged under this combined observation. To count: temporarily assign c+1 choices of peak to every ternary vector, giving `sum_s(c(s)+1)=3^n+n3^(n-1)`. A vector without active sources but with c>0 actually has c peaks rather than c+1; subtract one for each of the `2^n−1` such vectors. The all-U vector has one peak and requires no correction. The exact total is `K_n`.

**Theorem C.** Retain instead the boolean historical flag `H=[P=n]`. For n≥2, the minimal sufficient named-future plus historical-full-co-presence observer has

```text
B_n = 3^n+2^n−1
```

states; for n=1 it has three states. In the triadic case n=3, there are **34** states and again **6 fixed-width bits**. Proof: For a vector with at least one U, H=0 because not all sources ever went outbound. For s=A^n, H=1. For each vector with no U and at least one C (there are 2^n−1 such vectors), histories can (i) close one source before opening all the remaining ones, attaining H=0 when n≥2, or (ii) open all n before any close, attaining H=1. All distinct flags are immediately observable, and suffix legality again separates distinct s. H evolves by OR with the test `s'=A^n`.

A terminal example for three sources demonstrates the actual residual: `O1 I1 O2 I2 O3 I3` and `O1 O2 O3 I1 I2 I3` have identical final ternary state `CCC`, identical endpoint/branch counts of named O/I actions, and no allowed future named action; their peak values are respectively 1 and 3, and their historical full-triad flag values are 0 and 1. Hence source status alone cannot certify whether a triad ever shared one instant of the *abstract serial-event model*.

## 4. Exact reproducibility, transfer question

`R762J_PEAK_VERIFY.js` performs full explicit state graph expansion for n=1..8, verifies every status fiber equals the interval from Theorem A, and compares counts against Theorems B and C. `R762J_PEAK_EVIDENCE.json` contains its exact output; n=8 has 23,802 peak-augmented states and 6,816 full-triad-flag augmented states. This is a pure finite signed-X6 source-history/N-BRC branch-observer construction; no classical π, trig, or physical model-update arithmetic occurs.

The source-signaled **next admissibility test** is whether actual `TRIADIC_CLOSURE_E` needs *current joint occupancy*, *historical all-port co-presence*, or a stronger simultaneous equal-quantum force incidence. The proof identifies the correct retained memories for each candidate observer; only a source-native event predicate and V29/V39 update may decide which field is physically required. Event index is not a measured heartbeat interval. P000, frozen science and ACTIVE worldview remain unchanged. No formal Result, CLAIM, independent Driver review or physical propagation is claimed.
