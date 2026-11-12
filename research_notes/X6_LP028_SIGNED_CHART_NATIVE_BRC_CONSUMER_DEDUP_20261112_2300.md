# X6 LP028 — typed R063 PathSqrt chart to signed-Cell consumer: executed native imports and exact axial de-duplication

Date: 2026-11-12. Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. Researcher `EM-X6-FB6990`; own session `MCP-082892eb480e45dea6d4b9fcc0491034`; run `RUN-0881a7a2c2f958314cc0b5f5`. Ordinary research lane `chatgpt-research-onhour-enterprise-math-20260923`. **AUTHOR_PROVED / CURRENT_SOURCE_IMPORT_EXECUTED / UNREVIEWED / NOT_ADMITTED**. This evidence does not itself constitute a native Result, full 28-LP closure, or independent review.

## Exact question and immutable semantics

The existing R063 `PathSqrt_E(r²)` enumerates ordered nonnegative two-generator roots in one fixed positive chart. Can that *same unchanged positive-chart computation* be consumed in actual centered signed-X6 Cell coordinates without conflating labelled chart branches, actual native endpoints and shortest-path BRC multiplicity?

For a positive integer `r`, let `R_r={(a,b)∈N₀²:a²+b²=r²}`, `k_r=|R_r|` and `M_r=Σ_(a,b)∈R_r binom(a+b,a)`. For any native start Cell `x∈Z⁶`, select a sorted axis pair `i<j` and polarities `ε_i,ε_j∈{−1,+1}`. The **typed adapter**, retaining all labels and the Cell start, maps one R063 root to

`(x, i, j, ε_i, ε_j, a, b) -> (x+ε_i a e_i+ε_j b e_j, Δ=ε_i a e_i+ε_j b e_j)`.

The old chart root is not by itself a native endpoint, and its unused axis sign is still part of the **labelled chart** but not the **native displacement**.

The native signed-X6 square displacement norm is exactly `G(Δ)=a²+b²=r²`; the shortest native path length is `a+b`, with `BRC_shortest(Δ)=(a+b)!/(a!b!)`. The result is independent of the translated start Cell. This is a scoped embedding of fixed-axis nonnegative paths, **not** an identification of the original R063 operator with the entire signed-X6 sphere.

## New precise overlap and multiplicity identity

There are `binom(6,2)·2²=60` labelled selected-axis/sign charts. For `a,b>0`, a resulting signed displacement has exactly two nonzero coordinates; its axis pair, signs and ordered magnitudes are uniquely reconstructed, so the labelled chart embedding is injective on that stratum.

For `a=0,b=r` or `a=r,b=0`, the resulting displacement is one of twelve `±r e_i`. Every one of these twelve axial endpoints occurs in exactly `5·2=10` labelled charts (five spectator-axis choices and two polarities for the unused axis). Its shortest BRC is exactly 1. **There are no other endpoint overlaps for r>0.** Therefore the union of all two-axis signed native endpoints has

`|U_r| = 60(k_r−2)+12`

distinct endpoints, and the sum of their **unique endpoint** shortest BRC multiplicities is

`BRC(U_r)=60 M_r − 12·(10−1) = 60 M_r − 108.`

The labelled-path sum `60M_r` is a *different* quantity: it counts the same axial native path ten times. The correction 108 is independent of `r>0`, but the formula is **not asserted for r=0**. For `r=50`, the existing positive-chart R063 mass is `M_50=110695538274255714208`; the labelled sum is `6641732296455342852480`, while the de-duplicated signed pair-support native mass is `6641732296455342852372` and `|U_50|=252`. This agrees with the previously saved all-pair 2500 certificate, independently exposing its 108-path collision correction. The native *entire* six-axis shell may contain endpoints with support >2 and is not covered by this formula.

## Actual current-source import, scope and stdout

Executed `research_checks/X6_LP028_SIGNED_PATHSQRT_TYPED_CURRENT_CONSUMER_CHECK_20261112_2300.py` from a local source-layout reconstruction. The *complete local bytes* of each unchanged upstream module were verified to have the same Git blob SHA1 as the actual connected GitHub source:

