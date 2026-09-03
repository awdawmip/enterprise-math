# Research Return — P000 S4 equivariant PF-10 / connection moduli V19

Task: `RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE`  
Publication: `TP2-E5B7C19A3D604F821583`  
Researcher: `EM-P000FCC19-A4C91E`  
Claim: `chatgpt-p000fcc19-20260831-1331-16db0a`  
Execution: `ER-4E7A91C2D6B803F15A22`  
Result: `RR-3C8A71F5D2946BE01C44`  
Status: `SUCCESS / NONTRIVIAL_PF10_AND_NONFLAT_CONNECTION_MODULI_COMMON_MODEL_CLASSIFIED`

## 0. Terminal theorem

Generation 19 closes

`P000_S4_EQUIVARIANT_PF10_CONNECTION_MODULI_AND_COMMON_NONDEGENERATE_MODEL_EXACTLY_CLASSIFIED`.

The exact terminal class is

`NONTRIVIAL_PF10_AND_NONFLAT_CONNECTION_MODULI_COMMON_MODEL_CLASSIFIED`.

On the frozen K4/tetra visible structural model, with the six channel labels

`E1=AB, E2=AC, E3=AD, E4=BC, E5=BD, E6=CD`, 

and with independent edge transport frozen to the finite typed universe

`Sym({E1,...,E6}) = S6`, 

the transparent moduli are nondegenerate in both sectors:

1. PF-10 global `S4`-equivariant families are in bijection with a **12-parameter base-Cell orbit datum**: `2` parameters for `I_A`, `2` for `O_A`, and `8` for `M_A`.
2. Independent inverse-consistent `S4`-equivariant connections have exactly **12 raw standard-presentation solutions**.
3. Under the accepted Gen10 local presentation gauge `T_xy' = g_y T_xy g_x^-1`, those 12 raw solutions form exactly **8 gauge classes**.
4. Exactly **1** gauge class is flat; exactly **7** gauge classes are nonflat.
5. The Gen18 edge-to-opposite transposition connection is retained as one of those seven nonflat classes.
6. A single common Full-Cell witness simultaneously carries a Cell-to-Cell nonconstant equivariant PF-10 family and that nonidentity/nonflat independent connection, while satisfying both Gen17 charged transparency gates and the enriched relations `R_a^3=R_b^2=(R_aR_b)^4=id`.

Therefore the transparency gates force neither pointwise-constant PF-10 content nor gauge-trivial connection content.

## 1. Frozen boundary and transport universe

Preserved without modification:

- P000 root ontology and `REALITY_DIMENSION=7`, spatial `6`, time `1`;
- accepted FCC/tetra carrier action `S4` with `a=(BCD)`, `b=(AB)`;
- `a^3=b^2=(ab)^4=1`;
- Gen17 `PF10_STRUCTURAL_AUT_EQ` and `CONNECTION_STRUCTURAL_AUT_EQ` as two independently charged semantic gates;
- Gen18 full-lift-fiber generator criterion;
- `NO_KERNEL_QUOTIENT`;
- `CARRIER_S4 != COMPLETE_NATIVE_P000_ROTATION_GROUP`;
- `TIME_FIXED`.

The independent connection transport universe used here is **finite and typed**:

`T_xy in Sym(C_x,C_y)`, and in a fixed presentation `T_xy in S6`.

No continuous `SO(6)` transport is assumed or smuggled in.

The accepted gauge law from Gen10 is

`T_xy' = g_y T_xy g_x^-1`, with `g_x in S6`,

and loop holonomy transforms by root conjugation:

`Hol_x' = g_x Hol_x g_x^-1`.

This gauge changes local channel presentation only. It does not move opaque native Cell identity, named native axes, time, adjacency, or P000 dimension.

## 2. PF-10 equivariant moduli

### Theorem 2.1 — base stabilizer orbit classification

Take base Cell `A`. Its carrier stabilizer is

`H_A=Stab_S4(A) ~= S3`, 

acting on the six tetrahedral edge channels.

The channel orbit partition is exactly

- `STAR_A={E1,E2,E3}={AB,AC,AD}`;
- `FACE_A={E4,E5,E6}={BC,BD,CD}`.

Hence an `H_A`-fixed vector has exactly two independent entries. Therefore:

- `I_A` has `2` parameters;
- `O_A` has `2` parameters.

On ordered channel pairs, `H_A` has exactly eight orbits:

