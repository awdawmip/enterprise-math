# Viète gate refinement as a profinite precision space and a character-dual radical tower

Status: `FREE_RESEARCH / EXACT FINITE-GROUP LIMIT CLASSIFICATION + G1 CHARACTER INTERPRETATION / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`

## 1. Question

After selecting the connected binary cycle covers

\[
C_3\leftarrow C_6\leftarrow C_{12}\leftarrow C_{24}\leftarrow\cdots,
\]

what is the actual infinite-resolution object before any continuous circle is introduced?

The answer has two distinct sides:

1. an inverse-limit **precision-address space**;
2. a direct-limit **finite-character space**.

They are algebraically dual but must not be confused with each other or with a classical continuous circle.

## 2. The coherent gate tower

For `m>=0`, define

\[
G_m:=\mathbf Z/(3\cdot2^m)\mathbf Z.
\]

Thus

\[
G_0=C_3,
\quad G_1=C_6,
\quad G_2=C_{12},\ldots
\]

Use the natural coarse-graining maps

\[
\pi_m:G_{m+1}\to G_m,
\qquad
\pi_m([k]_{3\cdot2^{m+1}})=[k]_{3\cdot2^m}.
\]

Each `pi_m` is a connected two-fold cyclic cover at the graph/group level once the nontrivial `C2` holonomy class has been selected.

A coherent infinite-precision gate address is a sequence

\[
x=(x_0,x_1,x_2,\ldots)
\]

with

\[
\pi_m(x_{m+1})=x_m
\]

at every level.

Define

\[
G_\infty^{\rm prec}:=\varprojlim_m G_m.
\]

## 3. Exact inverse-limit classification

Because `3` and `2^m` are coprime, the Chinese remainder theorem gives compatible isomorphisms

\[
\mathbf Z/(3\cdot2^m)\mathbf Z
\cong
\mathbf Z/3\mathbf Z\times\mathbf Z/2^m\mathbf Z.
\]

The first factor is constant under refinement, while the second forms the usual inverse system defining the 2-adic integers.

Therefore

\[
\boxed{
G_\infty^{\rm prec}
\cong
C_3\times\mathbf Z_2.
}
\]

This is a compact totally disconnected profinite group.

No real angle, circle, sine, cosine, or classical pi is needed to define it.

Freeze:

`INFINITE_GATE_PRECISION_ADDRESS_SPACE = C3 x Z_2`.

`INFINITE_GATE_PRECISION_ADDRESS_SPACE != CONTINUOUS_CIRCLE`.

The result is standard inverse-limit group mathematics; no historical novelty is claimed. The Enterprise-specific content is its role as the exact precision carrier selected by the #1158 binary gate architecture.

## 4. Finite precision means projection, not approximation by a real angle

For

\[
x\in G_\infty^{\rm prec},
\]

its resolution-`m` state is simply

\[
x_m=\operatorname{pr}_m(x)\in G_m.
\]

Thus increasing precision means retaining one more compatible binary residue coordinate. It is an information refinement inside a discrete inverse system.

This makes precise the slogan

`PRECISION_IS_PART_OF_STATE`:

one infinite-precision object is represented by a coherent family of finite states, and a finite precision state is a quotient/projection of that family.

Nothing in this statement requires replacing the finite groups by a continuum.

## 5. Character side: direct limit of finite rotation characters

For each finite cyclic gate group, its one-dimensional character group is cyclic of the same order. Write

\[
G_m^\vee\cong\mu_{3\cdot2^m},
\]

where `mu_N` denotes the abstract group of `N`-th roots of unity in an algebraic character realization.

Pullback along

\[
\pi_m:G_{m+1}\to G_m
\]

injects character groups:

\[
\pi_m^*:G_m^\vee\hookrightarrow G_{m+1}^\vee.
\]

Hence the finite character tower has direct limit

\[
G_\infty^{\rm char}
:=
\varinjlim_m G_m^\vee.
\]

Since the 3-primary factor is constant and the 2-primary roots exhaust the Prüfer 2-group,

\[
\boxed{
G_\infty^{\rm char}
\cong
C_3\times C_{2^\infty}.
}
\]

Here `C_{2^infty}` is the Prüfer 2-group.

This is the continuous-character dual of the profinite group `C3 x Z_2`.

Freeze:

`PRECISION_ADDRESS_INVERSE_LIMIT = C3 x Z_2`.

`FINITE_CHARACTER_DIRECT_LIMIT = C3 x C_{2^infty}`.

`ADDRESS_SPACE != CHARACTER_SPACE`.

## 6. The character direct limit is still not a continuous circle

The direct limit

\[
C_3\times C_{2^\infty}
\]

is countable and torsion. It is not `U(1)` as an abstract group or as a topological space.

Only after choosing the classical complex character realization does this countable roots-of-unity subgroup sit densely in the classical unit circle. Taking its ordinary topological closure is then a later analytic completion:

\[
\overline{C_{2^\infty}}^{\,\text{classical topology}}=U(1).
\]

Thus the logical order is

```text
finite cyclic gate states
    -> profinite coherent precision addresses
    -> finite algebraic character direct limit
    -> optional classical topological closure
    -> U(1)
```

not

```text
continuous circle first
    -> sample finitely many angles afterward.
```

This gives a precise discrete-to-continuous boundary for the Euler/Viète program.

## 7. The two Viète root sheets are coherent profinite points

At level `m=1`, `G_1=C_6` has the half-turn state

\[
h_1=[3]_6.
\]

Its two quarter-turn lifts in `G_2=C_{12}` are

\[
[3]_{12},\qquad[-3]_{12}=[9]_{12}.
\]

Continue each by the normalized shortest-root section. This gives two coherent inverse-limit points

