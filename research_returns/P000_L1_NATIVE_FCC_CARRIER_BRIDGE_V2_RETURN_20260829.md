# P000 L1_NATIVE -> FCC six-line carrier atlas bridge — Research Return V2

Status: `RESEARCH_RETURN_FROZEN / BRIDGE_STRICTLY_TYPED / AWAITING_DRIVER_REVIEW`

Task: `RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE`  
Publication: `TP2-A9D4B718C2E65F3084D1`  
Researcher-ID: `EM-P000BR-3F7A9C`  
Claim: `chatgpt-p000br-20260829-1324-3f7a9c`  
Execution branch: `research/p000-l1-native-fcc-carrier-bridge-em-p000br-3f7a9c`

Hard target:

`P000_L1_NATIVE_FCC_CARRIER_ATLAS_BRIDGE_PROVED_OBSTRUCTED_OR_STRICTLY_TYPED`

## 1. Terminal verdict

Freeze exactly one terminal class:

`BRIDGE_STRICTLY_TYPED`.

Exact strength:

`AXIS-LABEL BIJECTION + L1 EDGE-TYPE READOUT + K4 STAR OBSERVATION ATLAS / NO NATIVE-STATE QUOTIENT / MINIMAL CLONE-PRODUCT FULL SLICE-ROTATION LIFT OBSTRUCTED / CHART-LOCAL ORIENTATION TORSOR REQUIRED`.

There is an exact, deterministic bridge from the six native axis **types** to the six FCC unoriented carrier-line families. After one explicit `K4` incidence choice, the four FCC `120 degree` slice types also have an exact native **observation-window** counterpart at the axis-label level.

What does **not** survive is stronger:

1. the already constructed minimal six-dimensional clone-product tomography model has two disjoint factor slices, while any two FCC `120 degree` star slices intersect in exactly one line;
2. therefore the clone-product whole-factor exchange rotation cannot intertwine with the physical FCC `S4` atlas action;
3. the four FCC star charts cannot be given one global signed choice of the six `[110]` carrier lines while keeping every chart a zero-sum `120 degree` triple; the overlap connection has gauge-invariant `Z2` loop holonomy `-1`;
4. HCP does not even possess the intrinsic six-antipodal-line target object: its accepted first shell has only three antipodal pairs.

Thus the exact bridge is **unoriented, chart-local and observation-only** beyond native axis/L1 typing. It does not identify native six-dimensional states with a 3D FCC carrier, does not quotient native states by FCC linear relations, and does not create primitive native negative axes.

No Foundation or Working-Truth promotion is claimed.

---

## 2. Sources and authority boundary

This execution preserves P000 unconditionally and reuses the exact minimal six-dimensional model from:

`research_returns/P000_6D_ROTATION_SLICE_TOMOGRAPHY_RETURN_20260829.md`.

The accepted current coordinate convention is:

`FCC_CUBIC_BARLOW = PRIMARY_COORDINATE_CARRIER`

with FCC line families

`L1=[(1,1,0)]`,
`L2=[(1,-1,0)]`,
`L3=[(1,0,1)]`,
`L4=[(1,0,-1)]`,
`L5=[(0,1,1)]`,
`L6=[(0,1,-1)]`.

The recent carrier-algebra return

`RR-774CF0739BD6CD117CF6`

is still awaiting Driver review. I use only its explicit `K4/S4` carrier interface and local chart sign section as a **non-authoritative disclosed prior result**, and independently re-check every finite fact used here. In particular it grants no native-state lift.

---

## 3. Explicit six-dimensional native model and L1_NATIVE

Reuse the minimal typed clone-product model.

Let

`K_A=(C_A,Adj_A,E_1,E_2,E_3,...)`

be the current exact three-positive-axis Cell slice, and let `K_B` be a disjoint typed copy with axes `E_4,E_5,E_6`.

Define

`X_6 := C_A x C_B`.

Write a state as

`x=(c,kappa(d))`.

Define native adjacency by the Cartesian relational rule

`Adj_6((c,kappa(d)),(c',kappa(d')))`

iff

`[Adj_A(c,c') and d=d'] OR [c=c' and Adj_A(d,d')]`.

Therefore

`L1_NATIVE = { unordered native state pairs at Adj_6 distance 1 }`.

Every L1 edge carries one of the six native positive axis-family types:

- first-factor edges: `E_1,E_2,E_3`;
- second-factor edges: `E_4,E_5,E_6`.

The model's proved admissible factor-slice family is only

`F_0={I_A,I_B}`

with

`I_A={1,2,3}`,
`I_B={4,5,6}`.

Its exact whole-factor exchange rotation is

`rho(c,kappa(d))=(d,kappa(c))`

and satisfies

`rho^2=id`,
`rho(I_A)=I_B`,
`rho(I_B)=I_A`.

