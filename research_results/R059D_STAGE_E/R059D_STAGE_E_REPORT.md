# R059D Stage E — System-Spanning Count Response / Localization

Researcher-ID: `EM-R059D-4C7E21`
Taskbook source: `9221cb7e04da772b68a9a663e07f6e2207f00e1e`
Frozen Stage-D parent: `04a9ec5570847f957f6ab56e4fa490a9eabb02a0`

## Disposition

`RESPONSE_RESOURCE_DEPENDENT_MIXED_REGIME`

Stage-D exact aligned recurrence is not system-spanning response. Under the frozen bounded-local controller `U_BPLUS2_ONEBIT`, all primary I1/I2 interventions have exact response-participant count `1` for every positive q (`q=3 or q>=5`) and every integer `N>=1`, under both schedulers. The q=3 reach-1 A1 comparator has at most `min(N,2)` participants. Thus the autonomous recurrence can be macro-endpoint exact while causally local.

## Causal count semantics

Primary causal response uses per-tag source-lineage CPBC counts `C_i(x)`. Independent Cartesian factors from other tags are not multiplied into `TAG_COUNT_CHANGE`. The global product-weighted history count is retained as a diagnostic only, because otherwise an I1 branch removal would mechanically rescale unrelated tag marginals and manufacture false system-spanning participation.

## Frozen interventions

- `I1_PLUS_ONLY`: chosen tag keeps launch H and loses H_INV.
- `I1_MINUS_ONLY`: chosen tag keeps launch H_INV and loses H.
- `I2_ADD_PLUS_TOKEN`: add exactly one source-lineage CPBC count token at the reachable post-V plus state of the chosen tag.

The chosen tag is a canonical relabeling representative; all theorems are tag-equivariant.

## Bounded-local baseline theorem

For `C0_U_BPLUS2_ONEBIT`:
- I1 plus: `RESPONSE_PARTICIPANT_COUNT=1`, endpoint remains D0 at round 3.
- I1 minus: participant `1`; perturbed tag is nonaligned at round 3.
- I2 +1 token: participant `1`; no action set changes; D0 endpoint remains exact with altered local multiplicity.

The mirror controller has the same response class. The q=3 A1 comparator has `min(N,2)` participants under I1 plus and `1` under I1 minus/I2.

For a fixed finite H-probe set P with `D=max|r|` and fixed T rounds, an intervention dependency edge can only join tag indices satisfying `|q(j-i)|<=D+2T`. Therefore

`RESPONSE_PARTICIPANT_COUNT <= min(N, 2*T*floor((D+2*T)/q)+1)`.

For fixed D,T,q this is independent of N. This is a relational dependency-word theorem, not a metric-ball claim.

## Resource search

For the diagnostic local H-window of resource K and the frozen I2 token, the exact responding-tag count is

`P_K(N,q)=|{d mod N: |q*d|<=K or |q*d-2|<=K}|`.

- Fixed `K in {1,2,4,8,16}`: bounded-local.
- `K=isqrt(N)`: subextensive. Exact certificates include `P_K<=2*isqrt(N)+3`; for every integer m>=1 and N>=16*m^2, `P_K<=N/m`; along `N=(q*m)^2`, `P_K>=2m+1`.
- `K=N`: extensive but not full on the large-N family:
  `P_N=min(N,floor(N/q)+floor((N+2)/q)+1)`,
  with `q*P_N>=N` and `P_N<N` for `N>=2q`.
- Per-tag full macrostep path cloud remains source-local and does not create cross-tag response by itself.
- Whole-system full-cloud parity gives `N:N` system-spanning response exactly, but is frozen as `GLOBAL_READOUT_CONTROL`.

Thus bounded, subextensive, extensive, and system-spanning response can all be produced by changing the declared information resource.

## Crossover identifiability

Two pre-frozen resource controls use:
- `K=2` below `N=17`, `K=N` at/above 17.
- `K=2` below `N=31`, `K=N` at/above 31.

They move the apparent bounded→extensive boundary from 17 to 31 without changing the relational carrier. Therefore this is a `COUNT_HORIZON_CROSSOVER` control, not an intrinsic N boundary.

Frozen:

`INTRINSIC_N_MACRO_MICRO_CROSSOVER_STATUS = NO_INTRINSIC_N_CROSSOVER_IDENTIFIED`.

## Checker

Deterministic checker: `65565/65565 PASS`.
Digest: `c50b5ea7596ecdd19edbadd2da218e85774714e58f01a3e7f4b3ad574c80289d`.

It independently regression-checks baseline intervention response with explicit finite carrier states, exact window formulas against brute finite cases, fixed-K/subextensive/extensive resource formulas, the frozen huge-N registry, and all kill gates. Huge-N checks are O(1) symbolic formulas; no `10^36` enumeration occurs.

## Firewalls

`PHYSICAL_PROBABILITY_FROM_COUNTING = NOT_ESTABLISHED`

`PHYSICAL_RIGIDITY_INTERPRETATION = NOT_ESTABLISHED`

`QUANTUM_BRIDGE = NOT_ESTABLISHED`

`STOP_FOR_DRIVER_REVIEW`
