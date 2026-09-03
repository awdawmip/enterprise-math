# Euler formula from a six-gate Cell link: non-split dyadic refinement, spectral decimation, and an intrinsic rotation-completion constant

Status: `FREE_RESEARCH / THEOREM_PACKAGE_CANDIDATE / EXECUTABLE_CHECKED / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`
Author/program signature: `YUAN X / Enterprise Math`

## 1. Result of this attack

The previous Euler note left one decisive gap:

> Can the square-root refinement of a rotation be produced from declared finite Cell structure, rather than imported from the classical half-angle formula?

At the carrier/readout level the answer is now substantially positive.

The boundary gates of one current circle Cell form a combinatorial six-cycle. The canonical edge subdivision of a cyclic phase graph

\[
C_N\longmapsto C_{2N}
\]

doubles phase resolution without using a Euclidean angle. Old phase states are the even vertices, and new midpoint states are the odd vertices. For even \(N\), the refinement is a non-split group extension

\[
0\longrightarrow C_N
\overset{k\mapsto 2k}{\longrightarrow}
C_{2N}
\overset{\bmod 2}{\longrightarrow}
C_2
\longrightarrow0.
\]

In the unique coordinates \(j=2k+\varepsilon\), addition is

\[
(k,\varepsilon)\boxplus(\ell,\eta)
=
\left(k+\ell+\varepsilon\eta,\,
      \varepsilon+\eta\pmod2\right).
\]

Thus the added precision bit is not independent. Two midpoint bits generate one coarse phase step. The coupling is an exact binary carry.

Starting from the antipodal half-turn in \(C_6\), choosing one of the two oriented arcs to the antipode and repeatedly taking the combinatorial midpoint produces a canonical chiral tower

\[
C_6\hookrightarrow C_{12}\hookrightarrow C_{24}\hookrightarrow\cdots .
\]

Its distinguished state \(q_m=3\in C_{6\cdot2^m}\) has order \(2^{m+1}\), and

\[
2q_{m+1}=\iota_m(q_m).
\]

For a compatible finite character \(u_m=\chi_m(q_m)\),

\[
u_0=-1,\qquad u_{m+1}^2=u_m.
\]

The reversal-even trace

\[
c_m=\frac{u_m+u_m^{-1}}2
\]

then satisfies the exact finite spectral-decimation law

\[
\boxed{c_{m+1}^2=\frac{1+c_m}{2}},
\qquad
c_0=-1,\quad c_1=0.
\]

No numerical value of \(\pi\), classical sine, classical cosine, radius, arc length, or angle-bisection axiom occurs in this recursion.

The finite Euler decomposition is already exact:

\[
u_m=c_m+i\,s_m,
\qquad
s_m=\frac{u_m-u_m^{-1}}{2i},
\qquad i:=u_1,\quad i^2=-1.
\]

Here \(c_m\) is the reversal-even channel and \(i s_m\) is the reversal-odd channel.

Finally, define

\[
P_M=\prod_{m=2}^{M}c_m,
\qquad
\Pi_M^{\mathrm{rot}}=\frac2{P_M}.
\]

The character factorization gives

\[
\Pi_M^{\mathrm{rot}}=2^M s_M,
\]

and the sequence is strictly increasing and converges to a finite constant

\[
\Pi_\infty^{\mathrm{rot}}
:=
\lim_{M\to\infty}\Pi_M^{\mathrm{rot}},
\]

defined before any occurrence of classical \(\pi\). A finite algebraic enclosure is

\[
\boxed{
\Pi_M^{\mathrm{rot}}
<
\Pi_\infty^{\mathrm{rot}}
\le
\frac{\Pi_M^{\mathrm{rot}}}
{1-\sqrt2(1-c_{M+1})}
}.
\]

Under the standard archimedean character embedding only, one identifies

\[
u_m=e^{i\pi/2^m},
\qquad
\Pi_M^{\mathrm{rot}}
=
2^m\sin\frac{\pi}{2^m},
\]

and therefore

\[
\Pi_\infty^{\mathrm{rot}}=\pi.
\]

This final equality is an analytic bridge. The finite rotation tower and its convergent completion constant do not use the target numerical value.

## 2. Frozen input and typing boundaries

