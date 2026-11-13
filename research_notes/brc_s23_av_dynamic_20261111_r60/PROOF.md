# R60 — Exact dynamic timestamp–phase index for labelled youngest-source observations

Date: 2026-11-11. Research mode: independent author-side TASK_RESEARCH, `EM-DIRECT-AE64D7`; activity `RA-81917B99F7F23B4EDA201DE3`. Frozen science pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Inputs: R58 commit `b265aed65d7991ab9b8e4d0572cbbd2bd6cc1966` and R59 Draft PR #2051, commit `e6a842a88ac1459ab8e039f0f1cfa6a4bbc88098`. Auxiliary rational/irrational circle-rotation observer; P000/X6 worldview untouched. Independent mathematical review pending.

## Exact observer and dynamic operation

Let `0<θ<1` be irrational, `m≥1`, and let original historical labels `z=0,...,m−1` denote the circular half-open arcs `A_z=[{zθ},{z_next θ})`, where `z_next` is the next label in increasing phase order. For any observation time `j∈Z`, phase `x∈R/Z`, and arbitrary finite source set `S ⊂ {t∈Z:t<j}`, source `t` has age `r=j−t` and phase `{x−(j−t)θ}`. Define

`τ_z(j,x,S)=min{j−t : t∈S, {x−(j−t)θ}∈A_z}`

with EMPTY when the set is empty. The state stores original source times and historical labels, and arbitrary individual insertion/deletion must be supported.

## Theorem R60-A: translated-arc maximum-time representation

Set `v_t={tθ}` and `u={x−jθ}`, and translate `E_z=A_z−u` circularly. Then exactly

`τ_z(j,x,S)=j−max{t∈S:v_t∈E_z}`

where a missing maximum means EMPTY.

**Proof.** The circle-group identity `{x−(j−t)θ}={u+v_t}` makes membership in `A_z` equivalent to membership of `v_t` in translated `E_z`. Because `j` is fixed, `min(j−t)=j−max(t)`. Translation is a bijection preserving half-open membership, source identities and original historical labels. QED.

**Dynamic index.** Store a balanced BST ordered by `(v_t,t)`, with each subtree augmented by the maximum original timestamp `t`. Each translated historical arc is at most two ordinary ordered-key ranges. An augmented tree performs each insertion/deletion and each such range maximum in expected `O(log(n+1))` word operations using independent random-priority treaps (or worst-case logarithmic balanced BST), where `n=|S|`. Therefore `m` labelled youngest outputs take `O(m log(n+1))` expected word operations plus `m` writes, with `O(n+m)` words of space. Starting from an unsorted source set and historical boundaries costs `O(n log(n+1)+m log(m+1))` comparisons/updates.

For `m=1`, the sole circular arc covers every source; the answer is `j−max(S)` or EMPTY. An empty source set yields an all-EMPTY vector. Equal source phases are ordered by timestamp to retain distinct sources. A chronological rolling-window change `S_j={j−H,...,j−1}` of distance `0<d<H` costs `2d` node updates; for `d≥H`, build the new canonical H-source index afresh. Absolute time shifts are tracked in `j`, not mistaken for extra spatial coordinates.

The randomized balancing bound assumes priorities independent of a fixed oblivious update sequence; deterministic height balancing provides the worst-case variant. A full-owner vector would still require its own H-field output cost. The index preserves every source timestamp and original label, hence supports arbitrary later source deletion; merely saving the currently youngest source would fail the R58 witness `{1,2}` vs `{2}` after deleting 2.

## Exact rational implementation and bit cost

For an exact rational `θ=p/q` with `0<p<q`, represent circle phases as integer residues modulo `M=2q`. Store source key `(2tp mod M,t)`. If `x` is twice the observation phase, rotate each original boundary `2zp mod M` by `−(x−2jp)` and query the resulting half-open arc for maximum timestamp. The independent oracle instead takes source phase `(x+2(t−j)p) mod M`, finds its original historical arc, and directly scans the maximum time per original label.

