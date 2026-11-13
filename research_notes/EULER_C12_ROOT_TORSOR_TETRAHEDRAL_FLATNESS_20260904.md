# C12 root torsor, tetrahedral face-flatness, and projective Euler descent

Status: `FREE_RESEARCH / EXACT FINITE THEOREM PACKAGE / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`
Author/program signature: `YUAN X / Enterprise Math`

## 1. Objective

The local Euler/Viète line already separates three layers:

1. the six directed gate states of one triangular Cell carrier;
2. the first connected binary root cover, where a quarter-turn appears;
3. the four overlapping FCC slice charts, on which local chiral generators must be compared.

The remaining ambiguity has often been called a `C2` ambiguity. That phrase hides three different objects:

- the orientation-reversal factor inside `C6`;
- the kernel of the connected root cover `C12 -> C6`;
- the choice between the two quarter-turn roots `+J` and `-J`.

This note separates them and proves the exact globalization theorem.

The principal conclusions are:

\[
\boxed{C_6\simeq C_3\times C_2,\qquad C_{12}\simeq C_3\times C_4,}
\]

and the root-cover reduction is

\[
\boxed{\operatorname{id}_{C_3}\times(C_4\to C_2).}
\]

The `C4 -> C2` factor is non-split. The two quarter-turn roots form a free `C2` torsor exchanged by inversion. On the tetrahedral four-slice atlas, edgewise root comparisons globalize to one signed `J` if and only if the three independent triangular face holonomies vanish. When they do, the global `J` is unique up to overall reversal.

The scalar half-period endpoint is invariant under `J -> -J`. Consequently the Euler half-period identity descends projectively even before a global signed chirality is selected, whereas the oriented odd/sine channel does not.

## 2. The two different C2 factors

Write cyclic rotation states additively.

The Chinese-remainder maps are

\[
\Phi_6:C_6\longrightarrow C_3\times C_2,
\qquad
x\longmapsto(x\bmod3,x\bmod2),
\]

with inverse

\[
\Phi_6^{-1}(a,b)=4a+3b\pmod6,
\]

and

\[
\Phi_{12}:C_{12}\longrightarrow C_3\times C_4,
\qquad
x\longmapsto(x\bmod3,x\bmod4),
\]

with inverse

\[
\Phi_{12}^{-1}(a,b)=4a+9b\pmod{12}.
\]

Let

\[
r:C_{12}\longrightarrow C_6,
\qquad r(x)=x\bmod6.
\]

Then the square

\[
\begin{array}{ccc}
C_{12}&\xrightarrow{\Phi_{12}}&C_3\times C_4\\
\downarrow r&&\downarrow \operatorname{id}\times(\bmod2)\\
C_6&\xrightarrow{\Phi_6}&C_3\times C_2
\end{array}
\]

commutes.

Therefore the old `C2` in `C6` is the half-turn/orientation-reversal coordinate, while the new binary precision sheet is the kernel

\[
\ker(C_4\to C_2)=\{0,2\}.
\]

They are isomorphic abstract groups, but they have different types and must not be silently identified.

Freeze:

`C6_ORIENTATION_FACTOR != C12_ROOT_COVER_KERNEL`.

## 3. The first connected root cover is non-split

The reduction map has exact kernel

\[
\ker r=\{0,6\}\simeq C_2
\]

and is surjective, so there is a short exact sequence

\[
0\longrightarrow C_2\longrightarrow C_{12}\xrightarrow{r}C_6\longrightarrow0.
\]

### Theorem 3.1 — non-splitting

This extension does not split as an extension of groups.

Indeed, if a homomorphic section existed, the generator `1 in C6` would lift to an element `q in C12` satisfying

\[
r(q)=1,
\qquad 6q=0.
\]

The only preimages of `1` are `1` and `7`, and both have order twelve. Equivalently,

\[
6\cdot1=6\ne0,
\qquad
6\cdot7=42=6\ne0\pmod{12}.
\]

Thus no such generator lift exists.

Under the CRT decompositions this is exactly the familiar non-split extension

\[
0\longrightarrow C_2\longrightarrow C_4\longrightarrow C_2\longrightarrow0
\]

on the two-primary factor.

This is the first finite place where quarter-turn precision is genuinely new rather than an independent Boolean annotation.

## 4. The quarter-turn root torsor

The half-turn in `C12` is the element `6`. Its square roots in additive notation solve

\[
2q=6\pmod{12}.
\]

There are exactly two:

\[
\boxed{q=3,\qquad q=9.}
\]

