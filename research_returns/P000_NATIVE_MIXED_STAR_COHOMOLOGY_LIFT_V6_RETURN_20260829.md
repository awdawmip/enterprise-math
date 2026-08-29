# P000 原生混合星切面、signed-K4 上同调与最小旋转提升 V6 — Research Return

Status: `RESEARCH_RETURN_FROZEN / EXACT_NATIVE_LIFT_OBSTRUCTION_AND_MINIMAL_MISSING_STATE_PROVED / AWAITING_DRIVER_REVIEW`

Task: `RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE`  
Publication: `TP2-CFE6E9F14623E929911E` (Generation 6)  
Researcher-ID: `EM-P000NATFCC6-E200EE`  
Claim: `chatgpt-p000natfcc6-20260829-1450-a1c3e7`  
Execution branch: `research/p000-native-mixed-star-cohomology-lift-v6-em-p000natfcc6-e200ee`

Hard target:

`P000_NATIVE_MIXED_STAR_COHOMOLOGY_AND_MINIMAL_ROTATION_LIFT_EXACTLY_CLASSIFIED`

## 1. Terminal verdict

Freeze exactly:

`EXACT_NATIVE_LIFT_OBSTRUCTION_AND_MINIMAL_MISSING_STATE_PROVED`.

The decisive separation is:

1. the accepted chart-transition signature is a **nonzero graph-cohomology / switching class** on `K4`;
2. nevertheless its `S4` **equivariant lifting obstruction is zero**: the class contains an `S4`-fixed all-negative representative and the exact gauge-correction cocycle is a coboundary;
3. the full switching-automorphism lift group of this carrier signature is therefore the **split** central extension `S4 x C2`, not a forced binary-octahedral / non-split `2.S4`;
4. relative to the chosen generators `a=(BCD)`, `b=(AB)`, the lifted relations have
   `alpha=beta=gamma=0`;
5. hence the carrier `Z2` holonomy does **not** explain the remaining P000-native failure;
6. the remaining obstruction lies one typed layer lower: the current native six-dimensional clone-product model exposes only whole-factor three-axis states and the declared native rotation algebra is only `G0={id,rho} ~= C2`; it contains no legal full-state lifts of `a` or `b`, and the mixed windows `J_B,J_C,J_D` are not native geometric slices in the current signature;
7. no passive finite hidden fiber, including one `Z2` bit, can manufacture the missing base-space mixed-slice restriction maps or a missing cross-block native transformation;
8. the first discriminating extra native operation is a `b`-type **partial cross-block axis mixer**. A block-preserving `3+3` symmetry algebra can realize the `a` axis permutation but cannot realize `b`.

Thus the task closes the cohomology/double-cover question and localizes the native frontier:

`CARRIER_H1_NONTRIVIAL BUT S4_LIFT_SPLIT`
  
`!=`
  
`FULL_NATIVE_S4_LIFT_EXISTS`.

The exact current blocker is:

`MIXED_NATIVE_SLICE_GEOMETRY + CROSS_BLOCK_FULL_STATE_ROTATION_NOT_PRESENT_IN_CURRENT_NATIVE SIGNATURE`.

No Foundation or Working-Truth promotion is claimed.

---

## 2. Frozen data and notation

Use chart vertices

`V={A,B,C,D}`

and `K4` edge order

`(AB,AC,AD,BC,BD,CD)`.

Encode an edge sign additively in `F2`, with

- `0 = +1`,
- `1 = -1`.

The accepted transition signature is

`q=(1,1,0,1,0,0)`,

i.e.

`q_AB=q_AC=q_BC=-1`,
`q_AD=q_BD=q_CD=+1`.

The native-to-carrier axis typing remains

`E1->AB`,
`E2->AC`,
`E3->AD`,
`E4->BC`,
`E5->BD`,
`E6->CD`.

The four K4 star windows are

`J_A={1,2,3}`,
`J_B={1,4,5}`,
`J_C={2,4,6}`,
`J_D={3,5,6}`.

The accepted carrier generators are

`a=(BCD)`,
`b=(AB)`,

with

`a^3=e`,
`b^2=e`,
`(ab)^4=e`.

Everything below keeps:

