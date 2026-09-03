# Euler FCC slice chirality: tetrahedral face-holonomy classification

Status: `FREE_RESEARCH / EXACT FINITE CLASSIFICATION / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Author/program signature: `YUAN X / Enterprise Math`

## 1. Question left by the Euler completion theorem

The local Euler program now has a normalized chiral generator

\[
J^2=-1,
\]

a finite compatible rotation-root tower, a unique normalized character-circle
completion, and the Cell-rooted Viète mean flow.  What remains open is not the
local meaning of Euler's formula.  It is the globalization problem:

> Can the four three-axis FCC slices use one globally signed generator `J`, or
> do their pairwise overlap identifications carry a nontrivial chirality
> twist?

The accepted P000 synthesis already records four tetrahedral/FCC charts and a
chart-transition signature whose triangle loop products are all negative.
Separately, R059D proves that the twelve oriented FCC nearest-neighbor
directions admit a globally coherent sign assignment.  These statements must
not be conflated:

- direction-sign closure orients individual nearest-neighbor lines;
- slice-chirality transport compares cyclic orders, hence the signs of local
  complex structures on three-axis slices.

The present note classifies the second object exactly.  It treats the six
slice-overlap signs as input data.  It does **not** derive those signs from bare
FCC incidence.

## 2. The tetrahedral transition system

Label the four three-axis slices by

\[
0,1,2,3.
\]

Every pair overlaps along one line family, so the overlap graph is the complete
graph

\[
K_4.
\]

Choose a signed local chiral generator `J_i` on each slice.  For every edge
`ij`, let

\[
e_{ij}\in\mathbf F_2
\]

record whether the overlap identification preserves or reverses the chosen
sign:

\[
J_j=(-1)^{e_{ij}}J_i.
\]

Thus one transition system is a six-bit edge cochain

\[
e=(e_{01},e_{02},e_{03},e_{12},e_{13},e_{23})
\in C^1(K_4;\mathbf F_2).
\]

Changing the sign of the generator in slice `i` is a vertex gauge

\[
g_i\in\mathbf F_2.
\]

The gauge action is

\[
\boxed{
 e_{ij}\longmapsto e_{ij}+g_i+g_j.
}
\]

The simultaneous reversal

\[
(g_0,g_1,g_2,g_3)=(1,1,1,1)
\]

acts trivially on every edge.  Hence the effective vertex-gauge group has
size

\[
\frac{2^4}{2}=8.
\]

## 3. Four face holonomies

For the four triangular faces, define

\[
\begin{aligned}
h_{012}&=e_{01}+e_{02}+e_{12},\\
h_{013}&=e_{01}+e_{03}+e_{13},\\
h_{023}&=e_{02}+e_{03}+e_{23},\\
h_{123}&=e_{12}+e_{13}+e_{23},
\end{aligned}
\qquad\text{in }\mathbf F_2.
\]

A local frame flip contributes twice to every adjacent triangle, so each
`h_ijk` is gauge invariant.

Every tetrahedral edge occurs in exactly two faces.  Consequently

\[
\boxed{
 h_{012}+h_{013}+h_{023}+h_{123}=0.
}
\]

This is the finite tetrahedral Bianchi identity.  The four face bits therefore
belong to the even-weight code

\[
E_4=
\left\{
 h\in\mathbf F_2^4:\sum_f h_f=0
\right\}.
\]

It has exactly eight elements:

\[
0000,\quad
1100,1010,1001,0110,0101,0011,\quad
1111.
\]

## 4. Completeness theorem

### Theorem 4.1 — face holonomy is the complete gauge invariant

For two edge assignments `e` and `e'`,

