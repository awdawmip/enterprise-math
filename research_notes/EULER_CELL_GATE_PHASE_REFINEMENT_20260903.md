# Euler rotation character: Cell-gate square root, dyadic phase precision, and the rotation derivative of pi

Status: `FREE_RESEARCH / STRONG FINITE THEOREM CORE / CANDIDATE / NOT FOUNDATION`  
Date: `2026-09-03`  
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`  
Author/program signature: `YUAN X / Enterprise Math`

## 1. Result

The first missing square root in the Enterprise Euler line can be obtained from the
current Cell carrier without importing a classical angle.

Fix one Cell as a pivot. Its six nearest-neighbor Cells form a cyclic coarse
orientation shell `C6`. Between every consecutive pair of neighbor states there is
one triple-intersection gate incident to the pivot Cell. Interleaving the six Cell
states and the six gate events gives a canonical oriented `C12` transition-phase
carrier

\[
N_0,G_0,N_1,G_1,\ldots,N_5,G_5.
\]

If `Q` is its successor and `R` is the coarse neighbor successor, then

\[
Q^2|_{\{N_k\}}=R,\qquad Q^{12}=1.
\]

Moreover,

\[
Q^4=\text{the carrier readout of one }120^\circ\text{ native-sector turn},
\]

\[
Q^6=\text{the based orientation reversal},
\]

and

\[
I:=Q^3,\qquad I^2=Q^6.
\]

Thus the first exact quarter-turn operator exists at the gate-refined level, not at
the Cell-only `C6` level. In the classical carrier drawing, `Q^3 N_0` is the upper
triple gate of the pivot Cell, but the type-safe statement is

\[
\chi(Q^3)=i,
\]

not “the gate is ontologically the complex number \(i\).”

The deeper dyadic tower is obtained by repeatedly subdividing every oriented phase
transition. The first subdivision is geometrically realized by existing Cell gates;
later subdivisions are formal transition-phase refinements unless further native
geometry is supplied.

This produces an exact discrete Euler/Viète chain:

\[
\text{Cell orientation}
\to
\text{gate phase}
\to
\text{dyadic phase digits}
\to
\text{finite rotation characters}
\to
\text{Archimedean phase completion}.
\]

## 2. Frozen type boundaries

The current foundation distinguishes:

- one Cell as the instantaneous state of a rotating trajectory;
- a triple boundary intersection as a transition/incidence event;
- a native directed line trace from its carrier endpoint;
- the canonical reverse trace from the groupoid inverse of the forward trace;
- the native directed line gauge from any carrier Euclidean metric.

This note preserves those distinctions.

The refined carrier contains two types:

\[
\mathcal O_1(C)
=
\{\text{neighbor-Cell orientation states}\}
\sqcup
\{\text{gate transition phases}\}.
\]

A gate is not promoted to a native Cell state. `Q` is a typed phase successor that
alternates `Cell -> gate -> Cell`; only `Q^2` is a Cell-to-Cell coarse rotation.

Freeze:

`GATE_PHASE_EVENT != NATIVE_CELL_STATE`.

`ROTATION_PHASE_DISTANCE != NATIVE_LINE_GAUGE`.

`CARRIER_DIRECTION_CHARACTER != NATIVE_METRIC_IDENTITY`.

## 3. Exact pivot-star carrier certificate

Use triangular axial coordinates with carrier quadratic form

\[
q(a,b)=a^2+ab+b^2.
\]

This quadratic form is used only to certify the selected classical carrier. It is
not the frozen Enterprise native line metric.

Around a pivot center \(0\), enumerate the six nearest neighbors by

\[
\begin{aligned}
n_0&=(1,0),&
n_1&=(0,1),&
n_2&=(-1,1),\\
n_3&=(-1,0),&
n_4&=(0,-1),&
n_5&=(1,-1).
\end{aligned}
\]

For every \(k\in\mathbf Z/6\mathbf Z\), define

\[
g_k=\frac{n_k+n_{k+1}}3.
\]

Direct calculation gives

\[
q(g_k)
=
q(g_k-n_k)
=
q(g_k-n_{k+1})
=
\frac13.
\]

Since the Cell radius is \(1/\sqrt3\), \(g_k\) is the common boundary point of the
pivot Cell and the two consecutive neighbor Cells. The three centers are
non-collinear, so this common equidistant point is unique. Hence each coarse
orientation interval \(N_k\to N_{k+1}\) has exactly one pivot-incident gate \(G_k\).

The six gate coordinates are

\[
\left(\frac13,\frac13\right),
\left(-\frac13,\frac23\right),
\left(-\frac23,\frac13\right),
\left(-\frac13,-\frac13\right),
\left(\frac13,-\frac23\right),
\left(\frac23,-\frac13\right).
\]

## 4. The gate-square-root theorem

Define the coarse successor

\[
R(N_k)=N_{k+1}
\]

and the refined typed successor

\[
Q(N_k)=G_k,\qquad
Q(G_k)=N_{k+1}.
\]

Then

\[
Q^2(N_k)=N_{k+1}=R(N_k)
\]

and

\[
Q^2(G_k)=G_{k+1}.
\]

Therefore \(Q\) is a 12-cycle and \(Q^2\) is the six-state coarse rotation on both
type layers.

Taking \(N_0\) as reference:

\[
Q^3N_0=G_1,
\qquad
Q^4N_0=N_2,
\qquad
Q^6N_0=N_3,
\qquad
Q^{12}N_0=N_0.
\]

The carrier embedding

\[
\Phi(a,b)
=
\left(a+\frac b2,\frac{\sqrt3}2b\right)
\]

sends

\[
g_1=\left(-\frac13,\frac23\right)
\]

to

\[
\Phi(g_1)=\left(0,\frac1{\sqrt3}\right),
\]

the upper boundary gate of the pivot Cell. Thus the standard carrier character
places \(Q^3\) at the classical quarter-turn direction. Again, this is a carrier
readout, not a redefinition of the native \(120^\circ\) right angle.

## 5. Minimality and the exact location of \(i\)

In a cyclic group \(C_N\), let \(H\) be the half-turn. A solution of

\[
X^2=H
\]

exists exactly when \(4\mid N\). Indeed, if \(g\) generates \(C_N\), then
\(H=g^{N/2}\), and \(X=g^a\) must satisfy

\[
2a\equiv \frac N2\pmod N,
\]

which is solvable exactly when \(4\mid N\).

Consequently:

\[
C_6\text{ contains }H\text{ but no square root of }H.
\]

Any cyclic refinement containing the six-state shell and an exact quarter-turn must
have order divisible by both \(6\) and \(4\), hence at least

\[
\operatorname{lcm}(6,4)=12.
\]

The gate carrier has exactly 12 phase positions, so it is a minimal cyclic
refinement.

There are two roots in \(C_{12}\):

\[
Q^3,\qquad Q^9=(Q^3)^{-1}.
\]

The declared cyclic orientation chooses the principal positive root \(Q^3\).
Without orientation/chirality, the two roots are indistinguishable. Therefore a
quarter-turn is not selected by reversal alone.

## 6. Relation to the three positive rays

Every other neighbor direction represents one of the three positive carrier-ray
families. Hence

\[
R^2
\]

is the positive three-ray cycle and

\[
R^3
\]

toggles the based orientation sign.

There is an exact Chinese-remainder coordinate

\[
C_6\longrightarrow C_3\times C_2,
\qquad
R^k\longmapsto(2k\bmod3,\ k\bmod2).
\]

The generator maps to \((2,1)\), and therefore

\[
(2,1)^2=(1,0),
\qquad
(2,1)^3=(0,1).
\]

So the six-state successor is uniquely characterized by

\[
R^2=\text{positive three-ray turn},
\qquad
R^3=\text{based reversal}.
\]

The second equation is a direction/phase quotient statement. It is not an assertion
that the canonical reverse native trace is literally the groupoid inverse of the
forward trace.

## 7. Precision refinement is quotient-remainder with carry

Let

\[
N_m=6\cdot2^m,\qquad
\mathcal O_m=C_{N_m}.
\]

Embed an old phase in the next level by

\[
\iota_m([k]_{N_m})=[2k]_{N_{m+1}}.
\]

Every fine phase has a unique decomposition

\[
j=2k+\varepsilon,
\qquad
\varepsilon\in\{0,1\}.
\]

Thus a refined orientation state consists of

\[
\boxed{\text{coarse phase }k+\text{ one residual phase bit }\varepsilon.}
\]

One fine successor obeys the exact carry law

\[
(k,0)\longmapsto(k,1),
\]

\[
(k,1)\longmapsto(k+1,0).
\]

This is the orientation analogue of finite integer precision: the residual bit
records whether the inserted half-step has been consumed.

At the first refinement,

\[
i\text{-position}=3=2\cdot1+1.
\]

Hence the quarter-turn is literally invisible in the coarse `C6` state and appears
as a nonzero first refinement residual.

For a compatible character with generators
\(\zeta_m=\zeta_{m+1}^2\),

\[
\zeta_{m+1}^{\,2k+\varepsilon}
=
\zeta_m^k\,\zeta_{m+1}^{\,\varepsilon}.
\]

This is the finite discrete exponential law: additive precision digits recompose
multiplicatively, including carry.

## 8. Canonical recursive phase subdivision

Given an oriented cyclic phase carrier \((\mathcal O_m,R_m)\), form one formal
midpoint event \(E_x\) for every oriented edge \(x\to R_mx\). Define

\[
\mathcal O_{m+1}
=
\mathcal O_m\sqcup\{E_x:x\in\mathcal O_m\}
\]

and

\[
R_{m+1}(x)=E_x,
\qquad
R_{m+1}(E_x)=R_mx.
\]

Then

\[
R_{m+1}^2|_{\mathcal O_m}=R_m,
\]

and \(R_{m+1}\) is a cycle of order \(2N_m\).

Relative to the cyclic orientation, this construction is unique: the inserted
event between \(x\) and \(R_mx\) must be the successor of \(x\), and \(R_mx\) must
be its successor. Reversing orientation gives the inverse root tower.

At level zero the midpoint events are supplied by the actual pivot gates \(G_k\).
For levels \(m\ge1\), the events are presently formal phase refinements. No current
Foundation theorem identifies them with new native Cells or new geometric gates.

## 9. Two different completions: a necessary no-go theorem

The bare group tower does not determine the continuous circle.

Under the embeddings \([k]\mapsto[2k]\), the direct limit is

\[
D
=
\left\{
\frac{k}{6\cdot2^m}\bmod1
:
k\in\mathbf Z,\ m\ge0
\right\}
\cong
C_3\oplus C_{2^\infty},
\]

where \(C_{2^\infty}\) is the Prüfer 2-group.

If one instead uses the natural reduction maps

\[
C_{6\cdot2^{m+1}}\to C_{6\cdot2^m},
\qquad
[k]\mapsto[k]\bmod 6\cdot2^m,
\]

then

\[
\varprojlim_m C_{6\cdot2^m}
\cong
C_3\times\mathbf Z_2.
\]

This inverse-limit completion is profinite/totally disconnected, not the
Archimedean phase circle.

The continuous phase circle appears only after declaring the normalized cyclic
phase metric

\[
d_m(k,\ell)
=
\frac{
\min(|k-\ell|,N_m-|k-\ell|)
}{N_m}.
\]

The embeddings are isometries for this metric. The map

\[
[k]_{N_m}\longmapsto \frac{k}{N_m}\bmod1
\]

identifies the direct union with a dense subgroup of
\(\mathbf R/\mathbf Z\), so its metric completion is

\[
\widehat D_{\rm phase}\cong\mathbf R/\mathbf Z.
\]

Therefore:

\[
\boxed{
\text{algebraic dyadic refinement alone does not force }U(1);
}
\]

\[
\boxed{
\text{oriented cyclic adjacency + full-turn normalization selects the
Archimedean phase completion.}
}
\]

The normalized phase metric is a derived orientation metric. It must not be
silently identified with the native directed line gauge, whose reversal asymmetry
is already frozen.

## 10. Euler formula as even/odd reversal decomposition

At any finite level containing a quarter-turn, let \(\chi\) be an oriented
one-dimensional character and put

\[
J=\chi\!\left(\frac14\right),
\qquad
J^2=-1.
\]

For any character state \(u\), define

\[
C(u)=\frac{u+u^{-1}}2,
\]

\[
S(u)=\frac{u-u^{-1}}{2J}.
\]

Then exactly

\[
\boxed{u=C(u)+J\,S(u).}
\]

In the standard complex readout,

\[
C(e^{i\theta})=\cos\theta,
\qquad
S(e^{i\theta})=\sin\theta.
\]

Thus cosine and sine are not primitive ingredients of rotation. They are the
reversal-even and reversal-odd projections of one rotation character under

\[
u\longmapsto u^{-1}.
\]

The imaginary unit is the normalization of the odd line selected by the first
principal quarter-turn gate:

\[
J=\chi(Q^3).
\]

At half-turn,

\[
u=-1,\qquad C(u)=-1,\qquad S(u)=0.
\]

Therefore Euler's identity has the finite geometric reading

\[
\boxed{\text{half-period phase has pure reversal-even value }-1.}
\]

## 11. Half-traces force the Viète recurrence without angles

Let

\[
U_0=-1
\]

and choose the principal dyadic roots

\[
U_{n+1}^2=U_n.
\]

In the finite phase tower one may take

\[
U_n=R_n^3,
\]

because \(R_n\) has order \(6\cdot2^n\). Then

\[
U_0=R_0^3=-1,
\qquad
U_1=R_1^3=J.
\]

Define

\[
c_n=\frac{U_n+U_n^{-1}}2.
\]

A purely algebraic calculation gives

\[
\begin{aligned}
c_{n+1}^2
&=
\left(\frac{U_{n+1}+U_{n+1}^{-1}}2\right)^2\\
&=
\frac{U_n+2+U_n^{-1}}4\\
&=
\frac{1+c_n}{2}.
\end{aligned}
\]

Since \(c_1=0\) and the chosen oriented root has positive even coordinate,

\[
\boxed{
c_{n+1}=\sqrt{\frac{1+c_n}{2}}.
}
\]

This derives the nested radicals from rotation roots and reversal half-traces,
without using a classical angle or the numerical value of \(\pi\).

With

\[
s_n=\frac{U_n-U_n^{-1}}{2J},
\]

one also has

\[
c_n^2+s_n^2=1
\]

and

\[
s_n=2c_{n+1}s_{n+1}.
\]

Since \(s_1=1\),

\[
1
=
2^{m-1}
\left(\prod_{n=2}^{m}c_n\right)s_m.
\]

Hence the finite rotation readout

\[
\Pi_m^{\rm rot}
=
2^m s_m
\]

satisfies the exact finite identity

\[
\boxed{
\Pi_m^{\rm rot}
=
\frac{2}{\prod_{n=2}^{m}c_n}.
}
\]

No target value of \(\pi\) appears in this construction.

The convergence assertion is also independent of a preassigned value of
\(\pi\). For \(n\ge1\), \(0\le c_n<1\), and

\[
c_{n+1}>c_n
\]

because \((1+c_n)/2>c_n^2\) on \([0,1)\). Hence \(c_n\to1\). Put
\(d_n=1-c_n\). Then

\[
d_{n+1}
=
\frac{d_n}{2(1+c_{n+1})}
\le
\frac{d_n}{2(1+c_2)}.
\]

The right-hand ratio is strictly below \(1\), so \(\sum d_n<\infty\). Since
\(c_n\ge c_2>0\), the elementary bound
\(-\log c_n\le (1-c_n)/c_2\) shows

\[
\prod_{n=2}^{\infty}c_n>0.
\]

Therefore \(\Pi_m^{\rm rot}\) strictly increases to a finite constant. This
constant may be defined internally as

\[
\pi_{\rm rot}
=
\lim_{m\to\infty}\Pi_m^{\rm rot}.
\]

Under the standard Archimedean character realization,
\(U_m=e^{i\pi/2^m}\), so \(s_m=\sin(\pi/2^m)\), and the internal constant agrees
with classical \(\pi\).

## 12. Pi as the half-speed of the completed rotation character

Normalize one full turn to phase length \(1\). Let

\[
\chi:\mathbf R/\mathbf Z\to U(1)
\]

be the completed oriented character. For the dyadic phase increment

\[
h_m=\frac1{2^{m+1}},
\]

one has \(U_m=\chi(h_m)\) and

\[
\Pi_m^{\rm rot}
=
\frac{
\left|\chi(h_m)-\chi(-h_m)\right|
}{4h_m}.
\]

Therefore

\[
\boxed{
\pi_{\rm rot}
=
\frac12\,\left|\chi'(0)\right|
}
\]

whenever the Archimedean derivative exists.

In the standard complex coordinate, \(\chi(t)=e^{2\pi i t}\), so
\(|\chi'(0)|=2\pi\). This gives the most precise current geometric meaning:

\[
\boxed{
\pi
=
\text{half the infinitesimal character speed per normalized full turn}.
}
\]

Equivalently, the Viète approximants are symmetric finite-difference estimates of
that rotation-generator scale.

This separates two roles:

- the finite Cell/gate/refinement system supplies orientation and phase precision;
- the Archimedean character supplies the metric conversion from normalized turn to
  Euclidean character displacement.

## 13. Why current native line length cannot yet be the Euler radius

The frozen directed line gauge is generally reversal asymmetric. A positive-axis
unit segment has forward/reverse spectrum

\[
\{1,\sqrt2\}.
\]

Hence based half-turn/reversal does not act isometrically on one directed native
gauge. It acts canonically only after retaining the full bidirectional segment
pair or passing to a direction/phase quotient.

Therefore the Euler character cannot currently be identified with the native line
length algebra. The valid typed chain is

```text
native Cell / line-trace data
    -> based orientation or bidirectional-segment quotient
    -> carrier C6 rotation shell
    -> pivot-gate C12 phase refinement
    -> formal dyadic transition refinements
    -> finite cyclotomic character
    -> normalized phase metric completion
    -> Euler complex coordinate
