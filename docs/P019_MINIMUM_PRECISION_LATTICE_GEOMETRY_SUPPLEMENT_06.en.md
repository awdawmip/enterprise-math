# P019 Supplement 06 — Value Associativity and Witness Non-Associativity

Status: `RESEARCH WIP / COUNTEREXAMPLE PRESERVED`

## 1. Two different levels

Supplements 04/05 proved the min-plus block-energy law

\[
\Psi_{a+b,s}=\Psi_{a,s}\square\Psi_{b,s},
\]

so minimum value/energy is associative under block grouping.

This does not imply that exact witnesses obtained by repeated boundary lifting are grouping-independent.

## 2. Minimal counterexample

Take four original unit slots, `s=2`, threshold `T=16`, and contract all slots to one final block.

For the chain tree

\[
(((1+1)+1)+1),
\]

reverse lifting through the unique right-boundary witness in each chosen directed channel gives

\[
\boxed{(2,1,0,-3)}.
\]

For the balanced tree

\[
(1+1)+(1+1),
\]

the same rule gives

\[
\boxed{(2,2,-2,-2)}.
\]

These are not related by a simple coordinate permutation, nor by global sign followed by permutation.

Hence

\[
\boxed{
\text{value associativity}
\not\Rightarrow
\text{witness associativity}.
}
\]

## 3. Interface with P021

This matches the P021 safe-reduction rule for direction transport: aggregated cardinality/value can compose while exact middle-witness identity may still be required for future exact composition.

For P019 contraction:

- if future work needs only minimum energy, ball counts, or block capacity, the final block-size partition is sufficient;
- if future work needs exact boundary witness composition, directional history, causal paths, or local incidence, the contraction tree / witness relation cannot be deleted automatically.

Thus there are at least two precision layers:

`coarse contracted state = visible totals + block sizes`

`composition-complete contracted state = coarse state + contraction/witness trace`.

Safety rule:

> Collapse witness trace to a block-size/cardinality shadow only after proving that the future observable is insensitive to contraction history.

## 4. Next steps

1. Define a typed `ContractionTrace` separate from ordinary value state.
2. Classify observables that depend only on final partition versus those that depend on contraction tree.
3. Test whether witnesses from different trees can still belong to the same full graph-automorphism orbit; the four-slot example already rules out the simplest permutation/sign equivalence.
4. Reuse P021 witness-relation join semantics rather than creating a parallel composition system.