This is a six-native-axis P000-compatible existence model, not a uniqueness theorem for P000.

---

## 4. Exact native-axis -> FCC-line bridge

Use the carrier relabeling

`L_AB=L1`,
`L_AC=L3`,
`L_AD=L6`,
`L_BC=L5`,
`L_BD=L4`,
`L_CD=L2`.

Freeze the explicit native-to-carrier axis map

`beta(E_1)=L_AB=L1`,
`beta(E_2)=L_AC=L3`,
`beta(E_3)=L_AD=L6`,
`beta(E_4)=L_BC=L5`,
`beta(E_5)=L_BD=L4`,
`beta(E_6)=L_CD=L2`.

This is a bijection

`beta : {E_1,...,E_6} -> {L_AB,L_AC,L_AD,L_BC,L_BD,L_CD}`.

For an individual native L1 edge `e=(x,y)` of native type `E_i`, define only the typed carrier readout

`B_1(e)=beta(E_i)`.

Classification:

- on six **axis types**, `beta` is bijective;
- on individual L1 edges, `B_1` is many-to-one because different native locations of the same axis type have the same carrier line-family readout;
- on native states, **no point-identity map is declared**.

This last clause is essential. The bridge does not extend `beta` linearly to `X_6`, so relations among FCC vectors have no native-state equality consequence.

Freeze:

`CARRIER_LINEAR_RELATION != NATIVE_STATE_RELATION`.

`EQUAL_CARRIER_READOUT != EQUAL_NATIVE_STATE`.

---

## 5. The four-star native observation incidence and its non-canonicity

With the chosen `beta`, define four native three-axis **observation windows**

`J_A={1,2,3}`,
`J_B={1,4,5}`,
`J_C={2,4,6}`,
`J_D={3,5,6}`.

Then exactly

`beta(J_A)=S_A={AB,AC,AD}`,
`beta(J_B)=S_B={AB,BC,BD}`,
`beta(J_C)=S_C={AC,BC,CD}`,
`beta(J_D)=S_D={AD,BD,CD}`.

Every `J_i` has size 3; every native axis occurs in exactly two `J_i`; and every pair of distinct windows intersects in exactly one axis. Hence the native observation incidence is exactly the `K4` vertex-star design.

### Finite-symmetry ambiguity

P000 supplies six native axis labels, but it does not by itself supply this `K4` star design.

On a fixed six-element labeled axis set there are exactly

`6!/|Aut(K4)| = 720/24 = 30`

distinct `K4` star-incidence structures.

The checker exhausts all 4-tuples of 3-subsets and obtains exactly `30`. Even after requiring the already visible factor slice

`I_A={1,2,3}`

to be one star, `6` distinct `K4` star atlases remain.

Therefore the FCC carrier plus a declared `beta` selects one exact observation incidence, but the incidence must not be back-propagated as a theorem that P000's six dimensions were derived from FCC.

This is the first strict-typing boundary.

---

## 6. Exact factor-slice obstruction

The existing minimal tomography model has the disjoint factor slices

`I_A={1,2,3}`,
`I_B={4,5,6}`,

so

`I_A ∩ I_B = empty`.

In the FCC `K4` star atlas, however, for distinct vertices `i != j`,

`|S_i ∩ S_j|=1`.

Therefore no two FCC `120 degree` star slices are disjoint.

Under the chosen bridge,

`beta(I_A)=S_A={AB,AC,AD}`,

while

`beta(I_B)={BC,BD,CD}=E(K4)\S_A`.

The latter is the triangle opposite vertex `A`; it is **not** any of `S_A,S_B,S_C,S_D`.

### Theorem 1 — no two-factor-slice FCC realization

For any bijection from the six native axes to the six `K4` edges, if one member of a complementary disjoint 3+3 partition maps to a star, the other member maps to the complementary triangle and cannot map to another star.

Proof: a bijection preserves disjointness, while every two distinct stars intersect in one edge. Equivalently, the complement of a `K4` vertex-star is the 3-cycle on the other three vertices, not another vertex-star. QED.

Consequently the old pair

`F_0={I_A,I_B}`

cannot itself be the four-slice FCC `120 degree` atlas.

This is not a failure of P000. It is an exact statement that the deliberately minimal two-factor tomography construction is too small to realize the new mixed-slice FCC atlas.

---

## 7. Exact rotation-lift obstruction for the old whole-factor exchange

Every physical FCC carrier atlas rotation in the frozen skeleton acts by some

`sigma in S4`

and therefore sends a vertex-star to another vertex-star:

`R_sigma(S_i)=S_{sigma(i)}`.

But the native clone-product rotation satisfies

`rho(I_A)=I_B`.

If there were a carrier rotation `R_sigma` intertwining `rho` through `beta`, then

`R_sigma(beta(I_A)) = beta(rho(I_A))`.

