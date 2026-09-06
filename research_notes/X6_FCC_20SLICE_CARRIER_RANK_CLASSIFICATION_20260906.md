# X6 selected 3-axis slices under the fixed FCC six-line readout: exact 4+4+12 rank/adjacency classification

Status: `FREE_RESEARCH / EXACT FIXED-CARRIER CLASSIFICATION + VIETE PLANAR-MECHANISM NO-GO / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Parent issue: `#1255`
Related Viète result: `research_notes/VIETE_X6_K4_ROOT_HOLONOMY_C24_ATLAS_20260906.md`
Current Foundation carrier: `definitions/P000_FCC_PRIMARY_COORDINATE_CARRIER_20260829.md`
Checker: `experiments/x6_fcc_20slice_carrier_rank_20260906/check_x6_fcc_20slice_carrier_rank.py`
Checker source commit: `73127e208605cf6423adbd31b6fa1742c3cd1d85`

## 1. Question

The current signed-X6 coordinate skeleton has 20 selected 3-of-6 native-axis slices.  Only four are presently equipped with the established close-packed triangular FCC STAR carrier projection and its physical `C6 -> C12` Cell/gate/OUTER Viète mechanism.

The exact question here is narrower and fixed-carrier typed:

> What do all 20 selected native-axis triples become under the **current official six FCC line-family representatives**, and which of them can support the already-proved connected planar C6 carrier mechanism without introducing a new carrier or transition law?

This does not ask whether another future carrier can represent the remaining slices.

## 2. Official six FCC line vectors and K4 labeling

Use the current carrier representatives

\[
\begin{aligned}
L_1&=(1,1,0),&L_2&=(1,-1,0),\\
L_3&=(1,0,1),&L_4&=(1,0,-1),\\
L_5&=(0,1,1),&L_6&=(0,1,-1).
\end{aligned}
\]

Let K4 vertices `0,1,2,3` denote the four established STARs `A,B,C,D`.  The unique shared line gives the edge labeling

\[
\begin{aligned}
E_{01}&=L_1,&E_{02}&=L_3,&E_{03}&=L_6,\\
E_{12}&=L_5,&E_{13}&=L_4,&E_{23}&=L_2.
\end{aligned}
\]

Then the four established STARs are exactly the four K4 vertex stars.

Every selected 3-of-6 axis triple is therefore one 3-edge subset of K4.  Its degree signature gives the exact S4 orbit type:

1. STAR: `(3,1,1,1)` — 4 triples;
2. TRIANGLE: `(2,2,2,0)` — 4 triples;
3. PATH: `(2,2,1,1)` — 12 triples.

Hence

\[
\boxed{20=4+4+12.}
\]

## 3. Determinant census: only STAR triples are carrier planes

For any chosen triple of line representatives form the `3x3` integer matrix with those vectors as rows.

The exhaustive exact census gives:

\[
\boxed{
\det=0\quad\text{for exactly the 4 STAR triples},
}
\]

while

\[
\boxed{
|\det|=2\quad\text{for every one of the 16 non-STAR triples}.
}
\]

Thus the fixed FCC carrier makes an exact rank split:

\[
\boxed{
\text{STAR orbit}:\operatorname{rank}=2,
\qquad
\text{TRIANGLE/PATH orbits}:\operatorname{rank}=3.
}
\]

This is the algebraic reason the current router has four close-packed planar STAR charts rather than twenty.

### STAR relation

For each STAR triple there are exactly two opposite sign choices

\[
(\sigma_1,\sigma_2,\sigma_3)\in\{\pm1\}^3
\]

satisfying

\[
\sigma_1v_1+\sigma_2v_2+\sigma_3v_3=0.
\]

After choosing one local orientation this is the familiar equal-vector triangular relation

\[
u_1+u_2+u_3=0.
\]

It supplies the rank-one common-depth kernel and the 2D triangular carrier plane.

No non-STAR triple admits any nonzero linear dependence, hence no sign choice can turn it into the same planar A2 relation.

## 4. Unexpected positive result: every non-STAR triple is a basis of the whole FCC parity lattice

Every official FCC line vector has even coordinate sum.  Hence every non-STAR triple generates a sublattice of

\[
D_3:=\{(x,y,z)\in\mathbf Z^3:x+y+z\equiv0\pmod2\}.
\]

The parity lattice `D3` has index two in `Z3`.

But every non-STAR triple has determinant absolute value two, so its generated lattice also has index two in `Z3`.

Containment plus equal index forces equality:

\[
\boxed{
\langle v_1,v_2,v_3\rangle_{\mathbf Z}=D_3
\quad\text{for all 16 non-STAR triples}.
}
\]

Therefore the remaining sixteen triples are not defective planes.  Under the fixed FCC readout they are **integer coordinate bases of the entire three-dimensional FCC carrier lattice**.

This gives a sharp type distinction:

\[
\boxed{
\begin{aligned}
4\text{ STAR triples}&:\text{ native Z3 slice }\to\text{ rank-2 triangular plane readout with kernel},\\
16\text{ non-STAR triples}&:\text{ native Z3 slice }\to D_3\text{ full-rank FCC carrier basis, injectively}.
\end{aligned}
}
\]

The fixed carrier therefore loses a common-depth coordinate on STAR charts but does **not** lose a coordinate on the 16 full-rank triples.

## 5. Signed-ray phase adjacency distinguishes all three orbit types

Each carrier line family is unoriented.  For one selected triple retain all six signed carrier rays

\[
\{\pm v_1,\pm v_2,\pm v_3\}.
\]

All have squared norm two.

Define the current nearest angular phase relation by classical carrier separation `60 degrees`, equivalently