1. `STAR -> STAR`, diagonal, size `3`;
2. `STAR -> STAR`, distinct, size `6`;
3. `STAR -> FACE`, adjacent/share the non-A endpoint, size `6`;
4. `STAR -> FACE`, opposite/disjoint, size `3`;
5. `FACE -> STAR`, adjacent/share the non-A endpoint, size `6`;
6. `FACE -> STAR`, opposite/disjoint, size `3`;
7. `FACE -> FACE`, diagonal, size `3`;
8. `FACE -> FACE`, distinct, size `6`.

Therefore an `H_A`-fixed ordered `6x6` passage matrix `M_A` has exactly `8` orbit parameters.

The base profile moduli in a fixed presentation is thus

`Fix_HA(P_A) ~= D^2 x D^2 x D^8 ~= D^12`,

where `D` denotes the allowed PF-10 scalar/count value domain.

This reproduces the required regressions:

- full local `S4` vector orbits = `1`;
- full local `S4` ordered-pair orbits = `3`;
- base tetra Cell stabilizer vector orbits = `2`;
- base tetra Cell stabilizer ordered-pair orbits = `8`.

### Theorem 2.2 — complete global reconstruction

For an `H_A`-fixed base profile `P_A=(I_A,O_A,M_A)`, define

`P_{gA}=rho(g) P_A`.

This is well-defined: if `gA=g'A`, then `g'^{-1}g in H_A`, which fixes `P_A`.

Conversely, every global `S4`-equivariant PF-10 family restricts at `A` to an `H_A`-fixed profile. Restriction to `A` and structural transport are inverse constructions.

Hence the `12` base orbit parameters are **complete and nonredundant** in the fixed presentation; they are not merely a lower bound.

### Corollary 2.3 — transparency does not force pointwise constancy

Take, for example,

- `I_A=1` on `STAR_A`, `2` on `FACE_A`;
- `O_A=3` on `STAR_A`, `4` on `FACE_A`;
- assign eight distinct allowed values to the eight ordered-pair orbits of `M_A`.

Transport this profile to `B,C,D` by the structural `S4` action. The four Cell profiles are pairwise different as raw labeled tensors, yet the family is exactly native-carrier equivariant.

Thus

`PF10_STRUCTURAL_AUT_EQ => POINTWISE_CONSTANT_PF10`

is false.

## 3. Independent connection: exact raw solution set

Choose representative oriented Cell edge `A->B` and write `T=T_AB in S6`.

The oriented-edge stabilizer is

`H_AB^+ = Stab_S4(A,B) = <(CD)> ~= C2`.

Its channel action is

`rho((CD))=(E2 E3)(E4 E5)`.

Well-defined structural transport of `T` to every other oriented edge requires

`T rho((CD)) = rho((CD)) T`.

The orientation reverser `b=(AB)` has channel action

`rho(b)=(E2 E4)(E3 E5)`.

Combining `S4` naturality with the reverse-edge law `T_BA=T_AB^-1` gives the second exact local condition

`rho(b) T rho(b)^-1 = T^-1`.

### Theorem 3.1 — representative-edge classification

Inside the full finite universe `S6`, the two conditions above have exactly **12** solutions:

- `id`;
- `(E1 E6)`;
- `(E2 E3)(E4 E5)`;
- `(E2 E4)(E3 E5)`;
- `(E2 E5)(E3 E4)`;
- `(E1 E6)(E2 E3)(E4 E5)`;
- `(E1 E6)(E2 E4)(E3 E5)`;
- `(E1 E6)(E2 E5)(E3 E4)`;
- `(E2 E4 E3 E5)`;
- `(E2 E5 E3 E4)`;
- `(E1 E6)(E2 E4 E3 E5)`;
- `(E1 E6)(E2 E5 E3 E4)`.

Thus raw standard-presentation count is

`12 = 1 identity + 11 nonidentity`.

### Theorem 3.2 — unique global generation

For any one of those twelve `T`, define

`T_{gA,gB}=rho(g) T rho(g)^-1`.

The oriented-edge stabilizer condition makes this independent of the choice of `g`; the orientation-reversal equation makes it inverse-consistent. Conversely every inverse-consistent `S4`-equivariant connection restricts to a representative `T_AB` obeying those same two equations.

Therefore the twelve-element list is the **complete** raw `S4`-equivariant connection solution set in the frozen `S6` transport universe.

