# R5 — First three exact fixed mixed-fault noise chambers

2026-11-17. Frozen science input: `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Research status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.

## Model and new theorem

The frozen 954-event derived indexed-center observer has 256 effective closure masks `b=0,...,255` and 101 integer query budgets `k=214,...,314`. An exact query at `k` returns the positive path-count `N_b(k)`, computed by the requirement-cohort subset-zeta identity `N_b(k)=Σ_{T⊆b} A_T(k)`. This is a typed, provenance-derived scalar observer; it is not an assertion that native X6 path/signed/phase states are fully determined by it.

Choose a **fixed nonadaptive multiset** of budgets, allowing repetitions, with total cost `Σk`. A non-erased, non-corrupted reading is any real `y` with `|y-N_b(k)|≤η` for common `η≥0`. The adversary may additionally mark up to `e` samples as erased and arbitrarily replace up to `f` other samples. Require unique identification of all 256 masks for every allowed observation/fault record. Let `r=e+2f+1` and `τ=2η`.

Set the **exact integers**

- `Δ0=76289178155959966960189440`;
- `Δ1=3133722521542003559403356160`;
- `Δ2=13883516118328421520506880000`.

**Theorem (three sharp chambers, all e,f).** For all nonnegative integers `e,f`, the least fixed-query total budget is

| Inclusive lower `τ` | Exclusive upper `τ` | Unique optimal multiset (order irrelevant) | Exact cost |
|---|---|---|---|
| `0` | `Δ0` | `r` copies each of 214, 223, 294 | `731r` |
| `Δ0` | `Δ1` | `r` copies each of 214, 223, 295 | `732r` |
| `Δ1` | `Δ2` | `r` copies each of 214, 223, 296 | `733r` |

All boundaries are exact: equality belongs to the next chamber. At `τ=Δ2`, the third displayed multiset loses its separation guarantee; no assertion about the next cost chamber is made here.

This extends the previously established `τ<Δ0` mixed erasure/Byzantine/analog-noise law into two additional nonempty noise intervals, with complete cost optimality and uniqueness for **arbitrary** finite `e,f`.

## Proof

**(A) Exact noise/error/erasure decoding criterion.** For masks `a≠b`, let
`D_τ(a,b)={k:|N_a(k)-N_b(k)|>τ}`. For a proposed query multiset `Q`, let `d_τ(a,b;Q)` be the number of query *positions* in `D_τ(a,b)`, including repetitions.

The necessary and sufficient condition for worst-case decoding is

`min_{a≠b} d_τ(a,b;Q) ≥ e+2f+1 = r`.

Indeed, at any position with separation larger than `2η`, the two closed observation intervals are disjoint. Even after `e` erasures, more than `2f` such positions remain when the condition holds, so no single record can be consistent with both masks after at most `f` arbitrary replacements for each mask. Conversely, if `d_τ≤e+2f`, erase up to `e` strongly distinct positions, split the remainder between the two masks (each blamed for at most `f` replacements), and select common values on all weakly distinct positions from the overlapping intervals. This constructs a record compatible with both.

**(B) Three disjoint witnesses.** Exhaustive exact integer checking on all 101 budgets establishes the *complete* nonzero-disagreement supports

- masks (16,17): `214..221`;
- masks (16,80): `223..291`;
- masks (16,32): `294..313`.

The sets are disjoint. Consequently a feasible `Q` needs at least `r` strong queries in each of these three support windows. For `0≤τ<Δ0`, the earliest possible strong query in each is 214, 223, 294. For `Δ0≤τ<Δ1`, the first two remain 214,223 while the earliest late-window query becomes 295, because `|N_16(294)-N_32(294)|=Δ0`. For `Δ1≤τ<Δ2`, the earliest late-window query becomes 296, since `|N_16(295)-N_32(295)|=Δ1`. The early/middle threshold comparisons at the two left boundaries are directly checked against the frozen integers. The resulting weighted lower bounds are respectively `731r`, `732r` and `733r`.

**(C) Achievability and uniqueness.** Exhaustive checks of all `256 choose 2 = 32640` unordered state pairs yield

`min_{a≠b} max_{k∈(214,223,294)} |N_a(k)-N_b(k)| = Δ0` (64 saturating pairs);

`min_{a≠b} max_{k∈(214,223,295)} |N_a(k)-N_b(k)| = Δ1` (64 saturating pairs);

`min_{a≠b} max_{k∈(214,223,296)} |N_a(k)-N_b(k)| = Δ2` (16 saturating pairs).

Thus throughout the specified open-upper chambers each pair is strongly distinguished at **at least one** member of the displayed triple. Repeating each member `r` times meets criterion (A). Equality in the lower bound requires exactly `r` samples from each witness window and selecting its unique cheapest **strong** budget, proving uniqueness.

This symbolic `r` argument covers every `e,f≥0`; finite checking establishes the claimed 256-state/101-budget integer inequalities. No floating-point inference is used.

## Exact verification and provenance

Saved: `VERIFY_R5_FIXED_NOISE_EF_FIRST_THREE_CHAMBERS.py` (Python 3 standard library), `RESULTS_EXACT.json` and this `RESEARCH.md`.

The script reconstructs all **25,856** `N_b(k)` integers by eight successive subset-zeta stages on the frozen `A_T(k)` cohort source; verifies all three complete disagreement supports, each of the **97,920** pair–triple comparisons, the 3 threshold integers and their 64/64/16 saturating-pair counts, plus the exact earliest-strong-witness budget at each chamber's left endpoint. The executed command also supplied an independently derived complete budget/count table and checked all 25,856 numbers again. Output: `PASS_R5_FIXED_MIXED_FAULT_THREE_NOISE_CHAMBERS`.

Reproduce with:

```bash
python VERIFY_R5_FIXED_NOISE_EF_FIRST_THREE_CHAMBERS.py INPUT_COHORTS.json EXACT_R5_ALL_101_BUDGETS.json
```

The two inputs are the already preserved R5 reproduction bundle's `INPUT_COHORTS.json` (SHA-256 `a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d`) and independent complete table (SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`). The source cohort computation and original 954-event topology are pinned by `435e77af0d180eac32bd1f9c4c464bc4010b7551`. The existing R5 mixed-fault work at `research_notes/portable_direct/r5_mixed_fault_fixed_query_20261117/` proves the first chamber and preserves earlier code/claims; the present note extends it rather than replacing historical evidence.

## Further research

1. Determine the exact next fixed mixed-fault cost chamber beginning at `τ=Δ2`. The cheapest late witness is still 296 at this boundary, but the triple (214,223,296) has 16 limiting **other** pairs, so the disjoint-window bound by itself is no longer tight.
2. Test whether mixtures of different query budgets at `r>1` can improve over simply repeating the single-readout optimum in later noise chambers; this is a finite weighted multicover problem with structured witness constraints.
3. Retain the earlier `K=214..291` `max-new/min-old` optimizer-set recourse question and provenance-sensitive joint BRC observer work.

Formal R5 TASK CLAIM and protected Activity/Result association are separate from independent scientific preservation and review.
