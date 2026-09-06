# Viète on the centered-X6/FCC atlas: K4 transposition holonomy, principal-root sign bundle, and the C24 balanced-spinor anchor

Status: `FREE_RESEARCH / EXACT CONNECTION-RELATIVE ATLAS THEOREM + S6 KINEMATIC ORIENTATION-COVER NO-GO / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Parent issue: `#1255`
Parent Viète line: `#1158`
Current source frontier consumed: `awdawmip/enterprise-math@51f46265710a3aa86e01eaa41487a439674cd184`
Checker: `experiments/viete_fcc_root_atlas_c24_20260906/check_viete_fcc_root_atlas_c24.py`
Checker source commit: `51f46265710a3aa86e01eaa41487a439674cd184`
BRC reuse: `EXTEND_EXISTING_TOOL = src/enterprise_math/euler_fcc_chirality.py`

## 1. Exact scope and why a bundle is required

The local centered-X6 OUTER microcycle already supplies a true primitive 12-Cell lift of the finite `C6 -> C12` rotation interface.  An oriented native half-turn arc on one such STAR selects the principal root/precision address

\[
\Sigma=3\varepsilon\in\mathcal P_{\rm rot},
\qquad
\varepsilon\in\{+1,-1\},
\]

with finite readouts

\[
[3\varepsilon]_{6\cdot2^m}.
\]

The unresolved atlas question is whether the sign `epsilon` can be chosen as one ordinary global scalar on all physical FCC STAR slices.

BRC observer discipline is essential here.  The coarse base observer records only the STAR label.  The future-operation horizon includes:

- change of STAR chart by an allowed axis-permutation transport;
- sweep reversal;
- the C12 signed quarter-root readout;
- the C24 balanced-spinor readout;
- all finite principal `+/-3` precision readouts.

Therefore a STAR-base quotient is safe only if these future outputs are constant on every discarded chirality fiber.  They are not.  The missing bit is a genuine predictive provenance coordinate.

## 2. K4 edge realization of the four physical FCC STARs

Label the six current FCC/native axis lines by the six edges of an abstract tetrahedron `K4`:

\[
E_{01},E_{02},E_{03},E_{12},E_{13},E_{23}.
\]

The four physical close-packed STARs are

\[
S_i=\{E_{ij}:j\ne i\},
\qquad i\in\{0,1,2,3\}.
\]

This is exactly the established `S4 < S6` six-edge action.

Choose an orientation of the abstract tetrahedron

\[
[0,1,2,3].
\]

Give STAR `S_i` the cyclic orientation induced by the oriented boundary face opposite `i`:

\[
o_i=(-1)^i[0,\ldots,\widehat{i},\ldots,3],
\]

with each remaining vertex `j` represented in the STAR by the incident axis `E_ij`.

Changing the global tetrahedron orientation reverses all four local STAR frames simultaneously.  Hence it is only one global gauge flip.

## 3. Natural K4 transposition atlas connection

For every distinct `i,j`, define

\[
T_{ij}:=(ij)\in S_4<S_6,
\]

acting on the six native/FCC axis labels by the induced action on K4 edges.

This is an explicit allowed axis-permutation automorphism of the current signed-X6 coordinate skeleton.  It preserves:

- signed primitive adjacency;
- the component norm `sum x_e^2`;
- K4 edge incidence;
- the OUTER Cell construction by linear transport of `a+b`.

It has the exact STAR behavior

\[
T_{ij}(S_i)=S_j,
\]

fixes the common axis

\[
T_{ij}(E_{ij})=E_{ij},
\]

and for every third vertex `k`

\[
T_{ij}(E_{ik})=E_{jk}.
\]

Thus it is the natural common-third-vertex identification of two overlapping STAR charts.

### Scope boundary

This note does **not** claim that current P000 uniquely selects `T_ij` as the one actual native rotation law.  It proves an exact theorem for this explicit admissible `S4<S6` atlas connection.  Bare FCC incidence and current P000 rotation underdetermination still permit the logical possibility of another connection/law.

Freeze:

`K4_TRANSPOSITION_CONNECTION = EXPLICIT_ADMISSIBLE_AXIS_PERMUTATION_CONNECTION`.

`K4_TRANSPOSITION_CONNECTION != UNIQUE_P000_ACTUAL_ROTATION_LAW`.

## 4. Theorem: every natural STAR transition reverses local chirality

For every `i != j`,

\[
\boxed{T_{ij}(o_i)=-o_j.}
\]

A short proof uses oriented boundaries.  The transposition `(ij)` is odd, so it reverses the orientation of the tetrahedron.  Boundary commutes with permutation, and `(ij)` carries the face opposite `i` to the face opposite `j`.  Therefore the induced orientation on the target face/STAR acquires exactly one minus sign.

