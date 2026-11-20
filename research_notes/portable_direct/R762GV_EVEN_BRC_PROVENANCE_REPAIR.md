# R762GV — Exact worst-case provenance repair for even signed STAR BRC words

Date: 2026-11-20 (Asia/Shanghai). Author-side mathematical research, **NOT_REVIEWED**.
Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, publication `TP2-8B7E13C5904A2D6F1142`; frozen taskbook `857280d1012943290d141d1317179c40ec3cbdf8` and P000 `a72226e2430ffa4786321ac86e7f0c599d5f0389`.
Predecessor: R762GU in Draft PR #2845, scientific commit `1bf0bbf396e41bea55d979a63d4b034e2b87e845`.
Historical contributor lineage: `EM-X6-3050F6`; this manuscript neither exercises a live task CLAIM nor impersonates a past run. All results below concern the precisely defined **free candidate language**, not native `TRIADIC_CLOSURE_E` admission.

## Carrier, observers and question

Four STAR labels `v=0,1,2,3` and each sign `s∈{+1,-1}` give eight **named** candidate composite letters `T(v,s)`. Each letter contributes the signed 4-inventory unit `s e_v`, with six-axis readout `s H_v` for K4 edge incidence `E=(01,02,03,12,13,23)`. Fix length `m` and let `W_m` be the 8^m ordered source words. The positive-integer BRC carrier counts words without identifying sign or source order.

For `w∈W_m`, `z(w)=sum s e_v∈Z^4` and `Y(w)=Bz(w)∈Z^6`. The source observer exposes only `(m,Y)`. R762GU proves that `B` is injective on integer `z` and that for readout `Y=(a,b,c,d,e,f)`, `z=((a+b-d)/2,(a+d-b)/2,(b+d-a)/2,c-(a+b-d)/2)` if and only if `e=c+d-b`, `f=c+d-a`, `a+b+d` is even. Define `N_m(z)=|{w∈W_m:z(w)=z}|`.

Question: how many **additional fixed-width binary bits** are necessary and sufficient to recover every named ordered source word from `(m,Y)` at an even length, assuming the future observer is allowed to inspect the entire source word?

## Theorem 1 — Sharp even-step central fibre maximum

For every `j≥0` and `z∈Z^4`,

`N_(2j)(z) ≤ N_(2j)(0)`.

For `j≥1`, equality holds only at `z=0`. For `j=0`, `N_0(0)=1` and all other counts vanish.

**Proof.** Let `a(x)=N_j(x)`, a nonnegative finitely supported integer function. Letter sign reversal gives `a(x)=a(-x)`. Concatenating two ordered words yields the exact positive BRC convolution
`N_(2j)(z)=sum_x a(x)a(z-x)=sum_x a(x)a(x-z)`.
Apply the finite-sum Cauchy–Schwarz inequality:
`N_(2j)(z) ≤ (sum_x a(x)^2)^(1/2)(sum_x a(x-z)^2)^(1/2) = sum_x a(x)^2 = N_(2j)(0)`.
Equality for `z≠0` would force the finitely supported nonzero function `a` to equal a nonzero translate of itself. Iterating that translation contradicts finite support. Hence the inequality is strict off zero. No probabilistic approximation is used.

## Theorem 2 — Exact minimum provenance repair and constructive rank/unrank

At each even length `m=2j`, the smallest possible *single fixed-width* repair field that makes `(m,Y,repair)` losslessly identify every ordered source word is

`b_(2j)=ceil(log_2 N_(2j)(0))` bits (with `b_0=0`).

**Necessity:** At `Y=0`, Theorem 1 gives the largest fibre, containing exactly `N_(2j)(0)` distinct source words. A fixed `b`-bit repair field distinguishes at most `2^b`; hence `2^b≥N_(2j)(0)`.

