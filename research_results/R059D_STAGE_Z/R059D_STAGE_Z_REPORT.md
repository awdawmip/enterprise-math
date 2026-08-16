# R059D Stage Z — Transverse Frontier / Gap-Count Coupling Report

Researcher-ID: `EM-R059D-4E8B71`  
Task-ID: `RS-R059D-STAGE-Z-TRANSVERSE-FRONTIER-GAP-COUNT-COUPLING`  
Taskbook source: `d5cf81641f36bfb57f86897ff2410a0b4e869d26`  
Owner branch: `research/r059d-stage-z-transverse-frontier-gap-count`  
Frozen parent: `bcbcb997104a1042408276b3ab9eb0aa01e30f91`  
Pre-score registry: `22d015b3c6f9f6e028c4cbebfd4ff176f8be91e3`

## Result

Stage Z establishes the abstract transverse frontier arithmetic but does **not** establish a primary-gap coupling.

For `B2(k)={1,...,k}^2`, the frontier `F2(k)=B2(k+1)\B2(k)` has the exact disjoint decomposition into the new row `{(k+1,j):1<=j<=k+1}` and the new column excluding the corner `{(i,k+1):1<=i<=k}`. Hence `|F2(k)|=(k+1)+k=2k+1`.

Under transverse slot swap there is exactly one fixed state `(k+1,k+1)` and `k` two-element off-diagonal orbits, so the quotient frontier has `k+1` orbits.

## Primary-gap freedom theorem

Let `A_k` be the first primary index with `a_n=k`. When `A_(k+1)` is finite, the complete k-layer occupancy interval is `I_k={n:A_k<=n<A_(k+1)}` with length `g_k=A_(k+1)-A_k`.

The frozen Stage-X theorem is stronger than any proposed frontier law: every binary staircase extends globally. Therefore for every sequence of positive integers `(g_k)_(k>=1)` there is an allowed global atlas whose activation gaps have exactly those lengths. Construct `A_1=1`, `A_(k+1)=A_k+g_k`, and keep `a_n=k` on `A_k<=n<A_(k+1)`.

Thus each `g_k` is free over the positive integers, with a terminal infinite plateau also allowed. In particular current frozen semantics do not force `g_k=2k+1`. A minimal witness is `k=1`: the allowed staircase prefix `0,1,2,...` has gap length `1`, while `|F2(1)|=3`.

## Reflection obstruction

The transverse reflection fixes every primary +u ray event but swaps the two frontier slots. If a pointwise map `f:D->F2(k)` is reflection-equivariant, then for every fixed primary event `d`, `f(d)=f(sigma d)=sigma f(d)`, so `f(d)` must be the unique fixed frontier state `(k+1,k+1)`. Therefore for every `k>=1` there is no reflection-equivariant pointwise surjection or bijection from primary gap events onto raw `F2(k)`.

Passing to swap orbits removes this obstruction but leaves only `k+1` orbit states. Recovering raw multiplicity `2k+1` would require distinguishing the two members of every off-diagonal orbit. No independent primary-side involution or transverse orientation exists in the frozen semantics, so one-primary-step-per-raw-incidence accounting is not established.

## Conditional square theorem

If a future theorem independently proves that the k-layer occupancy interval consumes all and only the raw frontier incidences, then `A_(k+1)-A_k=2k+1` and telescoping gives `A_k=sum_(r=0)^(k-1)(2r+1)=k^2`.

Under that specific phase convention square numbers are **activation thresholds**, and `C_k=(k+1)^2-1`. This conditional arithmetic is exact but its coupling premise is not established here.

Accordingly, `n=5` remains unresolved. Under the unproved occupancy-frontier premise it would lie in the k=2 layer between activation indices 4 and 9, giving the lower square 4; but Stage Z cannot promote this to `FIVE_TO_FOUR_FORCED_BY_FRONTIER_COUNT`.

## m-slot control and semantic typing

For `m=1..4`, `|Fm(k)|=(k+1)^m-k^m`, and these frontier counts telescope to perfect powers. The same gap-freedom theorem blocks every such fixed frontier law absent new structure. The explicit triaxial coordinate representation has two transverse coordinate slots relative to a chosen primary ray, but that implementation fact does not independently promote a two-slot Cartesian frontier to native primary-event semantics.

## Freezes

- `TRANSVERSE_FRONTIER_COUNT_2K_PLUS_1_ESTABLISHED_AS_ABSTRACT_COUNT = true`
- `PRIMARY_GAP_LENGTH_FREEDOM_ESTABLISHED = true`
- `RAW_FRONTIER_POINTWISE_REFLECTION_EQUIVARIANT_ENUMERATION_OBSTRUCTED_FOR_K_GE_1 = true`
- `PRIMARY_GAP_TO_TRANSVERSE_FRONTIER_COUPLING_ESTABLISHED = false`
- `PRIMARY_GAP_TO_TRANSVERSE_FRONTIER_COUPLING_NOT_ESTABLISHED = true`
- `ODD_GAP_SEQUENCE_CONDITIONALLY_FORCES_SQUARE_ACTIVATION_THRESHOLDS = true`
- `ODD_GAP_SEQUENCE_FORCES_SQUARE_THRESHOLDS = false` (unconditional)
- `TWO_SLOT_FRONTIER_NATIVELY_SELECTED = false`
- `M_SLOT_AMBIGUITY_REMAINS = true`
- `ROOT_DEGREE_REMAINS_UNIDENTIFIED = true`
- `FIVE_TO_FOUR_OR_NINE_UNRESOLVED = true`
- `UNIVERSAL_BRC_LAW_NOT_ESTABLISHED = true`

No Stage-AA or later task was consumed.
