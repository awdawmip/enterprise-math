# X6 LP026/LP028: first shell where min-zero + BRC fails, with one native future norm probe

Date: 2026-11-13. Parent: `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`. Research lane: `chatgpt-research-onhour-enterprise-math-20260923`. Scientific baseline: frozen P000 V5 / signed native `Z^6` at `59538f585d037d09ef687b28715c4bc1a3f9fe03`; historical comparison `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Status: **AUTHOR-PROVED / EXACT FINITE ORACLE EXECUTED / NONBLIND / UNREVIEWED / NOT_ADMITTED**.

## Exact new scientific unit

For `z in Z^6`, write `D=(1,1,1,1,1,1)`, `G(z)=sum z_i^2`, `rho(z)=z-min(z)D`, `T(z)=sum |z_i|`, and `B(z)=T(z)!/prod_i |z_i|!`, the **free unweighted signed primitive shortest-path** multiplicity. Define `S_N={z:G(z)=N}`.

**Theorem 1 (minimal collision norm):** The map `z -> (rho(z),B(z))` is injective on each of `S_0,S_1,S_2`, but not on `S_3`. On `S_3`, 160 native endpoints form 140 relative fibers, including exactly 20 double fibers and 120 singletons. Each double pair has identical `B=6`.

**Proof.** If `rho(z)=rho(w)` with `z!=w`, order the pair as `w=z+kD` with integer `k>=1`. Equality of squared norms `N` gives `sum z_i=-3k` and the midpoint bound
`N>=3k^2/2`. Also `sum z_i = sum z_i^2 (mod 2)`, so `k=N (mod 2)`. For `N=0,1` the midpoint bound rules out any `k`; for `N=2` parity requires `k>=2`, hence `N>=6`, also impossible. For `N=3`, necessarily `k=1`. Every shell point has exactly three `±1` coordinates and three zeros. The lower point must have sum `-3`, hence it is exactly `z=(-1 on A,0 off A)` for a unique three-element subset `A of {1,...,6}`. Then `w=z+D=(0 on A,1 off A)`. All 20 choices of `A` give distinct two-element fibers, and no other collision is possible by the above equation. Both members have `T=3`, `B=3!=6`. Counting `C(6,3)*2^3=160` states yields 120 singletons and 140 observer labels. QED.

Example `z=(-1,-1,-1,0,0,0)`, `w=(0,0,0,1,1,1)`: both have `G=3`, `rho=(0,0,0,1,1,1)`, `T=3`, `B=6`; they are distinct native Cell displacements.

**Consequence for actual BRC aggregation:** The native signed G=3 shell contains `160*6=960` free shortest path words. Counting one `B=6` per distinct min-zero observer label instead yields `140*6=840`, missing 120 (the second BRC mass of each of the 20 double fibers). This is a fully specified counterexample to extrapolating the already author-verified *G=25-specific* `(rho,B)` injectivity to every shell. It does not identify a wrong active consumer by itself.

**Theorem 2 (global one-probe recovery):** For any fixed native axis `i`, retain `r=rho(z)`, `g=G(z)`, and a genuinely measured native future-norm probe `q_i=G(z+e_i)`. For every `z in Z^6`,
`z_i=(q_i-g-1)/2`, `h=z_i-r_i`, and `z=r+hD`.
Thus `(rho(z),G(z),G(z+e_i))` is globally injective, provided that exact signed primitive unit step is an allowed operation and the probe is evaluated before any information-losing quotient. One probe suffices for endpoint recovery in this specific observer/probe language; path ordering, signed amplitudes and provenance remain separate.

Proof: Expand `G(z+e_i)=G(z)+2z_i+1` and substitute the decoded `z_i` into `rho(z)=z-hD`. QED.

## Exact execution and typed consumer boundary

Independent Python exact-integer checker: `research_checks/X6_G3_FIRST_RHO_BRC_COLLISION_AND_ONE_PROBE_20261113.py`; local executed file Git blob `7d38805220652d7a236b78dcba55aebc0df15685`, SHA256 `40398fa0363463141c694c09922fb69fe769babd534cad7f1054db8d7e93d14b`. Actual exit code 0 with status `PASS_X6_G3_FIRST_RHO_BRC_ALIAS`. Complete exhaustive `S_0,S_1,S_2,S_3`; 20 double-pair constructive checks; 15,625 states in `[-2,2]^6` checked with fixed-axis probe decoder; two additional exact large-integer/zero cases. Expected summary: shell state counts 1/12/60/160; observer labels 1/12/60/140; G3 path mass 960 versus naive de-duplicated observer mass 840.

Source-level interfaces verified at immutable Foundation commit `59538f585d037d09ef687b28715c4bc1a3f9fe03`: `experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py` (Git blob `ac32f6d82a91db99297e587cf63b0df95cece514`) provides `relative_class`, `Spatial6` and `full_distance_squared`; `signed_brc.py` (blob `300a96e3dc24bf6fff73743037a0347a8bc83176`) provides `shortest_path_multiplicity`. The current `relative_endpoint_multiplicity` is explicitly described as an *older positive-quotient observer formula*. It should not be reused as a native signed-shell endpoint count. The new standalone checker did **not** import or execute those native modules; original native benchmark and current consumer end-to-end verification remain separate.

## Current scientific frontier and custody

The earlier signed native G=25 certificate (7812 endpoints, 6372 `rho` labels, `(rho,B)` injective only on that shell) remains valid, frozen and consumed, not rerun. Original G25 Source publication request `onhour-20261113-1714-x6-native-g25-progress-v1` has since been read as `SUCCEEDED / SOURCE_CHECKPOINT_PUBLISHED`; this is authenticated Source progress, not mathematical admission.

New specific unfinished work: identify a real active LP026/LP028 caller using `(rho,T,B)` as a universally unique signed endpoint or using one BRC count per quotient label to infer native path mass. Use these 20 exact G3 pairs as input to its **original** checker; patch only a demonstrated wrong assertion, retaining original benchmark object, test scope and source pins. Continue LP011/LP019 precise old wrong-caller attribution and the 28-LP dependency closure. Preserve Researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`, historical winning CLAIM `MCP-bdd4acf9d96a8f1f0dfab4e9`, RUN `RUN-756de85b94c23b46b181f7b8`; new Source checkpoint requires fresh own native authorization and may not be inferred from this GitHub write. Independent Driver `REQUEST_REVISION` remains open.