\[
\boxed{
 e\sim_{\rm gauge}e'
 \iff
 h(e)=h(e').
}
\]

One proof is constructive.  Use vertex gauge to put every class in the star
gauge

\[
e_{01}=e_{02}=e_{03}=0.
\]

Then the remaining edges are forced to be

\[
(e_{12},e_{13},e_{23})
=(h_{012},h_{013},h_{023}),
\]

while the Bianchi relation forces

\[
h_{123}=h_{012}+h_{013}+h_{023}.
\]

Therefore

\[
\boxed{
C^1(K_4;\mathbf F_2)/\delta C^0(K_4;\mathbf F_2)
\cong E_4.
}
\]

The executable classifier exhausts all 64 edge assignments and all 16 vertex
gauges.  It finds:

- exactly 8 gauge classes;
- every class has 8 edge representatives;
- 8 assignments are flat;
- 48 assignments lie in one of the six weight-two classes;
- 8 assignments lie in the all-face-odd class.

### Theorem 4.2 — global signed generator criterion

There exists a choice of local signs making every overlap preserve `J` if and
only if

\[
\boxed{h(e)=0000.}
\]

Equivalently, a globally signed Euler generator exists exactly in the flat
class.

When it exists, the trivializing choice is unique up to simultaneous reversal
of all four slice generators:

\[
(J_0,J_1,J_2,J_3)
\longleftrightarrow
(-J_0,-J_1,-J_2,-J_3).
\]

## 5. Reduction by full tetrahedral symmetry

The coordinate-permutation group `S_4` acts transitively on the four faces.
On the even-weight code `E_4`, the orbits are completely determined by Hamming
weight:

\[
\begin{array}{c|c|c}
\text{weight}&\text{number of patterns}&\text{orbit size}\\ \hline
0&1&1\\
2&6&6\\
4&1&1
\end{array}
\]

Hence the only face vectors fixed by the full `S_4` action are

\[
0000
\quad\text{and}\quad
1111.
\]

The fixed subspace is therefore

\[
\boxed{
E_4^{S_4}=\langle1111\rangle\cong\mathbf F_2.
}
\]

This sharpens the earlier statement that the unrestricted gauge quotient has
three independent bits.  Before imposing full coordinate symmetry, the
quotient is indeed the three-dimensional code `E_4`.  After imposing full
`S_4` invariance, exactly one bit survives.

### Theorem 5.1 — unique nontrivial fully symmetric obstruction

Among all gauge classes, the all-face-odd class

\[
\boxed{1111}
\]

is the unique nonzero class invariant under all coordinate permutations.

Thus full tetrahedral symmetry does not force flatness.  It leaves precisely
one nontrivial symmetric alternative.

## 6. Identification of the accepted P000 signature

Encode a negative overlap sign by bit `1`.  The accepted all-negative edge
representative is

\[
e_{01}=e_{02}=e_{03}=e_{12}=e_{13}=e_{23}=1.
\]

Every triangle contains three negative edges, so

\[
1+1+1=1\pmod2.
\]

Therefore

\[
\boxed{
h(e)=1111.}
\]

The accepted P000 antibalanced transition signature is consequently the
unique nonzero fully `S_4`-invariant class of the Euler slice-chirality gauge
quotient.

This is a genuine bridge, but it is a **conditional identification**:

- given the accepted P000 overlap signature, its class is canonically `1111`;
- the present theorem does not derive the six overlap signs from FCC incidence;
- it does not assert that every previously occurring `C_2` residual is this
  same class.

## 7. Geometric meaning of the all-face-odd class

The class `1111` means that transport around every triangular cycle sends

\[
J\longmapsto-J.
\]

Therefore one cannot choose one untwisted globally signed `J` on all four
slices.

This does not destroy the local Euler character.  It says that the signed
chiral generator is a section of a twisted orientation line/torsor rather
than a global scalar-valued choice.

Objects even under reversal still descend.  In particular, quantities built
from

\[
J^2=-1,
\]

the character norm, and the reversal-even cosine/Viète channel are unaffected
by `J\mapsto-J`.  The reversal-odd sine channel changes sign and must remain
slice-framed or twisted.

The correct global distinction is therefore:

\[
\boxed{
\begin{aligned}
\text{flat class }0000
&:\text{ one global signed }J,\\
\text{antibalanced class }1111
&:\text{ one global }J\text{-torsor, but no global sign.}
\end{aligned}
}
\]

## 8. Relation to the twelve-direction sign theorem

R059D proves a globally coherent sign assignment on the twelve oriented FCC
nearest-neighbor directions.  That theorem remains fully valid in the
all-face-odd chirality class.

There is no contradiction because the two structures ask different
questions:

1. **direction sign:** does a shared line receive one consistent arrow?
2. **slice chirality:** do the three arrows in one local slice have a cyclic
   order compatible with the cyclic order in another slice?

A global orientation on every line does not by itself select compatible cyclic
orders on all four slice planes.  The first is a one-direction transport
problem; the second is a frame/complex-structure transport problem.

Freeze:

`TWELVE_DIRECTION_SIGN_CLOSURE_DOES_NOT_TRIVIALIZE_SLICE_CHIRALITY_HOLONOMY`.

## 9. Formal and executable coverage

The finite Lean module proves by exhaustive kernel reduction:

- the Bianchi parity identity;
- gauge invariance of all four face holonomies;
- completeness of face holonomy as a gauge invariant;
- realization of every even face vector;
- globalizability exactly in the flat class;
- uniqueness of a trivializing frame up to global reversal;
- the weight `0/2/4` trichotomy;
- the fully symmetric `0000/1111` dichotomy;
- the all-negative representative has holonomy `1111`;
- the antibalanced class is not globalizable;
- exact assignment counts `8/48/8`.

The Python checker independently enumerates all edge assignments, gauges, and
all 24 coordinate permutations.  Its tests compare all `64^2=4096` pairs of
edge systems to verify that equal face holonomy is equivalent to gauge
equivalence.

## 10. What is now closed

The following problem is now finite and complete:

\[
\boxed{
\text{classification of four-slice signed-}J\text{ transition systems}
\text{ modulo local frame reversal and }S_4.
}
\]

The exact answer is:

\[
\boxed{
\begin{aligned}
\text{unrestricted gauge quotient}&\cong E_4\cong\mathbf F_2^3,\\
\text{full-}S_4\text{ fixed quotient}&\cong\mathbf F_2,\\
\text{unique nonzero fixed class}&=1111.
\end{aligned}
}
\]

## 11. Remaining native problem

The next unresolved step is no longer a classification problem.  It is a
construction/derivation problem:

> Produce the six slice-overlap chirality transition bits from an explicit
> native six-dimensional Cell transport law, and prove that they equal the
> accepted P000 antibalanced signature—or else identify the additional native
> datum that selects another class.

Bare tetrahedral incidence cannot do this by itself: both `0000` and `1111`
are fully `S_4` symmetric.  A derivation must use additional transport,
orientation, path-history, parity, or operator data.

That remaining obstruction can now be stated sharply:

\[
\boxed{
\text{native globalization must select one of two fully symmetric classes.}
}
\]

The local Euler theorem is complete; the remaining six-dimensional question
is the origin of this single symmetric `C_2` bit.
