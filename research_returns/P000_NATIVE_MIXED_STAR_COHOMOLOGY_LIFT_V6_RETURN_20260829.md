# P000 原生混合星切面、signed-K4 上同调与最小旋转提升 V6 — Research Return

Status: `RESEARCH_RETURN_FROZEN / EXACT_NATIVE_LIFT_OBSTRUCTION_AND_MINIMAL_MISSING_STATE_PROVED / AWAITING_DRIVER_REVIEW`

Task: `RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE`
Publication: `TP2-CFE6E9F14623E929911E`
Researcher-ID: `EM-P000NATFCC6-E200EE`
Claim: `chatgpt-p000natfcc6-20260829-1450-a1c3e7`

Hard target: `P000_NATIVE_MIXED_STAR_COHOMOLOGY_AND_MINIMAL_ROTATION_LIFT_EXACTLY_CLASSIFIED`

## 1. Terminal result

Freeze:

`EXACT_NATIVE_LIFT_OBSTRUCTION_AND_MINIMAL_MISSING_STATE_PROVED`.

The accepted transition signs form a nonzero switching/graph-cohomology class on `K4`, but the `S4` equivariant lift is split. The remaining obstruction is native: the current `X6=C_A x C_B` interface has only whole-factor slices and the declared native rotation algebra is `G0={id,rho}~=C2`; it has no legal full-state lifts of the carrier generators and does not yet define the mixed windows `J_B,J_C,J_D` as native geometric slices.

The decisive separation is:

`NONTRIVIAL_GRAPH_H1 != NONTRIVIAL_S4_EXTENSION`.

No Foundation or Working-Truth promotion is claimed.

## 2. A — exact signed-K4 class

Use edge order `(AB,AC,AD,BC,BD,CD)` and additive `F2` signs (`1=-1`). The frozen signature is

`q=(1,1,0,1,0,0)`.

All four triangles have product `-1`; all three independent 4-cycles have product `+1`. Hence `q` is antibalanced.

Let `q_-=(1,1,1,1,1,1)` and `t=chi_D`. Then

`q=q_-+delta t`.

Therefore `[q]=[q_-]`. Since `K4` is a connected graph,

`dim H^1(K4;F2)=6-4+1=3`,

and `[q]` is nonzero because every triangle evaluates to `1`.

The switching orbit has exactly `8` representatives. Its unique fully `S4`-fixed representative is `q_-`. The minimum negative-edge weight is `2`, attained by exactly the three perfect matchings `{AB,CD}`, `{AC,BD}`, `{AD,BC}`. Thus symmetry-normal form and Hamming-minimal normal form are different notions.

These facts are standard signed-graph/switching mathematics, not novelty claims.

## 3. B/C — S4 correction cocycle and exact lift group

Use push-forward action `(sigma.q)(uv)=q(sigma^{-1}u,sigma^{-1}v)`. Define

`h_sigma=t+sigma.t`.

Then for every `sigma in S4`,

`sigma.q+delta h_sigma=q`.

Moreover,

`h_{sigma tau}=h_sigma+sigma.h_tau`

for all `24^2=576` ordered pairs. Thus the correction 1-cocycle is a coboundary and its induced 2-cocycle residue is zero.

For the frozen generators

`a=(BCD)`, `b=(AB)`,

we get

`h_a=chi_B+chi_D`,
`h_b=0`.

Define

`E_q={(sigma,g): sigma.q+delta g=q}`

with multiplication `(sigma,g)(tau,h)=(sigma tau,g+sigma.h)`. For each `sigma`, exactly two corrections exist, differing by the constant cochain. Hence `|E_q|=48`, the kernel is central `C2`, and the homomorphic section `sigma -> (sigma,h_sigma)` splits the extension:

`E_q ~= S4 x C2`.

Let the central constant flip be `z`. With `A~=(a,h_a)`, `B~=(b,h_b)`,

`A~^3=1`,
`B~^2=1`,
`(A~B~)^4=1`.

Therefore the requested central exponents are exactly

`(alpha,beta,gamma)=(0,0,0)`.