Hence all six transition bits are

\[
\boxed{e_{ij}=1.}
\]

The natural K4 transposition connection is therefore the all-negative edge representative.

Its four triangular face holonomies are

\[
\boxed{h=1111.}
\]

This recovers the existing Euler antibalanced class by direct connection construction rather than taking the six negative overlap signs as an unexplained input.

Global reversal of the original tetrahedron orientation changes every local frame at once and leaves the all-negative edge cochain unchanged modulo the global gauge kernel.

## 5. Stronger theorem: triangle holonomy is an actual X6 axis permutation

For distinct `i,j,k`, follow the atlas loop

\[
i\to j\to k\to i.
\]

The actual coordinate automorphism is

\[
H_{ijk}
=T_{ki}T_{jk}T_{ij}.
\]

Direct permutation multiplication gives

\[
\boxed{H_{ijk}=(jk).}
\]

This transposition fixes the starting STAR `S_i` as a set but swaps two of its visible axes.  Therefore it reverses its cyclic orientation:

\[
H_{ijk}(o_i)=-o_i.
\]

Thus the face holonomy `-1` is not merely an abstract sign decoration.  Under this connection it is realized by an explicit member of the current `S4<S6` axis-permutation skeleton.

Freeze:

\[
\boxed{
\text{K4 TRIANGLE HOLONOMY}
=\text{VISIBLE-AXIS TRANSPOSITION}
\Longrightarrow
\text{LOCAL SWEEP REVERSAL}.
}
\]

## 6. The Viète principal-root sign is the same local system as Euler chirality

Let one local STAR frame carry a signed Euler generator `J_i` with

\[
J_i^2=-1.
\]

Use the already classified transition law

\[
J_j=(-1)^{e_{ij}}J_i.
\]

For the oriented Viète half-turn root, let

\[
r_i=3\varepsilon_i,
\qquad
\varepsilon_i\in\{+1,-1\}.
\]

A chart transition which reverses the STAR cyclic orientation also reverses the local sweep coordinate.  Therefore

\[
\boxed{
\varepsilon_j=(-1)^{e_{ij}}\varepsilon_i
}
\]

and hence

\[
\boxed{
r_j=(-1)^{e_{ij}}r_i.}
\]

This is exactly the same `F2` edge cochain as for `J`.

Therefore the two apparently separate binary objects are not independent:

\[
\boxed{
\text{VIETE PRINCIPAL ROOT-SIGN LOCAL SYSTEM}
\cong
\text{EULER SLICE-CHIRALITY LOCAL SYSTEM}.
}
\]

In line-bundle language both are local coordinates in the same sign local system `L`.

### Exact globalizability criterion

A scalar choice of the four signs `epsilon_i` satisfying every overlap exists iff the edge system is flat, equivalently iff all face holonomies vanish.

The exhaustive finite system has:

- 8 flat edge assignments, each with exactly 2 compatible global sign choices;
- 56 nonflat assignments, each with no compatible base-slice scalar sign choice.

For the natural all-negative connection, no global signed `+3` or `-3` scalar exists downstairs on the four STAR labels.

## 7. The minimal global signed carrier is the existing cube orientation cover

The all-negative system has signed states

\[
(i,\sigma),
\qquad
\sigma\in\mathbf F_2,
\]

with transition

\[
(i,\sigma)\longrightarrow(j,\sigma+1)
\qquad(i\ne j).
\]

The existing Euler theorem identifies this eight-state cover exactly with the cube `Q3`.

On this same cover define the Viète principal root coordinate

\[
\boxed{
\widetilde\Sigma(i,\sigma)
=3(-1)^\sigma.
}
\]

The deck involution sends

\[
\widetilde\Sigma\mapsto-\widetilde\Sigma.
\]

Hence the Euler cube is simultaneously the atlas carrier on which the signed Viète principal-root coordinate becomes globally single valued.

This yields the stronger identification

\[
\boxed{
\text{EULER CHIRALITY CUBE}
=\text{VIETE PRINCIPAL-ROOT SIGN BUNDLE ATLAS}
}
\]

at the declared four-STAR connection strength.

## 8. BRC matched-fiber witness and minimality by future-operation horizon

Discard the sheet and retain only the STAR label `i`.

The two cover states

\[
(i,0),\qquad(i,1)
\]

lie in one base observer fiber.

At the coarse C6 readout,

\[
[3]_6=[-3]_6,
\]

so the two states remain observationally identical.

But already at C12,

\[
[3]_{12}\ne[-3]_{12},
\]

and therefore every finer principal level also separates them.

