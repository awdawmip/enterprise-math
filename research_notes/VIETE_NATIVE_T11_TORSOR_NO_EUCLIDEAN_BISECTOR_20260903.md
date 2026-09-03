# Viète native T11 seed: no Euclidean-bisector leakage, a two-path torsor, and a branch-free scalar shell circuit

Status: `FREE_RESEARCH / EXACT CURRENT-SEMANTICS SEED AND NO-GO + G1 SCALAR CIRCUIT / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Depends on:
- `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`
- `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md`
- `definitions/ENTERPRISE_PATH_VALUED_SQUARE_ROOT_OPERATOR_20260821.md`
- `research_notes/VIETE_SEGMENT_BISECTOR_ROTATION_PRECISION_20260903.md`
- `research_notes/VIETE_ORIENTATION_TORSOR_BRANCH_COVER_CELL_MEMORY_20260903.md`
- `research_notes/VIETE_ENTERPRISE_J_TRACE_PELL_PRECISION_20260903.md`

## 1. The word “bisector” needs a type correction

The prior normalized-resultant theorem used

\[
B(v)=\frac{e+v}{\|e+v\|}
\]

and called this a normalized segment bisector. That name is harmless inside the rebuilt Enterprise algebraic orientation readout, but it must not be read as the Euclidean angular bisector of the classical FCC/triangular carrier drawing.

Current Foundation explicitly separates these two geometries.

Inside one native right sector, the two active positive Enterprise components are orthogonal in the Enterprise sense and satisfy

\[
L_E(a,b)^2=a^2+b^2.
\]

Therefore the equal-component native trace has

\[
L_E(T_{1,1})=\sqrt2.
\]

By contrast, choose chart-local classical carrier representatives of the same two line families with Euclidean angle `120 degrees`. At the carrier presentation layer their equal unit vectors satisfy

\[
e_i+e_j=-e_k
\]

for the third oriented carrier direction, and their Euclidean resultant has length `1`.

These are deliberately different statements:

\[
\boxed{
\|e_i+e_j\|_{\rm carrier}=1,
\qquad
\|(1,1)\|_E=\sqrt2.
}
\]

Current native line theory also classifies the reverse-third-family shortcut to the same carrier endpoint as

`CARRIER_ONLY_SHORTCUT_NOT_NATIVE_LINE`.

Hence the Viète refinement cannot be using the classical 120-degree carrier-vector sum as its native square-root mechanism. If it did, the first equal-component state would collapse to the reverse third carrier direction instead of the native trace `T_11`.

Freeze:

`VIETE_NORMALIZED_EQUAL_RESULTANT != CARRIER_EUCLIDEAN_ANGLE_BISECTOR`.

`CARRIER_SUM_ZERO_RELATION != NATIVE_HALF_ANGLE_LAW`.

A safer name is **Enterprise normalized equal-resultant root**.

## 2. First Viète state is an exact native trace, not a carrier shortcut

The existing Enterprise `J` carrier has

\[
J^2=-1,
\qquad
N_E(a+bJ)=a^2+b^2.
\]

The first normalized root of the quarter-turn marker is

\[
B_E(J)=\frac{1+J}{\sqrt2}.
\]

The exact native line trace

\[
T_{1,1}^{(ij)}=[X_iX_j]
\]

has the same normalized Enterprise component readout

\[
\operatorname{NormTrace}(T_{1,1})=\frac{(1,1)}{\sqrt2}.
\]

Thus the first Viète factor `sqrt(2)/2` is internally anchored by a current native trace while simultaneously being *different* from the classical carrier Euclidean resultant of the two 120-degree presentation directions.

This is an exact anti-leakage witness: the same visible carrier pair produces a carrier resultant of length `1` and a native Enterprise equal-component trace of length `sqrt(2)`. The Viète mechanism follows the latter.

## 3. The native T11 realization fiber is already a free C2 torsor

Current native trace semantics gives exactly

\[
\operatorname{Realize}_E(T_{1,1})
=
\{p,q\}
\]

with

\[
p=\Sigma;X_iX_j,
\qquad
q=\Sigma;X_jX_i.
\]

Define the purely combinatorial order-swap involution

\[
\tau(p)=q,
\qquad
\tau(q)=p.
\]

Then

\[
\tau^2=\mathrm{id}
\]

and `tau` has no fixed point. Therefore the two-path realization fiber is a free `C2` torsor.

This statement does **not** identify order swap with native endpoint reversal, physical chirality, or carrier reflection. It only records an exact symmetry of this two-element path fiber.

## 4. The quarter-turn root pair is another free C2 torsor

At the finite orientation-readout layer the half-turn root relation is

\[
Q(h)=\{q_+,q_-\},
\]

and turn-sense reversal `S` exchanges the two roots:

\[
S(q_+)=q_-,
\qquad
S(q_-)=q_+.
\]

Thus `Q(h)` is also a free `C2` torsor.

Between any two free transitive `C2` torsors of cardinality two there are exactly two equivariant bijections. Here one may send

\[
p\mapsto q_+,
\quad q\mapsto q_-
\]

or

\[
p\mapsto q_-,
\quad q\mapsto q_+.
\]

No third equivariant bijection exists, and neither of the two is selected by torsor structure alone.

Therefore the current native `T_11` fiber has **exactly the correct two-branch torsor shape** to host the two quarter-turn root sheets, but it does not canonically label which native path is `+` and which is `-`.

Freeze:

`T11_PATH_FIBER_COMPATIBLE_WITH_QUARTER_ROOT_TORSOR = true`.

`T11_PATH_TO_CHIRALITY_LABEL = NONCANONICAL_WITHOUT_EXTRA_ODD_DATA`.

This is a structural bridge, not yet a physical identification theorem.

## 5. Scalar Viète seed is independent of the missing torsor labeling

Let `O` be any observer on the quarter-turn root pair satisfying

\[
O(Sx)=O(x).
\]

Both equivariant bijections from the native `T_11` path torsor to `Q(h)` give the same observed value because they differ only by `S`.

The scalar Viète observers are precisely of this kind:

- longitudinal coordinate `c`;
- absolute transverse coordinate `|s|`;
- product factor;
- scalar precision readout `Pi_n`.

Hence the absence of a canonical `p/q -> +/-` chirality labeling is **not a scalar Viète obstruction**.

It matters only if one asks for a single oriented lift.

This sharpens the previous branch-preservation result at native strength:

\[
\boxed{
\text{current }T_{1,1}\text{ already supplies an exact two-branch native carrier sufficient for every }S\text{-even scalar seed observer.}
}
\]

No extra binary variable is required merely to retain the two seed branches; the existing path fiber already contains the binary distinction. An extra odd datum is required only to *name* one branch as a preferred chirality.

## 6. Branch-free scalar shell circuit

The full oriented pair can be quotiented by `S` before scalar precision evaluation.

Use the positive scaled coordinates

\[
r_n=2c_n,
\qquad
h_n=2|s_n|.
\]

Start at the quarter-turn scalar shell

\[
r_0=0,
\qquad
h_0=2.
\]

The normalized equal-resultant refinement gives

\[
\boxed{
r_{n+1}=\sqrt{2+r_n}}
\]

and

\[
\boxed{
h_{n+1}=\sqrt{2-r_n}}.
\]

These satisfy the branch-free shell identity

\[
\boxed{r_{n+1}^2+h_{n+1}^2=4}.
\]

Moreover

\[
(2+r_n)(2-r_n)=4-r_n^2=h_n^2,
\]

so, taking positive roots,

\[
\boxed{r_{n+1}h_{n+1}=h_n.}
\]

Thus the scalar Viète circuit is the deterministic positive recurrence

```text
(r_0,h_0)=(0,2)
(r_{n+1},h_{n+1})=(sqrt(2+r_n), sqrt(2-r_n))
h_n=r_{n+1} h_{n+1}
Pi_n=2^n h_n
```

with no chirality choice at all.

The two oriented sheets are a lift of this scalar circuit rather than an input needed to define the scalar circuit.

## 7. Exact telescoping in shell variables

From

\[
h_n=r_{n+1}h_{n+1}
\]

one gets

\[
\prod_{k=1}^{n}r_k=\frac{h_0}{h_n}=\frac2{h_n}.
\]

Therefore

\[
\prod_{k=1}^{n}\frac{r_k}{2}
=
\frac{1}{2^{n-1}h_n}
\]

and the standard finite scalar readout is

\[
\boxed{
\Pi_n=2^n h_n
}
\]

when `n` counts from the quarter-turn shell `n=0`.

This is the same quantity as the previously indexed formula `2^{n+1}|s_n|`; here `h_n=2|s_n|`.

## 8. Precision defect can be stored as shell state

The longitudinal defect from the target-free completion note is

\[
d_n=1-c_n=1-\frac{r_n}{2}.
\]

Thus the intrinsic completion bracket

\[
\Pi_n\le\Pi_{\rm rot}\le\frac{\Pi_n}{1-4d_{n+1}}
\]

can be written entirely in terms of the current positive shell state `(r_n,h_n,r_{n+1})`.

So at scalar G1 strength the finite state already contains:

- current precision readout `Pi_n`;
- unresolved orientation defect through `2-r_{n+1}`;
- a target-free upper certificate for the completion constant.

No oriented branch label is required for this precision interval.

## 9. What is now genuinely native and what remains a bridge

Exact current-native facts used here:

1. sector-local Enterprise Pythagorean norm;
2. native line `T_11` and its length `sqrt(2)`;
3. exact two-path realization fiber `{XiXj,XjXi}`;
4. carrier reverse-third shortcut is not the same native line;
5. the canonical algebraic `J` component marker exists at G1.

Exact new deductions:

1. the Viète equal-resultant root is not the Euclidean carrier bisector;
2. `T_11` supplies the exact first normalized Viète trace state;
3. its two-path fiber and the quarter-root pair are isomorphic free `C2` torsors;
4. there are exactly two equivariant identifications and no canonical chirality label from torsor structure alone;
5. every `S`-even scalar Viète observer is independent of this noncanonical labeling;
6. the scalar tower admits a deterministic branch-free `(r,h)` shell circuit.

Still unproved:

- that native path order is physical turn chirality;
- that actual Cell rotation dynamics maps the `T_11` path torsor to the quarter-root torsor;
- that deeper algebraic shell states are native Cell/trace states rather than G1 readouts;
- a native six-dimensional lift.

## 10. Revised native frontier

The first seed no longer needs an invented binary carrier: current native line theory already provides a two-path torsor of exactly the required size and symmetry.

The remaining bridge question is narrower:

\[
\boxed{
\text{Does actual Cell/trace rotation make the }T_{1,1}\text{ order-swap torsor intertwine with turn-sense reversal on the two orientation-root sheets?}
}
\]

A positive theorem would canonically connect the existing native multipath fiber to the oriented Viète lift up to the unavoidable global chirality relabeling. A negative theorem would show that the two-path coincidence is merely structural and that a different native orientation carrier is required.