Both reduce to the half-turn state `3 in C6`:

\[
r(3)=r(9)=3.
\]

Adding the kernel element `6` interchanges them, and inversion does the same:

\[
3+6=9,
\qquad
-3=9\pmod{12}.
\]

Hence the root set

\[
\mathcal J=\{3,9\}
\]

is a free transitive `C2` torsor. We denote its two character readouts by

\[
+J\quad\text{and}\quad-J.
\]

### Theorem 4.1 — no inversion-invariant signed root

There is no element of `mathcal J` fixed by inversion. Therefore the unoriented pair

\[
\boxed{\{+J,-J\}}
\]

is canonical, while a signed `J` requires one chirality choice.

This is the exact finite seed obstruction already visible at the antipodal state. Away from the antipode, the positive-longitudinal/equal-resultant theorem propagates a chosen branch uniquely; at the antipode itself, no sign-free rule distinguishes the two roots.

## 5. Four FCC slice charts and edge transition bits

Label the four overlapping three-axis slice charts by

\[
A,B,C,D.
\]

Their pairwise overlaps form the six edges of `K4`:

\[
AB,AC,AD,BC,BD,CD.
\]

Suppose each slice carries a local member of the root torsor. Encode the local choice by a vertex bit

\[
s_v\in\mathbf F_2,
\]

where `0` and `1` represent the two signs of `J`.

The comparison on an overlap is

\[
\boxed{\varepsilon_{uv}=s_u+s_v\in\mathbf F_2.}
\]

Thus a globally generated transition system is the coboundary

\[
\varepsilon=\delta s.
\]

Conversely, an arbitrary assignment of six overlap signs is a one-cochain

\[
\varepsilon\in C^1(K_4;\mathbf F_2).
\]

Changing all local representatives by vertex bits `g_v` sends

\[
\varepsilon\longmapsto\varepsilon+\delta g.
\]

This is the exact gauge action of local chirality-frame changes.

## 6. Face holonomy and the globalization theorem

Define the four triangular face holonomies

\[
\begin{aligned}
h_{ABC}&=\varepsilon_{AB}+\varepsilon_{AC}+\varepsilon_{BC},\\
h_{ABD}&=\varepsilon_{AB}+\varepsilon_{AD}+\varepsilon_{BD},\\
h_{ACD}&=\varepsilon_{AC}+\varepsilon_{AD}+\varepsilon_{CD},\\
h_{BCD}&=\varepsilon_{BC}+\varepsilon_{BD}+\varepsilon_{CD}.
\end{aligned}
\]

Every edge occurs in exactly two faces, so

\[
\boxed{h_{ABC}+h_{ABD}+h_{ACD}+h_{BCD}=0.}
\]

Only three face bits are independent.

### Theorem 6.1 — tetrahedral face-flatness criterion

For an edge sign assignment `epsilon`, the following are equivalent:

1. there exist vertex signs `s_A,s_B,s_C,s_D` with
   \[
   \varepsilon_{uv}=s_u+s_v
   \]
   on every edge;
2. all four triangular face holonomies vanish;
3. the three face holonomies adjacent to `A` vanish.

Proof. Necessity follows by cancellation around each triangle. For sufficiency set

\[
s_A=0,
\qquad
s_B=\varepsilon_{AB},
\qquad
s_C=\varepsilon_{AC},
\qquad
s_D=\varepsilon_{AD}.
\]

The equations `h_ABC=h_ABD=h_ACD=0` give

\[
\varepsilon_{BC}=s_B+s_C,
\quad
\varepsilon_{BD}=s_B+s_D,
\quad
\varepsilon_{CD}=s_C+s_D.
\]

The fourth face equation follows automatically.

Therefore

\[
\boxed{\text{GLOBAL SIGNED }J\text{ EXISTS}\iff\text{ALL FACE HOLONOMIES VANISH}.}
\]

### Theorem 6.2 — uniqueness up to overall reversal

If two vertex assignments `s` and `t` produce the same edge signs, then

\[
t_v=s_v+c
\]

for one constant bit `c`. Thus a flat transition system has exactly two global lifts, exchanged by simultaneous reversal of every local `J`.

So a coherent signed chiral generator, when it exists, is a `C2` torsor rather than a canonical point.

## 7. The graph obstruction space and minimality

On the one-skeleton alone, gauge classes are classified by three independent face holonomies:

\[
\boxed{
C^1(K_4;\mathbf F_2)/\delta C^0(K_4;\mathbf F_2)
\simeq\mathbf F_2^3.
}
\]

An explicit complete invariant is

