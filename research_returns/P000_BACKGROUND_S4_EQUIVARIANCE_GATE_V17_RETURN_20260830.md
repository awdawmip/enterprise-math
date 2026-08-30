# Research Return — P000 background S4 equivariance gate V17

Task: `RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE`  
Publication: `TP2-A7D3C18E5B904F621476`  
Researcher: `EM-P000FCC17-9419D1`  
Claim: `chatgpt-p000fcc17-20260830-2248-da447a`  
Execution: `ER-8C935F2AC71254D9BFD2`  
Result: `RR-985AEE277DE45AFCC9D8`  
Status: `SUCCESS / MULTIPLE_INDEPENDENT_BACKGROUND_LEAK_SOURCES_AND_PARETO_GATES_CLASSIFIED`

## 0. Terminal theorem

Generation 17 closes the hard target

`P000_ZERO_COST_BACKGROUND_S4_COMPATIBILITY_GATE_AND_MINIMAL_CHARGED_EQUIVARIANCE_EXTENSION_EXACTLY_CLASSIFIED`.

Accepted terminal class returned by this execution:

`MULTIPLE_INDEPENDENT_BACKGROUND_LEAK_SOURCES_AND_PARETO_GATES_CLASSIFIED`.

The Generation-15 grammar remains immutable. The Generation-16 official positive frontier is **not** reinstated as an unconditional result. Instead, this execution identifies exactly which zero-cost background components can shrink the structural `S4` readout, proves a general compatibility-intersection theorem, exhibits a second independent leak source beyond PF-10, and freezes the minimal **atomic/separable** charged background-equivariance grammar required before the structural K4/TETRA proof can be reused.

The decisive new boundary is:

- PF-10 is a genuine zero-cost symmetry leak source.
- An independently retained connection is a second, logically independent zero-cost symmetry leak source.
- Frames and frame-induced transport are gauge/derived and do not need charged symmetry conditions.
- Merely demanding `Compat_B=S4` for each background component is not enough: different components can require incompatible lifts.
- The composable charged condition is therefore **structural-automorphism transparency**, `G_B=G0`, component by component.

Conditional extended Pareto frontiers are:

1. frame-induced/no independent connection: `{K4_ADJ, PF10_STRUCTURAL_AUT_EQ}`, cost `(0,0,0,0,0,0,2,0)`;
2. independent connection declared: `{K4_ADJ, PF10_STRUCTURAL_AUT_EQ, CONNECTION_STRUCTURAL_AUT_EQ}`, cost `(0,0,0,0,0,0,3,0)`.

The corresponding TETRA packages pass but are strictly Pareto-dominated in the frozen G15 cost coordinates. `UNIQUE_SECTION` is not asserted.

## 1. Frozen input and guards

Consumed and preserved:

- P000: `REALITY_DIMENSION=7`, spatial dimension `6`, time dimension `1`;
- accepted FCC carrier `S4` with `a=(BCD)`, `b=(AB)`, `a^3=b^2=(ab)^4=1`;
- Gen13: `BARE_P000_UNIVERSAL_S4_LIFT_DERIVABLE = FALSE`;
- Gen14: `Sec(q) <-> zero-residue frozen-generator lift pairs`, canonicality `<-> Aut_prim(M)` fixed point in `Sec(q)`;
- Gen15: four relation forms, five global constraints, fixed-sort definitional equivalence, cost vector `(s,r,a1,a2,a3,h,g,p)`, finite envelope, 90 package specifications;
- Gen16 Driver boundary: official `{K4_ADJ}` frontier rejected under unconstrained zero-cost PF-10 background.

Pinned G15 grammar-certificate SHA-256:

`50ef864f0713d1f19ddf918dae2486a05a7e1d52bf538f1603b2d1c6c655281e`.

Frozen guards remain `NO_KERNEL_QUOTIENT`, `TIME_FIXED`, `CARRIER_S4 != COMPLETE_NATIVE_P000_ROTATION_GROUP`, and `G15_IMMUTABLE`.

## 2. Structural reduct and exact compatibility theorem

For a frozen G15 package `P`, let `M0(P)` be the structural reduct retaining selected G15 relations/constraints, the actual `NativeAdj` valuation, typed sorts and accepted carrier/frame typing, but before contentful PF-10 or an independent retained connection delete symmetries.

