# Viète six-gate refinement as minimal winding-parity memory over the coarse C3 cycle

Status: `FREE_RESEARCH / EXACT ONE-BIT PROCESS-AUGMENTATION THEOREM + NATIVE-STATUS BOUNDARY / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`

## 1. Motivation

The corrected #1158 typing shows that the `C2` deck sheet needed for

\[
C_3\leftarrow C_6
\]

is not the same object as the already-frozen sweep/chirality variable `epsilon`, and it cannot be silently inherited from either the bidirectional segment pair or FCC carrier antipodes.

This leaves a different possibility:

> the deck sheet is not an extra spatial negative direction at all, but the minimum finite memory needed to remember loop history that the coarse `C3` position quotient forgets.

This note proves that one-bit winding parity is exactly the minimal such process-state augmentation.

## 2. Coarse directed cycle

Let the coarse orientation quotient be

\[
X=C_3=\{0,1,2\}
\]

with positive transition

\[
r(k)=k+1\pmod3.
\]

A coarse state records only the current ray/slice label.

After three positive transitions,

\[
r^3(k)=k.
\]

Therefore the coarse state alone cannot distinguish:

- a path ending at `k` with zero completed coarse windings;
- a path ending at the same `k` after one completed winding;
- or any two histories differing by an integer number of full coarse loops.

This is an exact information loss of the quotient.

## 3. Universal integer lift and winding number

Lift the coarse directed cycle to the integer line

\[
\widetilde X=\mathbf Z
\]

with transition

\[
\widetilde r(n)=n+1
\]

and projection

\[
p(n)=n\pmod3.
\]

For a lifted path ending at integer `n`, write uniquely

\[
n=3w+k,
\qquad k\in\{0,1,2\}.
\]

The integer

\[
w\in\mathbf Z
\]

is the winding count relative to the chosen lift/base convention.

The full integer winding is more information than required for the first binary refinement.

Reduce it modulo two:

\[
\boxed{\beta:=w\pmod2\in\mathbf F_2.}
\]

Call `beta` the winding-parity memory.

## 4. The one-bit augmented state is exactly C6

Use the finite augmented state

\[
Y=C_3\times\mathbf F_2.
\]

In the cut representative where the parity bit flips only on the edge `2 -> 0`, define

\[
R(0,\beta)=(1,\beta),
\]

\[
R(1,\beta)=(2,\beta),
\]

\[
R(2,\beta)=(0,\beta\oplus1).
\]

Starting from `(0,0)`, one obtains

\[
(0,0)\to(1,0)\to(2,0)\to(0,1)\to(1,1)\to(2,1)\to(0,0).
\]

Therefore

\[
\boxed{Y\text{ with }R\cong C_6.}
\]

One coarse winding flips `beta`; two coarse windings return the full augmented state.

This is the same nontrivial `C2` holonomy class already isolated by the finite `C3/C2` transport theorem.

## 5. Cut location is gauge, winding parity is invariant

The rule above chose the edge `2 -> 0` as the location where the local bit flips.

A different choice of cut moves the visible flip to another edge. More generally, vertex relabeling of the local `C2` fiber changes the edge flip packet by a `C2^3` gauge transformation.

The XOR of the three edge bits is unchanged:

\[
H=a_{01}\oplus a_{12}\oplus a_{20}=1.
\]

Hence the location of the local toggle is presentation/gauge, while odd winding parity is the gauge-invariant global content.

Freeze:

`LOCAL_CUT_POSITION = GAUGE`.

`ODD_WINDING_PARITY = GAUGE_INVARIANT_COVER_CLASS`.

## 6. Necessity: no current-position-only state can retain winding parity

Suppose an augmented process wants to distinguish two histories that:

1. end at the same coarse state `k`;
2. differ by one full coarse winding.

Any state function factoring only through current coarse position

\[
f:C_3\to Z
\]

assigns them the same state because their endpoint in `C3` is identical.

Therefore some information beyond current coarse position is necessary.

At least two values are required to distinguish even from odd winding count. Hence the information lower bound is

\[
\boxed{\text{at least one bit}.}
\]

The parity state `beta in F2` achieves this lower bound exactly.

Thus:

\[
\boxed{
\text{one bit is necessary and sufficient to retain the first nontrivial closed-loop history of }C_3.
}
\]

## 7. Uniqueness at one-bit loop-sensitive strength

Consider any two-sheet process augmentation of the directed `C3` state with local `C2` transport.

The accepted finite transport classifier proves that edge packets have exactly two gauge classes:

- trivial loop class `H=0`;
- nontrivial loop class `H=1`.

A one-bit augmentation is **loop-sensitive** precisely when one coarse winding changes the internal sheet. That condition is exactly

\[
H=1.
\]

Therefore, up to `C2` gauge/isomorphism, there is only one nontrivial one-bit loop-sensitive augmentation:

\[
\boxed{C_6.}
\]

This is a minimality/uniqueness theorem inside the declared two-sheet process-memory class.

