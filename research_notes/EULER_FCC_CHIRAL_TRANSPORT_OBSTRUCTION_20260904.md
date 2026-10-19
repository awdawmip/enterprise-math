# FCC chirality transport obstruction, exact sequence, and Euler monodromy

Status: `FREE_RESEARCH / EXACT FINITE THEOREM PACKAGE / NOT FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`
Author/program signature: `YUAN X / Enterprise Math`

## 1. Objective

The local Euler-rotation construction supplies a chiral complex structure
\(J_i\) on each of four tetrahedrally related FCC three-axis slices. The
remaining globalization question is not whether each slice has a valid
\(J_i^2=-1\), but whether the four local signs can be transported consistently
through the six pairwise overlaps.

This note closes the complete finite obstruction theory. It proves:

1. only three gauge-invariant chirality defects exist, not six;
2. they are the face holonomies of an exact tetrahedral cochain sequence;
3. flat transport is equivalent to a global signed \(J\), unique up to one
   overall reversal;
4. the minimum number of overlap-sign repairs is \(0,1,\) or \(2\), with an
   exact classification;
5. a nontrivial obstruction conjugates the odd Euler channel and reverses
   signed winding, while the scalar/even channel and the half-turn endpoint
   \(-1\) remain globally meaningful;
6. bare FCC incidence determines the obstruction operator but cannot determine
   the actual overlap connection.

The last point identifies the precise native datum still missing from P000.

## 2. Four slices, six overlaps, four face holonomies

Index the four local slices by \(0,1,2,3\). For each overlap edge \(ij\), let

\[
\varepsilon_{ij}\in\mathbf F_2
\]

record whether the overlap transport preserves or reverses the local chiral
generator:

\[
T_{ij}J_i=(-1)^{\varepsilon_{ij}}J_jT_{ij}.
\]

The six edge bits are ordered as

\[
(\varepsilon_{01},\varepsilon_{02},\varepsilon_{03},
  \varepsilon_{12},\varepsilon_{13},\varepsilon_{23}).
\]

For the four triangular faces define

\[
\begin{aligned}
h_{012}&=\varepsilon_{01}+\varepsilon_{02}+\varepsilon_{12},\\
h_{013}&=\varepsilon_{01}+\varepsilon_{03}+\varepsilon_{13},\\
h_{023}&=\varepsilon_{02}+\varepsilon_{03}+\varepsilon_{23},\\
h_{123}&=\varepsilon_{12}+\varepsilon_{13}+\varepsilon_{23},
\end{aligned}
\qquad\text{in }\mathbf F_2.
\]

They satisfy the exact parity identity

\[
\boxed{h_{012}+h_{013}+h_{023}+h_{123}=0.}
\]

Hence frustrated faces occur in an even number: zero, two, or four.

Only three face bits are independent. A convenient defect vector is

\[
\boxed{\kappa(\varepsilon)
=(h_{012},h_{013},h_{023})\in\mathbf F_2^3,}
\]

with

\[
h_{123}=h_{012}+h_{013}+h_{023}.
\]

## 3. Local frame gauge and the exact sequence

Changing the sign convention of the local generator on slice \(i\),

\[
J_i\longmapsto(-1)^{g_i}J_i,
\qquad g_i\in\mathbf F_2,
\]

changes the edge connection by

\[
\varepsilon_{ij}\longmapsto
\varepsilon_{ij}+g_i+g_j.
\]

Every face holonomy is invariant under this transformation.

Let \(C^0=\mathbf F_2^4\), \(C^1=\mathbf F_2^6\), and let
\(C^2_{\rm even}\subset\mathbf F_2^4\) denote the even-parity face patterns.
Then the tetrahedral operators fit into the exact sequence

\[
\boxed{
0\longrightarrow\mathbf F_2
\longrightarrow C^0
\xrightarrow{\delta_0}C^1
\xrightarrow{\delta_1}C^2_{\rm even}
\longrightarrow0.
}
\]

Here:

- the first \(\mathbf F_2\) consists of the two constant vertex flips;
- \(\delta_0g\) has edge value \(g_i+g_j\);
- \(\delta_1\varepsilon\) is the four-face holonomy vector.

Exactness gives all structural conclusions at once:

\[
\ker\delta_0=\{\text{global flips}\},
\]

\[
\ker\delta_1=\operatorname{im}\delta_0,
\]

\[
\operatorname{im}\delta_1=C^2_{\rm even}.
\]

Consequently:

\[
\boxed{
C^1/\operatorname{im}\delta_0
\cong\mathbf F_2^3.
}
\]

There are \(64\) raw edge connections, \(8\) gauge classes, and \(8\) edge
connections in each class. The flat class also contains exactly \(8\)
connections.

On the one-skeleton \(K_4\), this quotient is the orientation-line class

\[
w_1(\mathcal J)=[\varepsilon]\in
H^1(K_4;\mathbf F_2)\cong\mathbf F_2^3.
\]

Filling the four triangular faces converts the same three numbers into the
curvature obstruction to extending the local system across the tetrahedron.

