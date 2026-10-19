# Native-atlas orientation obstruction for the Euler generator

Status: `FREE_RESEARCH / EXACT GRAPH-GAUGE THEOREM / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`
Author/program signature: `YUAN X / Enterprise Math`

## 1. From six independent signs to one obstruction class

The abstract four-slice incidence graph is `K4`. Suppose a future native six-dimensional atlas assigns to every oriented overlap `u -> v` a tetrahedral chart transition

\[
g_{uv}\in S_4,
\qquad
g_{vu}=g_{uv}^{-1}.
\]

A local Euler generator changes under this transition by the parity character

\[
\varepsilon_{uv}
=\operatorname{sgn}(g_{uv})\in C_2.
\]

Changing the local chart frame at a vertex by `h_u in S4` changes the overlap parity by

\[
\varepsilon_{uv}
\longmapsto
\varepsilon_{uv}
+\operatorname{sgn}(h_u)
+\operatorname{sgn}(h_v)
\pmod2.
\]

Thus the six overlap bits are not six observables. They are one `C2`-valued 1-cochain modulo vertex gauge. Its gauge-invariant content is the first orientation class

\[
\boxed{
w_1=[\varepsilon]\in H^1(K_4;\mathbf F_2)
\cong\mathbf F_2^3.
}
\]

This identifies the previously computed `F2^3` sign space: it is the possible **orientation obstruction** of a native four-chart atlas before geometric flatness is established.

## 2. Three triangle tests

Order the six edges as

\[
01,02,03,12,13,23.
\]

The three independent triangle holonomies may be taken as

\[
\begin{aligned}
h_{012}&=\varepsilon_{01}+\varepsilon_{12}+\varepsilon_{02},\\
h_{013}&=\varepsilon_{01}+\varepsilon_{13}+\varepsilon_{03},\\
h_{023}&=\varepsilon_{02}+\varepsilon_{23}+\varepsilon_{03}.
\end{aligned}
\]

They are invariant under every vertex-frame change and form complete coordinates on `H1(K4,F2)`.

### Theorem 2.1 — orientation reduction criterion

The following are equivalent:

1. `w1=0`;
2. all three independent triangle parities vanish;
3. every cycle has even transition parity;
4. there exist vertex frame parities `a_u` such that
   \[
   \varepsilon_{uv}=a_u+a_v;
   \]
5. after a vertex gauge transformation, every overlap transition lies in `A4`;
6. the slice-local Euler generators admit one globally coherent sign.

Proof is constructive. Put

\[
a_0=0,\qquad
a_1=\varepsilon_{01},\qquad
a_2=\varepsilon_{02},\qquad
a_3=\varepsilon_{03}.
\]

This kills the three edges adjacent to vertex zero. The three triangle equations then kill the remaining edges `12,13,23`.

## 3. Uniqueness

On a connected graph, two gauges that make all overlap parities even differ by one global constant bit. Hence the coherent family is unique up to simultaneous reversal

\[
J_u\longmapsto-J_u
\quad\text{for every slice }u.
\]

This is exactly the expected ambiguity in choosing ambient chirality.

## 4. Concrete FCC carrier

For the regular tetrahedral normal realization, transitions can be chosen inside the ambient orientation-preserving group

\[
A_4\subset SO(3).
\]

Therefore every concrete carrier transition has parity zero and

\[
\boxed{w_1^{\rm FCC}=0.}
\]

The four local operators `J_u` consequently globalize as one `A4`-equivariant family. The full `S4` symmetry still acts by the orientation character: an odd ambient symmetry flips the whole family.

This reconciles two earlier statements:

- abstractly, an unstructured `K4` overlap system can carry eight distinct orientation classes;
- concretely, the oriented FCC tetrahedral carrier occupies the trivial class.

## 5. What the native six-dimensional theorem must now prove

The unresolved P000 problem has been reduced to a precise checklist.

A native globalization theorem must construct:

1. four native slice charts whose incidence reads out the current `K4` carrier;
2. overlap transports `g_uv` satisfying the groupoid inverse and composition laws;
3. a parity map from those transports to the tetrahedral sign representation;
4. vanishing of the three triangle parity holonomies.

Once these four items hold, no further `C2` obstruction remains: the local Cell-normalized Euler generators glue uniquely up to one global sign.

If one triangle parity is nonzero, then no global signed `J` exists. In that case the correct object is a twisted Euler character valued in the orientation line, not an ordinary globally signed complex character.

## 6. Relation to full frame holonomy

Vanishing `w1` removes only the chirality obstruction. It does not force the full overlap product to be the identity. In the concrete tetrahedral carrier a closed orientation-preserving transport can end in the local stabilizer

\[
C_3=\langle R_u\rangle.
\]

Because `C3` commutes with `J_u`, this residual frame holonomy is invisible to the sign class. Therefore the native hierarchy is

\[
\boxed{
S_4\text{ frame transport}
\longrightarrow
C_2\text{ orientation obstruction}
\longrightarrow
J\text{-gluing}.
}
\]

The first arrow forgets `C3` frame phase; the second asks only whether chirality can be globally chosen.

## 7. Research consequence

The former open question

> which six edge signs should be chosen?

is replaced by the sharper question

> does native P000 transport reduce the four-slice structure group from `S4` to `A4`?

At carrier level the answer is yes. At full native six-dimensional level this remains the exact unresolved lift.
