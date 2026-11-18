# X6 Unit125 — exact signed triadic-event excess over shortest native N-BRC

**Date:** 2026-11-18. **Task/publication:** `RS-X6-LEGACY-PLANE-RECONCILIATION` / `TP2-B4A441B23DA3159232C2`. **Author/lane:** `EM-X6-FB6990` / `chatgpt-research-onhour-enterprise-math-20260923`. **Status:** `AUTHOR-PROVED / EXACT INTEGER PYTHON EXECUTED / UNREVIEWED / NOT_ADMITTED`.

## Exact original consumer and mathematical scope

The actually inspected current-main program `experiments/x6_triadic_decomposition_brc_v2_20260906/check_triadic_decomposition_brc.py`, Git blob `5d0f2cb88a0d4e437b5025e9050e3044f7831cd4`, defines all 20 three-distinct-axis subsets of six named axes and 160 signed three-axis event types (lines 8–16), the ordered *underlying* event count `U(D)` (lines 19–35), and the exact signed event-incidence count `M(d)=U(D) product_i binom(D_i,d_(i,+))` (lines 91–95). Retain its combinatorial macro-event meaning. Freeze P000 V5 native six signed Cell directions and raw integer endpoint at `59538f585d037d09ef687b28715c4bc1a3f9fe03`; historical comparison at `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.

Take a feasible incidence vector `d=(d_(i,+),d_(i,-))_{i=1}^6` of nonnegative integers, with `D_i=d_(i,+)+d_(i,-)`, `sum_i D_i=3m`, `0<=D_i<=m`. Each macro-event has three *distinct* named axes and one signed step on each, and its three steps may be freely permuted inside a **contiguous** event block. This is a declared free spatial-word expansion, not an assertion about actual force-event dynamics. Let `W(d)` count the resulting distinct length-`3m` signed primitive words, and let `z_i=d_(i,+)-d_(i,-)` be their common native Cell displacement. Put `C(d)=sum_i min(d_(i,+),d_(i,-))`.

## Universal exact geodesic-excess theorem

For **every** feasible `d` (including empty `m=0`),

```
W(d) = 6^m U(D) product_i binom(D_i,d_(i,+));
L_native(z) = sum_i |z_i| = 3m - 2C(d);
B_native(z) = L_native(z)! / product_i |z_i|!;
length_of_each_expanded_word - L_native(z) = 2C(d).
```

Consequently:

1. `C(d)=0` **if and only if** every free event-block expansion is a native shortest signed spatial word; it then has exactly the Unit124 sign-coherent coverage `W(d)<=B_native(z)`, with equality exactly when `max_i D_i<=1`.
2. If `C(d)>0`, **none** of these `W(d)` expanded words is a native shortest path. The macro-event multiplicity is a valid `PATH_FORMAL / EVENT_BRC` count of length-`3m` histories, while the native shortest endpoint `N_BRC` counts a disjoint word population of length `3m-2C(d)`.
3. In the mixed-sign domain there is **no universal finite upper bound** on `W(d)/B_native(z)`.

**Proof:** The original producer assigns `U(D)` ordered unlabeled three-axis event lists. Each event's three distinct signed letters admits exactly six permutations. The ordered signed event list is uniquely recovered by splitting its expanded word at positions `3,6,...,3m`; hence the expansion is injective, giving the first formula. The native endpoint's positive and negative counts cancel *algebraically in the signed displacement* to `z_i`, but individual primitive steps remain actual words: `|d_(i,+)-d_(i,-)|=D_i-2min(d_(i,+),d_(i,-))`. Summing gives the length deficit `2C`. On the signed native axis graph, every word realizing `z` has length at least `sum_i|z_i|`, attained by the words using only the sign of each nonzero coordinate. Therefore the entire expanded word set is geodesic exactly when `C=0`; otherwise every expanded word has positive excess. Unit124 proves the sign-coherent coverage and equality criterion. The shortest-path multinomial is the usual distinct ordering count of its `|z_i|` signed steps.

For the unbounded claim, fix all nonzero signed incidences on axes 1,2,3 to `d_(i,+)=d_(i,-)=k` for each of these three axes, with all other incidences zero. Then `m=2k`, `D=(2k,2k,2k,0,0,0)`, `U(D)=1`, `z=0`, `B_native(0)=1`, and

```
W(d) = 6^(2k) * binom(2k,k)^3.
```

This diverges as `k` increases, whereas the true native shortest endpoint has only the empty word. In particular `k=1`: **288** length-six macro-block words, all net-zero, versus exactly **1** native shortest (empty) word. This is an exact separation of signed endpoint cancellation from *nonnegative BRC coefficient cancellation*; no path mass was algebraically subtracted from the producer.

## Executed exact certificate

An independent checker exhaustively generated all `160^2=25,600` ordered pairs of real source-defined signed event types, grouped them into **5,284** distinct 12-component signed incidence vectors, and compared the observed macro-history counts to `U(D)∏binom(D_i,d_i+)` for every vector. It verified the geodesic identity, multinomial native endpoint count, sign-coherent `W<=B`, and total expanded-word cardinality `25,600*36=921,600`.

| Cancellation `C` | Distinct incidence vectors | Length excess `2C` |
|---|---:|---:|
| 0 | 2,624 | 0 |
| 1 | 2,160 | 2 |
| 2 | 480 | 4 |
| 3 | 20 | 6 |

Total **362,880** free expanded words lie in the sign-coherent classes and **558,720** in nongeodesic mixed-sign classes; there are **64** distinct coherent incidence vectors for which `W=B_native`. The maximum tested `W/B_native` is **288**, for net zero and `C=3`. The family above gives `W=288,279936,373248000,576108288000` for `k=1,2,3,4`, each with `B_native=1`. Checker's CPython ordinary, `-O` and `-OO` modes all exited 0; the three exact JSON outputs are byte-identical, stdout SHA256 `b638c5149346b51db7bd10ab3036754a125afae5f8ce50edfd6b0caff910f337`. All checks are explicit always-on conditions. The universal theorem rests on the symbolic proof; the finite census checks its actual two-event specialization.

**Current consumer disposition:** The original source's `formula_signed_ordered` is `PRESERVE_PATH_BRC_AT_SIGNED_TRIADIC_MACRO_TYPE`. A downstream caller requiring shortest native signed Cell paths must use the native endpoint `z` and the shortest `B_native(z)`; a macro-event history report retains `d`, each event's signed axes, block order, and `C`/length excess. Equating macro signed process count with native shortest endpoint N-BRC is type-incorrect whenever `C>0`; an actual downstream erroneous caller requires its own exact `commit:path:line` verification. This directly refines LP019, LP020, LP023, LP026 and the current 28-LP dependency audit without changing the existing correctly typed producer or frozen original benchmark.

**Still open:** specific historic LP011 native dominant-axis wrong caller, LP019 alleged positive N-BRC subtraction caller, full 28-LP current consumer reachability, Driver `REQUEST_REVISION` and independent original R063 C3/C4 admission (Issue #2416). Prior Unit118 full original integration, Unit124 sign-coherent theorem, original six-file 512-case author benchmark, and all earlier GitHub/Native checkpoints are retained. Native semantic Source checkpoint remains an independent authorized write step.
