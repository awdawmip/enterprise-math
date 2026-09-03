# Viète native promotion boundary: C3/C2 holonomy specialization, matched Cell-rotation countermodels, and the independent shortest-root section

Status: `FREE_RESEARCH / EXISTING-C3-C2-HOLONOMY SPECIALIZATION + EXACT NATIVE-SELECTION NO-GO / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`

## 1. Frontier

The #1158 chain already proves at finite G1/G2 strength:

- the normalized equal-resultant root generates the Viète half-angle recursion without using the target value of pi;
- connected binary cycle refinement plus normalized Cayley-distance halving and inversion-symmetric tie retention uniquely forces the finite Viète refinement inside the declared cycle-cover architecture;
- the coarse three-ray cycle refines through `C3 <- C6 <- C12 <- C24 <- ...`;
- the finite completion constant `Pi_rot` exists, is internally bracketed, has intrinsic quadratic precision gain, and equals the independently generated Wallis completion constant `tau` before classical pi is named.

The remaining native question is no longer the algebra of Viète. It is whether current Cell/trace rotation semantics selects the two extra global ingredients required by the cycle-cover realization.

This note isolates those ingredients exactly.

## 2. Existing C3/C2 holonomy theorem is reused, not duplicated

Current main contains the accepted finite `C3` / `C2` bare-slice benchmark from PR #908. Its exact finite carrier is:

- coarse overlap graph: a simple triangle `C3`;
- local frame fiber: `C2`;
- edge transport: `sigma -> sigma XOR a_ij`;
- vertex gauge group: `C2^3`.

For edge bits

\[
a=(a_{01},a_{12},a_{20})\in\mathbf F_2^3,
\]

the complete gauge invariant is

\[
\boxed{H(a)=a_{01}\oplus a_{12}\oplus a_{20}.}
\]

There are exactly two edge-transport gauge orbits, `H=0` and `H=1`. The same accepted benchmark also separates this transport class from global effectivity: a nonzero holonomy packet can be a legitimate twisted globalization under one effectivity contract and have no global object under another.

Therefore #1158 does **not** claim a new general `H^1` or holonomy theorem. It specializes the existing finite `C3/C2` classifier to the orientation-cover question.

Freeze:

`VIETE_C3_C2_HOLONOMY = SPECIALIZATION_OF_EXISTING_C3_C2_TRANSPORT_CLASSIFIER`.

`HOLONOMY_CLASSIFICATION != NATIVE_ROTATION_EFFECTIVITY_OR_SELECTION`.

## 3. The transport packet is exactly a two-fold cover of the coarse rotation cycle

Construct the lifted state set

\[
\widetilde X=\{0,1,2\}\times\mathbf F_2.
\]

The first coordinate is the coarse three-ray orientation state and the second coordinate is a two-sheet orientation/sweep fiber.

For each directed coarse edge `i -> i+1 mod 3`, define the lift

\[
(i,\sigma)\longmapsto(i+1,\sigma\oplus a_i),
\]

where `(a_0,a_1,a_2)` is the edge packet.

After one full coarse turn,

\[
(i,\sigma)\longmapsto(i,\sigma\oplus H).
\]

Hence:

### H=0

One coarse loop returns the sheet to itself. The lifted graph has two connected components, each a three-cycle:

\[
\boxed{\widetilde X\cong C_3\sqcup C_3.}
\]

### H=1

One coarse loop exchanges the two sheets. Only after two coarse loops does the full state return. The lifted graph is one six-cycle:

\[
\boxed{\widetilde X\cong C_6.}
\]

Thus the earlier #1158 direct calculation

`connected double cover of C3 <=> odd C2 monodromy`

is precisely the `H=1` specialization of the existing C3/C2 gauge classifier.

Freeze:

\[
\boxed{C_3\to C_6\quad\Longleftrightarrow\quad H=1}
\]

at the finite cover-graph level.

This equivalence does not say that native Cell rotation must realize the `H=1` class.

## 4. Matched Cell-rotation countermodels

We now show that the currently frozen local rotating-segment semantics does not select between `H=0` and `H=1`.

Use the same state type in both models:

\[
S=(\rho,k,\epsilon),
\]

where:

- `rho` is one fixed radius label;
- `k in C3` is the same coarse positive-ray/slice orientation state;
- `epsilon in C2` is the same two-valued sweep-orientation fiber.

Both models have:

1. one instantaneous Cell/state per trajectory step;
2. the same coarse transition `k -> k+1` under positive sweep;
3. a two-valued local orientation state;
4. negative sweep equal to the inverse of positive sweep;
5. translation/homogeneity at the coarse cycle level;
6. the same local cardinalities and one-edge transport type.