`CARRIER_SWITCHING_EQUIVALENCE != NATIVE_STATE_EQUIVALENCE`

and

`CARRIER_SIGN != PRIMITIVE_NATIVE_NEGATIVE_AXIS`.

---

## 3. Required Output A — exact signed-K4 / H^1 classification

### 3.1 Cycle products

The four triangular cycle products are all negative:

`ABC=-1`,
`ABD=-1`,
`ACD=-1`,
`BCD=-1`.

The three independent 4-cycle products are all positive:

`ABCD=+1`,
`ABDC=+1`,
`ACBD=+1`.

Hence every odd cycle of `K4` is negative and every even cycle is positive.

Therefore the signature is exactly **antibalanced**.

This is classical signed-graph mathematics, not a novelty claim.

### 3.2 Switching to all-negative

Let

`q_-=(1,1,1,1,1,1)`

be the all-negative signature, and let `t=chi_D` be the vertex 0-cochain supported only at `D`.

The coboundary `delta t` toggles exactly the three edges incident to `D`, so

`q = q_- + delta t`.

Therefore:

`[q]=[q_-]`

in the switching quotient.

As a graph regarded as a one-dimensional CW complex,

`H^1(K4;F2)=C^1/im(delta:C^0->C^1)`

and

`dim H^1 = |E|-|V|+1 = 6-4+1 = 3`.

The class `[q]` is nonzero because it evaluates to `1` on every triangle.

This directly explains the earlier no-global-section result: switching cannot change cycle evaluations.

### 3.3 Exact switching orbit and normal forms

The switching orbit has exactly `2^(4-1)=8` signatures.

There are two useful normal-form notions and they must not be confused:

**Symmetry-normal form.**  
`q_-` is the unique representative in this switching class that is strictly fixed by all of `S4`.

**Hamming-minimal normal forms.**  
The minimum number of negative edges in the orbit is `2`. There are exactly three such representatives, namely the three perfect matchings:

`{AB,CD}`,
`{AC,BD}`,
`{AD,BC}`.

Thus there is no unique Hamming-minimal gauge without an extra symmetry-breaking convention.

The submitted checker exhausts all 16 vertex switching functions and recovers exactly these 8 signatures.

---

## 4. Required Output B — S4 action and exact gauge corrections

Use the push-forward convention

`(sigma.q)(uv)=q(sigma^{-1}u, sigma^{-1}v)`.

Since the all-negative representative is constant,

`sigma.q_- = q_-`

for every `sigma in S4`.

With `q=q_-+delta t`, define

`h_sigma = t + sigma.t`.

Then

`sigma.q + delta h_sigma`
`= q_- + delta(sigma.t) + delta(t+sigma.t)`
`= q_- + delta t`
`= q`.

So every carrier permutation preserves the switching class.

More strongly, the correction is an exact group 1-cocycle:

`h_{sigma tau} = h_sigma + sigma.h_tau`.

The checker verifies this identity for all `24^2=576` ordered pairs.

Because

`h_sigma = t + sigma.t`

is itself a **group coboundary**, the associated correction 2-cocycle is zero.

For the frozen generators:

- `a=(BCD)` gives `h_a=chi_B+chi_D`;
- `b=(AB)` fixes `D`, hence `h_b=0`.

The original representative `q` has strict stabilizer of order `6` (the `S3` fixing `D`), while `q_-` has strict stabilizer all `24` elements.

This is the key algebraic distinction:

`[q] != 0 in graph H^1`

but

`S4-equivariant correction obstruction = 0`.

A nontrivial cycle-holonomy class and a nontrivial group-extension class are different questions.

---

## 5. Required Output C — exact lift group and generator relations

Define the switching-automorphism lift group

`E_q = {(sigma,g): sigma in S4, g in C^0(K4;F2), sigma.q + delta g = q}`

with multiplication

`(sigma,g)(tau,h)=(sigma tau, g + sigma.h)`.

For each `sigma`, exactly two gauge corrections solve the preservation equation:

`g=h_sigma`

or

`g=h_sigma + 1_V`,

because the kernel of `delta:C^0->C^1` on connected `K4` is the constant cochains.

Hence

`|E_q|=24*2=48`.

