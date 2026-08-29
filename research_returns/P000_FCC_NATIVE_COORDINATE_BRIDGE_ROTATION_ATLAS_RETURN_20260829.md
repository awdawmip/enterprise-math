# P000 FCC 六轴原生坐标桥与旋转换图图册 — Research Return

Status: `FROZEN RESEARCH RETURN / DRIVER REVIEW REQUIRED`

Researcher-ID: `EM-P000FCC-7B4D2A`

Task-ID: `RS-P000-FCC-NATIVE-COORDINATE-BRIDGE-ROTATION-ATLAS`

Publication-ID: `TP2-0B7E6C14F3A95D208E61`

Claim-ID: `chatgpt-p000fcc-20260829-2118-7b4d2a`

Execution branch: `research/p000-fcc-native-coordinate-bridge-rotation-atlas-em-p000fcc-7b4d2a`

Execution base: `65d1cae115e648f5154a898cd3ba83a2a2b27223`

Hard target:

`P000_FCC_NATIVE_SIX_AXIS_ROTATIONAL_COORDINATE_ATLAS_EXACTLY_CLASSIFIED_OR_OBSTRUCTED`

Terminal class:

`STRICT_PARTIAL_OR_GROUPOID_ATLAS_PROVED`

## 1. Executive result

The FCC atlas can be made exact without collapsing native six-dimensional identity, but **not as a canonical unframed map** from the current P000 primitives.

The strongest exact result is a frame-conditioned regular-covering / chart-groupoid theorem.

1. Use one explicit task-local native model
   `N=Z^6`, with `q~q±e_i` for `i=1,...,6`.
   This is an explicit P000-compatible six-dimensional discrete Cell-address model for this task. It is not promoted to the canonical full-P000 Cell identity law.

2. Choose one typed axis-to-carrier frame
   `phi_0:(E1,E2,E3,E4,E5,E6)->(L1,L3,L6,L4,L5,L2)`.
   Then the established native slice `J_A={E1,E2,E3}` maps exactly to `S_A`, while `J_B={E1,E4,E5}` maps to `S_B`. The remaining two native chart triples are forced by the FCC incidence:
   `J_C={E2,E5,E6}` and `J_D={E3,E4,E6}`.

3. The resulting carrier readout `A:Z^6->D3` is a **regular graph covering** onto the FCC nearest-neighbor lattice
   `D3={(x,y,z) in Z^3 : x+y+z even}`.
   It is locally bijective on all 12 native `±e_i` adjacency steps and globally many-to-one with exact deck group `ker(A) ~= Z^3`. Thus a carrier collision is a readout collision, never native equality.

4. The orientation-preserving integral cubic rotation group `G=SO(3,Z)` has order `24`. It acts faithfully on the six FCC line families and on the four slice charts, with line stabilizer order `4` and slice stabilizer order `6`. Relative to a chosen frame it lifts exactly to a signed monomial action on the native address lattice satisfying `A R_tilde = R A`. The lift is finite/discrete; no continuous `SO(3)` or `SO(6)` geometry is imported as native truth.

5. The four chart orientations admit an exact `±1` transition cocycle. For every `R in G` and source chart `s`,
   `R(o_s(i)v_i)=tau(R,s) o_{Rs}(pi_R(i)) v_{pi_R(i)}`
   for all three lines of the chart, with one common `tau(R,s) in {±1}`. The checker verifies all `96` chart transports and all `2304` composition identities
   `tau(R2 R1,s)=tau(R2,R1 s) tau(R1,s)`.

6. The obstruction is the missing **canonical frame**. Before an axis-line frame is supplied there are `6!=720` equally valid bijections between six named native axes and six FCC line families. Merely requiring `J_A -> S_A` leaves `36` frames; also requiring `J_B -> S_B` leaves `4`. In the maximally symmetric case, pointwise anchors leave stabilizers `720,120,24,6,2,1,1` for `k=0,...,6`, so five independent pairings plus bijectivity fix the sixth.

Therefore the task does **not** close as `FULL_TYPED_ATLAS_PROVED`. It closes at the stronger-than-obstruction but weaker-than-canonical level:

`FRAME-CONDITIONED FULL COVERING ATLAS + UNFRAMED S6-TORSOR/GROUPOID`.

