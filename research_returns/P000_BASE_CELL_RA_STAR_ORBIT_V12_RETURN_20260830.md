# P000 framed Full-Cell `a` lift, K4-star orbit and exact `S4` relation closure V12 — Research Return

Status: `FROZEN RESEARCH RETURN / DRIVER REVIEW REQUIRED`

Researcher-ID: `EM-P000FCC12-A4C9E1`  
Task-ID: `RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE`  
Publication-ID: `TP2-B4D8C2F71A6E9053C118`  
Claim-ID: `chatgpt-p000fcc12-20260830-0915-a4c9e1`  
Execution branch: `research/p000-base-cell-ra-star-orbit-v12-em-p000fcc12-a4c9e1`  
Execution base: `7d22f77094e88dd3b9c2aa6118af8836fb212466`

Hard target:

`P000_FRAMED_BASE_CELL_a_LIFT_K4_STAR_ORBIT_AND_S4_RELATIONS_EXACTLY_CLASSIFIED`

Primary terminal class:

`FRAMED_COMMON_MODEL_S4_LIFT_AND_FOUR_STAR_ORBIT_EXACTLY_REALIZED`

## 1. Executive result

Gen12 has a finite exact **single common-model** positive witness.

Use the accepted K4 carrier incidence only as a downstream atlas:
the four carrier vertices are `A,B,C,D`, while the six frozen native axis types are the six K4 edges

`E1=AB, E2=AC, E3=AD, E4=BC, E5=BD, E6=CD`.

The two frozen carrier generators induce exactly

`a=(BCD)`,

`a_xi=(E1 E2 E3)(E4 E6 E5)`

and

`b=(AB)`,

`b_xi=(E2 E4)(E3 E5)`,

with `E1,E6` fixed under `b_xi`.

Now take four **distinct opaque Full-Cell identities**

`xA,xB,xC,xD`

with native adjacency the complete graph `K4`. Define independent Cell maps

`r_a=(xB xC xD)` with `xA` fixed,

`r_b=(xA xB)` with `xC,xD` fixed.

These are declared automorphisms of the four opaque Cell identities; the notation does **not** identify a Cell with a carrier vertex and does not quotient native identity by the carrier atlas.

Equip all four Cells with one common framed/PF-10 model:

- identity presentation frames `f_x`;
- uniform ingress and egress `(1,1,1,1,1,1)`;
- passage tensor `M_x=I_6`;
- frame-induced identity channel connection on every oriented K4 adjacency edge.

Then

`Pi^a_x=f_{r_a(x)} a_xi f_x^-1=a_xi`

and

`Pi^b_x=f_{r_b(x)} b_xi f_x^-1=b_xi`.

Both satisfy the Gen11 strict-lift criterion in the **same model**.

Exact enumeration gives

`|<R_a,R_b>|=24`,

the bare-Cell permutation image has order `24`, the axis-type image has order `24`, and both forgetful kernels are trivial. Moreover

`R_a^3=R_b^2=(R_a R_b)^4=id`

on the declared enriched framed/PF-10 state, not only on axis labels.

Therefore the common model realizes a faithful carrier-`S4` representation at:

1. enriched framed/PF-10 automorphism level;
2. bare opaque-Cell permutation level;
3. frozen six-axis readout level.

No relation residue is present **in this witness**.

This is an existence theorem in the declared downstream model class. It does **not** prove that bare P000 canonically supplies these four Cells, canonically selects `r_a,r_b`, or has complete native rotation group `S4`.

## 2. Frozen carrier-to-axis action is derived, not guessed

The K4 edge incidence gives a direct derivation.

Under `a=(BCD)`:

- `AB -> AC -> AD -> AB`, hence `(E1 E2 E3)`;
- `BC -> CD -> DB -> BC`, hence `(E4 E6 E5)`.

So

`a_xi=(E1 E2 E3)(E4 E6 E5)`.

Under `b=(AB)`:

- `AB` fixed;
- `AC <-> BC`, hence `E2 <-> E4`;
- `AD <-> BD`, hence `E3 <-> E5`;
- `CD` fixed.

So

`b_xi=(E2 E4)(E3 E5)`.

With the convention `pq=p o q` (apply `q` first), the checker verifies

