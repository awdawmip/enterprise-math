# The all-face-odd Euler chirality cover is the cube

Status: `FREE_RESEARCH / EXACT FINITE GRAPH ISOMORPHISM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Author/program signature: `YUAN X / Enterprise Math`

## 1. From an obstruction to a covering geometry

The tetrahedral face-holonomy classification leaves exactly one nonzero class
fixed by the full coordinate-permutation group:

\[
h=1111.
\]

This class prevents the four three-axis slices from carrying one untwisted
globally signed Euler generator `J`.  It does not prevent a two-sheeted
orientation cover in which both local choices `J` and `-J` are retained.

The cover has eight states:

\[
(i,\sigma),
\qquad
 i\in\{0,1,2,3\},
\quad
 \sigma\in\mathbf F_2.
\]

For the all-negative edge representative, every move from one slice to a
different slice flips the sheet:

\[
(i,\sigma)\sim(j,\sigma+1)
\quad\Longleftrightarrow\quad i\ne j.
\]

The resulting graph is the bipartite double cover of `K4`, equivalently
`K_{4,4}` with one perfect matching removed.  The main result of this note is
that this graph is exactly the three-dimensional cube.

## 2. Explicit cube labeling

Choose the four even-parity cube vertices

\[
\begin{aligned}
r_0&=000,\\
r_1&=011,\\
r_2&=101,\\
r_3&=110.
\end{aligned}
\]

They represent the four antipodal body diagonals of the cube.  Define

\[
\Phi(i,0)=r_i,
\qquad
\Phi(i,1)=r_i+111.
\]

Thus switching the chirality sheet complements all three cube bits.

The map `Phi` is visibly bijective because the four `r_i` are precisely the
even vertices and their complements are precisely the odd vertices.

For distinct slices `i` and `j`, the even vertices `r_i` and `r_j` differ in
exactly two coordinates.  Hence `r_i` and the complement of `r_j` differ in
exactly one coordinate.  Therefore

\[
\boxed{
(i,\sigma)\sim(j,\sigma+1)
\iff
\Phi(i,\sigma)\text{ and }\Phi(j,\sigma+1)
\text{ differ in one bit}.
}
\]

This proves a graph isomorphism

\[
\boxed{
\widetilde K_4^{\rm chir}\cong Q_3.
}
\]

The cover has eight vertices, twelve edges, and degree three, exactly as the
cube graph.

## 3. Deck transformation and body diagonals

The deck transformation is

\[
\delta(i,\sigma)=(i,\sigma+1).
\]

Under the cube labeling,

\[
\boxed{
\Phi(\delta(i,\sigma))
=
\Phi(i,\sigma)+111.
}
\]

So the residual chirality reversal

\[
J\longmapsto-J
\]

is the central antipodal map of the cube.

Each original slice is recovered as one antipodal pair:

\[
\{(i,0),(i,1)\}
\longleftrightarrow
\{r_i,r_i+111\}.
\]

Consequently the four tetrahedral slices are the four body diagonals of the
cube, and quotienting the cube vertices by antipodality recovers the four
vertices of the tetrahedral atlas.

## 4. Why `S4 × C2` appears naturally

The rotational symmetry group of a cube permutes its four body diagonals and
is the standard geometric copy of `S4`.  The central antipodal involution
commutes with all these rotations and supplies the additional `C2`.

Thus the pair

\[
S_4\quad\text{and}\quad C_2
\]

is not an arbitrary algebraic decoration in the all-face-odd Euler lift:

- `S4` permutes the four slice/body-diagonal labels;
- `C2` reverses the two endpoints of every body diagonal simultaneously;
- the eight signed local generators are the eight cube vertices.

At the level of the full cube symmetry group this is the familiar central
extension by inversion.  The present package uses only the explicit finite
vertex/edge isomorphism; it does not require a historical novelty claim about
cube or octahedral symmetry.

## 5. Gauge changes do not change the cover

For a general edge cochain `e`, define its orientation cover by

\[
(i,\sigma)\sim_e(j,\sigma+e_{ij}).
\]

A vertex gauge

\[
e'_{ij}=e_{ij}+g_i+g_j
\]

is implemented upstairs by the sheet relabeling

\[
(i,\sigma)\longmapsto(i,\sigma+g_i).
\]

Therefore gauge-equivalent edge systems have canonically isomorphic
orientation covers.  The cube is an invariant of the all-face-odd gauge
class, not an artifact of choosing the all-one edge representative.

The exact Python regression checks this adjacency equivalence for all

\[
64\times16\times8\times8
=65536
\]

combinations of edge systems, gauges, and ordered signed-state pairs.

## 6. Interpretation for Euler geometry

The all-face-odd class should no longer be described only as a failure to glue.
It has a positive global replacement:

\[
\boxed{
\text{the signed Euler generator globalizes on the cube orientation cover.}
}
\]

Downstairs on the four slices, only reversal-even observables are single
valued.  Upstairs on the cube, the reversal-odd coordinate is also globally
well defined because the two chirality sheets have been separated.

This gives the following hierarchy:

\[
\begin{array}{c|c}
\text{object}&\text{global status}\\ \hline
J^2,\ \text{norm},\ \text{cosine/Viète even channel}
&\text{single valued on the four-slice quotient}\\
J,\ \text{sine/chiral odd channel}
&\text{single valued on the eight-state cube cover}\\
\text{choice of one global sign of }J
&\text{not available in the all-face-odd class}
\end{array}
\]

## 7. Relation to the accepted P000 residual bit

Given the already accepted P000 all-triangle-negative transition signature,
the orientation cover constructed above is canonically the cube.  Its deck
involution is one concrete geometric realization of the remaining symmetric
`C2` bit.

This is stronger than merely observing a two-valued sign ambiguity.  It
identifies the minimal global state space supporting the signed local Euler
generator:

\[
\boxed{
4\text{ slices}\times2\text{ chirality sheets}
=8\text{ cube vertices}.
}
\]

The statement remains conditional on the accepted overlap signature.  Bare
FCC incidence still allows both the flat class and the all-face-odd class and
therefore does not by itself choose the cube cover.

## 8. Formal coverage and boundary

`EulerFccChiralityGluing.lean` proves:

- the eight signed slice states and eight cube vertices have the same finite
  cardinality;
- `cubeLabel` is bijective;
- cover adjacency is equivalent to Hamming-distance-one cube adjacency;
- the deck flip is cube antipodality;
- the deck flip has no fixed point.

The executable checker independently verifies the same graph isomorphism and
counts twelve undirected edges on both sides.

What remains open is the native selection theorem:

> derive the all-face-odd transition class, rather than the flat class, from
> an explicit six-dimensional Cell transport law.

The covering geometry is now exact.  Its native dynamical origin is the next
problem.
