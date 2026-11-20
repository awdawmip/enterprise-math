# R762HL — Cyclic seam-invariant positive-BRC flip complexity

**Research provenance:** Task `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, immutable publication `TP2-8B7E13C5904A2D6F1142`; preceding R762HK scientific source `enterprise-math@0778045cdbe977bf86e1d3f7557162e1ed6b33d8` (Draft PR #2879). Historical Researcher `EM-X6-3050F6`; source publication is not a new CLAIM. Scientific inputs remain frozen at `enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`, including `p000_reality_foundation.json`, the triadic balance definition, the X6 Cell torsor and the relevant joint-relation preservation contract. Author mathematical proof and independent finite computation; `NOT_REVIEWED`.

**Scope.** P000 fixes the six original spatial axes, independent time, primitive triadic stability, and the special Enterprise orthogonality. This note studies the previously declared *composite* candidate: a named closed walk of adjacent two-axis Ports, each transition supported on a three-axis subset of the six-dimensional Cell. These signed candidate transitions have not been certified as primitive `TRIADIC_CLOSURE_E` force events. BRC counts here are nonnegative integer multiplicities of ordered sources, not signed force masses.

## Definitions

Let `m>0` be even, and `P_0,P_1,...,P_m=P_0` a time-ordered closed walk of named two-axis Ports in `{0,...,5}`. Every adjacent pair shares exactly one axis. Write `h_t=1_{P_t ∪ P_{t+1}} ∈ {0,1}^6`, with exactly three nonzero entries, and `α_t=(-1)^t`. A zero-Cell signing is `ε_t ∈ {±1}` with `Σ_t ε_t h_t=0`.

Every signing has a unique binary word `b_t∈{0,1}` such that `ε_t=α_t(-1)^{b_t}`. The family `S` of zero-Cell binary words is closed under complement `b↦1-b` by global sign reversal. Let `k(b)` count maximal nonempty intervals of 1-bits in the **linear** word (initial external bit zero), and let

`r(b)=Σ_{t=0}^{m-1}[b_{t-1}=0,b_t=1]` (indices modulo `m`)

count 1-runs on the **cyclic** word. Both constant cyclic words have `r=0`. The cyclic generating polynomial is `C_m(u)=Σ_{b∈S}u^{r(b)}`. The R762HK linear generating polynomial at a chosen starting event `s` is denoted `B_m^{(s)}(u)`.

## HL1. Exact seam-invariance theorem

**Proposition.** For every such even-length candidate closed Port source history with a zero-Cell signing, the minimum linear flip-block count over all its zero-Cell signings is *independent* of which event is declared first. It is also unchanged by reversing the chronological order of the source history. At every seam,

`min_{b∈S} k(b) = min_{b∈S} r(b)`.

**Proof.** For every binary cyclic word cut at any seam, there is an exact identity

`k(b)=r(b)+[b_{m-1}=b_0=1]`.

Complementing the whole word preserves the cyclic run count, including the constant-word pair: `r(1-b)=r(b)`. The seam-boundary indicator cannot equal 1 simultaneously for `b` and `1-b`. Therefore

`min(k(b),k(1-b))=r(b)`.

Because `S` is complement closed, its minimum linear run count equals its minimum cyclic count. Rotating the source history by `s` changes its alternating reference signs by a common factor `(-1)^s`, so its binary words are precisely cyclic rotations of the original words, with an optional global complement. Reversing the order produces reversed binary words with an optional complement. Cyclic run counts are invariant under rotation, reversal and complement. The same minimum therefore holds for all seams and either chronological orientation. QED.

**Residual consequence.** The full linear histogram depends on which event is designated first, while its minimized block cost does not. Thus fixing a seam is unnecessary for the minimal-repair observer; other BRC statistics can still retain seam information.

## HL2. Exact cyclic positive-source transfer and seam averaging

Write `V=Σ_t α_t h_t`, `x^w=∏_{i=0}^5 x_i^{w_i}` in the six-variable integer Laurent polynomial ring. Use the R762HK two-state transfer

`T_t(p,q)=u^{(1-p)q} x^{q α_t h_t}`, `p,q∈{0,1}`.

**Proposition.** The cyclic positive-source histogram obeys the exact coefficient identity

`C_m(u)=[x^{V/2}] tr(T_0 T_1 ··· T_{m-1})`.

If some component of `V` is odd, the expression is interpreted as zero. Writing `C_m(u)=Σ_r N_r u^r`, the total of all `m` seam-dependent linear histograms satisfies

`Σ_{s=0}^{m-1} B_m^{(s)}(u) = Σ_r N_r ((m/2+r)u^r+(m/2-r)u^{r+1})`.

Every `N_r` is an **even nonnegative integer**. The identity includes the zero-runs/constant-word cases.

**Proof.** In the matrix product, tracing identifies the initial previous-bit state with the final bit. Consequently every cyclic binary source word appears exactly once and has `u` exponent equal to its cyclic number of `0→1` transitions, namely `r(b)`. Its Laurent exponent is `Σ_t b_t α_t h_t`. Since signed displacement is `V-2Σ_t b_t α_t h_t`, taking the coefficient at `V/2` retains exactly the zero-Cell source words, with positive integer coefficients.

At seam `s`, a given cyclic bit word has linear block count `r(b)+[b_{s-1}=b_s=1]`. The optional complement caused by an odd seam permutation does not change the *total* polynomial because `S` is complement closed. For a complement pair `(b,1-b)`, the sum of their counts of adjacent `11` pairs equals the number of equal adjacent pairs, `m-2r(b)`; every cyclic binary word has `2r` unequal adjacent pairs. Thus for the `N_r` signings of cyclic run count `r`, summed over all seams, the number of exponent-`r+1` contributions is `N_r(m/2-r)`; the remaining `N_r(m/2+r)` contributions have exponent `r`. Complementation is fixed-point-free and preserves `r`, making every `N_r` even. QED.

In particular, `C_m` is a seam-invariant positive BRC carrier sufficient to reconstruct the *seam-averaged* linear block histogram exactly; it need not determine an individual-seam histogram or all future concatenation behavior.

## New exact computation on the R762HK 14-event witness

Use the unchanged closed Port source

`01 → 15 → 12 → 25 → 24 → 04 → 05 → 03 → 04 → 24 → 23 → 25 → 35 → 05 → 01`.

Its six-axis support incidence is `(8,4,8,6,6,10)`, its alternating residual is `V=(2,0,0,0,-2,0)`, and exactly 104 of the `2^14=16,384` signing words have zero Cell displacement. The previously checked linear histogram is

`B_14^{(0)}(u)=20u²+46u³+36u⁴+2u⁵`.

**New cyclic histogram:**

`C_14(u)=36u²+52u³+16u⁴`.

The minimum repair cost equals **2 for every one of the 14 possible starting seams and for reversed order**. Across those seams there are **10 distinct linear histograms**. Their exact sum is

`Σ_s B_14^{(s)}(u)=324u²+700u³+384u⁴+48u⁵`.

Substituting `(N_2,N_3,N_4)=(36,52,16)` into the HL2 formula reproduces all four coefficients. All polynomials evaluate to the required total of 104 completions per seam; the seam total is 1,456.

## Verification, provenance and open questions

`R762HL_CHECK.js` is a stand-alone Node.js 18+ exact-integer checker. It checks every Port transition, independently enumerates all 16,384 bit assignments at each of 14 seams plus reversal, verifies the cyclic trace using a second map-based two-state Laurent dynamic program, and checks the universal complement/run lemma on all bit strings of even lengths 2–12. `R762HL_EVIDENCE.json` holds the reproducible exact outputs. The local integer computation returned `PASS`; it makes no claim of independent mathematical review.

Next: determine the minimum cyclic flip cost on longer Port histories and the remaining 10/12-event one-block question; separately seek a parity-even *unsignable* Port history, rather than equating a two-block obstruction with unsignability. Identify which extra Port/phase/provenance residues are needed under arbitrary future BRC composition. The task's P000-native force/Cell/Link/Port/time/rotation `TRIADIC_CLOSURE_E` bridge remains open.
