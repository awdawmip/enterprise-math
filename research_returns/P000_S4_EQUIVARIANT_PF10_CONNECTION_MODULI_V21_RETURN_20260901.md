# Research Return — P000 S4-equivariant PF10 / connection moduli V21

Task: `RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE`  
Publication: `TP2-FBDBDBE1C5BDF65F97A0`  
Researcher: `EM-P000FCC21R-8D4A2C`  
Claim: `chatgpt-p000fcc21r-20260901-1113-8d4a2c`  
Execution: `ER-E0723D1B7DC2C3F7EAA8`  
Result: `RR-3B20E8613C580F9F68D6`  
Status: `SUCCESS / NONTRIVIAL_PF10_AND_NONFLAT_CONNECTION_MODULI_COMMON_MODEL_CLASSIFIED`

## 0. Terminal theorem

Generation 21 closes the declared finite K4/tetra moduli target at the frozen Gen17/18 strength, using the typed connection value universe

`Bij({AB,AC,AD,BC,BD,CD})=S6`.

The exact result is:

1. the base-Cell `S3` stabilizer has exactly `2` channel orbits and `8` ordered-channel-pair orbits, so a framed equivariant PF10 profile has exactly `2+2+8=12` independent orbit parameters;
2. every such base profile reconstructs a unique global `S4`-equivariant PF10 family, and every global equivariant family is obtained this way;
3. the accepted pure-frame residual gauge is `C2=<omega>`, where `omega=(AB CD)(AC BD)(AD BC)` is the global opposite-edge involution;
4. for a common q-valued PF10 coefficient alphabet the framed family count is `q^12` and the frame-gauge quotient has `(q^12+q^6)/2` classes; for the exact binary regression this is `4096` framed families and `2080` gauge classes;
5. an `S4`-equivariant reverse-consistent independent connection is determined by one representative transport `t=T_AB in S6`;
6. the exact representative-edge equations leave `12` raw transports, and residual frame gauge reduces them to exactly `10` gauge classes;
7. exactly `2` raw transports / `2` gauge classes are flat, while `10` raw transports / `8` gauge classes are nonflat;
8. the Gen18 edge-to-opposite transposition connection is one of those nonflat classes and its three K4 basis-triangle holonomies are all the global opposite-edge involution;
9. a nonconstant PF10 family and that nonflat connection coexist in one and the same enriched K4/tetra Full-Cell model, with both charged Gen17 transparency gates satisfied and `R_a^3=R_b^2=(R_aR_b)^4=id` on the full enriched data.

Therefore transparency does **not** force PF10 pointwise constancy and does **not** force the independent connection to be identity/flat. The nonflat Gen18 witness is not isolated: it lies inside an exact eight-class nonflat gauge moduli.

Terminal class:

`NONTRIVIAL_PF10_AND_NONFLAT_CONNECTION_MODULI_COMMON_MODEL_CLASSIFIED`.

This is a theorem about the declared finite `S6` typed transport universe on the frozen K4/tetra structural model. It does not enlarge the connection universe to `SO(6)`, mutate P000, or identify carrier `S4` with the complete native P000 rotation group.

## 1. Frozen structural interface and the hidden-kernel issue

The Gen17 certificate freezes the per-Cell structural transport as

`Pi_x^u = f_{u(x)} rho(q0(u)) f_x^-1`,

where `q0:G0->S4` is the carrier readout and `f_x` is pure frame gauge.

Gauge-fix `f_x=id`. Then

`Pi_x^u=rho(q0(u))`.

This matters for Generation 21. For `k in K=ker(q0)`, the carrier Cell is fixed and the typed six-channel action is exactly identity. Hence **on the particular PF10 and independent-connection channel sorts used here**, kernel elements act trivially. Therefore every lift in `q0^-1(a)` has the same typed action as `a`, and every lift in `q0^-1(b)` has the same typed action as `b`.