```

The missing native theorem is not “does a square root exist?” The first square root
has now been constructed at the gate-event layer. The remaining hard problem is:

> Is the direction/phase quotient operation-safe for the actual rotating
> line-trace dynamics, and can higher phase events be realized by a canonical
> native precision refinement rather than by formal barycentric subdivision?

## 14. Relation to the existing algebraic marker \(J\)

The frozen path-valued square-root operator uses

\[
\mathbf Z[J]/(J^2+1)
\]

as a sector-local component algebra, while explicitly refusing to interpret \(J\)
as a classical native \(90^\circ\) axis.

The present result independently produces a rotation-character unit

\[
J_{\rm rot}=\chi(Q^3),
\qquad
J_{\rm rot}^2=-1.
\]

A possible bridge is

\[
J_{\rm component}
\longmapsto
J_{\rm rot}.
\]

This bridge is not yet proved. It would require an action of the gate-refined
rotation phase on native component traces that respects composition and the frozen
positive-axis typing.

Freeze:

`PATH_NORM_SQRT_J != ROTATION_CHARACTER_J` until a bridge theorem is proved.

## 15. Candidate statement

`AC-EM-FREE-F6D046-EULER-CELL-GATE-PHASE-V2`:

> A pivot Cell and its six neighbors provide a carrier-level `C6` orientation
> shell. The unique pivot-incident triple gate between each consecutive pair
> canonically barycentrically subdivides that shell to a typed `C12` phase
> carrier. Its successor \(Q\) satisfies \(Q^2=R\); \(Q^3\) is the principal
> quarter-turn character and squares to based reversal. Recursive oriented
> transition subdivision yields a dyadic phase-precision tower with exact
> quotient/remainder carry. Finite rotation characters decompose into
> reversal-even and reversal-odd parts, giving the algebraic Euler formula.
> Their dyadic half-traces force the Viète nested-radical recursion, and the
> resulting finite readouts converge to a rotation constant equal, under the
> standard Archimedean character completion, to classical \(\pi\). The bare
> group tower alone does not select \(U(1)\); the normalized cyclic phase metric
> is the required completion datum.

Status:

`CARRIER_GATE_GEOMETRY_EXACT`.

`FINITE_CYCLIC_REFINEMENT_EXACT`.

`HALF_TRACE_AND_VIETE_ALGEBRA_EXACT`.

`ARCHIMEDEAN_COMPLETION_TYPED_DERIVED`.

`NATIVE_OPERATION_SAFE_ROTATION_QUOTIENT_OPEN`.

## 16. Executable certificate

The companion module

`src/enterprise_math/rotation_phase_refinement.py`

checks, using exact rational arithmetic where applicable:

- all six pivot gates and their three squared distances \(1/3\);
- the `C12` typed successor and \(Q^2=R\);
- \(Q^3\), \(Q^4\), \(Q^6\), and \(Q^{12}\);
- the Chinese-remainder `C6 -> C3 x C2` generator;
- nonexistence of a quarter-turn in `C6` and its two roots in `C12`;
- exact quotient/remainder refinement and carry;
- isometry of the normalized phase embedding;
- the dyadic half-trace/Viète finite identity without importing \(\pi\).

The implementation is a project subtool composition of the existing precision,
finite-symmetry, and cocycle/transport tool families. No new top-level tool family
is claimed.