This agrees with the later Gen9 full-Cell axis-handle obstruction (PR #849 / `RR-7A29C4C19E5F83B602D7`), but the finite `720` frame ambiguity and the covering/rotation theorem here are independently certified in this task's checker.

## 2. Explicit six-dimensional native model

The task explicitly requires one six-dimensional native state/adjacency object. Freeze only for this research return:

`N=Z^6`.

A native address is `q=(q1,...,q6)`.

Native adjacency is the Cayley graph relation

`Adj_6(q,q') iff q'-q in {±e1,...,±e6}`.

Hence

`L1_NATIVE(q)={q±e_i:1<=i<=6}`

has degree `12`.

The coordinate increments `+e_i` and `-e_i` are declared inside this explicit model. Their existence is **not** derived from the carrier notation `[v]={v,-v}`. Forgetting the sign gives the six named native axis channels `E_i`; sign is address-step orientation metadata.

This model is a task-local witness model compatible with the P000 root axiom. It does not assert that opaque canonical P000 Cell identity is globally equal to a `Z^6` tuple.

## 3. Exact axis-to-line frame and four native charts

Freeze the FCC carrier representatives:

- `v1=(1,1,0)`, `v2=(1,-1,0)`;
- `v3=(1,0,1)`, `v4=(1,0,-1)`;
- `v5=(0,1,1)`, `v6=(0,1,-1)`.

`L_i=[v_i]` remains an unoriented **carrier** line.

Choose the task-local frame

`phi_0: E1->L1, E2->L3, E3->L6, E4->L4, E5->L5, E6->L2`.

Then the four native chart supports are

- `J_A={E1,E2,E3} -> S_A={L1,L3,L6}`;
- `J_B={E1,E4,E5} -> S_B={L1,L4,L5}`;
- `J_C={E2,E5,E6} -> S_C={L3,L5,L2}`;
- `J_D={E3,E4,E6} -> S_D={L6,L4,L2}`.

Every native axis occurs in exactly two charts. Every pair of charts overlaps in exactly one native axis:

- `A∩B=E1`;
- `A∩C=E2`;
- `A∩D=E3`;
- `B∩C=E5`;
- `B∩D=E4`;
- `C∩D=E6`.

Thus the line/slice incidence is the edge/vertex incidence of `K4`: the four charts are the four vertices and the six axis/line families are the six edges.

This replaces a disconnected two-block picture by one connected four-chart atlas.

## 4. Exact 120-degree chart orientations and overlap transitions

Use the chart-local carrier orientations

- `S_A: (+v1,-v3,-v6)`;
- `S_B: (+v1,-v4,-v5)`;
- `S_C: (+v2,-v3,+v5)`;
- `S_D: (+v2,-v4,+v6)`.

In every chart:

- each oriented vector has squared norm `2`;
- every pair has dot product `-1`;
- the three oriented vectors sum to zero.

Hence every chart is an exact equal-length `120 degree` triangular carrier chart.

The direct shared-line orientation transitions are:

| overlap | shared line | transition |
|---|---|---:|
| `A-B` | `L1` | `+1` |
| `A-C` | `L3` | `+1` |
| `A-D` | `L6` | `-1` |
| `B-C` | `L5` | `-1` |
| `B-D` | `L4` | `+1` |
| `C-D` | `L2` | `+1` |

These signs are carrier chart presentation data only. They do not create primitive native negative axes.

## 5. Carrier readout as an exact regular covering

Relative to `E1,...,E6`, the readout columns are

`W=(v1,v3,v6,v4,v5,v2)`,

so

```
A = [1 1  0  1 0  1
     1 0  1  0 1 -1
     0 1 -1 -1 1  0].
```

### 5.1 Image is exactly the FCC lattice `D3`

Every column has even coordinate sum, so `im(A) subseteq D3`.

Conversely, for `(x,y,z) in D3`, define

`alpha=(x+y-z)/2`, `beta=(x+z-y)/2`, `gamma=(y+z-x)/2`.

Parity makes these integers, and

`(x,y,z)=alpha v1 + beta v3 + gamma v5`.

Therefore `im(A)=D3`.

### 5.2 Exact kernel

For `q=(a,b,c,d,e,f)`, `Aq=0` is equivalent to

- `a+b+d+f=0`;
- `a+c+e-f=0`;
- `b-c-d+e=0`.

Taking `b,c,d` free gives

`q=(-c-d, b, c, d, -b+c+d, c-b)`.

Define the primitive chart relations

- `k_A=E1-E2-E3`;
- `k_B=E1-E4-E5`;
- `k_C=-E2+E5+E6`;
- `k_D=E3-E4+E6`.

Then

`q=-c k_A - d k_B + (c-b) k_C`,

so

`ker(A)=Z k_A direct-sum Z k_B direct-sum Z k_C ~= Z^3`.

The fourth chart relation is dependent:

`k_A-k_B-k_C+k_D=0`.

Thus every individual three-axis chart is carrier-rank `2`, but this relation is **only a readout kernel relation**. It is not a native state identity.

### 5.3 Local bijection / global collision

The 12 native adjacency increments `±e_i` map to the 12 distinct FCC nearest-neighbor rays `±W_i`.

Therefore the graph map

`A:Cay(Z^6,{±e_i})->Cay(D3,{±v_i})`

is locally bijective at every vertex. Since `A` is surjective and the fiber over every point is one coset of `K=ker(A)`, it is a regular covering with deck transformations

`q -> q+k`, `k in K`.

Exact identity boundary:

`A(q)=A(q') iff q-q' in K`,

but

`q=q' iff q-q'=0`.

So `K` classifies carrier collisions; it never quotients native identity.

## 6. Exact finite rotation action and lift

Let `G=SO(3,Z)` mean the orientation-preserving signed permutation matrices. There are exactly `24`.

Every `R in G` preserves `D3` and permutes the six unoriented line families. For fixed representatives, write uniquely

`R v_i = epsilon_R(i) v_{pi_R(i)}`, with `epsilon_R(i) in {±1}`.

The checker proves:

- `24` distinct line permutations;
- `24` distinct slice permutations;
- the action on the four slice charts is faithful and hence isomorphic to `S4`;
- each line stabilizer has order `4`;
- each slice stabilizer has order `6`.

Relative to the chosen frame, define the native-address lift

`R_tilde e_i = epsilon_R(phi_0(i)) e_{phi_0^{-1}(pi_R(phi_0(i)))}`.

Then, exactly,

`A R_tilde = R A`.

The checker verifies all `24` equivariance identities and all `24^2=576` composition identities

`R2R1_tilde = R2_tilde R1_tilde`.

It also verifies that `ker(A)` is invariant under every lifted rotation.

This is a discrete finite rotation representation on the **task-local native address model**. The signs are directed address-step data already declared by the model; they are not inferred from FCC antipodes.

## 7. Four-chart rotation groupoid and sign cocycle

For each chart `s`, let `o_s(i)` be its local orientation sign.

For every carrier rotation `R`, the line permutation sends the line set of `s` to one unique target chart `Rs`.

A stronger exact fact holds: there is one common sign `tau(R,s) in {±1}` such that for all three lines of the source chart,

`R(o_s(i)v_i)=tau(R,s) o_{Rs}(pi_R(i)) v_{pi_R(i)}`.

The checker enumerates:

- `24*4=96` chart transports;
- `48` with `tau=+1`;
- `48` with `tau=-1`.

Composition is exact:

`tau(R2R1,s)=tau(R2,R1s) tau(R1,s)`.

All `24^2*4=2304` cases pass.

Hence the four overlapping `120 degree` charts carry a finite exact transition groupoid, not merely a visual family of planes.

## 8. Canonical-frame obstruction and exact frame torsor

The above full construction depends on the choice of `phi_0`.

From the frozen task inputs alone there are six named native axes and six named FCC line families, but no theorem selects one of the `6!` bijections between them.

Therefore the unframed atlas object is not a function; it is an `S6`-torsor of frames.

Exact counts:

1. no constraint: `720` axis-line frames;
2. require only the established `J_A={E1,E2,E3}` to land on `S_A`: `3!*3!=36`;
3. also require `J_B={E1,E4,E5}` to land on `S_B`: `4`;
4. a full named frame such as `phi_0` selects one.

If `k` pointwise axis-line pairings are explicitly anchored, the residual frame ambiguity is `(6-k)!`, giving

`720,120,24,6,2,1,1`.

Thus five independent anchors plus bijectivity are sufficient in the worst symmetric case.

This is the carrier-facing analogue of the concurrent Gen9 native `AXIS_CHANNEL_FRAME(x,E,c)` obstruction. The present result does **not** assume that PR #849 is canonical authority: its own checker independently reproduces the `720` frame torsor and factorial stabilizers.

The correct typed interface is therefore:

`P000 NATIVE MODEL + AXIS/CARRIER FRAME -> FCC COVERING ATLAS`.

Without the frame:

`P000 NATIVE MODEL -> S6-GROUPOID OF POSSIBLE FCC ATLASES`.

## 9. Coordinate-continuity criterion

### Translation

For native translation by `u in Z6`,

`A(q+u)=A(q)+A(u)`.

Thus the carrier frame is basepoint-independent and needs no FCC stacking-phase state.

The only ambiguity is deck translation by `K=ker(A)`.

Carrier coordinates alone reconstruct only a coset in `Z6/K`; reconstructing a native address requires a chosen lift/initial native address.

### Rotation

Rotation transport is exact precisely when:

1. an axis-to-line frame is part of the atlas datum; and
2. the frame is transported by the signed lift `R_tilde`.

Then both the carrier and native-address diagrams commute.

Without a frame, only the induced action on the `S6`-torsor/groupoid of frames is canonical; no single named native-axis/FCC-line bridge is selected.

This is the exact coordinate-continuity boundary.

## 10. HCP mandatory regression

Retain the accepted exact HCP first-shell certificate.

The HCP shell contains `(1,1,1)` but not its antipode `(-1,-1,-1)` and is not centrally symmetric.

Therefore HCP does not supply six canonical unoriented opposite line families from its 12 contacts.

The present six-line/four-chart covering atlas is consequently:

`FCC-SELECTED / NOT BARLOW-UNIVERSAL`.

No inference

`12 carrier contacts -> 6 native axes`

is made.

## 11. Hard-target disposition

`STRICT_PARTIAL_OR_GROUPOID_ATLAS_PROVED`.

The task is closed at the strongest exact strength justified by the frozen inputs:

- a concrete six-dimensional discrete native-address witness exists;
- a chosen axis-line frame produces an exact regular covering of the FCC `D3` carrier;
- the carrier kernel is completely classified as rank `3`;
- the four `120 degree` slice charts and all overlaps are exact;
- the finite `24`-element rotation action lifts equivariantly;
- the chart transition `±1` cocycle is exact;
- carrier collisions never imply native equality;
- HCP remains a strict no-overclaim regression;
- but the frame itself is not canonically derivable, leaving an exact `S6` frame groupoid before additional native relation data are supplied.

So the correct boundary is neither “FCC is only a picture” nor “FCC is the native six-dimensional space”.

It is:

`FCC = EXACT FRAME-CONDITIONED READOUT COVERING / NOT NATIVE IDENTITY`.

## 12. Deterministic certificate

Checker:

`scripts/check_p000_fcc_native_coordinate_bridge_rotation_atlas.py`

Certificate:

`research_artifacts/P000_FCC_NATIVE_COORDINATE_BRIDGE_ROTATION_ATLAS/exact_certificate_20260829.json`

The checker uses only Python standard-library exact integer arithmetic. It verifies:

- source Git-blob pins for the frozen task/review inputs;
- six-line/four-slice incidence;
- all chart `120 degree` integer dot-product identities;
- all pairwise overlap orientation transitions;
- exact `D3` image formula;
- exact rank-3 kernel basis and chart-kernel relation;
- local 12-ray covering property;
- `720/36/4` frame-torsor counts and factorial pointwise stabilizers;
- all `24` integral carrier rotations;
- line and slice stabilizers;
- `576` signed-lift composition checks;
- `96` chart transports;
- `2304` chart cocycle identities;
- HCP failure of central symmetry.

Local execution of the mathematical core completed with all assertions passing. Source pins were independently checked against the frozen Git blobs before execution.

## 13. Method harvest

`TASK_LOCAL_METHOD_CANDIDATE_ONLY`.

Potentially reusable pattern:

`LOWER_RANK_CARRIER_READOUT = REGULAR_COVERING + DECK_KERNEL + FINITE_CHART_GROUPOID`.

No global Enterprise method/tool promotion is requested here.

## 14. Recommended Driver disposition

`ACCEPTED / NO FOUNDATION PROMOTION`.

If the Driver accepts the theorem, the next clean research split is:

1. native-relational lane: decide whether a canonical `AXIS_CHANNEL_FRAME` or equivalent axis-handle transport law should be added/derived for full P000 Cells;
2. atlas lane: with a declared frame, study higher native rotation/groupoid structures using the exact `24`-element FCC action and the rank-3 deck kernel as regressions.

Do not reopen the carrier/native identity boundary, and do not treat `Z6/K ~= D3` as a reduction of P000 dimension.
