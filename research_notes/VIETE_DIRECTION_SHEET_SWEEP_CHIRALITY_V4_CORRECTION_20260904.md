# Viète binary-type correction: direction-reversal deck sheet versus sweep chirality, and the V4 refinement square

Status: `FREE_RESEARCH / SEMANTIC CORRECTION + EXACT FINITE SYMMETRY THEOREM / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Corrects/narrows: `research_notes/VIETE_C3_C2_HOLONOMY_NATIVE_PROMOTION_BOUNDARY_20260904.md` (`cd6dd818...`)

## 1. Correction

The parent holonomy note used one symbol `epsilon` for the two-sheet fiber of the `C3 -> C6` cover and described it as an orientation/sweep fiber.

That identification is too strong.

Two different `C2` operations have already been distinguished in the #1158 line:

\[
H(u)=-u
\]

for **half-turn / directed-segment reversal**, and

\[
S(u)=u^{-1}
\]

for **turn-sense / sweep-chirality reversal**.

Current discrete rotating-segment state semantics uses an `epsilon` intended to distinguish the two local sweep orientations. It is therefore naturally `S`-typed.

By contrast, the deck involution of the binary state cover

\[
C_{2N}\to C_N
\]

is the half-period translation and is naturally `H`-typed.

Therefore:

\[
\boxed{
C2_{\rm cover\;deck}\neq C2_{\rm sweep}
}
\]

in general.

They must not be identified merely because both have two elements.

## 2. What survives from the parent holonomy theorem

The finite holonomy calculation itself is unchanged if its sheet coordinate is retyped as an **abstract direction/deck sheet**

\[
\beta\in C_2^H
\]

rather than the frozen sweep variable `epsilon`.

For a triangle `C3` with `C2^H` edge transports, the XOR holonomy

\[
H_{\rm loop}=a_{01}\oplus a_{12}\oplus a_{20}
\]

still classifies the two gauge orbits:

- `H_loop=0` -> disconnected `C3 sqcup C3`;
- `H_loop=1` -> connected `C6`.

The exact checker `research_checks/VIETE_C3_C2_HOLONOMY_NATIVE_PROMOTION_CHECK_20260904.py` remains valid at this abstract deck-sheet strength.

What is **not** valid without a new bridge is the stronger sentence that current native sweep `epsilon` itself is this deck sheet.

Freeze:

`C3_C2_HOLONOMY_CHECKER = VALID_FOR_ABSTRACT_DECK_SHEET`.

`ABSTRACT_DECK_SHEET != CURRENT_SWEEP_EPSILON_WITHOUT_BRIDGE`.

## 3. Finite cyclic model of the two involutions

Let

\[
G=C_N=\mathbf Z/N\mathbf Z,
\]

with `N` even.

Define the half-turn/deck involution

\[
\boxed{H_N(k)=k+N/2\pmod N}
\]

and turn-sense inversion

\[
\boxed{S_N(k)=-k\pmod N}.
\]

Both are involutions. They commute:

\[
H_NS_N(k)
=-k+N/2
=S_NH_N(k).
\]

Hence they generate an action of

\[
\boxed{V_4=C_2^H\times C_2^S}
\]

on the finite orientation states, except that individual state orbits may degenerate when a stabilizer is present.

## 4. H and S coincide exactly on quarter-turn states

Solve

\[
H_N(k)=S_N(k).
\]

This is

\[
k+N/2\equiv-k\pmod N,
\]

or

\[
2k\equiv N/2\pmod N.
\]

If `4|N`, the solutions are exactly

\[
\boxed{k=N/4,\qquad k=3N/4.}
\]

These are the two quarter-turn states.

Thus:

\[
\boxed{
H=S\text{ on the quarter-turn orbit, but }H\neq S\text{ generically.}
}
\]

This explains a persistent ambiguity in the early #1158 seed analysis: at the first root of the half-turn, direction reversal and sweep reversal exchange the same two states, so the two different binary structures are observationally collapsed at that resolution.

## 5. The V4 orbit appears immediately at the next refinement

At the `C12` quarter-turn seed, take

\[
k=3=N/4.
\]

Then

\[
H_{12}(3)=9=S_{12}(3),
\]

so the orbit has only two states:

\[
\{3,9\}.
\]

Now refine to `C24` and take the positive principal root state `k=3`.

The four `V4` images are

\[
\boxed{
3,\quad
H(3)=15,\quad
S(3)=21,\quad
HS(3)=9.
}
\]

All four are distinct.

They have different typed roles:

- `3` = positive-sweep principal root;
- `15=H(3)` = half-turn/deck mate, the far root of the same positive parent;
- `21=S(3)` = opposite-sweep principal root;
- `9=HS(3)` = far root of the opposite-sweep parent.

Thus the first nondegenerate deep refinement is naturally a four-state square, not one binary pair.

## 6. General deep Viète V4 orbit

At gate level

\[
G_m=C_{3\cdot2^m},
\qquad m\ge2,
\]

the positive principal Viète state is represented by

\[
q_{+,m}=3.
\]

Its sweep-inverse principal mate is

\[
q_{-,m}=S(q_{+,m})=-3.
\]

At `m=2` (`N=12`) these are quarter-turn states and the `V4` orbit collapses to two elements.

For every

\[
m\ge3,
\]

`3` is not a quarter-turn state, because

\[
3\neq\frac{3\cdot2^m}{4}.
\]

Therefore the orbit is exactly

\[
\boxed{
\{3,\;3+N/2,\;N-3,\;N/2-3\}
}
\]

with four distinct elements.

This proves that deep Viète precision intrinsically separates two binary questions:

1. `H`: principal versus antipodal/far root inside one parent-root fiber;
2. `S`: positive versus negative turn-sense/chirality branch.

## 7. Character-level action table

Let a finite character send state `k` to a unit algebraic value `u`.

Then the two operations act as

\[
H:u\mapsto-u,
\qquad
S:u\mapsto u^{-1}.
\]

Use the standard even/odd component readouts

\[
c(u)=\frac{u+u^{-1}}2,
\]

and

\[
s(u)=\frac{u-u^{-1}}{2J},
\]

with `J^2=-1` in the Enterprise algebraic component carrier.

Their parity is:

| operation | `c` | `s` |
|---|---:|---:|
| `S` | even | odd |
| `H` | odd | odd |
| `HS` | odd | even |

Indeed:

\[
c(u^{-1})=c(u),
\qquad
s(u^{-1})=-s(u),
\]

while

\[
c(-u)=-c(u),
\qquad
s(-u)=-s(u).
\]

This table makes the two binary carriers operationally distinguishable away from the quarter-turn degeneracy.

## 8. Principal-root selection breaks H, not S

For a non-antipodal parent state, its two square roots are

\[
w,\qquad-w=H(w).
\]

The positive-longitudinal rule proved in the sibling note selects the member with

\[
c(w)>0.
\]

Since `H` flips `c`, this selection chooses one side of the `H` root pair.

By contrast, `S` leaves `c` unchanged. Therefore both chirality branches

\[
w,\qquad w^{-1}
\]

have the same longitudinal Viète factor.

Thus the scalar Viète architecture has the precise form:

```text
H-root pair: choose principal positive-longitudinal member
S-chirality pair: retain both for oriented theory, or quotient them for scalar theory
```

The two operations do completely different jobs.

## 9. Why the quarter-turn seed hid the distinction

At the half-turn parent `u=-1`, the two roots are

\[
J,\qquad-J.
\]

On this pair,

\[
H(J)=-J
\]

and

\[
S(J)=J^{-1}=-J.
\]

Hence the same two-state torsor simultaneously carries the root-deck swap and the chirality swap.

This degeneracy is unique to the quarter-turn orbit. One refinement later the orbit expands to four states and the two `C2` actions separate.

Therefore the earlier phrase “the Viète seed needs one binary bit” must be read only at the degenerate quarter-turn strength. It is not the correct state typing for the full deep oriented refinement tower.

## 10. Consequence for the C3 -> C6 holonomy question

The `C2` fiber whose nontrivial loop holonomy turns

\[
C_3\sqcup C_3
\]

into

\[
C_6
\]

is an `H`-typed direction/deck sheet.

Current native rotation `epsilon`, however, is a local sweep-orientation datum and is `S`-typed unless an additional theorem says otherwise.

Therefore the native gap is actually stronger than the parent note stated:

\[
\boxed{
\text{CURRENT SWEEP ORIENTATION DOES NOT BY ITSELF SUPPLY THE C6 DECK SHEET.}
}
\]

A valid native bridge must first identify or construct the `H` direction sheet, and only then ask for its loop holonomy/effectivity.

The existing native unoriented segment structure does contain two directed canonical traces, but current Foundation explicitly distinguishes canonical endpoint reversal from groupoid inversion. Hence that structure cannot silently be collapsed into the required `H` sheet either.

## 11. Revised native information hierarchy

The typed binary hierarchy for #1158 is now:

### Layer D — direction/deck sheet (`H`)

Needed to form the two-fold orientation-state cover and its half-turn deck transformation.

Current native source: **not yet canonically identified**.

### Layer S — sweep/chirality (`S`)

Needed only for a signed/oriented lift distinguishing the two turn senses.

Current native source: the rotating-segment state already carries a candidate local sweep variable `epsilon`, but its exact intertwiner with the G1 character `S` action remains a bridge theorem.

### Root selection

At every non-antipodal refinement, principal-root choice selects within the `H` pair by positive longitudinal readout.

### Scalar quotient

Scalar Viète observables are `S`-even, so the `S` pair may recoalesce after the oriented data has been correctly typed.

This is strictly richer than one undifferentiated “orientation bit”.

## 12. Correction to the matched-countermodel claim

The matched `H=0/H=1` cover models in the parent note remain exact countermodels for an **abstract local `C2^H` sheet extension** of the coarse `C3` state.

They should no longer be described as two models obtained by transporting the already-frozen sweep variable `epsilon` differently.

The corrected statement is:

> Even after granting the same local two-valued direction/deck sheet `beta`, all proper path restrictions are gauge equivalent while the full loop admits both trivial and nontrivial holonomy. Current local Cell data does not select the loop class. Separately, current sweep `epsilon` is a different typed `C2` carrier.

This correction strengthens the no-go by removing an unsupported identification.

## 13. Updated G0 frontier

Inside the cycle-cover route, full native promotion now requires the following typed bridges:

1. **DIRECTION-SHEET BRIDGE:** construct/identify a native `C2^H` direction/deck sheet over the coarse orientation quotient;
2. **HOLONOMY/EFFECTIVITY:** prove that its nontrivial loop class is the effective connected refinement;
3. **ALGEBRAIC ROOT CHART:** extend the native positive-sector semantics to the G1 algebraic orientation state so the principal `H` root is selected at deep irrational directions;
4. **SWEEP INTERTWINER** only if a signed oriented theory is required: map native sweep `epsilon` to the `S` action up to the unavoidable global chirality gauge.

For scalar Viète precision, item 4 may be quotiented away after correct typing. Items 1–3 remain the genuine native bridge obligations.

Current P000 does not yet supply these bridges uniquely.
