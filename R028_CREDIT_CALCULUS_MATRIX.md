# R028 Credit Calculus Matrix

Researcher-ID: `EM-R028-4D91AF`  
Status: `NOT_CANONICAL`

| Credit coordinate | Exact definition | Positive law | Negative boundary | Runtime use |
|---|---|---|---|---|
| Pair coverage | newly covered pairs in `P(E,F)` | monotone, submodular; full cover iff exact completion | not equal/rank-equivalent to `M/B` | safe acquisition progress / verifier |
| Alphabet debt | `ΔM` | nonnegative, ordered telescope | order-dependent; neither sub- nor supermodular | side-label alphabet pressure |
| Bit debt | `ΔB` | nonnegative, ordered telescope | ceiling plateaus; order-dependent; neither sub- nor supermodular | fixed-width metadata pressure |
| Local multiplicity | per-current-fibre reductions | nonnegative under refinement | global `ΔM` can be zero while local credit positive | bottleneck diagnosis |
| Rewind | `R_before-R_after` after adding metadata/checkpoint access | nonnegative | not ordered the same as `B`; can be redundant/order-dependent | checkpoint selection |
| Cost | acquisition/storage/recompute/reread | explicit accounting | no free oracle; no canonical conversion to semantic credit | Pareto selector |
| Shapley comparator | classical Shapley of declared game `v(S)` | symmetric/order-averaged | same value can describe synergy and redundancy; not causal | diagnostic comparator only |

## Frozen interpretation

Use the profile

`(pair coverage, local multiplicity vector, ΔM, ΔB, Δrewind, acquisition cost, storage cost, recompute cost)`.

Do not scalarize without declared weights/convention.

## Strong claims killed

- order-independent intrinsic marginal debt credit;
- universal submodularity of debt gain;
- universal supermodularity of debt gain;
- pair coverage = precision-debt credit;
- realized suffix zero credit => ex-ante safe deletion;
- individual `M/B` feature credit always falls as future language shrinks.

## Positive conditional law

Nested/chain feature kernels imply submodular `M/B` gain, because the selected refinement is the finest selected kernel and total gain is a max-on-chain function.