The kernel over the identity permutation is

`{0,1_V} ~= C2`.

It is central.

But the section

`sigma -> (sigma,h_sigma)`

is a genuine homomorphism because the exact 1-cocycle identity holds.

Therefore:

`E_q ~= S4 x C2`.

This is a **split** central extension.

Let `z=(e,1_V)` denote the passive global chart-sign flip. Choose

`A~=(a,h_a)`,
`B~=(b,h_b)`.

Then exact finite multiplication gives

`A~^3=e`,
`B~^2=e`,
`(A~B~)^4=e`.

So in the requested notation

`A~^3=z^alpha`,
`B~^2=z^beta`,
`(A~B~)^4=z^gamma`

we obtain exactly

`(alpha,beta,gamma)=(0,0,0)`.

The checker also enumerates all words over `{a,b}` of length at most `8`; every word reaching carrier identity has zero correction residue under the split section.

Therefore:

`Z2_LOOP_HOLONOMY != NONSPLIT_2.S4`.

No binary octahedral group, `GL(2,3)`-type Schur cover, or other non-split double cover is forced by the frozen `q_ij` data.

Known nontrivial double covers of `S4` remain external comparison objects only.

---

## 6. Required Output D — what orientation state is actually needed

There are three different state questions.

### 6.1 Unoriented six-line carrier atlas

No extra orientation bit is required.

The physical carrier line object is already unoriented.

### 6.2 One active oriented 120-degree chart

Each chart has exactly two valid zero-sum signed `120 degree` presentations, related by common sign reversal.

Therefore, if the **active signed presentation itself** is operational state, exactly one `C2` bit is necessary and sufficient once the chart index is known.

The correction `h_sigma` tells which destination charts flip that bit under a carrier rotation.

This state is:

`CHART_INDEX + ONE_PRESENTATION_BIT`.

It is not a seventh spatial axis.

### 6.3 Whole-atlas gauge choice

The full switching orbit has eight representatives, parameterized by

`C^0(K4;F2) / <1_V> ~= C2^3`.

This `C2^3` is a gauge-choice space for a whole local-section atlas. It is not an additional native spatial fiber forced by P000.

The global constant `z` is a simultaneous presentation flip and makes the full switching-automorphism group `S4 x C2`; it remains carrier presentation state.

Thus the minimal carrier-side conclusion is:

- unoriented carrier: `0` extra bits;
- active oriented chart: `1` local presentation bit;
- no nontrivial central extension is needed.

---

## 7. Required Output E — mixed native star slices

The current native state model is frozen as

`X6 = C_A x C_B`

with state

`x=(c,kappa(d))`

and Cartesian adjacency.

Its only established three-axis slice projections are whole-factor maps

`Pi_A(x)=c`,
`Pi_B(x)=kappa(d)`,

for

`I_A={1,2,3}`,
`I_B={4,5,6}`.

The current interface does **not** contain per-axis state factors

`c=(c1,c2,c3)`

or

`d=(d4,d5,d6)`,

nor does it contain legal restrictions selecting, for example,

`E1` from the first factor together with `E4,E5` from the second.

Therefore the observation set

`J_B={1,4,5}`

cannot currently be promoted to a state restriction merely from the tuple `(c,kappa(d))`.

The same holds for `J_C` and `J_D`.

This is a type-level obstruction:

`AXIS-TYPE LABEL AVAILABLE`

does not imply

`AXIS-REFINED STATE PROJECTION AVAILABLE`.

Consequently the correct current classification remains:

`J_B,J_C,J_D = NATIVE_OBSERVATION_WINDOWS_ONLY`

and not

`NATIVE_GEOMETRIC_SLICES`.

A valid mixed-slice construction must newly supply, at minimum:

1. state restriction / local coordinates for one mixed star;
2. induced native adjacency;
3. comparison at the same declared strength as `J_A`;
4. overlap-axis transport;
5. carrier 120-degree readout;
6. chart-local orientation typing;
7. compatibility with full-state rotation.

No such data are derivable from `beta` alone.

---

## 8. Required Output F — native generator lifts

### 8.1 Existing native operation algebra is too small

The prior exact minimal tomography construction froze the available native rotation algebra as

