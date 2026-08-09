# P019 Supplement 18 — Quotient-Compatible Dynamics and the Hidden-to-Coarse Feedback Boundary

Status: `RESEARCH WIP / FINITE QUOTIENT CRITERION PROVED`

## 1. Necessary strengthening of Supplement 17

Supplement 17 proves that deleted internal `Z` relations may be erased permanently when every future program is only a further partition coarsening. But "never refine" is not sufficient for arbitrary dynamics: a fine operation may read a hidden relation and feed that distinction back into visible coarse totals or relations.

The correct condition is compatibility of every future operation with the quotient.

## 2. Quotient-compatible transition

Let `Q:X->Y` be a finite-state quotient and `T:X->X` a deterministic operation. Call `T` **Q-compatible** when

\[
\boxed{Q(x)=Q(y)\Longrightarrow Q(Tx)=Q(Ty).}
\]

Equivalently, there exists a unique coarse transition `bar T` on `Q(X)` such that

\[
\boxed{Q\circ T=\bar T\circ Q.}
\]

This is exact finite function factorization; no continuous structure is involved.

## 3. P019-X58 — If every generator descends, arbitrarily long futures are safe

Let the allowed operation family be `{T_a}`. If every generator is Q-compatible and observation also factors as `O=bar O\circ Q`, then every finite operation word `w` satisfies

\[
\boxed{Q(T_wx)=\bar T_w(Q(x)).}
\]

Therefore equal quotient states remain observationally indistinguishable under every finite allowed future program. The proof is finite induction on word length.

Thus `Q` is future-safe for the declared operation/observation language.

## 4. P019-X59 — Hidden-to-coarse feedback is the minimal failure mechanism

If there exist `x,y` with equal quotient but

\[
Q(Tx)\ne Q(Ty),
\]

then `T` reads a distinction erased by the quotient and feeds it back into the visible coarse layer. One future step already distinguishes the two fine states.

This is the precise failure pattern

\[
\boxed{
\text{hidden distinction}
\to
\text{operation-dependent branch}
\to
\text{different coarse successor}.
}
\]

## 5. Weighted-relation examples

- Internal redistribution that preserves a coarse block total descends to the identity quotient operation.
- Any block dynamics whose coarse effect is determined entirely by current capacities, coarse totals, and the weighted relation field descends directly.
- A rule that first tests a deleted internal `Z_ij` and then conditionally transfers one unit to another coarse block does not descend in general, even when refinement is never allowed.

## 6. Relation to coarsening-only safety

Partition coarsening already satisfies

\[
Q_\Sigma=Q_{\Sigma/\Pi}\circ Q_\Pi,
\]

so Supplement 17 is an important special case of X58 in which every future generator visibly factors through the current quotient.

## 7. P019-X60 — Replace "forward-only" by "quotient-closed future language"

The sharper notion is a **quotient-closed future language**:

1. observations read only the quotient;
2. every future operation descends to the quotient;
3. compositions close on the quotient state space.

For such a language, every distinction erased by the quotient can be discarded permanently.

The arrow of time alone is not the guarantee; closure of future dynamics on the quotient is.

## 8. Interface with P021 and P018

P021's witness rule can be restated in the same language: a witness-cardinality quotient is safe only when future witness joins descend to it. P018 precision projections can use the same test: a coarse precision state is exact for a task exactly when the allowed operation family factors through that precision quotient; otherwise refinement or bounded detail is required.

## 9. Implementation

`src/enterprise_math/future_quotient.py` adds `descended_transition`, `transition_descends_to_partition`, and `operation_family_descends`. Tests include a detail-blind operation that descends, a hidden-feedback operation that does not, and a family-level check requiring every generator to descend.

## 10. Prior-art boundary

Congruence quotients, bisimulation, lumpability, and automata minimization contain established versions of operation-respecting equivalence. P019 makes no general originality claim for the factorization principle. The project-specific use is as one safety gate for weighted relation deletion, precision detail, contraction history, and P021 witness transport.