Let

`G0 = Aut_car(M0(P))`

be the carrier-compatible typed structural automorphism group, with frozen readout

`q0:G0->S4`.

For a retained global background component `B`, define

`G_B={u in G0 : u preserves B}`

and

`Compat_B=q0(G_B)`.

The actual enriched group is

`G=intersection_B G_B`, with `q=q0|G`.

### Theorem 2.1 — compatibility-intersection upper bound

`im(q)=q0(intersection_B G_B) subseteq intersection_B q0(G_B)=intersection_B Compat_B`.

Every actual enriched automorphism preserves every retained background component, so the inclusion is immediate. For a global component `B`, `G_B` is a subgroup of `G0`, hence `Compat_B` is a subgroup of `S4`.

This subgroup statement must not be applied to local source-target fibers. A set `G_{B,x->y}={u in G_B:u(x)=y}` is generally a coset/groupoid fiber rather than a subgroup. In the exact tetrahedral `S4` action, the set sending `A` to `B` has six elements and does not contain identity, while the `A` stabilizer is an order-six subgroup.

### Theorem 2.2 — the inclusion can be strict

Componentwise full compatibility does **not** guarantee a simultaneous lift.

Take `H=C2 x S4`, `q(k,g)=g`. Let

`G1={(0,g):g in S4}`

and

`G2={(sgn(g),g):g in S4}`.

Both project onto all of `S4`, but their intersection projects only onto `A4` of order 12. Therefore the gate

`FOR_EACH_B: Compat_B=S4`

is insufficient: different background components may realize the same carrier element with incompatible kernel/lift choices.

This is why Gen17 freezes the stronger separable condition

`G_B=G0`

for each independently stored contentful background family.

## 3. Exact zero-cost background inventory

| background component | classification | Gen17 charge? | exact reason |
|---|---|---|---|
| `NativeAdj` valuation | `CONTENTFUL_SYMMETRY_LEAK_SOURCE` | no new charge; structural/G15-facing | `Aut(K4)=24`, `Aut(P4)=2`; Gen13 P4 no-lift is adjacency leakage |
| per-Cell frame `f_x` | `PURE_GAUGE_PRESENTATION` | none | unique typed transport `Pi_x=f_{u(x)} rho(q0(u)) f_x^-1`; gauge change conjugates laws |
| frame-induced `T_xy=f_y f_x^-1` | `DERIVED_AUTOMATICALLY_EQUIVARIANT` | none | connection naturality is an identity |
| PF-10 `P_x=(I_x,O_x,M_x)` | `CONTENTFUL_SYMMETRY_LEAK_SOURCE` | `PF10_STRUCTURAL_AUT_EQ` | `I=O=e1,M=I6` has compatibility subgroup order 4 |
| independent retained connection | `CONTENTFUL_SYMMETRY_LEAK_SOURCE + OPTIONAL_IF_MODEL_DECLARED` | `CONNECTION_STRUCTURAL_AUT_EQ` if declared | marked-edge K4 connection has compatibility order 4 with PF-10 fully symmetric |
| star/overlap/gluing family at accepted scope | `DERIVED_AUTOMATICALLY_EQUIVARIANT` | none | retained only as transported/derived data; a pointwise named star would add forbidden parameter/cross-sort structure |

Gen15 proved `K4_ADJ` does not parameter-free define tetrahedral `Cell x AxisType` incidence on the preexisting AxisType sort. Therefore retained Gen12 star/overlap/gluing material cannot be interpreted as a universal zero-cost primitive assigning a distinguished three-axis star to every NativeCell; otherwise `I_CA` would already be definable and Gen15 D2 would be false. A named individual star frozen pointwise would be a new parameter or cross-sort relation outside the G15 `p=0` firewall.

## 4. PF-10 symmetry gate

For `u in G0`, Cell `x`, and carrier action `rho(q0(u))`, define

`Pi_x^u=f_{u(x)} rho(q0(u)) f_x^-1`.

The exact PF-10 preservation equations are

`I_{u(x)}[Pi_x^u(c)]=I_x[c]`,

`O_{u(x)}[Pi_x^u(c)]=O_x[c]`,

`M_{u(x)}[Pi_x^u(c),Pi_x^u(d)]=M_x[c,d]`.