## 4. Flatness and global \(J\)

The connection is flat when

\[
h_{012}=h_{013}=h_{023}=h_{123}=0.
\]

Choose slice \(0\) as root and set

\[
g_0=0,\qquad
g_1=\varepsilon_{01},\qquad
g_2=\varepsilon_{02},\qquad
g_3=\varepsilon_{03}.
\]

Flatness forces

\[
\boxed{
\varepsilon_{12}=\varepsilon_{01}+\varepsilon_{02},\quad
\varepsilon_{13}=\varepsilon_{01}+\varepsilon_{03},\quad
\varepsilon_{23}=\varepsilon_{02}+\varepsilon_{03}.
}
\]

Thus

\[
\varepsilon_{ij}=g_i+g_j.
\]

After replacing \(J_i\) by \((-1)^{g_i}J_i\), all overlap transports preserve
the same sign. Conversely, any globally signed \(J\) gives these equations.

Therefore:

\[
\boxed{
\text{a global chiral generator exists}
\iff
\kappa(\varepsilon)=0.
}
\]

The potential \(g\) is unique modulo the constant flip
\((1,1,1,1)\), so the global generator is unique up to

\[
J\longleftrightarrow-J.
\]

## 5. Rooted normal form and the true three-bit residual

Keep the three rooted tree edges \(01,02,03\) and form their unique flat
extension

\[
\varepsilon^{\rm flat}
=
(a,b,c,a+b,a+c,b+c),
\]

where

\[
(a,b,c)
=
(\varepsilon_{01},\varepsilon_{02},\varepsilon_{03}).
\]

Then

\[
\boxed{
\varepsilon-\varepsilon^{\rm flat}
=
(0,0,0,h_{012},h_{013},h_{023}).
}
\]

This is a canonical spanning-tree gauge normal form. It proves that the six
raw overlap signs decompose into:

- three frame-dependent tree coordinates;
- three frame-independent obstruction coordinates.

So the native problem should not be phrased as “derive six physical bits.”
The gauge-invariant target is the three-bit residual \(\kappa\).

## 6. Exact minimum repair theorem

Suppose a computed or measured overlap connection is not flat. An edge repair
means toggling one overlap sign.

### 6.1 Two frustrated faces

If exactly two triangular faces have holonomy \(1\), they meet in one unique
tetrahedral edge. Toggling that edge toggles exactly those two face
holonomies.

Hence:

\[
\boxed{
\text{every two-face defect has one unique one-edge repair.}
}
\]

There are \(48\) such raw connections.

### 6.2 Four frustrated faces

If all four face holonomies are \(1\), no single edge can repair the
connection, because a single edge changes exactly two faces.

The minimum repair distance is \(2\). The three and only three minimum
repairs are the opposite-edge pairs

\[
\boxed{
\{01,23\},\qquad
\{02,13\},\qquad
\{03,12\}.
}
\]

There are \(8\) raw fully frustrated connections.

Thus the complete repair-distance distribution on all \(64\) states is

\[
\boxed{
8\text{ states at distance }0,\quad
48\text{ at distance }1,\quad
8\text{ at distance }2.
}
\]

The all-four-frustrated class is the unique obstruction class that cannot be
localized to one bad overlap.

## 7. Euler phase glues as an \(O(2)\) local system

Write a local Euler phase in slice \(i\) as

\[
E_i(t)=C(t)+J_iS(t).
\]

Across overlap \(ij\),

\[
\boxed{
E_i(t)\longmapsto
C(t)+(-1)^{\varepsilon_{ij}}J_jS(t).
}
\]

Thus a sign-preserving overlap acts as the identity on the complex character,
while a sign-reversing overlap acts as complex conjugation.

The local phases therefore always glue as an \(O(2)\)-type local system

\[
U(1)\rtimes\mathbf F_2,
\]

where \(\mathbf F_2\) acts on \(U(1)\) by inversion/conjugation. They reduce
to a globally oriented \(U(1)\) character exactly when \(w_1(\mathcal J)=0\).

The even and odd channels behave differently:

\[
C(t)\longmapsto C(t),
\]

\[
J_iS(t)\longmapsto(-1)^{\varepsilon_{ij}}J_jS(t).
\]

Therefore:

\[
\boxed{
\text{the reversal-even/scalar channel globalizes for every connection,}
}
\]

whereas

\[
\boxed{
\text{the reversal-odd/chiral channel globalizes exactly in the flat class.}
}
\]

This explains why scalar \(\pi\)-readouts can remain well defined before a
global choice of \(i\) has been derived.

## 8. Half-turn blindness and quarter-turn detection

Complex conjugation fixes the real axis. In particular,

\[
\overline{1}=1,\qquad
\overline{-1}=-1.
\]

Hence the half-period endpoint identity

\[
E_i(\pi_{\rm rot})=-1
\]

is compatible with every overlap sign and every holonomy class.

But conjugation reverses a quarter-turn:

\[
\overline{J_i}=-J_i.
\]

