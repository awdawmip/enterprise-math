# R130 — Sparse exact event log for the correlated S23 observer

Date: 2026-11-13 (Asia/Shanghai). Author-side auxiliary mathematics, not native X6 permission. Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Exact predecessor: R129, `ddef5881c7e9996fbc08c6f48cd0c387606d035d`, `research_notes/brc_s23_av_r129_oneparameter_event_sweep_20261113/PROOF.md`.

## Mathematical statement

Let `m>=1`, `x,l,h` rational with `l<h`, and `A,d,E` arbitrary integers. For `i=0,...,m-1`, define

`S_i(theta) = 1[{x+(A+i*d)theta} < {E theta}]`,

where `{z}=z-floor(z)` and the domain is the *open* rational interval `I=(l,h)`. R129's root set is

`C = Z_I(E theta) ∪ ⋃_i Z_I(x+(A+i*d)theta) ∪ ⋃_i Z_I(x+(A+i*d-E)theta)`,

with the convention `Z_I(b+s theta)=∅` when `s=0`, even if the affine function is identically integral. The isolated roots are all rational. Write `C={c_1<...<c_q}`. R129 proves that every S_i is constant on the open cells between the cuts and that the signatures at singleton cuts are also needed.

Set `r_v=|Z_I(E theta)|`, `r_u(i)=|Z_I(x+(A+i*d)theta)|`, `r_w(i)=|Z_I(x+(A+i*d-E)theta)|`. At each cut `c`, assign the *affected-coordinate set*

`J(c)={i : c is an isolated root of u_i, w_i, or v}`, with `v=E theta`, `u_i=x+(A+i*d)theta`, `w_i=u_i-v`. In particular, if `c` is an isolated root of `v`, every index `i` belongs to `J(c)`.

**R130.1 (lossless sparse transition certificate).** An initial `m`-bit signature on the first open cell plus, for each ordered cut `c`, two sparse coordinate-replacement lists `D_cut(c)`, `D_right(c)` relative to the immediately preceding open cell, is sufficient to reproduce exactly: (1) every singleton-cut signature; (2) every open-cell signature; and therefore (3) the full set of attained signatures on I. The lists can be constructed by evaluating only coordinates in `J(c)` at `c` and at any rational point in the immediately following open cell.

Here `D_cut(c)={(i,S_i(c)):i∈J(c), S_i(c) != S_i(left)}` and similarly `D_right(c)` uses the right open cell. The persistent working state is changed only by `D_right(c)`; the singleton-cut signature is the temporary application of `D_cut(c)` to the *left* state. Thus coincident roots, zero slopes, exact half-open boundaries, and isolated cut-only words are all retained.

**R130.2 (arithmetic operation bound).** Let `J_total=Σ_{c∈C}|J(c)|`. Then

`J_total <= Σ_i(r_u(i)+r_w(i)) + m*r_v`,

and the exact number of *single-bit S_i evaluations* in this construction is

`m + 2*J_total`,

rather than `m*(2q+1)` for re-evaluating the entire word at every cut and cell. The replacement log contains at most `2*J_total` changed-index entries, plus the initial `m` bits and cut positions. Generating and sorting roots uses `O(T log(T+1))` rational comparisons for `T=r_v+Σ_i(r_u(i)+r_w(i))`, with root construction and coefficient/bit costs accounted separately.

For a fixed interval length L and fixed integer `A,d,E`, the root count is `T=O(m^2)` from R129; `r_v=O(1)` and `J_total=O(m^2)`. The sparse log therefore uses `O(m^2)` indexed changes and `O(m^2 log(m+1))` rational comparisons (arithmetic-operation accounting). Index encoding introduces an additional `O(log m)` bits per changed-index entry, and exact rational arithmetic has input-dependent bit costs.

This is a **compressed ordered trace**. It does not claim an O(m²) cost for explicitly materializing or deduplicating every full m-bit word. The R129 sharp family has Θ(m²) distinct length-m words, so writing them all takes Ω(m³) bits. Reconstructing any individual full word costs its output size plus the changes required to reach it.

## Proof

Fix a cut `c` and a bit index `i∉J(c)`. By definition none of `v,u_i,w_i` crosses an integer at `c`; if one is identically integral, it introduces no isolated change. The fractional parts of `u_i` and `v` are continuous near c except at their own integer crossings, and their relative strict order changes only at a root of `w_i`. Consequently there is a neighborhood of c in which `S_i` takes exactly the same value on the left open cell, at c and on the right open cell. This proves that modifying only coordinates `J(c)` gives both cut and right signatures exactly. Induction over the ordered cuts proves R130.1, including simultaneous events. Each cut costs exactly `2|J(c)|` calls to the indicator, plus m calls for the first cell. A union bound on root incidences gives the bound on `J_total`. The open-interval affine integer root count from R129 is bounded by `ceil(|s|L)` for nonzero slope s. Summation yields the stated bounds. QED.

## Executed exact validation

Companion program `check_r130.py` uses only Python `fractions.Fraction`; every returned compressed singleton and open-cell word was compared against independent complete-word reevaluation. It covered 250 fixed-seed random signed/rational instances, 8 boundary/collision instances, 1 hundred-decimal-digit coefficient instance over a short parameter interval, and the exact Farey family for m=16,32,64: **262 cases, 133310 exact positions checked**. Result: `R130_SPARSE_SWEEP_PASS`. For the 258 ordinary cases, 130048 positions, 987167 naive indicator evaluations versus 177825 sparse indicator evaluations. At m=64 on the sharp family, 2455 exact positions needed 157120 naive versus 7752 sparse indicator evaluations. These are counts of indicator evaluations, not wall-clock speedups. The 100-digit coefficient instance had 49 exact positions and 69 sparse vs 245 naive indicator evaluations. Full counts are in `verification_r130.json`.

Finite tests validate the implementation within their stated coverage; the mathematical assertion is the argument above. The log is faithful to the signed S23 auxiliary observer only; native Cell/Link/Port admissibility needs its own transfer map and proof.

## Current unresolved follow-up

Construct random-access indexed persistent word representations and compare exact bit costs, memory and execution time with R129's dense sweep and R127/R126 fixed-dimensional integer feasibility for growing coefficient bit lengths. Determine whether period quotienting further reduces sparse-log size, without dropping singleton-only signatures.
