# Euler formula from the Cell–gate dyadic rotation tower

Status: `FREE_RESEARCH / FINITE_THEOREM_PACKAGE_CANDIDATE / NOT_FOUNDATION`  
Date: `2026-09-03`  
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`  
Author/program signature: `YUAN X / Enterprise Math`

## 0. Result in one sentence

The strongest current candidate is no longer merely that Euler's formula *resembles* rotation. A local six-orientation Cell shell has an exact first incidence refinement by its six transition gates,

\[
C_6\longrightarrow C_{12},
\]

and directed barycentric refinement then gives a minimal tower

\[
C_6\hookrightarrow C_{12}\hookrightarrow C_{24}\hookrightarrow\cdots .
\]

At depth \(m\), the state three refined steps from the identity has exact order \(2^{m+1}\); these states form the compatible root tower

\[
-1,\quad i,\quad \sqrt{i},\quad \sqrt[4]{i},\ldots .
\]

Their symmetric character traces satisfy Viète's nested-radical recursion, and their antisymmetric traces give a target-free monotone finite constant whose classical analytic identification is \(\pi\).

The first refinement is realized by actual Cell/gate incidence. Every later refinement necessarily introduces higher transition/history states. Thus the full Euler rotation law is not purely spatial Cell geometry: it is a completion of a time-ordered rotation trace.

## 1. Frozen type boundaries

This note uses the current three-positive-axis overlapping Cell plane only in the following typed sense.

1. There are three positive line/ray families in the slice.
2. Reversing an oriented segment is endpoint exchange / an independently decoded reverse trace, not a primitive negative native axis.
3. A pivot Cell has six nearest-neighbor direction classes in the carrier.
4. The boundary of the pivot Cell has six triple-intersection transition gates, one between each consecutive pair of neighbor-direction classes.
5. One physical instantaneous trajectory state remains one Cell. A gate is a transition/incidence event, not a simultaneous multi-Cell state.
6. The native \(120^\circ\) right-angle law and the Euclidean character picture remain different semantic layers.

Freeze:

`ROTATION_PHASE_STATE != PRIMITIVE_POINT_ADDRESS`.

`COMPLEX_CHARACTER != NATIVE_LENGTH_METRIC`.

`GATE_EVENT != MULTI_CELL_INSTANTANEOUS_STATE`.

`CARRIER_SIX_DIRECTIONS != P000_SIX_NATIVE_SPATIAL_AXES`.

## 2. The coarse six-orientation shell

Modulo translation, the three positive line families together with an explicit endpoint-orientation bit form six oriented unit-segment classes. Abstractly,

\[
\mathcal O_0\simeq C_3\times C_2\simeq C_6.
\]

The \(C_3\) factor records the positive-ray family. The \(C_2\) factor records endpoint reversal. The nontrivial \(C_2\) element is represented by a half-turn of the six-state shell.

Choose a cyclic ordering and write

\[
\Gamma_0=C_6=\mathbf Z/6\mathbf Z,
\qquad
r_0=[1].
\]

The native \(120^\circ\) positive-ray cycle is represented by \(r_0^2\), while endpoint reversal is

\[
h_0=r_0^3.
\]

The one-step generator \(r_0\) is a cyclic orientation coordinate. This note does not promote a carrier \(60^\circ\) move to a primitive native right turn.

## 3. The exact Cell–gate incidence refinement

Label the six neighbor Cell phases around one pivot Cell by

\[
C_0,C_1,\ldots,C_5
\]

in cyclic order. Let \(G_j\) be the triple-intersection gate incident with the pivot Cell and the two consecutive neighbor phases \(C_j,C_{j+1}\), indices taken modulo \(6\).

The incidence cycle is

\[
C_0-G_0-C_1-G_1-\cdots-C_5-G_5-C_0.
\]

Therefore the bipartite Cell/gate incidence graph is exactly \(C_{12}\). In residue coordinates,

\[
C_j\longleftrightarrow [2j],
\qquad
G_j\longleftrightarrow [2j+1]
\quad\text{in }\mathbf Z/12\mathbf Z.
\]

Let \(r_1=[1]\) be the refined successor and let

\[
\iota_0:\mathbf Z/6\mathbf Z\hookrightarrow\mathbf Z/12\mathbf Z,
\qquad
\iota_0([k])=[2k].
\]

Then

\[
r_1^2\iota_0=\iota_0r_0.
\]

Thus the first square root of the cyclic orientation transition is not merely postulated: it is realized by inserting the actual gate event between adjacent Cell-direction states.

## 4. Canonical directed subdivision tower

For \(m\ge0\), define

\[
N_m=6\cdot2^m,
\qquad
\Gamma_m=C_{N_m}=\mathbf Z/N_m\mathbf Z.
\]

The directed barycentric subdivision of a directed cycle inserts one transition token between every state and its successor. Hence

\[
B(C_N)\cong C_{2N}.
\]

Use the exact embedding

\[
\iota_m:\Gamma_m\hookrightarrow\Gamma_{m+1},
\qquad
\iota_m([k])=[2k].
\]

If \(r_m=[1]\), then

\[
2r_{m+1}=\iota_m(r_m).
\]

Equivalently, two fine transitions equal one embedded coarse transition.

At \(m=1\), the odd vertices are actual Cell gates. At \(m\ge2\), newly inserted odd vertices are higher transition/history tokens unless a separate physical Cell realization is proved. The combinatorial refinement is exact; its physical interpretation is intentionally typed.

## 5. Minimality of the tower

At depth \(m\), a compatible \(2^m\)-fold root of endpoint reversal has order

\[
2^{m+1}.
\]

Any cyclic phase carrier that simultaneously preserves the coarse \(C_6\) orientation shell and contains such an element must have order divisible by

\[
\operatorname{lcm}(6,2^{m+1})
=
3\cdot2^{m+1}
=
6\cdot2^m=N_m.
\]

The tower \(\Gamma_m=C_{N_m}\) attains this lower bound at every depth.

Therefore:

\[
\boxed{\Gamma_m\text{ is the minimal cyclic refinement preserving the six-state shell and an }m\text{-fold dyadic root of reversal}.}
\]

This is standard finite cyclic-group arithmetic, used here as a minimality certificate rather than as a historical novelty claim.

## 6. The three-step distinguished root tower

Define at every depth

\[
u_m=[3]\in\Gamma_m.
\]

Its order is

\[
\operatorname{ord}(u_m)
=
\frac{6\cdot2^m}{\gcd(6\cdot2^m,3)}
=
2^{m+1}.
\]

Moreover,

\[
2u_{m+1}
=
[6]
=
\iota_m([3])
=
\iota_m(u_m).
\]

Thus \(u_{m+1}\) is an exact square root of the embedded \(u_m\).

The first levels are:

\[
\begin{array}{c|c|c|c}
m & \Gamma_m & \operatorname{ord}(u_m) & \text{meaning}\\
\hline
0 & C_6  & 2 & \text{endpoint reversal / half-turn}\\
1 & C_{12} & 4 & \text{quarter-turn gate phase}\\
2 & C_{24} & 8 & \text{eighth-turn transition-history phase}\\
3 & C_{48} & 16 & \text{sixteenth-turn transition-history phase}
\end{array}
\]

The fixed residue \(3\) is not arbitrary. Since

\[
C_{6\cdot2^m}\simeq C_3\times C_{2^{m+1}},
\]

the element \([3]\) has trivial \(C_3\) component and generates the full \(2\)-primary factor. The three-positive-ray scaffold is therefore held fixed while the reversal fiber alone is dyadically refined.

A further exact observation is that \(u_m=[3]\) is newly born at every level \(m\ge1\): it is odd in the final residue coordinate and hence is not inherited from the preceding even-state embedding.

## 7. Where \(i\) first appears

At depth \(1\),

\[
u_1=[3]\in C_{12},
\qquad
2u_1=[6]=h_1.
\]

In the Cell/gate labeling, residue \(3\) is \(G_1\). The other square root of the half-turn is residue \(9=G_4\). Reflection of the cyclic order,

\[
\rho([k])=[-k],
\]

exchanges them:

\[
\rho([3])=[9].
\]

Therefore a bare unoriented incidence cycle cannot canonically select one of the two roots. A directed rotation order / chirality frame chooses one; reversing that frame interchanges \(i\) and \(-i\).

Freeze:

`I_REQUIRES_ORIENTATION_OR_CHIRALITY_CHOICE`.

`EULER_HALF_TURN_ENDPOINT_IS_CHIRALITY_INVARIANT`.

This is why the endpoint identity is more primitive than the sign of the quarter-turn coordinate.

## 8. A sharp local-geometry no-go theorem

The one-step local geometric phase set contains exactly

\[
6\text{ Cell-direction states}+6\text{ gate events}=12
\]

typed states.

Depth \(1\) requires exactly \(N_1=12\) states, so the Cell/gate geometry realizes the minimal quarter-turn refinement without redundancy.

Depth \(2\) requires

\[
N_2=\operatorname{lcm}(6,8)=24
\]

states. Consequently no faithful cyclic realization of the eighth-turn root can be built solely from the existing six Cell-direction states and six gate events.

More generally, depth \(m\) requires \(6\cdot2^m\) states. Hence:

\[
\boxed{\text{Cell+gate local geometry saturates at }C_{12}.}
\]

Every further exact root requires at least one new state type. Directed transition/history tokens provide the minimal such augmentation.

This gives a structural role to time: the first quarter-turn is visible as spatial incidence, while the infinite Euler tower requires progressively finer ordered transition history. The continuous exponential is therefore a space–time rotation completion, not a static spatial coordinate chart.

## 9. Finite characters before continuous angles

Choose compatible faithful characters

\[
\chi_m:\Gamma_m\longrightarrow \mu_{N_m}
\]

such that

\[
\chi_{m+1}(\iota_m x)=\chi_m(x).
\]

Set

\[
z_m=\chi_m(u_m).
\]

Then, exactly,

\[
z_0=-1,
\qquad
z_{m+1}^2=z_m,
\qquad
z_m^{2^m}=-1,
\qquad
z_m^{2^{m+1}}=1.
\]

No real angle, derivative, sine, cosine, or numerical value of \(\pi\) appears in these finite statements.

The direct limit of the distinguished dyadic subgroup is the Prüfer \(2\)-group \(\mu_{2^\infty}\). Under the standard complex character realization, its topological closure is \(U(1)\). Thus the continuous unit circle is a completion of a countable hierarchy of exact finite rotation states, rather than an obligatory primitive input.

## 10. Finite Euler decomposition

Let

\[
J=z_1,
\qquad
J^2=-1.
\]

Inside a common cyclotomic character field, let conjugation send \(z\mapsto z^{-1}\) and \(J\mapsto-J\). Define

\[
c_m=\frac{z_m+z_m^{-1}}2,
\qquad
s_m=\frac{z_m-z_m^{-1}}{2J}.
\]

Then the exact finite Euler decomposition is

\[
\boxed{z_m=c_m+Js_m.}
\]

It also satisfies

\[
c_m^2+s_m^2=1.
\]

For arbitrary dyadic phase states \(z,w\), the same definitions give

\[
c(zw)=c(z)c(w)-s(z)s(w),
\]

\[
s(zw)=s(z)c(w)+c(z)s(w).
\]

Therefore sine/cosine addition is already present as the symmetric/antisymmetric trace algebra of finite rotation characters. Calculus and power series are not needed at this layer.

## 11. Viète recursion from the root law

Since \(z_{m+1}^2=z_m\),

\[
c_m=2c_{m+1}^2-1
\]

and

\[
s_m=2c_{m+1}s_{m+1}.
\]

For the forward short-root branch,

\[
c_1=0,
\qquad
c_{m+1}>0\quad(m\ge1),
\]

so

\[
\boxed{c_{m+1}=\sqrt{\frac{1+c_m}{2}}.}
\]

Thus

\[
c_2=\frac{\sqrt2}{2},
\qquad
c_3=\frac{\sqrt{2+\sqrt2}}2,
\qquad
c_4=\frac{\sqrt{2+\sqrt{2+\sqrt2}}}{2},
\]

and so on. The nested radicals arise from taking compatible square roots of endpoint reversal in the finite phase tower; they are not introduced by first drawing a classical Euclidean angle.

Since \(s_1=1\), repeated use of \(s_{j-1}=2c_js_j\) gives

\[
1=2^{m-1}\left(\prod_{j=2}^m c_j\right)s_m.
\]

Define

\[
\boxed{
\Pi_m^{\mathrm{rot}}
=
2^m s_m
=
\frac{2}{\prod_{j=2}^m c_j}
\qquad(m\ge2).
}
\]

This is precisely the finite Viète product hierarchy, obtained without using a target numerical value of \(\pi\).

## 12. Target-free convergence theorem

For \(m\ge2\), \(0<c_m<1\). Therefore

\[
\Pi_{m+1}^{\mathrm{rot}}
=
\frac{\Pi_m^{\mathrm{rot}}}{c_{m+1}}
>
\Pi_m^{\mathrm{rot}}.
\]

Set \(d_m=1-c_m\). The half-root recursion gives

\[
d_{m+1}=\frac{d_m}{2(1+c_{m+1})}\le\frac{d_m}{2}.
\]

Since \(d_2=1-1/\sqrt2\),

\[
\sum_{m=2}^{\infty}d_m\le2d_2=2-\sqrt2<1.
\]

For \(0\le d_j<1\), \(\prod_j(1-d_j)\ge1-\sum_jd_j\). Hence

\[
\prod_{j=2}^m c_j\ge\sqrt2-1,
\]

and

\[
\Pi_m^{\mathrm{rot}}\le\frac2{\sqrt2-1}=2(1+\sqrt2).
\]

Thus the increasing sequence has an internally defined finite limit:

\[
\boxed{\pi_{\mathrm{rot}}:=\lim_{m\to\infty}\Pi_m^{\mathrm{rot}}.}
\]

No classical value of \(\pi\) is used in this definition or convergence proof.

Let \(B=2(1+\sqrt2)\). Since \(s_m=\Pi_m^{\mathrm{rot}}/2^m\le B/2^m\),

\[
1-c_m=\frac{s_m^2}{1+c_m}\le\frac{B^2}{4^m}.
\]

Consequently, for \(m\ge2\),

\[
0\le\pi_{\mathrm{rot}}-\Pi_m^{\mathrm{rot}}
\le
\Pi_m^{\mathrm{rot}}\frac{B^2}{3\cdot4^m-B^2}.
\]

This is a target-independent \(O(4^{-m})\) certificate.

## 13. Classical analytic identification

Under the standard complex realization,

\[
z_m=\exp\!\left(\frac{J\pi}{2^m}\right),
\qquad
s_m=\sin\!\left(\frac{\pi}{2^m}\right),
\]

and

\[
\Pi_m^{\mathrm{rot}}=2^m\sin\!\left(\frac{\pi}{2^m}\right).
\]

The classical limit \(\lim_{x\to0}\sin x/x=1\) then identifies

\[
\pi_{\mathrm{rot}}=\pi.
\]

This is an analytic identification of the independently defined finite completion constant.

Freeze:

`FINITE_ROTATION_TOWER_DEFINES_PI_ROT_WITHOUT_TARGET_PI`.

`PI_ROT_EQUALS_CLASSICAL_PI_USES_ANALYTIC_CHARACTER_COMPLETION`.

## 14. Euler's formula retyped

The normalized phase group can be written without \(\pi\) as dyadic turn fractions in \(\mathbf R/\mathbf Z\). The core endpoint statements are

\[
E(1)=1,
\qquad
E(1/2)=-1.
\]

Passing from turn fractions \(t\) to the unit-speed generator coordinate \(\theta=2\pi_{\mathrm{rot}}t\) gives

\[
E(\theta)=c(\theta)+Js(\theta).
\]

After classical identification \(J=i\) and \(\pi_{\mathrm{rot}}=\pi\), this becomes

\[
e^{i\theta}=\cos\theta+i\sin\theta
\]

and at the half-turn,

\[
e^{i\pi}+1=0.
\]

The geometric meanings are:

\[
-1=\text{sign-character value of endpoint reversal},
\]

\[
i=\text{a chirality-selected character coordinate of the first gate-level square root of reversal},
\]

\[
\pi=\text{the continuous generator-length calibration of one half-turn},
\]

\[
e^{i\theta}=\text{the continuous character of the completed ordered rotation trace}.
\]

## 15. Strongest current candidate

`AC-EM-FREE-F6D046-EULER-CELL-GATE-DYADIC-TOWER-V2`:

> The Enterprise three-positive-ray slice supplies a six-state oriented segment shell. Its six actual transition gates realize the minimal \(C_{12}\) refinement, in which a quarter-turn root of endpoint reversal first appears as a gate phase. Repeated directed barycentric subdivision gives the unique minimal cyclic tower \(C_{6\cdot2^m}\); the fixed three-step states form the compatible \(2\)-power root tower of reversal. Finite character traces obey the Euler addition algebra and Viète nested-radical recursion, and define a monotone target-free completion constant \(\pi_{\mathrm{rot}}\). Classical analysis identifies \(\pi_{\mathrm{rot}}\) with \(\pi\). Beyond the first gate layer, exact roots necessarily require higher transition/history states, so the full complex exponential is a completion of a time-ordered rotation trace rather than a primitive static spatial axis.

Status:

`FINITE_GROUP_AND_RADICAL_CHAIN_PROVED_IN_NOTE`.

`FIRST_CELL_GATE_REALIZATION_GEOMETRIC_FROM_DECLARED_CARRIER`.

`HIGHER_REFINEMENT_TRACE_NATIVE_NOT_YET_PHYSICALLY_CELL_REALIZED`.

`OPERATION_SAFE_QUOTIENT_FROM_ALL_NATIVE_ROTATION_TRAJECTORIES_OPEN`.

`NOT_FOUNDATION`.

## 16. Immediate next attacks

1. Formalize the cycle embeddings, distinguished-root order/minimality, and chirality obstruction in Lean.
2. Prove an operation-safe quotient for restricted pivot-preserving local rotation dynamics, or return a counterexample.
3. Determine whether higher transition tokens have a native realization through precision-scale Cell refinement; otherwise preserve the time/history typing.
4. Compare \(\pi_{\mathrm{rot}}\) with the multinomial precision-\(\pi\) tower by an explicit transform rather than matching limits.
5. Test whether the paired-Pell \(C_2\) shell norm is a quotient of the same dyadic reversal fiber; no identity is asserted yet.
6. Use the published Viète, Wallis, Machin, AGM, Basel, and Ramanujan free branches as independent falsification families.

Executable finite checker:

`src/enterprise_math/euler_rotation_refinement.py`

Regression:

`tests/test_euler_rotation_refinement.py`