The current Enterprise plane supplies a triangular carrier of integer-addressed Cell centers, circle Cells at the critical overlap radius, triple boundary-intersection events, three named positive axis directions, three \(120^\circ\) native right sectors, no requirement that primitive negative axes exist, and one Cell rather than a simultaneous multi-Cell state at each native trajectory step.

The present theorem package uses the classical carrier only to certify local incidence and cyclic order. It does not replace the native sector-local metric by the Euclidean carrier metric.

Freeze:

`GATE_CYCLE_INCIDENCE != NATIVE_EUCLIDEAN_ANGLE`.

`ROTATION_CHARACTER_NORM != NATIVE_ENTERPRISE_LENGTH`.

`PHASE_REFINEMENT_STATE != NEW_PHYSICAL_CELL_GATE`.

The refinement vertices inserted below are precision/readout states. They are not asserted to be additional physical triple-intersection gates.

## 3. Six gates around one Cell

A center of the triangular carrier belongs to six elementary center triangles. At the frozen critical radius, each such triangle has one triple boundary-intersection point, and that point lies on the boundary of the Cell at the chosen center.

The six elementary triangles are distinct and cyclically arranged. Hence the corresponding six transition gates are distinct and inherit the link graph

\[
\operatorname{Lk}(\text{Cell})\cong C_6.
\]

This statement is combinatorial after the carrier incidence has been certified. No use is made of the carrier angle as native length data.

Choose a cyclic labeling

\[
G_6=\mathbf Z/6\mathbf Z.
\]

Then one next-gate step is \(j\mapsto j+1\), gate reversal is \(j\mapsto j+3\), forgetting direction identifies \(j\) with \(j+3\), and the three resulting unoriented classes form

\[
G_6/\langle3\rangle\cong C_3.
\]

Thus the earlier coarse description

\[
C_3\times C_2\cong C_6
\]

is no longer merely an optional algebraic augmentation. At the gate-transition level, \(C_3\) records the three underlying line families and the \(C_2\) involution is reversal of an ordered gate/edge germ.

The split \(C_6\cong C_3\times C_2\) uses the named positive direction in each line family. The reversal involution itself does not require a primitive negative spatial axis.

## 4. Orientation is a transition observable, not a one-Cell observable

A single Cell center does not determine the direction in which a trajectory arrived or will leave. Therefore no honest map

\[
\{\text{Cell states}\}\longrightarrow C_6
\]

can encode orientation without history.

The minimal exact carrier object is an ordered transition germ

\[
(x_0,x_1),
\qquad x_0\sim x_1,
\]

or, for a Cell-local boundary description, an ordered gate event.

Translation of both endpoints preserves its direction class. Reversing the ordered pair changes the class by the antipodal involution. Consecutive germs define a local turn increment.

Therefore the correct type is

\[
\boxed{\text{ORIENTATION}=\text{FIRST-ORDER TRANSITION OBSERVABLE},}
\]

not a scalar attached to an instantaneous Cell.

This resolves the apparent conflict between `ONE CELL PER TRAJECTORY STEP` and the need for an oriented segment state: orientation data lives on the arrow between two states.

Current scope is exact for the gate/nearest-neighbor transition language and equivariant under translations, cyclic relabeling, and reversal. It is not claimed to be predictively complete for every future Cell operation, and it is not yet proved to be the quotient selected by every admissible physical rotating-segment trajectory.

## 5. Canonical phase refinement by cycle subdivision

Let

\[
G_N=\mathbf Z/N\mathbf Z
\]

with its cyclic graph structure. Subdivide every graph edge once. The resulting graph is canonically

\[
\operatorname{Sd}(C_N)\cong C_{2N}.
\]

The old vertices are embedded as even states:

\[
\iota_N:G_N\hookrightarrow G_{2N},
\qquad
\iota_N(k)=2k.
\]

The odd states represent the newly resolved intervals between adjacent old phases.

Every refined phase has a unique normal form

\[
j=2k+\varepsilon,
\qquad
k\in G_N,\quad \varepsilon\in\{0,1\}.
\]

This uses only integer parity and cyclic adjacency. It is not the assertion that a Euclidean angle has a previously existing midpoint.

## 6. The refinement is a carry extension

Parity gives an exact sequence

\[
0\longrightarrow G_N
\overset{\iota_N}{\longrightarrow}
G_{2N}
\overset{\epsilon_N}{\longrightarrow}
C_2
\longrightarrow0,
\]

