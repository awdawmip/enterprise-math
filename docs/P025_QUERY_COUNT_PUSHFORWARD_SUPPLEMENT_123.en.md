# P025 Supplement 123 — Task-Relative Witness-Count Pushforward

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-witness-count-stage121`  
Depends on: P025 Supplements 115, 121–122  
Hard block: `NONE`

## 1. Full ambient inversion is not automatically licensed

Supplement 121 shows that a full ideal-count table on `J(P)` recovers the ambient witness multiplicity function exactly. But a declared future may inspect only labels in a queried subposet

\[
Q\subseteq P.
\]

Such a future should not recover ambient distinctions that disappear under restriction to \(Q\).

## 2. P025-D48 — multiplicity pushforward

Let

\[
w:J(P)\to\mathbf N
\]

be ambient witness multiplicity. For every query ideal \(K\in J(Q)\), define the pushforward multiplicity

\[
\boxed{
\bar w_Q(K)
:=
\sum_{I\in J(P):\ I\cap Q=K}w(I).
}
\]

This groups together all ambient exact witnesses with the same declared-query state.

Total multiplicity is conserved:

\[
\boxed{
\sum_{I\in J(P)}w(I)
=
\sum_{K\in J(Q)}\bar w_Q(K).
}
\]

## 3. P025-T271 — query counts are the zeta transform of the pushforward

Let \(S\subseteq Q\) be a raw query. Then

\[
\begin{aligned}
c_P(S)
&=\sum_{I\supseteq S}w(I)\\
&=\sum_{K\in J(Q):\ K\supseteq S}\bar w_Q(K).
\end{aligned}
\]

After normalizing \(S\) to its induced-query ideal / maximal-antichain form, this is exactly the upper zeta transform on `J(Q)`.

Therefore

\[
\boxed{
\text{all essential }Q\text{-count queries}
\Longleftrightarrow
\bar w_Q.
}
\]

Möbius inversion reconstructs the **projected multiplicity distribution**, not the ambient multiplicity state.

## 4. Exact ambient collision

Take the two-element antichain

\[
P=\{a,b\},
\qquad Q=\{a\}.
\]

Compare two exact witness assignments:

- one witness at \(\{a\}\);
- one witness at \(\{a,b\}\).

They are different ambient states, but both restrict to the same query ideal \(\{a\}\). Hence

\[
\boxed{
\bar w_Q^{(1)}=\bar w_Q^{(2)}
}
\]

and every possible count query using only \(a\) agrees.

Thus count observables do not override declared-future visibility.

## 5. P025-T272 — task-relative count horizon

The full projected multiplicity \(\bar w_Q\) is recovered once count queries cover every ideal boundary of the induced query poset. Therefore the exact recovery horizon is

\[
\boxed{
\operatorname{width}(Q),
}
\]

not \(\operatorname{width}(P)\).

Worst-case sharpness follows already by taking `P=Q` to be an antichain and applying the even/odd construction of Supplement 122.

So task restriction changes both:

1. **what state is recoverable** — ambient `w` versus projected `bar w_Q`;
2. **how much essential query arity is required** — ambient width versus query width.

## 6. Chain query inside a branching ambient poset

In the diamond

\[
a<b<d,
\qquad a<c<d,
\qquad b\parallel c,
\]

full ambient width is two. But for

\[
Q=\{a,d\},
\]

the induced query poset is a chain of width one.

Singleton query counts plus the empty total count already recover the complete multiplicity distribution over the three query ideals

\[
\varnothing,
\{a\},
\{a,d\}.
\]

They still do not identify how the multiplicity at query state \(\{a\}\) is distributed between ambient branches \(b\) and \(c\).

## 7. Architectural consequence

Task-relative precision has two distinct quotient operations:

\[
\boxed{
\text{ambient exact state}
\xrightarrow{\text{query restriction}}
\text{projected state}
\xrightarrow{\text{chosen observable}}
\text{count response}.
}
\]

A strong observable can invert the second map without inverting the first.

Therefore

\[
\boxed{
\text{observable invertibility}
\neq
\text{ambient-state recoverability}.
}
\]

This is a useful boundary for A2/A4 future-signature language.

## 8. Prior-art discipline

Pushforwards of measures/counts, induced-subposet restriction and Möbius inversion are classical. No generic novelty claim is made.

The project-side result is the exact task-relative placement and counterexample inside the P025 precision hierarchy. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 9. Executable assets

Added:

- `src/enterprise_math/poset_query_count_pushforward.py`;
- `tests/test_poset_query_count_pushforward.py`.

The executable layer verifies pushforward conservation, zeta inversion on the query ideal lattice, ambient collisions with identical query multiplicity, width-one recovery inside a branching ambient poset, and identity recovery when `Q=P`.

## 10. Next frontier

Counts strictly refine existential support even when the support family itself is fixed. Stage 124 should make this value-precision layer explicit: MAY/MUST is obtained by thresholding counts at `0` and at the total count, while exact integer counts retain witness multiplicity that those truth values discard.