Freeze the atomic charged template

`PF10_STRUCTURAL_AUT_EQ`

iff these equations hold for every `u in G0`. Equivalently, `G_PF10=G0`.

The condition has an independently meaningful interpretation: the PF-10 background carries no extra symmetry-breaking information beyond the structural reduct. It does not mention a desired section, a selected generator lift, a residue, or a kernel quotient.

### 4.1 Gen16 leak certificate

Using carrier edges `E1=AB, E2=AC, E3=AD, E4=BC, E5=BD, E6=CD`, set

`I=O=e1=(1,0,0,0,0,0)`, `M=I6`.

`M` is invariant under every carrier permutation, while `I,O` force `E1` to be fixed. Hence

`Compat_PF10=Stab_S4(E1)`

and exact enumeration gives order `4<24`.

### 4.2 Full local S4 invariance versus orbitwise equivariance

The carrier `S4` action on the six edges is transitive, so a pointwise fully invariant vector has one orbit parameter. On ordered edge pairs there are exactly three orbits: equal edge, distinct adjacent edges, and disjoint opposite edges. Thus every pointwise fully invariant `6x6` matrix has three orbital parameters, equivalently `M=aI+bA_adj+cA_opp`.

Orbitwise Cell-equivariance is strictly weaker. For a tetrahedral Cell orbit, a base Cell has stabilizer `S3`; its six edges split into two orbits `{E1,E2,E3}` and `{E4,E5,E6}`, so a stabilizer-fixed vector has two parameters. On ordered edge pairs that `S3` has exactly eight orbits, versus three for pointwise full `S4` invariance.

Therefore the exact transparent gate is orbitwise `G0`-equivariance, not an unnecessary requirement that every Cell carry an identical pointwise `S4`-invariant tensor.

### 4.3 Generator-only conditions

When the declared structural action is coherent and generated by frozen `a,b`, equivariance for both generators implies equivariance for the whole generated `S4`. Each generator alone is strictly insufficient:

- `(1,1,1,0,0,0)` is `a`-invariant but not `b`-invariant;
- `e1` is `b`-invariant but not `a`-invariant.

## 5. Independent connection is a second leak source

Gen11 already froze the exact distinction: frame-induced connection naturality is automatic; independent connection naturality is additional.

For an independent retained connection, structural transparency is

`T_{u(x),u(y)} Pi_x^u = Pi_y^u T_xy`

for every `u in G0` and retained oriented adjacency edge. Freeze

`CONNECTION_STRUCTURAL_AUT_EQ`

iff this law holds for every `u in G0`; equivalently `G_conn=G0`.

Along paths this gives the accepted holonomy conjugacy law

`Hol_{u(x)}(u gamma)=Pi_x^u Hol_x(gamma) (Pi_x^u)^-1`.

The correct boundary remains

`NONFLAT_CONNECTION != AUTOMATIC_ROTATION_OBSTRUCTION`.

The issue is equivariance, not flatness.

### 5.1 Exact independent connection leak countermodel

Take the symmetric K4 structural model with completely carrier-symmetric PF-10:

`I=O=(1,1,1,1,1,1)`, `M=I6`.

Use identity presentation frames. Declare an independent connection on K4:

- on Cell edge `AB`, set order-two channel transport `T_AB=(E1 E6)`;
- on every other edge use identity;
- reverse transport is inverse, hence the same permutation on `AB`.

A carrier permutation preserving this connection must preserve the uniquely nonidentity Cell edge `AB`. The stabilizer of unordered pair `{A,B}` in `S4` has order four. Every element of that stabilizer fixes `E1=AB` and `E6=CD`, so it commutes with `(E1 E6)`.

Exact enumeration gives

`Compat_conn=Stab_S4({A,B})`

with order `4`.

The PF-10 profile in the same model has compatibility order `24`, so the connection obstruction is independent of the PF-10 obstruction.

## 6. Derived versus non-derived gates

Derived/no charge:

1. frame gauge covariance;
2. typed `Pi` construction and composition induced by frames;
3. frame-induced connection naturality;
4. transported star/overlap/gluing laws at accepted derived scope.

Not derivable:

1. `PF10_STRUCTURAL_AUT_EQ` — exact countermodel `I=O=e1,M=I6`;
2. `CONNECTION_STRUCTURAL_AUT_EQ` — exact marked-edge independent connection even with PF-10 transparent.

