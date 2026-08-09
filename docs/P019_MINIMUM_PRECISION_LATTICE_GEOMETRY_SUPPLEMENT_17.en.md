# P019 Supplement 17 — Permanent Safe Erasure of Internal Relations under One-Way Coarsening

Status: `RESEARCH WIP / EXACT FUTURE-SAFETY THEOREM PROVED`

## 1. Problem

Supplement 08 defines a future-safe quotient: two fine states may be merged only when no allowed future program can ever distinguish them.

Supplements 15/16 identify one internal weighted relation `Z_ij` deleted by each block merge.

We can now answer a nontrivial concrete question:

> If the future is allowed only to keep contracting/coarsening, must an already deleted `Z_ij` be retained?

No.

## 2. One-way coarsening future language

Fix a current partition `Pi`. Allowed future operations are only further coarsenings

\[
\Pi\preceq\Sigma_1\preceq\Sigma_2\preceq\cdots,
\]

with no split/refinement.

Allowed observations read only future coarse block capacities, totals, weighted relation fields, and deterministic quantities derived from those coarse states. Deleted fine internal witness identity is not itself observed.

## 3. P019-X55 — The current weighted quotient is future-safe for coarsening-only programs

Suppose fine states `x,y` have the same weighted quotient at the current partition:

\[
Q_\Pi(x)=Q_\Pi(y).
\]

Then for every future coarser partition

\[
\Sigma\succeq\Pi,
\]

\[
\boxed{Q_\Sigma(x)=Q_\Sigma(y).}
\]

Proof: Supplement 16 X50 gives

\[
Q_\Sigma=Q_{\Sigma/\Pi}\circ Q_\Pi.
\]

Equal current quotients therefore remain equal after every further quotient. ∎

Thus the current weighted quotient is already future-safe for this operation language.

## 4. P019-X56 — Deleted internal relations are permanently unobservable under pure forward coarsening

If a merge combines blocks `i,j` and deletes

\[
z=Z_{ij},
\]

all future partition quotients see only merged capacity `m_i+m_j`, merged total `c_i+c_j`, and summed external relations `Z_ik+Z_jk`.

The internal `Z_ij` never reappears in a future cross-block cut sum.

Hence

\[
\boxed{
\text{under a coarsening-only future language, deleted internal }Z
\text{ may be erased permanently.}
}
\]

Neither a complete oriented contraction flag nor the `z` history is required.

## 5. This is exact erasure, not approximation

The safety statement is not that the deleted relation has small influence or is statistically negligible. It is the exact future-equivalence statement

\[
\boxed{
\forall\text{ future coarsening programs},
\quad O(T_w(x))=O(T_w(y)).
}
\]

This is a complete proved instance of Supplement 08 future equivalence.

## 6. P019-X57 — Allowing refinement can destroy safety immediately

Take three unit blocks and fine states

\[
(1,-1,0)
\]

and

\[
(2,-2,0).
\]

Merge the first two units. Both produce capacities `(2,1)`, coarse totals `(0,0)`, and the same coarse weighted relation field. But their deleted internal relations are

\[
Z_{12}=2
\]

and

\[
Z_{12}=4.
\]

If a future refinement splits the capacity-two block back into two units, the distinction is immediately observable.

Therefore

\[
\boxed{
\text{coarsening-safe}
\not\Rightarrow
\text{refinement-safe}.
}
\]

## 7. Operation-family-dependent minimum relation memory

There is no task-independent smallest history.

### A. Pure forward coarsening

A sufficient current state is

\[
\boxed{
\text{current partition capacities}
+
\text{current weighted relation quotient}
+
\text{grand total}.
}
\]

All previously deleted internal `Z` values can be discarded.

### B. Exact refinement allowed

If a coarse block may later be split exactly, enough detail must be retained to recover its internal relation fiber. For a two-child split, one internal `Z` is a complete child-total fiber coordinate.

### C. Selected boundary lift allowed

The fiber endpoint must be retained or reconstructed; Supplement 09's fiber-root `(z,rho)` detail is a candidate.

### D. Actual process history queried

Even if the present fine state is reconstructible from a smaller relation object, the actual temporal order may still require a historical witness. Provenance is not the same thing as current geometry.

## 8. Relation to irreversibility

Mathematically, a forward merge that discards `Z` is many-to-one and the fine split is not uniquely recoverable. If the future language only coarsens, however, that irreversibility is completely safe for future coarse dynamics.

Thus

> **irreversibility is not automatically an error; the key question is whether the deleted distinction still belongs to the allowed future mathematical/physical language.**

This is compatible with P010/P011 history-fiber language, but it does not establish that physical ontology itself discards these relations.

## 9. Unification with P021 witness composition

P021's safety rule is that witness identity may be reduced to a cardinality/coarse shadow only after proving that it cannot affect future composition.

P019 now has the relation analogue: a deleted internal relation may be permanently erased only after proving that it cannot affect future allowed partition programs.

For coarsening-only programs, X55 supplies the proof. For languages with refinement or directional lifting, a finer state is required.

Both are instances of

\[
\boxed{
\text{safe collapse}
=
\text{quotient by future operational indistinguishability}.
}
\]

## 10. A concrete precision interpretation

In this geometric model, refinement can be read as re-enabling access to internal relations previously hidden inside coarse partition blocks.

- coarse precision: observe only block-to-block weighted relations;
- finer precision: split selected blocks and expose new internal `Z` relations;
- singleton precision: every original unit slot is individually distinguishable.

This is compatible with the project's precision-first worldview, but this supplement does not modify the protected worldview file.

## 11. Implementation and counterexample regression

Added `tests/test_relation_erasure.py`, checking that fine states with different deleted internal relations remain identical under several subsequent partition coarsenings once their current weighted quotients agree, while refinement immediately reveals the hidden relation in the minimal counterexample.

## 12. Next steps

1. extend X55 to coarsening plus selected block-local dynamics and classify which dynamics still ignore deleted `Z`;
2. for languages allowing refinement, find the minimum relation-memory set instead of retaining all history by default;
3. use Supplement 08 partition refinement to compute automatically which deleted-`Z` classes can be safely quotiented for a declared operation family;
4. define a relation-level future language for P021 direction transport and test how much deleted-`Z` memory supports exact witness joins;
5. connect `precision refinement = re-expose internal relations` formally to P018.
