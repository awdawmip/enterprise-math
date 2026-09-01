# Research Return — P000 S4-equivariant PF10 / connection moduli V21

Task: `RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE`  
Publication: `TP2-FBDBDBE1C5BDF65F97A0`  
Researcher: `EM-P000FCC21R-8D4A2C`  
Claim: `chatgpt-p000fcc21r-20260901-1113-8d4a2c`  
Execution: `ER-E0723D1B7DC2C3F7EAA8`  
Status: `SUCCESS / NONTRIVIAL_PF10_AND_NONFLAT_CONNECTION_MODULI_COMMON_MODEL_CLASSIFIED`

## 0. Terminal theorem

On the frozen K4/tetra structural model, with six typed channels
`AB, AC, AD, BC, BD, CD` and independent connection values in
`S6 = Bij({AB,AC,AD,BC,BD,CD})`, the Gen19/V21 target is closed exactly:

- PF10 framed equivariant moduli are `IVal^2 x OVal^2 x MVal^8` (12 orbit parameters).
- The residual pure-frame gauge is `C2=<omega>`,
  `omega=(AB CD)(AC BD)(AD BC)`.
- For a common finite coefficient alphabet of size `q`,
  PF10 gauge classes are `(q^12+q^6)/2`; the binary regression is `2080`.
- Equivariant reverse-consistent independent connections have exactly `12` framed solutions.
- Residual frame gauge gives exactly `10` connection gauge classes.
- Exactly `2` gauge classes are flat and `8` are nonflat.
- The Gen18 opposite-edge connection is one of the nonflat classes.
- One common Full-Cell model simultaneously carries a raw Cell-to-Cell nonconstant PF10 family and a nonidentity nonflat connection while preserving both charged Gen17 transparency gates and
  `R_a^3=R_b^2=(R_aR_b)^4=id`.

Hence transparency does not force PF10 pointwise constancy and does not force the independent connection to be identity or flat. The Gen18 nonflat witness belongs to an eight-class nonflat gauge moduli.

This result is only for the declared finite `S6` typed transport universe. It does not promote `S6` to a unique future connection universe, mutate P000/G15/Gen17 costs, identify carrier `S4` with the complete native P000 rotation group, or grant Working Truth/Foundation authority.

## 1. PF10 orbit classification

At base Cell `A`, `Stab(A)=S3` has two channel orbits:

- `S={AB,AC,AD}`;
- `F={BC,BD,CD}`.

Therefore `I` has parameters `I_S,I_F` and `O` has `O_S,O_F`.

The `36` ordered channel pairs for `M` split into exactly eight stabilizer orbits:

`SS_eq, SS_neq, FF_eq, FF_neq, SF_inc, SF_opp, FS_inc, FS_opp`.

Their sizes are respectively `3,6,3,6,6,3,6,3`.

Under full local `S4`, the six channels form one orbit, and ordered channel pairs have exactly three orbit types: diagonal, distinct-adjacent, and opposite. Thus the mandatory regressions are reverified:

- full local `S4`: vector orbits `1`, ordered-pair orbits `3`;
- base Cell stabilizer: vector orbits `2`, ordered-pair orbits `8`.

Any base profile constant on these 12 parameters reconstructs uniquely by
`P_x=rho(g_x)P_A` for any `g_x(A)=x`; stabilizer invariance makes this well-defined. Conversely every global equivariant PF10 family restricts to such a base profile, so the parameterization is complete and has no framed duplicates.

In the identity-frame slice the residual gauge centralizer is exactly
`{id,omega}`. Its action swaps

`I_S<->I_F`, `O_S<->O_F`,
`SS_eq<->FF_eq`, `SS_neq<->FF_neq`,
`SF_inc<->FS_inc`, `SF_opp<->FS_opp`.

Burnside therefore gives
`(q_I^2 q_O^2 q_M^8 + q_I q_O q_M^4)/2`
classes for finite alphabets of sizes `q_I,q_O,q_M`, and
`(q^12+q^6)/2` when all sizes are `q`.

A nonconstant witness is

`I_x(e)=O_x(e)=1[x in e]`,
`M_x(e,f)=1[x in e]1[x in f]`.

Its four raw Cell profiles are distinct, while the family is fully equivariant.

## 2. Connection classification

Fix representative oriented Cell edge `A->B` and let `t=T_AB`.

Set

- `c=rho((CD))=(AC AD)(BC BD)`;
- `s=rho((AB))=(AC BC)(AD BD)`.

Well-defined equivariant reconstruction and the reverse-edge law are exactly

`ct=tc`,
`s t s^-1=t^-1`.

The centralizer of `c` in `S6` has `16` elements. The reverse equation leaves exactly `12` solutions. With

`e=(AB CD)`,
`d=(AC BD)(AD BC)`,
`r=(AC BC AD BD)`,

and
`U={id,c,s,d,r,r^-1}`,
every solution is uniquely