Thus:

\[
\boxed{
\text{C6-ONLY HORIZON}:\text{ sheet may be discarded};
}
\]

whereas

\[
\boxed{
\text{ANY HORIZON CONTAINING C12+ SIGNED ROOT READOUT}:\text{ one C2 sheet is necessary}.
}
\]

It is also sufficient for the principal `+/-3` lineage because all finer signs are determined by the same sheet.

This is the exact BRC predictive-provenance residual for the four-STAR principal-root atlas.

`REUSE_APPLIED = EXISTING EULER K4 HOLONOMY/CUBE TOOL`.

`COMPOSE_APPLIED = LOCAL NATIVE OUTER C12 ROOT SECTION + EULER CHIRALITY LOCAL SYSTEM`.

`POSITIVE_WEIGHTED_BRC = NOT THE RELEVANT REDUCTION FOR THE SIGNED ATLAS GLUING`.

## 9. Holonomy cancellation: the physical C12 character descends

Although `epsilon_i` and `J_i` each twist, their product does not.

Define

\[
K_i:=\varepsilon_iJ_i.
\]

Across an overlap,

\[
\begin{aligned}
K_j
&=\varepsilon_jJ_j\\
&=(-1)^{e_{ij}}\varepsilon_i\,
  (-1)^{e_{ij}}J_i\\
&=K_i.
\end{aligned}
\]

Therefore

\[
\boxed{K=\varepsilon J\text{ IS SINGLE VALUED ON THE FOUR-STAR BASE}.}
\]

This is the precise cancellation mechanism: the root-sign line and the Euler-chirality line are the same `C2` local system, so their tensor product is trivial.

The C12 physical quarter-root character is therefore atlas-compatible even though neither local sign coordinate is globally trivializable on its own.

## 10. C24 balanced spinor is the second typed anchor and needs no new atlas bit

The existing native spinor theorem gives the distinguished C24 root in one local frame as

\[
U_{2,i}
=\frac{1+\varepsilon_iJ_i}{\sqrt2}
=\frac{1+K_i}{\sqrt2}.
\]

Because `K_i` is atlas-independent,

\[
\boxed{U_{2,j}=U_{2,i}}
\]

under the natural overlap transport.

Also

\[
U_{2,i}^2=K_i.
\]

Sweep reversal inside a fixed STAR changes `epsilon -> -epsilon`, hence `K -> -K` and

\[
\boxed{
U_2(-\varepsilon)=U_2(\varepsilon)^{-1}
}
\]

because

\[
\frac{1+K}{\sqrt2}\frac{1-K}{\sqrt2}=1
\qquad(K^2=-1).
\]

Therefore C24 introduces no additional atlas topology or binary memory:

\[
\boxed{
\text{C24 BALANCED-SPINOR GLUING OBSTRUCTION}
=\text{THE SAME C2 CHIRALITY SHEET ALREADY PRESENT AT C12}.
}
\]

This closes the requested second typed anchor:

```text
C6  : half-turn endpoint; chirality hidden
C12 : actual OUTER Cell/gate quarter-root; chirality sheet becomes visible
C24 : balanced native component spinor; same sheet, no new atlas bit
C48+: principal precision observer; no rational/integer two-component spinor
```

## 11. The same sheet controls every principal precision level

At level `m`, let

\[
N_m=6\cdot2^m.
\]

On the orientation cover define

\[
R_m(i,\sigma)
=[3(-1)^\sigma]_{N_m}.
\]

Then

\[
\operatorname{ord}(R_m)=2^{m+1},
\]

and standard precision collapse preserves the same signed residue lineage.

At `m=0` the two sheets coincide because `3=-3 mod 6`.  For every `m>=1` they are distinct.

Negation commutes with the root/refinement relations.  Hence no new binary atlas coordinate appears at any deeper principal precision level:

\[
\boxed{
\text{ONE ORIENTATION SHEET CONTROLS THE ENTIRE PRINCIPAL }+/-3\text{ ROOT LINEAGE}.
}
\]

This is not a claim that every generic point of `P_rot` has only one bit.  It applies to the previously selected principal two-point family `+/-3`.

## 12. Full 20-slice S6 kinematic orientation cover

The current signed-X6 axis-permutation skeleton acts on all

\[
\binom63=20
\]

three-axis selections.

Define the oriented-slice carrier

\[
\Omega_{20}
=\{(S,o):|S|=3,\ o\text{ is one of the two cyclic orientations of }S\}.
\]

Then

\[
\boxed{|\Omega_{20}|=40.}
\]

The exact `S6` action is transitive.

For one underlying slice, the stabilizer is

\[
S_3^{\rm visible}\times S_3^{\rm hidden},
\]

