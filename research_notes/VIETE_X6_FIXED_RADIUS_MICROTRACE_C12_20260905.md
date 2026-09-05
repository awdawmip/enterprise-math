# Viète in centered X6: fixed-radius no-go, BRC microtrace split, and an exact native C12 outer-Cell lift

Status: `FREE_RESEARCH / EXACT RESTRICTED DERIVATION / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Parent issue: `#1255`
Parent Viète line: `#1158`
Current Foundation rebase consumed: `main@f85daecab253228f9611c408a982d29a0865ded7`
Checker: `experiments/viete_x6_fixed_radius_c12_20260905/check_viete_x6_fixed_radius_c12.py`
Checker source commit: `3435b1a4e59b029037ee6bdb026091afc1be8d27`

## 1. Why the centered-X6 rebase changes the rotation question

The current spatial Foundation is now the signed Cell-centered torsor

\[
X_6\cong \mathbf Z^6
\]

relative to a chosen Cell anchor, with primitive coordinate adjacency

\[
x\longmapsto x\pm e_i
\]

and native squared component length

\[
L_E(x)^2=\sum_{i=1}^6x_i^2.
\]

The established FCC/K4 STAR slices are carrier/readout charts, not native identity. In one selected centered STAR slice, the six signed primitive directions project to the six nearest-neighbor carrier directions and hence supply the already-proved local `C6` phase shell. The carrier triple gates supply the already-proved local `C12` incidence refinement.

The present note asks a narrower but more native question than the earlier carrier construction:

> what does one local `C6 -> C12` rotation step look like when resolved back into current signed-X6 primitive Cell microsteps?

This is exactly where the new P000 rule

`OFF_NATIVE_AXIS_APPARENT_SEGMENT -> COMPOSITE_NATIVE_PATH`

and the BRC provenance gate become active.

## 2. Theorem: no primitive Cell step can preserve exact native radius

Let

\[
x=(x_1,\ldots,x_6)\in\mathbf Z^6
\]

and let one primitive step be

\[
s=\varepsilon e_i,
\qquad \varepsilon\in\{\pm1\}.
\]

Then

\[
\begin{aligned}
L_E(x+s)^2-L_E(x)^2
&=(x_i+\varepsilon)^2-x_i^2\\
&=2\varepsilon x_i+1.
\end{aligned}
\]

The right side is an odd integer, hence never zero.

Therefore

\[
\boxed{
L_E(x\pm e_i)^2\neq L_E(x)^2
\quad\text{for every }x\in\mathbf Z^6.
}
\]

Equivalently, for every integer shell

\[
\Sigma_N:=\{x\in\mathbf Z^6:L_E(x)^2=N\},
\]

the primitive coordinate-adjacency graph induced on `Sigma_N` has no edges.

### Consequence

A nonconstant exact fixed-radius rotation cannot simultaneously mean

1. every microtime state is a native Cell;
2. every microtime transition is one primitive signed-axis adjacency;
3. native radius is constant at every microstep.

At least one of these must be relaxed or retyped.

Under the current Foundation the natural retyping is:

\[
\boxed{
\text{fixed-radius phase motion is a macro/readout motion whose native realization is composite and radially jittering.}
}
\]

This does not forbid a radius-preserving rotation transformation such as an admitted axis permutation. It forbids interpreting such a transformation as a one-edge walk in the primitive Cell adjacency graph.

## 3. Local unit-shell C6 phase states

Fix one established STAR slice `S={i,j,k}` and pivot Cell `P`.

The six signed primitive radius-one states relative to `P` are

\[
\mathcal U_S=\{\pm e_i,\pm e_j,\pm e_k\}.
\]

Their STAR carrier readouts form the ordinary six nearest-neighbor directions of the triangular carrier. Hence one choice of chirality orders them as

\[
a_0,a_1,\ldots,a_5,
\qquad a_{r+3}=-a_r.
\]

Each adjacent pair `a_r,a_{r+1}` uses two distinct native axes.

The already-proved local C6 Cell phase identifies the Cell germ at `P+a_r` with one phase state `E_r`.

## 4. Theorem: every adjacent C6 macrostep has exactly two shortest native microtraces

Let

\[
a,b\in\mathcal U_S
\]

be adjacent in the local carrier C6 cycle.

Since they are signed unit vectors on two distinct native axes,

\[
d=b-a
\]

has exactly two nonzero components, each of absolute value one. Therefore

\[
N_{\min}(d)=2,
\qquad
L_E(d)^2=2,
\]

and the current X6 BRC shortest-path formula gives

\[
B_{\min}(d)=\frac{2!}{1!1!}=2.
\]