**Sufficiency:** Order the eight letters lexicographically `(0,+),(0,-),(1,+),(1,-),(2,+),(2,-),(3,+),(3,-)`. For fixed `m,Y`, uniquely recover `z` by the R762GU image-lattice formulas. Order all words in that fibre lexicographically, and transmit the zero-based *rank* as a `b_(2j)`-bit integer. To decode, for a candidate next symbol `T(v,s)` at prefix inventory `p`, the exact number of completions is `N_(ell-1)(z-p-s e_v)`, where `ell` is remaining length before the choice. Iteratively subtract preceding blocks and select the block containing the rank. This terminates in the unique original word. The positive BRC dynamic program is

`N_0(0)=1; N_0(z≠0)=0; N_(r+1)(z)=sum_(v=0..3)(N_r(z-e_v)+N_r(z+e_v))`.

This provides an actual finite, integer-only encoder and decoder; neither hidden source history nor a physical time increment is required during decoding. An individual readout's repair width may be reduced to `ceil(log_2 N_m(z))`; the theorem is the **global worst-case** fixed-width requirement.

## Theorem 3 — No bounded source-history repair over unbounded even horizons

R762GU gives the exact number of observable endpoint keys at length `m`:

`R_m=((m+1)^2(m^2+2m+3))/3`.

Since `sum_z N_m(z)=8^m`, Theorem 1 implies `N_(2j)(0)≥8^(2j)/R_(2j)`, while trivially `N_(2j)(0)≤8^(2j)`. Thus

`ceil(6j-log_2 R_(2j))≤b_(2j)≤6j`.

In particular `b_(2j)/(2j)→3` bits per event. Any constant-size repair field appended to `(m,Y)` eventually fails to reconstruct **all** ordered source words for arbitrarily large even lengths. This is an exact source-fidelity bound for the stated observer and language, not a native no-go on safe information loss when future operations depend on `Y` alone.

## Exact BRC data and validation

| m | all ordered words | readouts R_m | central fibre N_m(0) | sharp repair bits |
|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 0 |
| 2 | 64 | 33 | 8 | 3 |
| 4 | 4096 | 225 | 168 | 8 |
| 6 | 262144 | 833 | 5120 | 13 |
| 8 | 16777216 | 2241 | 190120 | 18 |
| 10 | 1073741824 | 4961 | 7939008 | 23 |
| 12 | 68719476736 | 9633 | 357713664 | 29 |
| 14 | 4398046511104 | 17025 | 16993726464 | 34 |
| 16 | 281474976710656 | 28033 | 839358285480 | 40 |

Reproducible script `R762GV_VERIFY.js` uses a typed alphabet with eight signed, named branches and BigInt positive BRC counts; its output is exactly `R762GV_EVIDENCE.json`. It verifies normalization, exact quartic support and unique central maximum at each even length 0..16; independently recomputes central coefficients for j=0..8 using the R762GU multinomial sum; and exhaustively rank/unrank-roundtrips every one of 4,681 source words of lengths 0..4. The general results rely on the proofs above, not extrapolation from finite tests.

## Native transfer and remaining question

The source alphabet is a **composite** signed STAR readout in a six-axis X6 Cell chart, not an asserted primitive off-axis step or fully licensed `TRIADIC_CLOSURE_E` force event. `m` is the ordering length, not the P000 independent time coordinate or a heartbeat duration. Sign denotes event-branch identity; nonnegative BRC word counts are not signed force amplitudes. No Euclidean vector-sum-zero axiom, pi expansion or classical propagation step is used.

This theorem quantifies the provenance residual necessary **if** an admissible future operation can distinguish arbitrary ordered source words. A gate reading only `(m,Y)` may permit lossless observer compression with no repair. To transfer the bound to native dynamics, specify Cell, Link, Port, triad-closure gate and separately typed event/time transitions, then prove which pair of same-`Y` source words are separated by an allowed native future context. In particular, test a zero-inventory signed pair of length two under one concrete legal Port update; this directly discriminates candidate memory from actual native residual.

Scientific status: **AUTHOR_PROVED; EXACT_INTEGER_BRC_CROSSCHECK_PASS; NOT_REVIEWED**. No formal Result/Review/CLAIM is asserted. Prior R762GU assertions remain at their original scope and evidence status.
