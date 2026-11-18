# R267 — Six-class price cone and exact eight-plane two-price atlas

Date: 2026-11-18 (Asia/Shanghai). Research status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFICATE / NOT_REVIEWED**. Independent portable-research continuation; neither a native TASK CLAIM nor Result/Review.

## Source, premises and precise observer

Continue R266 at immutable commit `340e33e20c1841f046e6f4fee8a431afe2f144e8` (R266 exact weighted observer proof and `R266_weighted_cost_phase_certificate.py`). Preserve scientific input pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`: seven-source positive-rational auxiliary scalar model with `s=67/169`, `J=1184397599`, `T=989553240`, `K=3805974000`. The 63 normalized labelled integer observation sequences `q_{m,k}` are tested modulo 13 at event `k>=3`. All Boolean supports repeat with period 2184, certified by 249 shifted taps of monic integer recurrences. Exactly two phases have every labelled source zero; 39 labels are identically zero, and the other 24 labels form six Boolean-support equivalence classes with representatives in fixed order `(9,10,12,13,24,26)`.

The oracle charges positive price `c_i` per original-labelled Boolean nonzero test of class `i`; equivalent labels have equal price. Only the all-zero predicate is sought, and the phase is hidden. On a nonzero value the algorithm stops with answer false; a continuation only follows zero responses. Event phases are uniformly weighted in this result, and correctness covers all 2184 phases.

## Theorem A — Complete six-price positive cone by 156 coefficient vectors

For any class subset `S`, let `U_i` be its nonzero phase support and set `M(S)=2184-|union_{i in S}U_i|`. A terminating all-zero path is a truncated permutation `o=(i_1,...,i_r)` covering all positive phases. Define its six-dimensional nonnegative integer coefficient vector by

```text
v_i(o) = M({i_1,...,i_(j-1)})  if i=i_j is queried,
         0                     if i is not queried.
```

For every `c=(c_9,c_10,c_12,c_13,c_24,c_26)` with all entries strictly positive,

```text
             C(c) = min_o <v(o),c>
                  = min_{v in V_156} <v,c>.
```

The exact finite set `V_156` is obtained by enumerating all 720 permutations, truncating immediately after complete positive-phase coverage, removing equal vectors, and removing all vectors componentwise dominated by another. There are **570 distinct six-component coefficient vectors** and **156 Pareto-minimal vectors**. The full 156-vector list and representative original-label query paths are written deterministically to `R267_verification.json` by the accompanying standard-library script.

**Proof.** The only nonterminating answer path is the string of zero responses. Each probe on that path costs `c_i` exactly on `M(S)` surviving phases, hence the total across the period is `<v(o),c>`. Repeating a class profile adds positive cost without changing the classification. Every correct all-zero path must cover all 2182 nonzero phases; any such distinct-label path is a truncated permutation of the six classes. If `v'<=v` componentwise, then `<v',c><=<v,c>` for every positive price vector. Thus discarding dominated vectors preserves the exact optimum everywhere in the positive cone. This reduction is finite and exact; it does not assert that every Pareto vector has a nonempty open winning chamber.

## Theorem B — Eight affine pieces in the entire two-price quadrant

Specialize `c_9=x>=1`, `c_26=y>=1`, and `c_10=c_12=c_13=c_24=1`. The exact optimal 2184-phase total cost is

```text
C(x,y) = min {
    16 +  168x + 2184y,
    16 + 2184x +  156y,
   160 + 2184x +   52y,
   196 +           2184y,
   208 + 2184x +   26y,
  2212 +            312y,
  2500 +             52y,
  2548 +             26y
},                              x>=1, y>=1.
```

All **eight planes** are necessary: each has a strict rational witness `(x,y)` in the open quadrant at which it uniquely wins.

**Exact exhaustive certificate.** Project the 156 six-dimensional vectors onto `(a,b,c)` with `a=v_10+v_12+v_13+v_24`, `b=v_9`, `c=v_26`; there are **116 distinct candidate affine forms**. For *each* candidate `l(x,y)=a+bx+cy`, the second program produces at most four exact rational coefficients `lambda_j>=0`, summing to 1, on the eight displayed planes `l_j=a_j+b_j x+c_j y`, satisfying three componentwise inequalities:

```text
sum lambda_j*(a_j+b_j+c_j) <= a+b+c
sum lambda_j*b_j           <= b
sum lambda_j*c_j           <= c
```

Writing `x=1+X, y=1+Y` with `X,Y>=0`, these inequalities give `min_j l_j(x,y) <= sum_j lambda_j*l_j(x,y) <= l(x,y)` for the **entire unbounded quadrant**. The certificate generator uses only exact fractions, exhaustive supports of size at most four, and small Gaussian eliminations; it also outputs strict rational witnesses for the eight surviving planes. Thus the displayed formula is an exact global lower envelope, rather than a sampled-grid inference.

Examples (exact whole-period totals):
- `C(1,1)=2356`, an optimal path `9,26,10,13`.
- `C(1,2)=2444`, an optimal path `9,10,13,26`.
- `C(2,1)=2380`, an optimal path `26,12,10,13`.
- `C(2,2)=2600`, an optimal path `12,10,13,26`.

The six-price cone also has **no universally mandatory first queried class**: when the chosen class has unit price and the other five each cost `10^6`, each of the six representatives is optimal as the first probe in its corresponding witness case. This is verified by exact 64-state dynamic programming.

## Reproduction and verification boundary

Run in the same directory:

```bash
python R267_six_price_cost_atlas.py
python R267_atlas_exact_proof.py
```

The first script derives the 63 modular supports from the unchanged rational recurrence, certifies the 249 recurrence taps, constructs all 720 paths, 570 full vectors, 156 Pareto vectors and 116 two-price forms, and performs **144 exact rational two-price comparisons** among 64-state DP, all full path vectors and Pareto projection. It writes the full `R267_verification.json`.

The second script regenerates the **116 exact dual comparison certificates** and **eight strict rational witnesses** to `R267_atlas_certificate.json`, using the first file as input. Both scripts executed locally successfully on 2026-11-18 with outputs `PASS`. Original local full evidence SHA-256: `R267_verification.json=2a7ecdf8063df060befc11b811dd2f2b71e6e6dd4b4b97b4fd11a8f012f06ab4`; `R267_atlas_certificate.json=70d5421570d9e7e0fae6ea6d9c48830ae5746b1157c7e382eff9e211aef4bb0c`. Scripts on GitHub regenerate those files; accompanying short summary is stored as a separate research artifact.

**Claim boundary:** This is a Boolean-support observer for a labelled auxiliary positive-rational model. The six class quotient does not identify distinct numerical values, signed BRC ports, native three-dimensional slices, X6 dynamics or provenance. Native typed BRC correspondence and independent mathematical review remain open. P000/ACTIVE worldview/frozen scientific inputs are unchanged.

## Next independently executable unit

Establish a minimal **typed provenance-preserving carrier** `(label,port,branch-history,modular-value)` for these six Boolean support classes and prove exactly when a zero-only decision factors through it under one declared class of future operations. Compare its additional storage/read costs with the eight-plane cost formula before claiming an algorithmic speedup. A second numerical continuation is to extend the eight-plane atlas to joint phase-biased workload weights, retaining exact rational dual certificates.