It does not say current P000 requires loop sensitivity.

## 8. Relation to time and process memory

P000 types time separately from the six spatial dimensions and gives it the role

`TIME_ROLE = TRACE_AND_ORDER_OF_RELATIONAL_CHANGE`.

The discrete rotation correction also explicitly allows additional finite memory if previous-cell/incoming-edge data is proved necessary.

The winding-parity variable `beta` fits this pattern:

- it does not add a second simultaneous Cell;
- it does not add a native negative spatial axis;
- it is derived from the ordered transition history;
- the instantaneous spatial state can remain one Cell;
- the extra bit records a process relation lost by the coarse positional quotient.

Thus the augmentation is **compatible in type** with current process semantics.

Compatibility is not derivation: P000 does not presently require that this specific loop-history bit be retained.

## 9. Character meaning of the history bit

Once the six-state augmented cycle is given a finite character readout, the deck involution

\[
\beta\mapsto\beta\oplus1
\]

is represented by multiplication by the half-turn character

\[
-1.
\]

Therefore the classical-looking negative sign can emerge as the character of odd winding parity:

\[
\boxed{
\text{ODD WINDING MEMORY}
\xrightarrow{\text{character}}
-1.
}
\]

This does not require a primitive native negative axis.

It gives a cleaner interpretation of the `H` deck operation in #1158: `H` may be a process-history sheet whose character readout is a half-turn, rather than an underlying signed spatial coordinate.

## 10. First quarter roots and sweep chirality

At the next binary refinement

\[
C_6\leftarrow C_{12},
\]

the half-turn character state has two quarter roots.

At that special quarter-turn orbit, direction/deck inversion `H` and sweep inversion `S` exchange the same two roots. Therefore the already-existing local sweep variable `epsilon` may label the two quarter-root branches up to a global chirality gauge.

One refinement later, the `V4` theorem shows `H` and `S` separate again. The winding-parity bit should therefore not be identified globally with sweep `epsilon`.

## 11. A precise optional extension principle

The six-gate cover becomes forced if one adds the following finite-precision principle:

> **FIRST LOOP-HISTORY RETENTION:** when refining a coarse cyclic orientation quotient by one binary precision level, retain the smallest nontrivial gauge-invariant closed-loop history distinguishable from current position.

For `C3`, the smallest such history is winding parity in `F2`, and the unique connected one-bit refinement is `C6`.

This principle is not currently Foundation. It is an explicit candidate extension whose mathematical consequence is now exact and noncircular.

Freeze boundary:

`FIRST_LOOP_HISTORY_RETENTION => C3_TO_C6_CONNECTED_COVER`.

`CURRENT_P000 => FIRST_LOOP_HISTORY_RETENTION` is **not proved**.

## 12. Repeated binary precision

The same idea iterates.

After retaining winding modulo `2`, a further binary refinement can retain winding modulo `4`, then modulo `8`, and so on. At finite level the process address is

\[
w\pmod{2^m}.
\]

Together with the coarse `C3` position this gives

\[
C_3\times\mathbf Z/2^m\mathbf Z
\cong
C_{3\cdot2^m}.
\]

Taking coherent inverse limits yields the profinite precision carrier already proved:

\[
\boxed{C_3\times\mathbf Z_2.}
\]

Thus the 2-adic factor has a direct process-memory meaning:

\[
\boxed{
\mathbf Z_2
=
\text{coherent all-depth binary winding-resolution memory}.
}
\]

This is stronger and more native-looking than interpreting `Z_2` as an abstract number-theoretic decoration.

## 13. Precision as winding-resolution, not decimal resolution

At level `m`, the additional state does not say “we know a real angle to m bits”. It says:

\[
\text{we distinguish winding/process histories modulo }2^m.
\]

The finite character readout translates that relational precision into a root-of-unity phase, whose even half-traces become the Viète radicals.

Hence the candidate causal chain is

```text
ordered Cell/ray transition history
    -> retain winding modulo 2^m
    -> C_{3*2^m} finite gate state
    -> finite character root tower
    -> Viète nested radical half-trace
    -> target-free scalar completion Pi_rot
```

The real/continuous phase remains a later compatibility layer.

## 14. Current status

This note closes an **existence/minimality route** for the missing direction/deck sheet at process-memory strength:

- one bit of winding parity is sufficient;
- one bit is necessary to distinguish one extra coarse winding;
- the nontrivial one-bit class is unique up to gauge;
- its state graph is exactly `C6`;
- repeated retention gives the `C3 x Z_2` precision carrier.

What remains open at native G0 strength is whether actual Enterprise rotation must retain this loop-history information as part of its effective state/precision semantics.

Thus the direction-sheet problem has changed from

`NO CONSTRUCTION KNOWN`

to

\[
\boxed{
\text{MINIMAL PROCESS-MEMORY CONSTRUCTION PROVED; NATIVE NECESSITY/PHYSICAL EFFECTIVITY OPEN}.
}