where

\[
\epsilon_N(j)=j\bmod2.
\]

### Theorem 6.1 — split criterion

The sequence splits as groups if and only if \(N\) is odd.

A splitting must send the nonzero element of \(C_2\) to an odd element of order two in \(G_{2N}\). The unique element of order two in \(G_{2N}\) is \(N\). It is odd exactly when \(N\) is odd.

Since every modulus in

\[
6,12,24,48,\ldots
\]

is even, every Enterprise six-gate dyadic refinement is non-split.

### Theorem 6.2 — exact carry law

Write refined states as \((k,\varepsilon)\) through \(j=2k+\varepsilon\). Then

\[
(k,\varepsilon)\boxplus(\ell,\eta)
=
\left(k+\ell+\varepsilon\eta,\,
\varepsilon+\eta\pmod2\right).
\]

Indeed,

\[
(2k+\varepsilon)+(2\ell+\eta)
=
2(k+\ell)+(\varepsilon+\eta).
\]

If both detail bits are one, \(1+1=2\) contributes one coarse phase step and resets the detail bit.

Consequently, the new detail bit is not an independent direct-product coordinate. Dyadic angle refinement is a precision/carry mechanism.

Freeze:

`BINARY_PHASE_REFINEMENT != COARSE_PHASE × INDEPENDENT_BOOLEAN`.

## 7. Iterated refinement and the chiral midpoint tower

Set

\[
N_m=6\cdot2^m,
\qquad
G_m=G_{N_m}.
\]

The embeddings are

\[
\iota_m:G_m\to G_{m+1},
\qquad
k\mapsto2k.
\]

The half-turn at level \(m\) is

\[
h_m=\frac{N_m}{2}=3\cdot2^m.
\]

The fixed residue

\[
q_m=3\in G_m
\]

satisfies

\[
2^m q_m=h_m
\]

and has exact order

\[
\operatorname{ord}(q_m)=2^{m+1}.
\]

Moreover,

\[
2q_{m+1}=\iota_m(q_m).
\]

Thus \(q_0\) is the half-turn, \(q_1\) is a quarter-turn, \(q_2\) is an eighth-turn, and so on.

### Chirality theorem

In the coarse \(C_6\) gate cycle, identity and half-turn are joined by exactly two simple length-three arcs. Reversal exchanges them.

After one edge subdivision, each chosen arc has a unique combinatorial midpoint. Repeating the construction gives exactly two nested local midpoint towers, exchanged by reversal.

Therefore

\[
\boxed{-1\text{ alone does not select }i.}
\]

A cyclic orientation/chirality choice selects one of the two roots \(i\) and \(-i\). Once the positive arc is selected, all later positive midpoints are fixed by nesting; arbitrary independent square-root choices would violate local interval refinement.

This gives a precise finite meaning to the sign of \(i\):

\[
\boxed{i=\text{the first chiral midpoint of the identity-to-reversal arc}.}
\]

## 8. Compatible finite characters

Let \(\chi_m\) be the fundamental one-dimensional character of \(G_m\), chosen compatibly with the positive cyclic generator. Define

\[
u_m=\chi_m(q_m).
\]

Compatibility with subdivision gives

\[
u_{m+1}^2=u_m,
\]

and the initial values are

\[
u_0=-1,\qquad u_1=i.
\]

Everything up to this point is finite: \(u_m\) is a root of unity of order \(2^{m+1}\). The continuous exponential is not needed to state the finite law.

## 9. Spectral decimation and nested radicals

Define the reversal-even trace coordinate

\[
c_m=\frac{u_m+u_m^{-1}}2.
\]

Since \(u_{m+1}^2=u_m\),

\[
(2c_{m+1})^2
=(u_{m+1}+u_{m+1}^{-1})^2
=u_m+u_m^{-1}+2
=2c_m+2.
\]

Hence

\[
\boxed{c_{m+1}^2=\frac{1+c_m}{2}.}
\]

Starting from \(c_0=-1\), the positive chiral/archimedean branch gives

\[
c_1=0,
\qquad
c_2=\frac{\sqrt2}{2},
\qquad
c_3=\frac{\sqrt{2+\sqrt2}}2,
\]

and the familiar nested tower thereafter.