So the visible `S4` enumeration below satisfies the accepted Gen18 **full lift-fiber** criterion without quotienting the kernel. The abstract Gen18 warning remains intact: for a different background on which `K` acts nontrivially, one chosen `a,b` lift pair would still be insufficient.

This is the exact model-specific bridge that permits the finite classification while preserving:

- `NO_KERNEL_QUOTIENT`;
- `CARRIER_S4 != COMPLETE_NATIVE_P000_ROTATION_GROUP`;
- `TIME_FIXED`;
- unchanged Gen17 gate count/cost.

## 2. PF10 equivariant moduli

Use the frozen six channels

`AB, AC, AD, BC, BD, CD`.

At base Cell `A`, `Stab(A)=S3` permutes `B,C,D`.

### 2.1 Channel orbits

There are exactly two channel orbits:

- `S = {AB,AC,AD}` — the three star edges incident to `A`;
- `F = {BC,BD,CD}` — the three opposite-face edges.

Thus each vector component `I` or `O` has two independent parameters:

`I_S, I_F` and `O_S, O_F`.

For comparison, the full local `S4` action is transitive on the six channels, hence has exactly one vector orbit.

### 2.2 Ordered-pair orbits for M

The `36` ordered pairs split under `Stab(A)` into exactly eight orbits:

1. `SS_eq`;
2. `SS_neq`;
3. `FF_eq`;
4. `FF_neq`;
5. `SF_inc`;
6. `SF_opp`;
7. `FS_inc`;
8. `FS_opp`.

The four equality/opposition classes have sizes `3,6,3,6`; the cross-orientation incident/opposite classes have sizes `6,3,6,3`.

Under full local `S4`, the same `36` ordered pairs collapse to exactly three orbit types:

- diagonal;
- distinct adjacent tetrahedral edges;
- opposite tetrahedral edges.

This re-verifies the mandatory `1/3` and `2/8` orbit regressions.

### 2.3 Exact reconstruction theorem

Let `P_A=(I_A,O_A,M_A)` be any base profile constant on the twelve orbit parameters above. For any Cell `x`, choose `g_x in S4` with `g_x(A)=x` and set

`P_x = rho(g_x) P_A`.

This is well-defined because two choices differ by `Stab(A)`, which fixes `P_A`.

Conversely, if `P` is a global equivariant family, then `P_A` is `Stab(A)`-fixed and the same formula recovers every `P_x`.

Therefore restriction to `A` gives a bijection

`PF10_framed^S4  <->  IVal^2 x OVal^2 x MVal^8`.

There is no framed duplicate.

### 2.4 Pure-frame gauge quotient

In the identity-frame slice, the residual gauge group is the centralizer of `Stab(A)` in `S6`. Exact enumeration gives

`C_{S6}(rho(Stab(A))) = {id, omega}`

with

`omega=(AB CD)(AC BD)(AD BC)`.

Its action exchanges:

- `I_S <-> I_F`;
- `O_S <-> O_F`;
- `SS_eq <-> FF_eq`;
- `SS_neq <-> FF_neq`;
- `SF_inc <-> FS_inc`;
- `SF_opp <-> FS_opp`.

Thus, for finite alphabets of sizes `q_I,q_O,q_M`, Burnside gives

`#PF10_gauge = (q_I^2 q_O^2 q_M^8 + q_I q_O q_M^4)/2`.

If all three alphabets have size `q`:

`#PF10_gauge = (q^12+q^6)/2`.

The binary exact regression is `2080`.

### 2.5 Nonconstant witness

For each Cell `x`, let

`I_x(e)=O_x(e)=1[x in e]`

and

`M_x(e,f)=1[x in e] 1[x in f]`.

This family is globally `S4`-equivariant, but the raw profile at each of `A,B,C,D` is different. In particular it is neither a pointwise constant vector family nor a single constant matrix family.

## 3. Exact connection moduli in S6

Fix the identity frame and representative oriented edge `A->B`.

