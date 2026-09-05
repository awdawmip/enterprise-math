# Viète rotation: physical phase refinement is not the precision pro-state clock

Status: `FREE_RESEARCH / EXACT TYPING NO-GO + REFACTORED TARGET / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Parent issue: `#1255`
Parent line: `#1158`
Depends on:
- `research_notes/VIETE_PIVOT_LOCAL_TRANSLATION_QUOTIENT_C12_20260905.md`
- `research_notes/VIETE_ROTATION_PRECISION_PROSTATE_FIRST_WINDING_20260905.md`
- `research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md`
- `research_notes/VIETE_X6_PROSTATE_PERIODICITY_MEMORY_NO_GO_20260905.md`
Checker: `experiments/viete_phase_precision_clock_separation_20260905/check_phase_precision_clock_separation.py`
Checker source commit: `ad8864e62a746abe4a26c6963fa395f61dab1aa1`

## 1. The key typing problem

Two different refinement structures currently use the same family of cyclic cardinalities

\[
C_6,C_{12},C_{24},\ldots
\]

but they use **different arrows**.

### Physical phase refinement

The proved local physical C12 source is

\[
E_k\to G_k\to E_{k+1}.
\]

If C12 is indexed in temporal order by

\[
E_k\leftrightarrow [2k]_{12},
\qquad
G_k\leftrightarrow [2k+1]_{12},
\]

then the old C6 Cell phase `k` is embedded by

\[
\iota_0([k]_6)=[2k]_{12}.
\]

A coarse Cell-to-Cell phase step is two fine C12 steps.

### Precision pro-state refinement

The already-proved precision observer tower uses

\[
P_{\rm rot}=\varprojlim_m C_{6\cdot2^m}
\]

with residue projection

\[
p_m([q]_{2N})=[q]_N,
\qquad N=6\cdot2^m.
\]

This projection preserves the **same residue address** across precision levels. The prior pro-state theorem explicitly states that changing `m` is a change of resolution, not physical time evolution.

These are not the same structure.

## 2. General physical phase embedding law

Let

\[
N_m=6\cdot2^m,
\qquad
Q_m([k])=[k+1]_{N_m}.
\]

The phase-preserving embedding of a coarse phase into the doubled phase grid is

\[
\iota_m([k]_{N_m})=[2k]_{N_{m+1}}.
\]

Then

\[
\begin{aligned}
\iota_m(Q_m[k])
&=[2k+2]_{N_{m+1}}\\
&=Q_{m+1}^2([2k]_{N_{m+1}})\\
&=Q_{m+1}^2(\iota_m[k]).
\end{aligned}
\]

Therefore

\[
\boxed{
\iota_m\circ Q_m
=Q_{m+1}^2\circ\iota_m.
}
\]

But

\[
\boxed{
\iota_m\circ Q_m
\neq
Q_{m+1}\circ\iota_m.
}
\]

So physical dyadic refinement is a **time-dilation/refinement relation**: one coarse phase step corresponds to two fine phase steps.

## 3. Precision projection uses a different commuting square

The standard residue projection

\[
p_m:C_{N_{m+1}}\to C_{N_m},
\qquad
p_m([q])=[q]\pmod{N_m}
\]

satisfies

\[
\boxed{
p_m\circ Q_{m+1}=Q_m\circ p_m.
}
\]

This is the ordinary synchronous odometer/projective relation.

However it does **not** undo the physical phase embedding:

\[
p_m(\iota_m[k])=[2k]_{N_m},
\]

which is generally not `[k]`.

Thus

\[
\boxed{
p_m\circ\iota_m\neq \mathrm{id}.
}
\]

The precision projection and physical coarse-phase collapse are different maps.

## 4. Exact C6/C12 contradiction for a synchronous physical collapse

Suppose a total map

\[
f:C_{12}\to C_6
\]

were required to satisfy both:

1. preserve the old physical Cell phases,
   \[
f(E_k)=k;
   \]
2. intertwine one fine successor with one coarse successor,
   \[
fQ_{12}=Q_6f.
   \]

Set `E_0` to phase zero. Then

\[
f(E_0)=0.
\]

