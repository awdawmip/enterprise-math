# R763 — Exact event-count saturation for one-chirality triadic port alphabets

Date: 2026-11-13 (Asia/Shanghai). Classification: author-side exact finite candidate-algebra theorem / exhaustive integer computation, NOT_REVIEWED and not native TRIADIC_CLOSURE_E admission. This is a continuation of R762D, not a replacement for P000.

Parent task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`; immutable publication `TP2-8B7E13C5904A2D6F1142`; task science pin `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389` unchanged.

Predecessor: R762D, Draft PR #2265, source commit `5bc9950dfc13359d7ac5c05d630036a0f53bfc6b` (four research artifacts). Current global P000 V4, Source P000 V5, ACTIVE X6 worldview and joint-relation observer-preservation policy remain in force.

## 1. Defined candidate and observer

At a fixed Cell in the native six-axis space, use the six *positive native axis port names* `0,1,2,3,4,5` as a symbolic indexing set (not six new spatial coordinates), with six persistent source labels. A candidate symbol is one orientation of a 3-cycle on a chosen 3-port support. An alphabet `E` has exactly three **distinct** supports and exactly one chosen direction for each. All symbols are assumed repeatedly admissible, independent of the current port-label permutation. This is an algebraic candidate language. It is not yet a proved native force/Link/Port scheduler or V29/V39 map.

With multiplication convention `p∘q` (apply q then p), define `φ: E* → A6` by ordered multiplication and

`S_n(E) = {φ(w) : w∈E*, |w|=n}`.

Define the **exact-event-count saturation index**

`N(E) = min{n≥0 : S_n(E) = A6}`

for alphabets that generate A6. Distinguish this index from the previously studied directed word diameter `D(E) = max_{g∈A6} min{|w|:φ(w)=g}`: the latter permits *at most* D operations, the former requires *exactly* n operations for all endpoints. The observed quantity here is **total candidate-event count** n, not full Source/branch/timestamp or V29's typed vector ledger.

## 2. Structural theorem: any generating alphabet is eventually exact-length complete

**Proposition 1.** Every three-symbol oriented triadic alphabet whose support hypergraph covers six ports and generates `A6` possesses identity words of lengths 3 and 10. Consequently, its directed endpoint language is aperiodic, and every `g∈A6` can be realized by all sufficiently large exact lengths. More concretely, combining R762D's proven finite upper bound `D(E)≤10`, **every** `n≥28` has `S_n(E)=A6`, independent of chirality choices.

*Proof.* Any chosen 3-cycle `a` has order three, so `a^3=e` is a length-three identity word. Among three distinct supports of size three that cover all six ports with connected incidence, at least one pair intersects in exactly one port: if a pair is disjoint, a third distinct triple meeting both cannot avoid a one-port intersection (its intersection sizes sum to 3); if all pairs intersect and none in one port, each meets another in at least two ports and the union of all three supports has size at most five. For 3-cycles `a,b` on supports meeting in exactly one label, `ab` is a 5-cycle regardless of their two possible orientations; thus `(ab)^5=e` is a length-ten identity word. Since every integer `k≥18` is a nonnegative combination `3u+10v` (Frobenius conductor for coprime 3 and 10), append these identity blocks to any word of length `d≤10` reaching `g`, yielding an exact length n realization whenever `n-d≥18`. In particular `n≥28` suffices. Because gcd(3,10)=1, the directed Cayley graph's period is one. □

This provides an analytic finite upper bound without any finite table. The sharper optimal bounds below come from exhaustive exact computation.

## 3. Sharp finite theorem for all 3-support single-chirality alphabets

**Theorem 2 (complete classification).** There are `C(20,3)·2^3=9120` labelled directed alphabets. Exactly 3,840 generate A6; the others generate groups of orders 12 (480 alphabets) and 60 (4,800 alphabets). For all 3,840 A6 alphabets, the exact-event-count saturation index is at most **13**, with the sharp distribution:

| N(E) | A6 directed alphabets |
|---:|---:|
| **8** | **720** |
| 9 | 720 |
| 10 | 960 |
| 12 | 720 |
| 13 | 720 |
| **Total** | **3,840** |

No alphabet reaches all 360 permutations at every exact length starting at 7 or less; 8 is the best possible saturation index in the declared three-generator alphabet family. The worst case is 13. Since `S_n(E)=A6` implies `S_{n+1}(E)=A6` by right multiplication with any fixed generator, these indices are lasting thresholds and not isolated exact-length coincidences.

The old shortest-depth diameter and the new exact-length threshold differ substantially:

| D(E) | N(E) | Alphabets |
|---:|---:|---:|
| 7 | 8 | 720 |
| 8 | 10 | 240 |
| 9 | 9 | 720 |
| 9 | 12 | 720 |
| 9 | 13 | 720 |
| 10 | 10 | 720 |

*Exhaustive certificate.* Enumerate 20 size-three supports of six ports, all 1,140 unordered distinct triples of supports, and all eight binary chirality assignments. Use exact image-tuple permutations, with no floating point. For each alphabet with six covered ports, start `S_0={e}` and iterate `S_{n+1}={p∘a : p∈S_n,a∈E}`, tracking both `S_n` and `∪_{k≤n} S_k`. The first n at which the union has 360 entries is D; the first n at which `S_n` has 360 entries is N. For other support sets, exhaust the subgroup and verify order 12 or 60. The checker asserts all counts above, all D/N cross-tab cells, and two explicit orientations. It also directly enumerates `3^7` and `3^8` words for the optimal family as a separate cross-check. This is a complete calculation on the declared finite domain; it is not an empirical extrapolation to native dynamics.

## 4. Witness: a real gap between shortest-reach and fixed-count reach

Let `E={a=(0 1 2), b=(0 3 4), c=(1 3 5)}` with all three directions forward as listed. This alphabet has `D(E)=7`, but exact-length reachability sizes for n=0,...,8 are

`1, 3, 9, 25, 66, 153, 283, 348, 360`.

Thus 12 of the 360 possible endpoint placements are **not** realized in exactly seven events, although all 360 are realized using at most seven events, and all 360 are realized in exactly eight events. By appending any fixed generator to a saturated layer, every subsequent exact length is also complete.

Keeping the same supports while reversing only b gives `D=8`, `N=10`; its exact-length layer sizes n=0,...,10 are

`1, 3, 9, 25, 67, 155, 274, 338, 356, 359, 360`.

This is a source-preserving orientation sensitivity in the symbolic port model, not a claim of changed native energy, physical time or BRC quantum.

## 5. Observer implications and native interface

**Corollary 3 (saturation of the count-conditioned fiber).** Fix any one of the 3,840 A6 alphabets. For each integer `n≥N(E)` and *every* final port-label permutation `g∈A6`, some permitted candidate word w has `|w|=n`, `φ(w)=g`. In particular, at every `n≥13`, this holds simultaneously for all 3,840 alphabets. Therefore the *total candidate-event count alone*, even when known exactly, leaves the entire 360-state endpoint fiber possible at sufficiently large n. There is no forced endpoint information at that observer resolution.

This is complementary to R762D's conditional V29 ledger no-go. If — and only if — one proves that every admissible repeated candidate triad event produces one fixed unit of some actual V29 occurrence counter with no additional scheduler restriction, then the total counter n would have the stated 360-way endpoint ambiguity after 13 events in these three-generator systems. V29 actually distinguishes typed PASS/TRANSFER coordinates and occurrence sources, so the complete `L` cannot be replaced by n. The exact observer-safe carrier for the stipulated fixed-increment language remains `(φ(w), L(w))`, retaining branch/source metadata when other outputs require it.

For the actual hard target, the open native type-check is still first and second use of the same directed `TRIADIC_CLOSURE_E` Cell/Link/Port event, after V29 PASS/TRANSFER updates and independently defined V39 based-loop transport. State guards, resource exhaustion, source reidentification, rotations or a failed triadic lift could invalidate unconditional repeatability. The finite theorem supplies a sharp control/counterexample test for a proposed bridge, not an automatic native interpretation.

## 6. Validation / provenance / further work

Executable: `research_notes/R763_VERIFY.py`, Python 3 standard library only. Machine evidence: `research_notes/R763_EVIDENCE.json`; no random seeds, tolerance or external numerical packages. The input scientific pin remains `a72226e2430ffa4786321ac86e7f0c599d5f0389`. Prior published candidate R762D is reused at exact Draft PR #2265 and not admitted as a formal Result merely because this paper extends it.

Next exact question: take one actual legal typed triad event and compare the state after first and second identical oriented applications. Derive its admission predicate and its real V29 and V39 increments. If repeatability fails, build the reachable *state-dependent* event graph (including any inventory/ledger/provenance state) and test whether its length-conditioned fibers still saturate; do not substitute the candidate Cayley graph for it.