`a_xi^3=id`,
`b_xi^2=id`,
`(a_xi b_xi)^4=id`

and independently enumerates

`|<a_xi,b_xi>|=24`.

Thus the six-axis action is the faithful K4-edge action of the accepted carrier `S4`, not a local-channel `S6` promotion.

## 3. Exact common Full-Cell witness

### 3.1 Opaque Cell set and native adjacency

Let

`X={xA,xB,xC,xD}`

be four distinct opaque Cell identities.

Set

`Adj={all unordered pairs of distinct Cells in X}`.

Hence the native adjacency graph in the witness is `K4`.

Define

`r_a(xA)=xA`,
`r_a(xB)=xC`,
`r_a(xC)=xD`,
`r_a(xD)=xB`;

and

`r_b(xA)=xB`,
`r_b(xB)=xA`,
`r_b(xC)=xC`,
`r_b(xD)=xD`.

Then

`r_a^3=id`, `r_b^2=id`,

and both preserve the actual Cell adjacency relation.

The construction is a downstream witness. The symbols `A,B,C,D` and `xA,xB,xC,xD` remain different typed objects; only an explicitly declared witness association is used to organize the four derived star objects below.

### 3.2 Frames and PF-10 data

For every Cell choose the identity presentation frame

`f_x:{E1,...,E6}->{0,...,5}`.

At every Cell set

`I_x=O_x=(1,1,1,1,1,1)`

and

`M_x=I_6`.

The tensors are invariant under both frozen six-axis permutations. Hence the Gen11 PF-10 equivariance conditions hold simultaneously for `R_a` and `R_b`.

The choice `M_x=I_6` also gives

`Omega_b=false`

at every Cell. Therefore this successful two-generator lift does not use the Gen8 contact route and preserves the Gen11 classification

`Omega_b = CONTACT_ROUTE_SPECIFIC`.

### 3.3 Retained connection

Use the frame-induced connection

`T_xy=f_y f_x^-1=id`

on every oriented adjacency edge.

It is flat. Every triangle holonomy, hence every K4 loop holonomy, is identity.

For `g in {a,b}` the naturality equation

`T_{r_g(x),r_g(y)} Pi^g_x = Pi^g_y T_xy`

holds exactly.

Nonflat connections are not being declared impossible. Gen11 already established that a nonflat independent connection can coexist with a rotation when the holonomy representation is equivariant. Gen12 needs only one exact common-model witness, so the flat frame-induced connection is the minimal retained connection choice.

## 4. Strict `a` and `b` lifts

Define

`Pi^a_x=f_{r_a(x)} a_xi f_x^-1`

and

`Pi^b_x=f_{r_b(x)} b_xi f_x^-1`.

The checker verifies for `R_a`:

1. `r_a` is a Cell bijection;
2. `r_a^3=id`;
3. native adjacency is preserved;
4. full PF-10 `I/O/M` data are equivariant under `Pi^a_x`;
5. retained connection naturality holds;
6. the three typed channel transports around the `r_a` orbit compose to identity.

It separately verifies the accepted Gen11 template for `R_b`:

1. `r_b` is a Cell bijection;
2. `r_b^2=id`;
3. native adjacency is preserved;
4. full PF-10 data are equivariant under `Pi^b_x`;
5. retained connection naturality holds;
6. the two typed channel transports compose to identity.

Thus this is a one-common-model lift. It is not a splice of the Gen11 two-Cell `b` witness with a separate `a` witness.

## 5. Four K4-star slice objects

Freeze the four derived axis stars:

`J_A={E1,E2,E3}`,
`J_B={E1,E4,E5}`,
`J_C={E2,E4,E6}`,
`J_D={E3,E5,E6}`.

The exact axis transport is

`a_xi(J_A)=J_A`,
`a_xi(J_B)=J_C`,
`a_xi(J_C)=J_D`,
`a_xi(J_D)=J_B`;

and

`b_xi(J_A)=J_B`,
`b_xi(J_B)=J_A`,
`b_xi(J_C)=J_C`,
`b_xi(J_D)=J_D`.

Gen12 does not stop at these set equalities.

Inside the declared witness define the downstream star object `S_U` to contain:

- the opaque Cell anchor `xU`;
- the incident three-axis set `J_U`;
- the restricted PF-10 ingress/egress/diagonal passage state;
- the complete local three-axis incidence relation;
- pairwise overlap/gluing with the other star objects;
- the corresponding native Cell adjacency.

For every distinct `U,V`,

`J_U intersect J_V={E_UV}`

is exactly one axis. The checker proves that `R_a` and `R_b` simultaneously transport:

- the opaque Cell anchor;
- the full three-axis set;
- the restricted PF-10 state;
- the local three-axis relation;
- the singleton overlap axis;
- the Cell adjacency supporting that overlap.

Hence `J_C,J_D` are not promoted merely by relabeling an FCC chart; in this witness their declared derived star objects are transported by the actual Cell automorphisms.

This remains downstream structure. It is not a new P000 root axiom saying that all native Cells intrinsically come in a canonical K4-star quadruple.

## 6. Exact relation closure

Let an enriched automorphism be represented by its pair

`(Cell permutation, axis-type permutation)`

together with the uniquely frame-compatible local channel transports.

Set

`R_a=(r_a,a_xi)`,
`R_b=(r_b,b_xi)`.

The checker computes, rather than assumes,

`R_a^3=id`,
`R_b^2=id`,
`(R_a R_b)^4=id`.

The same words are identity on:

- opaque Cell identities;
- frozen axis types;
- local PF-10 tensors;
- all four declared star objects;
- the retained frame-induced connection.

Thus the exact residue of every required relation word in this model is

`TRIVIAL_IN_DECLARED_MODEL`.

No hidden Cell-kernel action is being quotiented away.

## 7. Generated action, images and kernels

Breadth-first enumeration from the two exact generators gives

`|<R_a,R_b>|=24`.

Projecting the same 24 enriched automorphisms to bare Cell permutations gives `24` distinct permutations. Therefore

`|Image_Cell|=24`

and

`Ker(enriched -> bare Cell)=1`.

Projecting to the six frozen axis types also gives `24` distinct permutations. Therefore

`|Image_axis|=24`

and

`Ker(enriched -> axis readout)=1`.

Consequently the accepted carrier `S4` is faithfully represented at both levels **within this declared model**.

A small sharpness corollary is immediate: a faithful bare-Cell image of a 24-element group cannot act on fewer than four Cells because `|S_3|=6<24`; the four-Cell witness is therefore cardinality-minimal for a faithful 24-element bare-Cell permutation realization.

This minimality concerns this finite faithful witness problem, not a claim that P000 reality has four Cells.

## 8. Gauge regression

Identity frames are only a convenient presentation.

The checker applies four different local channel permutations `g_x`, replaces

`f_x` by `g_x f_x`,

co-transforms PF-10 data, and replaces the connection by

`T'_xy=g_y T_xy g_x^-1`.

It then recomputes

`Pi'^a_x=g_{r_a(x)} Pi^a_x g_x^-1`

and

`Pi'^b_x=g_{r_b(x)} Pi^b_x g_x^-1`.

Both strict lifts still pass.

More strongly, for every pair among the exactly enumerated 24 enriched group elements and every Cell, the checker verifies the typed channel-transport composition law. Hence the 24-element result is not an artifact of identity frames or channel names.

Local `S6` remains presentation/gauge symmetry only.

## 9. Connection and holonomy disposition

The positive witness uses a frame-induced flat connection, so every required holonomy is identity and every group word acts naturally on connection data.

The result does **not** revise Gen11's stronger statement:

`NONFLAT_CONNECTION != AUTOMATIC_ROTATION_OBSTRUCTION`.

If a later task asks for nonflat simultaneous `a,b` models, the exact condition must be equivariance of the holonomy representation under the whole generated action. That is outside the necessity of the present positive witness and is not promoted here as a new task.

## 10. Contact-route regression

Because `M=I_6`,

`Omega_b=false`

throughout the positive common model, while both `R_a` and `R_b` exist and close to the faithful 24-element action.

Therefore Gen12 gives an additional exact witness for the already accepted semantic guard:

`CONTACT_ROUTE_REQUIRED_FOR_ROTATION = FALSE`.

No contact premise enters the proof of the common-model group lift.