`NativeAdj` remains part of the structural reduct. If a package does not force a full-S4 structural base, the P4 model remains available with `|Aut(P4)|=2`. Background transparency cannot enlarge a structural group already cut down by native relations. Hence `K4_ADJ` or a stronger tetrahedral structural base remains necessary.

## 7. Gen17 charged grammar and atomicity firewall

Freeze

`G17_ATOMIC_BACKGROUND_EQUIVARIANCE_GRAMMAR_V1`.

It adds exactly two possible atomic global-constraint templates to immutable G15:

1. `PF10_STRUCTURAL_AUT_EQ`;
2. `CONNECTION_STRUCTURAL_AUT_EQ`, only when an independent connection is declared.

Neither adds a sort, relation symbol, arity coordinate, hidden flag, or parameter. Each increments the existing G15 global-constraint coordinate `g` by exactly `1`.

A syntactic macro such as `ALL_BACKGROUND_S4_EQ` is normalized to the independently stored background families it constrains before cost is computed. Therefore the conjunction of the PF-10 and independent-connection gates costs two global constraints, not one. This prevents a packaging trick from hiding two independently falsifiable laws inside a synthetic single `g=1` predicate.

PF-10 `I/O/M` is one accepted local tensor family `P_x=(I,O,M)` and therefore one atomic background component.

Forbidden charged primitives remain: section predicates, chosen `R_a/R_b`, `K=1`, zero-residue flags, carrier/native identity equations, kernel quotient predicates, and named Cell/star constants.

## 8. Why transparency, not merely Compat=S4

`q0(G_B)=S4` says every carrier element has some `B`-preserving lift. The strict `C2 x S4` witness proves that two components can each satisfy this and still have no common lift for odd permutations.

`G_B=G0` says the component removes no structural lift at all. Independently transparent components therefore compose monotonically:

`intersection_B G_B = G0`.

This is the weakest gate in the frozen **separable-transparency** grammar: any weakening that permits a proper `G_B` re-opens cross-component lift incompatibility unless a new coupled multi-background condition is introduced. Conjunction packing is excluded by the atomicity rule.

## 9. Positive-gate sufficiency and extended Pareto frontiers

Once all required contentful backgrounds are structurally transparent, the actual enriched group equals `G0`. The Gen16 Driver defect is removed without changing G15.

Targeted structural regressions are reverified exactly:

`|Aut(K4)|=24`, `|Aut(P4)|=2`, and tetrahedral Cell-Axis incidence has sort-preserving automorphism group order `24`.

### 9.1 Frame-induced/no independent connection subclass

Required K4 package:

`{K4_ADJ, PF10_STRUCTURAL_AUT_EQ}`

with cost `(0,0,0,0,0,0,2,0)`.

Under PF-10 transparency and derived frame connection, the actual enriched group equals the K4 structural group. The typed structural `S4` section survives and the Gen14 `Aut_prim` section action fixes the direct-factor section.

Thus `FAITHFUL_SPLIT=TRUE` and `CANONICAL_FIXED_POINT=TRUE`.

Delete `PF10_STRUCTURAL_AUT_EQ`: the `e1` profile leaves order-four compatibility. Delete `K4_ADJ`: choose P4, structural image order two. Both conditions are deletion-essential.

### 9.2 Independent-connection subclass

Required package:

`{K4_ADJ, PF10_STRUCTURAL_AUT_EQ, CONNECTION_STRUCTURAL_AUT_EQ}`

with cost `(0,0,0,0,0,0,3,0)`.

Delete the connection gate while retaining fully symmetric PF-10: the marked-edge connection leaves compatibility order four. All three conditions are deletion-essential.

### 9.3 Tetrahedral retest

`TETRA_CA` supplies a full structural `S4`; the same background gates make the contentful decorations transparent.

Costs:

- frame-induced connection: `(0,1,0,1,0,0,2,0)`;
- independent connection: `(0,1,0,1,0,0,3,0)`.

The corresponding K4 extended package has every coordinate no larger and strictly smaller relation/binary coordinates. K4 therefore strictly Pareto-dominates TETRA in both subclasses.

### 9.4 Resulting conditional frontiers

Frame-induced/no-independent-connection models:

