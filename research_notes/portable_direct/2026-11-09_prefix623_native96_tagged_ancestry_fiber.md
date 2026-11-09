# PREFIX-623 — A one-step tagged-action ancestry fiber invisible to the complete native 96-port endpoint

Date: 2026-11-09, Asia/Shanghai. Status: **author-side exact construction, independently reviewable; not formally admitted**.

**Input pin:** `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. The original four X6 STAR triples are `(1,3,6),(1,4,5),(2,3,5),(2,4,6)`, the six axis weights are `(1,1,1,1,0,0)`, and the observer uses 48 native phases, 96 bit ports and 576 typed actions. The initial phase probe is `d=e4+e11+e14+e32`, with original native embedding `E(d)`. Exact earlier author-side dependencies: PREFIX-597 (port decoder), PREFIX-617 (eight-state representation), PREFIX-622 (equal-phase/unequal-port pair, [PR #1863](https://github.com/awdawmip/enterprise-math/pull/1863), commit `321b5766a309733defc73998382fa4f33bb187a3`). Their Driver review status is not promoted by this note.

## Observer question

Let `A(s)` denote the **original** 96×96 typed-action update at gate `s>=0`. Its 576 distinct action labels `α=(i,j,u,v)` have nonnegative rational weights `w_α(s)`. The current port observer is the 96-vector `r_n`; the more discriminating *one-step tagged action-flow observer* reports each
```
J_α(r_{n-1},s) = w_α(s) r_{n-1}[2j+v],
```
including the identity of the source port at the **previous** instant. Summing these action flows at each destination gives `r_n=A(s)r_{n-1}`. This is a native positive path-flow observer: no signed cancellation is postulated for an individual path. The basic question is whether knowing the entire `r_n` and all common *future* gates determines these 576 preceding labelled flows.

## Theorem 623.1 — exact two-history endpoint collision with positive tagged ancestry separation

Consider two original native six-step gate histories, each starting from exactly `E(d)`:

```
A = (1,1,1,1,2,1)
B = (2,1,1,1,1,1).
```

After the first five native steps, the complete 48-phase readings coincide. The 96-port vectors `r^A_5,r^B_5` differ by

```
r^A_5-r^B_5 = 8 h,
h := sum_{j in {3,14,15}} (e_(2j+1)-e_(2j)).
```

For every common next nonnegative gate `s`, **`A(s)h=0`**, and consequently the full native terminal 96-port vectors coincide: `r^A_6=r^B_6` for `s=1` (indeed for any shared `s>=0`). Applying any further identical gate sequence maintains equality of all current native port readouts.

Nevertheless, when `s=1`, the positive tagged flow attributable to the *penultimate* source port `(phase 14,bit 1)`, native port index 29, differs. This source has exactly six positive outgoing typed actions, each with weight 1. The source masses are respectively `r^A_5[29]=48`, `r^B_5[29]=40`. The sum of outgoing tagged masses is therefore exactly

```
J^A_{source29}=6*48=288;    J^B_{source29}=6*40=240.
```

The 576-action tensors differ at exactly **12 labelled action coordinates**. In particular, each of the six destination ports `34,35,80,81,82,83` receives a positive source-29 tagged contribution 48 in history A and 40 in history B, although its **total** port output after summing all ancestral sources is identical in both histories.

**Proof.** The exact first-five-step identities are the PREFIX-622 source pair, verified again using the original enumerated actions in the appended checker. At the source coordinates `j=3,14,15` (none is the special gate phase `g=4`), the action coefficient for input bit 0 equals that for input bit 1 at every destination, since the sole bit-dependent gate coefficient is supported at the marked source phase `g=4`. Therefore each `e_(2j+1)-e_(2j)` lies in `ker A(s)` for every `s>=0`. In particular `A(s)h=0`. The tagged-action masses, computed **before** summation by destination, use their actual source port and remain different. Enumerating original predecessor pairs gives the six stated positive actions from source port 29. This establishes both the exact endpoint equality and the nonzero positive path statistic. ∎

The collision is stronger than the previous equal-48/different-96 example: **even a complete current 96-port observation cannot reconstruct the just-completed tagged action flow**. The distinction is a real (finite-memory) observer-language difference, not a claim that identical present port states diverge under the same future port update.

## Theorem 623.2 — one additional scalar is sharp for all 576 one-step action flows, given the predecessor phase vector

Assume the complete predecessor 48-phase readout `v=C r_{n-1}`, the subsequent gate `s>=0`, and that `r_{n-1}` belongs to the original X6-BRC reachable tail class after at least two native steps. Let `g=4` and `H={3,14,15}`, and write the predecessor bit imbalance scalar `δ`. The previously proved native decoder has the exact form

```
r[g,0]=r[g,1]=v[g],
r[i,0]=(v[i]-1_(i in H)*δ)/2, i != g,
r[i,1]=(v[i]+1_(i in H)*δ)/2, i != g.
```

Thus **one scalar `δ` in addition to `v` and `s` recovers every one of the 576 typed-action masses** via `J_α=w_α(s)r_{n-1}[source(α)]`. It also recovers the complete aggregate endpoint vector as their destination sums.

For the four-point-probe family above, **zero such scalars are insufficient**, even if the full *terminal* 96-port vector is supplied in addition to the predecessor phases: histories A and B have identical `v`, equal final `r_6`, but different `δ_A=16, δ_B=0` and different tagged-action flows. Hence the minimum additional scalar count for this conditional one-step action-tensor query is precisely **one**.

**Proof.** The decoder establishes sufficiency directly. Theorem 623.1 supplies the two-input lower-bound witness. ∎

This is a conditional **one-step** conservation/reconstruction statement; for multiple ancestral steps one must preserve a suitable earlier readout or tagged history state. The current endpoint is a sufficient state for **future endpoint-only** questions under common gates, but not for this declared path-label observer.

## Reproducible original-native evidence

`PREFIX623_native_ancestry_checker.py` is a standalone Python-standard-library `fractions.Fraction` checker. It reconstructs all 48 STAR phases, enumerates all 576 original typed-action weights, propagates both six-gate histories, tests `A(0)h=A(1)h=0` (which certifies affine `A(s)h=0`), compares all 96 terminal ports, and constructs all 576 labelled action masses before endpoint summation. It additionally verifies the `(v,δ)` decoder for both histories, six positive outgoing source-29 contributions and four later shared gates. The complete 96-vector and tagged port differences are in the companion JSON. Result: all assertions passed on exact rational arithmetic.

The code reuses the original action enumerator and phase/port definitions of PREFIX-622 verbatim in its setup; no substitute propagation model is introduced.

## Continuation

1. Extend the one-step action-tensor result to a finite horizon `k` with **explicit intermediate state/observer data**: given `v_{n-k}`, its `δ`, and the subsequent `k` gates, build the ordered labelled path tensor by repeated native action composition; determine whether a smaller factorized representation suffices for a declared family of path queries.
2. Characterize the image/kernel of the map from nonnegative tagged one-step flow vectors to the aggregate current 96-port state on the reachable four-point-probe family; measure minimal additional coordinates for *specific requested provenance queries*, not an untyped unrestricted history promise.
3. Independent Driver review and native Source activity/result intake remain separate from this author-side saved artifact. Formal CLAIM is not asserted.