For the visible kernel-free K4 witness `G0=S4`, the Gen18 full-lift fibers of `a,b` are singletons, so ordinary `a,b` naturality is exactly the full-fiber test in this witness. This statement is witness-local only and is not a kernel quotient.

## 4. Gauge quotient: exactly eight classes

K4 is connected and has cycle rank `6-4+1=3`. Choose root `A`, spanning tree

`{AB,AC,AD}`,

and rooted cycle basis

- `gamma_1=A-B-C-A`;
- `gamma_2=A-B-D-A`;
- `gamma_3=A-C-D-A`.

Under arbitrary accepted local `S6` presentation gauge, the tree transports can be gauged to identity. The remaining connection information is exactly the rooted holonomy triple

`(Hol_A(gamma_1),Hol_A(gamma_2),Hol_A(gamma_3))`,

modulo simultaneous conjugation by the residual root gauge `g_A in S6`.

Hence simultaneous `S6` conjugacy of this triple is a complete gauge invariant for connections on the connected K4 graph.

Exact enumeration of the twelve raw equivariant solutions gives **8 gauge classes**:

| class representative `T_AB` | raw members in standard equivariant presentation | triangle-basis conjugacy type | Hamiltonian 4-cycle type | sector |
|---|---|---|---|---|
| `id` | `id`, `(E2 E5)(E3 E4)` | `1^6` | `1^6` | flat |
| `(E1 E6)` | `(E1 E6)`, `(E1 E6)(E2 E5)(E3 E4)` | `2^3` | `1^6` | nonflat |
| `(E1 E6)(E2 E3)(E4 E5)` | singleton | `2^3` | `3^2` | nonflat |
| `(E1 E6)(E2 E4)(E3 E5)` | singleton | `4·1^2` | `3^2` | nonflat |
| `(E2 E3)(E4 E5)` | singleton | `4·2` | `3^2` | nonflat |
| `(E2 E4 E3 E5)` | it and its inverse `(E2 E5 E3 E4)` | `2·1^4` | `3·1^3` | nonflat |
| `(E2 E4)(E3 E5)` | singleton | `2^2·1^2` | `3^2` | nonflat |
| `(E1 E6)(E2 E4 E3 E5)` | it and its inverse `(E1 E6)(E2 E5 E3 E4)` | `5·1` | `5·1` | nonflat |

Consequently:

`CONNECTION_GAUGE_CLASSES=8`,

`FLAT_GAUGE_CLASSES=1`,

`NONFLAT_GAUGE_CLASSES=7`.

The nonidentity flat raw solution is gauge-equivalent to identity, exactly as the Gen10 flat-frame reconstruction theorem requires. All seven other gauge classes contain nontrivial cycle holonomy and cannot be gauge-equivalent to identity.

This answers the Gen19 degeneracy question sharply: nonflat equivariant connection content is not one accidental witness but a seven-class finite family in the frozen universe.

## 5. Holonomy classification and Gen18 mandatory regression

For the Gen18 witness take

`T_AB=(E1 E6)`.

Global structural transport assigns each undirected Cell edge `e` the transposition swapping channel `e` with its unique opposite tetrahedral edge.

For all three rooted triangle basis loops,

`Hol = J=(E1 E6)(E2 E5)(E3 E4)`,

of cycle type `2^3`.

For the three Hamiltonian K4 four-cycles the holonomy is identity.

Thus the witness is exactly:

- inverse-consistent;
- fully `S4`-equivariant;
- nonflat;
- in a nonidentity gauge class.

It realizes one of the seven nonflat classes above, so the Gen18 positive regression is retained strictly rather than merely reasserted.

The other six nonflat gauge classes realize triangle holonomy types

`2^3`, `4·1^2`, `4·2`, `2·1^4`, `2^2·1^2`, and `5·1`,

with the paired Hamiltonian-cycle types shown in the table. Full `S4` naturality transports these loop holonomies by conjugation, exactly matching the accepted holonomy covariance law.

## 6. One common non-degenerate Full-Cell model

Use the nonconstant PF-10 family of Section 2 with twelve visibly separated base orbit values, structurally transported from Cell `A`.

In the **same** K4/tetra Full-Cell model, retain the independent connection generated by

`T_AB=(E1 E6)`.

Then simultaneously:

- the PF-10 family is Cell-to-Cell nonconstant;
- `PF10_STRUCTURAL_AUT_EQ` holds;
- the independent connection is nonidentity;
- `CONNECTION_STRUCTURAL_AUT_EQ` holds;
- triangle holonomy is `J != id`, so the connection is nonflat;
- the connection is not frame-induced from one globally parallel frame field;
- neither background shrinks the visible structural `S4` group.

Because the same structural `S4` action preserves every retained datum, the enriched maps `R_a,R_b` are the structural action maps restricted to the enriched model. The exact finite checker verifies on Cells, channels, PF-10 tensors and all oriented connection edges that

`R_a^3=id`,

`R_b^2=id`,

`(R_a R_b)^4=id`.

This is a single model, not a splice of separate PF-10 and connection witnesses.

## 7. Hidden-kernel / full-lift-fiber boundary

The carrier-level moduli classification above is performed in the explicit faithful visible tetra witness, where `G0=S4` and the readout kernel is trivial.

It does **not** authorize the inference that a general hidden-kernel structural model can be checked on one chosen lift pair.

The checker re-runs the Gen18 exact regression

`G0=C2 x S4`:

- chosen lifts `(0,a),(0,b)` generate only order `24`;
- the full `a,b` lift fibers generate all order `48`.

Therefore, in any accepted model with hidden kernel, the PF-10 and connection data must still be transparent under the **full** Gen18 lift fibers. The twelve carrier-level connection representatives do not quotient or discard kernel action.

Freeze:

`VISIBLE_CARRIER_MODULI_CLASSIFICATION != HIDDEN_KERNEL_QUOTIENT`.

## 8. Degeneracy questions — exact answers

### PF-10

`TRANSPARENCY_FORCES_POINTWISE_CONSTANT_PF10 = FALSE`.

The exact fixed-presentation carrier moduli has twelve base orbit parameters, and explicit transported families are raw Cell-to-Cell nonconstant.

### Independent connection

`TRANSPARENCY_FORCES_CONNECTION_GAUGE_EQ_IDENTITY = FALSE`.

There are eight gauge classes, seven of them nonflat.

### Gen18 witness uniqueness

`GEN18_NONFLAT_EQUIVARIANT_CONNECTION_IS_UNIQUE_ACCIDENT = FALSE`.

Its class is one of seven nonflat gauge classes in the exact `S6` transport universe.

## 9. Verification

Deterministic checker:

`research_checks/P000_S4_EQUIVARIANT_PF10_CONNECTION_MODULI_V19_CHECK_20260831.py`.

It exhaustively verifies:

- carrier `S4` order `24` and frozen generator relations;
- K4/P4 automorphism regressions `24/2`;
- full-`S4` and base-stabilizer PF-10 orbit counts `1/3` and `2/8`;
- complete twelve-parameter PF-10 reconstruction and a four-profile nonconstant witness;
- all `720` channel permutations for representative-edge connection constraints;
- exact twelve raw equivariant connection solutions;
- reverse-edge consistency and full `S4` naturality for every raw solution;
- gauge quotient by rooted holonomy triple simultaneous conjugacy, yielding exactly eight classes;
- exactly one flat and seven nonflat gauge classes;
- Gen18 edge-to-opposite transposition regression;
- Gen18 `C2 x S4` chosen-lift `24` versus full-fiber `48` hidden-kernel guard;
- the common PF-10 + nonflat connection enriched witness;
- enriched `a^3,b^2,(ab)^4` relations.

Frozen certificate:

`research_artifacts/P000_S4_EQUIVARIANT_PF10_CONNECTION_MODULI_V19/MODULI_CERTIFICATE.json`.

Checker terminal output:

`PASS P000_S4_EQUIVARIANT_PF10_CONNECTION_MODULI_V19_CHECK`.

## 10. Disposition

Hard target disposition:

`P000_S4_EQUIVARIANT_PF10_CONNECTION_MODULI_AND_COMMON_NONDEGENERATE_MODEL_EXACTLY_CLASSIFIED`.

Terminal class:

`NONTRIVIAL_PF10_AND_NONFLAT_CONNECTION_MODULI_COMMON_MODEL_CLASSIFIED`.

No P000 mutation, G15 mutation, Gen17 gate-cost reduction, carrier/native identity collapse, time rotation, kernel quotient, or `UNIQUE_SECTION` claim is made.

Driver review is still required before canonical promotion or Working Truth status.