`FAITHFUL_FRONTIER = CANONICAL_FIXED_POINT_FRONTIER = {K4_ADJ,PF10_STRUCTURAL_AUT_EQ}`.

Independent-connection-declared models:

`FAITHFUL_FRONTIER = CANONICAL_FIXED_POINT_FRONTIER = {K4_ADJ,PF10_STRUCTURAL_AUT_EQ,CONNECTION_STRUCTURAL_AUT_EQ}`.

These are conditional successor frontiers, not a retroactive acceptance of the rejected Gen16 bare `{K4_ADJ}` theorem. `UNIQUE_SECTION_FRONTIER` remains unasserted.

## 10. Deterministic evidence

Checker:

`research_checks/P000_BACKGROUND_S4_EQUIVARIANCE_GATE_V17_CHECK_20260830.py`.

Machine certificate:

`research_artifacts/P000_BACKGROUND_S4_EQUIVARIANCE_GATE_V17/BACKGROUND_EQUIVARIANCE_CERTIFICATE.json`.

Observed task-local self-test:

```text
PASS P000_BACKGROUND_S4_EQUIVARIANCE_GATE_V17_CHECK
carrier_s4_order=24
pf10_e1_compat_order=4
pf10_symmetric_compat_order=24
local_full_s4_vector_orbits=1
local_full_s4_matrix_pair_orbits=3
tetra_cell_stabilizer_vector_orbits=2
tetra_cell_stabilizer_matrix_pair_orbits=8
connection_marked_edge_compat_order=4
frame_induced_connection_naturality=automatic
compat_projection_strict_witness_individual=24,24_joint=12
partial_fiber_A_to_B_size=6_not_subgroup=true
k4_pf10_gate_cost=(0,0,0,0,0,0,2,0)
k4_pf10_connection_gate_cost=(0,0,0,0,0,0,3,0)
terminal_class=MULTIPLE_INDEPENDENT_BACKGROUND_LEAK_SOURCES_AND_PARETO_GATES_CLASSIFIED
```

The repository checker additionally pins the G15 grammar hash; Gen12, Gen13, Gen14, Gen15 and Gen16 result regressions; the Gen16 Driver `REVISION_REQUIRED` boundary; and the V17 machine inventory/cost records.

## 11. Tool-reuse resolution

`T7_FINITE_SYMMETRY_EQUIVARIANCE`: `REUSE_APPLIED` for orbit/stabilizer/equivariant-profile and fixed-point reasoning. Its hard boundary was preserved: no canonical choice was inferred without invariant structural data.

`T9_HOLONOMY_COCOYCLE_GLUING`: `REUSE_APPLIED` for the holonomy/naturality semantic boundary. Nonzero holonomy was not treated as an automatic symmetry obstruction. The current T9 executable family is not claimed to have been executed as an S4 connection classifier; the marked-edge calculation is a task-local exact finite certificate.

No new general tool family is claimed.

## 12. Scope

This return does not assert that P000 itself has complete native rotation group `S4`, that carrier vertices are native Cells, that carrier opposite rays define primitive native negatives, that a kernel may be quotiented away, that every independent connection is flat, that flatness means trivial global holonomy, that Gen16's unconditional frontier is restored, that charged templates are root axioms, or that the section is unique.

## 13. Hard-target disposition

Hard target disposition: `SUCCESS`.

Terminal class: `MULTIPLE_INDEPENDENT_BACKGROUND_LEAK_SOURCES_AND_PARETO_GATES_CLASSIFIED`.

Exact closure achieved:

1. zero-cost background inventory;
2. global compatibility subgroup theorem and groupoid-fiber caution;
3. strict proof that componentwise `Compat_B=S4` can fail simultaneous compatibility;
4. PF-10 stabilizer and orbitwise-equivariance classification;
5. independent connection leak certificate with PF-10 symmetric;
6. derived-vs-charged classification;
7. atomic charged grammar and cost;
8. one-condition deletion certificates;
9. targeted K4/TETRA positive-gate retest;
10. conditional faithful/canonical Pareto frontier.

Recommended Driver action: review Gen17 at the exact charged-background-grammar strength above. If accepted, freeze the two model-subclass frontiers and the atomicity rule; do not mutate P000 or retroactively mark Gen16 accepted.