\[
x\cdot y=1.
\]

This relation is independent of which representative sign was initially chosen for each line family because both signs are present in the six-ray set.

The exact induced graphs are:

### STAR orbit

For every STAR triple:

\[
\boxed{G_{60}=C_6.}
\]

All six signed rays lie in one connected degree-two cycle.  This is exactly the existing planar local C6 phase shell.

### TRIANGLE orbit

For every K4 triangle triple:

\[
\boxed{G_{60}=C_3\sqcup C_3.}
\]

The six signed rays split into two disconnected 3-cycles exchanged by global sign reversal.  There is no connected six-state successor using only the existing 60-degree carrier-neighbor relation.

### PATH orbit

For every three-edge K4 path triple:

\[
\boxed{G_{60}=P_3\sqcup P_3.}
\]

The degree sequence is

\[
(1,1,1,1,2,2),
\]

so the selected signed rays are not cyclic even before asking for a half-angle refinement.

Thus the fixed carrier gives the complete combinatorial trichotomy

\[
\boxed{
\text{STAR}:C_6,
\qquad
\text{TRIANGLE}:2C_3,
\qquad
\text{PATH}:2P_3.
}
\]

## 6. Exact no-go for direct reuse of the existing planar Viète mechanism

The already-proved physical STAR Viète interface requires, at minimum:

1. one rank-two carrier plane containing the three line families;
2. six signed nearest-neighbor directions forming one connected C6 phase cycle;
3. adjacent pairs participating in the same triangular Cell/gate incidence mechanism;
4. OUTER intermediate Cells producing the C12 half-angle lift of that C6 cycle.

The 16 non-STAR triples fail the first two conditions exactly:

- their line vectors are rank three;
- their signed 60-degree adjacency graph is never a connected C6.

Therefore

\[
\boxed{
\text{CURRENT FIXED FCC PLANAR }C_6\to C_{12}\text{ VIETE MECHANISM}
\text{ EXTENDS TO EXACTLY 4 OF THE 20 X6 THREE-AXIS SELECTIONS}.
}
\]

and

\[
\boxed{
\text{DIRECT SAME-MECHANISM EXTENSION TO THE OTHER 16}=	ext{NO-GO}.
}
\]

This is a fixed-carrier/mechanism theorem.  It does not say the sixteen slices can never admit another native rotation/root construction.

## 7. BRC observer meaning

The census reveals that “selected 3-axis slice” is too coarse a label for carrier behavior.

A quotient which records only the number of selected axes would identify states with different future carrier operations:

- STAR triples have a one-dimensional carrier kernel and connected C6 phase successor;
- non-STAR triples have no carrier kernel and no connected C6 successor;
- TRIANGLE and PATH triples are both full rank but have different signed-ray adjacency graphs.

Therefore the smallest carrier-operation-safe type on this horizon must retain at least the S4 orbit label

\[
\boxed{\mathrm{STAR}/\mathrm{TRIANGLE}/\mathrm{PATH}.}
\]

For operations inspecting exact basis geometry, the actual triple or an equivalent transported frame must also be retained.

BRC resolution:

`REUSE_APPLIED = OBSERVER/FUTURE-OPERATION FACTORIZATION TEST`.

`POSITIVE_WEIGHTED_BRC = NOT_APPLICABLE TO THIS DETERMINISTIC RANK/INCIDENCE CLASSIFICATION`.

## 8. Relation to the 40-state S6 orientation cover

The preceding Viète atlas result proved that all 20 native three-axis selections have a 40-state S6 kinematic orientation cover.

The present theorem refines its physical/carrier boundary:

- all 20 may carry an abstract cyclic orientation of their three native axis labels;
- only the four STARs currently map to a planar six-ray C6 carrier shell;
- the four TRIANGLE triples instead map to two carrier C3 sheets;
- the twelve PATH triples map to two open P3 sheets.

Hence

\[
\boxed{
\text{KINEMATIC ORIENTATION COVER} \neq \text{PHYSICAL PLANAR C6 ROOT CARRIER}.
}
\]

This distinction prevents silently promoting a 40-state orientation torsor into twenty physical Viète planes.

## 9. New interpretation of the sixteen non-STAR slices

The full-rank result suggests a different role for the 16 non-STAR selections:

> they are candidate complete FCC 3D coordinate frames, not additional triangular plane charts.

The two S4 orbits distinguish the internal first-shell incidence of such frames:

- TRIANGLE bases use three pairwise nonorthogonal FCC line families and expose two opposite C3 carrier triangles;
- PATH bases contain one classically orthogonal carrier-line pair and expose two open P3 chains under 60-degree adjacency.

No Viète root theorem is inferred from this observation.  It is a new structural route for later 3D carrier research.

## 10. Consequence for #1255

The earlier four-STAR bundle theorem is now sharp with respect to the current fixed FCC carrier:

\[
\boxed{
\text{FOUR-STAR CUBE/ROOT BUNDLE IS NOT MERELY THE FIRST EXAMPLE; IT IS THE COMPLETE DOMAIN OF THE EXISTING PLANAR FCC C6/C12 MECHANISM AMONG ALL 20 THREE-AXIS SELECTIONS}.}
\]

Therefore the remaining physical globalization problem should **not** ask to copy the same STAR plane construction onto the other sixteen slices.

The next valid alternatives are:

1. accept the four-STAR physical root bundle as the complete current FCC planar domain and derive connection selection from native dynamics;
2. invent and prove a genuinely 3D root/rotation mechanism on the full-rank D3 bases;
3. choose a different carrier/readout for those slices and prove its operation-safe relation to current X6/FCC data.

Direct planar cloning is closed by the determinant and signed-ray graph census.