Consequently:

\[
\boxed{
\text{the Euler half-turn endpoint cannot detect FCC chirality obstruction,}
}
\]

while

\[
\boxed{
\text{a transported quarter-turn detects it exactly.}
}
\]

More generally, a loop with holonomy \(1\) sends

\[
C(t)+J_iS(t)
\longmapsto
C(t)-J_iS(t).
\]

Only phases with \(S(t)=0\) survive such a loop unchanged.

This also sharpens an earlier endpoint warning: the equality
\(e^{i\pi}=-1\) by itself is too coarse to prove the existence of a global
signed \(i\).

## 9. Signed winding has the same obstruction

Transport a local integer winding coordinate through overlap \(ij\) by

\[
W_j=(-1)^{\varepsilon_{ij}}W_i.
\]

Around a face \(ijk\),

\[
W_i\longmapsto(-1)^{h_{ijk}}W_i.
\]

Thus:

\[
\boxed{
\text{nonzero signed winding globalizes}
\iff
\kappa(\varepsilon)=0.
}
\]

If the obstruction is nonzero, orientation-blind quantities such as

\[
|W|,\qquad W^2,
\]

still globalize, while the sign of \(W\) does not.

The chirality obstruction for \(J\), the conjugation monodromy of the odd
Euler channel, and the sign obstruction for integer winding are therefore
one and the same three-bit class.

## 10. Incidence-only no-go theorem

Bare tetrahedral incidence determines:

- which six overlaps exist;
- which three edges bound each face;
- the maps \(\delta_0\) and \(\delta_1\);
- the test \(\kappa(\varepsilon)\);
- the repair rules once \(\varepsilon\) is supplied.

It does **not** supply an intertwiner \(T_{ij}\), a determinant sign, an
ordered overlap frame, or any other datum from which
\(\varepsilon_{ij}\) can be evaluated.

Moreover, on the set of flat connections the effective local-frame gauge
group

\[
C^0/\{\text{constant flips}\}\cong\mathbf F_2^3
\]

acts freely and transitively. A rule based only on data invariant under all
local frame flips would have to choose a gauge-fixed point invariant under
that free action, and no such point exists.

Therefore:

\[
\boxed{
\text{FCC incidence alone cannot canonically select the actual flat
chirality transport.}
}
\]

This is the exact finite reason the prior P000 axioms did not determine the
six overlap signs.

## 11. Minimal native augmentation

A sufficient typed augmentation is an overlap intertwiner for every edge:

\[
T_{ij}:V_i\to V_j,
\qquad
T_{ji}=T_{ij}^{-1},
\]

together with the computable sign relation

\[
T_{ij}J_i=(-1)^{\varepsilon_{ij}}J_jT_{ij}.
\]

The global theorem then requires only the three independent flatness checks

\[
h_{012}=h_{013}=h_{023}=0;
\]

the fourth follows automatically.

Equivalent minimal presentations are:

1. six edge transports plus three triangle flatness checks;
2. three spanning-tree transports, with the remaining three defined by flat
   completion;
3. one vertex-potential class
   \[
   [g]\in\mathbf F_2^4/\langle(1,1,1,1)\rangle;
   \]
4. a stronger coherent oriented-volume/chirotope rule that computes the same
   relative signs from native geometry.

The fourth option is conceptually preferable if the six-dimensional model can
supply it, because it derives the three relative bits structurally rather than
declaring them.

## 12. Closed and open frontier

Closed by this package:

\[
\boxed{
\begin{aligned}
&\texttt{FCC\_CHIRAL\_DEFECT\_SPACE}=\mathbf F_2^3,\\
&\texttt{FLAT\_IFF\_GLOBAL\_SIGNED\_J},\\
&\texttt{GLOBAL\_J\_UNIQUE\_UP\_TO\_SIGN},\\
&\texttt{REPAIR\_DISTANCE}\in\{0,1,2\},\\
&\texttt{ODD\_EULER\_CHANNEL\_OBSTRUCTION}=w_1(\mathcal J),\\
&\texttt{SIGNED\_WINDING\_OBSTRUCTION}=w_1(\mathcal J),\\
&\texttt{HALF\_TURN\_ENDPOINT\_IS\_OBSTRUCTION\_BLIND}.
\end{aligned}
}
\]

Still open:

1. construct the actual \(T_{ij}\) from native six-dimensional Cell
   transition data;
2. prove those native intertwiners satisfy the three flatness equations;
3. identify whether the resulting class is related by an explicit
   intertwining theorem to the previously observed tetrahedral \(C_2\),
   backtracking \(C_2\), or Pell-shell sign;
4. prove every admissible native six-dimensional rotation trajectory factors
   through the local directed-edge/turn system.

The next research target is therefore no longer vaguely “globalize \(i\).”
It is the explicit operator theorem

\[
\boxed{
\texttt{NATIVE\_FCC\_OVERLAP\_INTERTWINERS\_CONSTRUCTED\_AND\_FLAT}.
}
\]
