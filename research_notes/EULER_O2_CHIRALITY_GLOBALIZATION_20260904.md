# O(2) chirality globalization of the four-slice Euler structure

Status: `FREE_RESEARCH / EXACT FINITE GLOBALIZATION / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`
Author/program signature: `YUAN X / Enterprise Math`

## 1. Result in one line

The four FCC carrier slices need not admit one globally signed complex generator `J`.  Their natural coordinate-free globalization is instead an `O(2)=U(1) semidirect C2` rotation local system, where a chirality-reversing handoff acts on the phase circle by inversion/conjugation.  Nevertheless the Euler half-turn is globally canonical because

\[
(-1)^{-1}=-1,
\qquad
\exp(-J\pi_{\rm rot})=\exp(J\pi_{\rm rot})=-1.
\]

Thus a global signed `J` may be obstructed while the geometric content of Euler's identity still descends across every slice.

## 2. The four-slice overlap graph

Let

\[
V=\{A,B,C,D\}
\]

be the four three-axis FCC carrier slices and let the six shared line families be the edges of `K4`:

\[
E=\{AB,AC,AD,BC,BD,CD\}.
\]

Each slice carries a local chiral generator `J_v` satisfying

\[
J_v^2=-1.
\]

A handoff across a shared line family records whether the two local chiral frames agree or reverse.  Encode it by

\[
\varepsilon_{uv}\in\mathbf F_2,
\qquad
J_v=(-1)^{\varepsilon_{uv}}J_u
\]

after the chosen carrier identification.

Changing the sign convention in slice `v` by `sigma_v in F2` changes the edge data by

\[
\varepsilon_{uv}\longmapsto
\varepsilon_{uv}+\sigma_u+\sigma_v.
\]

Hence chirality handoffs are edge cochains modulo vertex gauge.

## 3. Exact gauge classification

Choose the three independent triangle holonomies

\[
\begin{aligned}
h_{ABC}&=\varepsilon_{AB}+\varepsilon_{AC}+\varepsilon_{BC},\\
h_{ABD}&=\varepsilon_{AB}+\varepsilon_{AD}+\varepsilon_{BD},\\
h_{ACD}&=\varepsilon_{AC}+\varepsilon_{AD}+\varepsilon_{CD}.
\end{aligned}
\]

The fourth triangle satisfies

\[
h_{BCD}=h_{ABC}+h_{ABD}+h_{ACD}.
\]

### Theorem 3.1 — complete finite classification

The map

\[
[\varepsilon]\longmapsto
(h_{ABC},h_{ABD},h_{ACD})
\]

is a bijection

\[
\boxed{
C^1(K_4;\mathbf F_2)/\delta C^0(K_4;\mathbf F_2)
\simeq
\mathbf F_2^3.
}
\]

Consequently the 64 edge-sign systems split into eight gauge classes, each containing eight representatives.

Proof.  Gauge changes cancel around every triangle, so the displayed holonomies are invariant.  Conversely, if two cochains have the same three values, their difference has zero holonomy on every triangle.  Fix `sigma_A=0` and put

\[
\sigma_B=\eta_{AB},\quad
\sigma_C=\eta_{AC},\quad
\sigma_D=\eta_{AD},
\]

where `eta` is their difference.  The three zero-holonomy equations give

\[
\eta_{BC}=\sigma_B+\sigma_C,
\quad
\eta_{BD}=\sigma_B+\sigma_D,
\quad
\eta_{CD}=\sigma_C+\sigma_D.
\]

Thus `eta=delta sigma`.  The kernel of `delta` consists of the two constant vertex assignments, so every gauge orbit has `16/2=8` representatives.

## 4. Global signed chirality and the orientation torsor

### Theorem 4.1 — trivial-holonomy criterion

A globally consistent signed generator exists exactly when all triangle holonomies vanish:

\[
\boxed{
\exists\sigma:\ \varepsilon=\delta\sigma
\iff
h_{ABC}=h_{ABD}=h_{ACD}=0.
}
\]

When it exists, the trivializing vertex assignment is unique up to the simultaneous flip

\[
\sigma_v\longmapsto\sigma_v+1
\qquad(v\in V).
\]

Therefore global signed chirality is naturally a two-element torsor, not a preferred sign.

### Theorem 4.2 — no canonical full-`S4` sign choice

The two orientations of the tetrahedron are exchanged by every odd permutation and preserved by every even permutation.  Hence bare unoriented `K4` incidence admits no `S4`-invariant choice of global chirality.  A choice is `A4`-equivariant and is unique up to global reversal.

This is a symmetry obstruction, not missing numerical information.  A canonical signed `J` requires orientation data.  Without that choice the correct symmetry type contains reflections.

## 5. The finite `O(2)` semidirect product

At a finite rotation resolution `C_N`, define

