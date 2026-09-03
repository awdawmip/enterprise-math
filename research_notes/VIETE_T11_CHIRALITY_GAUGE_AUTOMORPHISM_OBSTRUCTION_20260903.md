# Viète T11 chirality: automorphism obstruction to an absolute sign and the canonical C2-torsor alternative

Status: `FREE_RESEARCH / EXACT CURRENT-STRUCTURE CANONICALITY NO-GO / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Issue: `#1158`
Parent: `research_notes/VIETE_SCALAR_ORIENTED_NATIVE_STATE_MINIMALITY_20260903.md`

## 1. Reduced native seed structure

For the native equal-component trace

\[
T:=T_{1,1}^{(ij)},
\]

current line semantics gives exactly two path representatives

\[
F=\{p,q\},
\qquad
p=\Sigma;X_iX_j,
\qquad
q=\Sigma;X_jX_i.
\]

Both have the same currently frozen trace-level and endpoint observables:

- same native trace identity `T`;
- same component multiset `{X_i,X_j}`;
- same terminal Cell `C_ij(1,1)`;
- same native length `sqrt(2)`;
- same scalar normalized component readout `(1,1)/sqrt(2)`.

Define the order-swap permutation

\[
\tau(p)=q,
\qquad
\tau(q)=p.
\]

Relative to the reduced structure above, `tau` preserves every declared observable. It is therefore an automorphism of that reduced seed structure.

## 2. Absolute chirality cannot be canonical from the reduced structure

Suppose one tries to define an **absolute** sign label

\[
\epsilon:F\to\{+1,-1\}
\]

from the reduced native structure alone, with the target sign set carrying no compensating action.

Canonicity under automorphisms requires

\[
\epsilon(\tau x)=\epsilon(x).
\]

But `tau` is transitive on `F`, so this forces

\[
\epsilon(p)=\epsilon(q).
\]

Hence no automorphism-invariant absolute sign can distinguish the two paths.

Therefore

\[
\boxed{
\text{current reduced }T_{1,1}\text{ structure does not canonically determine an absolute }+/-\text{ chirality label.}
}
\]

Any rule that names `p` positive and `q` negative must use some additional structure not contained in the reduced trace/endpoint/length data.

## 3. The obstruction is to labeling, not to the two-branch carrier

The path fiber itself is already a free `C2` torsor under `tau`.

The quarter-turn root pair

\[
Q(h)=\{q_+,q_-\}
\]

is another free `C2` torsor under turn-sense reversal `S`.

A torsor isomorphism

\[
\phi:F\to Q(h)
\]

is required only to satisfy

\[
\phi(\tau x)=S\phi(x).
\]

Exactly two such isomorphisms exist. They differ by the global `C2` action:

\[
\phi' = S\circ\phi.
\]

Thus the current structure canonically supports a **relative two-sheeted orientation carrier up to global sign gauge**, even though it cannot select an absolute sign convention.

Freeze:

`T11_RELATIVE_CHIRALITY_TORSOR = STRUCTURALLY_AVAILABLE`.

`T11_ABSOLUTE_CHIRALITY_SIGN = REQUIRES_EXTRA_GAUGE_FIXING_DATA`.

## 4. Gauge-invariant observers descend without any sign fixing

Let `O` be an observer on the quarter-root torsor satisfying

\[
O(Sy)=O(y).
\]

For the two admissible torsor identifications `phi` and `phi'=S phi`,

\[
O(\phi'(x))
=O(S\phi(x))
=O(\phi(x)).
\]

Hence every `S`-invariant observer is independent of the global chirality gauge.

The scalar Viète observables have exactly this property:

- longitudinal half-angle factor;
- absolute transverse residual;
- scalar product factor;
- scalar finite `Pi_n`;
- target-free completion interval.

Therefore the scalar #1158 program does not need an absolute chirality gauge fixing at the seed.

## 5. Odd observers expose the missing gauge

A signed transverse observer satisfies

\[
O_{\rm odd}(Sy)=-O_{\rm odd}(y).
\]

Then the two torsor identifications give opposite values. Thus a signed oriented lift requires a choice of global chirality gauge, or additional native structure that fixes one.

This cleanly separates:

\[
\boxed{
\text{gauge-invariant scalar precision}
\quad\text{from}\quad
\text{gauge-dependent signed orientation}.}
\]

The distinction matches the project-wide rule that signed/orientation information must not be silently erased and that a positive/scalar recoalescence is observer-relative.

## 6. Relation to the previous one-bit statement

The parent proved that one binary distinction beyond trace identity is necessary and sufficient to retain the two oriented sheets structurally.

This note sharpens the interpretation:

- the existing path representative already supplies the binary **relative branch distinction**;
- no new binary state is needed merely to keep both sheets;
- what is not supplied is an **absolute sign label** on that distinction;
- choosing such a label is a global `C2` gauge fixing unless later native physics/geometry breaks the symmetry.

Thus the more precise statement is not “Viète needs one new chirality bit.” It is:

\[
\boxed{
\text{oriented Viète needs one retained two-branch distinction; current }T_{1,1}\text{ already has it, but its absolute sign is gauge.}
}
\]

## 7. Canonicality test for any future proposed native chirality rule

Any future rule claiming to derive an absolute chirality directly from the current `T_11` seed must identify a native datum `D` such that

\[
D(p)\neq D(q)
\]

and such that `D` is not merely a chosen carrier drawing convention.

If every admitted native datum remains invariant under `tau`, the automorphism obstruction above kills the proposed absolute rule.

Possible legitimate symmetry-breaking data, if later derived, could include an explicitly typed incoming frame, time-ordered rotational memory, or a native transport orientation. None is supplied by the current reduced `T_11` trace semantics merely from endpoint and length.

## 8. Current #1158 consequence

The seed problem is now largely closed at information-structure strength:

1. exact scalar first half-angle: native `T_11` trace;
2. exact two-sheet carrier: native `T_11` path fiber;
3. absolute sheet sign: not canonically selected by current reduced structure;
4. scalar Viète observers: gauge-independent;
5. signed oriented observers: require gauge fixing or additional native odd data.

The remaining native bridge question is no longer about inventing a missing branch bit. It is whether actual Cell/trace rotation dynamics supplies a physically meaningful intertwiner between path-order transport and the orientation torsor, and whether it ever canonically fixes the global chirality gauge.
