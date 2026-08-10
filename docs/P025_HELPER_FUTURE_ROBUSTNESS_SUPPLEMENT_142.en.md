# P025 Supplement 142 — Helper validity is relative to the future operation envelope

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-helper-cache-stage139`

## 1. Current correctness versus future robustness

A stale helper need not corrupt the **current** raw endpoint immediately.  Its danger depends on which raw operations are still allowed in the future.

For the sequential k-way compiler, helper `e_j` semantically certifies the raw prefix

\[
P_j=\{a_1,\ldots,a_j\}.
\]

Call an internal state **prefix-valid** when every present helper satisfies

\[
\boxed{e_j\in T\Rightarrow P_j\subseteq\pi(T).}
\]

## 2. A stale state can be currently harmless

In the four-way compiler, take

\[
T=\{e_2\}.
\]

This helper is stale because `a_1,a_2` are absent.  Nevertheless the current saturation cannot reach `z` because `a_3,a_4` are also absent. Hence the current raw projection remains correct.

Now allow the future raw operation that adds

\[
\{a_3,a_4\}.
\]

The stale `e_2` bypasses the missing prefix, generates `e_3`, then generates `z`. The pure raw conjunction still lacks `a_1,a_2`, so this future is incorrect.

Thus

\[
\boxed{
\text{current endpoint safety}\not\Rightarrow\text{future robustness}.
}
\]

## 3. Exact robustness theorem

Assume `z` is not already present in the raw projection.  Then an internal sequential-helper state preserves the pure raw closure under **every future monotone addition of raw antecedents** iff it is prefix-valid:

\[
\boxed{
\text{robust under all raw additions}
\iff
\forall j,\ e_j\Rightarrow(a_1\wedge\cdots\wedge a_j).
}
\]

### Sufficiency

If every retained helper certifies its full raw prefix, the same property is preserved by every internal rule:

\[
e_{j-1}a_j\Rightarrow e_j.
\]

Therefore deriving `z` implies that all raw antecedents are present, exactly matching the pure raw closure.

### Necessity

If some `e_j` is present while a prefix antecedent is missing, add all missing **suffix** antecedents `a_(j+1),...,a_k` in the future while leaving the missing prefix absent. The helper chain then reaches `z`, although the pure raw conjunction remains false. Hence the state is not robust.

If raw `z` is already present, helper staleness is invisible to this particular raw-output future because no helper rule can add any further raw label. Thus the complete condition is

\[
\boxed{
z\in\pi(T)\quad\text{or}\quad\text{prefix-validity}.}
\]

## 4. Legality is operation-language-relative

The same internal state can therefore be

- legal for the future language `read current raw endpoint only`;
- illegal for the richer language `permit arbitrary future raw antecedent additions, then read endpoint`.

So legality is not merely a property of a state representation. It is a compatibility relation between

\[
\boxed{
\text{internal state}
\times
\text{allowed future operations}
\times
\text{declared observables}.
}
\]

## 5. Architectural consequence

Stage 138's admissible-state invariant must itself be indexed by the future operation envelope.  Strengthening the future can require strengthening the hidden-state validity invariant even when neither the raw observable nor the internal coordinate set changes.

This is a hidden-state analogue of P023/P024 future-compatible quotient logic.

## 6. Prior-art boundary

Cache validity predicates, inductive invariants and robust safety under input extensions are classical verification ideas. No generic novelty claim is made. P025 contributes the exact iff boundary and the counterexample showing that `currently harmless` is weaker than `safe for the declared future`.
