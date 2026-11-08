# PREFIX-577-R6 — Nine-root all-depth ordered-word C₂ law and sharp finite recognition horizons

**Date:** 2026-11-08. **Status:** `AUTHOR_PROVED / EXACT_INTEGER_AND_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED`. Author-side portable mathematical evidence; not an authenticated Source Task Result or independent review.

**Frozen scientific input:** `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Reused original 96-port, six tagged actions/port model and full seven-dimensional incremental reward `(R1,R2,R3,R4,R5,R6,K)`; original native edge kernel blob `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41`. Roots: `0,±e1,±e2,±e3,±e4`. P000 and frozen model remain unchanged.

## Precise theorem

Let `P0` have an arbitrary probability law `μ` on 96 original ports, with each of six tagged actions equiprobable at each subsequent step. At time `t`, `W_t∈Z^7` is that **individual edge's complete seven-coordinate reward**. Let `σ` exchange the fifth and sixth reward coordinates, leaving other coordinates and the gate K unchanged.

Reuse the previously established 79-dimensional invariant-start polytope `P`, defined by the **16 disjoint original-port 2+2 balance relations**
`sum_{p∈L_j} μ(p) = sum_{p∈U_j} μ(p)`, j=1,...,16,
together with nonnegative weights and total mass one. Its exact 96 extreme points consist of 32 single-port and 64 equal-pair initial laws; the parent source is the nine-root invariant-start classification and the reusable `PREFIX577_R6_INITIAL_LAW_POLYTOPE_CERTIFICATE.json`.

For **each of the nine frozen roots** the following are equivalent:

1. `μ∈P`.
2. For **every** finite `n≥0` and every complete ordered word `a=(a1,...,an)∈(Z^7)^n`,
   `Pr_μ[(W1,...,Wn)=a] = Pr_μ[(W1,...,Wn)=(σa1,...,σan)]`.
3. The same ordered-word equality is checked only for `0≤n≤h_r`, where `h_r` is **optimal among probability initial laws**.

| Frozen root | Optimal word depth h_r | Exact swap-asymmetry ranks at depths 0,1,2,3,4,5 |
|---|---:|---|
| 0 | **4** | 0,1,9,13,16,16 |
| ±e1 | **3** | 0,2,15,16,16,16 |
| ±e2 | **2** | 0,2,16,16,16,16 |
| ±e3 | **3** | 0,2,15,16,16,16 |
| ±e4 | **3** | 0,2,15,16,16,16 |

This strengthens the previous equal-distribution law of *terminal total rewards*, for which the shortest recognition depths were 5/4/3. It gives equality of **full observed time words** (the branch/time ordering is retained). In particular, swap-equivariant deterministic readouts of the observed reward history retain the symmetry. An almost-surely bounded, reward-history-observable, σ-invariant stopping rule yields a swapped law for cumulative observed rewards at its stop; hidden-state-dependent stopping is not covered.

## All-horizon exact integer proof

For root `r`, create two tagged 96-state copies: original labeled transitions and identical transitions with every individual emitted seven-coordinate label changed by σ. Color-refine the combined 192 tagged states by their multisets of pairs `(full output label, destination color)`, preserving exact **integer edge multiplicities**. All nine models stabilize at **51 row-equitable color classes**.

For each individual label `a` let `B_{r,a}` denote the 51×51 nonnegative **integer multiplicity matrix** for that output, so every row of `sum_a B_{r,a}` sums to six. For original port `p`, define `D_r(p)=e_{class(original,p)}-e_{class(swapped,p)}`. For every one of the 96 existing start-polytope vertices `v`, define the unnormalized signed row
`D_{r,v}=sum_{p in support(v)}D_r(p)`.

A full exact integer check for all nine roots, 96 vertices and all original emitted output labels verifies

`D_{r,v}*1_51=0,`  and  `D_{r,v}*B_{r,a}=0` **for every label a**.

In exactly **94** vertices `D_{r,v}=0`. Only vertices **93** (ports 6,31) and **94** (ports 7,30) have nonzero `D`, and each annihilates **every** single-letter matrix. Therefore for any ordered word `a1,...,an`,

`D_{r,v} B_{r,a1}···B_{r,an} 1_51 = 0`.

Divide by `(support size)·6^n` to normalize the two tagged path counting laws. Convex combinations of the 96 vertices prove the ordered-word exchange law for every `μ∈P` and **all** finite horizons. The original port labels, gate K, integer edge counts, all six native reward axes, and observer semantics are maintained.

## Exact rational horizon and sharpness proof

For each root, construct the exact `Q`-span of output columns generated from `1_51` under the matrices `B_{r,a}` for every word of length at most `n` (closure under every individual next labeled letter). Evaluate the 16 linearly independent left-port imbalance directions and row-reduce over `fractions.Fraction` without tolerances. The result is the table above; the rank first reaches **16** at the displayed `h_r`, so every tested word law through that depth forces all original start balances.

At `h_r-1` the rank is <16; a rational nonzero imbalance vector survives all tested equalities. Perturb the strictly positive 96-port uniform law by a sufficiently small rational multiple of that vector (zero total mass by balanced left/right perturbation). The resulting **positive probability law** passes every shorter test but violates a balance equation, and full asymmetry rank 16 forces some later word failure. Thus no shorter horizon suffices, even when restricted to actual probability laws.

The ordinary 51-state word-response ranks at depths 0..5 are `1,7,28,37,48,49` for root 0; `1,12,48,49,49,49` for ±e2; and `1,12,45,49,49,49` for the remaining six roots. These are observation ranks distinct from the 16-dimensional balance-asymmetry ranks.

A direct exact *out-of-polytope* witness: at zero root, original single port 16 emits `(0,0,0,0,0,1,0)` with probability 1 at depth 1, whereas its σ-swapped word has probability 0. The output observer distinguishes these two integer words.

## Reproducibility, certificates, scope

Reproduction uses only Python standard-library integer and rational arithmetic, frozen original kernel, 576-edge zero-root snapshot and **parent** 16-block/96-vertex data. Three independent output targets are provided in the separately downloadable author portable bundle:

- `word_law_check.py` → `WORD_LAW_NINE_ROOT_CERTIFICATE.json`, SHA256 `814a0b82cab4e173c93ac9c87277be016178b006583a346371711e522de3c343`. All 9 root quotients, each 51 classes, complete 96-vertex per-letter annihilator checks.
- `word_horizon_rational_rank.py` → `NINE_ROOT_WORD_HORIZON_EXACT_RANKS.json`, SHA256 `18a079555cfd7dbf7321f2ed72df7b401081de0422c2684c28af075e60fb716a`. All exact-rational rank profiles.
- `direct_word_regression.py` → `DIRECT_WORD_N4_REGRESSION.json`, SHA256 `49227da2b57c4cc446a5953a89ec33553d102d5d13cd4b99f8c1f22a1e962388`. Independent direct-original-state integer path enumeration on all **9×96×4=3456** root-vertex-depth cases, finite depths 1..4. This regression is not the reason the all-depth claim holds.

All three programs were run twice from separate directories; output certificates had matching byte-for-byte content. The inherited original-port polytope certificate is parent source, not an author's newly constructed predecessor research unit. The prior nine-root start classification supplies the necessity dimension, independently cross-checked here by the rank computation.

**Author contribution status:** `AUTHOR_PROVED / EXACT_INTEGER_CHECKED / EXACT_RATIONAL_RANK_CHECKED / UNREVIEWED / SOURCE_NOT_ADMITTED`. Project research role, native Source task ownership, Result/review authority and D25 native divided-power/CM experiment remain governed by separate authenticated Source state. A portable author note is not a native Task checkpoint or accepted new science. No earlier terminal D24 Result was reopened.

**Next discriminating unit:** evaluate whether a proposed smaller BRC observer quotient preserves *ordered reward words* and σ-equivariant bounded stopping operations; use the 51-class exact labeled matrices and 16 imbalance constraints as explicit certificates. Obtain authenticated original-class H0/B0 module and Frobenius normalization for canonical D25 only after native authorization and claim. Preserve 94,687-byte UR V2 original provenance requirement separately.