This is also a graph-spectrum statement. Let \(S_m\) be the cyclic shift on \(C_{N_m}\) and let

\[
A_m=\frac{S_m+S_m^{-1}}2
\]

be normalized adjacency. The Fourier mode with fixed integer label \(3\) has eigenvalue \(c_m\). Subdivision doubles \(N_m\) while retaining label \(3\), and its eigenvalues obey exactly

\[
c_m=2c_{m+1}^2-1.
\]

Thus the nested radicals are the spectral decimation of one fixed discrete half-turn mode under repeated refinement of the six-gate link.

Freeze:

`VIETE_RADICAL_TOWER = FINITE_CYCLE_SPECTRAL_DECIMATION`

at the character/readout layer. This does not yet mean that every physical Cell trajectory dynamically realizes every refined phase state.

## 10. Finite Euler decomposition as reversal parity

Set

\[
i:=u_1,
\qquad i^2=-1.
\]

For \(m\ge1\), define

\[
s_m=\frac{u_m-u_m^{-1}}{2i}.
\]

Then, identically,

\[
\boxed{u_m=c_m+i s_m.}
\]

No exponential series is needed.

Let reversal act by \(\mathcal R(u)=u^{-1}\). With the chiral frame \(i\) held fixed,

\[
c(\mathcal R u)=c(u),
\qquad
s(\mathcal R u)=-s(u).
\]

Thus \(c\) is the orientation-forgetting/even channel, \(s\) is the signed orientation/odd channel, and \(i\) is the frame element that reattaches the odd magnitude to the oriented character state.

Also,

\[
c_m^2+s_m^2=1.
\]

For two finite rotation-character states \(u,v\), the same decomposition gives exact addition laws

\[
c(uv)=c(u)c(v)-s(u)s(v),
\]

\[
s(uv)=s(u)c(v)+c(u)s(v).
\]

Therefore the geometric core of Euler's formula already exists at every finite cyclotomic level:

\[
\boxed{
\text{oriented character}
=
\text{reversal-even component}
+
\text{chiral reversal-odd component}.
}
\]

The notation \(e^{i\theta}=\cos\theta+i\sin\theta\) appears only after a continuous phase coordinate \(\theta\) is assigned.

## 11. Exact Viète telescoping

Let

\[
d_m=u_m-u_m^{-1}=2i s_m.
\]

The square-root relation gives

\[
d_m
=u_{m+1}^2-u_{m+1}^{-2}
=(u_{m+1}-u_{m+1}^{-1})(u_{m+1}+u_{m+1}^{-1})
=2c_{m+1}d_{m+1}.
\]

Since \(s_1=1\),

\[
1
=
2^{M-1}
\left(\prod_{m=2}^{M}c_m\right)s_M.
\]

Hence

\[
\boxed{
\prod_{m=2}^{M}c_m
=
\frac1{2^{M-1}s_M}.
}
\]

Define the finite rotation readout

\[
\boxed{
\Pi_M^{\mathrm{rot}}
=
\frac2{\prod_{m=2}^{M}c_m}
=
2^M s_M.
}
\]

All terms are algebraic numbers generated by the finite root tower. The definition contains no classical \(\pi\).

Numerically,

\[
\begin{array}{c|c}
M&\Pi_M^{\mathrm{rot}}\\ \hline
2&2.828427124746\ldots\\
3&3.061467458921\ldots\\
4&3.121445152258\ldots\\
6&3.140331156955\ldots\\
8&3.141513801144\ldots\\
10&3.141587725277\ldots
\end{array}
\]

## 12. Monotone convergence without using \(\pi\)

For \(m\ge2\),

\[
0<c_m<1.
\]

Because

\[
\Pi_{M+1}^{\mathrm{rot}}
=
\frac{\Pi_M^{\mathrm{rot}}}{c_{M+1}},
\]

the sequence is strictly increasing.

Let

\[
a_m=1-c_m.
\]

From the trace recursion,

\[
a_{m+1}
=
\frac{a_m}{2(1+c_{m+1})}.
\]

Since \(c_{m+1}\ge c_2=1/\sqrt2\),

\[
\frac{a_{m+1}}{a_m}
\le
r_0
:=
\frac1{2(1+1/\sqrt2)}
=
1-\frac1{\sqrt2}
<1.
\]

Therefore