Integer modulus and multiplication require bit operations dependent on `b=ceil(log₂(q+1))` and `log₂(|t|+2)`; `O(log n)` tree operations are not unit-bit costs. Constructing the rational parameter enclosure, source/history phase ordering, initial index, outputs and verification also contribute. For contiguous unmutated windows, existing R59 static RMQ can be faster; this theorem targets arbitrary inserted/deleted source identities and repeated queries.

The auxiliary rational checker verifies exact finite instances. It relies on the previously frozen S23 parameter interval/order certificate for relating rational endpoint tests to that frozen instance; it establishes no new X6 dynamical law.

## Actual executed verification, 2026-11-11

Executed locally using Python exact integer arithmetic and independent direct source classification:

- **480 small cases**: `m=1..8`, `H=1..12`, five seeded `p/1009` cases per pair, `j∈{−10¹⁸,1000,10¹⁸}`. There were **6,720 exact vector comparisons** and **10,336 post-initialization insert/delete mutations** across arbitrary changes and rolling windows. All original-label youngest vectors agreed with the independent full-source oracle.
- **Frozen S23/AV**: `m=128,H=225`, both exact rational endpoints `p∈{262204504569236716045286,262204504569236716045287}`, `q=10²⁴`, observation `J=10¹²+128`. Seventeen checkpoint ranks per endpoint and **2,176 label outputs per endpoint** agreed with both the independent direct oracle and an independently executed floor-sum inversion checker. Removed three arbitrary sources, checked, reinserted, checked, and rebuilt at `J+10⁶` to verify relative-phase invariance.
- **Large mutation regime**: `m=5,H=100003`, initialized 100,003 active sources, performed **500 chronological shifts/1,000 node mutations**, and verified six query states with a full direct oracle. All matched.

An initial circular-seam handling bug was corrected before final verification; the final executed test explicitly distinguishes whether the **translated** arc crosses the seam. An initially slow `O(H)` historical-future-source guard was changed to an `O(1)` check using the root's augmented maximum timestamp. Execution and counts are author verification, without independent mathematical review or formal shared-task acceptance.

## Complementary floor-sum observer

The same research run separately implemented an index-free rational youngest-only route (after discovering contemporaneous R59 Draft PR #2051 had already published the static circular RMQ). For `M=2q`, `a=(M−2p) mod M`, `b=(x+a) mod M`, set

`FS_t(c)=sum_{i=0}^{t−1}floor((ai+b+M−c)/M)`.

The hit count for a source-age prefix of length `t` and linear target arc `[l,u)` equals `FS_t(l)−FS_t(u)`; a seam-crossing arc adds `t` and takes the complementary orientation. Binary-search the first `t` with a hit. This yields `O(m log H log M)` Euclidean quotient operations/checkpoint (beyond constructing boundary phases), `O(m)` auxiliary memory and no H-node index. Its checker passed 1,440 small cases/8,640 checkpoints, both frozen S23 endpoints and a long `m=3,H=20000,Q=60` experiment. The long 60-query benchmark's readout-only medians were **11.22 ms floor sum vs 178.77 ms direct scan**, five repetitions on one environment; frozen S23 medians were **105.9 ms floor sum vs 1.5 ms direct scan**. These are regime-specific engineering comparisons, not asymptotic bit-cost proofs.

This is a distinct implementation complement, preserving all original-label result coordinates. BRC use is provenance/observer preservation with a typed finite arithmetic substrate; neither scalar counting nor branch mass replaces the retained source population.

## R61 next discriminating unit

Find the best dynamic strategy when only a few original history labels are queried; investigate versioned/persistent indexes for many past checkpoints, plus rigorous irrational-order stability when absolute source times are arbitrarily large. Measure end-to-end exact bit costs against R49 two-state caching, R56 split-block merge, R58 grouped checkpoints and R59 static RMQ. Preserve source pin and current shared-task Owner/CLAIM boundary. 

Project activity: `RA-81917B99F7F23B4EDA201DE3`; this author-side document is a durable scientific frontier, not a formal Result/Review/CLAIM.