One fine step gives

\[
f(G_0)=1.
\]

A second fine step gives

\[
f(E_1)=2.
\]

But physical old-phase preservation requires

\[
f(E_1)=1.
\]

Contradiction.

Therefore

\[
\boxed{
\text{NO TOTAL C12->C6 MAP CAN BOTH PRESERVE THE PHYSICAL OLD PHASES AND COMMUTE WITH ONE-STEP SUCCESSOR.}
}
\]

This is not a numerical approximation issue. It is an exact clock/refinement mismatch.

## 5. The physical collapse exists, but it is a two-step semiconjugacy

Using canonical representatives

\[
q\in\{0,1,\ldots,2N-1\},
\]

define the typed temporal collapse

\[
r_m([q]_{2N})=[\lfloor q/2\rfloor]_N.
\]

At the first physical layer,

\[
r_0(E_k)=r_0(G_k)=k.
\]

It is a left inverse of the physical embedding:

\[
\boxed{r_m\circ\iota_m=\mathrm{id}.}
\]

It does not commute with one fine step. Instead

\[
\boxed{
r_m\circ Q_{m+1}^2
=Q_m\circ r_m.
}
\]

This is exactly the physical statement

\[
E_k\to G_k\to E_{k+1}.
\]

`r_m` is a typed set/readout map, not the group-homomorphic precision projection `p_m`.

## 6. Two arrows must now be frozen separately

The same finite cyclic labels support two distinct roles:

### Precision-collapse arrow

\[
\boxed{
p_m([q])=[q]\bmod N_m}
\]

Role:
- same pro-state observed at coarser resolution;
- compatible root/character readout;
- `m` is precision depth;
- synchronous `+1` algebraic translation commutes with projection.

### Physical phase-collapse arrow

\[
\boxed{
r_m([q])=[\lfloor q/2\rfloor]}
\]

on the declared refined phase grid.

Role:
- coarse physical phase obtained from two fine phase slots;
- one coarse successor = two fine successors;
- Cell/gate parity is the residual distinguishing the two fine slots;
- not a group homomorphism and not the pro-state bonding map.

Freeze:

\[
\boxed{
\text{PRECISION PROJECTION }p_m
\neq
\text{PHYSICAL PHASE COLLAPSE }r_m.
}
\]

and

\[
\boxed{
\text{PRECISION DEPTH CHANGE}
\neq
\text{PHYSICAL TIME STEP}.
}
\]

## 7. Consequence for the #1255 mother question

The #1255 wording asks for one trajectory-to-pro-state construction respecting actual native transition composition, finite phase successor, first Cell-gate refinement, and compatible precision readouts.

The exact C6/C12 calculation shows that this cannot mean a single **synchronous** factorization in which one native/fine transition becomes `+1` at every level of the ordinary inverse-limit system.

That interpretation is already impossible at the first physical refinement.

Therefore the synchronous reading receives the stronger disposition

\[
\boxed{
\texttt{NO_GO__SYNCHRONOUS_TRAJECTORY_SUCCESSOR_TO_PRECISION_INVERSE_LIMIT}.
}
\]

The periodicity theorem from the previous note remains valid under that same explicit lease, but the present C6/C12 clock mismatch is earlier and stronger: it kills synchronous compatibility before any infinite-level argument is needed.

## 8. Corrected architecture: trajectory base and precision fiber

The prior pro-state theorem already supplied the conceptual clue:

> changing precision level `m` is not physical time evolution.

The new native C12 lift supplies the complementary statement:

> physical local transition refinement has its own Cell/gate temporal clock.

Therefore the correct object should not be a simple quotient

\[
\text{trajectory state}\to P_{\rm rot}
\]

with one shared successor.

The minimal retyped architecture is instead a two-axis object

\[
\boxed{
\mathcal B
=
\text{TRAJECTORY PHASE BASE}
\times
\text{PRECISION/ROOT FIBER}.
}
\]

At minimum it must carry two different operations:

1. **time/trajectory transition** `T`, acting on the physical Cell/Cell-gate base;
2. **precision refinement/readout** `R`, acting on or reading the pro-state fiber.