\[
O_N=C_N\rtimes C_2
\]

with multiplication

\[
(a,e)(b,f)
=
\bigl(a+(-1)^e b,\ e+f\bigr).
\]

The nontrivial `C2` element acts on rotations by inversion.  In the continuous completion this becomes

\[
U(1)\rtimes C_2\simeq O(2),
\qquad
z\longmapsto z^{-1}=\overline z.
\]

The fixed phases of inversion in even `C_N` are exactly

\[
\boxed{0\quad\text{and}\quad N/2.}
\]

Equivalently, on `U(1)` the only inversion-fixed phases are

\[
\boxed{+1\quad\text{and}\quad-1.}
\]

The half-turn is therefore central in every `O_N` and in `O(2)`.

## 6. Orientation-independent Euler descent

In slice `v`, let

\[
E_v(t)=\exp(tJ_v).
\]

Across a handoff with sign `epsilon_uv`,

\[
E_v(t)
=
\begin{cases}
E_u(t),&\varepsilon_{uv}=0,\\
E_u(-t)=E_u(t)^{-1}=\overline{E_u(t)},&\varepsilon_{uv}=1.
\end{cases}
\]

For a generic phase, a chirality reversal changes the state.  At the internally constructed half-period, however,

\[
E_u(\pi_{\rm rot})=-1
\]

and inversion fixes `-1`.  Hence

\[
\boxed{
E_v(\pi_{\rm rot})=-1
\quad\text{for every slice }v,
}
\]

independently of every edge sign and every gauge choice.

### Theorem 6.1 — global Euler half-turn theorem

Every `C2`-twisted four-slice rotation local system has canonical global identity and half-turn sections.  Its local generators may fail to glue, but the Euler endpoint does glue:

\[
\boxed{
\exp(J_v\pi_{\rm rot})+1=0
\quad\text{in every chart, compatibly on every handoff.}
}
\]

After the already established equivalence `pi_rot=pi`, this is the ordinary Euler identity in every slice.

### Corollary 6.2 — maximality

At finite even resolution and in the completed circle, no phase other than the identity and half-turn is invariant under all chirality reversals.  Therefore Euler's endpoint is not merely one convenient global phase; it is one of the two maximal orientation-forgetting phase states.

## 7. What the formula means globally

The local dictionary is

\[
J_v=\text{Cell-radius-normalized local chiral turn},
\]

while the global dictionary is

\[
\begin{aligned}
U(1)&=\text{oriented rotation transport after a chirality choice},\\
O(2)&=\text{rotation transport before choosing global chirality},\\
-1&=\text{orientation reversal, fixed by complex conjugation},\\
\pi_{\rm rot}&=\text{the intrinsic half-period of the dyadic root completion}.
\end{aligned}
\]

Thus the geometric content of

\[
e^{i\pi}+1=0
\]

is stronger than the existence of one globally oriented complex plane:

> even when local notions of clockwise and counterclockwise are twisted from slice to slice, one completed half-turn is unambiguously the same line-segment reversal in every chart.

## 8. Native-globalization consequence

The remaining six-dimensional lift problem is now weaker and sharper.

It is **not** necessary to derive a preferred global sign of `J` from bare FCC incidence.  That is impossible under full `S4` symmetry without orientation data.  It is enough to derive:

1. a local `J_v` in each admissible slice;
2. a `C2` handoff on every shared line family;
3. the `O(2)` cocycle/transport law.

A reduction from `O(2)` to `U(1)` exists exactly when the chirality holonomy class is trivial.  Regardless of that reduction, the global Euler half-turn survives.

This isolates two separate claims:

\[
\boxed{
\text{GLOBAL EULER HALF-TURN}
\quad\text{does not require}\quad
\text{GLOBAL SIGNED }J.
}
\]

and

\[
\boxed{
\text{GLOBAL PHASE ORIENTATION}
\quad\text{requires a trivial chirality class or an orientation choice.}
}
\]

## 9. Boundaries

Proved here at the finite carrier/gauge level:

- complete `F2^3` gauge classification;
- exact criterion and twofold ambiguity for a global signed generator;
- the `O_N` semidirect-product law;
- inversion-fixed identity and half-turn phases;
- orientation-independent descent of the Euler half-turn;
- impossibility of a full-`S4`-invariant sign choice from unoriented tetrahedral incidence.

Not proved here:

- that P000 native six-dimensional dynamics supplies a specific edge cochain;
- that all physically admissible handoffs obey one chosen flatness law;
- that the local carrier `J_v` is a primitive native spatial axis;
- that the chirality class equals the tetrahedral residual torsion or a Pell-shell sign.

The new conclusion is exact even with these boundaries: a twisted `O(2)` globalization is sufficient for Euler's identity, while a global `U(1)` orientation is extra structure.