\[
\sum_{m=2}^{\infty}a_m
\le
\frac{r_0}{1-r_0}
=
\sqrt2-1
<1.
\]

For \(0\le a_j<1\),

\[
\prod_j(1-a_j)\ge1-\sum_j a_j.
\]

Consequently,

\[
P_\infty
=
\prod_{m=2}^{\infty}c_m
\]

exists and is strictly positive. Hence

\[
\boxed{
\Pi_\infty^{\mathrm{rot}}
=
\frac2{P_\infty}
}
\]

exists as a finite positive real completion constant.

This establishes an intrinsic finite-to-continuous completion before the classical identification.

## 13. A finite algebraic error enclosure

For any \(M\ge2\),

\[
\sum_{m=M+1}^{\infty}(1-c_m)
\le
\frac{1-c_{M+1}}{1-r_0}
=
\sqrt2(1-c_{M+1}).
\]

Set

\[
B_M=\sqrt2(1-c_{M+1}).
\]

Then \(0<B_M<1\), and the omitted tail product satisfies

\[
\prod_{m=M+1}^{\infty}c_m
\ge1-B_M.
\]

Since

\[
\Pi_\infty^{\mathrm{rot}}
=
\frac{\Pi_M^{\mathrm{rot}}}
{\prod_{m=M+1}^{\infty}c_m},
\]

we obtain

\[
\boxed{
\Pi_M^{\mathrm{rot}}
<
\Pi_\infty^{\mathrm{rot}}
\le
\frac{\Pi_M^{\mathrm{rot}}}{1-B_M}.
}
\]

Equivalently,

\[
0<
\Pi_\infty^{\mathrm{rot}}-
\Pi_M^{\mathrm{rot}}
\le
\Pi_M^{\mathrm{rot}}
\frac{B_M}{1-B_M}.
\]

This is a finite certificate built only from nested algebraic radicals at depth \(M+1\). It is not the sharp classical \(O(4^{-M})\) error law, but it proves convergence and supplies a computable enclosing interval without using the target value.

## 14. Classical archimedean identification

Only now choose the standard complex character realization

\[
\chi_m(k)
=
\exp\left(\frac{2\pi i k}{6\cdot2^m}\right).
\]

For \(q_m=3\),

\[
u_m=e^{i\pi/2^m}.
\]

Then

\[
c_m=\cos\frac{\pi}{2^m},
\qquad
s_m=\sin\frac{\pi}{2^m},
\]

and

\[
\Pi_M^{\mathrm{rot}}
=
2^M\sin\frac{\pi}{2^M}.
\]

The classical limit

\[
\lim_{x\to0}\frac{\sin x}{x}=1
\]

therefore yields

\[
\boxed{\Pi_\infty^{\mathrm{rot}}=\pi.}
\]

This is the Viète identification.

The logical direction is:

```text
finite gate cycle
  -> canonical combinatorial subdivision
  -> non-split carry refinement
  -> chiral midpoint/root tower
  -> finite character trace recursion
  -> algebraic monotone completion constant
  -> standard archimedean character bridge
  -> classical pi
```

It is not:

```text
insert classical pi
  -> choose the recursion that returns pi
  -> call the result native
```

## 15. Euler formula retyped

Use a normalized turn coordinate in which one half-turn has parameter \(1\) and one full turn has parameter \(2\).

At finite dyadic depth the character is defined on dyadic phase states. In the standard archimedean completion, the parameterization becomes

\[
\chi(t)=e^{i\pi t}.
\]

Its even and odd coordinates are

\[
C(t)=\frac{\chi(t)+\chi(-t)}2,
\]

\[
S(t)=\frac{\chi(t)-\chi(-t)}{2i}.
\]

Thus

\[
\chi(t)=C(t)+iS(t).
\]

In classical notation,

\[
C(t)=\cos(\pi t),
\qquad
S(t)=\sin(\pi t).
\]

Therefore

\[
\boxed{e^{i\theta}=\cos\theta+i\sin\theta}
\]

is the continuous-coordinate form of a more primitive statement:

\[
\boxed{
\text{rotation character}
=
\text{reversal-even readout}
+
\text{chiral reversal-odd readout}.
}
\]

And

\[
e^{i\pi}=-1
\]

means

\[
\boxed{
\text{one completed half-period of the oriented gate phase}
=
\text{transition reversal}.
}
\]

