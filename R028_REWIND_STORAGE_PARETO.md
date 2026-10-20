# R028 Rewind / Storage / Recompute Pareto

Researcher-ID: `EM-R028-4D91AF`  
Status: `NOT_CANONICAL`

## Exact sufficiency

Checkpoint `E_t` can recover target `F` without extra metadata iff

`E_t subseteq F`.

With metadata `Z_t`, replace this by

`E_t intersection ker(Z_t) subseteq F`.

Latest sufficient checkpoint `t*` minimizes no-extra-metadata rewind; current rewind is `T-t*`.

## R022 8-state replay

Target: four-pair partition `E1`.

- `E1`: 0 side bits, rewind 2;
- `E2` (two quartets): 1 side bit, rewind 1;
- `E3` (universal): 2 side bits, rewind 0.

`E0` (identity): 0 bits, rewind 3 and is dominated by `E1`.

## Why no scalar

Same `B` can require different rewind; same rewind can have different `B`. Add checkpoint bytes, acquisition reads and recomputation work and the tradeoff becomes genuinely multidimensional.

Recommended runtime decision:

1. enumerate semantically sufficient options;
2. attach actual storage/read/recompute/reread costs;
3. remove Pareto-dominated options;
4. choose only after an objective/weighting is declared.

No-resurrection means an option that cannot refine the retained encoding enough is infeasible regardless of how many downstream branches it creates.