`G0={id,rho} ~= C2`

with whole-factor exchange

`rho(c,kappa(d))=(d,kappa(c))`.

On native axis types this typed copy exchange is

`rho_axes=(E1 E4)(E2 E5)(E3 E6)`.

The previous accepted bridge already proved that this permutation is not any carrier `S4` edge action: it sends the established star `J_A` to the complementary triangle rather than another K4 star.

The present checker independently verifies:

- carrier edge actions: `24`;
- `rho_axes` is not among them;
- required `a` and `b` edge actions are not in `{id,rho_axes}`.

Hence no current native operation realizes either required generator.

### 8.2 Exact required axis permutations

Under the frozen edge typing,

`a=(BCD)` induces

`(E1 E2 E3)(E4 E6 E5)`.

It preserves the two `3+3` blocks setwise.

By contrast `b=(AB)` induces

`E2 <-> E4`,
`E3 <-> E5`,

while fixing `E1` and `E6`.

So `b` is a **partial cross-block mixer**.

This is the first generator that destroys the old whole-block system.

### 8.3 Block-symmetry stress test

To isolate the obstruction independently of the specific old `rho`, the checker uses a finite typed block model whose admissible axis action group is

`S3 wr C2`

of order

`72`.

This group permits arbitrary permutations inside each three-axis block plus optional whole-block exchange.

Exact enumeration gives:

`a_axes in S3 wr C2`

but

`b_axes notin S3 wr C2`.

Thus even a large natural enlargement of the old `C2` that preserves the `3+3` block system still cannot supply `b`.

This does not claim that the toy block model is the actual P000 Cell. It is a sharp symmetry witness for the kind of extra operation required.

### 8.4 Positive six-axis stress test

Conversely, the six-cube `Q6` admits every coordinate permutation and hence admits both required carrier edge permutations as adjacency automorphisms.

Again this is not claimed to be the P000 Cell.

Together the two stress tests show:

`six discrete axes alone`

do not decide the native lift.

The decisive missing input is the native geometry of partial cross-block mixing.

---

## 9. Passive hidden-state no-go lemma

Suppose one tries to repair the native problem by adding only a passive finite fiber

`pi: X_hat -> X6`

without changing the base native transformation law.

If a lifted rotation `R_hat_b` is required to project to a legal base transform `R_b`,

`pi o R_hat_b = R_b o pi`,

then the existence of `R_hat_b` already requires the base map `R_b`.

Therefore adding a fiber `F`, whether

`C2`, `C2^k`, or any other finite set,

cannot by itself create a missing base-space cross-block automorphism.

If instead `R_hat_b` is allowed to alter base state in a way not induced by any prior legal `R_b`, then the proposal is no longer a passive hidden-state extension; it is a **new native structural/operation extension** and must be justified as such.

Hence:

`ONE_Z2_BIT_IS_NOT_THE_MISSING_NATIVE_ROTATION`.

The carrier orientation bit solves presentation transport only.

It does not construct mixed native geometry.

---

## 10. Minimal native missing packet

The exact lower bound is now structural rather than cohomological.

Any successful full native `S4` lift must add enough native geometry to supply at least:

### M1 — one genuine mixed-star seed

At least `J_B` must become a legal native geometric slice, because `b` sends

`J_A <-> J_B`.

Without a legal codomain slice, `b` is not a legal slice-transport map.

### M2 — one cross-block full-state generator

A legal adjacency/relations-preserving

`R~_b`

must induce

`E2<->E4`,
`E3<->E5`

while fixing `E1,E6`.

This cannot be implemented by preserving or wholly swapping the old `3+3` factors.

### M3 — orbit completion

A legal full-state `R~_a` (or equivalent data) must realize the `a` action and transport

`J_B -> J_C -> J_D -> J_B`

while preserving `J_A`.

### M4 — exact relations

The native maps must satisfy, on full native/extended state,

`R~_a^3=id`,
`R~_b^2=id`,
`(R~_a R~_b)^4=id`

or else the exact native residue must be exhibited.

The carrier calculation proves there is **no carrier-forced central residue** waiting to explain a failure here.

Any future residue would therefore be genuinely native, not inherited from the signed-K4 switching class.