## 11. Exact theorem and scope

### Theorem — finite common-model realization

There exists a finite declared framed/PF-10 Full-Cell model with four distinct opaque Cells, retained native adjacency, full PF-10 state, a retained channel connection, a strict `a` lift and the accepted type of strict `b` lift such that:

1. the frozen six-axis actions are exactly
   `a_xi=(E1 E2 E3)(E4 E6 E5)` and
   `b_xi=(E2 E4)(E3 E5)`;
2. the four K4-star derived objects are transported equivariantly, including Cell anchors, restricted state, local relation and overlap/gluing;
3. `R_a^3=R_b^2=(R_aR_b)^4=id` on the declared enriched state;
4. `<R_a,R_b>` has exactly 24 elements;
5. the bare-Cell image and axis-type image both have exactly 24 elements;
6. the forgetful kernel to bare Cells and the axis-readout kernel are both trivial;
7. `Omega_b` is false, so the contact route is not used.

Hence valid terminal class:

`FRAMED_COMMON_MODEL_S4_LIFT_AND_FOUR_STAR_ORBIT_EXACTLY_REALIZED`.

### Non-theorem / frozen boundary

This return does **not** prove any of the following:

- bare P000 forces the four-Cell K4 witness;
- bare P000 canonically chooses `r_a` or `r_b`;
- every allowed Full-Cell model admits these generators;
- relation residues are impossible in other models;
- the complete native P000 rotation group is `S4`;
- local channel `S6` is a native rotation group;
- carrier labels equal native Cell identities;
- FCC readout equality defines native identity;
- time is rotated.

A stronger universal or canonical-existence statement requires a separate publication.

## 12. Deterministic evidence

Checker:

`research_checks/P000_BASE_CELL_RA_STAR_ORBIT_V12_CHECK_20260830.py`

Model certificate:

`research_artifacts/P000_BASE_CELL_RA_STAR_ORBIT_V12/MODEL_CERTIFICATE.json`

Exact checker output:

```text
PASS P000_BASE_CELL_RA_STAR_ORBIT_V12_CHECK
terminal_class=FRAMED_COMMON_MODEL_S4_LIFT_AND_FOUR_STAR_ORBIT_EXACTLY_REALIZED
axis_a=(E1 E2 E3)(E4 E6 E5)
axis_b=(E2 E4)(E3 E5)
Ra_order=3
Rb_order=2
RaRb_order=4
enriched_action_order=24
bare_cell_image_order=24
axis_type_image_order=24
forgetful_to_cell_kernel_order=1
axis_readout_kernel_order=1
relation_residue=TRIVIAL_IN_DECLARED_MODEL
star_orbit=A|BCD_under_a;AB_swap_under_b;C,D_fixed_under_b
geometric_star_transport=cell+axes+PF10+local_relation+overlap_gluing
connection=FRAME_INDUCED_FLAT_EQUIVARIANT
Omega_b=false_in_positive_common_model
contact_route_required=false
gauge_covariance=verified_nonuniform_local_reindexing
full_P000_native_rotation_group_promoted=false
```

Method reuse:

`T7_FINITE_SYMMETRY_EQUIVARIANCE=REUSE_APPLIED`

`T9_HOLONOMY_COCOYCLE_GLUING=REUSE_APPLIED`

No new general-purpose tool is claimed.

## 13. Hard-target disposition and routing

Hard target disposition: `SUCCESS`.

Primary verdict:

`FRAMED_COMMON_MODEL_S4_LIFT_AND_FOUR_STAR_ORBIT_EXACTLY_REALIZED`.

The decisive new information over Gen11 is not merely a standalone `R_a`: the exact same four-Cell framed/PF-10 model carries both generators, the full four-star transport, all required group words, and trivial forgetful kernels.

Recommended Driver decision:

- if the task only requires existential common-model realization and exact relation/kernel classification in the declared downstream model class, accept and freeze Gen12 at that strength;
- do **not** promote the result to bare-P000 canonical existence or complete native rotation-group status;
- if a next stage is desired, the genuinely new question is universal/canonical lifting or classification of possible nontrivial extension residues across a broader Full-Cell model class, which requires a separate task.

No Foundation/P000 source mutation is authorized by this return.