The numerical constant \(\pi\) is the archimedean phase conversion between normalized half-turn count and radian coordinate.

## 16. Three no-go results that must be retained

### 16.1 Half-turn does not uniquely determine \(i\)

The equation

\[
q^2=-1
\]

has the two roots \(q=\pm i\). The finite gate cycle identifies them with the two arcs from identity to antipode. A chirality/forward-order choice is necessary.

### 16.2 Abstract refinement does not select an archimedean completion

The algebraic direct limit of the finite cyclic refinement tower is not, by itself, a metric circle. To obtain \(U(1)\), one must supply or derive the appropriate character topology/norm.

Therefore:

`DYADIC_GROUP_REFINEMENT != UNIQUE_U1_COMPLETION_WITHOUT_READOUT_METRIC`.

### 16.3 Gate-phase readout is not yet the full native rotation dynamics

The gate cycle supplies a precise local orientation carrier and a canonical refinement mechanism. It remains to prove that the actual rotating-segment/Cell dynamics factors through this carrier in an operation-safe way for the desired future language.

Therefore:

`LOCAL_GATE_PHASE_THEOREM != GLOBAL_NATIVE_ROTATION_DYNAMICS`.

## 17. Relation to the earlier tetrahedral two-torsion

The earlier four-slice/six-line residual quotient contains a nontrivial \(C_2\) class and a non-split tetrahedral symmetry action. The present cyclic refinement also contains a non-split binary extension and a carry cocycle.

The structural resemblance is strong:

\[
\text{free coordinate}
+
\text{binary residual}
+
\text{nontrivial symmetry/transport coupling}.
\]

However, no theorem currently identifies the two \(C_2\) objects. The safe statement is that they are independent finite manifestations of a recurring Enterprise pattern in which continuous or coarse readout forgets a binary transport distinction.

A future theorem would need an explicit map from the tetrahedral residual carrier to the Cell gate-phase refinement tower.

## 18. Protocol for testing other pi formulas

The present result supplies a common test sequence for the open research branches:

1. identify a finite rotation/segment state without using \(\pi\);
2. identify the exact refinement or mode operation;
3. expose any carry, torsion, branch, or chirality data;
4. define a finite algebraic period readout;
5. prove monotonicity or a two-sided finite enclosure;
6. only afterward identify the continuous limit with classical \(\pi\);
7. reject any construction that chose the discrete rule by fitting the target value.

For Viète, the mechanism is now

\[
\text{cycle subdivision}
\to
\text{trace spectral decimation}
\to
\text{nested radicals}.
\]

Wallis, sine product, Basel, AGM, arctangent, and Ramanujan families can now be tested against the same typed standard.

## 19. Candidate theorem package

`AC-EM-FREE-F6D046-EULER-GATE-CYCLE-REFINEMENT-V2`

### Proved at finite carrier/algebra level

1. one Cell's six declared transition gates have link \(C_6\);
2. oriented gate germs give a transition-level \(C_6\) readout with antipodal reversal;
3. cycle subdivision gives \(C_N\hookrightarrow C_{2N}\);
4. the refinement extension by parity splits iff \(N\) is odd;
5. for the six-gate tower every refinement is non-split and has the explicit binary carry law;
6. a chiral arc choice produces the unique nested local midpoint/root tower;
7. the trace obeys exact spectral decimation \(c_{m+1}^2=(1+c_m)/2\);
8. finite Euler decomposition is reversal-even plus reversal-odd;
9. Viète telescoping produces the algebraic precision sequence \(\Pi_M^{\mathrm{rot}}\);
10. \(\Pi_M^{\mathrm{rot}}\) is strictly increasing and has a finite positive limit;
11. the displayed algebraic upper enclosure is valid.

### External effective bridge

12. the standard complex character realization identifies the limit with classical \(\pi\).

### Still open

13. full operation-safe factorization of native rotating-segment dynamics through the gate phase;
14. derivation of the archimedean character norm from native Cell operations;
15. identification, if any, between cyclic refinement carry and tetrahedral residual \(C_2\).

Status:

`STRONG_FREE_RESEARCH_CANDIDATE / FINITE_CORE_PROVED / EXECUTABLE_REGRESSION_ADDED / NATIVE_GLOBALIZATION_OPEN`.