Shortlex words through length `8` were exhaustively checked: every carrier identity word has zero correction residue under this split section.

So the earlier `Z2` loop holonomy does not force binary octahedral, `GL(2,3)`, or any non-split `2.S4`.

## 4. D — orientation state

The unoriented carrier needs `0` extra orientation bits.

Each active signed `120 degree` chart has exactly two legal overall orientations, so if signed presentation is operational state, `1` chart-local `C2` bit is necessary and sufficient once the chart index is known.

The whole-atlas switching-gauge space has `8` representatives, i.e. `C2^3`; this is presentation gauge, not three new native spatial bits. The central global flip in `E_q` is also presentation state, not a native negative axis.

Thus:

`CHART_SIGN != NATIVE_AXIS_SIGN`.

## 5. E/F — exact native obstruction

The frozen native model is

`X6=C_A x C_B`

with whole-factor projections `Pi_A`, `Pi_B`. It does not provide per-axis state factors or legal restrictions that select, for example, `E1` from the first factor together with `E4,E5` from the second. Therefore

`J_B={1,4,5}`,
`J_C={2,4,6}`,
`J_D={3,5,6}`

remain observation windows, not native geometric slices.

This is a type obstruction:

`AXIS-TYPE LABEL AVAILABLE != AXIS-REFINED STATE PROJECTION AVAILABLE`.

The current native rotation algebra is exactly `G0={id,rho}~=C2`. Under typed copy positions,

`rho_axes=(E1 E4)(E2 E5)(E3 E6)`,

and the accepted bridge already proves this is not any carrier `S4` edge action. The checker independently verifies that neither required generator action belongs to `G0`.

The carrier generator axis actions are:

`a_axes=(E1 E2 E3)(E4 E6 E5)`,

which preserves the `3+3` blocks, and

`b_axes=(E2 E4)(E3 E5)`,

fixing `E1,E6`, which partially mixes the blocks.

A finite block-symmetry stress model with axis group `S3 wr C2` has order `72`; exact enumeration gives

`a_axes in S3 wr C2`,
`b_axes notin S3 wr C2`.

Conversely, the six-cube `Q6` admits both actions as coordinate-permutation adjacency automorphisms. These are stress witnesses only, not claims that either toy model is the actual P000 Cell. They show that six discrete axes alone do not decide the lift; the missing datum is the native geometry of partial cross-block mixing.

## 6. Passive-hidden-fiber no-go and minimal missing packet

Suppose a passive finite extension `pi:X_hat->X6` is added without changing the base native transformation law. If a lifted `R_hat_b` must satisfy

`pi o R_hat_b = R_b o pi`,

then a legal base map `R_b` must already exist. Therefore a passive `C2` bit, `C2^k`, or any other finite fiber cannot create a missing cross-block base automorphism or missing mixed-slice restriction map.

Hence:

`ONE_Z2_BIT_IS_NOT_THE_MISSING_NATIVE_ROTATION`.

Any successful native `S4` lift must add, at minimum:

1. one genuine mixed-star seed geometry, at least `J_B`, because `b` sends `J_A<->J_B`;
2. a legal full-state cross-block transform `R~_b` inducing `E2<->E4` and `E3<->E5`;
3. a legal full-state `R~_a` or equivalent orbit-completion operation carrying `J_B->J_C->J_D`;
4. exact full-state relations `R~_a^3=1`, `R~_b^2=1`, `(R~_a R~_b)^4=1`, or an explicitly native residue.

The carrier calculation proves that no carrier-forced central residue remains to explain future failure. Any future residue would be genuinely native.

## 7. G — identity/residue classification

Carrier signed-atlas layer:

- `a^3`: strict identity;
- `b^2`: strict identity;
- `(ab)^4`: strict identity;
- no central/gauge residue under the split section.

Current native layer:

- no legal native `a` or `b` path exists in the declared operation algebra;
- therefore native `a^3` or `(ab)^4` must be typed `NON_LIFTABLE_WORD / NO_CURRENT_NATIVE_PATH`, not falsely called identities with hidden holonomy.

Time only orders relational change and cannot substitute for a missing spatial transformation.

