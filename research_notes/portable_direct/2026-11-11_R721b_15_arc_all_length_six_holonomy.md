# R721b — 15 directed arcs realize all six CNB V17 holonomies at every length

Date: 2026-11-11 (Asia/Shanghai). Research line: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`. Scientific context: frozen Source `a72226e2430ffa4786321ac86e7f0c599d5f0389`; current native P000 unchanged. Independent author-side exact combinatorial construction; review pending.

## Proposition: unconditional all-length 15-arc construction in the declared permission model

Within the five accessible axes `01234` of the unchanged native X6 system, consider directed transitions between three-axis triads that replace exactly one active axis. Start at triad `S=012` with ordered V17 slot frame `012`. A positive BRC branch is an ordered rooted closed directed path of length `m`, with cyclic non-backtracking: no transition immediately reverses the preceding triad state, including across the root seam.

**Theorem R721b.** The directed edge set

```text
012>024  012>123  012>124
013>012  013>023
023>012  023>013
024>023  024>124
123>013  123>023  123>134
124>123  124>134
134>013
```

has exactly 15 arcs, all legal Johnson-neighbor replacements. For **every integer `m>=4`**, its rooted cyclic non-backtracking closed walks realize **all six** final V17 permutations of `012`:

```
H_m(E) = {012, 021, 102, 120, 201, 210}.
```

This is a 15/60 = **25%** directed-arc existence result. No fixed set of nine R719q identity-repair triangles is assumed. Hence it improves the unconstrained upper bound of 18 arcs while leaving R721's sharp result for the nine-repair-arc family unchanged.

## Finite-state proof for every length

Let a state be a **four-tuple**

```
(p, v, f, q)
```

where `p` is the previous triad, `v` the present triad, `f` the ordered three-axis slot frame, and `q` the very first neighbor after root `S`. The last component is necessary for the cyclic seam condition at a final return.

For any arc `v>w` in the specified 15-edge graph with `w != p`, define the deterministic lifted transition

```
(p,v,f,q) -> (v,w,replace_slot(f,w),q).
```

Here `replace_slot(f,w)` replaces the unique axis not in `w` by the unique new axis in `w`, in its original slot. At length one, initialize

```
D_1 = {(S,w,replace_slot(S,w),w): S>w in E}.
```

Define `D_{t+1}=F(D_t)` by union of all legal lifted successors. A length `m>=2` path is a permitted cyclic non-backtracking rooted return with final ordered frame `h` precisely when there is a transition from some state in `D_{m-1}` to a state with `w=S`, and its last pre-root triad `v` differs from `q`. This is checked with the full four-tuple rather than projecting away the seam or slot frame.

The exact Boolean-state enumeration in `R721B_15_ARC_UNBOUNDED_VERIFY.py` gives

```
|D_1|=3, |D_2|=7, |D_3|=13, |D_4|=25, |D_5|=55,
|D_6|=113, |D_7|=183, |D_8|=244, |D_9|=268,
|D_10|=270, |D_11|=270, and D_10 = D_11 EXACTLY.
```

The last equality is of **the complete sets of 270 typed four-tuples**, not just their cardinalities. Since `F` is a deterministic set map, mathematical induction gives `D_{10+k}=D_{10}` for all integers `k>=0`. The admissible root-return holonomy set consequently stabilizes as well. Direct exact enumeration shows all six frames at each `m=4,5,...,11`; therefore all six occur for every integer `m>=4`. This closes the infinite claim by a finite exact state certificate.

## Independent positive-path histogram check

A separate exhaustive literal DFS in the same verifier counts the actual positive BRC histories rather than just Boolean support. Ordered frame counts:

| m | 012 | 021 | 102 | 120 | 201 | 210 |
|---|---:|---:|---:|---:|---:|---:|
| 4 | 1 | 1 | 1 | 1 | 1 | 2 |
| 5 | 1 | 1 | 1 | 3 | 1 | 1 |
| 6 | 3 | 1 | 2 | 3 | 2 | 3 |
| 7 | 8 | 6 | 6 | 7 | 7 | 9 |

These counts independently confirm the first four support checks; the larger-length proof uses the typed Boolean fixed-point certificate, which preserves exactly the information necessary for this declared existential relation-state observer. For counting branch multiplicity or future provenance-sensitive dynamics, retain the full positive path carrier.

Primary code: `research_notes/portable_direct/R721B_15_ARC_UNBOUNDED_VERIFY.py`. Computed evidence: `research_notes/portable_direct/R721B_15_ARC_UNBOUNDED_RESULTS.json`. Status: `R721B_15_ARC_ALL_LENGTHS_EXACT_PASS`. The script uses Python's standard library and exact integer/set operations.

## Relation to R719q and R721; next questions

R719q (commit `421b6ae328fa5ee9509b7b43c0fdd6e3ca46d85a`, Draft PR #2086) established a nine-repair-triangle finite sufficient certificate and gave 18 arcs. R721 (same PR as this R721b) proves **18 is the exact minimum** when those nine prescribed arcs are required. R721b supplies an *alternative finite-state certificate* with 15 arcs and no such repair requirement. There is currently no proven 15-arc global minimum over all directed J(5,3) permissions.

Next: search for 14-or-fewer-arc all-length six-state carriers and prove a global lower bound, or derive smaller independent periodicity certificates. Map these directed triad permissions to actual native Link/Port/Cell inventory and event-time dependency rules. This is a combinatorial candidate, not a claim of native V29 deployment or a new ontology.

BRC typing: histories are labeled, ordered positive count branches. The Boolean quotient `D_m` is justified for exactly the declared future operation (appending more permission arcs under the tracked tuple) and existential final V17 holonomy observation; it is not a multiplicity-preserving BRC observer.