The left side is a star. The right side is the complementary triangle

`{BC,BD,CD}`.

Contradiction.

### Theorem 2 — clone-product rho has no FCC-S4 intertwiner

Once the established visible native slice `I_A` is read as an FCC `120 degree` star, the minimal clone-product whole-block exchange `rho` cannot be represented by any carrier `S4` atlas rotation.

The checker enumerates all 24 induced edge permutations of `S4`; none sends `S_A` to its complementary triangle.

Hence:

`C2_WHOLE_BLOCK_EXCHANGE != FCC_S4_NATIVE_LIFT`.

This closes the previously open possibility that the old `C2` tomography rotation might simply be reinterpreted as one of the new carrier rotations.

---

## 8. What survives: a strict observation atlas

The four `J_i` above solve the finite **axis/slice incidence** problem exactly.

However, in the minimal clone-product state model only

`J_A=I_A`

is already an established native three-axis Cell slice.

The mixed triples

`J_B={1,4,5}`,
`J_C={2,4,6}`,
`J_D={3,5,6}`

combine axes from the two typed factors. The prior clone-product theorem deliberately did not assert that such mixed triples are admissible native Cell slices, nor did it provide native state automorphisms realizing the carrier `S4` edge action.

Therefore I freeze the exact surviving object as:

`NATIVE_K4_STAR_OBSERVATION_ATLAS`

not

`NATIVE_K4_STAR_GEOMETRIC_SLICE_ATLAS`.

A later full state-level lift would need **additional native data**:

1. four admissible native slice structures on `J_A,J_B,J_C,J_D`;
2. slice-local identifications with the current three-positive-axis Cell geometry at the strength intended;
3. a homomorphism
   `Phi:S4 -> Aut(X_6,Adj_6)`
   inducing the six-edge action on native axis types;
4. compatibility
   `Phi_sigma(J_i)=J_{sigma(i)}`;
5. explicit overlap/chart transport.

Those requirements are not consequences of the present minimal model and are not silently assumed.

---

## 9. Chart orientation is necessarily local: a Z2 holonomy obstruction

The FCC target lines are **unoriented**. To display one star as a carrier `120 degree` triple, choose chart-local signed representatives.

Using

`v_AB=(1,1,0)`,
`v_AC=(1,0,1)`,
`v_AD=(0,1,-1)`,
`v_BC=(0,1,1)`,
`v_BD=(1,0,-1)`,
`v_CD=(1,-1,0)`,

one zero-sum local section on each chart is

`A: -AB + AC + AD = 0`,
`B:  AB - BC - BD = 0`,
`C: -AC + BC + CD = 0`,
`D:  AD - BD + CD = 0`.

For each chart the checker verifies that exactly two signed versions satisfy both zero sum and pairwise dot product `-1`; they differ by one common overall sign.

Let `s_i(e) in {+1,-1}` denote the displayed local sign. On the unique line shared by charts `i,j`, define the overlap sign

`q_ij = s_j(e)/s_i(e)`.

The exact table is

`q_AB=-1`,
`q_AC=-1`,
`q_AD=+1`,
`q_BC=-1`,
`q_BD=+1`,
`q_CD=+1`.

For every triangular loop of pairwise chart overlaps,

`q_AB q_BC q_CA = -1`,
`q_AB q_BD q_DA = -1`,
`q_AC q_CD q_DA = -1`,
`q_BC q_CD q_DB = -1`.

A chart gauge flip `s_i -> t_i s_i`, `t_i in {+1,-1}`, changes

`q_ij -> t_j q_ij t_i`

but leaves every loop product invariant.

Therefore there is no global choice of one signed representative for each of the six FCC line families that makes all four star charts simultaneously zero-sum `120 degree` triples.

Equivalently:

`GLOBAL_SIGNED_SIX_LINE_SECTION_COMPATIBLE_WITH_ALL_FOUR_120_CHARTS = NONE`.

The checker also exhausts all `2^6` global sign assignments and finds zero solutions.

This is a genuine gluing/holonomy obstruction, not an error in the atlas. The four charts have pairwise one-line overlaps but no common three-chart axis intersection, so local sign sections are allowed; what fails is only a **global trivialization** of the orientation data.

Hence the correct bridge type is

`UNORIENTED_LINE_FAMILY + CHART_LOCAL_Z2_ORIENTATION_TORSOR`.

The sign is carrier presentation state. It is not a native negative axis.

Freeze:

`CHART_SIGN != NATIVE_AXIS_SIGN`.

`CARRIER_ANTIPODE != PRIMITIVE_NATIVE_NEGATIVE_AXIS`.

---

## 10. Carrier relations cannot quotient native state

The strict bridge deliberately stops at native edge/axis type and observation-window data.

The four carrier zero-sum equations are not native vector identities. For example,

`-v_AB+v_AC+v_AD=0`