\[
q_+=(q_{+,m})_{m\ge1},
\qquad
q_-=(q_{-,m})_{m\ge1}
\]

with

\[
q_{+,m}=[3]_{3\cdot2^m},
\]

and

\[
q_{-,m}=[-3]_{3\cdot2^m}.
\]

They coincide at the coarse half-turn level `m=1` because `3=-3 mod 6`, but split at every finer level.

Under

\[
G_\infty^{\rm prec}\cong C_3\times\mathbf Z_2,
\]

they are exactly

\[
\boxed{q_+=(0,3),\qquad q_-=(0,-3).}
\]

Inversion exchanges them.

Therefore the oriented Viète double sheet is naturally visible in the profinite precision carrier without assigning an absolute chirality sign.

## 8. Exact normalized gate distance along the Viète sheets

At level `m>=1`, the cycle has

\[
|G_m|=3\cdot2^m
\]

states and

\[
d_{G_m}(q_{\pm,m},0)=3.
\]

Hence the normalized Cayley distance is

\[
\boxed{
\theta_m(q_\pm)
=
\frac{3}{3\cdot2^m}
=
2^{-m}.
}
\]

Thus every binary precision lift halves the normalized rotation distance exactly.

This is the graph-theoretic half-angle law already proved at finite level, now seen as the finite projection of one coherent profinite address.

## 9. Native/profinite convergence and geometric/readout convergence are different

A subtle but important point follows.

The coherent point

\[
q_+=(0,3)\in C_3\times\mathbf Z_2
\]

is not approaching the identity in the profinite/2-adic topology as `m` increases. It is one fixed nonzero profinite state.

In particular `3` is a 2-adic unit:

\[
|3|_2=1.
\]

Yet its normalized finite-cycle distance satisfies

\[
\theta_m(q_+)\to0.
\]

Therefore

\[
\boxed{
\text{FINE ROTATION READOUT TENDS TO IDENTITY}
\neq
\text{NATIVE PROFINITE STATE CONVERGES TO IDENTITY}.
}
\]

The shrinking-angle picture belongs to the finite metric/character readout across changing resolutions; it is not convergence of the underlying precision address in its own native topology.

This sharply separates state ontology from analytic phase interpretation.

## 10. Viète radicals as real half-traces of the character-dual tower

Choose compatible primitive character generators

\[
\xi_m\in\mu_{3\cdot2^m}
\]

such that

\[
\xi_{m+1}^2=\xi_m.
\]

Evaluate the positive Viète profinite sheet:

\[
u_m:=\chi_m(q_{+,m})=\xi_m^3.
\]

Then `u_m` has exact order `2^m`, and

\[
\boxed{u_{m+1}^2=u_m.}
\]

The negative sheet gives

\[
u_m^{-1}.
\]

Define the inversion-even half-trace

\[
c_m:=\frac{u_m+u_m^{-1}}2.
\]

Then purely algebraically

\[
\begin{aligned}
c_{m+1}^2
&=\frac{u_{m+1}^2+2+u_{m+1}^{-2}}4\\
&=\frac{u_m+2+u_m^{-1}}4\\
&=\frac{1+c_m}{2}.
\end{aligned}
\]

Thus

\[
\boxed{
c_{m+1}=\sqrt{\frac{1+c_m}{2}}
}
\]

for the positive-longitudinal branch.

At the key levels:

- `m=1`: `u_1=-1`, half-turn;
- `m=2`: `u_2` is an order-four marker, so `c_2=0`;
- `m=3`: `c_3=sqrt(2)/2`;
- later levels produce the full Viète nested-radical chain.

Hence the strongest algebraic interpretation is

\[
\boxed{
\text{VIETE NESTED RADICALS}
=
\text{INVERSION-EVEN REAL HALF-TRACES OF THE CHARACTER DUAL OF THE BINARY GATE COVER TOWER}.
}
\]

No continuous circle is needed for this statement.

## 11. Scalar/oriented split becomes duality-theoretic

The two profinite sheets `q_+` and `q_-` are distinct and exchanged by inversion.

On the character side they give `u_m` and `u_m^{-1}`.

The scalar Viète factor is their inversion-even half-trace:

\[
c_m=\frac{u_m+u_m^{-1}}2.
\]

The signed transverse coordinate is inversion-odd.

Thus the earlier observer-relative statement gains a clean structural form:

- oriented precision lives on the two-sheeted profinite state / full character;
- scalar Viète precision lives on the inversion quotient / even character trace.

This is exactly why the scalar product is insensitive to the global chirality gauge.

## 12. Relation to the completion constant

The finite scalar readouts `Pi_m` constructed from the half-trace/transverse character data have already been proved to admit a target-free nested interval completion

\[
\Pi_{\rm rot}
\]

and independently to satisfy

\[
\Pi_{\rm rot}=\tau=2W_\infty
\]

with the Wallis rotation-completion constant.

The present theorem changes the interpretation of the input to that completion:

`Pi_rot` is not obtained by first postulating a continuous phase. It is a scalar completion readout of a countable character-dual tower whose native precision address space is profinite.

## 13. Current native boundary

This note assumes the connected binary cycle-cover tower as the finite orientation architecture. The parent no-go shows that current local Cell semantics does not itself select the effective nontrivial holonomy required to obtain that tower.

Therefore:

- the inverse/direct-limit classifications are exact once the cover tower is declared;
- the Viète character/radical interpretation is exact at G1 finite-algebraic strength;
- the emergence of `U(1)` remains an optional classical topological completion;
- native G0 still owes the selection/effectivity theorem for the nontrivial cover class.

The result does not identify `Z_2` with a spatial axis, a physical continuum, or the time dimension. `Z_2` is a precision-address factor of this specific binary orientation-cover architecture.