\[
\varepsilon\longmapsto
(h_{ABC},h_{ABD},h_{ACD}).
\]

Every triple occurs. After fixing the gauge `s_A=0` and killing the three star edges `AB,AC,AD`, the remaining entries on `BC,BD,CD` are exactly these three holonomies.

Consequently three independent flatness conditions are necessary and sufficient. Two face constraints can never force globalization: one independent obstruction bit remains.

If the four triangular faces are included, the atlas becomes the filled tetrahedron `Delta^3`. Flat one-cochains on this simplex are all coboundaries:

\[
\boxed{H^1(\Delta^3;\mathbf F_2)=0.}
\]

The difference between the graph and the filled atlas is therefore exact:

- graph-only data retain `F2^3` holonomy;
- face-flat atlas data admit one global root section, unique up to global reversal.

## 8. Projective Euler descent

The two local chiral roots have the same half-turn square:

\[
(+J)^2=(-J)^2=-1.
\]

In the finite model this is simply

\[
2\cdot3=2\cdot9=6\pmod{12}.
\]

Therefore the half-period endpoint is invariant under every local chirality flip.

### Theorem 8.1 — scalar endpoint descends without a signed J

Even if an overlap cocycle has nonzero holonomy and a global signed `J` does not exist, the local half-period endpoint `-1` agrees on every overlap. Hence the projective statement

\[
\boxed{\exp(\{\pm J\}\,\pi)=-1}
\]

is well typed as a chirality-even statement.

By contrast, the odd channel changes sign:

\[
\sin_{-J}(t)=-\sin_J(t),
\]

while the even channel does not:

\[
\cos_{-J}(t)=\cos_J(t).
\]

Thus:

\[
\boxed{
\text{GLOBAL ORIENTED EULER FLOW REQUIRES FLATNESS,}
\quad
\text{BUT THE HALF-PERIOD SCALAR IDENTITY DOES NOT.}
}
\]

This explains why scalar `pi` formulas can survive a lost chirality bit. They live in the reversal-even/projective channel. Continuous scalar completion may erase the sign torsor while retaining the common period normalization.

## 9. Propagation into the Viète tower

The antipodal state `-1` has the tied root pair `+/-J`. Once one global member is chosen, the existing positive-longitudinal/equal-resultant theorem selects the non-antipodal child root uniquely at every subsequent refinement level.

Hence, at the algebraic character level, the independent branch data are not one new Boolean choice per depth. They reduce to:

1. one initial global chirality torsor at the antipodal seed;
2. the deterministic positive-longitudinal section thereafter.

Therefore the minimal global Viète obligation is:

\[
\boxed{
\text{FACE-FLAT GLOBAL }\{\pm J\}\text{ LIFT}
+
\text{ONE OVERALL CHIRALITY CHOICE}
+
\text{DEEP-STATE TYPING BRIDGE}.
}
\]

The first two are now completely classified. The remaining native gap is the third: current integer Cell/trace coordinates do not contain all deep algebraic root directions exactly.

## 10. What this resolves in the Euler geometry line

The current local-to-global hierarchy is now:

```text
six directed Cell-edge states C6
  = C3 axis family x C2 orientation reversal
        |
        | connected binary root cover
        v
C12 = C3 x C4
  with non-split C4 -> C2
        |
        | half-turn root fiber
        v
{+J,-J}, a chiral C2 torsor
        |
        | overlap comparison on four FCC slices
        v
C1(K4;F2)
        |
        | triangular face holonomy
        v
flat iff one global signed J exists
        |
        | quotient by overall reversal
        v
projective Euler structure {+J,-J}
```

This closes the minimal finite selection/gluing problem. It does not manufacture a native sign from incidence alone; rather, it proves exactly what incidence plus face-flat transport can and cannot determine.

## 11. Boundaries

This note does not claim:

- that current P000/FCC incidence data already supply the six overlap signs;
- that current native dynamics force the three independent face holonomies to vanish;
- that one of the two global signs is preferred without an ambient chirality choice;
- that the root-cover kernel is identical to the earlier tetrahedral endpoint-sum torsion class;
- that the root-cover kernel is identical to a Pell shell sign;
- that `J` is a primitive native spatial axis;
- that all six-dimensional native trajectories factor through this local atlas.

The exact remaining native theorem is now sharply stated:

> construct overlap transition signs from actual six-dimensional Cell transport and prove their three independent triangular holonomies vanish.

Everything after that flatness theorem is forced up to one overall chirality reversal, and the scalar Euler half-period identity already descends before that last sign is chosen.