This packet is the smallest typed target exposed by the present proof. It is a new base geometric/operation packet, not merely additional state cardinality.

---

## 11. Required Output G — carrier identity versus native residue

### Carrier signed-atlas layer

For the split section `sigma -> (sigma,h_sigma)`:

- `a^3`: strict identity, no gauge/central residue;
- `b^2`: strict identity, no gauge/central residue;
- `(ab)^4`: strict identity, no gauge/central residue;
- every tested shortlex identity word through length `8`: strict identity;
- path to a fixed carrier permutation has the unique correction `h_sigma` under the chosen split section.

Thus there is no hidden path holonomy in this carrier group action beyond the already known graph cycle class `[q]`.

### Current native layer

There is no legal native path labeled by `a` or `b` in the current declared operation algebra.

Therefore expressions such as native `a^3` or native `(ab)^4` are not to be misclassified as identities with a hidden residue.

Their current type is:

`NON_LIFTABLE_WORD / NO_CURRENT_NATIVE_PATH`.

Time does not repair this. P000 time orders relational change; it cannot substitute for a missing spatial transformation.

---

## 12. Mandatory no-quotient boundary

The carrier bridge remains many-to-one on individual native edges of the same axis type.

Two distinct native edges can have the same line-family readout.

The checker includes a regression with two distinct native edge identities sharing the same `beta` label and keeps them unequal.

Hence:

`EQUAL_CARRIER_READOUT != EQUAL_NATIVE_STATE`

and

`CARRIER_KERNEL != AUTHORIZED_NATIVE_QUOTIENT`.

None of the switching, `S4`, or extension calculations changes this rule.

---

## 13. Required Output H — prior-art / novelty table

| INTERNAL_CLAIM | EXTERNAL_ANALOG | CLASS | P000_NATIVE_EXTRA_CONSTRAINT | NOVELTY_STATUS |
|---|---|---|---|---|
| `q` is antibalanced; cycle signs switching-invariant | Harary/Zaslavsky signed-graph balance and antibalance | `EXACT_DUPLICATE / STANDARD` | none at this layer | no novelty claim |
| `[q]=[all-negative]` | switching equivalence of antibalanced signatures | `EXACT_DUPLICATE / STANDARD` | carrier sign is not native axis sign | no novelty claim |
| `S4` stabilizes `[q]` | automorphisms of switching classes / two-graphs | `STANDARD FRAMEWORK + FINITE INSTANCE` | physical carrier subgroup fixed by prior atlas | no novelty claim |
| exact correction `h_sigma=t+sigma.t` | cohomological automorphism lifting of switching classes | `STANDARD FRAMEWORK + EXPLICIT PROJECT COMPUTATION` | must preserve project chart typing | no novelty claim |
| correction 2-cocycle is zero; `E_q ~= S4 x C2` | group-extension/cohomology theory | `STANDARD ALGEBRA + EXPLICIT INSTANCE` | global `C2` is presentation flip, not native axis | no novelty claim |
| non-split `2.S4` not forced | Schur covers / binary octahedral comparison objects | `BOUNDARY / REFUTED INFERENCE` | no Spin(3) import to native 6D | no novelty claim |
| `J_B,J_C,J_D` not constructible from current whole-factor interface | no exact external match expected | `P000-SPECIFIC TYPED OBSTRUCTION` | six native axes preserved; no carrier quotient | project-specific result; novelty undecided |
| current `G0=C2` cannot realize carrier generators | ordinary group-action obstruction | `STANDARD ARGUMENT + P000 INSTANCE` | full native state legality required | project-specific result; novelty undecided |
| passive hidden fiber cannot create missing base transform | equivariant projection/type principle | `GENERAL STRUCTURAL ARGUMENT` | hidden bit not extra spatial axis | no broad novelty claim |
| `b` is first cross-block discriminator | block-system / wreath-product symmetry | `STANDARD GROUP THEORY + P000 TYPING` | must realize native mixed Cell geometry | project-specific combination; novelty undecided |
| carrier readout collision cannot quotient native state | operation-safe semantic boundary | `PROJECT SEMANTIC CONSTRAINT` | native identity primitive | not a novelty claim |