The only difference is the global transport class around the three-edge loop.

### Model M0 — trivial holonomy

Choose the gauge representative

\[
a=(0,0,0).
\]

Then

\[
R_0(k,\epsilon)=(k+1,\epsilon),
\qquad
R_0^{-1}(k,\epsilon)=(k-1,\epsilon).
\]

The positive-sweep state graph is two disjoint three-cycles.

### Model M1 — nontrivial holonomy

Choose the cyclically homogeneous representative

\[
a=(1,1,1).
\]

Then

\[
R_1(k,\epsilon)=(k+1,\epsilon\oplus1),
\qquad
R_1^{-1}(k,\epsilon)=(k-1,\epsilon\oplus1).
\]

Here

\[
R_1^3(k,\epsilon)=(k,\epsilon\oplus1),
\qquad
R_1^6=\mathrm{id},
\]

so the positive-sweep state graph is one six-cycle.

Both models satisfy the currently declared local state/reversal architecture. They disagree on whether one coarse three-ray circuit flips the orientation sheet.

Moreover, on every proper tree/path obtained by cutting one edge of `C3`, the two transport packets are gauge equivalent, because the accepted benchmark proves that a path has only one edge-transport gauge orbit. Therefore the distinction is genuinely loop-global rather than a hidden local difference.

We obtain the exact no-go:

\[
\boxed{
\text{CURRENT LOCAL CELL/ORIENTATION SEMANTICS DOES NOT SELECT }H=1.
}
\]

Any theorem promoting the six-gate connected cover to native strength must use additional loop-global information.

## 5. Effectivity is an additional boundary even after H is known

The existing C3/C2 benchmark gives a further warning. The same `H=1` transport packet may be classified as:

- `TWISTED_GLOBALIZATION`, if the effectivity contract accepts the nontrivial loop class;
- `NO_GLOBAL_OBJECT`, if it does not.

For #1158, a native six-gate rotation cover requires not only the abstract statement `H=1`, but that the native rotation grammar actually treats this nontrivial class as effective.

Thus the precise native condition is better written

\[
\boxed{
H=1\quad\text{and}\quad 1\in E_{\rm rot}
}
\]

for whatever rotation-specific effectivity contract `E_rot` is eventually derived.

No such contract is currently supplied merely by P000 or by the one-Cell-per-step rule.

Freeze:

`NONTRIVIAL_HOLONOMY != NATIVE_EFFECTIVITY`.

`NATIVE_C6_REFINEMENT_REQUIRES_EFFECTIVE_NONTRIVIAL_HOLONOMY`.

## 6. The local epsilon fiber itself is not the obstruction

Current rotating-segment semantics already requires a two-valued local sweep orientation `epsilon` in the minimum candidate state `(rho,C,epsilon)`.

The G1 quarter-root pair `Q={q_+,q_-}` is also a free `C2` torsor under turn-sense reversal.

Any two free transitive two-element `C2` torsors admit exactly two equivariant bijections, differing by a global sign relabeling. Therefore the existence of a local orientation-fiber map

\[
\epsilon\text{-torsor}\longrightarrow Q
\]

is automatic up to one global chirality gauge.

This does **not** determine loop transport of epsilon. The local torsor and its global holonomy are distinct data.

Hence the native obstruction has now moved from

`DO WE HAVE TWO ORIENTATION STATES?`

to

`HOW ARE THOSE TWO STATES TRANSPORTED AROUND A CLOSED ROTATION LOOP?`

## 7. Connected cover still does not select the Viète root section

Assume now that the nontrivial class is effective and we have the connected binary refinement

\[
p:C_{2N}\to C_N,
\qquad
p(j)=j\pmod N.
\]

For every coarse state `k in C_N`, there are exactly two lifts/root states:

\[
k,\qquad k+N\quad\text{in }C_{2N}.
\]

Connectedness and inversion symmetry alone do not choose which lift realizes the half-refinement.

Let

\[
d_M(j)=\min(j,M-j)
\]

be the Cayley graph distance to identity in `C_M`.

For a non-antipodal coarse state, one lift is strictly nearer to identity and the other is strictly farther. There are therefore two global inversion-equivariant choices:

- `s_near(k)` — the nearer lift;
- `s_far(k)` — the farther lift.

They both satisfy

\[
p(s(k))=k
\]

and inversion equivariance

\[
s(-k)=-s(k),
\]

away from the antipodal tie, yet only the near section satisfies

\[
\boxed{
\frac{d_{2N}(s_{\rm near}(k))}{2N}
=
\frac12\frac{d_N(k)}{N}.
}
\]