They must not be identified by default.

A candidate local first layer is

\[
\mathcal B_{12}
=
\{E_k,G_k\}_{k\bmod6}
\times
\mathcal A,
\]

where `A` is a typed precision-address fiber whose semantic generation remains to be proved.

The principal Viète pro-state can then describe a refinement lineage/character address without pretending that moving to the next precision level is a Cell-time event.

## 9. A more precise interpretation of the principal pro-state

The distinguished point

\[
x_{\rm Viete}=3\in P_{\rm rot}
\]

has finite readouts

\[
[3]_{6},[3]_{12},[3]_{24},\ldots.
\]

These represent:

- half-turn at C6 character scale;
- quarter-turn at C12 character scale;
- eighth-turn at C24 character scale;
- and so on.

Therefore those coordinates are **not the same physical angular phase at successive time resolutions**. They are the compatible scale-root readouts of one precision address.

This makes the typing explicit:

\[
\boxed{
P_{\rm rot}\text{ IS A ROOT/PRECISION LINEAGE CARRIER, NOT A SYNCHRONOUS PHYSICAL TRAJECTORY PHASE SPACE.}
}
\]

That statement is fully compatible with the existing theorem that `m` is resolution depth rather than native time.

## 10. Why a pure winding counter does not yet solve the problem

One can remove the finite-period obstruction by replacing a periodic physical cycle with its universal history cover and retaining an unbounded winding integer `n`.

The diagonal residues

\[
([n]_{6\cdot2^m})_m
\]

do define a point of `P_rot`, and incrementing `n` gives the synchronous algebraic `+1` translation.

However this construction alone is only a **clock factorization**. It does not prove that the higher precision coordinates are generated by the native half-angle/refinement geometry rather than by an external step counter.

Moreover, the physical C12/C6 relation still has the two-fine-steps/one-coarse-step law above.

Therefore freeze:

`UNBOUNDED_WINDING_COUNTER -> REMOVES PERIODICITY OBSTRUCTION BUT DOES NOT BY ITSELF PROVE ROTATION-PRECISION SEMANTICS`.

This blocks a trivial circular solution to #1255.

## 11. BRC observer consequence

Erasing Cell/gate parity from C12 is already known to be unsafe for one-step physical successor.

The present theorem sharpens why: the parity bit is precisely the local clock-phase residual needed to distinguish

\[
\text{stay in coarse index}
\quad\text{from}\quad
\text{advance coarse index}.
\]

Thus the BRC observer-loss test separates two independent kinds of hidden information:

1. `CELL/GATE` parity — physical fine-clock residual;
2. higher pro-state bits — precision/root-address residual.

Neither may be silently substituted for the other.

Freeze:

\[
\boxed{
\text{PHYSICAL CLOCK RESIDUAL}
\neq
\text{PRECISION ADDRESS RESIDUAL}.
}
\]

Combined with the earlier result:

\[
\boxed{
\text{BRC PATH BRANCH BIT}
\neq
\text{CELL/GATE CLOCK BIT}
\neq
\text{DEEP DYADIC PRECISION BITS}.
}
\]

These are three different information layers.

## 12. Updated frontier

The original synchronous factorization problem is now refuted at the first physical refinement.

The stronger surviving research problem is:

> construct an operation-safe **bundle/cocycle** linking native trajectory evolution to a separate precision/root pro-state, with explicitly different time and refinement operators, and prove how native history selects or updates the precision fiber without importing it from the target by definition.

A successful future theorem should specify at least:

- physical base state and its transition `T`;
- precision fiber and refinement/readout operator `R`;
- any cocycle assigning precision information to a native transition/history segment;
- translation/rotation/reversal covariance;
- BRC provenance lease for path branch, physical clock parity, and deep precision bits separately;
- the exact compatibility law replacing the false synchronous square.

The first compatibility law to preserve is already known:

\[
\boxed{
\iota_m Q_m=Q_{m+1}^2\iota_m,
}
\]

not

\[
\iota_m Q_m=Q_{m+1}\iota_m.
\]

This retyping is the current strongest route toward a genuinely native trajectory/precision bridge.