does **not** imply any native relation such as

`-E_1+E_2+E_3=0`.

Indeed the native model has six typed axis families before `beta` is declared, and `beta` returns only an **unoriented carrier line label**.

Likewise, if some later 3D carrier point readout maps two native states to the same carrier point, that equality lies in a readout fiber and does not identify the native states without a separately authorized operation-safe quotient theorem.

No such quotient is used here.

---

## 11. HCP regression: FCC specificity is exact

Reuse the accepted exact integer first-shell coordinates from the first-shell classification checker.

The deterministic regression gives:

`FCC shell antipodal pairs = 6`.

`HCP shell antipodal pairs = 3`.

Thus the FCC first shell admits an intrinsic quotient of 12 contact rays into six unoriented line families.

The HCP first shell does not: it is not centrally symmetric and only three of its 12 rays participate in antipodal pairs.

Therefore the target object of `beta` is already FCC-selected. Any attempt to manufacture six HCP pairs would require extra noncanonical choices not supplied by the local HCP shell.

Freeze:

`FCC_SIX_UNORIENTED_LINES_IS_NOT_BARLOW_UNIVERSAL`.

This is the mandatory no-overclaim regression.

---

## 12. Deterministic finite certificate

Checker:

`research_checks/P000_L1_NATIVE_FCC_CARRIER_BRIDGE_CHECK_20260829.py`

Machine certificate:

`research_artifacts/P000_L1_NATIVE_FCC_CARRIER_BRIDGE/bridge_certificate_20260829.json`

Local deterministic run:

```text
PASS
native_beta= {1: 'AB', 2: 'AC', 3: 'AD', 4: 'BC', 5: 'BD', 6: 'CD'}
native_factor_A_to_carrier= ['AB', 'AC', 'AD']
native_factor_B_to_carrier_complement= ['BC', 'BD', 'CD']
k4_star_designs_on_six_labeled_axes= 30
designs_containing_visible_I_A= 6
carrier_S4_edge_actions= 24
global_120_orientation_sections= 0
triangle_Z2_holonomy= {'ABC': -1, 'ABD': -1, 'ACD': -1, 'BCD': -1}
FCC_antipodal_pairs= 6
HCP_antipodal_pairs= 3
```

The checker uses integer/permutation arithmetic only.

---

## 13. Tool reuse resolution

Coverage verdict:

`COMPOSE_EXISTING_TOOLS`.

Matched current tools:

- `T7_FINITE_SYMMETRY_EQUIVARIANCE`;
- `T9_HOLONOMY_COCOYCLE_GLUING`;
- `T6_OPERATION_SAFE_QUOTIENT` as a semantic boundary guard.

Reuse resolution:

`COMPOSE_APPLIED`.

How applied:

- `T7` supplies the finite group-action/equivariance viewpoint: `K4` star incidence, `S4` edge action, canonical-choice ambiguity, and the exact star-versus-complement obstruction.
- `T9` supplies the staged/local chart transport versus global-trivialization distinction; the `q_ij` loop products are used exactly as a holonomy obstruction.
- `T6` is used only as a guard: the preserved observation language is declared, and no FCC readout fiber is treated as semantically disposable native information.

Hard boundaries checked:

- no canonical signed structure inferred from symmetry without data;
- nonzero holonomy diagnoses failure of global trivialization but does not invent a repaired native object;
- no carrier/readout quotient is promoted to native identity.

No new general-purpose tool family is claimed. Method harvest recommendation:

`RESULT_ONLY`.

---

## 14. Final classification and next frontier

Terminal class:

`BRIDGE_STRICTLY_TYPED`.

Exact bridge that is now proved:

`NATIVE_AXIS_TYPE`
`-> beta`
`FCC_UNORIENTED_LINE_FAMILY`

together with the declared native `K4` observation incidence

`{J_A,J_B,J_C,J_D}`
`->`
`{S_A,S_B,S_C,S_D}`

and chart-local orientation transport.

Exact obstructions now proved:

1. the old disjoint two-factor slice family cannot realize two FCC star slices;
2. the old whole-factor exchange `rho` has no intertwiner in the physical carrier `S4` atlas action;
3. no global signed six-line section realizes all four 120-degree stars simultaneously;
4. HCP cannot support the intrinsic six-line target object.

Unresolved residue:

`MIXED_NATIVE_STAR_SLICE_GEOMETRY_AND_STATE_LEVEL_S4_LIFT_NOT_PROVED`.

If Driver accepts this return, the only mathematically new continuation should be one of:

- construct the three mixed native star slices plus a state-level `S4` action satisfying the exact lift certificate; or
- prove that the current native Cell axioms obstruct such mixed slices/state automorphisms.

Do **not** redo `K4/S4`, the star/complement obstruction, or the chart-sign holonomy census.

Stop here for Driver review.