The two path words are exactly

\[
\boxed{a\to0\to b}
\]

and

\[
\boxed{a\to a+b\to b}.
\]

Call them respectively

- `INNER_BRANCH`: intermediate Cell is the pivot `0`;
- `OUTER_BRANCH`: intermediate Cell is `a+b`.

Their intermediate native radii are

\[
L_E(0)^2=0,
\qquad
L_E(a+b)^2=2.
\]

Thus the coarse phase motion

\[
1\to1
\]

in radius has two shortest native microrealizations

\[
1\to0\to1
\]

and

\[
1\to\sqrt2\to1.
\]

This is an exact native meaning of radial `jitter/multipath` for the first nontrivial local rotation step.

### BRC status

This is a genuine branch population, so BRC is no longer merely a quotient warning:

`REUSE_EXECUTED = X6 N-BRC SHORTEST-PATH MULTIPLICITY`.

`BRANCH_COUNT = 2`.

`BRANCH_PROVENANCE = INNER_VS_OUTER`.

The two branches have identical macro endpoints and therefore cannot be reconstructed from the endpoint pair alone.

## 5. Theorem: the outer intermediate Cell is the exact C12 half-angle ray

Let the two adjacent carrier unit rays corresponding to `a,b` be

\[
u,v,
\qquad |u|=|v|=1,
\qquad u\cdot v=\frac12.
\]

The outer native intermediate Cell `a+b` projects to carrier displacement

\[
w=u+v.
\]

Hence

\[
|w|^2=1+1+2\cdot\frac12=3
\]

and its normalized direction is

\[
\widehat w=\frac{u+v}{\sqrt3}.
\]

Its correlation with either endpoint direction is

\[
\begin{aligned}
u\cdot\widehat w
&=\frac{1+1/2}{\sqrt3}\\
&=\frac{\sqrt3}{2}\\
&=\sqrt{\frac{1+1/2}{2}}.
\end{aligned}
\]

Thus the first Viète half-angle radical appears directly:

\[
\boxed{
\cos 30^\circ=\sqrt{\frac{1+\cos60^\circ}{2}}=\frac{\sqrt3}{2}.
}
\]

No target value of `pi` is used.

### Collinearity with the already-proved C12 gate

The existing pivot-local carrier gate between adjacent directions is at

\[
\gamma=\frac{u+v}{3}.
\]

The outer Cell carrier displacement is

\[
w=u+v=3\gamma.
\]

Therefore

\[
\boxed{
\text{OUTER NATIVE CELL, C12 TRIPLE GATE, AND VIETE NORMALIZED BISECTOR LIE ON THE SAME CARRIER RAY.}
}
\]

They are different typed objects at different radial positions; they must not be identified as the same state.

## 6. Exact native 12-Cell outer microcycle

Choose one chirality of the six local phase directions

\[
a_0,\ldots,a_5,
\qquad a_{r+6}=a_r.
\]

Define

\[
m_r=a_r+a_{r+1}.
\]

Then

\[
a_r\to m_r
\]

is the primitive signed-axis step `+a_{r+1}`, and

\[
m_r\to a_{r+1}
\]

is the primitive signed-axis step `-a_r`.

Therefore

\[
\boxed{
a_0,m_0,a_1,m_1,\ldots,a_5,m_5}
\]

is a 12-state closed cycle of actual native Cells connected entirely by primitive Cell adjacency.

All six `a_r` are distinct radius-one Cells and all six `m_r` are distinct radius-`sqrt(2)` Cells, so all twelve native states are distinct.

Let `F` be the primitive successor around this outer cycle. Then

\[
F^{12}=1.
\]

Because

\[
a_{r+3}=-a_r,
\qquad
m_{r+3}=-m_r,
\]

we also have the exact half-turn relation

\[
\boxed{F^6(z)=-z}
\]

for every relative state on the cycle.

## 7. Restricted operation-safe quotient onto the local C12 phase carrier

Define

\[
\Psi_{12}(a_r)=E_r,
\qquad
\Psi_{12}(m_r)=G_r,
\]

where `E_r,G_r` are the already-proved local C12 Cell/gate phase labels.

Then

\[
\Psi_{12}(F(a_r))=G_r,
\qquad
\Psi_{12}(F(m_r))=E_{r+1}.
\]

Hence

\[
\boxed{
\Psi_{12}\circ F=Q\circ\Psi_{12},
}
\]

where `Q` is the established local C12 successor

\[
E_r\to G_r\to E_{r+1}.
\]

This is a genuine native-Cell dynamical lift of the local C12 **phase sequence** on the declared outer branch.

The typing remains strict:

- `m_r` is a native Cell;
- `G_r` is a carrier incidence/gate phase token;
- `Psi_12` is a phase readout, not object identity.

The quotient is translation-equivariant because translating pivot and all twelve Cells by the same X6 translation leaves the relative cycle unchanged.

### Exact lease

The proved operation-safe horizon is generated by

- the outer-cycle primitive successor `F`;
- its inverse/predecessor;
- the six-step half-turn;
- native Cell versus phase-token typing under `Psi_12`;
- common translation of pivot plus trajectory.

It does **not** prove that every admissible native rotation law selects the outer branch, nor that every fixed-radius trajectory in full X6 enters this cycle.

## 8. The outer branch is uniquely selected by a nonzero-phase refinement requirement

For the two shortest branches joining adjacent unit-shell phase Cells:

- the inner branch has intermediate state `0`, where radial phase direction is undefined;
- the outer branch has intermediate state `a+b != 0`, whose carrier direction is exactly the half-angle bisector.

Therefore, within the two-shortest-path population,

\[
\boxed{
\text{REQUIRE A DEFINED NONZERO INTERMEDIATE PHASE}
\Longrightarrow
\text{UNIQUE OUTER BRANCH}.
}
\]

This is a scope-typed selection theorem, not a new P000 axiom and not a global law-selection result.

It provides a noncircular local reason for why the native microtrace supporting the C12 precision token is the radially outward realization rather than the pivot-crossing realization.

## 9. STAR-frame ambiguity: current Cell plus sweep bit is not globally enough

The current FCC/K4 STAR atlas is

\[
S_A=\{L_1,L_3,L_6\},
\quad
S_B=\{L_1,L_4,L_5\},
\]

\[
S_C=\{L_2,L_3,L_5\},
\quad
S_D=\{L_2,L_4,L_6\}.
\]

Every line family lies in exactly two STAR slices.

For example `L_1` lies in `S_A` and `S_B`. At the current signed radial direction `+L_1`:

- the two possible adjacent line families inside `S_A` are `L_3,L_6`;
- the two possible adjacent line families inside `S_B` are `L_4,L_5`.

These sets are disjoint.

Thus even after supplying one local sweep/chirality bit, erasing the STAR frame leaves two different possible next phase families.

For every line family the same K4-edge argument applies.

Therefore

\[
\boxed{
\text{CURRENT RADIAL CELL + SWEEP BIT DOES NOT DETERMINE AN ATLAS-WIDE LOCAL C6 SUCCESSOR.}
}
\]

At least one binary STAR-frame residual is required at a line shared by two STARs.

## 10. Previous/incoming phase is sufficient for STAR-frame recovery

Two distinct line families belonging to one STAR correspond to two K4 edges sharing exactly one K4 vertex. Therefore they belong to a unique STAR slice.

Hence, for a valid local C6 transition, the ordered previous/current signed phase pair

\[
(a_{r-1},a_r)
\]

determines the STAR frame uniquely.

Inside that C6 cycle, the ordered adjacent pair also fixes the sweep orientation: the next phase is the unique neighbor of `a_r` different from `a_{r-1}`.

Thus

\[
\boxed{
\text{PREVIOUS + CURRENT LOCAL PHASE IS SUFFICIENT TO RECOVER STAR FRAME AND C6 SWEEP}
}
\]

for the declared FCC/K4 local phase interface.

This is the first exact positive result on the `previous-Cell / incoming-edge` question in #1255, but its scope is deliberately narrow.

## 11. Previous/current endpoints are NOT sufficient for full native path provenance

The same macro transition

\[
a\to b
\]

has the two distinct shortest native microtraces

\[
a\to0\to b
\]

and

\[
a\to a+b\to b.
\]

Therefore knowing only the previous and current shell Cells does not tell which native branch was taken.

A future operation that asks any of the following distinguishes them immediately:

- did the trajectory visit the pivot?;
- what was the intermediate native radius?;
- what ordered signed-axis word was used?;
- what Path-formal/BRC branch identity was realized?

Consequently

\[
\boxed{
\text{PREVIOUS CELL IS SUFFICIENT FOR STAR-FRAME RECOVERY BUT INSUFFICIENT FOR FULL P000 PATH-PROVENANCE SAFETY.}
}
\]

On the unit-shell adjacent-phase interface the missing shortest-path provenance is exactly one branch bit

\[
\beta\in\{\mathrm{INNER},\mathrm{OUTER}\}.
\]

This bit is not the already-proved C12 `CELL/GATE` parity:

\[
\boxed{
\text{BRC INNER/OUTER BRANCH BIT} \neq \text{C12 CELL/GATE PHASE BIT}.
}
\]