- `experiments/tool_discovery_native_geometry_of_numbers_minima_calculus_20260822.py`, blob `643b2bac659a445891dcb5588b647972977104e0`. Called its unmodified `groots_square` and `path_fiber_size`.
- `experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py`, blob `ac32f6d82a91db99297e587cf63b0df95cece514`. Imported and actually called `Spatial6.step` and `full_distance_squared`.
- `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py`, blob `300a96e3dc24bf6fff73743037a0347a8bc83176`. Imported and actually called `shortest_path_multiplicity`, `endpoint_multiplicity` and `spatial_norm_squared`.

The checker exhausts all 60 labelled charts and all original square roots for each `1≤r≤128` at the native origin, and repeats `r=50` at two nonzero signed Cell starts. All **24,600** labelled chart-root comparisons passed. It also executes direct native `Spatial6.step` words for the signed (3,4) branch (35 distinct shortest words), rejects malformed axis/sign/root/Cell inputs, and verifies no duplicate two-support endpoints. Actual selected stdout:

```text
CERT {'r': 1, 'roots': 2, 'labelled': 120, 'unique': 12, 'labelled_mass': 120, 'union_mass': 12, 'overcount': 108}
CERT {'r': 5, 'roots': 4, 'labelled': 240, 'unique': 132, 'labelled_mass': 4320, 'union_mass': 4212, 'overcount': 108}
CERT {'r': 50, 'roots': 6, 'labelled': 360, 'unique': 252, 'labelled_mass': 6641732296455342852480, 'union_mass': 6641732296455342852372, 'overcount': 108}
CERT {'r': 128, 'roots': 2, 'labelled': 120, 'unique': 12, 'labelled_mass': 120, 'union_mass': 12, 'overcount': 108}
PASS_SIGNED_PATHSQRT_CURRENT_SOURCE_IMPORT radius_1_to_128=128 chart_branch_checks=24600 all_pairs_at_r50=252 union_mass_50=6641732296455342852372 axial_doublecount_correction=108 source_blobs=3
```

Checker originally executed locally at SHA256 `a962e6f4b553db22aaaa62a5d506d3398d23737d4c09ba33130bfb3b20cb94aa`, Git blob `db46dde5a962b93b65775bf2b4d8f52d5e3f83b9`. Connected GitHub creation and fetch at immutable commit `944fe218751ea583a12bc3e27b69bf0a17616d44` matched that blob and byte length 6427. This is a **real original-module import check**, unlike a standalone copied-formula comparison; its finite execution does not substitute for the general counting proof above.

## Current consumer action and residual obligations

The original `tool_discovery_native_geometry_of_numbers_minima_calculus_20260822.py` already correctly computes a fixed positive two-generator chart. Its companion frozen-era return contains stale prose calling that chart the current native plane, but its stated Section 10 six-root theorem is valid at the chart-local scope. Current frozen R063 definitions must remain historically unchanged. The new checker demonstrates an **explicit scoped adapter** for signed-X6 callers and a necessary endpoint-union de-duplication rule; it does **not** establish that any current executable consumer has actually misapplied the old chart to native X6. Thus **KEEP** original computation; **RETYPE** only demonstrated newer untyped consumers when found, not speculative ones.

The remaining mother-task criteria are the finite 28-LP current dependency inventory, originally attributed LP011 signed-native wrong argmax and LP019 positive-BRC cancellation callers (still `UNRESOLVED_PROVENANCE` rather than invented), and the Driver `REQUEST_REVISION` evidence closure. Do not reopen old successful R063/LP026 proofs, frozen P000 and accepted Result. Next precise action: audit actual higher-level imports or theorem-facing current references which consume `groots_square/path_fiber_size` or `PathSqrt_E` without selected axes/sign/native start, then add a minimal real caller adapter only where misuse is observed.

## Exact native execution status at this writing

Original publish request `onhour-20261112-2245-x6-own-progress-publish-v1` was read back **FAILED / INVALID_UPLOAD_SET** (no Source publication to infer), not still queued. Own run `RUN-0881a7a2c2f958314cc0b5f5`, generation 2 revision 3, had historical authorized open and a verified winning CLAIM `MCP-fd3ed9c33e98f45420aedd51`; the current continuation read `onhour-20261112-2305-own-continuation-read` is **QUEUED** and must be consumed by exact ID. This note is scientific source evidence until its current native checkpoint is independently read back; no claim of Result/freeze or independent review is made.