`t=e^epsilon u`, with `epsilon in {0,1}` and `u in U`.

Global reconstruction is
`T_{gA,gB}=rho(g)t rho(g)^-1`;
the edge-stabilizer equation makes it independent of the chosen `g`.

The residual pure-frame gauge is again `C2=<omega>`. It produces ten gauge classes. Representatives and K4 basis-triangle holonomy cycle types are:

| class | representative `T_AB` | raw orbit | holonomy type | flat |
| --- | --- | ---: | --- | --- |
| C0 | `id` | 1 | `1.1.1.1.1.1` | yes |
| C1 | `(AC AD)(BC BD)` | 1 | `4.2` | no |
| C2 | `(AC BC)(AD BD)` | 1 | `2.2.1.1` | no |
| C3 | `(AC BC AD BD)` | 2 | `2.1.1.1.1` | no |
| C4 | `(AC BD)(AD BC)` | 1 | `1.1.1.1.1.1` | yes |
| C5 | `(AB CD)` | 1 | `2.2.2` | no |
| C6 | `(AB CD)(AC AD)(BC BD)` | 1 | `2.2.2` | no |
| C7 | `(AB CD)(AC BC)(AD BD)` | 1 | `4.1.1` | no |
| C8 | `(AB CD)(AC BC AD BD)` | 2 | `5.1` | no |
| C9 | `(AB CD)(AC BD)(AD BC)` | 1 | `2.2.2` | no |

Thus there are exactly `2` flat and `8` nonflat gauge classes. Holonomy conjugacy type is gauge-invariant but is not a complete classifier, since three inequivalent classes have type `2.2.2`.

For `C5`, `t=(AB CD)`. The propagated rule swaps each Cell edge channel with its unique opposite tetrahedral channel. On the cycle basis

`A-B-C-A`, `A-B-D-A`, `A-C-D-A`,

all three holonomies equal

`omega=(AB CD)(AC BD)(AD BC) != id`.

This is exactly the mandatory Gen18 nonflat-equivariant regression.

## 3. Hidden-kernel audit

Gen17 freezes structural channel transport as

`Pi_x^u=f_{u(x)} rho(q0(u)) f_x^-1`.

After identity-frame gauge fixing, `Pi_x^u=rho(q0(u))`. Hence for
`k in K=ker(q0)`, the Cell is fixed and the action on the declared six-channel PF10/connection sorts is identity.

Therefore every lift in `q0^-1(a)` or `q0^-1(b)` induces the same typed action as the visible carrier generator. The visible finite enumeration consequently satisfies the accepted Gen18 full-lift-fiber criterion on these specific background sorts without quotienting `K`.

The general Gen18 warning remains unchanged: for other backgrounds carrying a nontrivial kernel action, a chosen lift pair alone is not sufficient.

## 4. Common enriched model

Take simultaneously:

- the PF10 incidence-star / star-outer-product witness from Section 1;
- connection class `C5`, `T_AB=(AB CD)`.

They use the same four Cells, six channel fibres and frozen structural action. Both retained backgrounds are fully equivariant, and Gen17 charges their transparency independently; there is no extra coupling equation that obstructs coexistence.

For `a=(BCD)` and `b=(AB)`, exact structural action satisfies
`a^3=b^2=(ab)^4=id` on Cells and channels. Equivariance then makes the same relations hold on the complete PF10-plus-connection enriched data.

So the common-model requirement is positively closed.

## 5. Deterministic verification and tool reuse

The task-local checker is

`research_checks/P000_S4_EQUIVARIANT_PF10_CONNECTION_MODULI_V21_CHECK_20260901.py`.

Its exact enumeration covers `|S4|=24`, all `720` elements of `S6`, the mandatory `1/3` and `2/8` orbit regressions, all `4096` binary framed PF10 parameter tuples, the `2080` binary residual-gauge classes, the `16` representative-edge centralizer candidates, all `12` connection solutions, all `10` gauge classes, the `2/8` flat/nonflat split, K4 basis holonomies, the Gen18 opposite-edge witness, the common enriched model, and frozen Gen17/18 guards.

The in-chat semantic-equivalent checker source passed its exact selftest before persistence. The persisted Git blob is separately pinned; no claim is made that the persisted byte sequence itself was executed in-chat.

Tool reuse:

- `T7_FINITE_SYMMETRY_EQUIVARIANCE`: reused for orbit/stabilizer/fixed-profile/equivariant reconstruction;
- `T9_HOLONOMY_COCOYCLE_GLUING`: reused for loop transport, holonomy conjugacy and flat/nonflat separation.

No new general tool family is claimed.

## 6. Review boundary

Researcher terminal class:

`NONTRIVIAL_PF10_AND_NONFLAT_CONNECTION_MODULI_COMMON_MODEL_CLASSIFIED`.

Driver review should specifically audit the residual-frame `C2` quotient, the model-specific hidden-kernel triviality step, and the ten-class connection/holonomy atlas before any canonical downstream use.
