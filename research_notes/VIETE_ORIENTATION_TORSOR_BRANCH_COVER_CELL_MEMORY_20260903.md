# Viète orientation torsor: two involutions, antipodal branch cover, and Cell-memory lower bound

Status: `FREE_RESEARCH / EXACT_G1_SYMMETRY_AND_BRANCH_THEOREMS + G0_MEMORY_NO-GO / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Predecessors:
- `research_notes/VIETE_SEGMENT_BISECTOR_ROTATION_PRECISION_20260903.md`
- `research_notes/VIETE_NATIVE_TRACE_ORIENTATION_QUOTIENT_OBSTRUCTION_20260903.md`

## 1. Frontier and correction

The predecessor established an exact normalized-bisector square-root mechanism at a rebuilt finite orientation-readout layer and showed that current G0 does not yet canonically derive it.

A second note correctly proved that current canonical endpoint reversal cannot simply be identified with character inversion. The next step is to sharpen why: two distinct involutions were being compared.

This note separates them and derives a branch-preserving route that removes the need for an arbitrary quarter-turn selector at scalar Viète strength.

## 2. Direction reversal and turn-sense reversal are different operations

Work in a finite cyclic orientation quotient after choosing a reference orientation `e`. Let `h` denote the unique half-turn element, so

\[
h^2=e,\qquad h\neq e.
\]

For a direction state `u`, distinguish:

1. **half-turn / directed-segment reversal**

\[
H(u)=hu;
\]

2. **turn-sense / chirality reversal relative to the reference**

\[
S(u)=u^{-1}.
\]

In a unit-pair readout `u=(c,s)`, these are represented by

\[
H(c,s)=(-c,-s),
\qquad
S(c,s)=(c,-s).
\]

Both are involutions and, because `h=h^{-1}` in an abelian cyclic quotient,

\[
HS=SH.
\]

But they are not the same operation. Exactly,

\[
H(u)=S(u)
\iff
hu=u^{-1}
\iff
u^2=h.
\]

Thus

\[
\boxed{H(u)=S(u)\text{ iff }u\text{ is a quarter-turn root of the half-turn}.}
\]

The two operations coincide only on the quarter-turn states. At the identity and half-turn they are maximally different:

\[
H(e)=h,\quad S(e)=e,
\]

\[
H(h)=e,\quad S(h)=h.
\]

This accidental coincidence at the Viète seed explains why endpoint reversal, character inversion, and chirality reversal can be conflated if their types are not frozen first.

Freeze:

`SEGMENT_HALF_TURN_REVERSAL != TURN_SENSE_INVERSION`.

## 3. C6 state resolution and dihedral symmetry are not the same 12-element object

The coarse oriented direction quotient proposed in the Euler candidate is

\[
C_3\times C_2\cong C_6,
\]

where the `C2` supplies the half-turn/opposite-direction augmentation of the three positive-ray classes. This is a six-state direction quotient, not a statement that six primitive native axes exist.

Adjoining the turn-sense involution `S:u\mapsto u^{-1}` as a symmetry operation produces the dihedral semidirect product

\[
\boxed{\operatorname{Dih}(C_6)=C_6\rtimes C_2},
\]

which has 12 symmetry operations and is nonabelian.

By contrast, the first dyadic direction-resolution refinement is

\[
\boxed{C_6\hookrightarrow C_{12}},
\]

where `C12` has twelve **direction states** and is abelian/cyclic.

Therefore

\[
\boxed{\operatorname{Dih}(C_6)\not\cong C_{12}}.
\]

The common cardinality 12 must not be used to identify symmetry enrichment with state-resolution refinement.

Freeze:

`SIX_GATE_SYMMETRY_ENRICHMENT != DYADIC_DIRECTION_REFINEMENT`.

## 4. Antipodal square-root selector no-go under turn-sense symmetry

Embed the coarse `C6` into the minimal cyclic refinement `C12`. Let `h` be the half-turn. Its square roots are exactly two quarter-turn states

\[
Q(h)=\{q_+,q_-\},
\qquad
q_- = q_+^{-1}.
\]

Turn-sense reversal fixes the half-turn,

\[
S(h)=h,
\]

but exchanges the two roots,

\[
S(q_+)=q_-,
\qquad
S(q_-)=q_+.
\]

Suppose there were a deterministic square-root selector `r` at the half-turn that were equivariant under `S`. Since `S(h)=h`, equivariance would require

\[
r(h)=r(S(h))=S(r(h)).
\]

But neither quarter-turn root is fixed by `S`. Contradiction.

Hence

\[
\boxed{\text{no deterministic }S\text{-equivariant quarter-turn selector exists from }h\text{ alone}.}
\]

A single oriented branch can be selected only by adding an `S`-odd chirality choice distinguishing `q_+` from `q_-`.

This is the group-theoretic form of the normalized-bisector singularity

\[
e+h=0.
\]

The obstruction is not numerical and does not involve the value of `pi`.

## 5. Branch preservation removes the arbitrary-choice problem at scalar Viète strength

The selector no-go does **not** imply that scalar Viète refinement must choose an arbitrary chirality.

Instead of choosing one root, retain the complete root relation

\[
\operatorname{Root}(h)=\{q_+,q_-\}.
\]

This is exactly invariant under `S`. It is a two-branch relation, not a two-valued instantaneous native state.

In the unit-pair readout write the two quarter-turn seeds as

\[
v_0^+=(0,1),
\qquad
v_0^-=(0,-1)=S(v_0^+).
\]

Apply the normalized-bisector refinement `B` separately to each branch. Since

\[
B(Sv)=S(Bv),
\]

induction gives

\[
v_n^- = S(v_n^+)
\]

for every depth `n`.

Write

\[
v_n^+=(c_n,s_n),\qquad s_n>0.
\]

Then

\[
v_n^-=(c_n,-s_n).
\]

Therefore the oriented refinement is an exact two-sheeted cover over the scalar Viète chain.

The longitudinal factors agree branchwise:

\[
\rho(v_n^+)=\rho(v_n^-)=c_n,
\qquad
\rho(c,s)=c.
\]

Likewise

\[
P_n=\prod_{k=1}^{n}c_k
\]

and

\[
\Pi_n=2^{n+1}|s_n|
\]

are identical on the two sheets.

Hence

\[
\boxed{\text{the scalar Viète precision sequence needs no chirality selector}.}
\]

What needs the chirality bit is a **single oriented lift** of the scalar sequence, not the scalar sequence itself.

This is a stronger resolution of the seed obstruction than selecting a preferred quarter-turn by hand.

Freeze:

`ORIENTED_VIETE_TOWER = TWO_SHEETED_S_COVER`.

`SCALAR_VIETE_TOWER = S_QUOTIENT_OF_ORIENTED_TOWER`.

## 6. General observer-factorization lemma

Let `S` be an involution, `B` an `S`-equivariant refinement,

\[
B\circ S=S\circ B,
\]

and `O` an `S`-invariant observer,

\[
O\circ S=O.
\]

Then for every state `x` and every `n>=0`,

\[
\boxed{O(B^n x)=O(B^n Sx)}.
\]

Proof is immediate from equivariance:

\[
B^nS=SB^n,
\]

followed by `O S=O`.

For Viète:

- `S(c,s)=(c,-s)`;
- `B` is normalized-bisector refinement;
- `O=c`, `O=|s|`, `O=P_n`, and `O=Pi_n` are `S`-invariant observers.

By contrast the signed transverse observer `s` is `S`-odd and does not descend.

This cleanly implements the project-wide signed-information boundary: scalar recoalescence is observer-relative and does not erase the existence of the oriented two-sheeted cover.

## 7. Parity statement corrected

The parity result in the Viète precision note is parity under **turn-sense reversal** `S`, not under directed-segment half-turn reversal `H`.

Thus:

\[
c_n\circ S=c_n
\]

is even,

\[
s_n\circ S=-s_n
\]

is odd, and the scalar precision defect is `S`-even/quadratic.

No corresponding claim is made automatically for current native endpoint exchange.

If a future native direction quotient maps canonical endpoint exchange to a half-turn action, its correct target intertwiner is of the form

\[
\chi(\operatorname{EndpointSwap}(T))
=
H(\chi(T)),
\]

not

\[
\chi(\operatorname{EndpointSwap}(T))
=
S(\chi(T)).
\]

The predecessor obstruction remains valid as a proof that the stronger endpoint-swap-to-inversion identification is not available. It is no longer a required target semantics.

## 8. Exact Cell-only local trajectory-orientation no-go

Current native line theory gives an exact commuting-diamond witness in a sector. For the trace

\[
T_{1,1}^{(ij)},
\]

two distinct path representatives are

\[
p=\Sigma_O^{(ij)};X_iX_j,
\qquad
q=\Sigma_O^{(ij)};X_jX_i.
\]

They terminate in the same native Cell

\[
C_{ij}(1,1),
\]

but their incoming primitive transition labels differ:

\[
\operatorname{last}(p)=X_j,
\qquad
\operatorname{last}(q)=X_i.
\]

Suppose a proposed local **trajectory-direction** quotient `theta` were a function of the instantaneous Cell alone and were required to distinguish the incoming primitive ray class. Then the common terminal Cell would have to satisfy simultaneously

\[
\theta(C_{ij}(1,1))=[X_j]
\]

and

\[
\theta(C_{ij}(1,1))=[X_i],
\]

which is impossible for `i!=j`.

Therefore

\[
\boxed{\text{any transition-sensitive local trajectory orientation cannot factor through bare Cell state alone}.}
\]

At least one incoming-transition/history distinction is necessary. The exact witness supplies a lower bound of one binary distinction even inside one two-axis sector.

This theorem is deliberately about **trajectory transition orientation**. It does not assert that the physical orientation of a rotating segment must equal the last path letter. A segment-orientation quotient may instead carry a separate trace/frame state; if so, that state must be declared explicitly rather than inferred from the Cell label.

Freeze:

`BARE_CELL_STATE_INSUFFICIENT_FOR_TRANSITION_SENSITIVE_ORIENTATION_QUOTIENT`.

## 9. Revised minimum native bridge obligations for #1158

The previous bridge checklist can now be narrowed and corrected.

A native-strength Viète bridge would need:

1. `DOMAIN` — specify whether the mapped object is a trajectory transition germ, an oriented trace/segment state, or another explicitly typed native state; a bare Cell is insufficient for transition-sensitive orientation;
2. `COARSE_QUOTIENT` — construct an operation-safe finite direction quotient whose current candidate shape is `C6` only at G1/readout strength;
3. `INVOLUTIONS` — keep half-turn direction reversal `H` separate from turn-sense inversion `S`; if endpoint exchange is mapped, prove the correct `H` intertwiner rather than assuming inversion;
4. `ANTIPODAL_BRANCH_RELATION` — derive a native pair of quarter-turn branches, not necessarily a canonical selector;
5. `REFINEMENT` — prove that branchwise native refinement descends to the normalized-bisector `B` law or an equivalent exact law;
6. `OBSERVER` — prove that the scalar precision observer is `S`-invariant so the two oriented branches recoalesce only at the declared scalar readout.

The crucial improvement is item 4: **scalar Viète does not require a preferred chirality branch.** It can retain both legitimate branches and quotient only at an even observer, matching the current project rule that branching trajectories remain single-valued individually rather than becoming one multivalued instantaneous state.

## 10. Current strength boundary

This note proves exact finite G1 symmetry/refinement facts and an exact G0 Cell-memory lower bound from current line semantics.

It does not prove:

- that the current native Cell dynamics supplies a canonical `C6` quotient;
- that a native half-turn event realizes both quarter-turn branches;
- that normalized-bisector refinement is the actual native Cell transition law;
- that canonical endpoint swap already satisfies the proposed half-turn intertwiner;
- that the three-axis slice result has a proved six-dimensional native lift.

Accepted Q29 remains relevant: current P000 does not select a unique native finite 6D rotation law at its declared finite comparison scope. Therefore the bridge above is a minimal research specification, not a Foundation promotion.

## 11. New decisive frontier

The remaining high-leverage question for #1158 is no longer “which quarter-turn branch is canonical?”

It is:

\[
\boxed{\text{Can native Cell/trace dynamics realize an }S\text{-paired antipodal branch relation and an }S\text{-equivariant refinement whose scalar quotient is }B?}
\]

A positive answer would derive the scalar Viète mechanism without an arbitrary orientation choice. A negative answer would isolate exactly which additional native frame/chirality structure is required.