Let

- `c=rho((CD))=(AC AD)(BC BD)`, the nontrivial element of the oriented-edge stabilizer;
- `s=rho((AB))=(AC BC)(AD BD)`, which maps `A->B` to `B->A`.

For `t=T_AB`, full visible equivariance is well-defined exactly when

`ct=tc`.

The reverse-edge law, combined with equivariance under `(AB)`, is exactly

`s t s^-1 = t^-1`.

These two equations are also full-lift-fiber equations in the frozen Gen17 channel representation by Section 1.

### 3.1 Structural reduction to twelve transports

`c` has cycle type `2^2 1^2`, so

`|C_{S6}(c)| = 16`.

Write

- `e=(AB CD)`;
- `d=(AC BD)(AD BC)`;
- `r=(AC BC AD BD)`.

On the four middle channels the centralizer is a `D8`. The reverse equation excludes exactly the two single transpositions `(AC AD)` and `(BC BD)` and retains

`U={id,c,s,d,r,r^-1}`.

Hence every solution is uniquely

`t=e^epsilon u`,  `epsilon in {0,1}`, `u in U`.

Therefore there are exactly `12` framed equivariant reverse-consistent connections.

Every global transport is reconstructed by

`T_{gA,gB}=rho(g) t rho(g)^-1`;

the edge-stabilizer equation makes this independent of the chosen `g`.

## 4. Gauge quotient and holonomy

After fixing the pure frames to identity, the residual gauge is again `{id,omega}`. A gauge `h_A` propagates equivariantly to every Cell and acts on the representative transport by

`t -> h_B t h_A^-1`.

Here `omega` commutes with the structural `S4`, so it acts by conjugation. It fixes the four middle elements `id,c,s,d`, and exchanges `r <-> r^-1`, independently in the `epsilon=0,1` sectors.

Thus the `12` raw solutions form exactly `10` gauge classes: eight singleton orbits and two two-element orbits.

Using the K4 cycle basis

`A-B-C-A`, `A-B-D-A`, `A-C-D-A`,

the exact gauge-class atlas is:

| class | representative `T_AB` | raw gauge-orbit size | basis holonomy cycle type | verdict |
| --- | --- | ---: | --- | --- |
| C0 | `id` | 1 | `1.1.1.1.1.1` | flat |
| C1 | `(AC AD)(BC BD)` | 1 | `4.2` | nonflat |
| C2 | `(AC BC)(AD BD)` | 1 | `2.2.1.1` | nonflat |
| C3 | `(AC BC AD BD)` | 2 | `2.1.1.1.1` | nonflat |
| C4 | `(AC BD)(AD BC)` | 1 | `1.1.1.1.1.1` | flat |
| C5 | `(AB CD)` | 1 | `2.2.2` | nonflat |
| C6 | `(AB CD)(AC AD)(BC BD)` | 1 | `2.2.2` | nonflat |
| C7 | `(AB CD)(AC BC)(AD BD)` | 1 | `4.1.1` | nonflat |
| C8 | `(AB CD)(AC BC AD BD)` | 2 | `5.1` | nonflat |
| C9 | `(AB CD)(AC BD)(AD BC)` | 1 | `2.2.2` | nonflat |

Cycle type is written as a partition of `6`; e.g. `2.2.2` means three disjoint transpositions.

Consequences:

- flat raw solutions: exactly `2`;
- nonflat raw solutions: exactly `10`;
- flat gauge classes: exactly `2`;
- nonflat gauge classes: exactly `8`.

The holonomy cycle-type distribution among the ten gauge classes is:

- `1^6`: 2 classes;
- `4+2`: 1;
- `2+2+1+1`: 1;
- `2+1+1+1+1`: 1;
- `2+2+2`: 3;
- `4+1+1`: 1;
- `5+1`: 1.

Hence holonomy conjugacy class is gauge-invariant but is **not** a complete gauge classifier: three inequivalent classes already share cycle type `2+2+2`.

