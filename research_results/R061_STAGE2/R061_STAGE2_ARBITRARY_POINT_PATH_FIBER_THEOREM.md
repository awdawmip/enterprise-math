# R061 Stage 2 — Arbitrary-Point Native Path Fiber Theorem

Task-ID: `RS-R061-STAGE2-ARBITRARY-POINT-NATIVE-LINE-TRANSLATION-CROSS-SECTOR-GLUING`  
Taskbook source: `8b197776249e0b18850cee8375488de9aa57cbb4`  
Researcher-ID: `EM-R061S2-3CE600`

## Status

`ARBITRARY_POINT_PATH_FIBER_EXACT = true`  
`PATH_FIBER_CARDINALITY_TRANSLATION_INVARIANT = true`

## 1. Realization formula

For an open translated sector trace

`T_{P;a,b}^{(ij)}`,

define

`Realize_E(T_{P;a,b}^{(ij)}) = { Sigma_P^(ij) ; w : w in Sh_{a,b}(X_i,X_j) }`.

This is exactly the frozen Stage 1 realization translated by `tau_P`.

## 2. Prefix state theorem

For a word `w`, after a prefix containing `u` copies of `X_i` and `v` copies of `X_j`, the instantaneous state is exactly one circle cell

`C_P^(ij)(u,v)`.

Because `u,v>=0` for every prefix, every prefix cell lies in the translated sector affine chart. No multi-cell instantaneous state is introduced.

Each letter changes the cell center by one frozen nearest-neighbor center vector, so every center transition joins overlapping nearest-neighbor circle cells.

## 3. Terminal typing

Every word in `Sh_{a,b}` terminates at

`C_P^(ij)(a,b)`.

The coordinate endpoint is

`Q = V_P^(ij)(a,b)`.

The constant translated affine offset gives

`ctr(C_P^(ij)(a,b)) - Q = s_ij`,

so the terminal cell is incident to `Q` exactly as at the origin.

The vertex owns native component length; the terminal cell owns the discrete terminal state.

## 4. Trace identity and cardinality

All representatives contain exactly `a` labels `X_i` and `b` labels `X_j`, with no third-family label. Hence they share one translated native component trace.

Different shuffle words remain different cell trajectories. Translation creates no new collision or deduplication.

Therefore

`|Realize_E(T_{P;a,b}^{(ij)})| = binom(a+b,a)`.

Graph jump count remains `a+b` for each such representative and is not the native line length.

## 5. Axis and zero fibers

For a global translated axis identity, the two adjacent sector-local singleton fibers are retained after identity gluing. They begin at different sector anchor cells and are distinct physical trajectories.

For the zero trace `T_P^0`, the three incidence-only sector branches are retained as separate chart realizations.

## 6. Deterministic replay

The checker explicitly replayed every translated trace pair with `a+b<=12` over seven nontrivial start vertices in all three sectors:

- translated trace cases: `1,911`;
- explicit path representatives: `172,011`;
- center transitions checked: `1,892,394`;
- paths per sector: `57,337`;
- endpoint errors: `0`;
- non-neighbor transition errors: `0`;
- translated affine-chart prefix errors: `0`;
- within-trace trajectory collisions: `0`;
- binomial count mismatches: `0`.

Thus the Stage 1 path fiber translates exactly to arbitrary integer-addressed starts.