of order

\[
36.
\]

For one oriented slice, only even visible permutations preserve the local cyclic orientation, so the stabilizer is

\[
A_3^{\rm visible}\times S_3^{\rm hidden},
\]

of order

\[
18.
\]

Orbit-stabilizer therefore gives

\[
720/18=40.
\]

### No S6-equivariant orientation section

A transposition of two visible axes fixes the underlying three-axis set but reverses its cyclic orientation.  Hence an `S6`-equivariant map choosing one of the two orientations over every one of the 20 base slices cannot exist.

Thus

\[
\boxed{
\text{FULL S6-COVARIANT SIGNED-ORIENTATION ARCHITECTURE}
\Longrightarrow
\text{AT LEAST THE 2-SHEET ORIENTATION COVER}.
}
\]

This is an exact kinematic no-go/cover theorem.

## 13. The four physical STARs sit inside the 40-state orientation cover

Restrict `Omega_20` to the four K4 STAR triples and the carrier-preserving subgroup `S4`.

The orbit contains exactly

\[
4\times2=8
\]

oriented STAR states.

Under the natural transposition connection, distinct STAR transitions change the sheet.  The resulting eight-state graph is precisely the already-proved cube orientation cover.

Therefore the cube is not a disconnected auxiliary construction: it is the physical-FCC four-STAR restriction of the natural signed orientation lift of the larger S6 slice atlas.

## 14. Critical boundary: only four slices presently have physical C12 root geometry

The 40-state `Omega_20` theorem concerns signed-X6 **kinematics and orientation provenance**.

Current physical close-packed C12 Cell/gate/OUTER microcycle geometry has only been proved for the four FCC/K4 STAR slices.

The remaining 16 native three-axis selections consist of:

- 4 K4 triangle/face triples;
- 12 K4 three-edge-path triples.

No theorem here manufactures physical C12 gates or OUTER 12-Cell root cycles on those slices.

Freeze:

\[
\boxed{
\text{20-SLICE ORIENTATION COVER GLOBALIZES KINEMATIC CHIRALITY, NOT YET PHYSICAL VIETE ROOT ANCHORS ON ALL 20 SLICES}.
}
\]

Any extension of the actual C12/C24 root section beyond the four physical STARs requires a new native/carrier realization theorem.

## 15. Relation to the original #1255 global-factorization question

The original synchronous trajectory-to-`P_rot` interpretation remains refuted by the previously proved clock-separation theorem.

The present result instead gives a strong positive global structure for the correctly retyped problem:

\[
\boxed{
\text{PHYSICAL FOUR-STAR TRAJECTORY/FRAME BASE}
\quad+\quad
\text{ONE CHIRALITY SHEET}
\quad\longrightarrow\quad
\text{PRINCIPAL VIETE ROOT PRECISION LINEAGE}.
}
\]

On the natural K4 transposition atlas connection:

1. local OUTER native C12 cycles transport exactly by `S4<S6` axis permutations;
2. the root-sign local system is the Euler chirality local system;
3. its face holonomy is the concrete visible-axis transposition holonomy `1111`;
4. the eight-state cube is the minimal signed atlas for C12+ root coordinates;
5. C24 balanced spinors glue with no new binary coordinate;
6. the same sheet controls every principal `+/-3` precision level;
7. full 20-slice S6 covariance requires an orientation cover, but physical root anchoring outside the four STARs remains open.

This is a `SUCCESS` at **connection-relative four-FCC-STAR root-bundle globalization + C24 anchor strength**, together with a `NO_GO` for an untwisted S6-equivariant global orientation section on the 20-slice base.

It is not a Foundation promotion and not a theorem that P000 uniquely selects this connection.

## 16. Smallest remaining research units

The new frontier separates into three exact problems:

1. **connection selection:** derive the natural K4 transposition connection, or an equivalent antibalanced connection, from an actual selected native rotation law rather than choosing it as an admissible axis-permutation connection;
2. **16-slice physical extension:** determine whether the 4 face triples and 12 path triples admit a native C12/C24 root anchor or only kinematic orientation state;
3. **generic precision semantics:** determine whether non-principal `P_rot` addresses have native history/process meaning or remain pure precision observers.

The principal Viète line itself now has a continuous typed provenance chain through two physical/native anchors without introducing any new atlas bit beyond chirality:

\[
\boxed{
\text{OUTER C12 NATIVE CELL MICROTRACE}
\to
\text{CUBE CHIRALITY/ROOT SHEET}
\to
\text{C24 BALANCED NATIVE SPINOR}
\to
\text{PRINCIPAL DEEP PRECISION LINEAGE}.
}
\]