## 5. Gen18 nonflat regression

Take

`t=(AB CD)`.

The reconstructed transport on every undirected Cell edge `e` is precisely the channel transposition swapping `e` with its unique opposite tetrahedral channel.

For all three basis triangles the holonomy is

`omega=(AB CD)(AC BD)(AD BC) != id`.

This exactly reproduces the Driver-accepted Gen18 nonflat fully-equivariant witness, now as one member of the complete finite moduli.

## 6. One common non-degenerate enriched model

Use simultaneously:

- the PF10 star/outer-product witness of Section 2.5;
- the connection class `C5` with `T_AB=(AB CD)`.

They live on the same four Cells, the same six channel fibres, and the same frozen structural `S4` action.

The Gen17 grammar contains no extra coupling equation forcing one retained component to alter the other; it charges their transparency independently. Exact enumeration verifies both are invariant under every visible `S4` element, and Section 1 lifts this to the full Gen18 structural lift-fiber criterion on the frozen typed channel representation.

For

`a=(BCD)`, `b=(AB)`,

the structural permutations satisfy

`a^3=b^2=(ab)^4=id`

on Cells and on all six channels. Since both retained backgrounds are equivariant, their induced action on PF10 tensors and connection transports is compatible with exactly the same group multiplication. Therefore the relations hold on the complete enriched model, not merely on labels.

This closes the common-model requirement positively.

## 7. Degeneracy verdict

All three Generation-19/21 degeneracy questions are answered:

- `PF10_STRUCTURAL_AUT_EQ` does **not** force pointwise constant PF10 content;
- `CONNECTION_STRUCTURAL_AUT_EQ` does **not** force gauge-equivalence to identity;
- nonflat equivariant connections form `8` gauge classes in this finite universe, so the Gen18 witness is not isolated.

## 8. Deterministic checker and tool reuse

Checker:

`research_checks/P000_S4_EQUIVARIANT_PF10_CONNECTION_MODULI_V21_CHECK_20260901.py`

It exactly verifies:

- `|S4|=24` and the `a,b` relations;
- mandatory `1/3` and `2/8` orbit counts;
- binary PF10 reconstruction injectivity over all `2^12=4096` framed parameter tuples;
- the `C2` residual-frame action and `2080` binary quotient classes;
- all `720` elements of `S6`;
- the `16` representative-edge centralizer candidates;
- exactly `12` reverse/equivariant transports;
- exactly `10` gauge classes;
- the `2/10` raw flat/nonflat split and `2/8` gauge-class split;
- all three K4 basis holonomies;
- exact recovery of the Gen18 opposite-edge witness;
- the common enriched PF10+nonflat-connection model;
- frozen Gen17/18 kernel, time and carrier/native guards when run in repository context.

Tool-coverage resolution:

- `T7_FINITE_SYMMETRY_EQUIVARIANCE`: `REUSE_APPLIED` for orbit/stabilizer/fixed-profile/equivariant reconstruction;
- `T9_HOLONOMY_COCOYCLE_GLUING`: `REUSE_APPLIED` for loop transport, holonomy conjugacy and flat/nonflat separation.

No new general tool family is claimed; the new code is a task-local finite certificate checker.

## 9. Frozen boundaries and review request

No claim is made that:

- `S6` is the only possible future typed connection universe;
- carrier `S4` is the complete native P000 rotation group;
- presentation/gauge data is a native spatial axis;
- the Gen17 semantic gate count/cost is reduced;
- the Gen18 chosen-lift hidden-kernel counterexample disappears in other background representations;
- this Researcher result has Working Truth/Foundation/canonical-promotion status before Driver review.

The Generation-21 hard target is closed **for the declared finite `S6` transport universe and frozen K4/tetra model**. Driver review should audit the residual-frame quotient, the model-specific kernel-triviality step, and the connection atlas before any downstream canonical use.