External antecedents checked/disclosed:

- Peter J. Cameron, “Automorphisms and cohomology of switching classes”, *J. Combin. Theory Ser. B* 22 (1977), 297–298, DOI `10.1016/0095-8956(77)90079-X`.
- Peter J. Cameron, “Cohomological aspects of two-graphs”, *Math. Z.* 157 (1977), 101–119, DOI `10.1007/BF01215145`.
- Peter J. Cameron and A. L. Wells Jr., “Signatures and signed switching classes”, *J. Combin. Theory Ser. B* 40 (1986), 344–361, DOI `10.1016/0095-8956(86)90088-2`.
- standard signed-graph switching/antibalance literature summarized in the frozen project prior-art note.
- standard nontrivial double covers of `S4` are comparison objects only.

The bounded external check does not establish mathematical novelty for the P000-specific combination.

---

## 14. Required Output I — deterministic certificate

Checker:

`research_checks/P000_NATIVE_MIXED_STAR_COHOMOLOGY_LIFT_V6_CHECK_20260829.py`

Machine certificate:

`research_artifacts/P000_NATIVE_MIXED_STAR_COHOMOLOGY_LIFT_V6/certificate_20260829.json`

The checker uses finite integer/bit/permutation arithmetic only.

Expected deterministic output:

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

It verifies:

1. all K4 triangle / 4-cycle signs;
2. full switching orbit and both normal-form notions;
3. S4 strict action on the symmetric representative;
4. all gauge corrections;
5. all 576 cocycle equations;
6. split extension order `48` and generator relations;
7. mixed-star incidence;
8. current `G0` obstruction and block/Q6 stress witnesses;
9. old `rho` no-intertwiner regression;
10. chart-local two-state orientations and zero global signed sections;
11. FCC/HCP antipodal `6/3`;
12. many-to-one carrier readout without native identity collapse.

---

## 15. Tool reuse resolution

Coverage verdict:

`COMPOSE_EXISTING_TOOLS`.

Reused conceptual tools:

- `T7_FINITE_SYMMETRY_EQUIVARIANCE`;
- `T9_HOLONOMY_COCOYCLE_GLUING`;
- `T6_OPERATION_SAFE_QUOTIENT`.

New work is the exact composition:

`signed-K4 class`
`-> symmetric switching representative`
`-> explicit S4 gauge coboundary`
`-> split lift group`
`-> separation from native mixed-slice legality`
`-> cross-block generator lower bound`.

No new general-purpose tool family is claimed.

Method harvest:

`RESULT_ONLY`.

---

## 16. Final classification

The accepted `q_ij` carries genuine nontrivial graph holonomy:

`[q] != 0 in H^1(K4;F2)`.

But the full carrier rotation symmetry has a strict invariant representative and a split correction section:

`E_q ~= S4 x C2`.

Therefore the signed-K4 data do not force a projective/native double cover.

The remaining native problem is not “which 2.S4?” but:

> What native Cell structure makes a partial cross-block rotation like `b=(AB)` legal on full six-dimensional state, and thereby turns at least one mixed observation window into a genuine native geometric slice?

Current exact state:

`CARRIER_COHOMOLOGY_CLASSIFIED`.

`CARRIER_S4_LIFT_SPLIT`.

`NO_CARRIER_FORCED_CENTRAL_RESIDUE`.

`CURRENT_NATIVE_G0_HAS_NO_a_OR_b_LIFT`.

`MIXED_NATIVE_STARS_NOT_YET_GEOMETRIC_SLICES`.

`PASSIVE_Z2_STATE_INSUFFICIENT`.

`FIRST_DISCRIMINATING_NATIVE_OPERATION = CROSS_BLOCK_b_TYPE_MIXER`.

Recommended successor, if Driver accepts this return:

1. do **not** reopen signed-graph / Schur-cover classification;
2. construct `J_B` directly from primitive native Cell relations at the same strength as `J_A`;
3. construct one full-state `R~_b` carrying `J_A<->J_B`;
4. construct/verify `R~_a` and use it to generate `J_C,J_D`;
5. only then check the exact native relations and any genuinely native residue.

Stop here for Driver review.