## 8. No-quotient boundary

Distinct native edges may share the same carrier line-family readout. They remain distinct native objects:

`EQUAL_CARRIER_READOUT != EQUAL_NATIVE_STATE`.

No switching operation, carrier kernel, or gauge equivalence authorizes a native-state quotient.

## 9. H — prior-art boundary

| Internal claim | External analog | Classification | Novelty status |
|---|---|---|---|
| antibalance / switching class | Harary-Zaslavsky signed graphs | standard | no novelty claim |
| automorphisms of switching class | Cameron 1977 | standard framework + finite instance | no novelty claim |
| cohomological lift corrections | Cameron two-graph/cohomology framework | standard framework + explicit computation | no novelty claim |
| `E_q~=S4 x C2` | ordinary group extension theory | explicit project instance | no novelty claim |
| non-split `2.S4` not forced | Schur covers / binary octahedral comparison | refuted inference | no novelty claim |
| mixed native slices / full-state lift | no exact off-the-shelf P000 theorem located | P000-specific compatibility problem | novelty undecided |
| no carrier quotient of native state | project semantic guard | P000-specific boundary | no novelty claim |

External antecedents checked/disclosed:

- Peter J. Cameron, “Automorphisms and cohomology of switching classes”, JCTB 22 (1977), 297-298, DOI `10.1016/0095-8956(77)90079-X`.
- Peter J. Cameron, “Cohomological aspects of two-graphs”, Math. Z. 157 (1977), 101-119, DOI `10.1007/BF01215145`.
- Peter J. Cameron and A. L. Wells Jr., “Signatures and signed switching classes”, JCTB 40 (1986), 344-361, DOI `10.1016/0095-8956(86)90088-2`.

The bounded prior-art check does not establish novelty for the P000-specific combination.

## 10. I — deterministic certificate

Checker:

`research_checks/P000_NATIVE_MIXED_STAR_COHOMOLOGY_LIFT_V6_CHECK_20260829.py`

Machine certificate:

`research_artifacts/P000_NATIVE_MIXED_STAR_COHOMOLOGY_LIFT_V6/certificate_20260829.json`

Deterministic output:

```text
PASS
signed_K4=ANTIBALANCED; H1_dim=3; switching_orbit=8; symmetric_normal_form=all_negative
strict_stabilizer_q=6; strict_stabilizer_all_negative=24
g_a= (0, 1, 0, 1) g_b= (0, 0, 0, 0) ; cocycle_pairs=576
lift_group=E_q_order_48_is_S4xC2; lift_relations: a^3=1 b^2=1 (ab)^4=1; central_residue=(0,0,0)
local_chart_orientations=2_each; global_signed_sections=0
native_current_G0=2; carrier_actions=24; rho_not_carrier_action=True
block_axis_group=72; a_in_block_group=True; b_in_block_group=False
Q6_full_coordinate_permutation_witness=True
FCC_antipodal_pairs=6; HCP_antipodal_pairs=3
```

Regressions include: all triangle holonomies `-1`, zero global signed section, old `rho` no-intertwiner, FCC/HCP antipodal `6/3`, and carrier-readout collision without native identity collapse.

## 11. Final classification and routing

Exact state:

`CARRIER_COHOMOLOGY_CLASSIFIED`.

`CARRIER_S4_LIFT_SPLIT`.

`NO_CARRIER_FORCED_CENTRAL_RESIDUE`.

`CURRENT_NATIVE_G0_HAS_NO_a_OR_b_LIFT`.

`MIXED_NATIVE_STARS_NOT_YET_GEOMETRIC_SLICES`.

`PASSIVE_Z2_STATE_INSUFFICIENT`.

`FIRST_DISCRIMINATING_NATIVE_OPERATION=CROSS_BLOCK_b_TYPE_MIXER`.

Method harvest: `RESULT_ONLY`.

If Driver accepts this return, the successor should not reopen signed-graph or Schur-cover classification. It should construct `J_B` directly from primitive native Cell relations, construct a legal full-state `R~_b`, then construct/verify `R~_a` and transport to `J_C,J_D`.