The far section violates exact distance halving.

At a coarse half-turn, the two lifts are tied and inversion exchanges them; symmetry requires retaining both as the quarter-root pair.

Therefore:

\[
\boxed{
\text{EFFECTIVE CONNECTED BINARY COVER DOES NOT IMPLY VIETE SHORTEST-ROOT REFINEMENT.}
}
\]

The normalized-distance-halving/shortest-lift clause is a second independent extension.

## 8. Exact two-clause native promotion boundary inside the cycle-cover architecture

Combining the previous results gives a sharper form of the #1158 native gap.

The current substrate already supplies or tolerates:

- coarse `C3` positive-ray cyclic structure at the orientation-readout level;
- a local two-valued sweep-orientation fiber;
- inversion/reversal of sweep;
- one Cell per instantaneous trajectory state;
- finite algebraic normalized-root dynamics once a fine orientation state is declared.

To force the Viète six-gate/dyadic refinement at native cycle-cover strength, two **independent** global clauses remain:

### Clause A — effective nontrivial binary holonomy

At each binary refinement layer, the `C2` transport class around the coarse cycle is nontrivial and effective:

\[
H=1,\qquad1\in E_{\rm rot}.
\]

This chooses the connected double cover rather than two disconnected copies.

### Clause B — normalized shortest-root section

Among the two lifts of every non-antipodal orientation state, refinement chooses the unique lift minimizing normalized Cayley distance to identity; at the antipodal tie it retains both inversion-related minimizers.

This yields exact normalized-distance halving.

Together A+B are sufficient for the finite Viète root tower already proved in the parent notes.

They are independently necessary within this architecture:

- without A, the same local data admits the disconnected `C_N sqcup C_N` refinement;
- without B, the same connected cover admits an inversion-equivariant far-root section that does not halve precision distance.

Thus:

\[
\boxed{
\text{NATIVE VIETE CYCLE-COVER PROMOTION}
\iff
\text{EFFECTIVE NONTRIVIAL HOLONOMY}
+
\text{SHORTEST-ROOT DISTANCE HALVING}
}
\]

within the explicitly declared finite cycle-cover architecture and the already-frozen symmetry/tie-retention rules.

This is a necessity/sufficiency statement about that architecture class, not a universal theorem about every conceivable native rotation ontology.

## 9. Repeated tower: one loop-global decision at every precision lift

The same elementary calculation works for any cycle `C_N` with a `C2` edge-transport fiber. The XOR of all edge flip bits is invariant under vertex gauge. The lifted two-sheet cover is connected iff this total holonomy is nonzero.

Therefore the coherent tower

\[
C_3\leftarrow C_6\leftarrow C_{12}\leftarrow C_{24}\leftarrow\cdots
\]

requires the nontrivial effective `C2` class at every binary cover stage.

Nothing in the mere existence of the previous connected layer forces the next layer's class. Each precision lift contains one new loop-global binary transport choice before the shortest-root section is applied.

This gives a concrete information interpretation of dyadic rotation precision:

- local state count doubles;
- one new binary cover sheet is introduced;
- its connectedness is controlled by one new global `C2` loop class;
- the Viète precision law then chooses the near/root section and halves normalized graph distance.

## 10. Current strongest #1158 verdict

The mother problem is now split into three strengths.

### Closed at G1/G2 finite-refinement strength

- exact target-free nested radical recursion;
- normalized equal-resultant square-root theorem;
- finite gate/cycle root refinement and exact normalized-distance halving;
- scalar branch-free shell circuit;
- target-free monotone and two-sided certified completion;
- intrinsic `1/4` scalar error law and quadratic gate-count precision law;
- exact precision/state-complexity tradeoffs;
- internal equality `Pi_rot=tau=2W_inf` with the Wallis completion constant.

### Closed at finite native-information/no-go strength

- bare Cell/trace/path state is insufficient to generate the oriented refinement;
- radial T11 path order is not fixed-radius rotation chirality;
- absolute chirality labeling is gauge;
- local `C2` orientation fiber alone does not determine connected six-gate transport;
- existing C3/C2 holonomy classification gives the exact missing loop bit;
- connected cover alone does not determine the shortest-root section.

### Still open at G0 native-dynamics strength

Derive, rather than stipulate, why actual Enterprise Cell rotation satisfies:

1. effective nontrivial `C2` holonomy at each binary precision cover;
2. normalized shortest-root/distance-halving refinement.

Current P000 and current one-Cell rotation semantics do not select either clause uniquely.

That is now the entire remaining native content of #1158 inside the cycle-cover route.