They solve different information-loss problems.

Under the mandatory observer-preservation rule, `beta` remains `UNPROVEN_RETAIN` unless the declared future-operation horizon is proved insensitive to it or a law canonically selects one branch.

## 12. C24 single-Cell ray no-go in the triangular carrier

The first half-angle layer is special because the sum of two equal-radius adjacent C6 rays is itself an integer carrier-lattice vector.

The next half-angle would require a `15 degree` carrier ray.

Use a triangular-lattice basis

\[
u=(1,0),
\qquad
v=(1/2,\sqrt3/2).
\]

Any carrier Cell-center displacement is

\[
p u+q v,
\qquad p,q\in\mathbf Z,
\]

with slope

\[
\tan\theta=\frac{q\sqrt3}{2p+q}.
\]

If `theta=15 degrees`, then

\[
\frac{q\sqrt3}{2p+q}=2-\sqrt3.
\]

Equivalently

\[
q\sqrt3=(2p+q)(2-\sqrt3).
\]

Comparing rational and `sqrt(3)` coefficients in `Q(sqrt(3))` gives

\[
2(2p+q)=0,
\qquad
q=-(2p+q).
\]

Thus

\[
p=q=0.
\]

Therefore

\[
\boxed{
\text{NO NONZERO TRIANGULAR CARRIER CELL-CENTER RAY HAS EXACT }15^\circ\text{ PHASE.}
}
\]

So the exact C24 phase token cannot be required to be a new single Cell center in this STAR carrier lattice.

This is compatible with the prior result that C24 has a balanced component-spinor realization: the present theorem rules out only the stronger `single spatial Cell ray` demand.

## 13. Rebased answer to the #1255 state question

At the current centered-X6 / FCC-STAR interface, the smallest state claims that are now actually proved are:

### Macro phase only

For local C6 phase continuation across the four-STAR atlas:

\[
\boxed{
(\text{previous shell phase},\text{current shell phase})
}
\]

is sufficient to recover the STAR frame and sweep at the carrier-phase level.

### Native path/provenance horizon

For a shortest native realization of one adjacent C6 macrostep, previous/current endpoints alone are not sufficient. One must additionally retain

\[
\boxed{\beta=\mathrm{INNER/OUTER}}
\]

unless a branch-selection/descent theorem is supplied.

### Outer phase-refinement lease

If the declared refinement requires a nonzero intermediate phase, `beta=OUTER` is uniquely selected and the resulting actual native Cell microtrajectory admits the exact operation-safe local C12 phase quotient

\[
\Psi_{12}.
\]

### Deep refinement

C24 cannot be demanded as another single centered STAR Cell ray. Deeper precision must use a richer typed carrier such as the already-studied spinor/history/pro-state layer, or an as-yet-unproved native object.

## 14. What this closes and what remains open

### Closed here

1. `PRIMITIVE_FIXED_RADIUS_MICROSTEP = NO_GO` in signed X6.
2. Every adjacent local C6 unit-shell macrostep has exactly two shortest native BRC branches.
3. The outer branch intermediate Cell is exactly on the C12 Viète/gate half-angle ray.
4. The all-outer choice yields a genuine 12-Cell primitive native cycle with `F^12=1` and `F^6=-1`.
5. This cycle factors operation-safely to the already-proved local C12 phase successor on the declared lease.
6. One incoming/previous phase is sufficient to recover STAR frame and sweep locally.
7. Previous/current endpoints are insufficient for full path provenance; one inner/outer branch bit remains.
8. No exact C24/15-degree single Cell-center ray exists in the triangular STAR carrier.

### Still open for #1255

1. prove that an actual global/relevant native rotation law canonically selects the outer microtrace, or prove a different branch law;
2. decide whether the inner/outer BRC bit can be safely quotiented for a strictly phase-only future horizon;
3. globalize the local incoming-edge state across all relevant STAR transitions with explicit chart transport;
4. integrate the current C24 spinor/history state with this native C12 outer-Cell lift;
5. construct or refute the full trajectory-to-`P_rot` semiconjugacy once the domain state and branch law are frozen.

Strongest current synthesis:

\[
\boxed{
\text{CENTERED X6 MAKES ROTATION PRECISION LITERALLY MULTISCALE:}
}
\]

\[
\boxed{
\text{C6 FIXED-RADIUS MACRO PHASE}
\;\longrightarrow\;
\text{TWO-BRANCH NATIVE MICROTRACE}
\;\longrightarrow\;
\text{OUTER C12 VIETE BISECTOR CELL}
}
\]

with deeper C24+ precision leaving the single-Cell ray category.
