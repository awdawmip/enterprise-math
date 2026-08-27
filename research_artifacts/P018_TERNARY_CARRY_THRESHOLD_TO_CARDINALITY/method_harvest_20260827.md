# P018 method harvest — binary atlas replay

This replay discovered an independent historical proof asset on `research/p018-binary-root-atlas-lean@9fa0a84b4fff7f5140bc6cf96779a774c891ebcb` (Draft PR #246).

The harvested architecture is not a downstream theorem assumption. It is an earlier P018 formal proof route for the same binary quotient-root atlas:

1. define the physical positive quotient-root state Finset as the image of denominators `1..n`;
2. split it at the exact high cutoff `D`;
3. prove the high image has cardinality `D` by injectivity;
4. identify the low part as `1..H-1` plus the optional horizon root `H`;
5. use disjointness to derive `N+1=D+H+kappa`;
6. feed that identity into the independently existing `ternary_count_from_binary_carry` theorem.

The current execution ports only this architecture. All load-bearing arithmetic inequalities are taken from the stronger current #328 lineage (`RootStateAtlasCardinality.lean`, `RootStateCountCarryExact.lean`, `RootStateCountCarryUpper.lean`), not copied as assumptions from the historical branch.

Provenance classification: `INTERNAL_PRIOR_RESEARCH_METHOD_HARVEST / SAME_TASK_LINEAGE / NOT_CANONICAL_TRUTH`.
